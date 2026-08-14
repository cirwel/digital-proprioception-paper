# Digital Proprioception and Allostatic Load

A deployed synthetic-system report on the cumulative-deviation hypothesis and its limits as an allostatic-load analogue.

**Author:** Kenny Wang (Independent Researcher, CIRWEL Systems) — ORCID [0009-0006-7544-2374](https://orcid.org/0009-0006-7544-2374)
**Status:** v1.0 — first stable release; claims reconciled with the deployed system (2026-08-14 audit)
**License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

> **Plain-language summary.** Biologists have a long-standing concept called *allostatic load* — the accumulated cost an adaptive system pays for staying regulated away from its operating point. It's been theoretically useful for thirty years but hard to measure as a real-time control signal in living systems. This paper reports that a deployed AI-agent observability framework (UNITARES, in production since November 2025) records a structural analogue of allostatic load end-to-end — every ingredient of the integral is captured at each check-in — with the automatic intervention loop on it specified but not yet wired. The contribution is *structural and informational*, not biological: it tests whether the mathematical core of allostatic load survives outside its original substrate. A Lumen case study (an embodied AI agent on a Raspberry Pi) shows the framework catching a substrate-induced behavioral shift that a stale calibration anchor initially misclassified.

## Abstract

Allostatic load (McEwen and Stellar 1993) — the time-integrated cost of regulating an adaptive system away from its operating point — has been an influential theoretical construct in physiology and psychiatry for thirty years. Its mathematical core has remained, in clinical practice, difficult to test as a real-time control signal. This paper presents UNITARES, a governance framework for heterogeneous AI agent fleets in production since November 2025, as a deployed structural analogue for the mathematical core of allostatic load on a four-dimensional informational manifold. The Anima Void Integral $V_{\text{anima}}$ has its integrand recorded at every check-in, making the integral computable end-to-end over any window; its coupling to intervention is specified by the companion trajectory-identity framework but not yet wired in production. It is a control-signal analogue, not a biological or clinical allostatic-load measure.

The paper makes four bounded contributions: $V_{\text{anima}}$ as a deployed cumulative-deviation control-signal analogue; class-conditional calibration as a quantified anti-homogenization intervention, now bounded by a same-row formula-vs-calibration ablation; McEwen's Four Types as an imported but non-exhaustive failure-mode taxonomy; and a synthetic-psychology stance for generating and stress-testing informational hypotheses about adaptive systems. A Lumen case study that initially appeared Type-3-like under a stale calibration anchor is resolved by recalibration as a candidate substrate-associated basin transition. That case is provenance-backed single-agent case-report evidence for the transition's date, magnitude, and shape, and anomaly-grade for substrate causality pending artifact release, independent audit, or replication.

## Read

- **[paper.md](paper.md)** — the paper (v1.0)
- **[references.bib](references.bib)** — bibliography stub (canonical list lives in `paper.md` § References for now)
- **[CITATION.cff](CITATION.cff)** — citation metadata
- **[.zenodo.json](.zenodo.json)** — Zenodo deposit metadata (DOI minted on first stable tag)
- **[docs/submission/cover-letter-framing.md](docs/submission/cover-letter-framing.md)** — venue-agnostic cover-letter framing that keeps the manuscript in synthetic-systems / hypothesis-generation territory

## Companion artefacts

- **UNITARES governance MCP** — [CIRWEL/unitares](https://github.com/CIRWEL/unitares); paper at [CIRWEL/unitares-paper-v6](https://github.com/CIRWEL/unitares-paper-v6) (Zenodo concept [10.5281/zenodo.19647159](https://doi.org/10.5281/zenodo.19647159))
- **Trajectory identity framework (TIWD)** — Wang 2026b, Zenodo concept [10.5281/zenodo.20098168](https://doi.org/10.5281/zenodo.20098168) (v0.15); source [cirwel/trajectory-identity-paper](https://github.com/cirwel/trajectory-identity-paper)
- **EISV-Lumen benchmark** — [CIRWEL/eisv-lumen](https://github.com/CIRWEL/eisv-lumen); dataset [hikewa/unitares-eisv-trajectories](https://huggingface.co/datasets/hikewa/unitares-eisv-trajectories) (revision pinned: `aeb47055ee5f27cb93124e4e3df065301ada6909`, 2026-05-09)
- **Anima/Lumen substrate** — [CIRWEL/anima-mcp](https://github.com/CIRWEL/anima-mcp)

## Status of empirical claims

The paper contains substantial empirical content where biological theory supplies an analogy or vocabulary (basin-flip rate, envelope spread, and an apparent Type-3-like case resolved by recalibration as a basin transition) and substantial argument elsewhere (the bridge claims and methodological proposals). §1.3 gives an evidence-grade / falsifier table; §9.2 lays out the show-vs-argue balance; the appendix separates pipeline reproducibility, production-number verification, and independent validation. Reviewers should evaluate each contribution at its appropriate level of evidence.

The 28.9% basin-flip rate (§3.4) is inherited from Wang 2026a §11.6 and now has a same-row ablation in `analysis/phase-2-2026-04-18/`: production legacy → grounded fleet-wide flips 11.2%, grounded fleet-wide → grounded class-conditional flips 23.5%, and the full substitution remains 28.9%. The Lumen recalibration case study (§5.3) is original to this paper: an 86-minute window initially resembling Type 3 under the stale Phase 2 anchor, then reclassified by post-event recalibration as calibration staleness after a 2026-04-17 basin transition. The transition is case-report evidence for date, magnitude, and shape, and anomaly-grade for substrate causality pending multi-agent or multi-revision replication.

## Citation

See [CITATION.cff](CITATION.cff). Zenodo concept DOI (resolves to latest version): [10.5281/zenodo.21930092](https://doi.org/10.5281/zenodo.21930092).
