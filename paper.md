# A Flat Coherence Score: What a Production-Data Replay Does and Does Not Show About Agent Self-State Gating

## Notes toward digital proprioception

**Author:** Kenny Wang, Independent Researcher
**ORCID:** 0009-0006-7544-2374
**Status:** Short-form rewrite of v1.2 (DRAFT, unreleased). It replaces the 27,800-word v1.2 and has not been tagged or deposited. Corrections to v1.2 are listed in Appendix B.

---

## Abstract

A running multi-agent system I operate computes a scalar "coherence" for every agent check-in and uses it, among other inputs, to place each state in one of three basins (high, boundary, low). On a 30-day production slice of 13,292 rows, the deployed score was flat within a narrow band: its 1st to 99th percentile range was 0.447 to 0.499. It never reached the 0.40 threshold below which it could push a state into the low basin, and it cleared the 0.45 high-basin threshold for 98.7% of rows, so it almost never decided a basin. The score is not empty. It carries some class information (its distributions for two classes separate with an AUC of 0.88), and it correlates r = 0.73 with a smoothed energy-integrity imbalance. But within each class, its association with distance from that class's own healthy operating point was weak and went both ways: Spearman ρ from -0.37 to +0.18 across classes, with the wrong sign in two of five, and in three of five in a later window.

I replaced the score with a class-conditional "grounded" form on the same rows and recomputed every basin under both forms. The grounded form spans 0 to 0.995, and on the full substitution every row whose recomputed basin changes moves downward (§4). The replay is an offline counterfactual on frozen data. It shows that the old score was inert at its decision thresholds. It does not show that the new labels are right, and no outcome, harm or operator judgment was used to grade either form. The rate of label change rose from 28.8% to 44.3% between two public windows whose end dates are four to five days apart. That rise is not noise. Rows whose stored values occur in both windows flip at 30.3%, and rows that appear only in the later window, inferred to be recorded after 2026-04-18, flip at 80.6%. The flip rate therefore depends on how far the state distribution has moved from the frozen class anchors; it is not a fixed property of the formula swap.

Three adjacent results bound the claim. Whether per-agent state forecasts bad outcomes is unresolved, pending one pre-registered read (§6). A genesis-anchored lineage check meant to catch slow drift does not discriminate as instrumented (§7). The cumulative-deviation integral that motivated earlier versions of this paper is specified but not computed by any production code path (§8). A single-agent case study tests an apparent "delayed shut-down" reading: the April anchor's calibration window ended a day after a shift in the agent's operating point, and recalibration moves toward the current state, as staleness predicts. That result does not by itself exclude a persistent shift, and the cause is open (§5).

**Keywords:** agent state monitoring, coherence score, class-conditional calibration, counterfactual replay, calibration staleness, digital proprioception

---

## 1. Introduction

### 1.1 What this paper is about

The system is UNITARES (Wang 2026a). Each agent in a small production fleet checks in periodically, and the system estimates a four-coordinate state for it, called E, I, S and V. From that state it computes a coherence value, combines coherence with the other coordinates and a risk score, and classifies the state into a basin. The intent behind the design is what I have called digital proprioception: an agent-side analogue of the sense an organism has of where its own limbs are (Proske and Gandevia 2012), supplied to agents that otherwise have no such sense. The term imports a function, not a failure mode and not a claim about experience.

The question here is narrow. Did the deployed coherence score do the job it was given, which is to indicate how far an agent is from its own healthy operating point, at the thresholds the classifier applies to it? For the window I could measure, it did not. Everything else in the paper is a consequence of that fact, a test of what replacing the score does, or a statement of what I cannot yet claim.

### 1.2 Contributions

1. **A measured negative about the deployed score (§3).** The legacy coherence score had an observed range of 0.068 on 13,292 rows. It could not reach the low-basin threshold, it almost always cleared the high-basin threshold, and within each class it did not consistently track distance from the class healthy point, although its distributions do differ between classes.
2. **A reproducible replay with an exact window decomposition (§4).** Replacing the score changes recomputed basin labels for 28.8% of rows, always downward on the full substitution. The higher rate in a later window decomposes, by counting matched stored values, into rows that appear only in the later window (inferred to be recorded after 2026-04-18), which flip at 74% to 100% in four of five classes. The export and scripts are public.
3. **A calibration case (§5).** A single-agent case that looked like a failure mode from the allostatic-load literature is consistent with a calibration anchor whose window closed a day after a shift in operating point. Recalibration is consistent with that reading but cannot exclude a persistent shift, and the cause remains open.
4. **A status ledger (§§6 to 8).** Outcome forecasting is unresolved, not negative. The lineage check does not discriminate. The cumulative-deviation integral is specified and uncomputed.

### 1.3 What I do not claim

