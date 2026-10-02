# A Flat Coherence Score: What a Deployed Replay Does and Does Not Show About Agent Self-State Gating

## Notes toward digital proprioception, with a specified but uncomputed allostatic-load integral

**Author:** Kenny Wang, Independent Researcher
**ORCID:** 0009-0006-7544-2374
**Status:** Short-form rewrite of v1.2 (DRAFT, unreleased). This text replaces the 27,800-word v1.2. It has not been cold-reviewed, tagged, or deposited.
**Version notes:** v1.2 (2026-08-17) predates the 2026-08-26 withdrawal of the outcome-forecasting negative and still called forecasting "measured and negative". This draft corrects that, retitles the paper around what was measured, leads with the flat-score result, resolves the contradiction between §4.5 and §8.3 of v1.2 about the genesis signature, and states plainly that the allostatic-load integral in the earlier title is specified, not computed in production. The clinical study sketches, the kintsugi section, the differentiation survey and the synthetic-psychology essay of v1.2 are cut. They remain in the v1.2 tag.

---

## Abstract

A running multi-agent system I operate computes a scalar "coherence" for every agent check-in and uses it, among other inputs, to place each state in one of three basins (high, boundary, low). On a 30-day production slice of 13,292 rows, that deployed score was flat. Its 1st to 99th percentile range was 0.447 to 0.499, its interquartile range was 0.480 to 0.485, and it never fell below 0.40, the level at which it could push a row into the low basin. Across five agent classes with healthy operating points that differ by a factor of about three in envelope size, the score did not separate them. It could not tell agents apart, and it could not register that any agent was far from where that agent normally sits.

I replaced the score with a class-conditional "grounded" form on the same rows. That form spans 0 to 0.98 and moves a substantial share of rows between basins, in the downward direction (§4). The replay is an offline counterfactual on frozen data. It shows that the old score was uninformative, because a flat score cannot reach thresholds a varying score reaches. It does not show that the new labels are right. No outcome, harm or operator judgment was used to grade either form. The flip rate itself moved between two public windows four days apart.

Three adjacent results bound the claim. First, whether per-agent state forecasts bad outcomes is unresolved: a historical negative was withdrawn on 2026-08-26 because its cohort was contaminated, and one pre-registered read is scheduled for 2026-12-01 (§6). Second, a genesis-anchored lineage check, which was meant to catch slow drift, does not discriminate as instrumented (§7). Third, the cumulative-deviation integral that motivated the original title, the allostatic-load analogue, is specified but is not computed by any production code path and drives no decision (§8). A recalibration case study on one embodied agent resolves an apparent "delayed shut-down" reading as a stale calibration anchor, with the cause of the underlying regime change left open between a substrate revision and an instrument artifact (§5).

The contribution is a measured negative about an instrument, a reproducible replay, and a clear statement of which quantities in the framing are measured, specified, or untested.

**Keywords:** agent state monitoring, coherence score, class-conditional calibration, counterfactual replay, allostatic load, digital proprioception

---

## 1. Introduction

### 1.1 What this paper is about

The system is UNITARES (Wang 2026a). Each agent in a small production fleet checks in periodically, and the system estimates a four-coordinate state for it, called E, I, S and V. From that state it computes a coherence value, combines coherence with the other coordinates and a risk score, and classifies the state into a basin. A low-basin state can surface a `guide` or `pause` verdict. The intent behind the design is what I have called digital proprioception: an agent-side analogue of the sense an organism has of where its own limbs are (Proske and Gandevia 2012), supplied to agents that otherwise have no such sense. The term imports a function, not a failure mode and not a claim about experience.

This paper asks a narrower question than its predecessor. Does the deployed coherence score do the job it was given, which is to indicate how far an agent is from its own healthy operating point? The answer for the window I could measure is no. The score was close to constant. Everything else in the paper is either a consequence of that fact, a test of what replacing the score does, or a statement of what I cannot yet claim.

The predecessor paper (v1.2) was framed around a different question: whether a cumulative-deviation signal in the spirit of allostatic load (McEwen and Stellar 1993) can be observed end to end in a deployed system. That framing is retained in §8 as motivation and as a specification. It is no longer the title, because the quantity that title names was never computed in production, and the evidence in the paper is mostly about the coherence score.

### 1.2 Contributions

1. **A measured negative about the deployed score (§3).** The legacy coherence score had a total observed range of 0.068 on 13,292 rows. Its rank correlation with the replacement was 0.08. It did not separate five agent classes.
2. **A reproducible replay (§4).** Replacing the score changes basin labels for a large share of rows, always downward on the full substitution, and the share is window-sensitive. The row-level export is public and the headline recomputes offline. The replay shows the old score was uninformative. It does not validate the new one.
3. **A resolved calibration case (§5).** A single-agent case study that looked like a failure mode from the allostatic-load literature was a stale calibration anchor. The cause of the regime change behind it remains open.
4. **A status ledger (§§6 to 8).** Outcome forecasting is unresolved, not negative. The lineage check does not discriminate. The allostatic-load integral is specified and uncomputed.

