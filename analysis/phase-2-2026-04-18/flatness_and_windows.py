#!/usr/bin/env python3
"""Recompute the paper's §3 flatness statistics and §4.2 window decomposition.

Standard library only. Reads the two public exports in this directory and
prints every §3 / §4.2 number the paper quotes that `reproduce_basinflip.py`
does not already print.

    python3 flatness_and_windows.py

The window decomposition matches the two exports on the full stored tuple
(class, E, I, S, V, risk, c_legacy), counted with multiplicity: a multiset
intersection of stored values, not a row-by-row join. The exports carry no row
identifiers or timestamps, and some rows share all seven key values with
another row. c_grounded is not in the key: it is computed from unrounded
coordinates, so it can differ between rows whose rounded values match. Rows
sharing a key carry identical stored labels, so the counts are unaffected. Basin labels are a deterministic function of the stored values
and the frozen Phase 2 constants, so a value tuple present in both windows
carries the same flip label in both. Flip rates in the decomposition use the
labels stored in the export.
"""
import csv
import math
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
W1_FILE = "verdict_counterfactual_v6_submission.csv"   # window ending 2026-04-18
W2_FILE = "verdict_counterfactual_2026-04-23.csv"      # window ending 2026-04-23

# Frozen Phase 2 healthy points; identical to reproduce_basinflip.py.
HEALTHY_POINT = {
    "Lumen": (0.7454, 0.8001, 0.1678),
    "default": (0.7264, 0.7934, 0.2364),
    "Sentinel": (0.7506, 0.7981, 0.1934),
    "Vigil": (0.7371, 0.7896, 0.2404),
    "Watcher": (0.7482, 0.7686, 0.2477),
}
NUMERIC = ("E", "I", "S", "V", "risk", "c_legacy", "c_grounded")

# Basin thresholds (paper §2.1); identical to reproduce_basinflip.py.
LOW_I_CEIL, LOW_COHERENCE_CEIL, LOW_V_ABS_FLOOR, LOW_RISK_FLOOR = 0.5, 0.40, 0.30, 0.70
HIGH_E_MIN, HIGH_I_MIN, HIGH_S_MAX = 0.6, 0.7, 0.25
HIGH_V_ABS_MAX, HIGH_COHERENCE_MIN, HIGH_RISK_MAX = 0.15, 0.45, 0.45


def load(name):
    with open(os.path.join(HERE, name), newline="") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        for k in NUMERIC:
            r[k] = float(r[k])
        r["flipped"] = int(r["flipped"])
    return rows


def pct(xs, p):
    xs = sorted(xs)
    k = (len(xs) - 1) * p / 100
    f = math.floor(k)
    c = min(f + 1, len(xs) - 1)
    return xs[f] + (xs[c] - xs[f]) * (k - f)


def mean(xs):
    return sum(xs) / len(xs)