I do not claim that the replacement score is better than the legacy score at anything an outcome would grade. I do not claim that agents are conscious, that the system implements the biology of allostatic load, or that the cumulative-deviation integral has been tested. I do not claim that these results transfer to another deployment: the data come from one operator's fleet, a good part of which is a single embodied agent on one device. I do not claim the replay's flip rate is a stable property of the fleet.

---

## 2. The system and its instruments

### 2.1 State, coherence and basins

Each check-in writes a state vector (E, I, S, V) to a database relation. E is an energy or resource-rate proxy, I is an integrity proxy bounded in [0, 1], and S is an entropy or uncertainty proxy bounded in [0, 1]. V is the coordinate that needs care.

**V is not an independent axis.** The v6 specification describes V as an accumulator driven by the imbalance between E and I (Wang 2026a, Appendix A). Since April 2026 the production system surfaces a behavioral V instead: an exponentially smoothed E minus I. On the released rows of the first window, regressing V on the instantaneous E minus I gives r = 0.953 and $R^2$ = 0.908, with sd(V) = 0.081 against sd(V - (E - I)) = 0.026. The EISV vector is therefore better described as three state coordinates plus a smoothed imbalance term than as four independent dimensions. The older accumulator-style coordinate was demoted to a separate diagnostic, and that diagnostic still feeds the legacy coherence. Two different variables are therefore both called V in the codebase and in earlier drafts. I write V for the surfaced behavioral coordinate and say so when I mean the other.

**The legacy coherence score.** The fleet-wide form is

$$C_{\text{legacy}} = 0.5\,\bigl(1 + \tanh(V_{\text{void}} / V_{\text{scale}})\bigr)$$

with one fleet-wide $V_{\text{scale}} = 1$, where $V_{\text{void}}$ is the demoted accumulator-style coordinate. (The code writes the scale as a gain, $C_1 = 1.0$, and multiplies by a ceiling $C_{\max} = 1$; both values are the same in the source on 2026-03-11 and on 2026-04-24, either side of the first window.) It reads that one coordinate only. The replay uses the stored legacy score and does not recompute it.

**The grounded coherence score.** The replacement reads (E, I, S) and measures distance to a class-specific healthy point $\mu_c$, scaled by a class-specific envelope $\Delta_{\max,c}$:

$$C_{\text{grounded}}(\mathbf{x}, c) = \max\left(0,\ 1 - \lVert \mathbf{x}_{EIS} - \boldsymbol{\mu}_c \rVert_2 / \Delta_{\max,c}\right)$$

The class constants come from a 30-day healthy slice frozen on 2026-04-18: rows whose recorded regime label was nominal, STABLE, CONVERGENCE or EXPLORATION, labels the system under study itself produced. The healthy point is the coordinate-wise median of (E, I, S), and the envelope is the 95th percentile of distance from it (CIRWEL 2026, unitares, `scripts/calibrate_class_conditional.py`, commit c9cc38c). The two forms read different coordinates, so substituting one for the other replaces the signal, not a parameter of it. The two signals are not unrelated, though: the legacy score correlates r = 0.73 with the surfaced V, which is itself mostly E minus I.

**Basin classification.** The production `classify_basin` function returns high, boundary or low. Low is disjunctive: I < 0.5, C < 0.40, |V| > 0.30, or risk $\geq$ 0.70 each enter it. High is conjunctive: E $\geq$ 0.6, I $\geq$ 0.7, S $\leq$ 0.25, |V| $\leq$ 0.15, C $\geq$ 0.45 and risk $\leq$ 0.45 must all hold. Boundary is the remainder. A change in coherence alone can move a row only when the other coordinates do not already force low or block high. In the current decision code, a low basin yields a `pause` and a boundary basin a `guide`, after higher-priority checks.

### 2.2 Classes

Class assignment checks the agent's label first: a named resident is its own class. Otherwise a tag decides (embodied, ephemeral, or persistent and autonomous), and an agent with none of these is in the default class, which the code describes as session-bounded agents and anything unrecognized. Five classes received frozen constants: Lumen (an embodied agent on a Raspberry Pi with environmental sensors), Sentinel, Vigil, Watcher (autonomous services), and default. A class without frozen constants falls through to a fleet fallback (the corner of the high basin, E = 0.6, I = 0.7, S = 0, with an envelope of 1.8); in the original pull only 42 `ephemeral` rows did (§4.2). The class constants, from the Phase 2 calibration (Wang 2026a §11.5; the healthy counts are those recorded in commit c9cc38c):

| Class | Healthy N | $E_h$ | $I_h$ | $S_h$ | $\Delta_{\max}$ |
|---|---|---|---|---|---|
| Lumen | 7,320 | 0.745 | 0.800 | 0.168 | 0.119 |
| default | 2,033 | 0.726 | 0.793 | 0.236 | 0.202 |
| Sentinel | 1,870 | 0.751 | 0.798 | 0.193 | 0.170 |
| Vigil | 384 | 0.737 | 0.790 | 0.240 | 0.171 |
| Watcher | 283 | 0.748 | 0.769 | 0.248 | 0.395 |