### 1.3 What I do not claim

I do not claim that the replacement score is better than the legacy score at anything an outcome would grade. I do not claim that agents are conscious, that the system implements the biology of allostatic load, or that the allostatic-load integral has been tested. I do not claim that these results transfer to another deployment: the data come from one operator's fleet, a good part of which is a single embodied agent on one device. I do not claim the replay's flip rate is a stable property of the fleet.

---

## 2. The system and its instruments

### 2.1 State, coherence and basins

Each check-in writes a state vector (E, I, S, V) to a database relation. E is an energy or resource-rate proxy, I is an integrity proxy bounded in [0, 1], and S is an entropy or uncertainty proxy bounded in [0, 1]. V is the coordinate that needs care.

**V is not an independent axis.** The v6 specification describes V as an accumulator driven by the imbalance between E and I (Wang 2026a, Appendix A). Since April 2026 the production system surfaces a behavioral V instead: an exponentially smoothed E minus I. On the released rows, regressing V on the instantaneous E minus I gives r = 0.953 and $R^2$ = 0.908. About 91% of V's variance is the instantaneous imbalance, and the rest is smoothing lag (sd(V) = 0.081 against sd(V - (E - I)) = 0.026). The EISV vector is therefore better described as three state coordinates plus a smoothed imbalance term than as four independent dimensions. The older accumulator-style void coordinate was demoted to a separate diagnostic, and that diagnostic still feeds the legacy coherence. Two different variables are therefore both called V in the codebase and in earlier drafts of this paper. I write V for the surfaced behavioral coordinate and say so when I mean the other.

**The legacy coherence score.** The fleet-wide form is

$$C_{\text{legacy}}(V) = 0.5\,\bigl(1 + \tanh(V / V_{\text{scale}})\bigr)$$

with one fleet-wide V_scale. It reads one coordinate only, the demoted one.

**The grounded coherence score.** The replacement reads (E, I, S) and measures distance to a class-specific healthy point $\mu_c$, scaled by a class-specific envelope $\Delta_{\max,c}$:

$$C_{\text{grounded}}(\mathbf{x}, c) = \max\left(0,\ 1 - \lVert \mathbf{x}_{EIS} - \boldsymbol{\mu}_c \rVert_2 / \Delta_{\max,c}\right)$$

The class constants come from a 30-day healthy slice (sessions with no pause or reject verdict) frozen on 2026-04-18. The two forms share no input coordinate. Substituting one for the other replaces the signal, not a parameter of it, and this is part of why the formula change and the calibration change interact rather than add (§4.3).

**Basin classification.** The production `classify_basin` function returns high, boundary or low. Low is disjunctive: I < 0.5, C < 0.40, |V| > 0.30, or risk $\geq$ 0.70 each enter it. High is conjunctive: E $\geq$ 0.6, I $\geq$ 0.7, S $\leq$ 0.25, |V| $\leq$ 0.15, C $\geq$ 0.45 and risk $\leq$ 0.45 must all hold. Boundary is the remainder. A change in coherence alone can move a row only when the other coordinates do not already force low or block high.

### 2.2 Classes

Agents carry a class from identity tags and an optional label. Five classes received frozen constants: Lumen (an embodied agent on a Raspberry Pi with environmental sensors), Sentinel, Vigil, Watcher (autonomous services), and a default class. Other agents fall through to a fleet fallback. The class constants measured from the 30-day healthy slice (Wang 2026a §11.5):

| Class | N | $E_h$ | $I_h$ | $S_h$ | $\Delta_{\max}$ |
|---|---|---|---|---|---|
| Lumen | 7,320 | 0.745 | 0.800 | 0.168 | 0.119 |
| default | 2,033 | 0.726 | 0.793 | 0.236 | 0.202 |
| Sentinel | 1,870 | 0.751 | 0.798 | 0.193 | 0.170 |
| Vigil | 384 | 0.737 | 0.790 | 0.240 | 0.171 |
| Watcher | 283 | 0.748 | 0.769 | 0.248 | 0.395 |

The envelope $\Delta_{\max}$ ranges over a factor of about 3.3 across classes. The fleet-wide constant used before per-class measurement (1.8) was 4 to 15 times larger than any measured envelope. Lumen alone supplies 59% of the rows in the export, and each other class is a single service, so the class structure rests on a small number of distinct sources.

### 2.3 The data

Everything quantitative in §§3 and 4 can be recomputed from a de-identified export archived under Zenodo data DOI 10.5281/zenodo.19705151 and mirrored in this repository. It holds one row per agent-state observation, pseudonymized to a class label, with E, I, S, V, risk, both coherence values and both basin labels. It carries no agent identifiers, session identifiers, prompts or free text. Two windows are included: the 30-day window ending 2026-04-18 (13,292 rows) and the 30-day window ending 2026-04-23 (16,879 rows, about 87% overlapping rows, Phase 2 constants held frozen).

