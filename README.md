# A Flat Coherence Score: What a Production-Data Replay Does and Does Not Show About Agent Self-State Gating

Notes toward digital proprioception.

**Author:** Kenny Wang (Independent Researcher, CIRWEL Systems) — ORCID [0009-0006-7544-2374](https://orcid.org/0009-0006-7544-2374)  
**Status:** v2.0 (2026-10-02). A short-form rewrite that replaces the 27,800-word v1.2; corrections are listed in the paper's Appendix B.  
**License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

> **Plain-language summary.** A multi-agent system I run gives every agent check-in a "coherence" score and uses it to sort agent states into high, boundary and low basins. On 13,292 production rows that score sat in a band too narrow to reach its own thresholds, so it almost never decided a basin. Replacing it with a score measured against each agent class's own healthy point changes about 29% of the recomputed labels, largely because the reference points had gone stale. The paper shows the old score was inert at its thresholds. It does not show that the new labels are right, and whether any of this forecasts bad outcomes is unresolved.

## Abstract

A running multi-agent system I operate computes a scalar "coherence" for every agent check-in and uses it, among other inputs, to place each state in one of three basins (high, boundary, low). On a 30-day production slice of 13,292 rows, the deployed score was flat within a narrow band: its 1st to 99th percentile range was 0.447 to 0.499. It never reached the 0.40 threshold below which it could push a state into the low basin, and it cleared the 0.45 high-basin threshold for 98.7% of rows, so it almost never decided a basin. The score is not empty. It carries some class information (its distributions for two classes separate with an AUC of 0.88), and it correlates r = 0.73 with a smoothed energy-integrity imbalance. But within each class, its association with distance from that class's own healthy operating point was weak and went both ways: Spearman ρ from -0.37 to +0.18 across classes, with the wrong sign in two of five, and in three of five in a later window.

I replaced the score with a class-conditional "grounded" form on the same rows and recomputed every basin under both forms. The grounded form spans 0 to 0.995, and on the full substitution every row whose recomputed basin changes moves downward (§4). The replay is an offline counterfactual on frozen data. It shows that the old score was inert at its decision thresholds. It does not show that the new labels are right, and no outcome, harm or operator judgment was used to grade either form. The rate of label change rose from 28.8% to 44.3% between two public windows whose end dates are four to five days apart. That rise is not noise. Rows whose stored values occur in both windows flip at 30.3%, and rows that appear only in the later window, inferred to be recorded after 2026-04-18, flip at 80.6%. The flip rate therefore depends on how far the state distribution has moved from the frozen class anchors; it is not a fixed property of the formula swap.

Three adjacent results bound the claim. Whether per-agent state forecasts bad outcomes is unresolved, pending one pre-registered read (§6). A genesis-anchored lineage check meant to catch slow drift does not discriminate as instrumented (§7). The cumulative-deviation integral that motivated earlier versions of this paper is specified but not computed by any production code path (§8). A single-agent case study tests an apparent "delayed shut-down" reading: the April anchor's calibration window ended a day after a shift in the agent's operating point, and recalibration moves toward the current state, as staleness predicts. That result does not by itself exclude a persistent shift, and the cause is open (§5).

## Read

- **[paper.md](paper.md)**: the paper (v2.0)
- **[digital-proprioception.pdf](digital-proprioception.pdf)**: the distribution PDF
- **[CITATION.cff](CITATION.cff)**: citation metadata
- **[.zenodo.json](.zenodo.json)**: Zenodo deposit metadata
- Earlier versions, including the long-form v1.2, stay available as tags and under the Zenodo concept DOI.

## Companion artefacts

- **UNITARES governance MCP** — [CIRWEL/unitares](https://github.com/CIRWEL/unitares); paper at [CIRWEL/unitares-paper-v6](https://github.com/CIRWEL/unitares-paper-v6) (Zenodo concept [10.5281/zenodo.19647159](https://doi.org/10.5281/zenodo.19647159))
- **Trajectory identity framework (TIWD)** — Wang 2026b, Zenodo concept [10.5281/zenodo.20098168](https://doi.org/10.5281/zenodo.20098168); source [cirwel/trajectory-identity-paper](https://github.com/cirwel/trajectory-identity-paper)
- **EISV-Lumen benchmark** — [CIRWEL/eisv-lumen](https://github.com/CIRWEL/eisv-lumen); dataset [hikewa/unitares-eisv-trajectories](https://huggingface.co/datasets/hikewa/unitares-eisv-trajectories) (revision pinned: `aeb47055ee5f27cb93124e4e3df065301ada6909`, 2026-05-09)
- **Anima/Lumen substrate** — [CIRWEL/anima-mcp](https://github.com/CIRWEL/anima-mcp)

## Reproducing the headline

```
python3 analysis/phase-2-2026-04-18/reproduce_basinflip.py
```

Standard library only — no database, no network, no third-party packages. It runs against the frozen, de-identified row-level export (13,292 rows, archived under Zenodo data DOI [10.5281/zenodo.19705151](https://doi.org/10.5281/zenodo.19705151), mirrored here with its SHA-256 pinned), recomputes the grounded coherence and both basin labels from the published state coordinates and the published Phase 2 constants, and counts the flip rate from the recomputed labels. It returns **28.84%** against the 28.9% reported, with 26,574 of 26,584 basin labels reproducing exactly.

Two limits are disclosed. The production database no longer retains the measurement window, so the export is the surviving record and a private audit of the production rows is not available. And a second public window gives 44.3% instead of 28.8%: that difference is a deterministic composition effect, which `flatness_and_windows.py` decomposes by exact count (paper §4.2). See [`analysis/phase-2-2026-04-18/REPRO.md`](analysis/phase-2-2026-04-18/REPRO.md).

## Citation

See [CITATION.cff](CITATION.cff). Zenodo concept DOI (resolves to latest version): [10.5281/zenodo.21930092](https://doi.org/10.5281/zenodo.21930092).
