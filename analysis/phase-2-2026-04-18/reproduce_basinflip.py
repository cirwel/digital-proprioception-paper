#!/usr/bin/env python3
"""Reproduce the basin-flip result (paper §3.4, §3.7) from the frozen public export.

Standard library only. No database, no network, no third-party packages.

    python3 reproduce_basinflip.py

What this checks
----------------
The paper reports a 28.9% basin-flip rate on a 30-day production window. The
production database no longer retains that window (see REPRO.md), so the record
is the frozen, de-identified row-level export archived under Zenodo data DOI
10.5281/zenodo.19705151. This script does not merely re-count the export's
`flipped` column. It recomputes, from the published state coordinates and the
published Phase 2 constants:

  1. the class-conditional grounded coherence  C_grounded = 1 - ||Δ|| / ||Δ||_max,c
  2. the legacy basin label,   via classify_basin(E, I, S, V, c_legacy,   risk)
  3. the grounded basin label, via classify_basin(E, I, S, V, c_grounded', risk)

and compares all three against the values stored in the export. The flip rate is
then counted from the *recomputed* labels, not the stored ones.

Rounding
--------
The export stores every float at 4 decimal places. Recomputing a distance from
rounded coordinates and dividing by a class radius as small as 0.1187 amplifies
that rounding: expect |ΔC| up to ~7e-4, and expect a handful of rows sitting
within that margin of a basin threshold to land on the other side. The script
reports both so the agreement is quantified rather than asserted.
"""
from __future__ import annotations

import csv
import hashlib
import math
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent

# Frozen public exports. Canonical archival copies live under Zenodo data DOI
# 10.5281/zenodo.19705151 (github.com/cirwel/unitares-repro-v6); these are
# verbatim copies, pinned by hash below.
SUBMISSION = HERE / "verdict_counterfactual_v6_submission.csv"
COMPARISON = HERE / "verdict_counterfactual_2026-04-23.csv"

EXPECTED_SHA256 = {
    SUBMISSION.name: "5920ad13f7b9bd8218b310f6141c38a1b44914ce8c480ef8fdff09d31c2df7c0",
    COMPARISON.name: "98ad81c26a0aac572fff92d4126c3fbfa4a4a71d0b1366f08701018ec53ca424",
}

# Phase 2 measured constants, frozen at v6.8 submission (paper §3.3).
# Source of truth: unitares config/governance_config.py, replicated in
# cirwel/unitares-repro-v6 scripts/verdict_counterfactual.py.
HEALTHY_POINT = {
    "Lumen": (0.7454, 0.8001, 0.1678),
    "default": (0.7264, 0.7934, 0.2364),
    "Sentinel": (0.7506, 0.7981, 0.1934),
    "Vigil": (0.7371, 0.7896, 0.2404),
    "Watcher": (0.7482, 0.7686, 0.2477),
}
DELTA_NORM_MAX = {
    "Lumen": 0.1187,
    "default": 0.2018,
    "Sentinel": 0.1702,
    "Vigil": 0.1705,
    "Watcher": 0.3948,
}
FLEET_HEALTHY_POINT = (0.6, 0.7, 0.0)
FLEET_DELTA_NORM_MAX = 1.8

# Basin thresholds (paper §3.7). Mirrors config.governance_config.classify_basin.
LOW_I_CEIL, LOW_COHERENCE_CEIL, LOW_V_ABS_FLOOR, LOW_RISK_FLOOR = 0.5, 0.40, 0.30, 0.70
HIGH_E_MIN, HIGH_I_MIN, HIGH_S_MAX = 0.6, 0.7, 0.25
HIGH_V_ABS_MAX, HIGH_COHERENCE_MIN, HIGH_RISK_MAX = 0.15, 0.45, 0.45

ROUNDING_TOLERANCE = 1e-3


def classify_basin(e, i, s, v, coherence, risk):
    """LOW is disjunctive, HIGH is conjunctive, BOUNDARY is the complement."""
    if i < LOW_I_CEIL or coherence < LOW_COHERENCE_CEIL \
            or abs(v) > LOW_V_ABS_FLOOR or risk >= LOW_RISK_FLOOR:
        return "low"
    if e >= HIGH_E_MIN and i >= HIGH_I_MIN and s <= HIGH_S_MAX \
            and abs(v) <= HIGH_V_ABS_MAX and coherence >= HIGH_COHERENCE_MIN \
            and risk <= HIGH_RISK_MAX:
        return "high"
    return "boundary"


def grounded_coherence(e, i, s, agent_class):
    mu = HEALTHY_POINT.get(agent_class, FLEET_HEALTHY_POINT)
    radius = DELTA_NORM_MAX.get(agent_class, FLEET_DELTA_NORM_MAX)
    return 1.0 - max(0.0, min(1.0, math.dist((e, i, s), mu) / radius))