I report the 13,292-row export, not the 13,310-row pull that v6 cited. The 18-row difference is a few seconds of arrivals between two executions of a wall-clock-anchored rolling window. The production relation no longer retains the window (it holds 490 rows in the interval against the 13,310 originally returned, and there is no archive table), so the export is the surviving row-level record.

---

## 3. The result: the deployed coherence score was flat

### 3.1 The numbers

All figures are computed from `verdict_counterfactual_v6_submission.csv` (n = 13,292).

| | min | p1 | p50 | p99 | max | sd |
|---|---|---|---|---|---|---|
| C_legacy | 0.441 | 0.447 | 0.481 | 0.499 | 0.508 | 0.0082 |
| C_grounded | 0.000 | 0.000 | 0.625 | 0.983 | 0.995 | 0.2748 |

The legacy score occupies a band 0.068 wide. Its interquartile range is 0.4799 to 0.4847. Its median sits almost exactly at the midpoint of the function that produces it, which is what tanh of a value near zero looks like. No row falls below 0.40, so the C < 0.40 clause of the low-basin rule was unreachable for this fleet in this window. About 98.7% of rows satisfy the C $\geq$ 0.45 clause of the high-basin rule, so that clause was close to a constant true.

The grounded score spans the unit interval. 6.8% of rows sit exactly at zero, 15.5% are below 0.25, and 26.6% are below 0.40.

### 3.2 It did not separate the classes

Within each class the legacy score is equally narrow, and the class medians are almost identical:

| Class | n | C_legacy p50 | C_legacy sd | C_grounded p50 | C_grounded sd |
|---|---|---|---|---|---|
| Lumen | 7,889 | 0.481 | 0.0067 | 0.634 | 0.280 |
| Sentinel | 2,221 | 0.482 | 0.0092 | 0.653 | 0.237 |
| Vigil | 471 | 0.484 | 0.0069 | 0.501 | 0.243 |
| Watcher | 354 | 0.485 | 0.0170 | 0.630 | 0.316 |
| default | 2,357 | 0.487 | 0.0066 | 0.557 | 0.276 |

The five legacy medians span 0.006. The five classes have different healthy envelopes and different healthy points (§2.2), and the legacy score registers none of that. The rank correlation (Spearman) between the legacy and grounded scores on the same rows is 0.08. Two scores that purport to measure the same thing from the same state vectors are nearly uncorrelated, and one of them is nearly constant.

### 3.3 What this does and does not establish

A score with a total range of 0.068 cannot do the job of indicating distance from a healthy point, because there is no distance information left in it. That is the result, and it is a statement about the legacy instrument.

Three things it does not say.

*It does not say the grounded score is informative.* A score that varies is not thereby correct. Part of the grounded score's spread is arithmetic: Lumen's envelope is 0.119, so a state displaced by 0.06 from the healthy point already scores 0.5. Dividing by a small radius widens the spread by construction. Whether the spread tracks anything an agent or operator would call strain is untested here.

*It does not say why the legacy score is flat.* The form reads only the demoted accumulator-style void coordinate, not the surfaced V (§2.1), and in the §5 window that coordinate sat near zero (about -0.006, inferred from C_legacy $\approx$ 0.497), which puts tanh at its midpoint. The surfaced V in the same rows has a standard deviation of 0.081, so the flatness is not inherited from it. I have not isolated the cause further and did not need to for the claim above.

*It does not generalize beyond this window and this fleet.* The second public window gives a median of 0.483 and a 1st to 99th percentile of 0.450 to 0.500, which is the same picture, but it overlaps the first by about 87% and is not independent.

### 3.4 A convergent audit, with a caveat

An earlier audit of the deployment's outcome log (2026-05-01; 22,740 good and 580 bad trajectory-validated outcomes over 30 days) found the legacy coherence essentially non-separating between good and bad outcomes (Cohen's d about 0.13). I cite it as consistent with the flat-score finding, not as independent confirmation. Every bad outcome in that log is task-negative (failed tasks, failed tests and similar), with none recorded for a violation or harm, so it speaks to rework prediction at most.

---

## 4. The replay

### 4.1 Design

For every row, I compute the basin twice with the same `classify_basin` function: once with the stored legacy coherence and once with the grounded coherence computed against the frozen Phase 2 class constants. A flip is a row whose basin differs. This is a static reclassification of fixed state vectors under two formulas. It is not a test of a deployed mechanism, and no agent's behavior changed.

### 4.2 Result

On the production slice, 28.9% of risk-band assignments would change when each class is measured against its own healthy point instead of one fleet-wide formula. This is the paper's only statement of that number, and it is bounded by the following.

