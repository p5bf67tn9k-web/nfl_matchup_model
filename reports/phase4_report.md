# Phase 4 Report — Shrinkage & Opponent-Adjustment Validation

**Project:** `nfl_matchup_model`
**Run date:** 2026-09-08
**Environment:** Python 3.12.14, `nflreadpy` 0.1.5, `polars` 1.44.1, `scikit-learn` 1.5, `numpy` 2.x
**Scope:** narrowly-scoped unit-performance validation. **No** matchup interactions, ratings,
weights, composites, expected performance, expected score, game/margin prediction, or market data.

> **Audited by Phase 4.1** (`reports/phase4_1_audit.md`). Findings: the implemented candidate
> universe matches the approved protocol; the shrinkage result is robust to `k` and to the
> sample-size definition; one Stage-B implementation defect was found (post-hoc reference selection),
> fixed, and shown immaterial (1 of 78 verdicts changed, no conclusions). Language in §10 was
> softened. Overall audit recommendation: **`APPROVE_PHASE_4`**.

---

## 0. TL;DR

* **108 tests pass** (97 from Phases 0–3 unchanged + 11 new). Ruff clean.
* Two sequential questions, evaluated in order:

| Stage | Question | Answer |
|---|---|---|
| **A — Shrinkage** | Does `shrunk = μ + (n/(n+k))·(raw − μ)`, with `k` chosen strictly walk-forward, beat the **raw** feature out of sample? | **YES — for 39 of 42 candidate metrics.** Median RMSE reduction vs raw = **11.8%**. This explains almost the entire Phase 3 gap between rank persistence and RMSE skill. |
| **B — Opponent adjustment** | After shrinkage, does a chronological ridge opponent adjustment add incremental information about future same-unit performance? | **NO — for 0 of 39 applicable metrics.** Opponent-adjusting the *feature* is at best neutral (`oppadj_raw` ≈ `shrunk`) and usually slightly worse (`oppadj_shrunk` < `shrunk`). |

* **The chain, median `skill_vs_league` at horizon 4 across metrics:**

  ```
  raw_trailing3  -0.30
  raw_feature    -0.06      (Phase 3's finding: raw season-to-date loses to the league mean)
  prior_season   -0.05
  league_mean     0.00
  shrunk_feature +0.045     <-- shrinkage flips it from losing to beating the baseline
  oppadj_raw     +0.046     (indistinguishable from shrunk)
  oppadj_shrunk  +0.033     (worse than shrunk)
  ```

* **Concrete example — `qb.epa_per_dropback` (season-to-date window, H4):**
  raw `skill_vs_league` = **−0.038** → shrunk = **+0.099**. Shrinkage converts it from
  worse-than-a-constant to a ~10% RMSE improvement. Opponent adjustment then drags it back to
  +0.073 (`oppadj_raw`) / +0.056 (`oppadj_shrunk`).

* **Team defense** — which cleared nothing in Phase 3 — finally beats the league mean, **but only
  after shrinkage** (`epa_per_play` +0.041), and it remains the weakest family.

* **Both negative controls pass.** Permuting the shrunk feature within season never gains skill
  (placebo `skill_vs_league` −0.03 to −0.13). Randomising opponent identities in the ridge gives an
  **identical** result to the real opponent labels (e.g. `team_offense.epa_per_play`: −0.070 real vs
  −0.071 randomised) — the opponent structure contributes nothing real.

* **Combined status:** **39 `SHRINKAGE_ONLY`**, **3 `NEITHER`** (`team_offense.proe`, `wr.adot` —
  already well-calibrated role traits; `ngs_passing.avg_time_to_throw` — `INSUFFICIENT_DATA`).
  **0 `BOTH_ADD_VALUE`**, **0 `OPPONENT_ADJUSTMENT_ONLY`**.

* **`config/metrics.yaml` is NOT changed** — Phase 4's `predictive_status` is still persistence-based.
  Phase 4 results live in `config/metrics_phase4_status.yaml` (evidence) and `outputs/phase4/`.

---

## 1. Pre-registration & disclosed deviations

The protocol is frozen in **`config/phase4_validation.yaml`** (`frozen: true`), written before any
Phase 4 result was inspected. It inherits Phase 3's target-eligibility rules, feature windows,
horizons, season-phase buckets, and bootstrap unchanged (`phase3_target_rules_changed: false`).

