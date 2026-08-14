# Reproducing the basin-flip result

Paper §3.4 and §3.7 report a 28.9% basin-flip rate when class-conditional grounded
coherence replaces fleet-wide `tanh`-of-$V$ on a 30-day production window
(N = 13,310). This directory holds the record of that measurement and a
reviewer-runnable reproduction of it.

## Run it

```
python3 reproduce_basinflip.py
```

Standard library only. No database, no network, no third-party packages.

The script verifies both input hashes, then recomputes the class-conditional
grounded coherence and *both* basin labels from the published state coordinates
and the published Phase 2 constants, compares them against the labels stored in
the export, and counts the flip rate from the recomputed labels. Expected output:

| | Recomputed here | Paper §3.4 |
|---|---:|---:|
| Full substitution | **28.84%** (3,834 / 13,292) | 28.9% (3,844 / 13,310) |
| Lumen | 32.2% | 32.3% |
| default | 30.6% | 31.2% |
| Sentinel | 15.8% | 15.8% |
| Vigil | 33.5% | 33.1% |
| Watcher | 18.9% | 18.5% |

26,574 of 26,584 basin labels reproduce exactly. The ten that do not sit within
6.7e-4 of a threshold: the export stores floats at 4 decimal places, and
recomputing a distance from rounded coordinates and dividing by a class radius as
small as 0.1187 amplifies that rounding. The script reports the margin rather
than asserting exactness.

## What the inputs are

`verdict_counterfactual_v6_submission.csv` — 13,292 rows, the 30-day window ending
2026-04-18 21:00 MDT. One row per agent-state observation, pseudonymized to a class
label: no agent UUIDs, session IDs, prompts, or knowledge-graph content.

`verdict_counterfactual_2026-04-23.csv` — 16,879 rows, the window ending 2026-04-23,
with the Phase 2 calibration constants held frozen. Included because it is the
paper's own evidence on between-window variance (see below).

Both are verbatim copies of the archived dataset, pinned by SHA-256 in the script:

- **Canonical archive:** Zenodo data DOI [10.5281/zenodo.19705151](https://doi.org/10.5281/zenodo.19705151)
- **Source repository:** [cirwel/unitares-repro-v6](https://github.com/cirwel/unitares-repro-v6)
- **Provenance:** UNITARES production governance database, 30-day rolling window of
  `core.agent_state`, exported 2026-04-23.

## Why the export is the record, not the database

The production database no longer retains this window. `core.agent_state` holds
**490 rows** in the 2026-03-19 → 2026-04-18 interval, against the 13,310 the original
pull returned, and there is no archive table. Monthly row counts show the cliff:

```
2025-12  445     2026-04    599
2026-01   33     2026-05 12,630
2026-02  369     2026-06 27,868
2026-03  344     2026-07 16,869
```

The frozen export is therefore the only surviving row-level record of the
measurement. Re-running the original DB query cannot reproduce it, and a private
audit of the production rows is no longer possible. The paper states this in §3.7
and the Appendix rather than offering a check that cannot be performed.

## The 18-row difference

The export carries 13,292 rows against the paper's 13,310. The export was taken by a
separate run of the counterfactual against a rolling window anchored in wall-clock
time, so the two pulls differ by a few seconds of row arrivals. This is the source of
the 28.9% / 28.8% difference, and it is the whole difference: per-class rates agree
within 0.5 percentage points.

The export also carries five classes, not six. The 42 `ephemeral` rows in the paper's
§3.4 table have no counterpart here; they had no frozen Phase 2 envelope, fell through
the fleet fallback, flipped zero times, and are not interpreted in the paper either.

## Between-window variance

The two windows are four days apart with roughly 87% row overlap, and give **28.8%**
and **44.3%**. That 15.5-point spread against a within-window sampling CI of ±0.8
points is why the paper quotes the existence and order of magnitude of the
disagreement rather than the third digit. Neither snapshot is privileged; the 2026-04-18
window is reported because it is the one the v6 measurement was taken on.

## What is *not* reproducible from these files

`formula_calibration_ablation.py` computes the four-condition ablation (LF / GF / GC /
LC, paper §3.7). Its GF and LC conditions need a fleet-wide healthy slice, which
requires the per-row `regime` column — and `regime` is not in the export. That script
therefore still requires the production database, which no longer holds the window.
Its recorded output is preserved verbatim in `formula_calibration_ablation_results.txt`
and is provenance-backed rather than re-runnable. The full-substitution headline
(LF → GC), which is what the paper leads with, *is* re-runnable and is what
`reproduce_basinflip.py` checks.