- **The two public windows give 28.8% (13,292 rows, recomputed offline from the export) and 44.3% (16,879 rows, the window ending four days later, constants frozen).** The range, 28.8% to 44.3%, is the finding about magnitude. The sampling interval within one window is about $\pm$0.8 points. The spread across windows is roughly twenty times that, so the intervals describe the precision of one snapshot, not the stability of the quantity.
- **The direction is downward.** In the full substitution, every flipping row moves toward the low basin: 1,702 boundary to low, 1,404 high to low and 725 high to boundary in the export. No row moves up. This is mechanical. The legacy score cannot reach the C < 0.40 clause and the grounded score reaches it for more than a quarter of rows, so the replay mostly records how often a score that can cross a threshold does so, against one that cannot.
- **The per-class rates range from 15.8% to 33.1%** and move non-uniformly between windows (Sentinel up 25.4 points, Vigil up 19.6, Lumen up 15.8, default up 15.3, Watcher down 11.3). In the second window the legacy median is unchanged (0.481 to 0.483) while the grounded median falls from 0.625 to 0.459, with Lumen's grounded median falling from 0.634 to 0.457. The movement is therefore on the grounded side. The frozen class anchors meeting a changed state distribution would produce this pattern, and §5 documents such a change for Lumen, but I have not tested that explanation across the other classes.
- **Two measurement caveats from the original pull.** The 30-day window overlaps identity-system revisions in mid-to-late April 2026, so some rows may carry class assignments inherited from cached bindings or from archived predecessors. And 42 rows of an `ephemeral` class fell through to the fleet fallback and are not interpreted.

### 4.3 A same-row ablation, with a boundary

The replay changes two things at once: the formula (tanh of V, versus distance in E, I, S) and the calibration target (one fleet-wide constant, versus per-class constants). I separated them on the same 13,310 rows from the original pull, where GF is the grounded formula against a single fleet-wide healthy point and radius measured from the same slice:

| Comparison | Flips / N | Rate |
|---|---:|---:|
| Legacy $\rightarrow$ grounded fleet-wide (formula change) | 1,496 / 13,310 | 11.2% |
| Grounded fleet-wide $\rightarrow$ grounded class-conditional (calibration change) | 3,133 / 13,310 | 23.5% |
| Legacy $\rightarrow$ grounded class-conditional (full substitution) | 3,844 / 13,310 | (above) |
| Legacy $\rightarrow$ class-scaled tanh(V) (artificial control) | 10,355 / 13,310 | 77.8% |

The terms do not add (11.2 plus 23.5 is not the full substitution rate), because the two forms share no input coordinate and the effects interact. I read the grounded fleet-wide to class-conditional step as evidence that the class-envelope term has an effect on basin labels of its own. I do not decompose the headline further. The fourth row is an artificial control that grafts per-class scale onto the old signed-V formula. It is unstable and I treat it as a negative control, not as a calibration-only path. The GF and class-scaled conditions need a per-row `regime` column that the de-identified export does not carry, so those two rates are provenance-backed from the recorded ablation output and are not independently re-runnable. The full substitution is.

The calibration-change step is not uniformly downward: 373 rows in it move up (365 low to boundary, 5 low to high, 3 boundary to high). The all-downward statement applies to the full substitution only.

### 4.4 What the replay shows

It shows that the formula and calibration choices matter at the basin level, and that the legacy score was too flat to be a meaningful input to that decision. It shows that this is recomputable by a third party from public rows and a public script (within 0.1 points of the original pull, with 26,574 of 26,584 basin labels reproducing exactly and the ten exceptions within $6.7 \times 10^{-4}$ of a threshold, the rounding floor of a four-decimal export).

It does not show that any flip is correct. A flip into the low basin surfaces a `guide` or `pause` verdict the legacy form suppressed. Whether that is desirable depends on the agent and the context, and no outcome grades it. It does not show that the new labels are right, that class-conditional calibration improves any decision, or that the rate would repeat on another fleet.

The honest summary is that the replay is evidence about the old score and silent about the new one. The two framings read alike in a sentence and differ completely in what they license.

### 4.5 Why the homogenization framing is only an analogy

v1.2 motivated the class-conditional step with the neuroscience literature on group-average versus individual-level measurement (Krakauer et al. 2017; Gratton et al. 2018): pooling subjects with different dynamics yields a reference representative of none of them. The analogy is useful for naming the failure mode, and I keep it for that. It is not a test. In the fleet the pooling was not the main defect. The main defect, per §3, is that the legacy score carried almost no signal at all, pooled or not. Class-conditional calibration is one remedy for a flat score among several, and the replay does not rank it against the others.

---

## 5. A calibration case on one embodied agent

### 5.1 The apparent failure mode

