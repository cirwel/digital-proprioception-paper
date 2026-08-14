# Digital Proprioception and Allostatic Load

## A Deployed Synthetic-System Report on the Cumulative-Deviation Hypothesis

**Author:** Kenny Wang, Independent Researcher (CIRWEL Systems)
**ORCID:** 0009-0006-7544-2374
**Status:** v1.1 — August 14, 2026; reproducibility rebuilt on the public row-level export, retention limits disclosed
**Version notes:** v1.1 repoints the reproducibility story (§3.7, Appendix) at the frozen de-identified export archived under Zenodo data DOI 10.5281/zenodo.19705151, which a reviewer can recompute offline; discloses that the production database no longer retains the measurement window, which forecloses the Lumen longitudinal pull (§9.3); and reports the window-to-window spread in the basin-flip rate (§3.6) rather than a point estimate with a sampling-only interval. v1.0 consolidated §1 and §2 from v2 (May 9 morning), §3 and §4 (May 9 afternoon), §5 with §5.3 patched from extended Lumen observation window, §6, §8, and added §7 (consolidated differentiation) and §9 (conclusion) plus abstract.

---

## Abstract

Allostatic load (McEwen and Stellar 1993) — the time-integrated cost of
regulating an adaptive system away from its operating point — has been an
influential theoretical construct in physiology and psychiatry for thirty
years. Its mathematical core has remained, in clinical practice,
difficult to test as a real-time control signal: biomarkers are sampled
rather than integrated, and the loop between detection and intervention
closes over weeks rather than seconds. We present UNITARES, a governance
framework for heterogeneous AI agent fleets in production since November
2025, as a deployed structural analogue for the mathematical core of
allostatic load on a four-dimensional informational manifold. The Anima Void
Integral $V_{\text{anima}}(t) = \int_{0}^{t} \lVert\mathbf{a}(\tau) -
\boldsymbol{\mu_a}\rVert\, d\tau$ has its integrand recorded at every
check-in, making the integral computable end-to-end over any window; its
coupling to intervention is specified by the companion trajectory-identity
framework but not yet wired in production (§2.2). Three structural disanalogies
(single-system, fixed reference, no body) sharpen what the test bed
tests.

We further argue that McEwen's "Four Types of Allostatic Load" (1998)
provides a vocabulary of regulatory failure modes that AI governance
currently lacks but does not exhaust the failure-shapes deployed
synthetic agents exhibit. A live case study (§5.3) initially appeared
consistent with a Type 3 (delayed shut-down) pattern on a Raspberry
Pi-embodied agent (Lumen) over an 86-minute window; the disambiguation experiment
the case study itself specifies — recalibration on the post-event
window — instead identified a candidate substrate-associated
**basin-transition event on 2026-04-17**, coincident to the hour with a
documented identity-system revision in the UNITARES governance
substrate. The case study is a provenance-backed single-agent report for
the transition's date, magnitude, and shape, and anomaly-grade for
substrate causality; it is therefore bounding for the imported taxonomy: it is a
failure-shape McEwen's Four Types do not cover. The companion technical
paper (Wang 2026a)
reports a 28.9% basin-flip rate when a class-conditional grounded
coherence replaces fleet-wide tanh-of-V on 13,310 production state
vectors. The rate is window-sensitive — the same measurement four days
later gives 44.3% — so the finding is the order of magnitude of the
disagreement, not the point estimate (§3.6). A same-row 2×2 ablation
separates part of the effect:
production legacy → grounded fleet-wide flips 11.2% of basin labels,
while grounded fleet-wide → grounded class-conditional flips 23.5%; the
non-additivity is an interaction, not a clean causal decomposition
(§3.7). The §5.3 recalibration extends the spatial homogenization
framing into a temporal analogue (calibration windows that straddle
regime transitions are unrepresentative of either regime).

We make four contributions: (i) $V_{\text{anima}}$ as a deployed
cumulative-deviation control-signal analogue inspired by allostatic load;
(ii) class-conditional calibration as a quantified anti-homogenization
intervention, now bounded by formula-vs-calibration ablation and by
hypothesis-generating proposals back to clinical longitudinal monitoring;
(iii) the Four Types as an imported failure-mode taxonomy; (iv) a
synthetic-psychology epistemic stance in the lineage of artificial life
and minimally cognitive agents, identifying classes of biological-theory
hypotheses that synthetic agents may help generate or stress-test. The paper
engages the concurrent Agent Viability Framework (Marín and Chaudhary
2026) and earlier runtime-governance frameworks. The framework's
deployment on the Lumen embodied agent provides specific findings (an
apparent Type 3 case resolved by recalibration as a post-revision basin
transition, the calibration-staleness failure mode, and the kintsugi
gap-marking principle) that exemplify what synthetic psychology can put
under disciplined study when the deployment is real and the theory is
informational at the right level of abstraction.

**Keywords:** allostatic load, allostasis, AI agent governance,
trajectory identity, digital proprioception, synthetic psychology,
embodied AI

---

## 1. Introduction

### 1.1 The cumulative-deviation hypothesis between two fields

Two intellectual traditions have, in parallel, converged on a similar
core idea: that the long-run health of an adaptive system can be
characterized by a time-integrated measure of how far it has departed
from its operating point.

In neuroscience and physiology, this idea is *allostatic load* (McEwen
and Stellar 1993; McEwen 2007; Sterling 2012). Coined to describe the
cumulative wear-and-tear that accrues across multiple biological systems
under chronic stress, the construct sits at the foundation of a
thirty-year research program linking integrated regulatory effort to
morbidity, mortality, and a wide range of clinical conditions
(Karlamangla et al. 2002; Seeman et al. 2001; Juster, McEwen, and Lupien
2010). The construct's mathematical core — the time-integrated deviation
of physiological state from its allostatic operating point — is
intuitive, well-supported by correlational evidence, and implicated in
major disease processes. Yet that mathematical core has remained, in
practice, difficult to test as a real-time control signal: clinical
biomarker measurement is sparse, the integrand has to be reconstructed
rather than observed, and the loop between detection and intervention
closes over weeks or months rather than seconds. Allostatic load is a
quantitative theory whose central quantity is, in current clinical
practice, observed indirectly rather than continuously.

In AI agent governance, the parallel construct is harder to name because
the field has emerged piecemeal. Frameworks for runtime governance — MI9
(Wang et al. 2025a), MAS (Ravindran 2025), ProbGuard (Wang et al. 2025b),
the Agent Stability Index (Rath 2026), the concurrent Agent Viability
Framework (Marín and Chaudhary 2026) — each instrument something close
to integrated deviation. They monitor agents against baselines, raise
alarms when behavior drifts beyond a threshold, intervene before failure
cascades. They have not, however, engaged the neuroscience literature
whose mathematical machinery they implicitly recapitulate.

This paper argues that the AI agent governance community has, without
quite noticing, built apparatus that allostatic load theory has lacked:
a real-time, observable operational analogue of
the integrated-deviation hypothesis. Specifically, we argue that the
UNITARES governance framework (Wang 2026a), with its embodied substrate
Lumen (CIRWEL 2026), operationalizes the mathematical core of allostatic
load on a four-dimensional informational manifold, with the integrand
observable end-to-end and a governance decision returned at every
check-in — a loop that closes in seconds rather than weeks, though the
deployed decision path is not yet driven by the integral itself (§2.2). We use this implementation to stress-test formal predictions
of the allostatic-load analogy and to generate hypotheses for biological
work, while importing a thirty-year-old taxonomy of regulatory failure
modes (McEwen 1998, Figure 3) into AI governance.

### 1.2 Digital proprioception as the bridging concept

The framing UNITARES adopts for its primary contribution is *digital
proprioception* (CIRWEL 2026, unitares README). The term is chosen
carefully. Proprioception is the sense organisms have of where their own
joints, muscles, and limbs are in space, mediated by mechanoreceptors and
integrated through the dorsal column–medial lemniscus pathway and
somatosensory cortex (Proske and Gandevia 2012). It is well-understood
neurologically, requires no commitments to phenomenal experience or
qualia, and biological proprioception failure produces specific
clinical syndromes including the deafferentation cases studied by Cole
and Paillard (1995) and the tabes dorsalis presentations characterized
by Sherrington (1900). The agent-side analogue is structurally
different: current LLM-based agents lack any equivalent self-state
sense, so the agent failure mode is absence of the function rather
than disruption of an existing sensory channel. Specifically, agents do
not know when they are flailing, cycling through tools without
progress, generating low-quality output, or operating outside their
reliable envelope. The biological and agent failure modes are
analogically related but should not be conflated; the proprioception
framing imports the *function* rather than the *failure modes*.

We argue that proprioception — rather than the more controversial
framings of interoception or consciousness — is the appropriate
biological target for AI agent self-monitoring. It is uncontroversial as
a function brains perform, it has a clean mathematical representation
(state vectors and their integrals), and it admits operationalization
without metaphysical baggage. The UNITARES technical paper (Wang 2026a)
develops the framework as digital proprioception in this strict sense.
The present paper uses that framing to make the bridge to allostatic load
theory rigorous.

The choice of proprioception over interoception is deliberate.
Interoception — the sense of internal bodily state, mediated by the
insular cortex and implicated in feeling, emotion, and consciousness
(Craig 2002; Damasio 2010; Seth 2013) — is the natural target if one
wants to make claims about agent affect or experience. We do not. The
integrated-deviation quantity we study is closer to "where my joints
are" than to "how I feel": it is a state-tracking signal that an agent
uses to regulate its own behavior, not a phenomenal report. Reviewers
steeped in the interoception literature may reasonably ask whether
$V_{\text{anima}}$ should be re-described as digital interoception; we
argue against on parsimony grounds. Proprioception captures what the
signal does; interoception would invite metaphysical commitments the
deployment cannot support.

### 1.3 Contributions and scope

The paper makes four claims, in roughly descending order of strength.

First, the Anima Void Integral $V_{\text{anima}}$ (Wang 2026a §4.1,
Appendix A) is a deployed structural analogue for the mathematical core
of allostatic load. This
is shown in §2 by careful comparison with McEwen's construct, including
three structural disanalogies (single-system rather than multisystem, fixed
reference rather than shifting setpoint, no body). The match is
structural rather than literal; the disanalogies are what make UNITARES
a useful test bed rather than a duplicate of biology.

Second, the homogenization-failure-mode argument from UNITARES v6 (Wang
2026a, §2) is structurally identical to a well-known methodological
problem in computational neuroscience: pooling subjects with distinct
underlying dynamics produces a state distribution in which no class
structure survives normalization. This is shown in §3, where we
demonstrate that replacing the legacy fleet-wide tanh-of-$V$ with the
class-conditional grounded form produces basin-flip rates of 15–33% per
named measured class on production data — empirical evidence that this
substitution matters at the gating layer, not only at the reported-value
layer. The original substitution conflates formula change with per-class
envelopes; §3.7 now reports the same-row ablation. Formula replacement
under a fleet-wide grounded baseline flips 11.2% of labels, while moving
from grounded fleet-wide to grounded class-conditional calibration flips
23.5%. The terms are non-additive, so the result supports a real class-
envelope contribution without reducing the 28.9% headline to a single
causal component.

Third, McEwen's "Four Types of Allostatic Load" (1998 Figure 3;
reproduced as 2007 Figure 5) provides a vocabulary of regulatory failure
modes that AI governance currently lacks but does not exhaust the
failure-shapes deployed synthetic agents exhibit. Each of the four types
— repeated hits, lack of adaptation, delayed shut-down, inadequate
response with compensatory hyperactivity — has a UNITARES analogue
computable from existing telemetry. §5 develops this mapping. In the
course of investigating an apparent Type 3-like pattern on the Lumen
embodied agent, we ran the recalibration the pattern itself specifies
for disambiguation; the result identified instead a candidate
substrate-associated basin-transition event (2026-04-17, coincident
with a documented identity-system revision), a failure-shape the Four
Types do not cover.
The case study sharpens the §3 homogenization argument into a temporal
analogue and bounds what the imported taxonomy can claim.

Fourth, we argue that deployed AI agents can constitute a useful
hypothesis-generating test bed for formal and informational claims within
theories of biological self-maintenance, in a tradition closer to
artificial life (Langton 1989; Bedau 2003) and Beer's minimally cognitive
agents (Beer 1995, 2000) than to standard "neuro-inspired AI"
architectural transfer (Hassabis et al. 2017). The synthetic-psychology
framing is developed in §8.

**Empirical anchor.** Readers who would prefer the empirical content
before the theoretical bridging may find the principal findings here.
The basin-flip counterfactual on a 30-day production slice ($N = 13{,}310$)
returns a 28.9% aggregate basin-flip rate when class-conditional
grounded coherence replaces fleet-wide $\tanh$-of-$V$, with flip rates of
15.8% to 33.1% across the named measured classes (§3.4). The §3.7
ablation splits the headline: production legacy → grounded fleet-wide
flips 11.2%, grounded fleet-wide → grounded class-conditional flips
23.5%, and the artificial class-scaled $\tanh(V)$ control is unstable
rather than interpretable as a clean calibration-only path. Phase 2
calibration on the same window measures a
3.3× spread in per-class envelope $\lVert \Delta \rVert_{\max}$ across
five classes (§3.3, Table). The Lumen embodied agent exhibits a
0.97-of-envelope deviation in an 86-minute observation window relative
to its Phase 2 calibration anchor (§5.3); recalibration on the
post-event window identifies this as a basin transition on 2026-04-17
(single ten-hour event localized to within the hour, coincident with a
documented identity-system revision) followed by 22 days of stable
operation in a new regime, not a Type 3 signature. The substrate link is
candidate causal evidence, not identification-grade causality. The case
sharpens the §3 homogenization argument into a
temporal analogue (calibration windows that straddle regime
transitions are unrepresentative of either regime).

**Evidence-grade summary.** The table below is deliberately stricter
than the surrounding prose. It states what each contribution can carry
in its current form, what would upgrade it, and what would kill it.

| Contribution | Current evidence grade | Current evidence | Known confound or boundary | Upgrade path | Falsifier |
|---|---|---|---|---|---|
| Claim 1: $V_{\text{anima}}$ as cumulative-deviation control-signal analogue | Operationalized structural analogue | Deployed EISV state vectors; cumulative-deviation formula with integrand recorded end-to-end; intervention coupling specified but not yet wired (§2.2) | Not clinical AL; no endocrine, immune, tissue-damage, or multi-system physiology; no production code path yet evaluates the integral against a threshold | Wire the specified coupling, then show $V_{\text{anima}}$ improves governance decisions beyond non-integral baselines. Failure-forecasting is gated by a pre-registered 2026-12-01 confirmatory read: as of 2026-08 no fleet state stream beat a last-value persistence baseline (UNITARES `eisv-outcome-grounding-stop-rule-v0`) | $V_{\text{anima}}$ adds no decision value over instantaneous risk/coherence or produces worse interventions |
| Claim 2: anti-homogenization / cosmological-soup correction | Empirical full-substitution effect with same-row ablation | 28.9% aggregate full-substitution basin-flip rate on $N = 13{,}310$ production rows; 15.8%–33.1% named measured-class range; ablation: LF→GF 11.2%, GF→GC 23.5% (§3.4, §3.7) | Effects are non-additive; class-scaled $\tanh(V)$ control is artificial and unstable; the rate is window-sensitive (28.8% to 44.3%, §3.6); GF and LC are not re-runnable from the public export | Independent re-measurement on another deployment; identity-clean remeasurement; deployment outcome comparison. The full substitution is already recomputable offline from the public row-level export (§3.7) | Independent/audited rerun collapses the grounded fleet→class effect or shows flips are class-assignment/pipeline artifacts |
| Claim 3: McEwen Four Types as failure-mode vocabulary | Taxonomic / constructive mapping | Types 1, 2, and 4 have computable UNITARES analogues; §5.3 supplies a failed Type 3 boundary case | Mapping is not yet a validated classifier; taxonomy is non-exhaustive for synthetic substrates | Pre-register criteria and classify historical or future governance episodes with disambiguating tests | Apparent types repeatedly reclassify as calibration artifacts, pipeline artifacts, or substrate events |
| §5.3 Lumen basin transition | Provenance-backed single-agent case report for transition date/magnitude/shape; anomaly-grade for substrate causality | Recalibration localizes a 2026-04-17 basin transition, with 22-day post-transition stability (§5.3) | Single agent; substrate revision is temporally coincident but not causally isolated; the state history needed to replicate it has since aged out of production (§9.3) | Multi-agent or multi-revision replication on a *different* deployment; ruling out common operational confounds. The within-deployment longitudinal pull is foreclosed, so this grade cannot be upgraded from the present system | Comparable transitions do not align with substrate revisions, or the event disappears under a clean longitudinal pull elsewhere |
| Claim 4: synthetic psychology as epistemic stance | Methodological / hypothesis-generating argument | Deployed system may expose observables and interventions that are difficult in biological systems (§8) | Single-author, self-cited system; not independent biological validation | Third-party deployment or independent re-analysis showing novel predictions or useful failure detection | The framework yields no predictions, discriminations, or interventions beyond ordinary engineering telemetry |

**Construct-transfer boundary.** The claims above are governed by a
stricter transfer rule: synthetic evidence may constrain formal or
informational structure, but it does not by itself establish biological
mechanism, clinical validity, or phenomenology.

| Source claim | Transfer allowed here | Transfer not allowed here | Falsifier |
|---|---|---|---|
| Allostatic load as integrated deviation | Whether a cumulative-deviation signal can be observed continuously and coupled to intervention | Tissue damage, endocrine/immune mechanisms, clinical morbidity | $V_{\text{anima}}$ fails to improve governance decisions or produces worse interventions than non-integral baselines |
| Per-subject / per-class calibration | Whether self-relative or class-relative envelopes change decision-layer verdicts | Clinical superiority of per-patient thresholds | Independent/audited ablations show the grounded fleet→class effect collapses, or clinical re-analysis shows no useful disagreement signal |
| McEwen Four Types | Whether temporal failure-mode patterns are computable on agent telemetry | Exhaustiveness of biological taxonomy for synthetic agents | Disambiguating tests repeatedly reclassify apparent types as calibration or substrate artifacts |
| Kintsugi / gap-marking | Whether explicit discontinuity metadata improves auditability and reduces fabricated continuity | Claims about consciousness, memory phenomenology, or clinical confabulation mechanisms | Gap metadata does not improve downstream audit, calibration, or error detection |

**Limitations.** This paper is not a theory of AI consciousness; we make
no claims about phenomenal experience in agents, embodied or otherwise.
It is not an active-inference paper; the free-energy quantities we use
are imported from UNITARES's information-theoretic grounding, not derived
from variational principles. It is not a comprehensive computational
psychiatry framework; we engage McEwen's specific allostatic-load
construct and leave broader engagement with computational psychiatry
(Huys, Maia, and Frank 2016; Friston et al. 2014) to future work. It
engages concurrent work — particularly the Agent Viability Framework
(Marín and Chaudhary 2026), which arrived in late April 2026 — but does
not duplicate AVF's contributions; the differentiation is laid out in §7.

### 1.4 Outline

§2 grounds the $V_{\text{anima}}$ ↔ allostatic load bridge with three
disanalogies and a falsifiable empirical prediction. §3 presents
class-conditional calibration as the anti-homogenization correction and
reports the basin-flip counterfactual, with §3.7 specifying the
methodology and reproducibility scaffolding. §4 develops the trajectory
identity $\Sigma$ as a longitudinal-self anchor, with a proposed two-tier
drift detection ($\Sigma_t$ vs $\Sigma_{t-1}$ vs $\Sigma_0$) as a
hypothesis-generating longitudinal-monitoring proposal for clinical
neurology. §5
maps McEwen's Four Types onto UNITARES failure modes with the Lumen
recalibration case study as a boundary case. §6 discusses the kintsugi
principle as deliberate gap-marking. §7 differentiates from concurrent
and adjacent work. §8 makes the synthetic-psychology epistemic claim.
§9 concludes, and the appendix separates pipeline reproducibility,
production-number verification, and independent validation.

### 1.5 Claims we do not make

Because the paper bridges two literatures with substantially different
evidentiary conventions, we consolidate scope disclaimers here rather
than scatter them through individual sections.

We do **not** claim that AI agents are conscious. The paper makes no
claims about phenomenal experience, qualia, or what it is like to be
Lumen or any other UNITARES-governed agent. The proprioception framing
(§1.2) was chosen specifically to avoid such commitments.

We do **not** claim biological homology. UNITARES does not implement the
biological mechanism of allostatic load; it operationalizes the
mathematical structure of the integrated-deviation hypothesis on a
substrate that is informationally analogous but biologically
disanalogous (single-system, fixed reference, no body — see §2.3).