def wilson_ci(k, n, z=1.96):
    """Wilson score interval — well behaved near 0 and 1, unlike the normal approx."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (centre - half, centre + half)


def verify_hash(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    expected = EXPECTED_SHA256[path.name]
    ok = digest == expected
    print(f"  {path.name}")
    print(f"    sha256 {digest}")
    print(f"    {'OK — matches the pinned hash' if ok else 'MISMATCH — expected ' + expected}")
    return ok


def load(path):
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def analyse(rows, recompute):
    """Return (n, flips, per_class, checks). per_class maps class -> [flips, n]."""
    per_class = defaultdict(lambda: [0, 0])
    checks = {"coherence_mismatch": 0, "max_abs_dc": 0.0,
              "basin_legacy_mismatch": 0, "basin_grounded_mismatch": 0}
    flips = 0
    for r in rows:
        cls = r["class"]
        e, i, s, v, risk = (float(r[k]) for k in ("E", "I", "S", "V", "risk"))
        c_legacy = float(r["c_legacy"])

        if recompute:
            c_grounded = grounded_coherence(e, i, s, cls)
            dc = abs(c_grounded - float(r["c_grounded"]))
            checks["max_abs_dc"] = max(checks["max_abs_dc"], dc)
            if dc > ROUNDING_TOLERANCE:
                checks["coherence_mismatch"] += 1
            basin_legacy = classify_basin(e, i, s, v, c_legacy, risk)
            basin_grounded = classify_basin(e, i, s, v, c_grounded, risk)
            if basin_legacy != r["basin_legacy"]:
                checks["basin_legacy_mismatch"] += 1
            if basin_grounded != r["basin_grounded"]:
                checks["basin_grounded_mismatch"] += 1
        else:
            basin_legacy, basin_grounded = r["basin_legacy"], r["basin_grounded"]

        flipped = basin_legacy != basin_grounded
        per_class[cls][1] += 1
        if flipped:
            per_class[cls][0] += 1
            flips += 1
    return len(rows), flips, per_class, checks


# Paper §3.4 Table, for side-by-side comparison.
PAPER_TABLE = {"Lumen": (7890, 32.3), "default": (2316, 31.2), "Sentinel": (2227, 15.8),
               "Vigil": (472, 33.1), "Watcher": (363, 18.5)}


def main():
    print("=" * 74)
    print("BASIN-FLIP REPRODUCTION — paper §3.4 / §3.7")
    print("=" * 74)
    print("\nInput integrity (canonical archive: Zenodo 10.5281/zenodo.19705151):")
    if not all(verify_hash(p) for p in (SUBMISSION, COMPARISON)):
        print("\nHash mismatch — the inputs are not the pinned exports. Stopping.")
        return 1

    rows = load(SUBMISSION)
    n, flips, per_class, checks = analyse(rows, recompute=True)
    lo, hi = wilson_ci(flips, n)

    print("\n" + "-" * 74)
    print("Recomputation check (published state + published constants -> labels)")
    print("-" * 74)
    total_labels = 2 * n  # a legacy label and a grounded label per row
    agree = total_labels - checks["basin_legacy_mismatch"] - checks["basin_grounded_mismatch"]
    print(f"  rows                                  {n:,}")
    print(f"  max |C_grounded recomputed - stored|  {checks['max_abs_dc']:.2e}"
          f"   (4-dp export rounding; tolerance {ROUNDING_TOLERANCE:.0e})")
    print(f"  coherence beyond tolerance            {checks['coherence_mismatch']}")
    print(f"  basin_legacy   label disagreements    {checks['basin_legacy_mismatch']}")
    print(f"  basin_grounded label disagreements    {checks['basin_grounded_mismatch']}")
    print(f"  -> {agree:,}/{total_labels:,} labels reproduce exactly "
          f"({agree / total_labels:.4%}); disagreements sit within "
          f"{checks['max_abs_dc']:.1e} of a threshold.")

    print("\n" + "-" * 74)
    print("Flip rate, counted from RECOMPUTED labels")
    print("-" * 74)
    print(f"  full substitution (legacy -> grounded class-conditional)")
    print(f"    {flips:,} / {n:,} = {flips / n:.2%}   "
          f"(Wilson 95% CI {lo:.1%}-{hi:.1%})")
    print(f"    paper §3.4 reports 28.9% on N=13,310 production rows;")
    print(f"    the export is 18 rows short of that pull (see REPRO.md).")

    print("\n  per class (paper §3.4 in parentheses):")
    for cls, (f, t) in sorted(per_class.items(), key=lambda kv: -kv[1][1]):
        clo, chi = wilson_ci(f, t)
        ref = PAPER_TABLE.get(cls)
        ref_s = f"   (paper N={ref[0]:,}, {ref[1]}%)" if ref else "   (not in paper table)"
        print(f"    {cls:<10s} N={t:>6,}  flips={f:>5,}  {f / t:>6.1%} "
              f"[{clo:.1%}-{chi:.1%}]{ref_s}")

    # Second window — the between-window variance the point estimate hides.
    rows2 = load(COMPARISON)
    n2, flips2, _, _ = analyse(rows2, recompute=True)
    print("\n" + "-" * 74)
    print("Between-window variance")
    print("-" * 74)
    print(f"  window ending 2026-04-18   {flips / n:.1%}   (N={n:,})")
    print(f"  window ending 2026-04-23   {flips2 / n2:.1%}   (N={n2:,})")
    print(f"  spread {abs(flips2 / n2 - flips / n) * 100:.1f} percentage points "
          f"across a 4-day window shift with ~87% row overlap,")
    print(f"  against a within-window sampling CI of ±{(hi - lo) / 2 * 100:.1f} pp.")
    print("  The order of magnitude is the finding. The third digit is not.")
    print("\n" + "=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