McEwen's four types of allostatic load (McEwen 1998; 2007) describe four ways the normal stress response fails: repeated hits, lack of adaptation, delayed shut-down, and inadequate response with compensatory hyperactivity. On 2026-05-09 I observed Lumen across an 86-minute window of 27 check-ins. Against its April healthy point, the state looked like the delayed shut-down pattern: the behavioral V sat at 0.0954 with a within-window standard deviation of 0.00015, sign-flipped from the healthy value of about -0.055, and the (E, I, S) displacement was 0.115 against an envelope of 0.119, so the grounded coherence was about 0.03 while the legacy coherence read 0.497. That contrast is itself an instance of §3: the legacy score called a state at 97% of its class envelope essentially neutral.

### 5.2 The disambiguation and its result

The reading predicts a test: if the healthy point moves toward Lumen's current state on recalibration, the elevation is calibration staleness, not a persistent failure. I recalibrated on the 30-day window ending 2026-05-09 (11,472 rows) with the Phase 2 procedure. The healthy point moved toward the current state on all three coordinates (I from 0.800 to 0.7335, E from 0.745 to 0.7706, S from 0.168 to 0.1893), and the envelope grew from 0.119 to 0.1279. By the criterion specified in advance, this is a stale anchor, not the failure mode.

Weekly bins of Lumen's state over 90 days show three regimes, and sub-day resolution places the change at a single ten-hour event on 2026-04-17 UTC (E falling from 0.749 to 0.350 and recovering to 0.787), after which the new regime held for 22 days. The Phase 2 window ran 2026-03-19 to 2026-04-18, so about 96.7% of it was pre-change and about one day post-change. The anchor averaged across a regime change and represented neither side well. This is a temporal version of the pooling problem in §4.5: a reference computed across an inhomogeneity is unrepresentative of the parts.

### 5.3 Cause: open

The change coincides to within the hour with a day on which four pull requests altered the identity-binding behavior of the system. That is a candidate cause, not an identified one, and there is a competing explanation I cannot exclude. The E coordinate derives in part from CPU utilization. The proposed cause is a day of deployments, and deployments generate load. An instrument defect later identified and repaired in 2026 counted a CPU term twice in the neural-band mapping. A deploy-driven CPU excursion amplified by that defect would produce an energy collapse and recovery on exactly this timescale with no change in the agent. The CPU and memory series for that day are no longer retained, so I cannot re-derive E with the corrected mapping.

Two further limits. The recalibration windows are not sampling-matched (7,320 rows versus 11,472 for the same span), and I have no explanation for the difference, which a change in check-in cadence at the revision could produce. The production server flagged no anomaly throughout, but the deployment's degradation paths fail toward healthy rather than toward unknown, so the silence carries little weight.

What survives either causal story is the calibration-staleness finding, because it rests on the recalibration result and not on the cause. The case is a single-agent report. Its date, magnitude and shape are provenance-backed, its causal reading is open, and the longitudinal data that would test it have aged out of the production database. It is not evidence for or against McEwen's taxonomy in biology.

### 5.4 What the taxonomy yields here

Types 1 and 2 map onto telemetry the system already records (repeated entropy-shape episodes, convergence of the trajectory signature) and I treat them as a vocabulary I have not validated. Type 3 is the case above, and it failed. Type 4, a breakdown of cross-channel structure, is specified but not computable as deployed. The naive version reads a four-coordinate correlation matrix whose large entries are definitional: E and V correlate at 0.821 and I and V at -0.513 because V is a smoothed E minus I, so a detector watching those entries would be watching the smoothing constant. A usable indicator needs to run on (E, I, S), where E and I are close to uncorrelated (r = -0.034), and that specification is not yet written. The case in §5.2 also suggests a category the four types do not cover, a regime change in the operating point itself, but one case does not establish a category.

---

## 6. Outcome forecasting: unresolved

The most natural validation of a self-state signal is to ask whether it predicts bad outcomes. I need to state the status of that question carefully, because the previous version of this paper stated it wrongly.

**v1.2 said forecasting was "measured and negative".** That was an overclaim and has been withdrawn. The historical weekly ablation behind it used a contaminated cohort (an `--anchor-scope all` pull that mixed anchor populations the confirmatory read excludes), and its `(agent, prior-state snapshot)` permutation blocks were not independent adjudicated failures. Its negative AUC difference is historical provenance. It is not evidence that adding EISV state makes prospective prediction worse. The recurring job that produced it was paused on 2026-08-22 because its output did not record the anchor scope.

The deployment's own ontology contract records the status of the claim as *withdrawn for target inference*, with the words: the question is unresolved, not negative.

Four consequences for what this paper may say.