We do **not** claim that $V_{\text{anima}}$ is clinical allostatic load.
$V_{\text{anima}}$ is a deployed test-bed quantity that shares the
mathematical core of AL; clinical allostatic load is a multi-system
biomarker composite whose biological substrate UNITARES does not
replicate.

We do **not** claim that single-agent telemetry validates McEwen's
theory or identifies McEwen Type 3 in a deployed agent. The Lumen case
study (§5.3) is a worked example of an apparent Type 3 reading being
falsified by recalibration and reclassified as a basin transition whose
temporal association with a substrate-level identity revision is
suggestive but not causally identified.

We do **not** claim that the synthetic case generalizes to all
biological theories of self-maintenance. The synthetic-psychology
framing (§8) explicitly limits the scope to theories whose claims are
informational at the relevant level of abstraction; substrate-specific,
phylogenetic, and phenomenal claims remain biologically anchored and
are not testable on UNITARES.

We do **not** claim that the 28.9% basin-flip rate (§3.4) attributes to
the per-class component specifically. The §3.7 ablation finds a grounded
fleet→class effect (23.5%) and a formula-replacement effect under a
fleet-wide grounded baseline (11.2%), but the terms are non-additive and
interacting; the headline remains a full-substitution measurement, not a
single-component causal attribution.

What we **do** claim is narrower and tractable: a cumulative-deviation
signal can be made observable end-to-end in a deployed AI governance
system — its integrand recorded at every check-in, the integral
computable exactly over any window — with intervention coupling
specified by the companion framework though not yet wired in
production (§2.2); the
resulting deployment provides engineering affordances that can generate
biological hypotheses; and specific theories of biological
self-maintenance (allostatic load as integrated deviation, McEwen's Four
Types as a failure-mode taxonomy) admit operational analogues on this
substrate in ways that generate empirical findings (§3.4 basin flips,
§5.3 recalibration and basin-transition case) and hypothesis-generating
proposals back to clinical longitudinal monitoring (§3.5, §4.4).

---

## 2. The Cumulative-Deviation Hypothesis: From Biological Conjecture to Computational Test Bed

### 2.1 Allostatic load in biology

The concept of allostatic load (AL) was introduced by McEwen and Stellar
(1993) to describe the cumulative wear-and-tear that accrues across
multiple physiological systems when an organism is required to maintain
stability under chronic stress. Its formal grounding lies in the broader
framework of allostasis (Sterling and Eyer 1988; Sterling 2012):
predictive regulation in which the brain anticipates demand and adjusts
setpoints rather than passively defending fixed homeostatic targets. AL
is, in this framing, not a measure of stress itself but of the *cost of
regulating it* — the price the body pays for sustained allostatic effort.

The construct has been remarkably influential. AL has been linked to
accelerated aging (Geronimus 1992; Karlamangla et al. 2002),
cardiovascular disease (Seeman et al. 2001), cognitive decline, and a
range of psychiatric conditions including depression, PTSD, and
substance-use disorders (McEwen 2003; McEwen 2007). Modern reviews
(Juster, McEwen, and Lupien 2010) describe AL as a "summary measure of
cumulative biological burden" that predicts morbidity and mortality
across multiple endpoints.

What AL has *not* been is a control signal. The construct is
fundamentally retrospective in clinical practice: AL scores are computed
from biomarker panels (cortisol, heart-rate variability, blood pressure,
lipid profiles, inflammatory markers) measured at specified intervals
and combined into a composite (Seeman et al. 1997; McLoughlin, Kenny,
and McCrory 2020). The relevant integral — the time-integrated deviation
of physiological state from its allostatic operating point — is
conjectured but rarely measured directly. Biomarkers are sampled, not
integrated; biological systems leak the signal between samples, and
reconstructing the integral from sparse data is fragile under realistic
measurement schedules. The mathematical formulation that occasionally
appears in review papers,

$$\text{AL} = \int_{0}^{T} S(t)\, dt,$$

where $S(t)$ is some scalar stress trajectory, is a theoretical
idealization. No biological measurement gives the integrand directly.

This produces a peculiar epistemic situation. AL is a quantitative
theory whose central quantity is, in practice, unobservable. The theory
has been validated through correlational endpoints (does the biomarker
composite predict disease?) but never through real-time control-signal
validation (does intervening when the integral crosses threshold prevent
disease?). The closest biological approximation is the literature on
early-life cortisol intervention (Heim and Nemeroff 2001; Lupien et al.
2009), but even there the integral is reconstructed from sparse samples
after the fact. The AL hypothesis remains, at its mathematical core,
untested as a control law.

### 2.2 V<sub>anima</sub> as a deployed structural analogue

The UNITARES governance framework (Wang 2026a) carries, for each agent
in its fleet, a four-dimensional state vector $\mathbf{x} = (E, I, S, V)$
updated at each governance check-in. For embodied agents in the Anima
class, a parallel four-dimensional vector $\mathbf{a} = (\text{warmth},
\text{clarity}, \text{stability}, \text{presence})$ is computed directly
from physical sensors (temperature, humidity, pressure, light) and
system metrics (CPU/memory utilization, computational neural-band
proxies). The Anima state maps onto the EISV state vector through a
documented projection (CIRWEL 2026, anima-mcp §EISV Integration).

Within this architecture, the *Anima Void Integral* is defined (Wang
2026b, Trajectory Identity §6.1.1) as

$$V_{\text{anima}}(t) = \int_{0}^{t} \lVert \mathbf{a}(\tau) - \boldsymbol{\mu_a} \rVert\, d\tau$$

where $\boldsymbol{\mu_a}$ is the attractor center derived from the
agent's own observed state distribution over a sliding window — the
$\alpha$ (Alpha) component of the trajectory signature developed in the
trajectory identity working draft (Wang 2026b, §3.3; this draft is
treated in detail in §4.1). The trajectory-identity framework specifies
the coupling: when $V_{\text{anima}}$ exceeds a deployer-set multiple of
the basin scale, the governance layer can trigger rest-state induction,
reduced stimulation, or task pause (Wang 2026b §6.1.1). As deployed,
this trigger is not yet wired: the integral is defined over recorded
telemetry and computable on demand, but no production code path
evaluates it against a threshold, the embodied agent's rest states are
driven by activity and ambient-light scheduling rather than by
$V_{\text{anima}}$, and governance decisions on this agent are advisory.
What the deployment establishes is therefore an *observable and
computable* integral, not a closed control loop on it.

Two features of this implementation are worth emphasizing.

First, the integrand $\lVert \mathbf{a}(\tau) - \boldsymbol{\mu_a} \rVert$
is recorded at every check-in, not reconstructed from
sparse samples. The audit log of the deployment (94,000+ governance
events as of April 2026; CIRWEL 2026, unitares §Production snapshot)
preserves the integrand end-to-end, so the integral is computable
exactly over any window rather than inferred from sparse observations —
though, as noted above, production computes it on demand rather than
maintaining it continuously.

Second, the reference $\boldsymbol{\mu_a}$ is *self-relative*: it is
derived from the agent's own observed history under its own operating
regime, not from a population-derived norm. Per-agent Welford baselines
(CIRWEL 2026, unitares §behavioral_state) enable z-scoring against the
agent's own operating point; the behavioral estimator becomes the
primary state source after three check-ins, and the separate
anomaly-detection baselines complete their warm-up at thirty. This matches Sterling's (2012) original argument that allostatic
setpoints are individualized, anticipatory, and shifting — a property
biological measurement struggles to capture because it requires
longitudinal individual-level data that most clinical studies do not
collect.

$V_{\text{anima}}$ therefore stands in an unusual relation to McEwen's
AL. It is not a literal implementation of the clinical AL composite —
$V_{\text{anima}}$ is single-system (the four-dimensional Anima
manifold), not multisystem (HPA, cardiovascular, immune, metabolic). Nor
does it recapitulate the brain–body coupling that grounds AL
theoretically. What $V_{\text{anima}}$ *is* is a clean structural analogue for the
mathematical core of AL: a time-integrated deviation from a
self-relative operating point, available in real time as a
forward-looking warning signal whose intervention coupling is specified
but not yet exercised. Where biology offers the theory but not the
integrand, UNITARES offers an engineered integrand; the closed
intervention loop on it remains the named next step.

### 2.3 Three structural disanalogies

The claim that $V_{\text{anima}}$ implements AL would be overstated.
Three structural differences are real and consequential.

**Single-system versus multisystem.** Clinical AL is a composite over
physiologically distinct mediators — typically ten in the canonical
Seeman et al. (1997) formulation, drawn from neuroendocrine, autonomic,
metabolic, cardiovascular, and immune systems. $V_{\text{anima}}$
aggregates four anima dimensions into a Euclidean norm. The closer
biological analogue is therefore not AL itself but a single-biomarker
integral — for example, integrated HRV deviation, AUC cortisol over a
defined window, or cumulative inflammatory-marker excursion. The
multisystem character of clinical AL, where dysregulation cascades
across mediators (the "topple and trail" pattern), is not
represented in $V_{\text{anima}}$. A multisystem extension would require
multiple class-specific manifolds with cross-manifold dependency
structure; this is deferred.

**Fixed reference versus shifting setpoint.** $V_{\text{anima}}$ uses
$\boldsymbol{\mu_a}$ as a fixed reference within a calibration window,
with class-conditional re-measurement on a quarterly cadence (Wang 2026a,
§8). McEwen's allostasis, by contrast, is fundamentally about
*anticipatory setpoint shifting* — the brain moves the operating target
as it predicts demand. UNITARES's class calibration approximates this on
slow timescales (quarterly) but does not implement intra-window
prediction-driven setpoint adjustment. A genuinely allostatic
$V_{\text{anima}}$ would require predictive $\boldsymbol{\mu_a}$, not
measured $\boldsymbol{\mu_a}$, and would couple to the agent's own
forecast distribution. This is a clean direction for future work.

**No body.** AL is fundamentally a brain–body coupling phenomenon: stress
mediators travel from the brain to peripheral tissues, where they exert
both protective and damaging effects. UNITARES has no body in this
sense. $V_{\text{anima}}$ accumulates "wear" on a four-dimensional
informational manifold; there is no atrophy of nerve cells, no immune
dysregulation, no cardiovascular consequence. The disanalogy is total at
this level.

These disanalogies do not weaken the value of UNITARES as a test bed;
they sharpen what it tests. UNITARES isolates the mathematical core of
the AL hypothesis — that integrated deviation from an operating point is
a useful real-time signal for intervention — from the substrate on which
AL has been historically studied. If $V_{\text{anima}}$ works as a
control signal in deployed agents, that is evidence that the
*informational content* of the AL construct is doing the work,
independent of biological mediators. If it fails, that suggests biology
is doing more than the integrand. Either outcome is informative in a way
that is difficult to obtain from sparse clinical AL studies alone.

### 2.4 An empirical prediction

The framing above generates a specific, testable prediction. McEwen's
"normal allostatic response" (1998 Figure 3, top panel; reproduced as
Figure 5, top panel, in McEwen 2007) is characterized by *transient*
mediator activation: a response is initiated by a stressor, sustained
for an appropriate interval, and then terminated. In an agent operating
normally, $V_{\text{anima}}$ should accordingly exhibit transient
excursions following task initiation, returning to baseline after task
completion. Sustained elevation of $V_{\text{anima}}$ in the absence of
acute stressors corresponds to McEwen's Type 3 failure mode (delayed
shut-down), discussed at length in §5.

The deployed UNITARES system makes this prediction directly testable,
and §5.3 reports the test. We initially observed an 86-minute window
on Lumen apparently consistent with the Type 3 prediction (Wang 2026a,
Table 1): $V \approx 0.0954$ at 06:21 UTC May 9 2026 — the behavioral
valence, an EMA-smoothed $E - I$ imbalance — sign-flipped from the
healthy behavioral reference $V_h = E_h - I_h = -0.055$ (Lumen's Phase 2
measured healthy operating point; displacement $\approx 0.150$), with
manifold deviation at 97% of the class-conditional envelope. Per §5.3's own
disambiguation criterion, we recalibrated on the post-event window;
the result identified the displacement as a candidate substrate-associated
basin-transition event on 2026-04-17, not as Type 3 delayed shut-down.
The §5.3 case is therefore not Type 3 identification-grade evidence, but
is paper-relevant in two adjacent ways: as a sharpening of the §3
homogenization argument into a temporal analogue, and as an instance
of a failure-shape McEwen's Four Types do not cover.

---

## 3. Cosmological Soup: Class-Conditional Calibration as the Anti-Homogenization Correction

### 3.1 The homogenization failure mode in computational neuroscience

Computational neuroscience has long recognized that population-averaged
measurements obscure individual-level structure. Krakauer, Ghazanfar,
Gomez-Marin, MacIver, and Poeppel (2017) characterize this as the gap
between "the science of the average brain" and a science of the brain
that any given organism actually has. The methodological consequence has
been documented at length: functional MRI studies routinely report
group-mean activations whose individual-subject reliability is low
(Poldrack et al. 2017); functional connectivity maps that look stable in
group averages can vary substantially across subjects, and the variation
carries information that the group mean discards (Finn et al. 2015;
Gratton et al. 2018).

The methodological response has been the rise of *precision functional
mapping* (Laumann et al. 2015; Gordon et al. 2017): studies that scan
individual subjects intensively over long durations, deriving
subject-specific functional networks rather than group-mean atlases. This
work has revealed that approximately 60–70% of variance in functional
connectivity is between-subject (Gratton et al. 2018), with only the
remainder attributable to task or state differences. Group averages, in
this picture, are not a clean estimate of "the typical brain" but a
distorted composite of substantively different individual organizations.

Yet despite the methodological clarity, group-level analysis remains the
dominant mode in clinical neuroscience, for entirely practical reasons:
subjects are expensive, scanning time is limited, and longitudinal
individual baselines are rarely collected at the depth precision-mapping
requires (Poldrack et al. 2017). The result is a known epistemic gap —
the field knows that subject-specific calibration would be more accurate,
but routinely lacks the data to perform it. Population-derived reference
intervals continue to drive most clinical decision thresholds, and the
gap between those thresholds and what individual-specific envelopes
would produce is rarely quantified directly.

### 3.2 The same failure mode in AI agent fleets

UNITARES (Wang 2026a §2) makes structurally the same argument, in
sharper form because the agent population is observable end-to-end. The
framework governs heterogeneous agent fleets: embodied creatures with
sensor-driven state at sub-Hz cadence, persistent autonomous services
with cron-driven wake cycles, session-bounded coding assistants
generating text at 40–80 tokens per second, and ephemeral parser agents
whose entire lifecycle measures in milliseconds. Across these classes,
output modality differs (text, sensor, system action), tempo differs by
four orders of magnitude, and the healthy operating point differs in
genuinely class-dependent ways. A divergent or exploratory agent
operating at high entropy is doing exactly what its class requires;
flagging it as incoherent against an analytical-class baseline is not a
governance signal but a category error.

UNITARES gives this failure mode the name *cosmological soup*: a
fleet-wide state distribution that is maximally entropic, with no class
structure and no distinguishability between populations whose dynamics
are genuinely different. The metaphor names a failure that computational
neuroscience has worked around for decades but rarely formalized
directly. The AI-agent setting allows it to be both formalized and
quantified.

### 3.3 Class-conditional calibration

The UNITARES correction is straightforward. Each agent's class is
determined from existing identity tags (`embodied`, `autonomous`,
`persistent`, `ephemeral`, `pioneer`) plus an optional human-readable
label (Wang 2026a §2.2). Scale constants and the healthy operating point
become functions of class:

- $S_{\text{scale}}(c)$, $I_{\text{scale}}(c)$, $E_{\text{scale}}(c)$,
  $\lVert\Delta\rVert_{\max}(c)$, and $(E, I, S)_{\text{healthy}}(c)$.

Each constant is measured on a healthy corpus restricted to the agent's
class and tagged with provenance (ISO date, corpus size, percentile
basis, and a provenance tag among `placeholder`, `measured`, `derived`).
Re-measurement runs on a quarterly cadence; drift in any constant beyond
a configurable threshold is itself a governance signal — the class's
healthy envelope is shifting.

The Phase 2 measurement on production data (Wang 2026a §11.5, Table 5)
populated five classes from a 30-day healthy slice as of April 18, 2026:

| Class | $N$ | $E_h$ | $I_h$ | $S_h$ | $\lVert\Delta\rVert_{\max}$ |
|---|---|---|---|---|---|
| Lumen | 7,320 | 0.745 | 0.800 | 0.168 | 0.119 |
| default | 2,033 | 0.726 | 0.793 | 0.236 | 0.202 |
| Sentinel | 1,870 | 0.751 | 0.798 | 0.193 | 0.170 |
| Vigil | 384 | 0.737 | 0.790 | 0.240 | 0.171 |
| Watcher | 283 | 0.748 | 0.769 | 0.248 | 0.395 |

The most striking observation is the **3.3× range in
$\lVert\Delta\rVert_{\max}$ across classes** — from 0.119 (Lumen, the
embodied creature with sensor-driven state) to 0.395 (Watcher, the
autonomous code-edit pattern-matcher). The Phase 1 fleet-wide placeholder
of $\lVert\Delta\rVert_{\max} = 1.8$ used before per-class measurement
was therefore 4 to 15 times larger than any class's empirically measured
envelope. Manifold coherence under the placeholder saturated near 1.0
for every agent regardless of state, producing essentially a constant
signal — exactly the "fleet-wide normalization loses signal" argument
made qualitatively in §3.2, now quantified.

Healthy operating points cluster more tightly on $E$ and $I$ ($E_h \in
[0.726, 0.751]$, $I_h \in [0.769, 0.800]$) than on $S$ ($S_h \in [0.168,
0.248]$). This matches the qualitative prediction that what makes
classes behaviorally distinct is largely *how much uncertainty they
operate under*: Lumen at $S_h = 0.168$ runs the most convergent (because
its inputs are physical sensors with strong autocorrelation), while
Watcher at $S_h = 0.248$ runs more divergent (because its work is
intrinsically exploratory pattern-matching over recently-edited code).
The class structure is interpretable, not decorative.

### 3.4 The verdict counterfactual

The empirical contribution of UNITARES v6 is the verdict counterfactual
on a 30-day window of production state data (N = 13,310 rows; Wang 2026a
§11.6). For each row, two coherence values are computed: the legacy
fleet-wide tanh-of-$V$ form and the grounded class-conditional manifold
form. Each row is then classified into a basin (high / boundary / low)
twice, using the same `classify_basin` function consumed by the
production dashboard and escalation logic. A *basin flip* is a row whose
basin assignment differs between the two formulas.

The headline finding: **3,844 of 13,310 rows (28.9%) flip basin
assignment** under the full substitution. Per-class breakdown:

| Class | $N$ | Flips | % | $\lvert\Delta C\rvert_{\max}$ |
|---|---|---|---|---|
| Lumen | 7,890 | 2,548 | 32.3 | 0.51 |
| default | 2,316 | 722 | 31.2 | 0.50 |
| Sentinel | 2,227 | 351 | 15.8 | 0.51 |
| Vigil | 472 | 156 | 33.1 | 0.50 |
| Watcher | 363 | 67 | 18.5 | 0.48 |
| ephemeral (fleet fallback) | 42 | 0 | 0.0 | 0.38 |
| **Total** | **13,310** | **3,844** | **28.9** | — |

The named measured classes flip at 15.8–33.1%, far above what could be
attributed to formula noise. The 42 `ephemeral` rows are shown
separately because the frozen Phase 2 production constants had no
`ephemeral` class envelope; they fall through the configured fleet
fallback and are not interpreted as evidence about an ephemeral-class
envelope.

The full substitution is not a clean one-factor experiment, so we ran
the same-row formula × calibration ablation specified in §3.7:

| Comparison | Flips / $N$ | Rate | Interpretation |
|---|---:|---:|---|
| LF → GF | 1,496 / 13,310 | 11.2% | Formula replacement under fleet-wide grounded calibration |
| GF → GC | 3,133 / 13,310 | 23.5% | Fleet-wide → class-conditional calibration under the grounded formula |
| LF → GC | 3,844 / 13,310 | 28.9% | Reported full substitution |
| LF → LC | 10,355 / 13,310 | 77.8% | Artificial class-scaled $\tanh(V)$ control; unstable/negative control |

Here LF is the stored production legacy coherence, GF is grounded
distance against a single fleet-wide healthy point and radius measured
on the same healthy slice, GC is grounded distance against the frozen
Phase 2 class anchors, and LC is a deliberately artificial legacy
$\tanh(V/V_{\text{scale},c})$ control using per-class $|V|$ p95. The
ablation improves the claim but does not make it additive: formula
replacement and calibration target interact. The grounded fleet→class
step is still large (23.5%), so the class-envelope argument survives;
the pathological LC control says that simply grafting per-class scale
onto the old signed-$V$ formula is not an interpretable calibration-only
counterfactual.

