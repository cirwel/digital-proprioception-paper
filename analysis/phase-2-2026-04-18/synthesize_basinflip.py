#!/usr/bin/env python3
"""
Synthetic reproducibility artifact for the Phase 2 basin-flip (28.9%) claim.

The empirical numbers (paper §3.4/§3.7) run on 13,310 production rows that are
not releasable. This generates a SYNTHETIC, distribution-preserving stand-in that
a reviewer can run through the SAME classifier (formula_calibration_ablation.py)
to reproduce the qualitative basin-flip result on releasable data.

Method: per agent-class, fit a Gaussian copula over the six variables the
classifier reads -- (E, I, S, V, risk, stored_coherence) -- plus the empirical
regime distribution. A copula reproduces each marginal (via interpolated
empirical quantiles -> novel values, not real rows) and the cross-correlations,
which is exactly the joint structure the LF/GC basin assignment depends on.

HONEST SCOPE: validates the PIPELINE on releasable data (a reviewer reproduces
the qualitative flip rate and component ordering), NOT the empirical numbers,
which stay anchored to the private production DB. Gaussian-copula marginals are
smooth; boundary-sensitive flip rates may differ by a few points from production.
Not tuned to hit 28.9%.

Outputs: synthetic_basinflip_states.csv  (RELEASABLE)
Reuses the real classifier from formula_calibration_ablation.py.
"""
import numpy as np, csv
from collections import Counter
from scipy.stats import norm, rankdata
import formula_calibration_ablation as abl

RNG = 20260603
COLS = ["e", "i", "s", "v", "risk", "stored_coherence"]
DB = "postgresql:///governance"
START, END = "2026-03-19 21:28:53.257824-06", "2026-04-18 21:28:53.257824-06"
rng = np.random.default_rng(RNG)


def fit_copula(M):
    """M: (n,6) real. Return sampler() drawing novel rows preserving marginals+corr."""
    n = len(M)
    Z = np.column_stack([norm.ppf((rankdata(M[:, j]) - 0.5) / n) for j in range(M.shape[1])])
    C = np.corrcoef(Z.T)
    C = np.nan_to_num(C, nan=0.0); np.fill_diagonal(C, 1.0)
    L = np.linalg.cholesky(C + 1e-6 * np.eye(C.shape[0]))
    grids = [(np.arange(n) + 0.5) / n for _ in range(M.shape[1])]
    sorts = [np.sort(M[:, j]) for j in range(M.shape[1])]

    def sample(m):
        Zs = rng.standard_normal((m, M.shape[1])) @ L.T
        U = norm.cdf(Zs)
        return np.column_stack([np.interp(U[:, j], grids[j], sorts[j])
                                for j in range(M.shape[1])])
    return sample


def main():
    real = abl.fetch_rows(DB, START, END)
    print(f"fetched {len(real)} real rows (to FIT only; not released)")

    # group real rows by class
    by_cls = {}
    for r in real:
        by_cls.setdefault(r.agent_class, []).append(r)

    syn_rows = []
    for cls, rows in by_cls.items():
        M = np.array([[r.e, r.i, r.s, r.v, r.risk, r.stored_coherence] for r in rows])
        regimes = [r.regime for r in rows]
        reg_vals, reg_cnt = zip(*Counter(regimes).items())
        reg_p = np.array(reg_cnt) / len(regimes)
        if len(rows) < 8:                       # too few to fit; resample regimes, jitter
            idx = rng.integers(0, len(rows), len(rows))
            S = M[idx] + rng.normal(0, 0.01, M[idx].shape)
        else:
            S = fit_copula(M)(len(rows))
        reg_s = rng.choice(reg_vals, size=len(rows), p=reg_p)
        for k in range(len(rows)):
            e, i, s, v, risk, coh = S[k]
            syn_rows.append(abl.StateRow(
                agent_class=cls, regime=reg_s[k],
                e=float(e), i=float(i), s=float(s), v=float(v),
                risk=float(np.clip(risk, 0, 1)),
                stored_coherence=float(np.clip(coh, 0, 1))))

    # ---- run the REAL classifier on synthetic rows ----------------------
    cal = abl.measure_calibration(syn_rows, 30)
    basins = abl.condition_basins(syn_rows, cal)
    n = len(syn_rows)

    def flip(a, b):
        return sum(1 for x, y in zip(basins[a], basins[b]) if x != y)
    lf, gf, gc = "LF_stored_legacy_fleet", "GF_grounded_fleet", "GC_grounded_class_frozen"
    print(f"\nSYNTHETIC basin-flip reproduction (n={n}):")
    print(f"  LF -> GF (formula change)        : {flip(lf,gf)/n:5.1%}   [real 11.2%]")
    print(f"  GF -> GC (class calibration)     : {flip(gf,gc)/n:5.1%}   [real 23.5%]")
    print(f"  LF -> GC (full substitution)     : {flip(lf,gc)/n:5.1%}   [real 28.9%]  <- headline")

    # per-class LF->GC
    print("\n  per-class LF->GC:")
    by = {}
    for r, x, y in zip(syn_rows, basins[lf], basins[gc]):
        by.setdefault(r.agent_class, [0, 0]); by[r.agent_class][1] += 1
        if x != y: by[r.agent_class][0] += 1
    for cls, (f, t) in sorted(by.items(), key=lambda kv: -kv[1][1]):
        print(f"    {cls:14s} {f:4d}/{t:5d} = {f/t:5.1%}")

    # ---- save releasable synthetic CSV ----------------------------------
    out = "synthetic_basinflip_states.csv"
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["agent_class", "regime", *COLS])
        for r in syn_rows:
            w.writerow([r.agent_class, r.regime, r.e, r.i, r.s, r.v, r.risk, r.stored_coherence])
    print(f"\nwrote {out} ({n} synthetic rows; releasable -- no production rows)")


if __name__ == "__main__":
    main()