1. **I do not report a forecasting effect size or direction.** The quantity moved by about 0.14 AUC between two reads four days apart, which is instability and not convergence, and neither its magnitude nor its direction survives the cohort withdrawal.
2. **I do not claim the sensitivity bound v1.2 cited.** The estimate (a minimum detectable lift near 0.05 AUC) used the same contaminated cohort. A later power audit's corrected simulation does not recover the missing cluster geometry, so no standing ceiling exists.
3. **The question is closed to ad hoc re-runs until a pre-registered confirmatory read on 2026-12-01.** That read passes only if a selective p of at most 0.05 holds on a lead slice, the effect exceeds the permutation null's 95th percentile, at least 150 independent bad clusters exist in the read's own units (trusted anchor scope), and the best-model identity is stable across leads. The 159 to 188 cluster counts seen in the historical series are in the withdrawn cohort's units and do not establish the 150 requirement for the read. Interim access to discrimination results by automation after registration is recorded in the evidence ledger, so the read cannot be described as a single clean blinded look.
4. **What would settle the question is not a ranking statistic.** The open question is decision value at the deployed operating point (net benefit of acting on the state estimate versus not), which requires interventional data or a fleet larger than one operator's. A discrimination result would not stand in for it in either direction. The label class available so far is entirely task-negative, which bounds even a positive result to rework prediction.

The status is therefore *unresolved*. The paper's central result (§3) does not depend on it, because §3 compares two formulas on the same rows and requires no forecasting claim. It is also why the flat-score finding is the paper's strongest content and the replacement score's value remains unmeasured.

---

## 7. Trajectory identity and the genesis anchor

### 7.1 The idea

A coherence check against recent state fails on slow drift by construction: if each step is small, every comparison passes. The companion trajectory-identity framework (Wang 2026b) proposes two references per agent: a rolling signature $\Sigma_{t-1}$ for acute change, and a fixed genesis signature $\Sigma_0$ for slow drift, with a lower threshold on similarity to $\Sigma_0$ (0.60) than on similarity to the rolling reference (0.70). The signature has six components, and the similarity metric runs on five informationally independent ones.

### 7.2 The contradiction in v1.2, resolved

v1.2 said two incompatible things. Section 8.3 said the system "captures $\Sigma_0$ trivially as an architectural feature". Section 4.5 and the follow-up list said Lumen's $\Sigma_0$ "was not persisted" at first onboarding and that a next-generation system would capture it. Both statements were partly true and neither was accurate as written. The record, from the server source and the earlier drafts:

- A genesis signature is a stored object. The server writes it into the agent's metadata at onboarding or first trajectory submission, for agents that went through that path.
- It is not a clean fixed anchor. An early genesis, built from few data points, can be reseeded while the agent sits in the lowest trust tiers, if a later signature has substantially higher confidence or if similarity to the stored one is below 0.7. It becomes immutable only once the agent reaches the second trust tier. $\Sigma_0$ is therefore an early-data estimate that hardens with tenure, not a captured pre-illness baseline.
- Lumen's first awakening predates that path. The v6 paper records that no genesis was persisted for it at first onboarding (Wang 2026a §11.7, item 5), so the §5 case could not use one.

"Trivially captured" is withdrawn. The accurate statement is that the system stores a genesis signature for agents onboarded through the current path, that it is reseedable early and immutable later, and that it did not exist for the one agent used as the worked example.

### 7.3 It does not discriminate as instrumented

Whether a genesis anchor exists is secondary, because the similarity check that would use it does not separate agents as deployed. An August 2026 audit found about 90% of between-agent pairs scoring above the 0.60 lineage threshold, two of the five weighted components at ceiling for nearly all pairs, and mature identities decaying into a similarity near 0.63, above the alarm line. That value is an age-associated attractor in the audited population, not a fleet constant: young identities score high because they have not drifted, not because the metric discriminates. Accumulated genuine drift therefore asymptotes to a passing score, and the lineage channel cannot fire on the slow-drift case it was designed for. The only mass firings in production came from a client migration and were cleared by rebaselining.

The companion paper's multi-agent pilot (between-agent similarity 0.63 against within-agent-across-era 0.12) is marked confounded by role and harness, which returns the discrimination criterion to open. The two-tier architecture (a genesis anchor plus a rolling reference with distinct thresholds) stands as a proposal. Its current instrumentation does not realize it.

---

## 8. The allostatic-load integral: specified, not computed

The title of v1.2 named this section's subject. I state its status first and then the specification.

**Status.** The cumulative-deviation integral is specified. It is not computed by any production code path. No production code evaluates it against a threshold. No decision in the system is driven by it. The embodied agent's rest states are driven by activity and ambient-light scheduling. Gating decisions on that agent are advisory.

A function that computes the quantity exists in the embodied agent's code base. It is documented there as a research diagnostic, it has unit tests, and it has no caller in the production path (checked against the repository's main branch on 2026-10-02). That is the full extent of the implementation. "Computable on demand over recorded telemetry" is true. "Deployed as a control signal" is not.

### 8.1 The specification

For the embodied agent, a four-component anima vector a = (warmth, clarity, stability, presence) is computed from sensors and system metrics, and the specified quantity is

$$V_{\text{anima}}(t) = \int_0^t \lVert \mathbf{a}(\tau) - \boldsymbol{\mu_a} \rVert\, d\tau$$