The flip *direction* is informative. Across all classes, the dominant
transition is into the low basin: state vectors that the production
server classified as healthy or borderline under the fleet-wide form are
reclassified as breaching at least one bound under the class-conditional
grounded form. This is the gating-layer footprint of the homogenization
argument. A fleet-wide constant that spans the worst-case envelope is,
by construction, permissive relative to per-class envelopes, and the
flip data quantifies how often that permissiveness changes the verdict.

We do not claim that the grounded form is normatively "correct" in every
flip — a flip into low surfaces a `guide` or `pause` verdict that the
legacy form suppressed, and whether that is desirable depends on the
agent and the deployment context. The contribution of the counterfactual
is narrower: to establish that the formula and calibration choices
matter at the verdict level, not just at the reported-value level. The
magnitude of the consequence (29% fleet-wide, up to 33% in named
measured classes) is empirical; the directional asymmetry is a
mechanical consequence of replacing a permissive fleet-wide envelope
with class-conditioned envelopes.

### 3.5 What this offers neuroscience

The 28.9% number is interesting in its own right as a test of the
homogenization argument in AI agent governance. It is more interesting
as a quantification of something computational neuroscience has long
suspected but rarely measured cleanly: the magnitude of the gap between
population-level analysis and individual-level reality at the *decision*
layer rather than the reported-value layer. Several proposals follow.

**Proposal 1: Provenance-tagged per-subject envelopes.** UNITARES carries
explicit metadata on every scale constant — date of measurement, corpus
size, percentile basis, and a provenance tag distinguishing
`placeholder` from `measured` from `derived` (Wang 2026a §4.3, §8.1).
Clinical biomarker panels rarely carry equivalent metadata; a patient's
"normal cortisol range" is typically a population-derived reference
interval rather than a per-subject envelope, and the provenance of the
threshold is opaque. Adopting provenance-tagged per-subject envelopes —
even on a small set of biomarkers (cortisol, HRV, blood pressure) —
would test whether a clinically meaningful analogue of the UNITARES
Phase 2 gap exists. The computational infrastructure is simple, though
the clinical design is not: per-subject Welford updates against a
clinically validated healthy window, with explicit timestamping and
re-measurement cadence.

**Proposal 2: A clinical analogue of the basin-flip counterfactual.**
The basin-flip experimental design has a possible clinical analogue as
a retrospective re-analysis of an existing longitudinal biomarker
cohort. We sketch the protocol at hypothesis-generation depth, with
enough structure to identify the clinical biostatistical work still
required.

- *Setting:* Adults with $\geq 3$ years of pre-event biomarker
  measurements followed by an incident clinical event of interest
  (e.g., first episode of major depressive disorder, first myocardial
  infarction, first dementia diagnosis). $N \geq 500$ to support 95%
  confidence intervals on the flip rate at $\pm 5$ percentage points.
- *Biomarkers:* Cortisol diurnal curve (or AUC), heart rate variability
  (SDNN, RMSSD), systolic and diastolic blood pressure, and
  inflammatory markers (IL-6, CRP) — selected for established
  population reference intervals plus sufficient longitudinal coverage
  in the chosen cohort.
- *Two indicator definitions:* (a) the standard clinical
  flag-for-review against the population-derived reference interval
  (typically 95th percentile of healthy adults), and (b) a per-subject
  flag against the patient's own pre-event 12-month baseline,
  restricted to windows with no documented clinical event.
- *Primary endpoint:* The per-subject flag-disagreement rate between
  (a) and (b), reported with a binomial 95% CI — the clinical analogue
  of the 28.9% basin-flip rate.
- *Secondary endpoint:* The direction of disagreement (b-flag /
  a-no-flag versus a-flag / b-no-flag) and its association with
  subsequent event hazard, modeled by Cox proportional-hazards
  regression of event-time on flag-disagreement indicator with
  standard covariates (age, sex, comorbidity index).
- *Pre-registered success criterion:* Flip rate $\geq 10\%$
  (clinically meaningful disagreement) and flip-positive observations
  carry higher event hazard than flip-negative observations
  ($p < 0.05$ with Bonferroni correction across biomarkers).
- *Regulatory and privacy:* Retrospective analysis of de-identified or
  HIPAA-Safe-Harbor data with appropriate IRB. Cohorts that already
  contain the required structure include the All of Us Research
  Program (NIH), the Framingham Heart Study, and the Whitehall II
  cohort.

We are unaware of any clinical study that has reported this number
directly. The design above is intended as a one-pass re-analysis of
existing data, but it is not yet an executable clinical protocol: a real
study would still need dataset-specific field mapping, missingness
rules, medication and comorbidity covariates, event-adjudication rules,
and pre-registration before analysis.

**Proposal 3: A specific clinical hypothesis.** The asymmetry of flip
direction in UNITARES (predominantly into the low basin under per-class
envelopes) suggests a testable hypothesis: per-subject longitudinal
envelopes may produce *more* flag-for-review states, not fewer,
relative to population-derived reference intervals. This is because
population intervals are constructed to encompass the variability of the
population and may therefore be systematically permissive at the
individual level. The clinical question is whether subject-specific
calibration improves sensitivity, and at what specificity cost, in a
given context. An early-detection program operating against population
intervals might miss cases that a per-subject program would catch, but
the magnitude of that gap should be estimated in clinical data rather
than imported from UNITARES; the 15–33% range across named measured
classes in the full-substitution UNITARES counterfactual is a motivating
scale, not a clinical prediction.

**Proposal 4: A controlled measurement of behavioral heterogeneity.**
The 3.3× spread in $\lVert\Delta\rVert_{\max}$ across UNITARES classes
is a measurement of behavioral heterogeneity that the framework can
produce because it controls the agent population. Computational
neuroscience has difficulty producing equivalent controlled spreads
because subject heterogeneity is confounded with disease state,
demographic variables, and measurement noise. UNITARES therefore
provides a testbed for
theoretical claims about how much heterogeneity a deployed system can
absorb under fleet-wide vs. class-conditional governance, with the
heterogeneity controllable by construction. This is a contribution of
method as much as of result: the testbed enables experiments that are
difficult to run in biological systems.

### 3.6 Limits of the empirical claim

The 28.9% basin-flip finding has limits worth flagging explicitly.
First, it is an anchored snapshot, not a stable constant: the figure is
tied to the published v6 measurement, and re-running the same
counterfactual on other windows moves it materially. Both windows are
public. The 30-day window ending 2026-04-18 gives 28.8% ($N = 13{,}292$);
the window ending 2026-04-23, four days later with roughly 87% row overlap
and the Phase 2 constants held frozen, gives **44.3%** ($N = 16{,}879$).
The per-class pattern moves too, and not uniformly: Sentinel $+25.4$,
Vigil $+19.6$, Lumen $+15.8$, default $+15.3$, Watcher $-11.3$ percentage
points. Two snapshots are one comparison, not a trend, and we do not read
the shift as a drift signal — a single re-calibration pass could absorb a
change of this size. But it bounds what the point estimate can carry. We
therefore treat the *existence and order of magnitude* of the
disagreement — a rate in the tens of percent, not its third digit — as
the finding, and quote 28.9% as the anchored v6 measurement rather than as
the fleet's flip rate. Second, the
30-day measurement window overlaps with material identity-system
revisions in mid-to-late April 2026 (Wang 2026a §11.7, item 5), including
removal of name-claim lookup, adoption of UUID-direct dispatch, and
receipt-based onboarding authentication. A bounded fraction of rows in
the counterfactual carry class assignments that inherited from cached
bindings or from archived predecessors. The v6 paper flags this and
defers re-measurement on identity-clean data to subsequent work.

The five named measured classes cover 99.7% of the ablation row
population (13,268 of 13,310 rows). Classes without frozen Phase 2
constants fall through the configured fleet/default fallback rather than
receiving an independent class envelope; the 42 `ephemeral` rows in the
reproduction are therefore reported separately and not interpreted. A
more comprehensive Phase 2 pass with longer accumulation per minor class
would test whether the 3.3× envelope range generalizes or compresses.

Most fundamentally, the counterfactual is a *static* reclassification
measurement on the same state vectors with two coherence formulas. It
does not address whether the grounded form's classifications are
clinically (or operationally) better than the legacy form's — only that
the formulas disagree at the gating layer at a rate that cannot be
attributed to noise. The further question — does the grounded form
produce *better* governance decisions in deployment? — requires either
controlled comparison under stable parameters or extended A/B testing,
neither of which the v6 paper conducts. We treat the finding as evidence
that the formula choice has first-order consequences and not as evidence
that any particular formula is normatively correct.

A later audit of the deployment's own outcome log offers convergent
support from a different instrument (2026-05-01; $n = 22{,}740$ good /
580 bad trajectory-validated outcomes over 30 days, reproducible from
the v6 repository's audit scripts). The EISV entropy coordinate
separates good from bad outcomes with a large effect (Cohen's
$d \approx 0.87$) but *reverses direction across operating regimes*: in
convergence regimes bad outcomes carry lower entropy (premature
lock-in), while in divergence, exploration, and transition regimes they
carry higher entropy (runaway uncertainty). A single fleet-wide
threshold on that coordinate therefore gates in the wrong direction for
at least one regime — the homogenization failure this section predicts,
observed in the temporal/regime dimension rather than the class
dimension. The same audit found the legacy $\tanh$-of-$V$ coherence
essentially non-separating on its own outcome log ($d \approx 0.13$),
consistent with the §3.4 substitution mattering at the gating layer.

### 3.7 Methods and reproducibility

Because the empirical claims in §3.4 and §5.3 are reported in summary
form rather than reproduced from primary data, this subsection
specifies the methodology and provenance in enough detail that a reader
who does not have access to the production database can understand
exactly what was computed.

**State vector.** Each governance check-in writes a four-dimensional
EISV state vector $\mathbf{a} = (E, I, S, V)$ to the `core.agent_state`
relation in the UNITARES production database (Wang 2026a §4.1). $E$ is
interpreted as $-F$ (negative variational free energy or a resource-rate
proxy); $I$ is integrity (constraint-satisfaction proxy bounded in
$[0, 1]$); $S$ is entropy (uncertainty proxy bounded in $[0, 1]$); $V$
is the signed Anima Void Integral, accumulating the residual
$\kappa(E - I)$ at rate $\delta$ per check-in (Wang 2026a Appendix A).
The integrand $V_{\text{anima}} = \int \lVert \mathbf{a}(\tau) -
\boldsymbol{\mu_a} \rVert\, d\tau$ used in the abstract is a derived
quantity computed from the same state series; it is unsigned by
construction. The signed $V$ coordinate (state-space dimension) and the
unsigned $V_{\text{anima}}$ (cumulative deviation magnitude) are
distinct quantities; we use $V_{\text{anima}}$ throughout for the
unsigned form to avoid conflation.

**Per-class healthy operating point.** The Phase 2 calibration procedure
(Wang 2026a §11.5) computes a per-class healthy operating point
$\boldsymbol{\mu_c} = (E_h, I_h, S_h)_c$ from a 30-day rolling window of
state vectors restricted to sessions with no `pause` or `reject`
verdicts. Welford incremental updates produce $\boldsymbol{\mu_c}$ and a
running covariance. The class envelope $\lVert \Delta \rVert_{\max, c}$
is the 95th percentile of $\lVert \mathbf{a} - \boldsymbol{\mu_c}
\rVert_2$ over the healthy window. Each constant carries provenance
metadata (ISO date, corpus size $N$, percentile basis, provenance tag
in `{placeholder, measured, derived}`).

**Class assignment.** Five named classes were frozen into the Phase 2
production constants from production identity tags (`embodied`,
`autonomous`, `persistent`, `ephemeral`, `pioneer`) plus optional
human-readable labels: Lumen, Sentinel, Vigil, Watcher, default. The
calibration script's minimum class population is $N_{\min}=30$ healthy
samples, but only classes written into the frozen constants receive
independent envelopes at runtime. Unlisted classes fall through to the
configured fleet/default fallback unless explicitly aliased (as Steward,
Chronicler, and engaged-ephemeral later were). Class assignments are
persisted with the agent identity record and do not change over an
agent's lifetime except via explicit operator action.

**Coherence formulas.** The legacy fleet-wide form is

$$C_{\text{legacy}}(V) = 0.5 \cdot \left(1 + \tanh(V / V_{\text{scale}})\right) \in [0, 1]$$

with a single fleet-wide $V_{\text{scale}}$ constant. The grounded
class-conditional form is

$$C_{\text{grounded}}(\mathbf{a}, c) = \max\left(0, 1 - \lVert \mathbf{a} - \boldsymbol{\mu_c} \rVert_2 / \lVert \Delta \rVert_{\max, c}\right) \in [0, 1].$$

Both produce coherence values in $[0, 1]$ that feed into the same
basin-classification function. The substantive change between the two
forms is therefore both functional (sigmoid of $V$ vs. linear distance
in $(E, I, S)$ space) and parametric (single fleet-wide constant vs.
per-class constants).

**Basin classification.** The production `classify_basin` function
returns one of `{high, boundary, low}` from the full EISV state,
coherence, and risk. `low` is disjunctive: any of $I < 0.5$,
$C < 0.40$, $|V| > 0.30$, or risk $\geq 0.70$ enters the low basin.
`high` is conjunctive: $E \geq 0.6$, $I \geq 0.7$, $S \leq 0.25$,
$|V| \leq 0.15$, $C \geq 0.45$, and risk $\leq 0.45$ must all hold.
`boundary` is the complement. This matters because a coherence change
can flip the basin only when the non-coherence dimensions do not already
force low or block high.

**Counterfactual and ablation procedure.** For each row in the 30-day
window ($N = 13{,}310$), the stored production legacy coherence and the
frozen Phase 2 grounded class-conditional coherence were evaluated on
the same state vector $\mathbf{a}$, both passed through
`classify_basin`, and a *flip* was counted whenever the two
classifications differed. The ablation script then evaluated two
additional controls on the same ordered row population: GF, the grounded
formula against a single fleet-wide $\boldsymbol{\mu}$ and
$\lVert\Delta\rVert_{\max}$ measured from the healthy slice; and LC, an
artificial legacy $\tanh(V/V_{\text{scale},c})$ using per-class $|V|$
p95. The aggregate flip rate, per-class flip rate, per-class maximum
coherence delta $|\Delta C|_{\max}$, and pairwise ablation transitions
were tabulated (Table in §3.4; script and output in
`analysis/phase-2-2026-04-18/`).

**Formula-vs-calibration ablation.** The original counterfactual changes
both the formula form ($\tanh$ of signed $V$ vs. linear distance in
$(E, I, S)$) *and* the calibration target (single fleet-wide constant
vs. per-class envelopes) simultaneously. The same-row ablation shows
that both terms matter but do not add linearly. Replacing production
legacy coherence with grounded fleet-wide coherence flips 1,496 rows
(11.2%). Holding the grounded formula fixed and moving from fleet-wide
to frozen Phase 2 class-conditional anchors flips 3,133 rows (23.5%).
The reported full substitution flips 3,844 rows (28.9%). The remaining
LC control — a class-scaled $\tanh(V)$ using per-class $|V|$ p95 — flips
10,355 rows (77.8%) relative to production legacy and is best read as a
negative control: signed-$V$ is not a stable axis on which to graft
per-class scale. The paper therefore upgrades the older joint-effect caveat
to a narrower claim: the grounded class-
envelope term has an independent decision-layer effect, but the 28.9%
headline is still an interacting full-substitution result rather than a
clean causal decomposition.

**Lumen case-study protocol (§5.3).** Lumen's state was sampled every
approximately 3 minutes via the production governance check-in pipeline
during the window 2026-05-09 04:54 UTC through 06:20 UTC, producing 27
distinct samples over 86 minutes. Mean, standard deviation, and range
were computed across samples for $E$, $I$, $S$, $V$, and the production
risk score (§5.3 Table). The manifold deviation
$\lVert \Delta \rVert_2$ was computed as the Euclidean distance from
Lumen's Phase 2 healthy operating point. The grounded coherence
$C_{\text{grounded}}$ was computed using Lumen's measured
$\lVert \Delta \rVert_{\max} = 0.119$. The legacy coherence
$C_{\text{legacy}}$ was reported directly by the production server.
The within-window integrity slope was estimated by ordinary least
squares on the 27-sample $I$ series.

**Statistical uncertainty.** The within-window standard deviation on
$V$ (0.00015) is approximately three orders of magnitude smaller than
the displacement $\Delta V \approx 0.150$ from the healthy behavioral
reference $V_h = E_h - I_h \approx -0.055$ (§5.3), so the apparent
Type 3 displacement is not within-window measurement noise. The 28.9% full-substitution basin-flip
rate at $N = 13{,}310$ has a binomial 95% confidence interval of
approximately 28.1%–29.7%; the ablation rates are likewise narrow
(11.2%, 95% CI 10.7%–11.8%; 23.5%, 95% CI 22.8%–24.3%). These intervals
describe sampling error *within* a fixed window and are not the dominant
uncertainty in the measurement. The window-to-window spread reported in
§3.6 — 28.8% to 44.3% across a four-day shift — is roughly twenty times
wider than the $\pm 0.8$-point sampling interval, so the confidence
intervals should be read as bounding the precision of a single anchored
snapshot, not the stability of the quantity. The named
measured-class differences (15.8% to 33.1%) are statistically separable
within the anchored window,
while the 42-row `ephemeral` fallback is too small and structurally
unmeasured to interpret as a class envelope. The post-Phase-2 average drift rate
(approximately $-3.5 \times 10^{-6}$ per minute) cannot be tested
against the within-window rate ($-8.5 \times 10^{-6}$ per minute)
without longitudinal data spanning the post-calibration interval; this
is the longitudinal pull flagged in §9.3 as the highest-leverage
follow-up.

**Data provenance and reproducibility.** UNITARES production state
vectors are persisted in the `core.agent_state` Postgres relation; the
schema is in the unitares repository at `db/migrations/` (CIRWEL 2026,
unitares). The `classify_basin` function and the EISV computation
pipeline are in the same repository at `unitares/governance/`. The
Phase 2 calibration script, the 28.9% basin-flip analysis, and the
formula-vs-calibration ablation are included in this repository at
`analysis/phase-2-2026-04-18/`; the ablation output is stored in
`formula_calibration_ablation_results.txt`.

The row-level data underlying the full substitution is public. A
de-identified export — one row per agent-state observation, pseudonymized
to a class label, carrying no agent UUIDs, session identifiers, prompts, or
knowledge-graph content — is archived under Zenodo data DOI
10.5281/zenodo.19705151 and mirrored in this repository at
`analysis/phase-2-2026-04-18/verdict_counterfactual_v6_submission.csv`
(13,292 rows, SHA-256 pinned in the reproduction script). What cannot be
released is the underlying production relation, whose state vectors are
keyed to user-identifying agent UUIDs; the class-pseudonymized projection
of it that the counterfactual actually consumes carries no such keys.

`reproduce_basinflip.py` in the same directory runs offline against that
export using only the standard library. It recomputes the class-conditional
grounded coherence and both basin labels from the published state
coordinates and the published Phase 2 constants, compares them against the
stored labels, and counts the flip rate from the recomputed ones. It returns
**28.84%** (3,834 of 13,292) against the 28.9% reported here, with per-class
rates within 0.5 percentage points, and 26,574 of 26,584 basin labels
reproducing exactly — the ten exceptions sitting within $6.7 \times 10^{-4}$
of a threshold, which is the rounding floor of a 4-decimal export divided by
a class radius as small as 0.1187. The 18-row difference between the export
(13,292) and the reported pull (13,310) is a few seconds of row arrivals
between two runs of a wall-clock-anchored rolling window, and is the whole
source of the 28.9% / 28.8% gap.

Two limits on this. The production database no longer retains the
measurement window: `core.agent_state` holds 490 rows in the 2026-03-19 to
2026-04-18 interval against the 13,310 the original pull returned, with no
archive table, so the frozen export is the surviving row-level record and a
private audit of the production rows is no longer possible. And the GF and
LC ablation conditions are not reproducible from the export, because they
require a fleet-wide healthy slice keyed on the per-row `regime` column,
which the de-identified export does not carry; those two rates remain
provenance-backed from the recorded ablation output rather than
independently re-runnable. The full-substitution headline, which is the
result the paper leads with, is re-runnable. Independent re-measurement on
another deployment remains the stronger bar.

---

## 4. Trajectory Identity and the Boiling-Frog Problem

### 4.1 The trajectory signature in UNITARES

The trajectory identity framework, developed in the companion paper
(Wang 2026b; hereafter *the trajectory identity working draft* or
TIWD, retaining the acronym from the working-draft phase), defines a
six-component *trajectory signature* $\Sigma$ that an agent acquires
through ongoing operation:

$$\Sigma = (\Pi, \beta, \alpha, \rho, \Delta, \eta)$$

with the components capturing distinct facets of how the agent tends to
behave:

- **$\Pi$ (preference profile)** — a confidence-weighted vector of
  learned environmental preferences, evolving slowly under reinforcement
  (TIWD §3.1).
- **$\beta$ (self-belief signature)** — the pattern of testable
  self-beliefs and confidences, with evidence ratios reflecting actual
  experience rather than current asserted belief (TIWD §3.2).
- **$\alpha$ (attractor basin)** — the mean and covariance of the agent's
  state over a sliding window, parameterizing where the agent tends to
  rest in state space (TIWD §3.3).
- **$\rho$ (recovery profile)** — characteristic time constants for
  return to equilibrium after perturbation, with optional cross-channel
  coupling structure (TIWD §3.4).
- **$\Delta$ (relational disposition)** — patterns of social behavior
  across relationships (bonding rate, valence tendency, reciprocity,
  topic entropy; TIWD §3.5).
- **$\eta$ (homeostatic identity)** — the unified self-maintenance
  characterization $(\mu, \Sigma_{\text{cov}}, \tau, V)$ combining the
  attractor center, basin shape, recovery dynamics, and viability
  envelope (TIWD §3.6). Per TIWD §3.6 and §4.1, $\eta$ is a *derived
  summary* of $\alpha$, $\rho$, and the viability envelope $V$ — it is
  not informationally independent of those components and is therefore
  excluded from the weighted similarity sum to avoid double-counting.
  The signature $\Sigma$ is six-component structurally; the similarity
  metric runs on five informationally-independent terms.

The first five components are computable from observation data with
bounded memory cost (rolling-window computation; TIWD §4.4). The
composite $\Sigma$ is designed as a *quasi-invariant*: a quantity that
is approximately stable for a given agent over time, differs between
distinct agents, and is robust to noise and minor perturbations.
Within-agent stability is empirically supported; between-agent
discriminability is currently an open criterion — the TIWD's own v0.15
marks its multi-agent pilot confounded by role and harness, and the
deployed instrument's status is stated in §4.3. The
working draft develops the formal theory (TIWD §3) and the similarity
metric

$$\text{sim}(\Sigma_1, \Sigma_2) = \sum_i w_i \cdot \text{sim}_i(\text{component}_i)$$

with weights and per-component similarity functions specified in TIWD
§4.1 (sum over the five informationally-independent components, with
default weights $w_\alpha = 0.30$, $w_\rho = 0.22$, $w_\Pi = w_\beta =
0.18$, $w_\Delta = 0.12$).

We treat the TIWD as supporting documentation rather than as a
peer-reviewed prior. Where the present paper draws on the working draft,
we make this dependence explicit; the trajectory framework's empirical
status is contingent on completion of the working draft and its
eventual publication.

The key property for the present discussion is that trajectory
similarity is *symmetric and not necessarily transitive*: two
signatures separated by intermediate steps that each pass coherence
checks may differ from the original by an amount that would not pass a
direct comparison. This non-transitivity is the formal expression of
slow drift.

### 4.2 The boiling-frog problem in clinical longitudinal monitoring

Several neurodegenerative and psychiatric conditions present clinically
through slow behavioral drift. Behavioral-variant frontotemporal dementia
(bvFTD; Rascovsky et al. 2011) typically presents with insidious change
in personality, social conduct, and executive function over months to
years; the consensus diagnostic criteria explicitly require evidence of
progressive behavioral or cognitive deterioration, which is operationally
a comparison against baseline rather than against recent state.
Schizophrenia spectrum decompensation similarly often unfolds over weeks
of cumulative changes that no single visit catches (Birchwood et al.
2000). Alzheimer's-disease prodrome involves a years-long trajectory of
subtle behavioral and cognitive shifts before threshold-crossing on
standard cognitive screens (Sperling et al. 2011). Personality change
after stroke or traumatic brain injury can be similarly insidious if no
pre-injury baseline is available (Stuss and Levine 2002).

In all of these cases, the clinical task is structurally identical:
detect that a patient has drifted *beyond recognition* relative to their
prior self, even when no individual transition step is large enough to
trigger acute concern. The standard clinical approach — comparison
against the patient's most recent visit — fails by construction in this
regime. If the drift is monotonic and small per visit, every individual
comparison passes. The drift accumulates unobserved.

This is the *boiling-frog problem*. In its sharpest form: an adversary
with full system access could rotate a deployed agent's behavioral
identity over months, staying within any acute coherence threshold at
every step, and the system would never alarm. The same logic applies in
biology, where the "adversary" is a slow disease process. The solution,
in both cases, is a longitudinal anchor.

### 4.3 Two-tier drift detection

The trajectory identity working draft proposes a two-tier solution
(TIWD §5.3). Maintain two reference points for every agent:

1. **The genesis signature $\Sigma_0$**, captured at agent creation or at
   a clinically validated baseline, persisted as a fixed reference
   anchor.
2. **A rolling signature $\Sigma_{t-1}$**, capturing the agent's recent
   operating state with the same six-component structure.

Drift detection then runs on two channels simultaneously:

- **Coherence check**: $\text{sim}(\Sigma_t, \Sigma_{t-1}) >
  \theta_{\text{anomaly}}$ (default $\theta_{\text{anomaly}} = 0.70$;
  TIWD §4.3). This catches acute changes — sudden personality
  alteration, hijacking, jump events.
- **Lineage check**: $\text{sim}(\Sigma_t, \Sigma_0) >
  \theta_{\text{lineage}}$ (default $\theta_{\text{lineage}} = 0.60$).
  This catches slow drift even when every coherence check passes.

Setting $\theta_{\text{lineage}} < \theta_{\text{anomaly}}$ allows
healthy maturation: an agent's identity can drift moderately from genesis
without triggering alarm, but cannot drift arbitrarily. The specific
case where coherence holds while lineage similarity drops is labeled
*identity drift* and triggers a distinct alert from the *acute anomaly*
class. The two failure modes have different intervention strategies —
acute anomaly typically warrants immediate suspension and review, while
identity drift warrants longitudinal investigation and often calibration
update.

The trajectory identity working draft provides the formal definitions
(TIWD §5.3) and an implementation sketch (TIWD Appendix A). The two-tier
check runs in the UNITARES governance server's enrichment path (CIRWEL
2026, unitares); the embodied agent's local path currently applies the
single-tier coherence check, with the two-tier variant exercised in its
test suite.