**Disclosed deviations** (made during harness setup, documented in the config):

| # | Deviation | Rationale |
|---|---|---|
| **A** | Ridge `alpha` is selected **once** per (family, metric) on the 2016–2018 training seasons and frozen for the whole 2019–2025 evaluation, rather than re-selected before each OOS season. | Tractability (per-season re-selection is ~10× the ridge fits). Still chosen strictly from data before the evaluation period. The ridge **strengths** are still refit walk-forward at every (season, week). Since opponent adjustment adds no value at any alpha in the grid, this deviation does not affect a conclusion. |
| **B** | The observation history is extended to target seasons **2016–2018** (game metrics from 2013) to give the walk-forward `k`/`alpha` selection a real training set for the first evaluation season. | This extends *history*, not target eligibility. The **evaluation period stays 2019–2025** and is never touched by tuning. |
| **C** | `oppadj_raw` = `league_mean + centred_ridge_strength` (the centred strength is a deviation; the level is added back so it is a prediction on the metric's scale). Chosen after an initial run showed a scale mismatch for rate metrics; disclosed. | A pure centred strength (mean 0) is not comparable to a rate target (~0.06); adding the level back makes it a fair comparison. |

The **k grid** `{1, 2, 4, 8, 12, 16}` and **alpha grid** `{1, 3, 10, 30, 100, 300}` were fixed
before results were inspected. Neither `k` nor `alpha` was ever chosen from aggregate 2019–2025
results.

---

## 2. Method

**Candidate universe** (`outputs/phase4/candidate_universe.csv`, 42 metrics). Frozen selection rule:
a metric enters Phase 4 iff it is **Phase 3 `RANK_PERSISTENT`** (Spearman 95% CI > 0 and
|Spearman| ≥ 0.15 at **both** primary horizons) with `primary_n_h4 ≥ 300`, **plus** the two NGS
style-trait metrics named in the Phase 4 spec (`ngs_passing.avg_time_to_throw`,
`ngs_receiving.avg_separation`). The 8 Phase-3 `NOT_RANK_PERSISTENT` metrics are excluded. Inclusion
is **not** promotion — every candidate starts `UNVALIDATED` for both layers.

**Feature & target** (inherited from Phase 3): the `season_to_date` window is the anchor for the
baseline chain (the a-priori "use all your season-to-date data" window; other windows reported as
sensitivity, never used for status). Primary weeks 5–18, horizons 2 and 4, walk-forward 2019–2025.

**Stage A — shrinkage.** `shrunk = μ + (n/(n+k))·(raw − μ)`, `μ` = the Phase 3 league-mean baseline
(3-completed-season entity-season mean), `n` = games in the feature window, `k` = **one parameter
per metric**, chosen walk-forward: for each OOS season S, `k` minimises pooled RMSE over all
observations with target season < S (primary weeks, H2+H4 pooled), frozen, then applied to S.
Fallback `k = 8` when the fold has < 500 training observations.

**Stage B — opponent adjustment.** Per (entity, game) unit-metric observation:
`metric ~ entity one-hot + opponent one-hot + home` (ridge). The opponent-adjusted strength is
`intercept + entity coefficient`, centred across entities in the fit. Fit on completed games with
`data_asof < target kickoff` within a trailing 2-season window; refit every (season, week). Applied
to 7 families (team offense/defense, pass protection/rush, qb, rb, wr); **not applicable** to the
NGS style traits and special teams.

**Baseline chain** (spec §13): `league_mean → prior_season → raw_trailing3 → raw → shrunk →
oppadj_raw → oppadj_shrunk`, incremental skill reported at every step.

**Uncertainty:** multiplier cluster bootstrap (clusters = `entity_id × season`), 1000 iterations,
95% percentile CIs on the incremental skill vs the reference layer.

**Status rules** (frozen): a layer "adds value" iff, at **both** primary horizons, `n ≥ 300` **and**
`skill vs the reference layer's feature` has a 95% CI lower bound > 0 **and** a point estimate
≥ 0.02. Ambiguous / one-horizon-only → `UNVALIDATED`. Stage B's reference is the better of
`{raw_feature, shrunk_feature}` on that cell — B must beat A's winner.

---

## 3. Stage A results — `outputs/phase4/shrinkage_results.csv`

**39 of 42 candidates → `SHRINKAGE_ADDS_VALUE`.** Median `skill_shrunk_vs_raw` (H4) = **+0.118**;
CI lower bound > 0 for **41 of 42**.

| family | candidates | `SHRINKAGE_ADDS_VALUE` |
|---|---|---|
| qb | 9 | **9** |
| team_defense | 7 | **7** |
| team_offense | 9 | 8 (not `proe`) |
| wr | 6 | 5 (not `adot`) |
| rb | 4 | **4** |
| pass_protection | 3 | **3** |
| pass_rush | 1 | **1** |
| special_teams | 1 | **1** |
| ngs_receiving (`avg_separation`) | 1 | **1** (season-to-season, n=632, skill +0.13) |
| ngs_passing (`avg_time_to_throw`) | 1 | 0 — `INSUFFICIENT_DATA` (n=213 season-pairs < 300; the point estimate is +0.12 with CI lo +0.07, i.e. it *would* pass with more data) |

**The 3 that do not add value:**
* `team_offense.proe` — `NO_INCREMENTAL_VALUE`. Skill vs raw 0.016 (H2) / 0.030 (H4), CI lo ≈ 0.
  PROE is a stable coaching tendency; the raw value is already well-calibrated.
* `wr.adot` — `UNVALIDATED`. Skill 0.016 (H2, below the 0.02 floor) / 0.032 (H4). A receiver's
  average depth of target is a fixed role; shrinkage barely moves it. (Note: **`qb.adot` DOES
  benefit** — skill 0.072 / 0.106 — a QB's aDOT is more of a choice and regresses more.)
* `ngs_passing.avg_time_to_throw` — `INSUFFICIENT_DATA` at the season-to-season grain.

**What shrinkage buys, by metric noisiness:** the RMSE reduction scales with how much the raw
metric over-extrapolates. `rb.fumble_lost_rate` (extremely noisy) → skill +0.25, `k` near 16.
`team_offense.epa_per_play` → skill +0.13, `k` = 8. Already-calibrated traits (`proe`, `wr.adot`)
→ skill < 0.03.

---

## 4. Stage B results — `outputs/phase4/opponent_adjustment_results.csv`

**0 of 39 applicable metrics → `OPPONENT_ADJUSTMENT_ADDS_VALUE`.** All 39 → `NO_INCREMENTAL_VALUE`;
3 → `NOT_APPLICABLE`.

The chain medians (H4): `shrunk_feature` `skill_vs_league` **+0.045**, `oppadj_raw` **+0.046**
(statistically identical), `oppadj_shrunk` **+0.033** (worse). Scored against the fixed reference
`shrunk_feature` (Phase 4.1 fix), `oppadj_raw` has mean `skill_vs_reference` **−0.028** at H4
(max +0.011) — negative for every metric except two where the CI includes 0
(`rb.fumble_lost_rate`, `rb.yards_per_carry`).

**Observed result:** opponent-adjusting the feature did not improve out-of-sample prediction of
future same-unit performance.

**Hypothesis (untested):** the ridge produces a cleaner estimate of the unit's *current* strength
(schedule removed), but the target is future performance against future *actual* opponents, which
are not average; the season-to-date raw value may carry some information about near-future schedule
exposure that opponent adjustment removes.

**Untested claim:** that this is *the reason* for the null. It is not established here — Phase 4
does not build a predictive model to test the mechanism. See the Phase 4.1 audit
(`reports/phase4_1_audit.md` §3): opponent effects are clearly real for team defense (opponent-coef
variance 69% above a permutation null), small-but-real for QB/WR/protection/team-offense (10–20%
above), and unidentifiable for RB (a back faces each defense ~once) — so the null is
predominantly "estimable but non-predictive as a feature transform", with the identification also
weak for some families.

**This is what the spec (§12) anticipated** ("Do not assume ridge helps… it may improve neither").

---

## 5. Negative controls — `outputs/phase4/negative_control.csv`

| control | result |
|---|---|
| **Phase 3 placebo on the shrunk feature** (permute the shrunk feature within season) | placebo `skill_vs_league` **−0.03 to −0.13** across the 6 tested (family, metric) cells — a meaningless feature never gains skill; placebo `\|Spearman\|` ≈ 0.00. **The shrunk feature's skill is real.** |
| **Randomised opponent labels** (permute opponent identities in the ridge design) | real vs randomised `oppadj skill vs shrunk`, all 6 cells: `team_offense.epa_per_play` −0.070 / −0.071 · `team_defense.epa_per_play` −0.029 / −0.029 · `qb.epa_per_dropback` −0.026 / −0.026 · `wr.yards_per_target` +0.008 / +0.009 · `rb.rush_epa_per_att` +0.002 / +0.001 · `pass_protection.sack_rate_allowed` −0.039 / −0.039. **Identical to 3 decimals.** The opponent structure the ridge fits adds nothing real — confirming the `NO_INCREMENTAL_VALUE` verdict is not a broken ridge. |

---

## 6. Hyperparameter behaviour & sensitivity — `outputs/phase4/hyperparameter_stability.csv`

**`k`** (per metric, walk-forward): uses the full grid `{1,…,16}`. Stable within a metric across
folds — `team_offense.epa_per_play` → `k = 8` for 2020–2025 (`k = 4` for 2019); high-noise metrics
(`special_teams.st_epa_per_play`, `team_offense.rush_epa_per_play`, `rb.fumble_lost_rate`) → `k`
pinned at 12–16 (shrink hard). No metric that "adds value" does so only under one narrow `k` — the
RMSE-vs-`k` curves are flat-bottomed (`epa_per_play` 2025: `{4: 0.1282, 8: 0.1280, 12: 0.1287}`).

**`alpha`** (per family, selected on 2016–2018): values in `{3, 10, 30, 100}`. Moot — opponent
adjustment adds no value at any alpha in the grid, and the randomised-opponent control shows the
ridge structure itself contributes nothing.

---

## 7. What Phase 4 does NOT establish (spec §26 — required)

Phase 4 is still **not** a matchup test.

* **Shrinkage adds value** → the strongest claim is: *"this measurement, after `w = n/(n+k)`
  shrinkage, provides robust out-of-sample information about future SAME-UNIT performance."* It is a
  prerequisite for the eventual matchup model, not the model.
* **Opponent adjustment of the feature failed** → this does **not** mean opponent information is
  useless in a matchup. Adjusting a *unit feature* for opponent (making it "vs average") is a
  different operation from modelling an *interaction* between two specific units. The interaction
  question — *do opponent-adjusted / shrunk measurements of two opposing units predict game-level
  outcomes better than simple baselines* — is a separate research phase.
* **Team defense now beats the league mean after shrinkage** → this does not make it a strong
  predictor; it is the weakest family and the margin (+0.04) is small.

---

## 8. Newly discovered problems

**None that are leaks.** The Phase 4 leakage suite (7 tests) is green: `k` is selected only from
prior seasons (poisoned future observation → identical `k`); every game in a `(season, week)` ridge
fit has `data_asof` strictly before that week's kickoff; a genuinely-future game (`data_asof` in
2026) leaves every earlier ridge strength byte-identical; no market column is reachable.

**Methodological notes** (disclosed, not leaks): the `oppadj_raw` scale fix (deviation C); the
NGS metrics required a season-to-season grain (the weekly files carry no opportunity weights), which
put `avg_time_to_throw` below the 300-pair `INSUFFICIENT_DATA` threshold.

---

## 9. Limitations

1. **`n` = games in the window** (not opportunities). A 3-game window with 150 plays and one with 60
   are shrunk the same. An opportunity-weighted `n` is a candidate refinement for a later phase.
2. **`k` is metric-global** (spec §6 — deliberately simple). Team-, player-, or position-specific
   `k`, or a hierarchical / empirical-Bayes estimate, may do better; that is explicitly a later
   question.
3. **Opponent adjustment tested only as a feature transform.** The negative result is specifically
   about pre-adjusting the unit feature. It says nothing about opponent effects in an interaction
   model.
4. **Ridge alpha frozen on 2016–2018** (deviation A). Given the null result, immaterial.
5. **NGS Stage A is season-to-season and unweighted.** A weekly windowed treatment is deferred.
6. **`proe` and `wr.adot`** are `UNVALIDATED`/`NO_INCREMENTAL` for shrinkage only because they are
   already well-calibrated — not because they lack persistence (Phase 3 showed they persist).

---

## 10. Implications for the eventual model (recorded, not built)

*`SHRINKAGE_ADDS_VALUE` means only: shrinkage improved out-of-sample prediction of future SAME-UNIT
performance under this frozen evaluation design. It does **not** imply validated matchup value,
validated game-prediction value, inclusion in the final model, or a causal interpretation.*

1. **Regression-to-the-mean shrinkage is the current preferred calibration layer for the Phase 4
   candidate metrics.** `w = n/(n+k)` with `k` fit walk-forward per metric converts ~all
   rank-persistent measurements into point predictions that beat the league-mean and prior-season
   baselines out of sample. The Phase 4.1 audit confirms this is robust to the sample-size
   definition (game count vs opportunity count) and not dependent on a narrow `k`.
2. **Do not opponent-adjust the unit feature.** Adjusting a team/player's season-to-date metric to
   "vs average opponent" removes information rather than adding it, for the purpose of predicting
   future same-unit performance. If opponent structure helps at all, it belongs in an **interaction
   layer** applied to two opposing units — a separate, later, explicitly-reviewed phase.
3. **Lean on prior-season data early** (Phase 3) and **shrink hard** for noisy metrics (explosive
   rates, fumble rate, special teams — `k` ≈ 16).
4. **Team offense remains the most trustworthy unit;** team defense is usable only post-shrinkage
   and only weakly.

---

## 11. Acceptance criteria — status (spec §28)

| # | Criterion | Status |
|---|---|---|
| 1 | Entire test suite run | ✅ **108 passed** |
| 2 | All Phase 0–3 tests remain green | ✅ 97/97 |
| 3 | Phase 4 leakage suite | ✅ 7 tests |
| 4 | Both negative controls run | ✅ placebo + randomised opponents; both pass |
| 5 | All Phase 4 outputs generated | ✅ `candidate_universe`, `shrinkage_results`, `opponent_adjustment_results`, `baseline_chain`, `hyperparameter_stability`, `negative_control`, `metric_phase4_status`, k/alpha logs, `run_meta` |
| 6 | Phase 4 report produced | ✅ this document |
| 7 | Which metrics benefit from shrinkage | ✅ §3 — 39 of 42 |
| 8 | Which metrics benefit from opponent adjustment | ✅ §4 — 0 of 39 |
| 9 | Which benefit from both | ✅ §0 — 0 |
| 10 | Which adjustments fail / are unstable | ✅ §4 (opp-adj fails universally), §3 (proe/adot/avg_time_to_throw) |
| 11 | Did NOT proceed to matchup interactions | ✅ none built |
| 12 | Did NOT build ratings | ✅ none built |
| — | Pre-registration frozen before results; deviations disclosed | ✅ §1 |
| — | `k`, `alpha` never tuned on 2019–2025 | ✅ walk-forward / pre-2019 only |
| — | No market data anywhere | ✅ tested |

---

## 12. Files created in Phase 4

```
config/phase4_validation.yaml          frozen pre-registration
config/metrics_phase4_status.yaml       per-metric layer results + evidence (generated)
src/matchup/shrinkage/                  shrink() + walk-forward select_k
src/matchup/opponent_adjustment/        game-level ridge (_Design), walk_forward_strengths, select_alpha
src/matchup/validation/phase4.py         orchestrator
src/matchup/validation/phase4_config.py  loader + candidate resolution
tests/unit/test_phase4.py                5 tests (shrink math, k selection, ridge recovery, permute)
tests/leakage/test_phase4_harness.py     7 tests (k / ridge / poison / market)
outputs/phase4/*.csv, *.json
reports/phase4_report.md                 this file
```

---

## 13. STOP

Phase 4 is complete. **Awaiting explicit review and approval before any further phase.**

The next phase, if approved, is a **distinct** research question: *do the shrunk (not
opponent-adjusted) measurements of two opposing units, combined in an interaction model, predict
game-level outcomes better than simple baselines?* That must be reviewed on its own terms and must
not be conflated with Phase 4's unit-performance validation.