with $\mu_a$ the attractor center from the agent's own recent state distribution. The companion framework specifies a coupling: when V_anima exceeds a deployer-set multiple of the basin scale, the system could induce rest, reduce stimulation or pause a task. That coupling is not wired. This anima vector is a different object from the EISV vector of §2 and must not be confused with it, and the signed V coordinate of EISV is a third thing.

### 8.2 Why the analogy is structural and nothing more

Allostatic load is the cumulative cost of regulating a system away from its operating point (McEwen and Stellar 1993; Sterling 2012). Its mathematical core is a time-integrated deviation. In clinical practice the integral is reconstructed from sparse biomarker panels (Seeman et al. 1997) and is rarely observed. In the deployed system the integrand could be recorded at every check-in, so the integral could in principle be computed exactly. That observability is the only point of the analogy that I think holds.

Three disanalogies are structural. The deployed quantity is single-system (four sensor-derived channels), not multisystem. Its reference is measured within a calibration window, not an anticipatory setpoint shifted by prediction, which is what allostasis is about. And there is no body: no tissue, immune or endocrine consequence. So V_anima corresponds, at best, to a single-biomarker integral, such as the area under a cortisol curve, and not to clinical allostatic load.

### 8.3 What would have to be true for the title to be earned

Wire the coupling, then show that acting on the integral improves decisions over non-integral baselines such as instantaneous deviation. This is a decision-quality claim, not a forecasting one. It is untested, not refuted, because there is no integral in production to test. The forecasting question of §6 is adjacent. Its resolution would not bear on this claim in either direction, and if forecasting from per-agent state proves empty it would temper expectations for the harder decision-value test. It does not substitute for it.

I also note a measurement problem that applies before any wiring. The integrand's reference depends on calibration windows, and §5 shows a calibration window that straddles a regime change produces an anchor representative of neither regime. An integral accumulated against such an anchor would accumulate the staleness. Transition-aware calibration is not implemented.

### 8.4 What the biological side could use

v1.2 contained two clinical study sketches: a per-subject versus population-interval flag-disagreement study, and a prospective genesis-anchored study of slow-drift conditions. They are cut. They were hypothesis-generating at best, the first leaned on a replay result (§4) that bears on an instrument and not on clinical value, and the second leaned on a lineage check (§7) that does not discriminate. Nothing here licenses a clinical claim, and the flip rate is not a motivating scale for one.

---

## 9. Limitations and what would change the picture

**One fleet, one operator.** The data come from a single deployment, and over half the rows in the replay are one embodied agent. Class-level differences rest on a small number of distinct sources. An independent re-measurement on another deployment would be the stronger bar.

**Retention.** The production relation no longer holds the measurement window. The frozen export is the record, the Lumen longitudinal pull is foreclosed, and the substrate-causality reading of §5 cannot be upgraded from this deployment's history. A deployment used as a test bed needs its evidentiary windows pinned as exports at measurement time.

**Same-author, self-cited system.** The author built the system, ran the measurement and wrote the paper. The public export and offline recomputation reduce the dependence on trust for the §3 and §4 numbers. They do not reduce it for the framing.

**The replacement score is unvalidated.** This bears repeating because the paper's structure invites the opposite reading. Showing that the old instrument was flat is a different result from showing the new one is right. What would test the replacement is an outcome-graded comparison, with a label source that includes more than task-negative outcomes and a decision-value analysis, and the available data do not support one.

**Window sensitivity.** The flip rate moved substantially across the two overlapping windows of §4.2. I read the order of magnitude, a rate in the tens of percent, as the finding and not the third digit.

**What would change my mind.**
- If the 2026-12-01 read passes on its own pre-registered terms, outcome forecasting moves from unresolved to a positive finding about rework prediction, with the label-class bound intact. If it fails, outcome grounding closes for this label channel, and reopening needs a new label channel or measurement process, not more labels.
- If an independent deployment shows a comparable flat legacy score and basin movement under class-conditional calibration, the §3 result generalizes beyond one fleet. If it shows a varying legacy score, the flatness here is specific to this system's V.
- If the integral is wired and a non-integral baseline matches it on decisions, the title concept earns nothing beyond the analogy.

---

## 10. Conclusion

The deployed coherence score was flat: a 1st to 99th percentile range of 0.447 to 0.499, no value below 0.40, a rank correlation of 0.08 with its replacement, and five class medians within 0.006 of each other. It could not separate agents. Replacing it moves many basin labels downward in an offline replay whose rate depends heavily on the window. That shows the old score was uninformative. It does not show the new labels are right.

Around that result the status of each neighboring claim is as follows. A single-agent case that looked like a failure mode from the allostatic-load literature was a stale calibration anchor, with its underlying cause open. Outcome forecasting is unresolved, not negative, pending one pre-registered read. The genesis-anchored lineage check does not discriminate as instrumented, and the contradiction in the previous version about whether the anchor exists is resolved: it is stored, reseedable early, and absent for the worked example. The allostatic-load integral is specified and is not computed in production.