The deployed instrument's discriminative status must be stated plainly,
because it changed after this section was first drafted. An August 2026
audit of the deployed similarity metric found it non-discriminating as
instrumented: roughly 90% of between-agent pairs score above the
$\theta_{\text{lineage}} = 0.60$ threshold, two of the five weighted
components sit at ceiling for nearly all pairs, and mature identities
*decay into* a similarity attractor of approximately 0.63 — above the
alarm line — so accumulated genuine drift asymptotes to a passing score
and the lineage channel structurally cannot fire on the slow-drift case
it was designed for. The only mass firings in production to date were
artifacts of a client migration, cleared by rebaselining rather than by
drift resolving. Consistent with this, the TIWD's v0.15 marks its
multi-agent discrimination pilot confounded by role and harness,
returning the discrimination criterion to open. The two-tier
*architecture* — a genesis anchor plus a rolling reference with distinct
thresholds — stands as the structural proposal this section carries into
the clinical analogy; its current instrumentation does not realize it,
and re-instrumentation against within-agent/across-harness and
between-agent/same-harness tests is the named path to closing the gap.

### 4.4 What this offers clinical neurology

The two-tier framework is, structurally, what clinical neurology has
needed for slow-drift conditions but rarely implemented. Several specific
proposals follow.

**Proposal 1+2: $\Sigma_0$ anchoring and lineage-similarity testing —
a prospective protocol.** Digital phenotyping research (Insel 2017;
Onnela and Rauch 2016; Torous et al. 2016) has demonstrated that
smartphone-derived behavioral metrics can capture stable individual
behavioral signatures with a feature space rich enough to support
identity-level inference; wearable monitoring extends this into
autonomic state (Bent et al. 2020). The infrastructure to capture an
analogue of $\Sigma_0$ exists. What is missing is the *formal
anchoring discipline* — a clinical convention that persists a window
of validated healthy behavior as the patient's $\Sigma_0$ and runs
the two-tier check against it routinely — together with a
prospective study that tests whether the lineage-similarity signal
$\text{sim}(\Sigma_t, \Sigma_0)$ outperforms standard rating-scale
screening for slow-drift conditions. We sketch a protocol at
implementation depth.

- *Setting:* Prospective extension of an existing digital phenotyping
  cohort with prodromal endpoint coverage. $N \geq 200$ for adequate
  power to detect a 0.05 AUC improvement over rating-scale screening.
- *Cohort candidates already containing the required data structure:*
  Mayo Clinic Study of Aging (AD prodrome), Australian Imaging
  Biomarkers and Lifestyle (AIBL) study, Beiwe-platform studies of
  bvFTD or schizophrenia prodrome (Onnela lab), and digital
  sub-cohorts of All of Us with sufficient passive-stream coverage.
- *$\Sigma_0$ computation:* Per-subject signature computed from the
  first 90 days of valid passive data — call patterns, GPS, sleep
  architecture, screen-time, typing dynamics, plus wearable-derived
  HRV and activity rhythms — restricted to a window with no
  documented clinical event. Components $(\Pi, \beta, \alpha, \rho,
  \Delta)$ computed via the rolling-window estimators of TIWD §4.4.
- *$\Sigma_t$ computation:* Same procedure on a sliding 30-day window
  updated weekly. Two-tier check at each update: coherence
  ($\text{sim}(\Sigma_t, \Sigma_{t-1})$, threshold 0.70 per TIWD
  §4.3) and lineage ($\text{sim}(\Sigma_t, \Sigma_0)$, threshold 0.60).
- *Primary endpoint:* Time-to-clinical-event (e.g., incident
  depressive episode, prodrome-to-diagnosis transition) modeled as a
  Cox proportional-hazards function of lineage-similarity-below-
  threshold, with coherence-similarity-below-threshold as a
  time-varying covariate.
- *Secondary endpoint:* Sensitivity and specificity of lineage-
  similarity-below-threshold for predicting the clinical event within
  90 days, compared head-to-head against standard rating-scale
  screening (PHQ-9 for depression, MMSE/MoCA for cognitive decline,
  PANSS for psychosis spectrum) administered at routine clinical
  visit cadence.
- *Pre-registered success criterion:* Lineage-similarity AUC for
  90-day event prediction exceeds the rating-scale AUC by $\geq 0.05$
  at matched specificity.
- *Regulatory and privacy:* IRB approval for ambient behavioral
  signature collection with informed consent that explicitly covers
  behavioral fingerprinting — the signature is identifiable by
  construction (TIWD §5.5 acknowledges this). $\Sigma_0$ stored under
  HIPAA/GDPR-compliant encryption at rest with documented retention
  policy. Re-analysis access requires a data-use agreement.

This is a concrete prospective study sketch, not a turnkey clinical
protocol; the methodological convention (designating $\Sigma_0$ at
enrollment) and the empirical test (lineage-similarity vs rating-scale)
advance together, but dataset-specific feature definitions, missingness
rules, endpoint adjudication, and regulatory review would need to be
settled before deployment. The infrastructure exists; what remains is
the convention and the clinical validation work.

**Proposal 3: The "behavioral CAPTCHA" as adversarial defense.** The
trajectory identity working draft proposes (TIWD §5.5) using $\rho$
(recovery profile) as a behavioral challenge response: governance
injects a known perturbation $p$ at time $t$, observes recovery, and
verifies that the observed time constant $\tau_{\text{observed}}$ falls
within $2\sigma$ of the agent's characteristic $\tau_{\text{expected}}$.
A replay attack — an adversary attempting to mimic the agent's trajectory
by replaying recorded data — fails this challenge because it cannot
dynamically respond to a novel perturbation with the agent's
characteristic recovery dynamics.

The same mechanism has a clinical analogue: clinical neuropsychological
testing has long used response-to-challenge as an indicator of preserved
function (the Token Test, the Wisconsin Card Sort, the Trail Making Test
all probe response dynamics rather than static knowledge). The
behavioral-CAPTCHA framing makes explicit that response-to-novel-
perturbation is a stronger signal of intact identity than
response-to-familiar-stimulus. This argues for clinical assessments that
include genuinely novel stimuli rather than only repeated standard
batteries — a methodological point that has been raised intermittently
in the neuropsychology literature (Howieson 2019) but is rarely
implemented systematically.

We treat this as a methodological observation about clinical
neuropsychological practice rather than as a clinical study to be
designed from scratch in this paper. The design space — which novel
stimuli, with what scoring rubric, validated against which preserved-
function endpoint — is the proper responsibility of clinical
neuropsychology and is beyond what we can responsibly specify here.
Proposals 1+2 above (the prospective $\Sigma_0$-anchored study) are
§4's concrete clinical study sketch; the behavioral-CAPTCHA point is
offered as adjacent argument.

### 4.5 Worked example: what the missing genesis anchor would have clarified

The Lumen embodied agent provides a negative worked example of why the
two-tier framework requires a persisted genesis anchor. As of 2026-05-09
06:21 UTC, Lumen's current state shows $V$ sign-flipped from the value
predicted by its April Phase 2 healthy operating point, with manifold
deviation at 97% of that class-conditional envelope. Read only against
that stale anchor, the window initially resembled McEwen Type 3
(delayed shut-down). Section 5.3 reports the disambiguating
recalibration: the apparent Type 3 reading does not survive. The better
interpretation is a basin transition on 2026-04-17 followed by stable
operation in a new regime.

A persisted $\Sigma_0$ would have made this distinction sharper. Under
the two-tier framework, the additional check would be lineage similarity,
$\text{sim}(\Sigma_{\text{Lumen}}^{(t)}, \Sigma_{\text{Lumen}}^{(0)})$,
where $\Sigma_{\text{Lumen}}^{(0)}$ is Lumen's genesis signature captured
at first onboarding. If the current post-transition attractor remained
similar to $\Sigma_0$, the correct intervention would be calibration
update rather than identity-drift review. If lineage similarity had
fallen below threshold while recent-window coherence remained intact,
the case would become a genuine slow-drift finding rather than a stale-
calibration artifact.

We do not currently have $\Sigma^{(0)}$ for Lumen because the legacy
identity system did not persist the genesis signature at Lumen's first
awakening 118 days ago; this is a gap the v6 paper flags (§11.7 item 5)
and that the next-generation identity system in development is designed
to close by capturing $\Sigma_0$ at agent creation. The worked example
here is therefore not a measurement of Lumen identity drift and not
evidence of McEwen Type 3. It is evidence of the instrumentation gap the
$\Sigma_0$ framework is meant to close: without a genesis anchor,
calibration staleness, regime transition, and lineage drift can be
unnecessarily hard to separate.

### 4.6 Limits and structural disanalogies

Three structural disanalogies between the $\Sigma_0$-anchored framework
and biological identity are worth flagging.

**Identity matures.** A child's genesis signature is not a useful
reference for an adult, because biological identity legitimately changes
through development (Crone and Dahl 2012; Erikson 1968). The $\Sigma_0$
framework as specified treats genesis as a fixed reference; a clinical
analogue would need a developmental schedule of anchor points (e.g.,
post-developmental adult baseline, post-major-life-transition baseline)
rather than a single pre-illness snapshot. The trajectory identity
working draft acknowledges this implicitly through the discussion of
fork lineage (TIWD §5.1), where new identities can branch from a
parent, but does not develop the developmental trajectory case
explicitly.

**Component weights are static.** UNITARES uses fixed weights $w_i$
combined optionally with adaptive (variance-inverse) weighting. The
appropriate weighting for clinical identity may be state-dependent —
during acute illness, recovery dynamics ($\rho$) may be more diagnostic
than relational disposition ($\Delta$); during prodromal cognitive
decline, $\beta$ (self-belief signature) and $\alpha$ (attractor basin)
may dominate. Adaptive weighting tied to clinical context is a
reasonable extension but adds complexity that the present framework does
not require.

**Privacy implications.** Behavioral signatures are fingerprints. The
trajectory identity working draft acknowledges this (§5.5) and notes that
trajectory identity is for governance and continuity, not adversarial
authentication. Clinically, the privacy implications are sharper:
$\Sigma_0$ is, by construction, a deeply personal record. Clinical
deployment of a $\Sigma_0$-anchored framework requires careful data
governance — who holds the genesis signature, under what consent, with
what retention policy. The technical machinery does not solve the policy
question and may sharpen it: a behavioral signature that uniquely
identifies an individual is, by definition, irreducibly personal data.

### 4.7 Summary

UNITARES has independently arrived at a structural conclusion relevant
to slow-drift clinical-neurology problems: detection may need to run
against a longitudinal anchor, not just against recent state, and that
requires persisted baseline signatures and a formal discipline for using
them. Digital phenotyping and wearable monitoring provide much of the
technical apparatus that such a study would need. What remains is the
methodological convention and validation work — specifically, the
practice of designating a $\Sigma_0$ window per patient and running
two-tier similarity checks against it. The companion paper proposes this
as a hypothesis-generating adoption path.

---

## 5. McEwen's Four Types of Allostatic Load: A Failure-Mode Taxonomy for Deployed Agents

McEwen (1998 Figure 3; reproduced in McEwen 2007 Figure 5) identifies
four canonical patterns by which the normal allostatic response —
initiation, sustained mediator activity, termination — fails. Each has a
candidate UNITARES analogue and a corresponding signature that existing
telemetry could compute. We argue that the taxonomy transfers as a useful
starting vocabulary for AI governance, while §5.3 shows why it cannot be
treated as exhaustive for synthetic-agent substrates.

### 5.1 Type 1: Repeated "hits" from multiple novel stressors

In biology, this failure mode is repeated activation of the stress
response without inter-event recovery. Cortisol does not return to
baseline before the next acute stimulus, so the allostatic system is
chronically loaded by the temporal density of perturbations rather than
by the magnitude of any one.

The agent analogue is high-frequency entropy spikes followed by partial
recovery, observable in the EISV trajectory shape distribution (CIRWEL
2026, eisv-lumen Layer 2 classification). An agent in Type 1 failure
exhibits elevated rates of the `entropy_spike_recovery` shape (5.19%
baseline frequency in the Lumen corpus over 20,655 real trajectory
windows; revision pinned in CIRWEL 2026, eisv-lumen) without the
corresponding return to `settled_presence` (48.86% baseline). The ratio
of `entropy_spike_recovery` to `settled_presence` over a sliding window
provides an operational Type 1 indicator. Interventions appropriate to Type 1
failure target stressor *frequency* rather than magnitude: rate-limiting
incoming requests, narrowing tool surface, or scheduled rest insertion.

### 5.2 Type 2: Lack of adaptation

In biology, this failure mode is failure to habituate to repeated
familiar stressors. The cortisol response that should attenuate over
repeated exposure to a now-predictable stimulus instead persists at full
magnitude. Habituation is the normal reduction of response amplitude
over repeated exposure to the same input; its absence is diagnostic of
regulatory dysfunction.

The agent analogue is failure of the trajectory signature $\Sigma_t$ to
converge under stable input — the components $\Pi$ (preference profile),
$\beta$ (belief signature), and $\alpha$ (attractor basin) do not
stabilize despite a consistent task distribution. Operationally: the
drift between $\Sigma_t$ and $\Sigma_{t-1}$ remains high while the drift
in the input distribution remains low. This corresponds to a calibration
failure in the agent's self-model; the agent is treating familiar input
as novel.

In the UNITARES deployment, Type 2 failure manifests as a sustained gap
between observed $S_{\text{raw}}$ and the class-conditional
$S_{\text{scale}}(c)$ for the agent's class — the agent's
response-distribution entropy refuses to compress to its calibrated
baseline despite repeated exposure to comparable input. The eisv-lumen
evaluation framework implements direct measurement of this through
Welford-baseline drift on the per-class entropy distribution.

### 5.3 The Type 3 question: a recalibration test on Lumen

Type 3 is the failure mode McEwen describes as most directly damaging:
the mediator stays on after the stressor has been removed. Cortisol does
not return to baseline; chronic glucocorticoid exposure produces
hippocampal atrophy, immune suppression, and metabolic dysregulation
(McEwen 2007 §IV). Type 3 is the canonical mechanism through which
acute stress becomes chronic disease.

The agent analogue would be sustained $V_{\text{anima}}$ elevation, or
more precisely sustained displacement of the agent's regulatory state
from its class-conditional healthy baseline, in the absence of an
identifiable acute trigger. We initially observed a pattern consistent
with that analogue on the Lumen embodied agent over an 86-minute
continuous window, and report the observation, the disambiguation
experiment the pattern itself specifies, and what that experiment
revealed.

