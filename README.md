# Digital Proprioception and Allostatic Load

A working implementation of the cumulative-deviation hypothesis in a deployed multi-agent system.

**Author:** Kenny Wang (Independent Researcher, CIRWEL Systems) — ORCID [0009-0006-7544-2374](https://orcid.org/0009-0006-7544-2374)
**Status:** First complete draft — v0.3, 2026-05-09
**License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

## Abstract

Allostatic load (McEwen and Stellar 1993) — the time-integrated cost of regulating an adaptive system away from its operating point — has been an influential theoretical construct in physiology and psychiatry for thirty years. Its mathematical core has remained, in clinical practice, difficult to test as a real-time control signal. We present UNITARES, a governance framework for heterogeneous AI agent fleets in production since November 2025, as a deployed instantiation of the mathematical core of allostatic load on a four-dimensional informational manifold. We make four contributions: $V_{\text{anima}}$ as a deployed allostatic-load test bed; class-conditional calibration as the cosmological-soup correction with proposals back to clinical longitudinal monitoring; McEwen's Four Types as an imported failure-mode taxonomy; and a synthetic-psychology epistemic stance in the lineage of artificial life and minimally cognitive agents.

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

The paper contains substantial empirical content where biology has parallels (basin-flip rate, Type 3 signature, envelope spread) and substantial argument elsewhere (the bridge claims, the methodological proposals). § 9.2 lays out the show-vs-argue balance explicitly; reviewers should evaluate each contribution at its appropriate level of evidence.

The 28.9% basin-flip rate (§3.4) is inherited from Wang 2026a §11.6. The Lumen Type 3 case study (§5.3) is original to this paper — an 86-minute window framed as a worked example pending longitudinal validation rather than as a measurement claim about Lumen's full 118-day operational lifetime.

## Citation

See [CITATION.cff](CITATION.cff). DOI will be minted on first stable tag via Zenodo-GitHub integration.
