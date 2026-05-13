#!/usr/bin/env python3
"""Formula-vs-calibration ablation for the Phase 2 basin-flip claim.

This script reproduces the paper's reported comparison and adds the two
controls requested in paper §3.7:

1. LF: legacy fleet-wide production coherence stored in core.agent_state.
2. GF: grounded manifold formula with one fleet-wide healthy point/radius.
3. GC: grounded manifold formula with frozen Phase 2 class constants.
4. LC: artificial legacy tanh(V) control with per-class V scale.

The raw production database is not publishable; this script is the local
verification harness for the private production DB.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import psycopg2
import psycopg2.extras

KNOWN_RESIDENT_LABELS = {"Lumen", "Vigil", "Sentinel", "Watcher", "Steward", "Chronicler"}
HEALTHY_REGIMES = {"nominal", "STABLE", "CONVERGENCE", "EXPLORATION"}

# Frozen Phase 2 constants from unitares/config/governance_config.py.
# These are historical provenance constants, not current-date placeholders.
FROZEN_DELTA_NORM_MAX_BY_CLASS: Dict[str, float] = {
    "Lumen": 0.1187,
    "default": 0.2018,
    "Sentinel": 0.1702,
    "Vigil": 0.1705,
    "Watcher": 0.3948,
    "Steward": 0.2018,
    "Chronicler": 0.2018,
    "engaged_ephemeral": 0.2018,
}

FROZEN_HEALTHY_POINT_BY_CLASS: Dict[str, Tuple[float, float, float]] = {
    "Lumen": (0.7454, 0.8001, 0.1678),
    "default": (0.7264, 0.7934, 0.2364),
    "Sentinel": (0.7506, 0.7981, 0.1934),
    "Vigil": (0.7371, 0.7896, 0.2404),
    "Watcher": (0.7482, 0.7686, 0.2477),
    "Steward": (0.7264, 0.7934, 0.2364),
    "Chronicler": (0.7264, 0.7934, 0.2364),
    "engaged_ephemeral": (0.7264, 0.7934, 0.2364),
}

FROZEN_FLEET_HEALTHY_POINT = (0.6, 0.7, 0.0)
FROZEN_FLEET_DELTA_NORM_MAX = 1.8


@dataclass(frozen=True)
class StateRow:
    """One production state row needed for the ablation."""

    agent_class: str
    regime: Optional[str]
    e: float
    i: float
    s: float
    v: float
    risk: float
    stored_coherence: float

    @property
    def healthy(self) -> bool:
        """Whether this row belongs to the calibration healthy slice."""
        return self.regime in HEALTHY_REGIMES


@dataclass(frozen=True)
class Calibration:
    """Fleet and class calibration constants measured from the row window."""

    fleet_mu: Tuple[float, float, float]
    fleet_delta95: float
    fleet_v_abs95: float
    class_mu: Mapping[str, Tuple[float, float, float]]
    class_delta95: Mapping[str, float]
    class_v_abs95: Mapping[str, float]
    class_healthy_n: Mapping[str, int]
    healthy_n: int


def parse_jsonish(value: Any) -> Any:
    """Parse JSONB values that may arrive as strings from psycopg2."""
    if value is None:
        return {}
    if isinstance(value, str):
        try:
            return json.loads(value)
        except (TypeError, ValueError):
            return {}
    return value


def classify_from_db_row(label: Optional[str], tags: Sequence[str]) -> str:
    """Mirror the UNITARES class-indicator logic for DB-row inputs."""
    if label and label in KNOWN_RESIDENT_LABELS:
        return label
    tags_set = set(tags or [])
    if "embodied" in tags_set:
        return "embodied"
    if "ephemeral" in tags_set:
        return "ephemeral"
    if "persistent" in tags_set and "autonomous" in tags_set:
        return "resident_persistent"
    return "default"


def percentile(values: Sequence[float], p: float) -> float:
    """Linear-interpolation percentile for a finite numeric sequence."""
    if not values:
        return 0.0
    ordered = sorted(values)
    k = (len(ordered) - 1) * (p / 100.0)
    floor_i = math.floor(k)
    ceil_i = math.ceil(k)
    if floor_i == ceil_i:
        return ordered[int(k)]
    return ordered[floor_i] * (ceil_i - k) + ordered[ceil_i] * (k - floor_i)


def median(values: Sequence[float]) -> float:
    """Median with an explicit empty-sequence guard."""
    return statistics.median(values) if values else 0.0


def classify_basin(e: float, i: float, s: float, v: float, coherence: float, risk: float) -> str:
    """Mirror config.governance_config.classify_basin at measurement time."""
    if i < 0.5 or coherence < 0.40 or abs(v) > 0.30 or risk >= 0.70:
        return "low"
    if e >= 0.6 and i >= 0.7 and s <= 0.25 and abs(v) <= 0.15 and coherence >= 0.45 and risk <= 0.45:
        return "high"
    return "boundary"


def fetch_rows(db_url: str, start: str, end: str) -> List[StateRow]:
    """Load the production state rows for a half-open timestamp interval."""
    sql = """
        SELECT
          i.metadata->>'label'                AS label,
          COALESCE(i.metadata->'tags', '[]')  AS tags,
          s.regime                            AS regime,
          s.entropy                           AS entropy,
          s.integrity                         AS integrity,
          s.volatility                        AS volatility,
          s.coherence                         AS coherence,
          s.state_json                        AS state_json
        FROM core.agent_state s
        JOIN core.identities i USING (identity_id)
        WHERE s.recorded_at >= %s::timestamptz
          AND s.recorded_at <  %s::timestamptz
          AND s.state_json ? 'E'
        ORDER BY s.recorded_at, s.state_id
    """
    conn = psycopg2.connect(db_url)
    rows: List[StateRow] = []
    with conn, conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(sql, (start, end))
        for raw in cur:
            tags = parse_jsonish(raw["tags"])
            if not isinstance(tags, list):
                tags = []
            state_json = parse_jsonish(raw["state_json"])
            try:
                e = float(state_json["E"])
                i_val = float(raw["integrity"])
                s_val = float(raw["entropy"])
                v_val = float(raw["volatility"])
                risk = float(state_json.get("risk_score", 0.0) or 0.0)
                stored_coherence = float(raw["coherence"])
            except (KeyError, TypeError, ValueError):
                continue
            if not (0.0 <= e <= 1.0 and 0.0 <= i_val <= 1.0 and 0.0 <= s_val <= 1.0):
                continue
            rows.append(
                StateRow(
                    agent_class=classify_from_db_row(raw["label"], tags),
                    regime=raw["regime"],
                    e=e,
                    i=i_val,
                    s=s_val,
                    v=v_val,
                    risk=risk,
                    stored_coherence=stored_coherence,
                )
            )
    return rows


def measure_calibration(rows: Iterable[StateRow], n_min: int) -> Calibration:
    """Measure fleet-wide and class-conditional constants on the healthy slice."""
    healthy = [row for row in rows if row.healthy]
    fleet_mu = (
        median([row.e for row in healthy]),
        median([row.i for row in healthy]),
        median([row.s for row in healthy]),
    )
    fleet_delta95 = percentile([distance_eis(row, fleet_mu) for row in healthy], 95) or FROZEN_FLEET_DELTA_NORM_MAX
    fleet_v_abs95 = percentile([abs(row.v) for row in healthy], 95) or 1.0

    by_class: Dict[str, List[StateRow]] = defaultdict(list)
    for row in healthy:
        by_class[row.agent_class].append(row)

    class_mu: Dict[str, Tuple[float, float, float]] = {}
    class_delta95: Dict[str, float] = {}
    class_v_abs95: Dict[str, float] = {}
    class_healthy_n: Dict[str, int] = {}

    for agent_class, class_rows in by_class.items():
        class_healthy_n[agent_class] = len(class_rows)
        if len(class_rows) < n_min:
            continue
        mu = (
            median([row.e for row in class_rows]),
            median([row.i for row in class_rows]),
            median([row.s for row in class_rows]),
        )
        class_mu[agent_class] = mu
        class_delta95[agent_class] = percentile([distance_eis(row, mu) for row in class_rows], 95) or fleet_delta95
        class_v_abs95[agent_class] = percentile([abs(row.v) for row in class_rows], 95) or fleet_v_abs95

    return Calibration(
        fleet_mu=fleet_mu,
        fleet_delta95=fleet_delta95,
        fleet_v_abs95=fleet_v_abs95,
        class_mu=class_mu,
        class_delta95=class_delta95,
        class_v_abs95=class_v_abs95,
        class_healthy_n=class_healthy_n,
        healthy_n=len(healthy),
    )


def distance_eis(row: StateRow, mu: Tuple[float, float, float]) -> float:
    """Euclidean distance from a row's (E, I, S) point to a baseline."""
    return math.dist((row.e, row.i, row.s), mu)