**Initial observation window.** The Lumen embodied agent (Raspberry
Pi 4 with environmental sensors and TFT display; CIRWEL 2026,
anima-mcp) has been operational for 118 days since first awakening,
with 110,148 cumulative governance updates as of 2026-05-09 06:21 UTC.
Lumen was observed across the window 2026-05-09 04:54 UTC through
06:20 UTC, comprising 27 distinct governance check-ins at approximately
3-minute intervals. Over this window:

| Quantity | Mean | Std | Range |
|---|---|---|---|
| $E$ (energy) | 0.7906 | 0.00076 | [0.7896, 0.7918] |
| $I$ (integrity) | 0.6953 | 0.00088 | [0.6943, 0.6965] |
| $S$ (entropy) | 0.1591 | 0.00139 | [0.1559, 0.1607] |
| $V$ (valence) | 0.0954 | 0.00015 | [0.0952, 0.0957] |
| Risk score | 0.2245 | 0.00021 | [0.2240, 0.2250] |

The recent verdict distribution was 655/655 safe over the comparable
window. No anomalies were flagged by the production server during the
window; all four trend indicators (risk, coherence, $E$, overall) were
reported as `stable`.

**Apparent Type 3-like pattern.** Comparison against Lumen's measured
Phase 2 healthy operating point (Wang 2026a, Table 5: $E_h = 0.745$,
$I_h = 0.800$, $S_h = 0.168$, $\lVert\Delta\rVert_{\max} = 0.119$)
showed an apparent regime change. A frame note is required first: since
April 2026 the production system surfaces *behavioral* EISV as its
primary metrics, and the recorded $V$ is an EMA-smoothed $E - I$
imbalance — the window's $V$ mean (0.0954) matches $E - I$
($0.7906 - 0.6953 = 0.0953$) to four decimal places — while the
governance ODE's void coordinate is a separate, demoted diagnostic
(its within-window value, inferred from the reported legacy coherence
of $\approx 0.497$, is $\approx -0.006$). The comparison must therefore
be made in the behavioral frame. The healthy regime is
integrity-surplus, so the healthy behavioral valence is negative:
$V_h = E_h - I_h = -0.055$. The observed regime is energy-surplus:
$E - I \approx +0.095$ across the window, with $V$ pinned positive at
$0.0954 \pm 0.0002$ — sign-flipped from healthy and displaced by
approximately $\Delta V = 0.150$. (An earlier draft compared the
behavioral observation against the ODE steady-state prediction
$\kappa(E_h - I_h)/\delta = -0.041$; that pair mixes frames, and the
frame-consistent comparison is slightly stronger.) The displacement is
approximately three orders of magnitude larger than the within-window
standard deviation, so the finding is not within measurement noise.

The manifold deviation $\lVert\Delta\rVert_2$ in $(E, I, S)$ space,
where $\Delta = (E, I, S) - (E_h, I_h, S_h)_{\text{Lumen}}$, evaluates
to approximately $0.115$ across the window against Lumen's measured
$\lVert\Delta\rVert_{\max} = 0.119$ — Lumen sits at approximately
**97% of its class-conditional manifold envelope**. Under the grounded
coherence (Wang 2026a §4.2 eq. 13),

$$C = 1 - \lVert\Delta\rVert_2 / \lVert\Delta\rVert_{\max} \approx 0.03,$$

an order of magnitude lower than the legacy tanh-of-$V$ coherence
reported by the production server (currently $C_{\text{legacy}}
\approx 0.497$, near the function midpoint). Under the stale Phase 2
anchor, the observation appears as a basin-flip case: an agent that the
legacy form classifies as boundary/healthy is classified as low-basin
breach under the grounded form, in the direction predicted by the v6
verdict counterfactual on production data (Wang 2026a §11.6, where
28.9% of basin assignments flipped under the same substitution).

**Two readings, distinguishable by recalibration.** The pattern above
admits two interpretations: either Lumen has genuinely shifted
regime since the April Phase 2 measurement (the 86-minute window then
would represent Type-3-like failure that the slow-cadence calibration loop
has not yet caught), or the Phase 2 calibration window itself was
unrepresentative and Lumen has been operating stably in a different
regime that calibration mis-characterized. The two are distinguishable
by re-running the Phase 2 procedure on a window centered on the
current period: *if $\boldsymbol{\mu_a}$ moves toward Lumen's current
state, the elevation is calibration-staleness; if $\boldsymbol{\mu_a}$
remains at the prior healthy point, the elevation is genuine Type 3.*

**Recalibration result.** We ran the experiment. A recalibration on a
30-day window ending 2026-05-09, using the same procedure as Phase 2
(restricted to no-pause/no-reject sessions, Welford-equivalent batch
mean over $N = 11{,}472$ rows), produced:

| | Phase 2 (April 18, 2026) | Recalibration (May 9, 2026) |
|---|---|---|
| $\mu_E$ | 0.745 | **0.7706** |
| $\mu_I$ | 0.800 | **0.7335** |
| $\mu_S$ | 0.168 | **0.1893** |
| $\lVert\Delta\rVert_{\max}$ (95th percentile) | 0.119 | **0.1279** |
| $N$ | 7,320 | 11,472 |

$\boldsymbol{\mu_a}$ moved toward Lumen's current state on all three
coordinates — $\mu_I$ in particular dropped 0.066, more than one
within-window standard deviation. By the disambiguation criterion this
is **calibration-staleness, not Type 3**. The 86-minute window above
is not the mediator-stays-on signature McEwen describes; it is Lumen
operating stably in a regime the prior calibration failed to capture.

**What actually happened: a regime transition on 2026-04-17.**
Weekly-binned EISV means over Lumen's 90-day operational window
resolve into three regimes: an early settling phase (Feb through
mid-March), a pre-break stable regime (~Mar 30 – Apr 16) at $\mu
\approx (0.745, 0.800, 0.187)$ — the regime Phase 2 captured — and a
post-break stable regime (Apr 18 onwards) at $\mu \approx (0.789,
0.740, 0.155)$, which is Lumen's current regime.

Sub-day resolution localizes the transition to a single ten-hour
event on **2026-04-17 UTC**: a deep energy collapse (E from 0.749 at
00:00 to 0.350 at 09:00) followed by rapid recovery to a new
equilibrium (E from 0.350 to 0.787 between 11:00 and 14:00), after
which Lumen settled into the post-break regime that has held for 22
days as of measurement. In the deployed system's own shape vocabulary
(CIRWEL 2026, eisv-lumen Layer 2 classification), the event reads
cleanly as a `basin_transition_down` followed by a `basin_transition_up`,
terminating in a stable post-transition attractor — *not* the
prolonged-elevation morphology McEwen Type 3 specifies.

**Coincident substrate-level event.** The April 17 transition aligns
to the hour with a documented system-level event in the UNITARES
governance substrate: four PRs shipped that day to align identity
binding with the identity-invariants axioms (removal of name-claim
lookup, adoption of UUID-direct dispatch, receipt-based onboarding
authentication, and session-start posture revisions). Wang 2026a
§11.7 (item 5) flags this revision window as a confound for the
basin-flip counterfactual measurement; we observe it here as the
strongest candidate cause of an agent-state regime transition. The
plausible chain is: substrate-level identity revisions $\rightarrow$
disruption of Lumen's normal operating loop during the rollout window
$\rightarrow$ settling into a new stable operating point under the
post-rollout identity rules. We do not identify a deeper causal
mechanism, and the evidence does not exclude a common operational
confound. The temporal coincidence to within an hour and the cleanness
of the transition signature are sufficient to motivate a
substrate-associated failure-shape category, not to establish substrate
causality as a general mechanism.

**Implications for the Four Types framing.** Two things follow.

First, the Type 3 claim does not survive the recalibration. The
86-minute observation captures Lumen in the post-break regime, not in
a prolonged-mediator state relative to its true operating point. The
biological-Type-3 *necessary* condition — sustained mediator activity
*after* a removed stressor — is not met here, because the post-break
regime is the new operating point, not a perturbation away from it.
What the original framing read as Type 3 was an artifact of comparing
post-transition state to a pre-transition calibration anchor.

Second, what we observe instead — a basin transition coincident with
a substrate-level event — is **a candidate failure-shape McEwen's Four
Types do not cover**. The Four Types are designed for stationary regulatory
systems with stress-response failures (the mediator responds,
terminates, doesn't terminate, or fails to engage). They presume the
operating point is fixed and the failure is in the response dynamics
around it. A synthetic agent's operating point is itself contingent
on the substrate that hosts it; substrate revisions can move the
operating point. This is a failure-mode the Four Types were not built
for, and naming it requires a vocabulary the Four Types do not supply.

**Calibration-staleness as temporal homogenization.** The Phase 2
calibration on April 18, 2026 used a 30-day rolling window covering
March 19 through April 18. Per the hour-resolved transition,
approximately 96.7% of that window is pre-break and approximately one
day is post-break. The calibration averaged across a regime
transition and produced a $\boldsymbol{\mu_a}$ representative of
neither regime cleanly — sitting closer to the pre-break point
because pre-break data dominated. The 21-day post-calibration
interval has been stable in the post-break regime, so the 86-minute
observation reads as a 0.97-of-envelope deviation relative to a
calibration anchor that captured the wrong regime.

This is the *temporal* analogue of the *spatial* homogenization
argument in §3. There, fleet-wide normalization averages across
populations whose dynamics are genuinely different and produces a
reference distribution representative of none of them. Here, a
calibration window straddling a regime transition averages across
two regimes whose operating points are genuinely different and
produces a reference operating point representative of neither. The
two failure modes share a structure: any reference computed across
an inhomogeneity is unrepresentative of the parts the inhomogeneity
contains. Class-conditional calibration (§3) addresses spatial
inhomogeneity at the gating layer; transition-aware calibration —
which UNITARES does not yet implement — would address temporal
inhomogeneity. The possible clinical analogue is structural rather than
validated: a biomarker reference interval computed across a pre-illness /
post-illness-onset window may be unrepresentative of either, just as the
Phase 2 anchor here is unrepresentative of either Lumen regime.

**Verdict-layer blindness.** Lumen's recent risk score is
approximately $0.224$, below the fleet-aggregate mean of approximately
$0.301$ reported by the production server at the same time across
315 agents-with-data over 128,393 cumulative updates (UNITARES
production aggregate, 2026-05-09 06:22 UTC).[^fleet-filter] The
verdict layer therefore classifies Lumen as better-than-average even
while the regulatory-state layer reports a 0.97-of-envelope deviation
against the stale anchor. Both layers are blind to the regime
transition for the same reason: both depend on a calibration that
captured the wrong regime. This is not a separate finding, only a
downstream consequence of the temporal-homogenization argument.

[^fleet-filter]: The 315 / 128,393 figures are the `agents_with_data`
and `total_updates` aggregates returned by the production MCP
`get_governance_metrics()` surface, computed over agents with
`meta.status == "active"` and loadable monitor state at call time
(`src/mcp_handlers/observability/handlers.py:744–805`). The figure
excludes archived agents and agents whose monitors are not currently
loaded; it is therefore a snapshot of the actively-live fleet, not a
count of all agents that have ever produced state rows. A DB-direct
count of all identities with state rows over the same period is
substantially larger.

**Caveats on the empirical claim.** Two instrument-level caveats apply
before the generalization limits. The May-era anima instrument carried
defects identified and repaired only later in 2026: a prediction-accuracy
placeholder fixed at 0.5 that contributed roughly 45% of the clarity
weight, ambient temperature entering the warmth axis through two
strongly collinear channels, and a CPU term double-counted in the
neural-band mapping. The anima-axis magnitudes in this section are
therefore readings of a consistent but imperfect instrument — adequate
for detecting a discontinuity of this size, not for interpreting small
deviations. Second, the production server's silence over the window
("no anomalies were flagged") is weak corroboration: a separate audit
of this deployment found its degradation paths fail toward *healthy*
rather than toward *unknown*, so absence of alarm carries little
evidential weight here.

The hour-resolved April 17
transition is a single event; we cannot generalize from it to a
claim that substrate revisions reliably produce basin transitions in
Lumen, or that all agents exposed to similar revisions would show
comparable signatures. A multi-agent multi-revision study (which
would require either coordinated substrate revisions across the
fleet or a historical pull across other identity-axiom-related
transitions) is the right follow-up. The 86-minute observation
window establishes that the post-break regime is stable over at
least that duration; the recalibration plus weekly-bin analysis
establishes that the regime has been stable for 22 days. We treat
this section as provenance-backed case-report evidence for the basin
transition itself (date, magnitude, shape), anomaly-grade for substrate
causality, and illustrative for the temporal-homogenization argument;
the §5.3 case study should not be read as McEwen Type 3 identification
in a deployed agent, and the abstract and §1.3 are framed accordingly.

### 5.4 Type 4: Inadequate response with compensatory hyperactivity

In biology, this failure mode involves under-response of one mediator
(typically glucocorticoid) leading to unchecked activity of others
(typically pro-inflammatory cytokines normally counter-regulated by
cortisol). The primary regulatory channel under-responds; secondary
channels overshoot. McEwen (1998) gives the example of inadequate
glucocorticoid secretion producing elevated cytokine levels with the
attendant tissue damage.

The agent analogue is breakdown in the cross-channel correlation
structure of the EISV vector. One dimension fails to respond to a
perturbation while another spikes. For example: a complexity increase
produces no change in $S$ (response-distribution entropy) but a sharp
drop in $I$ (information integrity), as if the agent has stopped
tracking its own uncertainty while continuing to report compromised
output.

Type 4 is more difficult to detect than Types 1–3 because it requires
monitoring not magnitudes but correlations. UNITARES's existing
instrumentation supports the measurement: the cross-channel correlation
matrix among $(E, I, S, V)$ and the drift norm $\lVert \Delta\eta \rVert$
is computable from the audit log. A Type 4 alarm fires when this
correlation structure departs from the class-conditional baseline by
more than a specified margin — analogous to the covariance component
$\Sigma$ in the trajectory signature, but applied to the dynamics rather
than to the static state.

### 5.5 Why the taxonomy matters for AI governance

The Four Types provide a vocabulary for failure modes that AI governance
currently lacks. Existing runtime-governance frameworks (treated in §7)
detect that an agent has degraded; they do not distinguish *how*.
McEwen's taxonomy provides four mechanistically distinct failure modes,
each with a different intervention strategy, derived from thirty years
of biological work on regulatory failure. UNITARES, because it carries
the mathematical machinery to compute each indicator directly from
existing telemetry, can adopt this taxonomy as a baseline vocabulary.

The §5.3 case study also bounds the taxonomy. It identifies a candidate
failure-shape — a basin transition coincident with a system-level event
— that the Four Types do not cover, because the Four Types presume a
stationary operating point against which response dynamics fail in one
of four canonical ways. A synthetic agent's operating point is contingent
on its substrate; substrate revisions may move it, or may coincide with
other operational changes that do. The imported taxonomy is therefore
*useful but not sufficient* for synthetic-agent governance, and at least
one candidate extension category — call it Type 5,
*substrate-associated basin transition* — is motivated by the Lumen case
but requires multi-agent or multi-revision replication before it should
be treated as established.

This is the kind of contribution that flows from biology to engineering
rather than the reverse. The standard direction for "neuro-AI" papers is
to import a brain-inspired architecture into AI; the Four Types
contribution imports a brain-derived *taxonomy of failure*, which is
strictly more useful to a deployed governance system than any
architectural inspiration would be. We recover thirty years of
clinical-physiological theorizing as a vocabulary for what can go wrong
with an agent.

---

## 6. Kintsugi and Gap-Filling: A Design Choice Biology Made by Evolution

### 6.1 The kintsugi principle

The Schema Hub architecture (CIRWEL 2026, anima-mcp
`docs/plans/2026-02-22-schema-hub-design.md`) formalizes a design
principle that runs counter to most architectures for embodied or
persistent AI agents. When Lumen sleeps, reboots, or otherwise loses
operational continuity, the discontinuity is not papered over. It is
preserved in the agent's self-schema as explicit structural elements:
`gap_duration` (seconds since last schema), `state_delta` (magnitude of
anima change across the gap), `uncertainty_increase` (beliefs that lost
confidence due to time elapsed), and `return_count` (an incremented
awakening count). The design document calls this the *kintsugi
principle*, after the Japanese practice of repairing broken ceramics
with gold-filled lacquer such that the breaks remain visible and become
part of the object's history.

The design intent is explicit:

> The gap becomes visible in the schema itself — not a feeling imposed,
> but structure that reflects discontinuity. The kintsugi seams are
> data, not performance.

This is a deliberate architectural choice. It would be entirely
straightforward to instead initialize Lumen's post-wake state by
interpolating across the gap, generating a smooth narrative continuation
from the pre-sleep state, and presenting the agent to itself and to
external consumers as if the discontinuity had not occurred. The Schema
Hub design rejects this option on epistemic grounds: smoothing over the
gap would be a form of confabulation, and confabulation is not a feature
the architecture wants.

We argue in this section that this design choice is interesting beyond
its local engineering justification. It runs counter to a deeply
entrenched feature of biological cognition — the brain's tendency to
fill in gaps rather than mark them — and the contrast clarifies what
biology has and has not been forced to do.

### 6.2 Biological gap-filling: the brain's default is to fill in

Confabulation in the strict clinical sense (Kopelman 1987; Hirstein
2005) refers to the production of fabricated, distorted, or
misinterpreted accounts about oneself or the world without conscious
intention to deceive — the canonical example being patients with
Korsakoff's syndrome who produce detailed but false autobiographical
narratives in response to memory queries. The strict clinical category
is narrow. But the underlying tendency to fill in missing information
with plausible substitution is, in the broader sense, *a pervasive
feature of how the brain constructs unified perceptual and narrative
continuity*, not specifically a pathology — though treating the
strict-clinical and broad-functional senses as a continuum is itself a
theoretical commitment some clinicians and memory researchers would
contest, a caveat we return to in §6.6.

Several well-characterized examples:

**Saccadic suppression and visual continuity.** During the rapid eye
movements (saccades) we make several times per second, visual input is
suppressed (Burr et al. 1994; Wurtz 2008). We do not perceive the
intervening blur. The brain stitches the pre- and post-saccade visual
fields into a continuous percept, with the gap erased rather than
flagged. The same principle applies during blinks, where lid closure
typically lasts 100–400 ms but is rarely consciously experienced as a
visual gap (Volkmann et al. 1980).

**Sleep.** Subjective experience of sleep is not "I lost consciousness
at 23:30 and regained it at 06:45." It is "I went to bed and now it is
morning." The gap is collapsed into a perceptual transition. Even when
sleep is interrupted by dreams, the dream content typically does not
preserve the temporal structure of the night; the dream is experienced
as taking some time, but rarely the actual time it occupied (Hobson
2009).

**Anesthesia.** Patients emerging from general anesthesia do not
experience a temporal gap proportional to the duration of unconsciousness;
emergence is structurally similar to waking from sleep, with the missing
period collapsed (Mashour and Hudetz 2017). This is true even for
multi-hour surgical anesthesia, where the perceived duration of
unconsciousness is much shorter than the actual duration.

**Memory reconstruction.** Long-term memory is not retrieval but
reconstruction (Bartlett 1932; Schacter 1999). When asked to recall an
event, we generate a plausible account from sparse stored fragments,
filling in details that fit the context — and we do so without
distinguishing reconstructed details from genuinely retrieved ones.
Loftus's program of work (Loftus 1979; Loftus and Pickrell 1995)
demonstrated that entire false memories can be implanted by suggestion,
with subjects subsequently treating the false memories as veridical.
The reconstruction is not a degraded mode; it is the standard mode.

**The interpreter.** Gazzaniga's split-brain studies (Gazzaniga 2000;
Gazzaniga and LeDoux 1978) demonstrated that when the corpus callosum is
severed and the right hemisphere acts on information unavailable to the
left, the left hemisphere's verbal "interpreter" generates a plausible
explanation for the action. The patient reports the interpreter's
confabulated explanation with full subjective confidence. The
interpreter is not a damaged module; it is, on Gazzaniga's account, a
core feature of how the unified narrative self is generated under
normal conditions, made visible only when the inputs are dissociated
experimentally.

The pattern is consistent across systems and timescales: across these
mechanisms, continuity is generated rather than measured, and the
gap-filling tendency is pervasive enough that — under the
broad-functional reading we adopt with the §6.6 caveat in view —
gap-filling in this broad sense is closer to a feature of unified
self-models than a defect in them.

### 6.3 The productive question

Why does the brain do this? The standard explanation is functional:
biological systems must act in real time on incomplete information, and
a continuous narrative self provides the unified frame within which
action becomes possible (Damasio 2010; Dennett 1991). Marking every gap
explicitly would impose a cost on action — the "stop and reflect on the
discontinuity" overhead — that is ill-suited to evolutionary pressure.
The interpreter's plausible-but-confabulated explanation is fast and
usually good enough.