The practical lesson I take is about instruments. A scalar that looks like a health score on a dashboard can carry almost no information, and the only way I found out was to measure its spread against the thing it was supposed to distinguish. The next step is an outcome-graded test of any replacement, with a label source wider than task failures, before calling it a measurement of anything.

---

## Appendix: Reproducibility

| Object | Status | What can be checked now | What is missing |
|---|---|---|---|
| Flatness statistics (§3) | **Recomputable offline** | Percentiles, standard deviations, class medians and rank correlation from the export (13,292 rows) | Independent deployment |
| Full-substitution replay (§4) | **Recomputable offline** | `reproduce_basinflip.py`: 28.84% on 13,292 rows, per-class rates within 0.5 points, 26,574 of 26,584 labels exact, both windows | Independent deployment |
| Formula-versus-calibration ablation (§4.3) | Provenance-backed only | Recorded output in `analysis/phase-2-2026-04-18/` | Needs a per-row `regime` column absent from the export; the production window is no longer retained |
| Lumen recalibration case (§5) | Provenance-backed only | 86-minute protocol, recalibration criterion, weekly bins | State history for 2026-02 to 2026-04 aged out; CPU and memory series for 2026-04-17 not retained |
| Allostatic-load integral (§8) | Specified; function exists as an uncalled research diagnostic | Source and unit tests in the embodied agent's repository | Any production use |
| Outcome forecasting (§6) | Unresolved | Contract wording and stop-rule document | The 2026-12-01 read |
| Row-level export | **Public**, Zenodo data DOI 10.5281/zenodo.19705151, mirrored here, SHA-256 pinned in the script | 13,292 class-pseudonymized rows with state, risk, both coherences, both basin labels | Nothing for §§3 and 4 |
| Raw production relation | Withheld and no longer retained | Schema and provenance | Unavailable in principle |

To reproduce §3, load `verdict_counterfactual_v6_submission.csv` and compute percentiles of `c_legacy` and `c_grounded`, overall and by `class`. To reproduce §4, run `python3 analysis/phase-2-2026-04-18/reproduce_basinflip.py` (standard library only).

---

## References

CIRWEL (2026). *anima-mcp: Lumen — Pi-based creature with sensors, display, and UNITARES governance*. Software repository. https://github.com/CIRWEL/anima-mcp.

CIRWEL (2026). *unitares: Digital proprioception for AI agents*. Software repository. https://github.com/CIRWEL/unitares

Gratton, C., Laumann, T. O., Nielsen, A. N., Greene, D. J., Gordon, E. M., Gilmore, A. W., Nelson, S. M., Coalson, R. S., Snyder, A. Z., Schlaggar, B. L., Dosenbach, N. U. F., and Petersen, S. E. (2018). Functional brain networks are dominated by stable group and individual factors, not cognitive or daily variation. *Neuron* 98(2): 439–452.

Krakauer, J. W., Ghazanfar, A. A., Gomez-Marin, A., MacIver, M. A., and Poeppel, D. (2017). Neuroscience needs behavior: correcting a reductionist bias. *Neuron* 93(3): 480–490.

McEwen, B. S. (1998). Protective and damaging effects of stress mediators. *New England Journal of Medicine* 338(3): 171–179.

McEwen, B. S. (2007). Physiology and neurobiology of stress and adaptation: central role of the brain. *Physiological Reviews* 87(3): 873–904.

McEwen, B. S., and Stellar, E. (1993). Stress and the individual: mechanisms leading to disease. *Archives of Internal Medicine* 153(18): 2093–2101.

Proske, U., and Gandevia, S. C. (2012). The proprioceptive senses: their roles in signaling body shape, body position and movement, and muscle force. *Physiological Reviews* 92(4): 1651–1697.

Seeman, T. E., Singer, B. H., Rowe, J. W., Horwitz, R. I., and McEwen, B. S. (1997). Price of adaptation — allostatic load and its health consequences: MacArthur studies of successful aging. *Archives of Internal Medicine* 157(19): 2259–2268.

Sterling, P. (2012). Allostasis: a model of predictive regulation. *Physiology & Behavior* 106(1): 5–15.

Wang, K. (2026a). UNITARES: Information-theoretic governance of heterogeneous agent fleets. Published April 20, 2026. *Zenodo*. https://doi.org/10.5281/zenodo.19647159 (concept DOI; v6.9.1 https://doi.org/10.5281/zenodo.19722512, April 24, 2026).

Wang, K. (2026b). Trajectory Identity: A Mathematical Framework for Enactive AI Self-Hood. Published May 9, 2026. *Zenodo*. https://doi.org/10.5281/zenodo.20098168 (concept DOI; v0.11.1 https://doi.org/10.5281/zenodo.20098169). Source repository: https://github.com/cirwel/trajectory-identity-paper.