def grounded_coherence(row: StateRow, mu: Tuple[float, float, float], delta95: float) -> float:
    """Manifold coherence: 1 - distance/radius, clipped to [0, 1]."""
    ratio = distance_eis(row, mu) / delta95
    return 1.0 - max(0.0, min(1.0, ratio))


def legacy_tanh_coherence(row: StateRow, v_scale: float) -> float:
    """Artificial tanh(V/V_scale) coherence for the LC control condition."""
    return 0.5 * (1.0 + math.tanh(row.v / v_scale))


def condition_coherences(row: StateRow, calibration: Calibration) -> Dict[str, float]:
    """Return coherence values for the four ablation conditions."""
    agent_class = row.agent_class
    frozen_mu = FROZEN_HEALTHY_POINT_BY_CLASS.get(agent_class, FROZEN_FLEET_HEALTHY_POINT)
    frozen_delta = FROZEN_DELTA_NORM_MAX_BY_CLASS.get(agent_class, FROZEN_FLEET_DELTA_NORM_MAX)
    v_scale = calibration.class_v_abs95.get(agent_class, calibration.fleet_v_abs95)
    return {
        "LF_stored_legacy_fleet": row.stored_coherence,
        "LC_legacy_class_vscale": legacy_tanh_coherence(row, v_scale),
        "GF_grounded_fleet": grounded_coherence(row, calibration.fleet_mu, calibration.fleet_delta95),
        "GC_grounded_class_frozen": grounded_coherence(row, frozen_mu, frozen_delta),
    }