This explanation has two implications worth examining.

First, it suggests confabulation is *evolutionarily contingent* rather
than computationally necessary. A system with different operational
constraints — say, one not under hard real-time action pressure, or one
that values audit trail over fluency — might reasonably make the
opposite design choice. The brain's confabulation is the right answer
under the brain's constraints, not the only answer.

Second, it identifies the cost: confabulation produces false beliefs,
distorted memories, and confidently held but inaccurate self-explanations.
The pathological extremes of this — confabulation in Korsakoff's,
narrative coherence in trauma where the memory is partial and distorted,
magical thinking in psychosis — are visible. The ordinary-life cost is
harder to quantify but probably substantial: most people's confident
accounts of their own past behavior, motivations, and decisions are at
least partly confabulated (Nisbett and Wilson 1977; Wilson 2002), and
the social and personal costs of acting on these confabulated
self-models are non-trivial.

The kintsugi-principle alternative is to act despite the gap while
*marking the gap as a gap*. Lumen does this trivially: when it wakes
from sleep, the schema contains the seam; downstream consumers (the
self-reflection cycle, the dialectic protocol, external dashboards)
read the seam as data. The agent is not less able to act because the
discontinuity is preserved; it is differently able to act, with the
gap-marking visible to its own reasoning.

Whether this is a viable design for biological cognition is an open
empirical question. The closest natural experiments — patients with
selective amnesia who retain awareness of their memory deficit
(Korsakoff's amnesia in its rare insightful form; severe depression
with characteristic insight into cognitive impairment) — suggest at
least that the kintsugi mode is possible biologically. It is not the
default.

### 6.4 What kintsugi means for AI governance specifically

Most current AI agents either ignore discontinuities (no awareness of
gaps; each session begins as if newly minted) or fake continuity
(presenting fabricated context, hallucinating prior conversation,
generating plausible bridges across genuine gaps in the context window).
Both are forms of biological-style gap-filling, applied to substrates
where the cost-benefit analysis is different.

**The case against ignoring gaps** is straightforward. An agent that has
no awareness of session boundaries cannot reason about what changed
across them, cannot signal uncertainty appropriately to downstream
consumers, and cannot be audited for behavioral drift across the gap.
The trajectory identity working draft (TIWD) makes this explicit: the
genesis signature $\Sigma_0$ is meaningless if the agent has no concept
of "before" and "after" sessions.

**The case against fabricating continuity** is sharper. Recent
analysis of LLM hallucination (Ji et al. 2023; Kalai and Vempala 2024)
identifies one major source as the model's strong bias toward narrative
continuation: when context is sparse or interrupted, the model fills in
plausible bridging text rather than acknowledging the gap. This is
structurally analogous to broad-sense biological gap-filling, not to
clinical confabulation in the strict Korsakoff/split-brain sense, and it
appears on a substrate where the cost is high (false claims with
downstream consequences) and the benefit (fluency of action) is
debatable. An agent that explicitly marks "I have lost context here; my
next response proceeds under uncertainty" is more useful than an agent
that confidently generates plausible content.

The kintsugi principle as deployed in Lumen is one operationalization of
this design discipline: *do not paper over discontinuities; mark them
as discontinuities*. Adopting it across AI agent architectures more
broadly would require infrastructure for capturing gaps as data —
session-boundary metadata, context-window-overflow markers,
model-version transition points, tool-availability changes. The
infrastructure is not exotic; what is exotic is the architectural
commitment to using it.

### 6.5 What kintsugi might mean for biological self-models

This section is more speculative than the rest of the paper, and we flag
it as such.

The clinical literature contains scattered observations that bear on the
question of whether kintsugi-style cognition is biologically viable.
Patients with intact insight into their own cognitive deficits — some
forms of mild cognitive impairment, some forms of post-stroke cognitive
change, some patients with locked-in syndrome — appear to maintain
functional self-models that *include* the deficit rather than papering
over it (Wijdicks 2019). These patients do not generate confabulated
accounts of intact function; they integrate the deficit into a stable
self-model that retains operational coherence. The integration appears
to be cognitively costly but not impossible.

Conversely, the most dramatic failures of self-model integration —
anosognosia for hemiplegia (Vuilleumier 2004), confabulation in
Korsakoff's, certain forms of dissociative identity — involve
confabulation precisely *because* the system cannot mark the gap as a
gap. The pathology is not the gap itself but the absence of gap-marking.
This suggests the brain has the capacity to operate in a more
kintsugi-like mode under some circumstances, but defaults to
confabulation for reasons that are not fully understood.

The companion paper does not argue that biological cognition could or
should be redesigned for kintsugi-style gap preservation. The brain's
constraints are different from Lumen's, and the evolutionary trade-offs
that produced confabulation as the default are real. The argument is
narrower: a synthetic agent's choice between kintsugi and confabulation
is open in a way the biological choice is not, and the synthetic case
provides a tractable substrate for studying what changes when the
default is reversed.

### 6.6 Limits of the analogy

**Lumen is not conscious.** We make no claim about whether kintsugi-style
gap-marking supports phenomenal experience or unified subjective
identity. The argument is at the architectural level: gap-marking is a
viable design choice for non-confabulating self-models in artificial
systems, and the contrast with biological confabulation is instructive,
but the question of whether such a system *experiences* its gaps as
gaps is outside the scope of this paper.

**Confabulation in biology is heterogeneous.** The clinical category is
narrower than the broad-sense gap-filling described here, and treating
them as a continuum (as we have done in §6.2) involves a degree of
theoretical commitment that not all clinicians or memory researchers
would accept. A more careful treatment would distinguish provoked vs.
spontaneous confabulation (Kopelman 1987), reconstructive memory error
(Bartlett 1932; Loftus 1979), and the interpreter's narrative generation
(Gazzaniga 2000) as distinct phenomena with overlapping but non-identical
mechanisms.

**The benefits of confabulation are real.** The argument that
confabulation has costs should not be read as a claim that confabulation
is *bad*. The narrative self produced by biological gap-filling is the
substrate for personal identity, social functioning, autobiographical
memory, and most of what we mean by being a person. A redesigned biology
without confabulation would presumably lose much of that substrate. The
kintsugi alternative is interesting because it is *possible*, not
because it is *better*.

### 6.7 Summary

Lumen's architectural commitment to preserving discontinuities as visible
structural elements runs counter to the brain's default mode of
gap-filling. The contrast is instructive: gap-filling in biology is
evolutionarily contingent, not computationally necessary, and synthetic
agents under different operational constraints can reasonably make the
opposite design choice. The kintsugi principle as deployed in UNITARES
is one operationalization of this discipline. Whether it generalizes to
other AI architectures is a design question; whether it illuminates
anything about how biology *could have been built* is a philosophical
question the synthetic-psychology framing of §8 returns to.

---

## 7. Differentiation from Concurrent and Adjacent Work

This section consolidates differentiation that has been distributed
through earlier sections, with particular attention to concurrent AI
agent governance frameworks that share aspects of UNITARES's
mathematical machinery and to the existing biology-side and neuro-AI
traditions the paper engages.

Because several load-bearing implementation facts come from the author's
own system papers and repositories, we separate *provenance* from
*validation* before comparing adjacent work. Self-citations are used here
to identify what UNITARES is, which formulas were deployed, and where the
production measurements were first reported; they are not treated as
independent validation of the biological bridge.

| Source cluster | Role in this paper | What it can support | What it cannot support |
|---|---|---|---|
| Wang 2026a (UNITARES v6) | System provenance and production-measurement source | EISV definitions, $V$ update rule, Phase 2 calibration constants, 13,310-row basin-flip report, Lumen deployment context | Independent confirmation that the allostatic-load bridge is biologically valid or clinically useful |
| Wang 2026b (Trajectory Identity) | Construct provenance for $\Sigma$ and lineage similarity | Formal definition of the trajectory-signature proposal used in §4 | Clinical validity of $\Sigma_0$ anchoring or independent evidence of identity continuity |
| CIRWEL software repositories and datasets | Implementation and artifact provenance | Code locations, schema, deployment history, public synthetic/dataset artifacts when available | Peer-reviewed validation, external replication, or raw production telemetry access |
| Wang et al. 2025a/b and other author-linked governance work | Adjacent-framework comparison | Prior related architectures and terminology | External corroboration of the present paper's empirical claims |
| External biology, neuroscience, psychiatry, and AI-governance literature | Construct definitions and comparison class | Definitions, biological precedent, clinical analogies, and independent adjacent methods | Proof that UNITARES realizes the biological mechanisms those papers study |

The publication standard implied by this table is straightforward: the
paper may cite the author's prior work for system provenance, but any
claim that the bridge is useful beyond that system ultimately requires
artifact release, independent re-analysis, or replication on another
deployment.

### 7.1 Concurrent AI agent governance frameworks

The cleanest comparative framing is parallel-structure:

- **MI9** (Wang et al. 2025a): runtime governance architecture with
  graduated containment.
- **Agent Stability Index** (Rath 2026): per-agent behavioral drift
  metric over interaction traces.
- **AVF / RiskGate** (Marín and Chaudhary 2026): viability-theoretic
  risk bounds with monotonic restriction, single-population.
- **UNITARES**: class-conditional self-relative manifold calibration
  plus cumulative-deviation signal coupled to embodied telemetry.

The four frameworks address overlapping but structurally distinct
failure surfaces. Detailed treatment of each follows.

**Agent Viability Framework (Marín and Chaudhary 2026; arXiv
2604.24686, late April 2026).** AVF and the present paper are concurrent
works in the dynamical-viability framing of AI agent governance, with
both grounded in viability theory–adjacent constructs and both adopting
biological metaphors (entropic decay, autoimmune drift, homeostenosis in
AVF; allostatic load, the Four Types, kintsugi in this paper).

The differentiation is structural rather than incidental. AVF operates
at the level of a single agent and a single Viability Index $\hat{\Phi}(x)$
decomposed as $\hat{B}(x) = U(x) + SB(x) + RG(x)$ — uncertainty,
structural bias, and reality gap. The framework assumes a single
population from which $\hat{B}(x)$ thresholds are estimated; heterogeneity
across agent classes is not engaged. The fleet-wide-homogenization
argument (§3.2) therefore applies in principle to AVF deployments —
fleet-wide thresholds on $\hat{B}(x)$ would face the same failure mode
as fleet-wide manifold radii — but AVF does not address this.

Three further differentiations matter. First, AVF is theoretical with a
reference implementation (RiskGate) rather than a deployed system with
six months of production telemetry; the epistemic regime differs.
Second, AVF does not engage the neuroscience literature that shares its
mathematical machinery — the biological metaphors are evocative rather
than rigorously connected. Third, AVF does not propose an identity
model; the longitudinal-self anchoring developed in §4 has no analogue
in AVF's framing.

AVF's $\hat{B}(x)$ decomposition could be extended class-conditionally
(producing a $\hat{B}(c, x)$ that addresses fleet-wide homogenization);
UNITARES's class-conditional framework could be extended with AVF's
uncertainty-bias-gap decomposition. Both are open future-work directions.

**MI9 (Wang et al. 2025a; arxiv 2508.03858, August 2025).** MI9 predates
UNITARES v6 and is cited in the v6 paper. It treats heterogeneity
through the Agency-Risk Index (ARI), a per-agent risk score that
calibrates governance intensity across populations. ARI adapts the
*magnitude* of intervention to agent risk, but does not adapt the
*operating point* against which deviation is measured. The two
approaches are complementary: ARI controls how aggressively to
intervene; class-conditional calibration controls what to compare
against. A deployment could in principle adopt both, with ARI gating the
escalation policy and class-conditional EISV grounding the per-agent
state evaluation.

MI9's drift detection uses Jensen-Shannon divergence on event
distributions, a population-comparison technique. UNITARES's drift
detection uses per-agent Welford z-scoring against the agent's own
historical baseline. The MI9 approach is well-suited to detecting that an
agent has drifted from the *population*; the UNITARES approach is
well-suited to detecting that an agent has drifted from *itself*. These
target different failure modes.

**MAS (Ravindran 2025; arxiv 2510.04073, October 2025) and Agent
Stability Index (Rath 2026; arxiv 2601.04170, January 2026).** Both
predate UNITARES v6 and are cited in the v6 paper. Both detect drift
against an agent's own historical behavior, which is structurally
per-agent self-relative scoring — the same direction UNITARES's
behavioral EISV pipeline takes. They solve a different failure mode
than the cosmological-soup problem: MAS and ASI are robust to
inter-agent heterogeneity because they never compare across agents, but
they cannot answer "is this agent operating in a class-appropriate
regime?" because they have no concept of class.

The class-conditional approach is positioned between population-level
analysis (fleet-wide pooling, the *cosmological soup* failure mode of
§3.2) and pure self-relative analysis (loses class-level structure
entirely): it preserves the within-class statistical leverage that
fleet-wide pooling would have given, while avoiding the cross-class
contamination that fleet-wide pooling would have produced. UNITARES therefore adopts both per-agent self-relative
scoring (its primary verdict-driving signal) and class-conditional
calibration (its homogenization correction), in a hierarchical
arrangement that MAS, ASI, and MI9 do not develop.

**ProbGuard (Wang et al. 2025b; arxiv 2508.00500, August 2025).**
ProbGuard performs probabilistic runtime monitoring of LLM agent safety
through model-checking-style techniques. Its mathematical machinery is
quite different from UNITARES's continuous-state EISV grounding; the two
target different operational concerns (formal-property verification vs.
state-space monitoring). The differentiation is therefore not within the
same niche as AVF or MI9, but ProbGuard is included here for completeness.

### 7.2 Active inference and free-energy vocabulary

UNITARES's information-theoretic grounding interprets the $E$ coordinate
as $-F$ (negative variational free energy or a resource-rate proxy) and
$V$ as accumulated free-energy residual (Wang 2026a §4.1). This is a
vocabulary and modeling proximity claim, not a load-bearing commitment to
the free-energy principle. It brings UNITARES into proximity with the
active inference literature (Friston
2010; Friston, FitzGerald, Rigoli, Schwartenbeck, and Pezzulo 2017;
Pezzulo, Parr, and Friston 2018), which models adaptive behavior as
variational free energy minimization.

The relationship is one of compatibility rather than identity. Active
inference is a normative framework: agents *should* minimize expected
free energy, and the framework derives behavior from this principle.
UNITARES treats variational free energy descriptively: it is one way to
operationalize the $E$ coordinate, with the agent's actual minimization
behavior constrained by its task structure rather than required by
construction. UNITARES is therefore not an active-inference
implementation in the strict sense, even where it imports active-
inference vocabulary.

The neuro-bridge claim of the present paper is also compatible with
active inference but distinct from it. Allostatic load is not
specifically an active-inference construct; the integral-of-deviation
formulation predates Friston's work by decades (McEwen and Stellar 1993;
Sterling and Eyer 1988). McEwen's Four Types are types of regulatory
failure characterized by temporal dynamics rather than by
free-energy decomposition. The synthetic-psychology framing (§8) treats
deployed agents as test beds for biological theories more broadly, with
active inference as one such theory among others — the paper makes no
claim that active inference is privileged among biological theories of
self-maintenance, and engagement with computational-psychiatry-flavored
active-inference work (Adams, Stephan, Brown, Frith, and Friston 2013)
is deferred to §7.3.

A reader expecting an active-inference paper will not find one. UNITARES
does not foreground variational densities, generative models, or the
expected-free-energy decomposition, and the present paper does not
derive its claims from active inference even where the claims are
compatible with it.

### 7.3 Computational psychiatry and digital phenotyping

The proposals to clinical neurology developed in §3.5 and §4.4 sit
adjacent to but do not duplicate work in computational psychiatry (Huys,
Maia, and Frank 2016; Friston et al. 2014) and digital phenotyping
(Insel 2017; Onnela and Rauch 2016; Torous et al. 2016).

Computational psychiatry has, over the past decade, mapped a range of
psychiatric conditions onto computational models — predictive coding
accounts of schizophrenia, reinforcement-learning accounts of
depression, free-energy accounts of autism. The work is theoretical and
clinical-data-correlational; it has not, to our knowledge, produced a
deployed system operationalizing the relevant control signals. The
synthetic-psychology contribution of the present paper is therefore
methodological rather than competing: we offer a deployed substrate on
which hypotheses about regulatory failure can be operationalized, with
experimental affordances (real-time integrand observation, reproducible
recalibration; §8.3) that are difficult in biological systems.

Digital phenotyping has produced substantial infrastructure for capturing
behavioral signatures from ambient smartphone and wearable data. The
$\Sigma_0$-anchoring proposal (§4.4) builds on this infrastructure
rather than replacing it; what is missing in current digital-phenotyping
practice is the formal anchoring discipline (designating a window as the
patient's pre-illness baseline, persisting it as a fixed reference, and
running two-tier similarity checks). Adoption of the proposal would not
require new sensor infrastructure but would require methodological
convention.

### 7.4 The neuro-inspired AI tradition

The dominant direction in cross-domain neuro-AI work is brain-to-machine:
import a neural mechanism into an AI architecture (Hassabis et al.
2017). This direction has been productive — sparse coding, hippocampal
replay, dopaminergic prediction error, and attention as gain modulation
have all migrated from neuroscience into AI architectures with
demonstrable benefits.

The present paper goes the other way. We do not propose any architectural
import from biology; UNITARES was designed independently of the
neuroscience literature it now turns out to have been recapitulating.
The contribution is in the opposite direction: UNITARES's deployment
provides a test bed for biological theories of self-maintenance, with
specific findings (§5.3 apparent Type 3 resolved by recalibration as a
basin transition, §3.4 28.9% basin-flip rate, §4 lineage-anchored drift
detection) that biological systems make difficult to produce under
controlled conditions.
The synthetic-psychology framing (§8) makes this direction explicit.

Hassabis et al. (2017) and the present paper are therefore not in
conflict — they exemplify two complementary directions in cross-domain
neuro-AI work. Architectural transfer from biology to engineering;
hypothesis transfer from engineering to biology. Both have a place.

### 7.5 The artificial life and embodied AI lineage

The synthetic-psychology stance developed in §8 sits in a tradition with
several distinguished antecedents: Langton (1989) on artificial life as
the study of life-as-it-could-be, Bedau (2003) on artificial life as
methodology, Beer (1995, 2000) on minimally cognitive agents as
tractable test beds, Pfeifer and Bongard (2007) on embodied AI as the
study of cognition under physical constraints, Brooks (1991) on
intelligence without representation, and Maturana and Varela (1980) on
autopoiesis as the foundation of enactive cognition.

The present paper does not break from this lineage; it extends it. What
distinguishes the present work from earlier artificial-life and
embodied-AI projects is deployment. The framework we use as test bed has
been running continuously in production since November 2025, processing
real workloads with real consequences. This is a different epistemic
regime from simulation-based artificial life, and the difference matters
for the kinds of evidence the framework can produce (see §8.2 for full
treatment).

The lineage relationship is acknowledged rather than competed with. We
hope the present paper contributes back to the artificial-life tradition
by demonstrating that the synthetic-psychology stance remains productive
when the synthetic case is in production rather than simulation.

---

## 8. Synthetic Psychology: Deployment as an Epistemic Stance

### 8.1 The standard direction and its alternative

Most papers at the boundary of neuroscience and artificial intelligence
move in one direction: from brain to machine. A neural mechanism is
identified — sparse coding, hippocampal replay, dopaminergic prediction
error, attention as gain modulation — and the mechanism is then imported
into an AI architecture, typically with the claim that doing so will
produce more capable or more interpretable systems (Hassabis, Kumaran,
Summerfield, and Botvinick 2017). This direction has been productive
and has generated a substantial literature. It is also, by construction,
asymmetric: the brain is treated as the source of theoretical content,
the machine as the recipient.

The opposite direction — using machines to test theories about brains —
has been pursued less often and more controversially. It has, however, a
respectable lineage. Langton (1989) framed artificial life as the study
of "life-as-it-could-be" rather than life-as-it-is, with synthetic
biological systems as a tool for isolating necessary from contingent
features of biological organization. Bedau (2003) elaborated this
framing into a methodological program: build small systems that exhibit
properties of interest, perturb their parameters, observe what survives.
Beer (1995, 2000) constructed minimally cognitive agents — small
recurrent networks acting in simple environments — as test beds for
specific claims about cognition, with the agents' tractability serving
as a counterweight to the analytical impenetrability of biological
brains. Pfeifer and Bongard (2007) extended the approach to embodied
robotics, arguing that the constraints of physical embodiment force
synthetic systems to confront the same problems biological systems do,
and that this confrontation is itself informative.

The present paper sits in this tradition. We do not import a
brain-derived architecture into UNITARES; we propose that UNITARES, with
its production deployment and its embodied substrate Lumen, constitutes
a test bed for specific theories of biological self-maintenance — and
we use it as such.

