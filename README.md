# Digital Proprioception and Allostatic Load

A working implementation of the cumulative-deviation hypothesis in a deployed multi-agent system.

**Author:** Kenny Wang (Independent Researcher, CIRWEL Systems) — ORCID [0009-0006-7544-2374](https://orcid.org/0009-0006-7544-2374)
**Status:** First complete draft — v0.3, 2026-05-09
**License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

## Abstract

Allostatic load (McEwen and Stellar 1993) — the time-integrated cost of regulating an adaptive system away from its operating point — has been an influential theoretical construct in physiology and psychiatry for thirty years. Its mathematical core has remained, in clinical practice, difficult to test as a real-time control signal. We present UNITARES, a governance framework for heterogeneous AI agent fleets in production since November 2025, as a deployed instantiation of the mathematical core of allostatic load on a four-dimensional informational manifold. We make four contributions: $V_{\text{anima}}$ as a deployed allostatic-load test bed; class-conditional calibration as the cosmological-soup correction, now bounded by a same-row formula-vs-calibration ablation; McEwen's Four Types as an imported but non-exhaustive failure-mode taxonomy; and a synthetic-psychology epistemic stance in the lineage of artificial life and minimally cognitive agents.

## Read

- **[paper.md](paper.md)** — the working draft (v0.3)
- **[references.bib](references.bib)** — bibliography stub (canonical list lives in `paper.md` § References for now)
- **[CITATION.cff](CITATION.cff)** — citation metadata
- **[.zenodo.json](.zenodo.json)** — Zenodo deposit metadata (DOI minted on first stable tag)

## Companion artefacts

- **UNITARES governance MCP** — [CIRWEL/unitares](https://github.com/CIRWEL/unitares); paper at [CIRWEL/unitares-paper-v6](https://github.com/CIRWEL/unitares-paper-v6) (Zenodo concept [10.5281/zenodo.19647159](https://doi.org/10.5281/zenodo.19647159))
- **Trajectory identity framework (TIWD)** — Wang 2026b, Zenodo concept [10.5281/zenodo.20098168](https://doi.org/10.5281/zenodo.20098168) (v0.11.1); source [cirwel/trajectory-identity-paper](https://github.com/cirwel/trajectory-identity-paper)
- **EISV-Lumen benchmark** — [CIRWEL/eisv-lumen](https://github.com/CIRWEL/eisv-lumen); dataset [hikewa/unitares-eisv-trajectories](https://huggingface.co/datasets/hikewa/unitares-eisv-trajectories) (revision pinned: `aeb47055ee5f27cb93124e4e3df065301ada6909`, 2026-05-09)
- **Anima/Lumen substrate** — [CIRWEL/anima-mcp](https://github.com/CIRWEL/anima-mcp)

## Status of empirical claims

The paper contains substantial empirical content where biology has parallels (basin-flip rate, envelope spread, and an apparent Type 3 case resolved by recalibration as a basin transition) and substantial argument elsewhere (the bridge claims, the methodological proposals). §1.3 now gives an evidence-grade / falsifier table; §9.2 lays out the show-vs-argue balance; the appendix separates pipeline reproducibility, production-number verification, and independent validation. Reviewers should evaluate each contribution at its appropriate level of evidence.

The 28.9% basin-flip rate (§3.4) is inherited from Wang 2026a §11.6 and now has a same-row ablation in `analysis/phase-2-2026-04-18/`: production legacy → grounded fleet-wide flips 11.2%, grounded fleet-wide → grounded class-conditional flips 23.5%, and the full substitution remains 28.9%. The Lumen recalibration case study (§5.3) is original to this paper: an 86-minute window initially resembling Type 3, then reclassified by post-event recalibration as calibration staleness after a 2026-04-17 basin transition. The transition is identification-grade for date/magnitude/shape and anomaly-grade for substrate causality pending multi-agent or multi-revision replication.

## Citation

See [CITATION.cff](CITATION.cff). DOI will be minted on first stable tag via Zenodo-GitHub integration.
