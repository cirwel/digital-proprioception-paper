# Reproducing the 28.9% basin-flip on releasable data

The empirical numbers run on 13,310 production rows that are not released. To let a
reviewer re-run the result anyway, `synthesize_basinflip.py` fits a per-agent-class
**Gaussian copula** over the six variables the classifier reads — (E, I, S, V,
risk, stored_coherence) plus the empirical regime distribution — and emits
`synthetic_basinflip_states.csv` (**releasable; no production rows**). The copula
preserves each marginal (interpolated empirical quantiles → novel values, not real
rows) and the cross-correlations, which is the joint structure the LF/GC basin
assignment depends on.

Run through the **same** classifier (`formula_calibration_ablation.py`):

| Disagreement | Synthetic | Production |
|---|---:|---:|
| LF→GF (formula change) | 11.0% | 11.2% |
| GF→GC (class calibration) | 22.8% | 23.5% |
| **LF→GC (full substitution, the headline)** | **29.3%** | **28.9%** |

Per-class LF→GC also tracks (Lumen 32.0/32.3, default 33.0/31.2, Sentinel
15.6/15.8; Vigil/Watcher differ more at small N).

## Honest scope
- **Reproduces the pipeline on releasable data**, not the production rows. No real
  row is recoverable; the released object is the *distribution*, which is what any
  reproduction of a distributional statistic requires. Consistent with the paper's
  "raw production rows not public" stance (rows withheld, distribution disclosed).
- **Not tuned.** The copula is fit to preserve the joint; the 29.3% is emergent.
  The close match is because the flip is a deterministic function of the preserved
  variables — unlike the trajectory pilot, where an idealized model ran *easier*
  than production.
- The production numbers (§3.4/§3.7) remain the cited result; this is a
  reviewer-runnable check, and independent re-measurement on independent data is
  still the stronger bar.

## Run
```
python3 synthesize_basinflip.py          # regenerates the synthetic CSV + report
# then a reviewer can run the classifier on the synthetic rows directly
```