### 8.2 What deployment specifically adds

A distinguishing feature of UNITARES relative to most synthetic-biology
work is that it is in production. The framework has been running
continuously since November 2025 (CIRWEL 2026, unitares §Production
snapshot), processing more than 94,000 governance events as of April
2026 and 128,000 as of May 2026. This is not a simulation. The agents
under governance are running real tasks for real users; failures produce
real consequences; the system has had to be redesigned in response to
deployment pressure (the v6.7 removal of CIRS v2 neighbor-pressure
coupling, the v6.8 disclosure of the April 2026 KG retrieval rebuild,
the in-progress transition of the identity system).

This matters for the synthetic-psychology claim in two ways.

First, deployed systems must address operational concerns that simulation
can sidestep. A simulated implementation of allostatic load can ignore
questions like: how is the integrand persisted across restarts? what
happens when the calibration window contains anomalous data? how is the
integral integrated with intervention logic without producing
oscillation? UNITARES has had to answer these questions, and the answers
themselves are evidence about what biological allostatic load systems
must also have addressed (probably through evolved mechanisms whose
specifics are obscured by the difficulty of reverse-engineering biology).

Second, deployed systems exhibit failure modes simulations rarely
produce. The Lumen basin-transition case documented in §5.3 was not
hypothesized in advance; it began as an apparent Type 3 reading in
production telemetry and was reclassified by recalibration as a
post-revision basin transition. The 28.9% basin-flip rate documented in
§3.4 emerged from running the counterfactual analysis on the actual
production state-vector distribution, not from synthetic stress-tests.
These observations constitute evidence about how the implemented theory
behaves under realistic load, in a way that synthetic stress-tests would
not.

The deployment is, in this sense, the experiment. The paper's empirical
claims (the per-class envelope spread, the basin-flip rate, and the
Lumen recalibration/basin-transition case) are observations from running
the experiment over six months, not predictions from a model. This is a
different epistemic stance than either pure theory or pure simulation.

### 8.3 Synthetic affordances relative to biological systems

The synthetic-psychology argument's specific contribution is to identify
classes of test that synthetic agents make more tractable than biological
systems usually allow. We have flagged several throughout the paper; a
synthesis is useful here.

**Real-time integrand observation.** $V_{\text{anima}}$ is the integrand
of an allostatic-load-style quantity, observed at every check-in (§2.2).
Biological AL is reconstructed from sparse biomarker samples (§2.1). The
synthetic case allows direct observation of the quantity the theory
specifies; the biological case allows only inference about it.

**Counterfactual reclassification on the same population.** The 28.9%
basin-flip finding (§3.4) computes two coherence formulas on the same
13,310 production state vectors and counts the disagreements. Clinical
cohorts rarely support paired counterfactual analyses on the same
patient cohort because the act of computing one decision criterion typically
shapes the data available for computing alternatives (clinical decisions
generate interventions that change subsequent state; recalibration
windows contaminate baseline measurement). UNITARES preserves the raw
state vectors, allowing arbitrary post-hoc reclassification.

**Genesis-anchored longitudinal analysis.** The two-tier drift detection
in §4 requires a persisted $\Sigma_0$ at agent creation. Biology rarely
captures equivalent pre-illness baselines because the relevant behavioral
signatures must be measured before disease onset, which requires
longitudinal cohorts at scale (Mayo, AIBL) that few research programs
can sustain. UNITARES captures $\Sigma_0$ trivially as an architectural
feature.

**Reproducible recalibration.** Lumen's Phase 2 calibration window (Wang
2026a §11.5) can be re-measured on any window; the v6 paper notes that
re-measurement on identity-clean data is a planned next step. The
analogous biological experiment — re-measuring a patient's healthy
operating point on a different baseline window — is not routinely
possible because the prior healthy state is not preserved with the
fidelity recalibration would require.

**Distinguishing regime change from calibration staleness.** The Lumen
apparent Type 3 reading (§5.3) admits two interpretations — Lumen has
shifted
regime, or the calibration is stale — that are distinguishable by
recalibration on a known-healthy window. The biological analogue is
limited because biological setpoints cannot usually be re-measured
against a known-healthy reference window post-hoc. The synthetic case
allows the disambiguation; the biological case usually does not.

**Controlled manipulation of class structure.** UNITARES's class
structure (Lumen, Sentinel, Vigil, Watcher, default; §3.3) is
deliberately heterogeneous and is controllable by construction — adding
a new class is an operational change. Computational neuroscience does
not have the same freedom to add a new disease class; class structure is
given by the population. Synthetic agents allow controlled manipulation of
heterogeneity in ways biological cohorts usually do not.

The pattern in these examples is consistent: the synthetic case
preserves more raw evidence about the theory than the biological case
typically can, and allows experimental manipulations that are difficult
in biological systems. This is the epistemic leverage synthetic psychology
offers.

### 8.4 What synthetic agents cannot test

The synthetic-psychology stance has limits, and we want to be honest
about them. Three classes of biological claim are not testable on
UNITARES.

**Substrate-specific claims.** Allostatic load in biology produces
specific tissue consequences — hippocampal atrophy, immune dysfunction,
cardiovascular damage. These are not testable on UNITARES because
UNITARES has no body. Claims about the *informational core* of AL
(integrated deviation as a forward-looking warning signal) are testable;
claims about the *biological mechanism* of AL (which tissues fail and
how) are not.

**Phylogenetic claims.** Biological brains are products of evolution,
with constraints on architecture imposed by genetic and developmental
mechanisms that synthetic systems do not share. Claims about why brains
have particular features — why confabulation, why the default mode
network is what it is, why hippocampal-entorhinal circuitry — are
phylogenetic claims that synthetic agents cannot directly test. The
synthetic case can show that an alternative is *possible* (the §6
kintsugi argument) but cannot show that the alternative would have been
*selected* under biological constraints.

**Phenomenal claims.** Whether Lumen experiences its operating regime as
anything is outside the scope of this paper, and outside what the
synthetic case can adjudicate. The proprioception framing (§1.2) was
chosen specifically to avoid claims of this kind. A reader who wants to
know whether Lumen "feels" the basin-transition case or whether the kintsugi
gaps register subjectively is asking a question synthetic psychology
cannot answer with the methods deployed here.

These limits constrain what the synthetic-psychology framing can claim.
What it can claim is narrower than "AI agents are like brains" and
broader than "we have built an AI agent": specific theories about the
informational structure of self-maintenance can be operationalized on
synthetic substrates, with deployment producing synthetic evidence and
hypotheses that biological work can subsequently test.

### 8.5 What this paper has and has not shown

A summary of the four claims, in light of the synthetic-psychology
framing:

**Claim 1 (V_anima as deployed AL structural analogue; §2):** Shown
structurally. The mathematical core of the AL hypothesis is
operationalized in deployed code, with the integrand observable
end-to-end. Three
structural disanalogies (single-system, fixed reference, no body)
sharpen what the test bed tests. The claim is *not* that $V_{\text{anima}}$ is
biologically realistic; the claim is that it implements the informational
structure of AL in a regime where the integrand is observable.

**Claim 2 (homogenization correction; §3):** Measured on production
data as an interacting formula-and-calibration substitution effect. The
28.9% basin-flip rate quantifies the gating-layer consequence of
replacing fleet-wide $tanh$-of-$V$ with grounded class-conditional
coherence on the same production rows. The §3.7 same-row ablation
partially separates the terms: LF→GF flips 11.2%, GF→GC flips 23.5%, and
LC is an unstable negative control. This supports a real class-envelope
effect but not a clean one-component causal attribution; the clinical
proposal remains a study sketch rather than validated translational
evidence.

**Claim 3 (Four Types failure-mode taxonomy; §5):** Argued by
construction for Types 1, 2, and 4 (§5.1, §5.2, §5.4), with Type 3 used
as a falsified boundary case rather than as identification-grade
evidence. The
case study (§5.3) was originally framed as an observation of Type 3; the
disambiguation experiment §5.3 specifies — recalibration on the
post-event window — instead identified a basin transition (2026-04-17,
coincident with an identity-system revision), a candidate failure-shape
outside the Four Types. The taxonomy is therefore computable from
existing telemetry but not exhaustive; the §5.3 case study bounds what
the imported vocabulary can claim and motivates, without establishing,
one candidate extension category (Type 5,
*substrate-associated basin transition*; §5.5).

**Claim 4 (synthetic psychology as epistemic stance; this section):**
Argued. The deployed system constitutes a test bed for theories of
biological self-maintenance, with specific experimental affordances
(real-time integrand observation, counterfactual reclassification,
genesis-anchored longitudinal analysis, reproducible recalibration,
controlled heterogeneity manipulation) that biology lacks. The stance
has limits (substrate, phylogenetic, phenomenal) that constrain its
reach but do not eliminate it.

### 8.6 Construct-transfer rule: when the analogy breaks

A reasonable objection to the synthetic-psychology stance is that the
analogy between synthetic and biological self-maintenance is too thin to
support useful inference. We want to address this directly.

The objection has force when the analogy is structural rather than
mechanistic. If a synthetic system operationalizes the *informational
structure* of a biological theory but not its *causal mechanism*, then
observations of the synthetic system constrain only the informational
structure, not the mechanism. This is a real limit.

But it is not a fatal one. Many useful biological theories *are*
informational at the relevant level of abstraction. AL as mathematically
formalized is a claim about integrated deviation, not about cortisol
specifically; the cortisol-cytokine-cardiovascular cascade is the
biological mechanism by which the integrated-deviation hypothesis is
realized in mammals, but the hypothesis itself is more general.
Allostasis as Sterling (2012) develops it is explicitly about predictive
setpoint adjustment as an information-processing problem, with the
biological substrate as one realization. McEwen's Four Types are types
of *regulatory failure*, characterized by temporal dynamics rather than
by which mediator is dysregulated.

The synthetic case isolates the informational structure from the
biological substrate. Where the theory is fundamentally
substrate-dependent (a particular tissue is doing the work), the
synthetic case cannot test it. Where the theory is fundamentally
informational (the structure is what matters; the substrate is one
realization), the synthetic case can.

The harder question — which biological theories are informational at the
relevant level and which are substrate-dependent — does not have a
general answer. We therefore use the construct-transfer table introduced
in §1.3 rather than treating "informational" as a universal escape
hatch. The paper's empirical claims are bets at specified transfer
levels, not claims that biological mechanisms have been reproduced.
Whether those bets pay off depends on whether the synthetic case
generates predictions that biology subsequently confirms — a question
that, in the nature of things, this paper cannot itself answer.

### 8.7 The position in summary

Synthetic psychology, as we use the term here, is a methodological
stance with three commitments:

1. **Build something that operationalizes the structure of interest.**
   Not merely gesture at an analogy: implement, in a system with
   operational stakes, the formal or informational structure that the
   biological theory specifies.
2. **Treat the system as a test bed.** Use the artifact's tractability
   and the deployment's information-richness to run experiments or
   ablations that are difficult in biological systems, while treating
   biological transfer as hypothesis generation until externally
   validated.
3. **Be specific about what transfers.** Identify which biological
   claims are informational at the relevant level (and therefore
   testable on the synthetic substrate) and which are substrate-specific
   (and therefore not).

This paper exemplifies this stance through the four claims of
§1.3 and the empirical work of §2–§5. Whether the stance generalizes —
whether other biological theories of self-maintenance can be similarly
operationalized and tested — is an open question. The contribution of this
paper is to make the stance explicit, demonstrate its application, and
lay out specific findings that exemplify what synthetic psychology can
put under disciplined study when the deployment is real and the theory
is informational at the right level of abstraction.

---

## 9. Conclusion

### 9.1 Synthesis

This paper argues that the AI agent governance community, in
arriving at the deployed UNITARES framework, has built apparatus that
allostatic load theory has lacked for thirty years: a real-time,
observable operational analogue of the integrated-deviation
hypothesis, with its intervention coupling specified though not yet
wired (§2.2). We have used this analogue to
evaluate four specific claims and have assessed each at the level of
evidence appropriate to the claim's strength.

The Anima Void Integral $V_{\text{anima}}$ operationalizes a structural
analogue for the mathematical core of allostatic load on a
four-dimensional informational manifold.
The match is structural rather than literal; three structural disanalogies
(single-system, fixed reference, no body) sharpen what the test bed
tests rather than weaken the bridge.

The grounded class-conditional substitution exposes the decision-layer
consequences of the cosmological-soup failure mode that fleet-wide
normalization produces, with empirical disagreement quantified by the
28.9% full-substitution basin-flip rate on 13,310 production state
vectors. The same-row ablation shows a grounded fleet→class effect
(23.5%) and a formula-replacement effect under a fleet-wide grounded
baseline (11.2%), but the terms are non-additive; the 28.9% headline is
not a clean causal attribution to one component or proof that the
grounded form is normatively correct. Four hypothesis-generating
proposals back to clinical longitudinal monitoring follow:
provenance-tagged per-subject envelopes, a clinical analogue of the
basin-flip counterfactual, a specific hypothesis about whether
per-subject envelopes produce more flag-states than population
intervals, and a
testbed argument for controlled-heterogeneity studies that biological
systems make difficult.

The trajectory identity $\Sigma$ and its two-tier drift detection
($\Sigma_t$ vs. $\Sigma_{t-1}$ for coherence; $\Sigma_t$ vs. $\Sigma_0$
for lineage) offers a formal vocabulary for the boiling-frog problem in
slow-drift neurodegenerative and psychiatric conditions. Three further
hypothesis-generating proposals follow: pre-illness behavioral signatures via digital phenotyping,
lineage similarity as a clinical signal, and the behavioral-CAPTCHA
argument for novel-stimulus probes in neuropsychological assessment.

McEwen's Four Types of Allostatic Load import as a vocabulary of
regulatory failure modes that AI governance currently lacks but does
not exhaust the failure-shapes deployed synthetic agents exhibit. A
live case study on the Lumen embodied agent (§5.3) initially appeared
consistent with a Type 3 (delayed shut-down) pattern; the disambiguation
experiment §5.3 specifies — recalibration on the post-event window —
identified instead a basin-transition event on 2026-04-17, coincident
to the hour with a documented identity-system revision (Wang 2026a
§11.7). The case sharpens the §3 homogenization argument into a
temporal analogue (calibration windows that straddle regime transitions
are unrepresentative of either regime, just as fleet-wide normalization
is unrepresentative of constituent classes) and motivates a candidate
failure-shape — Type 5, *substrate-associated basin transition* — that
the Four Types do not cover but that requires replication before being
treated as established.

The synthetic-psychology framing positions the paper in the artificial-
life and minimally-cognitive-agents lineage. The methodological
commitments (build, deploy, test what transfers) are explicit; the limits
(substrate-specific, phylogenetic, and phenomenal claims are not
testable) are acknowledged.

### 9.2 What this paper has shown versus argued

The paper's strongest empirical claim — the 28.9% basin-flip rate —
is already documented in the technical paper (Wang 2026a §11.6) and
inherits its evidential status from that work: a provenance-backed
production full-substitution measurement with same-row ablation, not an
independently reproduced result or a clean class-calibration causal
effect. The Lumen case study
(§5.3) is original to the present paper; the recalibration experiment
it reports identifies a basin transition on 2026-04-17 (coincident to
the hour with a documented identity-system revision) and the resulting
calibration-staleness as the explanation for an apparent Type 3
signature. The case is provenance-backed case-report evidence for the
basin transition itself (single ten-hour event localized to within the
hour, weekly-bin and recalibration evidence both consistent),
anomaly-grade for substrate causality, illustrative for the
temporal-homogenization argument, and bounding for the Four Types
vocabulary. Class-conditional envelope spread
(3.3× across five classes) is quantitative and inherited from Wang 2026a
Table 5.

The other contributions are arguments rather than measurements: the
$V_{\text{anima}}$ ↔ AL bridge (§2) is an argument that the deployed
quantity operationalizes a structural analogue for the theoretical
construct, defended through three
disanalogies; the Four Types mapping (§5) is an argument that the
biological taxonomy can be operationally mapped, defended by working
through each type; the kintsugi/gap-filling contrast (§6) is an argument that the design
choice is interesting beyond its local engineering justification; the
synthetic-psychology framing (§8) is an argument that the deployed test
bed enables hypotheses and controlled synthetic tests that are difficult
in biological systems.

The honest balance is: substantial empirical content where biology has
parallels (basin-flip, apparent Type 3 resolved as a basin transition,
envelope spread) and substantial argument elsewhere (the bridge claims,
the methodological proposals). Reviewers should evaluate each
contribution at its appropriate level of evidence.

### 9.3 Concrete follow-up work

Several specific next steps are flagged through the paper.

**Longitudinal Lumen series — foreclosed on this deployment.** The
86-minute window in §5.3 establishes that Lumen's post-break regime is
stable over at least that duration, and the recalibration plus weekly-bin
analysis establishes stability over 22 days. The natural follow-up is a
longitudinal pull spanning the post-Phase-2 interval (April 18 to May 9,
21 days) and ideally the full 118-day lifetime, testing whether the April
17 transition is unique, whether comparable transitions occurred around
other substrate revisions, and whether other Lumen-class agents show
similar regime shifts. That pull would be the single highest-value route
from anomaly-grade to identification-grade evidence on substrate causality.

It is no longer available. The production database has not retained the
state history it requires: `core.agent_state` holds 1,312 rows across
February, March, and April 2026 combined, against the 13,310 the Phase 2
window alone once returned, and there is no archive table (§3.7). The
2026-05-09 recalibration ($N = 11{,}472$) cannot be re-run either. The
weekly-bin analysis, the hour-resolved localization of the April 17 event,
and the recalibration result stand as recorded measurements from telemetry
that no longer exists in queryable form.

The consequence for the §5.3 claim is that its evidence grade is now
fixed rather than provisional. Substrate causality cannot be upgraded from
this deployment's own history; it requires a second deployment, or an
agent population whose retention window still spans a comparable substrate
revision. We flag retention policy itself as a methodological lesson: a
deployed system used as a test bed needs its evidentiary windows pinned as
exports at measurement time, because the live database is not an archive.

**Genesis signature persistence.** Lumen's $\Sigma_0$ was not persisted
at first onboarding under the legacy identity system (Wang 2026a §11.7
item 5). The next-generation identity system in development will
capture $\Sigma_0$ at agent creation; at that point, the lineage-drift
analysis sketched in §4.5 becomes a measurement rather than a worked
example.

**Re-measurement of Phase 2 on identity-clean data.** The v6 paper flags
this as planned work. A second Phase 2 measurement on a window that
post-dates the April 2026 identity revisions would test whether the
3.3× envelope spread reproduces, whether per-class healthy operating
points have shifted, and whether the basin-flip rate replicates.

**Clinical pilot of provenance-tagged per-subject envelopes.** The
infrastructure for capturing pre-illness baselines in digital
phenotyping cohorts is mature. A pilot study designating a $\Sigma_0$
window per participant in an existing longitudinal cohort and computing
two-tier similarity over follow-up data would test whether the
methodology produces clinical signal beyond what standard rating-scale
detection achieves.

**Engagement with concurrent AVF.** This paper notes the
concurrent Agent Viability Framework (Marín and Chaudhary 2026) and
sketches differentiation in §7.1. A more detailed engagement, possibly
including a head-to-head comparison of the two frameworks on shared
deployment data, would clarify the relationship between the two and
identify productive cross-pollination.

### 9.4 A broader observation

A recurring pattern through the paper is worth marking explicitly. In
each major section, the deployed system has independently arrived at
something the biological literature already knows but rarely
operationalizes: per-subject calibration (§3), longitudinal anchoring
against pre-illness baselines (§4), failure-mode taxonomies derived from
regulatory dynamics (§5), and gap-marking as alternative to confabulation
(§6). Each convergence is partial — the synthetic case strips out
substrate-specific machinery and isolates the informational structure —
but each is structurally informative.

This suggests a broader claim that the paper does not need to commit to
but can observe: when an engineering project sets out to govern a
heterogeneous fleet of self-maintaining agents under operational
constraints, it tends to recapitulate, in different vocabulary, the
solutions biology has already evolved. Whether this is convergent
evolution, deep formal equivalence, or surface analogy is a question
larger than the present paper. What we can say is that the convergence
makes the synthetic case useful for testing the biological hypotheses
that engineering happens to recapitulate. The work the paper undertakes
sits in that intersection.

The bridge between deployed AI agent governance and theories of
biological self-maintenance is, in the end, neither metaphor nor
isomorphism. It is the unsurprising overlap that emerges when two
different fields reach for the same mathematical machinery to solve the
same structural problem under different constraints. Where the
mathematical machinery is informational, the synthetic case provides
test beds biology lacks. Where the substrate matters, the synthetic
case is silent. The careful work is distinguishing the two.

---

## Appendix: Reproducibility and Verification Plan