The envelope $\Delta_{\max}$ ranges over a factor of about 3.3 across classes. The fleet-wide constant used before per-class measurement (1.8) was 4 to 15 times larger than any measured envelope. The same-row ablation of §4.3 re-measured these constants on its own pull and obtained slightly different healthy counts and envelopes (for example default 0.200, Watcher 0.398). The replay uses the frozen values above. Lumen supplies 59% of the rows in the export, and Sentinel, Vigil and Watcher are each a single service, so the class structure rests on a small number of distinct sources.

### 2.3 The data

Everything in §3 and the full-substitution replay of §4 can be recomputed from a de-identified export archived under Zenodo data DOI 10.5281/zenodo.19705151 and mirrored in this repository. The §4.3 ablation cannot, for the reason given there. The export holds one row per agent-state observation, pseudonymized to a class label, with E, I, S, V, risk, both coherence values and both recomputed basin labels. It carries no agent identifiers, session identifiers, prompts or free text. Two windows are included: the 30-day window ending 2026-04-18 (13,292 rows) and the 30-day window ending 2026-04-23 (16,879 rows, Phase 2 constants held frozen). Matching on stored values and counting with multiplicity, 12,177 value tuples occur in both: 91.6% of the first window and 72.1% of the second. The match is by value, not by row identity, because the export has no row identifiers.

I report the 13,292-row export, not the 13,310-row pull that v6 cited. They are two executions of a wall-clock-anchored rolling window, and they differ by more than arrivals: by class, the export has Lumen −1, Sentinel −6, Vigil −1, Watcher −9, default +41, and none of the original 42 `ephemeral` rows, so 59 rows fewer and 41 more. The ephemeral −42 and default +41 suggest those agents were reclassified between the runs; I have not verified that. The production relation no longer retains the window (it holds 490 rows in the interval against the 13,310 originally returned, and there is no archive table), so the export is the surviving row-level record.

---

## 3. The result: the deployed coherence score was inert at its thresholds

### 3.1 The numbers

All figures are computed from `verdict_counterfactual_v6_submission.csv` (n = 13,292) by `flatness_and_windows.py`.

| | min | p1 | p50 | p99 | max | sd |
|---|---|---|---|---|---|---|
| C_legacy | 0.441 | 0.447 | 0.481 | 0.499 | 0.508 | 0.0082 |
| C_grounded | 0.000 | 0.000 | 0.625 | 0.983 | 0.995 | 0.2748 |

The legacy score occupies a band 0.068 wide, with an interquartile range of 0.4799 to 0.4847. No row falls below 0.40, so the C < 0.40 clause of the low-basin rule was unreachable for this fleet in this window. 98.7% of rows satisfy the C $\geq$ 0.45 clause of the high-basin rule, so that clause was close to a constant true. The coherence input therefore almost never decided a basin. Setting coherence to 1 for every row, so that both of its clauses always pass, changes 6 of the 13,292 recomputed basins (0.045%).

The grounded score spans the unit interval. 6.8% of rows sit exactly at zero, 15.5% are below 0.25, and 26.6% are below 0.40.

### 3.2 It did not track distance from the agent's own healthy point

The legacy score correlates r = 0.73 with the surfaced V, and it carries some class information: the probability that a random row of one class scores above a random row of another (the AUC) ranges from 0.54 to 0.88 across class pairs, highest for Lumen against default.

A working distance-from-healthy-point score should fall as a state moves away from its class's healthy point, within every class. The legacy score did not:

| Class | n | Spearman ρ, C_legacy vs distance | C_legacy p50, far rows (C_grounded < 0.1) | C_legacy p50, near rows (C_grounded > 0.8) |
|---|---|---|---|---|
| Lumen | 7,889 | -0.27 | 0.480 (n = 646) | 0.482 (n = 2,343) |
| Sentinel | 2,221 | +0.18 | 0.472 (n = 161) | 0.482 (n = 343) |
| Vigil | 471 | +0.07 | 0.495 (n = 37) | 0.483 (n = 76) |
| Watcher | 354 | -0.27 | 0.456 (n = 72) | 0.485 (n = 45) |
| default | 2,357 | -0.37 | 0.485 (n = 306) | 0.485 (n = 169) |

The association is weak and goes both ways: the wrong sign in two of five classes here, and in three in the second window (Lumen +0.24, Sentinel +0.50, Vigil +0.52). Where the sign is right, the size is not usable: the largest gap between far and near medians is 0.03 (Watcher), and the far rows still sit above the 0.40 low-basin threshold. A Lumen state at the edge of its envelope and one at its centre receive scores 0.002 apart.