def sd(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def pearson(a, b):
    ma, mb = mean(a), mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
    return num / den


def ranks(xs):
    order = sorted(range(len(xs)), key=xs.__getitem__)
    out = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for k in range(i, j + 1):
            out[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return out


def spearman(a, b):
    return pearson(ranks(a), ranks(b))


def auc(a, b):
    """P(a > b) + 0.5 P(a == b), via the Mann-Whitney rank sum."""
    r = ranks(list(a) + list(b))
    ra = sum(r[: len(a)])
    return (ra - len(a) * (len(a) + 1) / 2) / (len(a) * len(b))


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


def by_class(rows):
    out = defaultdict(list)
    for r in rows:
        out[r["class"]].append(r)
    return dict(sorted(out.items()))


def flatness(name, rows):
    print(f"\n== {name}: n = {len(rows):,}")
    for col in ("c_legacy", "c_grounded"):
        x = [r[col] for r in rows]
        print(f"  {col:10s} min {min(x):.4f}  p1 {pct(x, 1):.4f}  p25 {pct(x, 25):.4f}  "
              f"p50 {pct(x, 50):.4f}  p75 {pct(x, 75):.4f}  p99 {pct(x, 99):.4f}  "
              f"max {max(x):.4f}  sd {sd(x):.4f}")
    cl = [r["c_legacy"] for r in rows]
    cg = [r["c_grounded"] for r in rows]
    n = len(rows)
    print(f"  legacy < 0.40: {sum(c < 0.40 for c in cl)} rows;  legacy >= 0.45: {sum(c >= 0.45 for c in cl) / n:.2%}")
    print(f"  grounded == 0: {sum(c == 0 for c in cg) / n:.2%};  < 0.25: {sum(c < 0.25 for c in cg) / n:.2%};  "
          f"< 0.40: {sum(c < 0.40 for c in cg) / n:.2%}")
    print(f"  median tanh argument of legacy, atanh(2C - 1): {pct([math.atanh(2 * c - 1) for c in cl], 50):+.4f}")
    v = [r["V"] for r in rows]
    ei = [r["E"] - r["I"] for r in rows]
    rv = pearson(v, ei)
    print(f"  V ~ (E - I): r {rv:.3f}  R^2 {rv * rv:.3f}  sd(V) {sd(v):.4f}  sd(V - (E - I)) {sd([a - b for a, b in zip(v, ei)]):.4f}")
    print(f"  r(legacy, V) {pearson(cl, v):.3f}")
    gate = sum(classify_basin(r["E"], r["I"], r["S"], r["V"], r["c_legacy"], r["risk"])
               != classify_basin(r["E"], r["I"], r["S"], r["V"], 1.0, r["risk"]) for r in rows)
    print(f"  basins changed by setting coherence to 1 (its clauses always pass): {gate} of {n:,} ({gate / n:.3%})")

    print("  per class: n, legacy p50 / sd, grounded p50 / sd, flip rate, "
          "Spearman(legacy, distance to own healthy point), legacy p50 far (C_g < 0.1) / near (C_g > 0.8)")
    print("  (flip rates here use the labels stored in the export; reproduce_basinflip.py recomputes them)")
    classes = by_class(rows)
    for c, rs in classes.items():
        a = [r["c_legacy"] for r in rs]
        g = [r["c_grounded"] for r in rs]
        d = [math.dist((r["E"], r["I"], r["S"]), HEALTHY_POINT[c]) for r in rs]
        far = [r["c_legacy"] for r in rs if r["c_grounded"] < 0.1]
        near = [r["c_legacy"] for r in rs if r["c_grounded"] > 0.8]
        flips = sum(r["flipped"] for r in rs)
        print(f"    {c:9s} n {len(rs):5d}  L {pct(a, 50):.4f}/{sd(a):.4f}  G {pct(g, 50):.4f}/{sd(g):.4f}  "
              f"flip {flips / len(rs):6.1%}  rho {spearman(a, d):+.3f}  "
              f"far {pct(far, 50):.4f} (n {len(far)})  near {pct(near, 50):.4f} (n {len(near)})")
    names = list(classes)
    pair = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            x = auc([r["c_legacy"] for r in classes[names[i]]], [r["c_legacy"] for r in classes[names[j]]])
            pair.append((max(x, 1 - x), names[i], names[j]))
    lo, hi = min(pair), max(pair)
    print(f"  pairwise class AUC of legacy score (folded): {lo[0]:.3f} ({lo[1]}/{lo[2]}) to {hi[0]:.3f} ({hi[1]}/{hi[2]})")
    trans = Counter((r["basin_legacy"], r["basin_grounded"]) for r in rows if r["basin_legacy"] != r["basin_grounded"])
    print(f"  stored-label transitions: {dict(trans)}  (total {sum(trans.values()):,})")


def decompose(w1, w2):
    key = lambda r: (r["class"], r["E"], r["I"], r["S"], r["V"], r["risk"], r["c_legacy"])
    remaining = Counter(map(key, w1))
    dup_groups = [v for v in remaining.values() if v > 1]
    shared = defaultdict(lambda: [0, 0])
    new = defaultdict(lambda: [0, 0])
    new_below = Counter()
    new_zero = Counter()
    for r in w2:
        k = key(r)
        bucket = shared if remaining[k] > 0 else new
        if remaining[k] > 0:
            remaining[k] -= 1
        else:
            new_below[r["class"]] += r["c_grounded"] < 0.40
            new_zero[r["class"]] += r["c_grounded"] == 0
        bucket[r["class"]][0] += 1
        bucket[r["class"]][1] += r["flipped"]
    remaining_w2 = Counter(map(key, w2))
    dropped = [0, 0]
    for r in w1:
        k = key(r)
        if remaining_w2[k] > 0:
            remaining_w2[k] -= 1
        else:
            dropped[0] += 1
            dropped[1] += r["flipped"]

    def tot(b):
        return sum(v[0] for v in b.values()), sum(v[1] for v in b.values())

    sn, sf = tot(shared)
    nn, nf = tot(new)
    print("\n== Window decomposition (multiset match on stored values; stored labels)")
    print(f"  first-window duplicate value groups: {len(dup_groups):,}, holding {sum(dup_groups):,} rows "
          f"({sum(v - 1 for v in dup_groups):,} beyond the first in each group)")
    print(f"  rows in both windows: {sn:,} = {sn / len(w1):.1%} of the first window, {sn / len(w2):.1%} of the second")
    print(f"  first-window rows absent from the second: {dropped[0]:,}, flip {dropped[1] / dropped[0]:.1%}")
    print(f"  rows in both windows:                     {sn:,}, flip {sf / sn:.1%}")
    print(f"  second-window-only rows:                  {nn:,}, flip {nf / nn:.1%}")
    for c in sorted(new):
        n, f = new[c]
        s_n, s_f = shared[c]
        print(f"    {c:9s} shared {s_n:5d} flip {s_f / s_n:6.1%}   new {n:5d} flip {f / n:6.1%}  "
              f"C_g < 0.40 {new_below[c] / n:6.1%}  C_g = 0 {new_zero[c] / n:6.1%}")


def main():
    w1, w2 = load(W1_FILE), load(W2_FILE)
    flatness("window ending 2026-04-18", w1)
    flatness("window ending 2026-04-23", w2)
    decompose(w1, w2)


if __name__ == "__main__":
    main()