def condition_basins(rows: Sequence[StateRow], calibration: Calibration) -> Dict[str, List[str]]:
    """Classify all rows under each ablation condition."""
    basins: Dict[str, List[str]] = defaultdict(list)
    for row in rows:
        for name, coherence in condition_coherences(row, calibration).items():
            basins[name].append(classify_basin(row.e, row.i, row.s, row.v, coherence, row.risk))
    return dict(basins)


def transition_counter(a: Sequence[str], b: Sequence[str]) -> Counter:
    """Count basin transitions between two condition assignments."""
    return Counter(f"{left}->{right}" for left, right in zip(a, b) if left != right)


def format_pct(numerator: int, denominator: int) -> str:
    """Format a percentage with one decimal place."""
    return f"{100.0 * numerator / denominator:.1f}%" if denominator else "0.0%"


def format_wilson_ci(numerator: int, denominator: int, z: float = 1.96) -> str:
    """Format an approximate Wilson 95% confidence interval for a proportion."""
    if denominator <= 0:
        return "0.0%-0.0%"
    p_hat = numerator / denominator
    z2 = z * z
    denom = 1.0 + z2 / denominator
    center = (p_hat + z2 / (2.0 * denominator)) / denom
    half_width = z * math.sqrt((p_hat * (1.0 - p_hat) + z2 / (4.0 * denominator)) / denominator) / denom
    lo = max(0.0, center - half_width)
    hi = min(1.0, center + half_width)
    return f"{100.0 * lo:.1f}%-{100.0 * hi:.1f}%"