### 3.3 What this does and does not establish

The result is a statement about the legacy instrument at its deployed thresholds: it could not reach one of them, it almost always cleared the other, and it did not consistently register distance from a class's healthy point.

*It does not say the grounded score is informative.* A score that varies is not thereby correct. Part of the grounded score's spread is arithmetic: Lumen's envelope is 0.119, so a state displaced by 0.06 from the healthy point already scores 0.5. Dividing by a small radius widens the spread by construction. Whether the spread tracks anything an agent or operator would call strain is untested here.

*It does not say why the legacy score is narrow.* The median legacy score in this window corresponds to a tanh argument of -0.037, close enough to zero that tanh is near its midpoint. I have not isolated why the demoted coordinate sat there.

*It does not generalize beyond this fleet.* The second public window gives a legacy median of 0.483 and a 1st to 99th percentile of 0.450 to 0.500, the same picture, but it shares 12,177 matched rows with the first and is not independent.

---

## 4. The replay

### 4.1 Design

For every row, I compute the basin twice with the same `classify_basin` function: once with the stored legacy coherence and once with the grounded coherence computed against the frozen Phase 2 class constants. Both basins are recomputed by the replay from stored columns of the state relation (E from the stored state record, and I, S, V and the stored coherence). They are not read from persisted production verdicts, and I have not checked that these stored columns are identical to the inputs the live decision path saw. A flip is a row whose recomputed basin differs. This is a static reclassification of fixed state vectors under two formulas. It is not a test of a deployed mechanism, and no agent's behavior changed.

### 4.2 Result

On the public export of the first window, 28.8% of rows (3,834 of 13,292, counted from recomputed labels; the original 13,310-row pull gave 28.9%) would change recomputed basin when each class is measured against its own healthy point instead of the fleet-wide formula. Per-class rates range from 15.8% (Sentinel) to 33.5% (Vigil).

- **The direction is downward.** In the full substitution, every flipping row moves toward the low basin: 1,702 boundary to low, 1,404 high to low and 725 high to boundary, counted from the labels stored in the export. No row moves up. This is mechanical. The legacy score cannot reach the C < 0.40 clause and the grounded score reaches it for more than a quarter of rows, so the replay mostly records how often a score that can cross a threshold does so, against one that cannot.
- **The later window decomposes by composition.** The window ending 2026-04-23 gives 44.3%. Because recomputed labels are a deterministic function of the stored values and frozen constants, a value tuple present in both windows flips the same way in both, and the difference is entirely composition. Rows are matched on their stored values, counted with multiplicity: a multiset intersection, not a row-by-row join. The export has no row identifiers, and the match uses seven columns (class, E, I, S, V, risk and the legacy score; the grounded score is left out because it is computed from unrounded coordinates). On that key the first window has 377 groups of rows that share all seven values, holding 1,228 rows. Rows in a group carry identical stored labels in both windows, so the counts are unaffected, but a match does not establish that both windows contain the same observation. The export also has no timestamps, so the timing in the row labels below is inferred from window membership. The flip rates use the labels stored in the export:

| Rows | n | Flip rate |
|---|---:|---:|
| In the first window only (inferred: its earliest rows) | 1,115 | 13.1% |
| In both windows | 12,177 | 30.3% |
| In the second window only (inferred: recorded after 2026-04-18) | 4,702 | 80.6% |
| of which Lumen | 1,694 | 100.0% |
| of which Sentinel | 1,023 | 96.1% |
| of which Vigil | 173 | 96.0% |
| of which default | 1,288 | 73.6% |
| of which Watcher | 524 | 0.0% |

  In three classes, rows recorded after 2026-04-18 flip almost without exception, and most of them fall below the 0.40 grounded threshold (Lumen 100%, Vigil 87%, Sentinel 70%). Far fewer lie outside the frozen envelope altogether, at C_grounded = 0 (16.6%, 12.1% and 3.1%). The flip rate therefore tracks how far the current state distribution has moved from the frozen anchors. That is what anchor staleness would produce, but flips also depend on the other basin coordinates and on risk, so the rate is not a direct measure of staleness. A sampling interval (about $\pm$0.8 points within one window) does not describe this kind of movement. The first-window rate is a property of that window and those anchors, not of the formula swap in general. The second window also shows the row rate rising: 4,702 rows between the two window ends, four to five days apart, against about 440 per day across the first window.
- **Two measurement caveats from the original pull.** The 30-day window overlaps identity-system revisions in mid-to-late April 2026, so some rows may carry class assignments inherited from cached bindings or from archived predecessors. And 42 rows of an `ephemeral` class fell through to the fleet fallback and are not interpreted; the export carries none of them (§2.3).

### 4.3 A same-row ablation, with a boundary