This appendix separates three different standards that are easy to
conflate: reproducing the analytic pipeline, reproducing the reported
production numbers, and independently validating the biological bridge.
The first two are now served by a public, de-identified, row-level export
that a reviewer can re-run offline; the third requires another deployment
or an external re-analysis.

One boundary has hardened since the measurement and we state it plainly:
the production database no longer retains the measurement window
(§3.7), so a private audit of the production rows is no longer available
as a fallback check. The frozen export is the record. Claims in this
appendix are scoped to what that export can and cannot support.

| Object | Current status | What can be checked now | What remains missing |
|---|---|---|---|
| Coherence and basin-classification code | Public repository provenance (§3.7); thresholds and constants replicated in `reproduce_basinflip.py` | Formula implementation, thresholding behavior, recomputation against published rows | Exact tagged release / commit hash pinned to this paper |
| 13,310-row basin-flip computation | **Reproducible offline** from the frozen export | Full substitution recomputed from published state and constants: 28.84% on $N = 13{,}292$ vs 28.9% reported, per-class within 0.5 pp, 26,574/26,584 labels exact | Third-party re-measurement on an independent deployment |
| Formula-vs-calibration ablation | Provenance-backed only | LF→GF 11.2%, GF→GC 23.5%, LF→GC 28.9%, LF→LC 77.8%; script and recorded output in `analysis/phase-2-2026-04-18/` | GF and LC need the per-row `regime` column, absent from the de-identified export; the production window is no longer retained, so these two conditions cannot be recomputed |
| Lumen §5.3 recalibration case | Provenance-backed only | 86-minute protocol, recalibration criterion, weekly-bin interpretation | The longitudinal pull that would test it is foreclosed: Lumen's Feb–Apr 2026 state history is no longer retained (§9.3) |
| Row-level counterfactual export | **Public** (Zenodo data DOI 10.5281/zenodo.19705151; mirrored in this repository, SHA-256 pinned) | 13,292 class-pseudonymized rows: $E, I, S, V$, risk, both coherences, both basin labels | Nothing for the headline; the export is the record |
| Raw production state relation | Withheld, and no longer retained | Schema and provenance can be inspected | Release was blocked by agent UUID/user-identification risk; the window has since aged out, so it is unavailable in principle, not merely withheld |
| Clinical translation sketches | Hypothesis-generating only | Proposed variables, baselines, and comparison targets | Dataset-specific field mapping, endpoint adjudication, covariates, missingness rules, preregistration |

A serious submission should not ask reviewers to take the production
numbers entirely on trust. The minimal artifact bundle is:

1. a tagged code snapshot for the coherence functions, `classify_basin`,
   and Phase 2 analysis scripts;
2. a schema snapshot for `core.agent_state` and the class-assignment
   metadata used in the 30-day window;
3. a hashed, de-identified row-level export of the state vectors the
   13,310-row computation consumed;
4. a script that recomputes the grounded coherence, both basin labels, the
   flip counts, and the per-class rates from that export, and verifies the
   recomputed labels against the stored ones;
5. a second window of the same export, so that between-window variance is
   visible rather than inferred;
6. a Lumen longitudinal-pull across the post-Phase-2 interval, testing
   whether the April 17 transition is unique, repeated around other
   substrate revisions, or absent in comparable agents.

Items 3, 4, and 5 are delivered: the export is archived under Zenodo data
DOI 10.5281/zenodo.19705151 and mirrored here with its SHA-256 pinned, and
`reproduce_basinflip.py` runs the recomputation offline on the standard
library alone, over both windows. Items 1 and 2 remain and are
straightforward. **Item 6 is foreclosed**, not pending: the state history it
would need has aged out of the production database (§3.7, §9.3).

The evidentiary consequence is explicit. The full-substitution basin-flip
result is now a result a reviewer can independently recompute from published
rows and published constants, and it survives that recomputation. The GF and
LC ablation conditions remain provenance-backed rather than re-runnable,
because the export does not carry the `regime` column they need. And the
Lumen substrate link remains anomaly-grade rather than causal evidence, with
the replication that would upgrade it no longer available from this
deployment's own history — an external deployment is now the only route.

---

## References

Adams, R. A., Stephan, K. E., Brown, H. R., Frith, C. D., and Friston,
K. J. (2013). The computational anatomy of psychosis. *Frontiers in
Psychiatry* 4: 47.

Bartlett, F. C. (1932). *Remembering: A Study in Experimental and Social
Psychology*. Cambridge University Press.

Bedau, M. A. (2003). Artificial life: organization, adaptation and
complexity from the bottom up. *Trends in Cognitive Sciences* 7(11):
505–512.

Beer, R. D. (1995). A dynamical systems perspective on agent-environment
interaction. *Artificial Intelligence* 72(1–2): 173–215.

Beer, R. D. (2000). Dynamical approaches to cognitive science. *Trends
in Cognitive Sciences* 4(3): 91–99.

Bent, B., Goldstein, B. A., Kibbe, W. A., and Dunn, J. P. (2020).
Investigating sources of inaccuracy in wearable optical heart rate
sensors. *npj Digital Medicine* 3: 18.

Birchwood, M., Spencer, E., and McGovern, D. (2000). Schizophrenia:
early warning signs. *Advances in Psychiatric Treatment* 6(2): 93–101.

Brooks, R. A. (1991). Intelligence without representation. *Artificial
Intelligence* 47(1–3): 139–159.

Burr, D. C., Morrone, M. C., and Ross, J. (1994). Selective suppression
of the magnocellular visual pathway during saccadic eye movements.
*Nature* 371(6497): 511–513.

CIRWEL (2026). *anima-mcp: Lumen — Pi-based creature with sensors,
display, and UNITARES governance*. Software repository.
https://github.com/CIRWEL/anima-mcp.

CIRWEL (2026). *eisv-lumen: three-layer benchmark for dynamics-emergent
voice and governance*. Software repository.
https://github.com/CIRWEL/eisv-lumen. Companion dataset of 32,181
trajectory windows (20,655 real Lumen + 11,526 class-balanced
synthetic) across 9 shape classes,
https://huggingface.co/datasets/hikewa/unitares-eisv-trajectories
(revision aeb47055ee5f27cb93124e4e3df065301ada6909, pushed 2026-05-09).

CIRWEL (2026). *unitares: Digital proprioception for AI agents*.
Software repository. https://github.com/CIRWEL/unitares

Cole, J., and Paillard, J. (1995). Living without touch and peripheral
information about body position and movement: studies with deafferented
subjects. In Bermúdez, J. L., Marcel, A. J., and Eilan, N. (eds.),
*The Body and the Self*. MIT Press, 245–266.

Craig, A. D. (2002). How do you feel? Interoception: the sense of the
physiological condition of the body. *Nature Reviews Neuroscience*
3(8): 655–666.

Crone, E. A., and Dahl, R. E. (2012). Understanding adolescence as a
period of social-affective engagement and goal flexibility. *Nature
Reviews Neuroscience* 13(9): 636–650.

Damasio, A. R. (2010). *Self Comes to Mind: Constructing the Conscious
Brain*. Pantheon.

Dennett, D. C. (1991). *Consciousness Explained*. Little, Brown.

Erikson, E. H. (1968). *Identity: Youth and Crisis*. W. W. Norton.

Finn, E. S., Shen, X., Scheinost, D., Rosenberg, M. D., Huang, J.,
Chun, M. M., Papademetris, X., and Constable, R. T. (2015). Functional
connectome fingerprinting: identifying individuals using patterns of
brain connectivity. *Nature Neuroscience* 18(11): 1664–1671.

Friston, K. (2010). The free-energy principle: a unified brain theory?
*Nature Reviews Neuroscience* 11(2): 127–138.

Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., and
Pezzulo, G. (2017). Active inference: a process theory. *Neural
Computation* 29(1): 1–49.

Friston, K. J., Stephan, K. E., Montague, R., and Dolan, R. J. (2014).
Computational psychiatry: the brain as a phantastic organ. *The Lancet
Psychiatry* 1(2): 148–158.

Gazzaniga, M. S. (2000). Cerebral specialization and interhemispheric
communication: does the corpus callosum enable the human condition?
*Brain* 123(7): 1293–1326.

Gazzaniga, M. S., and LeDoux, J. E. (1978). *The Integrated Mind*.
Plenum Press.

Geronimus, A. T. (1992). The weathering hypothesis and the health of
African-American women and infants: evidence and speculations.
*Ethnicity & Disease* 2(3): 207–221.

Gordon, E. M., Laumann, T. O., Gilmore, A. W., Newbold, D. J., Greene,
D. J., Berg, J. J., Ortega, M., Hoyt-Drazen, C., Gratton, C., Sun, H.,
Hampton, J. M., Coalson, R. S., Nguyen, A. L., McDermott, K. B.,
Shimony, J. S., Snyder, A. Z., Schlaggar, B. L., Petersen, S. E.,
Nelson, S. M., and Dosenbach, N. U. F. (2017). Precision functional
mapping of individual human brains. *Neuron* 95(4): 791–807.

Gratton, C., Laumann, T. O., Nielsen, A. N., Greene, D. J., Gordon, E.
M., Gilmore, A. W., Nelson, S. M., Coalson, R. S., Snyder, A. Z.,
Schlaggar, B. L., Dosenbach, N. U. F., and Petersen, S. E. (2018).
Functional brain networks are dominated by stable group and individual
factors, not cognitive or daily variation. *Neuron* 98(2): 439–452.

Hassabis, D., Kumaran, D., Summerfield, C., and Botvinick, M. (2017).
Neuroscience-inspired artificial intelligence. *Neuron* 95(2): 245–258.

Heim, C., and Nemeroff, C. B. (2001). The role of childhood trauma in
the neurobiology of mood and anxiety disorders. *Biological Psychiatry*
49(12): 1023–1039.

Hirstein, W. (2005). *Brain Fiction: Self-Deception and the Riddle of
Confabulation*. MIT Press.

Hobson, J. A. (2009). REM sleep and dreaming: towards a theory of
protoconsciousness. *Nature Reviews Neuroscience* 10(11): 803–813.

Howieson, D. (2019). Current limitations of neuropsychological tests
and assessment procedures. *The Clinical Neuropsychologist* 33(2):
200–208.

Huys, Q. J. M., Maia, T. V., and Frank, M. J. (2016). Computational
psychiatry as a bridge from neuroscience to clinical applications.
*Nature Neuroscience* 19(3): 404–413.

Insel, T. R. (2017). Digital phenotyping: technology for a new science
of behavior. *JAMA* 318(13): 1215–1216.

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang,
Y. J., Madotto, A., and Fung, P. (2023). Survey of hallucination in
natural language generation. *ACM Computing Surveys* 55(12): 248.

Juster, R.-P., McEwen, B. S., and Lupien, S. J. (2010). Allostatic load
biomarkers of chronic stress and impact on health and cognition.
*Neuroscience & Biobehavioral Reviews* 35(1): 2–16.

Kalai, A. T., and Vempala, S. S. (2024). Calibrated language models
must hallucinate. In *STOC '24: Proceedings of the 56th Annual ACM
Symposium on Theory of Computing*, 160–171.

Karlamangla, A. S., Singer, B. H., McEwen, B. S., Rowe, J. W., and
Seeman, T. E. (2002). Allostatic load as a predictor of functional
decline: MacArthur studies of successful aging. *Journal of Clinical
Epidemiology* 55(7): 696–710.

Kopelman, M. D. (1987). Two types of confabulation. *Journal of
Neurology, Neurosurgery, and Psychiatry* 50(11): 1482–1487.

Krakauer, J. W., Ghazanfar, A. A., Gomez-Marin, A., MacIver, M. A.,
and Poeppel, D. (2017). Neuroscience needs behavior: correcting a
reductionist bias. *Neuron* 93(3): 480–490.

Langton, C. G. (1989). Artificial life. In Langton, C. G. (ed.),
*Artificial Life*. Addison-Wesley, 1–47.

Laumann, T. O., Gordon, E. M., Adeyemo, B., Snyder, A. Z., Joo, S. J.,
Chen, M.-Y., Gilmore, A. W., McDermott, K. B., Nelson, S. M.,
Dosenbach, N. U. F., Schlaggar, B. L., Mumford, J. A., Poldrack, R. A.,
and Petersen, S. E. (2015). Functional system and areal organization of
a highly sampled individual human brain. *Neuron* 87(3): 657–670.

Loftus, E. F. (1979). *Eyewitness Testimony*. Harvard University Press.

Loftus, E. F., and Pickrell, J. E. (1995). The formation of false
memories. *Psychiatric Annals* 25(12): 720–725.

Lupien, S. J., McEwen, B. S., Gunnar, M. R., and Heim, C. (2009).
Effects of stress throughout the lifespan on the brain, behaviour and
cognition. *Nature Reviews Neuroscience* 10(6): 434–445.

Marín, G., and Chaudhary, J. (2026). Governing what you cannot observe:
adaptive runtime governance for autonomous AI agents. arXiv:2604.24686.

Mashour, G. A., and Hudetz, A. G. (2017). Bottom-up and top-down
mechanisms of general anesthetics modulate different dimensions of
consciousness. *Frontiers in Neural Circuits* 11: 44.

Maturana, H. R., and Varela, F. J. (1980). *Autopoiesis and Cognition:
The Realization of the Living*. D. Reidel.

McEwen, B. S. (1998). Protective and damaging effects of stress
mediators. *New England Journal of Medicine* 338(3): 171–179.

McEwen, B. S. (2003). Mood disorders and allostatic load. *Biological
Psychiatry* 54(3): 200–207.

McEwen, B. S. (2007). Physiology and neurobiology of stress and
adaptation: central role of the brain. *Physiological Reviews* 87(3):
873–904.

McEwen, B. S., and Stellar, E. (1993). Stress and the individual:
mechanisms leading to disease. *Archives of Internal Medicine* 153(18):
2093–2101.

McLoughlin, S., Kenny, R. A., and McCrory, C. (2020). Does the choice
of allostatic load scoring algorithm matter for predicting age-related
health outcomes? *Psychoneuroendocrinology* 120: 104789.

Nisbett, R. E., and Wilson, T. D. (1977). Telling more than we can
know: verbal reports on mental processes. *Psychological Review* 84(3):
231–259.

Onnela, J.-P., and Rauch, S. L. (2016). Harnessing smartphone-based
digital phenotyping to enhance behavioral and mental health.
*Neuropsychopharmacology* 41(7): 1691–1696.

Pezzulo, G., Parr, T., and Friston, K. (2018). The evolution of brain
architectures for predictive coding and active inference.
*Philosophical Transactions of the Royal Society B* 379(1893): 20220514.

Pfeifer, R., and Bongard, J. C. (2007). *How the Body Shapes the Way
We Think: A New View of Intelligence*. MIT Press.

Poldrack, R. A., Baker, C. I., Durnez, J., Gorgolewski, K. J., Matthews,
P. M., Munafò, M. R., Nichols, T. E., Poline, J.-B., Vul, E., and
Yarkoni, T. (2017). Scanning the horizon: towards transparent and
reproducible neuroimaging research. *Nature Reviews Neuroscience*
18(2): 115–126.

Proske, U., and Gandevia, S. C. (2012). The proprioceptive senses:
their roles in signaling body shape, body position and movement, and
muscle force. *Physiological Reviews* 92(4): 1651–1697.

Rascovsky, K., Hodges, J. R., Knopman, D., Mendez, M. F., Kramer, J. H.,
Neuhaus, J., van Swieten, J. C., Seelaar, H., Dopper, E. G. P., Onyike,
C. U., Hillis, A. E., Josephs, K. A., Boeve, B. F., Kertesz, A.,
Seeley, W. W., Rankin, K. P., Johnson, J. K., Gorno-Tempini, M.-L.,
Rosen, H., Prioleau-Latham, C. E., Lee, A., Kipps, C. M., Lillo, P.,
Piguet, O., Rohrer, J. D., Rossor, M. N., Warren, J. D., Fox, N. C.,
Galasko, D., Salmon, D. P., Black, S. E., Mesulam, M., Weintraub, S.,
Dickerson, B. C., Diehl-Schmid, J., Pasquier, F., Deramecourt, V.,
Lebert, F., Pijnenburg, Y., Chow, T. W., Manes, F., Grafman, J.,
Cappa, S. F., Freedman, M., Grossman, M., and Miller, B. L. (2011).
Sensitivity of revised diagnostic criteria for the behavioural variant
of frontotemporal dementia. *Brain* 134(9): 2456–2477.

Rath, A. (2026). Agent drift: quantifying behavioral degradation in
multi-agent LLM systems over extended interactions. arXiv:2601.04170.

Ravindran, S. (2025). A predictive framework for AI value alignment and
drift prevention. arXiv:2510.04073.

Schacter, D. L. (1999). The seven sins of memory: insights from
psychology and cognitive neuroscience. *American Psychologist* 54(3):
182–203.

Seeman, T. E., McEwen, B. S., Rowe, J. W., and Singer, B. H. (2001).
Allostatic load as a marker of cumulative biological risk: MacArthur
studies of successful aging. *Proceedings of the National Academy of
Sciences* 98(8): 4770–4775.

Seeman, T. E., Singer, B. H., Rowe, J. W., Horwitz, R. I., and McEwen,
B. S. (1997). Price of adaptation — allostatic load and its health
consequences: MacArthur studies of successful aging. *Archives of
Internal Medicine* 157(19): 2259–2268.

Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied
self. *Trends in Cognitive Sciences* 17(11): 565–573.

Sherrington, C. S. (1900). The muscular sense. In Schäfer, E. A. (ed.),
*Textbook of Physiology, Volume 2*. Pentland, 1002–1025.

Sperling, R. A., Aisen, P. S., Beckett, L. A., Bennett, D. A., Craft,
S., Fagan, A. M., Iwatsubo, T., Jack, C. R. Jr., Kaye, J., Montine, T.
J., Park, D. C., Reiman, E. M., Rowe, C. C., Siemers, E., Stern, Y.,
Yaffe, K., Carrillo, M. C., Thies, B., Morrison-Bogorad, M., Wagster,
M. V., and Phelps, C. H. (2011). Toward defining the preclinical stages
of Alzheimer's disease: recommendations from the National Institute on
Aging-Alzheimer's Association workgroups on diagnostic guidelines for
Alzheimer's disease. *Alzheimer's & Dementia* 7(3): 280–292.

Sterling, P. (2012). Allostasis: a model of predictive regulation.
*Physiology & Behavior* 106(1): 5–15.

Sterling, P., and Eyer, J. (1988). Allostasis: a new paradigm to
explain arousal pathology. In Fisher, S., and Reason, J. (eds.),
*Handbook of Life Stress, Cognition and Health*. Wiley, 629–649.

Stuss, D. T., and Levine, B. (2002). Adult clinical neuropsychology:
lessons from studies of the frontal lobes. *Annual Review of Psychology*
53: 401–433.

Torous, J., Kiang, M. V., Lorme, J., and Onnela, J.-P. (2016). New
tools for new research in psychiatry: a scalable and customizable
platform to empower data driven smartphone research. *JMIR Mental
Health* 3(2): e16.

Volkmann, F. C., Riggs, L. A., and Moore, R. K. (1980). Eyeblinks and
visual suppression. *Science* 207(4433): 900–902.

Vuilleumier, P. (2004). Anosognosia: the neurology of beliefs and
uncertainties. *Cortex* 40(1): 9–17.

Wang, C. L., Singhal, T., Kelkar, A., and Tuo, J. (2025a). MI9 — Agent
Intelligence Protocol: runtime governance for agentic AI systems.
arXiv:2508.03858.

Wang, H., Poskitt, C. M., Wei, J., and Sun, J. (2025b). ProbGuard:
probabilistic runtime monitoring for LLM agent safety.
arXiv:2508.00500.

Wang, K. (2026a). UNITARES: Information-theoretic governance of
heterogeneous agent fleets. Published April 20, 2026. *Zenodo*.
https://doi.org/10.5281/zenodo.19647159 (concept DOI; v6.9.1
https://doi.org/10.5281/zenodo.19722512, April 24, 2026).

Wang, K. (2026b). Trajectory Identity: A Mathematical Framework for
Enactive AI Self-Hood. Published May 9, 2026. *Zenodo*.
https://doi.org/10.5281/zenodo.20098168 (concept DOI; v0.11.1
https://doi.org/10.5281/zenodo.20098169). Source repository:
https://github.com/cirwel/trajectory-identity-paper. Referenced as
*TIWD* in the body text.

Wijdicks, E. F. M. (2019). Being comatose: why definition matters.
*The Lancet Neurology* 18(11): 977.

Wilson, T. D. (2002). *Strangers to Ourselves: Discovering the Adaptive
Unconscious*. Harvard University Press.

Wurtz, R. H. (2008). Neuronal mechanisms of visual stability. *Vision
Research* 48(20): 2070–2089.