def render_report(start: str, end: str, rows: Sequence[StateRow], calibration: Calibration) -> str:
    """Render the ablation report as plain terminal-friendly text."""
    basins = condition_basins(rows, calibration)
    names = [
        "LF_stored_legacy_fleet",
        "LC_legacy_class_vscale",
        "GF_grounded_fleet",
        "GC_grounded_class_frozen",
    ]
    pairs = [
        ("LF_stored_legacy_fleet", "GF_grounded_fleet", "formula change under fleet calibration"),
        ("GF_grounded_fleet", "GC_grounded_class_frozen", "class calibration under grounded formula"),
        ("LF_stored_legacy_fleet", "GC_grounded_class_frozen", "reported full substitution"),
        ("LF_stored_legacy_fleet", "LC_legacy_class_vscale", "artificial legacy class-V-scale control"),
        ("LC_legacy_class_vscale", "GC_grounded_class_frozen", "formula change under class-ish calibration"),
    ]

    lines = [
        "PHASE 2 FORMULA × CALIBRATION ABLATION",
        f"Window: {start} -> {end}",
        f"Rows: {len(rows)}",
        f"Healthy calibration rows: {calibration.healthy_n}",
        f"Fleet grounded mu: ({calibration.fleet_mu[0]:.4f}, {calibration.fleet_mu[1]:.4f}, {calibration.fleet_mu[2]:.4f})",
        f"Fleet grounded delta95: {calibration.fleet_delta95:.4f}",
        f"Fleet |V| p95 for LC control: {calibration.fleet_v_abs95:.4f}",
        "",
        "Class calibration measured from the same healthy slice:",
    ]
    for agent_class in sorted({row.agent_class for row in rows}):
        lines.append(
            f"  {agent_class:<20} healthy_n={calibration.class_healthy_n.get(agent_class, 0):5d} "
            f"delta95={calibration.class_delta95.get(agent_class, float('nan')):.4f} "
            f"v_abs95={calibration.class_v_abs95.get(agent_class, float('nan')):.4f}"
        )

    lines.extend(["", "Condition basin distributions:"])
    for name in names:
        counts = Counter(basins[name])
        lines.append(
            f"  {name:<30} high={counts['high']:5d} "
            f"boundary={counts['boundary']:5d} low={counts['low']:5d}"
        )

    lines.extend(["", "Pairwise disagreement rates:"])
    for left, right, label in pairs:
        transitions = transition_counter(basins[left], basins[right])
        total = sum(transitions.values())
        lines.append(
            f"  {left} -> {right}: {total}/{len(rows)} = {format_pct(total, len(rows))} "
            f"(95% CI {format_wilson_ci(total, len(rows))})  [{label}]"
        )
        for transition, count in transitions.most_common():
            lines.append(f"    {transition}: {count}")

    lines.extend(["", "Reported full substitution by class (LF -> GC):"])
    by_class_total: Counter = Counter(row.agent_class for row in rows)
    by_class_flip: Counter = Counter()
    by_class_transition: Dict[str, Counter] = defaultdict(Counter)
    left = basins["LF_stored_legacy_fleet"]
    right = basins["GC_grounded_class_frozen"]
    for row, left_basin, right_basin in zip(rows, left, right):
        if left_basin != right_basin:
            by_class_flip[row.agent_class] += 1
            by_class_transition[row.agent_class][f"{left_basin}->{right_basin}"] += 1
    for agent_class, n_rows in by_class_total.most_common():
        flips = by_class_flip[agent_class]
        transitions = ", ".join(f"{k}:{v}" for k, v in by_class_transition[agent_class].most_common()) or "none"
        lines.append(
            f"  {agent_class:<20} N={n_rows:5d} flips={flips:5d} {format_pct(flips, n_rows):>6} "
            f"(95% CI {format_wilson_ci(flips, n_rows)})  {transitions}"
        )

    lines.extend([
        "",
        "Interpretation guard:",
        "  LC_legacy_class_vscale is an artificial scale-only tanh(V) control, not a deployed alternative.",
        "  It shows that a naive per-class V-scale graft onto the legacy formula is unstable/pathological.",
        "  The grounded-form fleet->class comparison is the cleaner calibration ablation.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    """Parse arguments, run the ablation, and print the report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-url", default="postgresql:///governance")
    parser.add_argument("--start", default="2026-03-19 21:28:53.257824-06")
    parser.add_argument("--end", default="2026-04-18 21:28:53.257824-06")
    parser.add_argument("--n-min", type=int, default=30)
    args = parser.parse_args()

    rows = fetch_rows(args.db_url, args.start, args.end)
    calibration = measure_calibration(rows, args.n_min)
    print(render_report(args.start, args.end, rows, calibration), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