The replay changes two things at once: the formula (tanh of the void coordinate, versus distance in E, I, S) and the calibration target (one fleet-wide constant, versus per-class constants). I separated them on the same 13,310 rows from the original pull, where GF is the grounded formula against a single fleet-wide healthy point and radius measured from the same slice:

| Comparison | Flips / N | Rate |
|---|---:|---:|
| Legacy $\rightarrow$ grounded fleet-wide (formula change) | 1,496 / 13,310 | 11.2% |
| Grounded fleet-wide $\rightarrow$ grounded class-conditional (calibration change) | 3,133 / 13,310 | 23.5% |
| Legacy $\rightarrow$ grounded class-conditional (full substitution) | 3,844 / 13,310 | 28.9% |
| Legacy $\rightarrow$ class-scaled tanh (artificial control) | 10,355 / 13,310 | 77.8% |

The terms do not add (11.2 plus 23.5 is not 28.9) because the effects interact. I read the grounded fleet-wide to class-conditional step as evidence that the class-envelope term has an effect on basin labels of its own, and I do not decompose the headline further. The fourth row grafts a per-class scale onto a tanh form, but applies it to the surfaced V rather than to the demoted coordinate the production score reads, so it changes the input as well as the scale. It is unstable and I treat it as a negative control, not as a calibration-only path. The GF and class-scaled conditions need a per-row `regime` column that the de-identified export does not carry, so those two rates are provenance-backed from the recorded ablation output (`formula_calibration_ablation_results.txt`) and are not independently re-runnable.

The calibration-change step is not uniformly downward: 373 rows in it move up (365 low to boundary, 5 low to high, 3 boundary to high). The all-downward statement applies to the full substitution only.

### 4.4 What the replay shows

It shows that the formula and calibration choices matter at the basin level, and that the legacy score almost never decided a basin. It is recomputable by a third party from public rows and public scripts: `reproduce_basinflip.py` reproduces 26,574 of 26,584 basin labels exactly, with the ten exceptions within $6.7 \times 10^{-4}$ of a threshold, the rounding floor of a four-decimal export.

It does not show that any flip is correct. Under the current decision code, a recomputed flip into the low basin corresponds to a `pause`, and a flip from high to boundary to a `guide`. Whether that is desirable depends on the agent and the context, and no outcome grades it. The replay is evidence about the old score and is silent about the new one.

### 4.5 Why the homogenization framing is only an analogy

The class-conditional step was motivated by the neuroscience literature on group-average versus individual-level measurement (Krakauer et al. 2017; Gratton et al. 2018): pooling subjects with different dynamics yields a reference representative of none of them. The analogy names a failure mode. It is not a test. In the fleet the pooling was not the main defect. The main defect, per §3, is that the legacy score did not act at its thresholds, pooled or not. Class-conditional calibration is one remedy among several, and the replay does not rank it against the others. §4.2 also shows its cost: class anchors frozen at one date stop describing the fleet as it changes.

---

## 5. A calibration case on one embodied agent

### 5.1 The apparent failure mode

McEwen's four types of allostatic load (McEwen 1998; 2007) describe four ways the normal stress response fails: repeated hits, lack of adaptation, delayed shut-down, and inadequate response with compensatory hyperactivity. On 2026-05-09 I observed Lumen across an 86-minute window of 27 check-ins. Against its April healthy point, the state looked like the delayed shut-down pattern. The behavioral V sat at 0.0954 with a within-window standard deviation of 0.00015, sign-flipped from the healthy value of about -0.055. The (E, I, S) displacement was 0.115 against an envelope of 0.119, so the grounded coherence was about 0.03, while the legacy coherence read 0.497. That contrast is itself an instance of §3: the legacy score called a state at 97% of its class envelope essentially neutral.

### 5.2 The disambiguation and its result

The reading predicts a test: if the healthy point moves toward Lumen's current state on recalibration, the elevation is calibration staleness, not a persistent failure. I recalibrated on the 30-day window ending 2026-05-09 (11,472 rows) with the Phase 2 procedure. The healthy point moved toward the current state on all three coordinates (I from 0.800 to 0.7335, E from 0.745 to 0.7706, S from 0.168 to 0.1893), and the envelope grew from 0.119 to 0.1279. That is the result the criterion specified in advance treats as staleness. It is not decisive: a reference refit on data from a persistently shifted state would also move toward that state, so the test separates the two readings only if the newer window is itself healthy, and nothing independent of the system confirms that.

Weekly bins of Lumen's state over 90 days show three regimes, and sub-day resolution places the change at a single ten-hour event on 2026-04-17 UTC (E falling from 0.749 to 0.350 and recovering to 0.787), after which the new regime held for 22 days. About 96.7% of the Phase 2 window's duration (2026-03-19 to 2026-04-18) predates the event. The share of its rows is not recoverable, because the exports carry no timestamps. How much of the anchor's data comes from each regime is therefore unknown. What is known is that the new regime spans at most the window's last day. The second-window rows in §4.2 show that the anchor does not describe the later state: every Lumen row recorded after 2026-04-18 flips and falls below the 0.40 grounded threshold against the April anchor, and 16.6% of them lie outside its envelope altogether.

### 5.3 Cause: open

The change coincides to within the hour with a day on which four pull requests altered the identity-binding behavior of the system. That is a candidate cause, not an identified one, and there is a competing explanation I cannot exclude. The E coordinate derives in part from CPU utilization, and a day of deployments generates load. At the time, a single CPU reading entered two anima dimensions, suppressing E and inflating I at once, a defect repaired in August 2026 (CIRWEL 2026, anima-mcp, PRs #173 and #176). A deploy-driven CPU excursion amplified by that defect would produce an energy collapse and recovery on this timescale with no change in the agent. The CPU and memory series for that day are no longer retained, so I cannot re-derive E with the corrected mapping.

One observation from the public export bears on this without settling it. Rows recorded after 2026-04-18 flip at 96% for Sentinel and Vigil, as well as 100% for Lumen, and fall below the 0.40 grounded threshold at 70% (Sentinel) and 87% (Vigil), as well as 100% (Lumen) (§4.2). The CPU defect was in Lumen's sensor mapping. A shift shared by the autonomous services points toward a server-side change. The export has no timestamps, so this cannot place the other classes' shift on 2026-04-17.

Two further limits. The recalibration windows are not sampling-matched: the Phase 2 Lumen healthy slice held 7,320 rows and the recalibration window 11,472, and I have not confirmed that both counts apply the same healthy filter. The rise in row rate visible in §4.2 would account for part of the difference. The production server flagged no anomaly throughout, but the deployment's degradation paths fail toward healthy rather than toward unknown, so the silence carries little weight.

What survives either causal story is narrower: the April anchor's window closed a day after the shift, and the anchor no longer describes the agent's current state. Whether the new state is healthy is not established. The case is a single-agent report. Its date, magnitude and shape are provenance-backed, its causal reading is open, and the longitudinal data that would test it have aged out of the production database. It is not evidence for or against McEwen's taxonomy in biology. It does suggest a category the four types do not cover, a shift in the operating point itself, but one case does not establish a category.

---

## 6. Outcome forecasting: unresolved

The most natural validation of a self-state signal is to ask whether it predicts bad outcomes. The status of that question is *unresolved*. A historical weekly ablation that appeared to show a negative result used a cohort that mixed anchor populations the confirmatory read excludes, and its permutation blocks were not independent adjudicated failures. It was withdrawn for target inference on 2026-08-26, and its numbers are historical provenance, not evidence in either direction (CIRWEL 2026, unitares, `docs/ontology/eisv-proprioception-contract.md`, item 4). I report no forecasting effect size, direction or sensitivity bound.

A confirmatory read is pre-registered for 2026-12-01 (CIRWEL 2026, unitares, PR #1425). It passes only if a selective p of at most 0.05 holds on a lead slice, the effect exceeds the permutation null's 95th percentile, at least 150 independent bad clusters exist in the read's own units, and the best-model identity is stable across leads. The evidence ledger records interim access to discrimination results by automation after registration, so the read cannot be described as a single clean blinded look.

Two limits apply whatever the read shows. Every bad outcome available so far is task-negative (failed tasks, failed tests and similar), which bounds even a positive result to rework prediction. And a discrimination statistic is not decision value at the deployed operating point, which would require interventional data or a larger fleet. §3 does not depend on any of this, because it compares two formulas on the same rows.

---

## 7. Trajectory identity and the genesis anchor

### 7.1 The idea

A coherence check against recent state fails on slow drift by construction: if each step is small, every comparison passes. The companion trajectory-identity framework (Wang 2026b) proposes two references per agent: a rolling signature $\Sigma_{t-1}$ for acute change, and a fixed genesis signature $\Sigma_0$ for slow drift, with a lower threshold on similarity to $\Sigma_0$ (0.60) than on similarity to the rolling reference (0.70).

### 7.2 What the genesis signature is

A genesis signature is a stored object, written into the agent's metadata at onboarding or first trajectory submission for agents that go through that path. It is not a clean fixed anchor. An early genesis, built from few data points, can be reseeded while the agent sits in the lowest trust tiers, if a later signature has substantially higher confidence or if similarity to the stored one is below 0.7. It becomes immutable only once the agent reaches the second trust tier. $\Sigma_0$ is therefore an early-data estimate that hardens with tenure, not a captured pre-illness baseline. Lumen's first awakening predates that path, and no genesis was persisted for it at first onboarding (Wang 2026a §11.7, item 5), so the §5 case could not use one.

### 7.3 It does not discriminate as instrumented

Whether a genesis anchor exists is secondary, because the similarity check that would use it does not separate agents as deployed. An audit of the production similarity metric (CIRWEL 2026, unitares, `docs/ontology/eisv-proprioception-contract.md`, trajectory-identity items, added 2026-07-30 and refined 2026-08-20) found the following:

- Two of the weighted components give near-free credit, and one input is never populated.
- The composite saturates near 0.633 for long-running agents.
- Binned by observation count, the median similarity to genesis is 0.996 for identities with fewer than 20 observations and 0.631 for those with at least 1,000.

Identities decay into that floor as drift accumulates. Young identities score high because they have not drifted, not because the metric discriminates. Accumulated genuine drift therefore asymptotes to a passing score above the 0.60 line, and the lineage channel cannot fire on the slow-drift case it was designed for.

A cross-agent audit reported in the companion paper's v0.15 correction (Wang 2026b, §6.5) found the ordering inverted: between-agent similarity of 0.63, against 0.12 for one agent compared with itself across a client migration, with roughly 90% of between-agent pairs clearing the 0.60 threshold. The companion paper accordingly marks its multi-agent discrimination pilot confounded by role and harness, and returns the discrimination criterion to open. The two-tier architecture stands as a proposal. Its current instrumentation does not realize it.

---

## 8. The cumulative-deviation integral: specified, not computed

**Status.** Earlier versions of this paper were titled around a cumulative-deviation integral in the spirit of allostatic load (McEwen and Stellar 1993). That integral is specified. It is not computed by any production code path, no production code evaluates it against a threshold, and no decision in the system is driven by it. A function that computes it exists in the embodied agent's code base, documented there as a research diagnostic, with unit tests and no caller outside them (checked against the repository's main branch on 2026-10-02). It is computable on demand over recorded telemetry. It is not deployed as a control signal.

**Specification.** For the embodied agent, a four-component anima vector a = (warmth, clarity, stability, presence) is computed from sensors and system metrics, and the specified quantity is

$$V_{\text{anima}}(t) = \int_0^t \lVert \mathbf{a}(\tau) - \boldsymbol{\mu_a} \rVert\, d\tau$$

with $\mu_a$ the attractor center from the agent's own recent state distribution. The companion framework specifies a coupling (when V_anima exceeds a deployer-set multiple of the basin scale, induce rest, reduce stimulation or pause a task) that is not wired. The anima vector is a different object from the EISV vector of §2, and the signed V coordinate of EISV is a third thing.

**The analogy and its limits.** Allostatic load is the cumulative cost of regulating a system away from its operating point (McEwen and Stellar 1993; Sterling 2012). In clinical practice it is reconstructed from sparse biomarker panels (Seeman et al. 1997). In the deployed system the integrand could be recorded at every check-in, so the integral could in principle be approximated by numerical integration over those check-ins rather than reconstructed from sparse panels, and that observability is the only point of the analogy I think holds. The deployed quantity is single-system, its reference is measured in a calibration window rather than set anticipatorily, and there is no body. At best it corresponds to a single-biomarker integral, not to clinical allostatic load.

**What would earn it.** Wire the coupling, then show that acting on the integral improves decisions over non-integral baselines such as instantaneous deviation. That is untested, not refuted. A measurement problem applies before any wiring. §§4.2 and 5 show the fleet moving away from frozen anchors, and an integral accumulated against an anchor that no longer describes the agent would accumulate that gap. Transition-aware calibration is not implemented.

---

## 9. Limitations and what would change the picture

**One fleet, one operator.** The data come from a single deployment, and over half the rows in the replay are one embodied agent. Class-level differences rest on a small number of distinct sources. An independent re-measurement on another deployment would be the stronger bar.

**Retention.** The production relation no longer holds the measurement window. The frozen export is the record, the Lumen longitudinal pull is foreclosed, and the causal reading of §5 cannot be upgraded from this deployment's history. A deployment used as a test bed needs its evidentiary windows pinned as exports at measurement time.

**Same-author, self-cited system.** The author built the system, ran the measurement and wrote the paper. The public export and offline recomputation reduce the dependence on trust for the §3 and §4 numbers. They do not reduce it for the framing.

**The replacement score is unvalidated.** Showing that the old instrument did not act at its thresholds is a different result from showing the new one is right. Testing the replacement needs an outcome-graded comparison, with a label source wider than task-negative outcomes and a decision-value analysis, and the available data do not support one.

**Anchor staleness.** The replay's rate depends on how far the state distribution has moved from frozen anchors (§4.2). Any deployment of class-conditional calibration would need a recalibration policy, which this paper does not test.

**What would change my mind.**
- If the 2026-12-01 read passes on its own pre-registered terms, outcome forecasting moves from unresolved to a positive finding about rework prediction, with the label-class bound intact. If it fails, outcome grounding closes for this label channel, and reopening needs a new label channel or measurement process, not more labels.
- If an independent deployment shows a legacy-style score that does reach its thresholds and does track within-class distance, the §3 result is specific to this system's demoted coordinate.
- If the integral is wired and a non-integral baseline matches it on decisions, the cumulative-deviation framing earns nothing beyond the analogy.

---

## 10. Conclusion

The deployed coherence score was flat within a band from 0.447 to 0.499 (1st to 99th percentile). It never reached the 0.40 low-basin threshold and almost always cleared the 0.45 high-basin threshold, so it almost never decided a basin. It carried some class information, but within each class it did not consistently track distance from that class's healthy point. Replacing it moves many recomputed basin labels downward in an offline replay, and the rate of that movement depends heavily on how far the fleet has moved from the frozen class anchors. That shows the old score was inert where it mattered. It does not show the new labels are right.

The neighbouring claims stand as follows. A single-agent case that looked like a failure mode from the allostatic-load literature is consistent with a calibration anchor whose window closed a day after a shift in operating point, though a persistent shift is not excluded and the cause is open. Outcome forecasting is unresolved, pending one pre-registered read. The genesis-anchored lineage check does not discriminate as instrumented. The cumulative-deviation integral is specified and not computed in production.

The practical lesson is about instruments. A scalar that looks like a health score on a dashboard can sit where its thresholds never touch it, and the way to find out is to measure its spread against the thresholds and against the thing it is supposed to distinguish. The next step is an outcome-graded test of any replacement, with a recalibration policy and a label source wider than task failures, before calling it a measurement of anything.

---

## Appendix A: Reproducibility

| Object | Status | What can be checked now | What is missing |
|---|---|---|---|
| Flatness and within-class statistics (§3) | **Recomputable offline** | `flatness_and_windows.py`: percentiles, threshold shares, within-class Spearman, far/near medians, class AUCs, both windows | Independent deployment |
| Full-substitution replay (§4.2) | **Recomputable offline** | `reproduce_basinflip.py`: 28.84% (3,834 / 13,292 from recomputed labels; the labels stored in the export give 3,831), per-class rates within 0.6 points of the original pull, 26,574 of 26,584 labels exact | Independent deployment |
| Window decomposition (§4.2) | **Recomputable offline** | `flatness_and_windows.py`, matching stored values with multiplicity: a multiset count, not a row-level join (no row identifiers exist) | Row identifiers; timestamps |
| Formula-versus-calibration ablation (§4.3) | Provenance-backed only | Recorded output in `formula_calibration_ablation_results.txt` | Needs a per-row `regime` column absent from the export; the production window is no longer retained |
| Lumen recalibration case (§5) | Provenance-backed only | 86-minute protocol, recalibration criterion, weekly bins | State history for 2026-02 to 2026-04 aged out; CPU and memory series for 2026-04-17 not retained |
| Cumulative-deviation integral (§8) | Specified; function exists as an uncalled research diagnostic | `compute_void_integral` and its tests in the embodied agent's repository | Any production use |
| Outcome forecasting (§6) | Unresolved | Ontology contract item 4 and the pre-registered stop rule | The 2026-12-01 read |
| Row-level export | **Public**, Zenodo data DOI 10.5281/zenodo.19705151, mirrored here, SHA-256 pinned in `reproduce_basinflip.py` | 13,292 and 16,879 class-pseudonymized rows with state, risk, both coherences, both recomputed basin labels | Nothing for §3 and §4.2 |
| Raw production relation | Withheld and no longer retained | Schema and provenance | Unavailable in principle |

Both scripts are in `analysis/phase-2-2026-04-18/` and use the standard library only.

## Appendix B: Corrections to v1.2

- v1.2 called outcome forecasting "measured and negative". That claim was withdrawn on 2026-08-26 (§6). The question is unresolved.
- v1.2 said in one place that the genesis signature is "captured trivially" and in another that Lumen's was not persisted. §7.2 states what is stored, when it can be reseeded, and that Lumen has none.
- v1.2's title named a cumulative-deviation integral that is not computed in production (§8).
- v1.2 described the two public windows as roughly 87% overlapping in rows and read the change in flip rate between them as window sensitivity. The row overlap is 91.6% of the first window and 72.1% of the second, and the change is a deterministic composition effect (§4.2).
- v1.2 read the Lumen anchor as averaging across a regime change. About 96.7% of its window's duration predates the change, so the shift came in the window's last day; the share of the anchor's rows from each regime is not recoverable (§5.2).
- The clinical study sketches, the kintsugi section, the differentiation survey and the synthetic-psychology essay are cut. They remain in the v1.2 tag.

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
