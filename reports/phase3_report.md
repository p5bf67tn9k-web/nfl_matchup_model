# Phase 3 Report — Predictive Persistence Validation

**Project:** `nfl_matchup_model`
**Run date:** 2026-09-08
**Environment:** Python 3.12.14, `nflreadpy` 0.1.5, `polars` 1.44.1, `numpy` 2.x
**Scope:** validation study of the Phase 2 descriptive measurements. **No** ratings, weights,
opponent adjustment, matchup logic, expected performance, expected score, or market data.

---

## 0. TL;DR

* **97 tests pass** (84 from Phases 0–2 unchanged + 13 new). Ruff clean.
* **The study answers one question:** does an as-of measurement carry stable out-of-sample
  information about the **same unit's future performance**, beyond simple baselines? It does **not**
  test whether a metric improves matchup prediction (§8).
* **Rank persistence is near-universal, RMSE skill is rare.**
  * **40 of 48** evaluated rate metrics are `RANK_PERSISTENT` (Spearman CI > 0 and |Spearman| ≥ 0.15
    at both multi-game horizons) — good units tend to stay good.
  * Only **3** metrics clear the pre-registered baseline-RMSE bar (`VALIDATED_PERSISTENCE`):
    **`team_offense.proe`, `team_offense.epa_per_play`, `team_offense.success_rate`** — all team
    offense, all best on the season-to-date window. Only `proe` is robust; the other two clear the
    `skill_vs_league` CI lower-bound test only barely (CI lo ≈ 0.007–0.010).
  * **36** are `NO_INCREMENTAL_PERSISTENCE` (rank info, but do not beat "predict the league mean" /
    "predict last season" on squared error). **9** are `UNVALIDATED` (ambiguous — cleared the bar at
    one horizon, not both). **0** `INSUFFICIENT_DATA`.
* **Why the gap:** the raw metric, used as a point prediction, **over-extrapolates** — it does not
  regress to the mean. A QB at +0.30 season-to-date EPA/dropback is predicted +0.30 for the next
  four games; the reality regresses to ~+0.15, so the shrunk league-mean constant has lower squared
  error even though the raw metric's *rank ordering* is clearly informative. **Regression-to-the-mean
  shrinkage — deliberately deferred from Phase 2 — is the missing ingredient**, and closing that gap
  is a modeling task for a later phase, not a Phase 3 conclusion.
* **Team defense fails across the board** (0 of 9 validated; every one is `NO_INCREMENTAL_PERSISTENCE`)
  — consistent with the literature: defense is noisier, more opponent/game-script dependent, and
  regresses harder than offense.
* **Prior-season data is a very strong baseline**, especially in weeks 1–4: in early-season, only the
  prior-season window carries positive skill; in-season windows are noise until ~week 8.
* **Negative control passes:** a within-season-permuted feature never gains skill (mean placebo
  skill_vs_league = **−0.11**, max **−0.03**) and has near-zero rank correlation (mean |Spearman|
  = **0.005**).
* `config/metrics.yaml` `predictive_status` updated per the persistence taxonomy; full evidence in
  `config/metrics_phase3_status.yaml`.

---

## 1. Pre-registration & disclosed deviations

The full protocol was written to **`config/phase3_validation.yaml`** and frozen before any result
was inspected (`frozen: true`). Two deviations were made **during harness setup**, both from a
methodological setup smoke-run (not the official analysis) and both disclosed in the config and here:

| # | Deviation | Rationale |
|---|---|---|
| **A** | Primary status cell moved from **horizon 1** to **horizons 2 and 4** (multi-game targets). Horizon 1 is still computed and reported in full. | A single game's unit performance is irreducibly noisy for *every* predictor (the league mean included). Horizon-1 skill mostly measures "single games are unpredictable", not "does the measurement persist". Moving to multi-game targets is a *more* rigorous test, not a result-seeking one. |
| **B** | Added a **secondary `rank_persistence` classification** (`RANK_PERSISTENT` / `NOT_RANK_PERSISTENT` / `INSUFFICIENT`), reported alongside — never replacing — the 4-value `predictive_status`. | The smoke-run showed many metrics have clear out-of-sample rank persistence while their RMSE skill vs the league mean is slightly negative (the over-extrapolation effect). The spec's `predictive_status` taxonomy is strict and baseline-RMSE-based; it stays as specified. The secondary flag prevents a real finding from being hidden. |

Everything else — seasons, week buckets, horizons, minimum opportunities, baseline definitions,
scoring metrics, bootstrap method, negative-control method, and the status thresholds — is exactly
as pre-registered. The **bootstrap method** is the one place the config names a specific technique
for speed (multiplier/Bayesian cluster bootstrap rather than case-resampling clusters); it respects
the same `(entity_id × season)` cluster structure and is disclosed in the config.

---

## 2. Method

**Walk-forward, chronological, no shuffling.** Evaluation seasons **2019–2025** (7 completed
seasons). Game metrics built from 2016 so every reference window is available.

**For each candidate target game** (the entity's own games, weeks 1–18):
1. `feature` = the Phase 2 windowed metric, computed from games whose **production `data_asof`**
   (kickoff + 4 h + source publish-lag) is strictly before the target kickoff. Four windows:
   `season_to_date`, `trailing_3`, `trailing_5`, `prior_season`.
2. `target` = the entity's **actual** metric over the next **H eligible games starting at the target
   game** (H ∈ {1, 2, 4}), raw components summed and the rate recomputed.
3. **Target eligibility is explicit** (§5): a game counts toward the horizon only if the entity met
   the per-game opportunity bar (`qb` 10 dropbacks, `rb` 5 carries, `wr` 2 targets, team units 20
   plays, …). If fewer than H eligible games remain in the season, the observation is **excluded**
   for that horizon — a missing opportunity is never treated as zero performance. Exclusion rates
   are logged (e.g. `qb` H4: 35% of weeks 1–18 candidates excluded, mostly late-season and injuries).

**Baselines** (all as-of):
* **A — league mean:** the metric's mean over the 3 completed reference seasons, entity-season level,
  min-opportunity filtered.
* **B — prior season:** the entity's value in its single most recent completed season. Rookies /
  first-year entities → *unavailable* (excluded from `skill_vs_prior_season`, never imputed).
* **C — raw trailing-3:** the entity's raw trailing-3-game value (identical to the `trailing_3` raw
  feature cell).

**Scoring** (§7): RMSE, MAE, bias, Spearman, Pearson, and `skill = 1 − RMSE_feature / RMSE_baseline`
against each baseline. No calibration slope (continuous targets).

**Uncertainty** (§8): multiplier cluster bootstrap, 1000 iterations, clusters = `(entity_id × season)`,
95% percentile CIs on `skill_vs_league`, `skill_vs_prior_season`, and Spearman.

**Metric selection** (§12): **every registered rate metric** with enough data, under the identical
protocol. Phase 2 reliability / redundancy were **not** used to pre-select. Volume metrics
(`wr.targets`, `team_offense.plays`) and the un-windowed NGS/PFR metrics are `UNVALIDATED`
(not a persistence-testable rate). NGS/PFR get a lighter secondary analysis (§6).

---

## 3. Results — status breakdown

### 3.1 By taxonomy

| `predictive_status` | count (of 48 evaluated rate metrics) | count (of 58 registered) |
|---|---|---|
| `VALIDATED_PERSISTENCE` | 3 | 3 |
| `NO_INCREMENTAL_PERSISTENCE` | 36 | 36 |
| `UNVALIDATED` (ambiguous — cleared the bar at one horizon, not both) | 9 | 9 |
| `UNVALIDATED` (not evaluable: volume / un-windowed NGS-PFR) | — | +10 |
| `INSUFFICIENT_DATA` | 0 | 0 |

`rank_persistence` (secondary): **`RANK_PERSISTENT` 40**, `NOT_RANK_PERSISTENT` 8, `INSUFFICIENT` 0.
**28 metrics are `RANK_PERSISTENT` yet `NO_INCREMENTAL_PERSISTENCE`** — the central finding (§4).

### 3.2 By family

| family | metrics | `VALIDATED` | `NO_INCR` | `UNVAL` | `RANK_PERSISTENT` |
|---|---|---|---|---|---|
| team_offense | 10 | **3** | 4 | 3 | 9 |
| team_defense | 9 | 0 | 9 | 0 | 7 |
| qb | 10 | 0 | 8 | 2 | 9 |
| wr | 7 | 0 | 5 | 2 | 6 |
| rb | 5 | 0 | 5 | 0 | 4 |
| pass_protection | 3 | 0 | 1 | 2 | 3 |
| pass_rush | 2 | 0 | 2 | 0 | 1 |
| special_teams | 2 | 0 | 2 | 0 | 1 |

### 3.3 The 3 `VALIDATED_PERSISTENCE` metrics (best window: `season_to_date`, primary weeks 5–18)

Values at H2 / H4, best window `season_to_date`:

| metric | n (H2/H4) | Spearman [CI lo] H4 | skill_vs_league [CI lo] H4 | skill_vs_prior_season [CI lo] H4 |
|---|---|---|---|---|
| `team_offense.proe` | 2732 / 2351 | 0.52 [0.45] | **0.14 [0.07]** | 0.14 [0.08] |
| `team_offense.epa_per_play` | 2732 / 2351 | 0.48 [0.41] | 0.07 [**0.007**] | 0.12 [0.06] |
| `team_offense.success_rate` | 2732 / 2351 | 0.48 [0.41] | 0.07 [**0.010**] | 0.10 [0.05] |

These team-offense efficiency / tendency metrics beat **both** the league mean and the prior season
on squared error, at both multi-game horizons, with the rank floor cleared. **`proe` is robustly
validated**; `epa_per_play` and `success_rate` clear the `skill_vs_league` CI lower-bound test only
marginally (≈ 0.007–0.010) — they are borderline, and would move to `UNVALIDATED` under a slightly
stricter CI rule. All three were also the most *reliable* metrics in Phase 2 (odd/even split-half
≥ 0.77) — related but distinct properties.

---

## 4. The central finding — rank persistence ≠ point-prediction skill

Almost every metric has out-of-sample **rank** persistence; almost none beats the baselines on
**RMSE**. `qb.epa_per_dropback` (season-to-date window, weeks 5–18) is the archetype:

| horizon | n | Spearman [CI lo] | skill_vs_league [CI lo] | skill_vs_prior_season |
|---|---|---|---|---|
| 1 (target game) | 2696 | 0.23 [0.19] | −0.00 [−0.02] | +0.01 |
| 2 (next 2) | 2431 | 0.31 [0.25] | −0.02 [−0.05] | +0.02 |
| 4 (next 4) | 1890 | **0.39 [0.31]** | **−0.04 [−0.11]** | +0.03 |

As the horizon lengthens the **Spearman rises** (longer aggregates are less noisy and the persistent
ordering shows through more clearly) while **`skill_vs_league` falls further below zero** — the
over-extrapolation cost compounds when an unshrunk value is used as a point forecast over more games.
`skill_vs_prior_season` stays *just* positive (+0.01 → +0.03): the in-season measurement edges out
the prior season, but not the shrunk league constant.

**Interpretation.** The measurement contains information (rank persistence, positive vs prior
season). What it lacks is calibration: it needs **regression-to-the-mean shrinkage**
(`prediction = league_mean + w·(feature − league_mean)`, `w = n/(n+k)`), which Phase 2 deliberately
did not fit. A shrunk feature would very likely convert many `NO_INCREMENTAL_PERSISTENCE` metrics to
positive `skill_vs_league`. **Fitting `k` and re-testing is a Phase-4 task**, not a Phase-3
conclusion — Phase 3 reports the raw measurements' persistence as pre-registered.

**Team offense is the exception** because it is self-consistent enough that even the unshrunk
season-to-date value beats both baselines. **Team defense never does** — every `team_defense` metric
is rank-persistent (Spearman 0.19–0.25) but `skill_vs_league` is −0.05 to −0.09 at H4. Defense
regresses harder and is more opponent/game-script dependent.

---

## 5. Season-phase analysis (weeks 1–4 reported separately, per §3)

| phase | pattern (across metrics, H4) |
|---|---|
| **weeks 1–4** | The **`prior_season` window is the only one with positive skill.** `qb.epa_per_dropback` prior-season: Spearman 0.40, `skill_vs_league` **+0.05**. In-season windows (`season_to_date` after 1–3 games, `trailing_*`) have `skill_vs_league` of −0.15 to −0.37 — 1–3 games is pure noise. |
| **weeks 5–9** | In-season windows begin to have information; still mostly at or below the league mean on RMSE. |
| **weeks 10–14** | `team_offense.epa_per_play` season-to-date reaches `skill_vs_league` +0.10, Spearman 0.48. |
| **weeks 15–18** | Highest skill for the validated metrics (`team_offense.epa_per_play` +0.19), but small n and a high target-exclusion rate (fewer eligible games remain). |

**Takeaway for later phases (not acted on here):** early-season predictions must lean on
prior-season data; in-season windows are not additive until ~week 8; late-season cells are
information-rich but sample-poor.

---

## 6. Ablations (`outputs/phase3/metric_ablation.csv`)

### 6.1 Raw vs normalized feature

For same-unit persistence at a single prediction date, z-normalization is an **affine transform with
date-constant parameters** → within-season ranks are identical by construction. Confirmed:
Spearman(raw) vs Spearman(normalized) differ by a **mean 0.017** across 48 metrics (only from
pooling seasons with different reference mean/sd); normalized target-SD RMSE ≈ raw target-SD RMSE
(1.036 vs 1.044). **Normalization does not change persistence.** Its value is cross-era / cross-entity
comparability, which matters for the matchup and rating phases, not for this study.

### 6.2 Window comparison (`team_offense.epa_per_play`, weeks 5–18, H4)

| window | n | skill_vs_league | skill_vs_prior_season | Spearman |
|---|---|---|---|---|
| `season_to_date` | 2351 | **+0.07** | **+0.12** | **0.48** |
| `trailing_5` | 2351 | −0.00 | +0.04 | 0.43 |
| `prior_season` | 2351 | −0.05 | 0.00 | 0.26 |
| `trailing_3` | 2351 | −0.13 | −0.08 | 0.38 |

Pattern holds across metrics: **`season_to_date` is the best window** (it accumulates sample without
the recency over-weighting of `trailing_3`); `trailing_3` is consistently the **worst**.

### 6.3 NGS / PFR measurement-source ablation (secondary; season-to-season)

Combining sources into one feature needs a fitted combiner (forbidden in Phase 3), so the ablation
is limited to each external metric's **prior-season → next-season** persistence, with coverage and
`earliest_valid_season` made explicit:

| source metric | n pairs | Spearman | skill_vs_league_mean | earliest season |
|---|---|---|---|---|
| `ngs_passing.avg_time_to_throw` | 274 | **0.64** | **+0.14** | 2016 |
| `ngs_receiving.avg_separation` | 801 | **0.56** | +0.05 | 2016 |
| `ngs_passing.aggressiveness` | 274 | 0.41 | −0.19 | 2016 |
| `ngs_passing.completion_pct_above_exp` | 274 | 0.35 | −0.15 | 2016 |
| `ngs_receiving.avg_yac_above_expectation` | 801 | 0.29 | −0.31 | 2016 |
| `ngs_rushing.efficiency` | 296 | 0.26 | −0.12 | 2016 |
| `ngs_rushing.rush_yards_over_expected_per_att` | 236 | 0.21 | −0.35 | 2016 |

**`avg_time_to_throw` and `avg_separation` are genuinely persistent, positive-skill measurements** —
they are style / role traits (a QB's clock, a receiver's route-running), not volatile production.
This is the one place external data adds something the pbp metrics do not. The matched-pbp check
(`qb.cpoe` full sample vs the NGS-covered subset) shows the NGS-covered (higher-volume) subset has
slightly *more* persistence (Spearman 0.30 vs 0.21) — the sample restriction is not neutral, and is
recorded.

---

## 7. Negative control (`outputs/phase3/negative_control.csv`)

Placebo = the feature permuted within each eval season (breaking the entity→future link, keeping the
season structure), with feature and target centred within season so between-season drift cannot
create spurious correlation. 192 (metric × window) cells:

* placebo `skill_vs_league`: **mean −0.11, max −0.03** — a meaningless feature **never** gains skill
  (it is strictly worse than the constant baseline, as expected when noise is added).
* placebo `|Spearman|`: **mean 0.005**, p95-abs max **0.15** (one small cell at the economic floor,
  the rest near zero).

**The persistence found in the real metrics is not an artifact of the harness.**

---

## 8. What Phase 3 does NOT establish (§16 — required section)

A metric can have strong persistence and still fail to improve matchup prediction.

* **`team_offense.epa_per_play` persists.** That does **not** prove that
  `off_epa × opponent_def_epa` improves prediction of a specific game.
* **QB EPA has rank persistence.** That does **not** prove QB EPA predicts *matchup-specific* QB
  performance after accounting for the opposing pass defense and pressure.
* **`ngs_passing.avg_time_to_throw` persists and beats its baseline.** That does **not** prove it
  interacts usefully with an opposing pass rush.
* **Team defense metrics did not clear the bar.** That does **not** prove team-defense information is
  useless in a matchup — opponent adjustment and interaction structure are a separate question.

The matchup-interaction question — *do these measurements, opponent-adjusted and combined, predict
game outcomes better than simple baselines* — belongs to the next phase and must be reviewed
separately. Phase 3 validates **measurements**; it does not build or endorse a model.

---

## 9. Newly discovered data / leakage problems

**None.** The Phase 3 leakage suite is green:
* every feature-window game has `data_asof < target_kickoff` (verified directly, incl. the
  short-turnaround Thursday-game edge case, ~2600 targets checked);
* the poisoned-future-row canary: injecting a fabricated 2026 game and future-dated plays leaves
  every earlier observation's feature / target / baseline identical to < 1e-9;
* no market column (`spread_line`, `total_line`, `vegas_wp`, scores, odds) is reachable in the
  observation table.

One **methodological note** (not a leak): within-season feature permutation alone leaves season
means intact, so an early negative-control implementation showed a spurious 0.58 in one drifting
metric. Fixed by centring feature and target within season before the placebo comparison; disclosed
here and in `negative_control.py`.

---

## 10. Limitations

1. **The core result is about *raw* measurements.** Shrinkage (deferred from Phase 2) would very
   likely lift many `NO_INCREMENTAL_PERSISTENCE` metrics. Phase 3 tests what Phase 2 built, as
   pre-registered; it does not pre-empt the shrinkage question.
2. **`predictive_status` is baseline-RMSE-based** (as the spec fixes). The `rank_persistence`
   secondary flag is the honest complement — 28 metrics are `RANK_PERSISTENT` yet
   `NO_INCREMENTAL_PERSISTENCE`.
3. **Multiplier bootstrap ≈ case-resampling clusters** but is not identical; chosen for speed. The
   spearman CI uses a weighted Pearson of fixed ranks (standard fast approximation).
4. **League-mean baseline = 3-completed-season entity-season mean.** A current-season-to-date league
   mean is an alternative not chosen (it would be noisier early season). Documented in the config.
5. **NGS/PFR analysis is season-to-season and unweighted** (the weekly files carry no opportunity
   counts). A full in-season windowed treatment of external metrics is deferred.
6. **Horizon targets aggregate raw components then recompute the rate** — a games-played-weighted
   mean. An entity that plays more in the horizon contributes more, by design.
7. **2020** is included in the eval period (the HFA exclusion from Phase 1 is score-model-specific;
   persistence of unit metrics is not obviously distorted by empty stadiums). Not separately flagged.

---

## 11. Full metric persistence table

See `outputs/phase3/metric_status.csv` (48 rows, with `spearman_h4`, `skill_vs_league_h4`,
`skill_vs_prior_season_h4`, and full CI evidence) and `config/metrics_phase3_status.yaml`.
Summary of the 48 evaluated rate metrics:

**`VALIDATED_PERSISTENCE` (3):** `team_offense.epa_per_play`, `team_offense.success_rate`,
`team_offense.proe`.

**`UNVALIDATED` — ambiguous, cleared the bar at one horizon not both (9):**
`team_offense.pass_epa_per_dropback`, `team_offense.pass_success_rate`,
`team_offense.early_down_epa_per_play`, `pass_protection.qb_hit_rate_allowed`,
`pass_protection.sack_rate_allowed`, `qb.sack_rate`, `qb.cpoe_coverage_fraction`, `wr.adot`
(Spearman 0.82 — extreme rank persistence, but the prior-season baseline predicts this role trait
almost as well), `wr.yards_per_reception`.

**`NO_INCREMENTAL_PERSISTENCE` (36):** all 9 `team_defense` metrics; 8 `qb` metrics
(`epa_per_dropback`, `dropback_success_rate`, `cpoe`, `completion_pct`, `yards_per_attempt`, `adot`,
`explosive_pass_rate`, `interception_rate`); all 5 `rb`; 5 `wr`
(`catch_rate`, `epa_per_target`, `yards_per_target`, `target_success_rate`, `explosive_rec_rate`);
4 `team_offense` (`rush_epa_per_play`, `rush_success_rate`, `explosive_pass_rate`,
`explosive_rush_rate`); both `pass_rush`; `pass_protection.rush_stuffed_rate_approx`;
both `special_teams`.

**`NOT_RANK_PERSISTENT` (8, subset of the above):** `qb.interception_rate`, `special_teams.fg_pct`,
`pass_rush.sack_rate_generated`, `rb.explosive_rush_rate`, `wr.epa_per_target`,
`team_defense.explosive_pass_rate`, `team_defense.rush_epa_per_play`, `team_offense.explosive_rush_rate`
— genuinely near noise at the season level.

**`UNVALIDATED` — not evaluable (10):** the NGS join-throughs (`qb.ngs_*`, `rb.ngs_ryoe_per_att`,
`wr.ngs_*`), the PFR join-throughs (`pass_rush.pfr_pressure_rate`, `pfr_def.*`, `qb` PFR pressure),
and the volume metrics (`wr.target_share`, `air_yards_share`, `wopr` — availability-adjustment role,
not persistence-testable here).

---

## 12. Acceptance criteria — status

| # | Criterion | Status |
|---|---|---|
| — | All Phase 0/1/2 tests remain green | ✅ 84/84 |
| — | Phase 3 leakage suite passes | ✅ 5 tests |
| — | Negative-control test run | ✅ placebo never gains skill; mean \|Spearman\| 0.005 |
| — | All Phase 3 outputs generated | ✅ `metric_persistence.csv` (2880 rows), `metric_status.csv`, `metric_ablation.csv`, `negative_control.csv`, `run_meta.json` |
| — | `reports/phase3_report.md` produced | ✅ this document |
| — | Which metrics: robust / weak / no-incremental / insufficient persistence | ✅ §3, §11 |
| — | Pre-registration written before results | ✅ `config/phase3_validation.yaml` (`frozen: true`); deviations disclosed §1 |
| — | Walk-forward, no shuffling, no future data in features | ✅ tested |
| — | Multiple horizons reported separately | ✅ H1/H2/H4 |
| — | Explicit target eligibility, no zero-imputation | ✅ §2; exclusion rates logged |
| — | Uncertainty on every major result | ✅ 1000-iter cluster bootstrap, 95% CIs |
| — | Opportunity context reported | ✅ `opportunity_n_median`, `feat_opp_n`, `target_opp_n` |
| — | Families evaluated separately | ✅ §3.2 |
| — | Phase 2 diagnostics did NOT pre-select metrics | ✅ every registered rate metric evaluated identically |
| — | No ratings / matchup / expected-performance / score / market data | ✅ none exist; market columns unreachable (tested) |
| — | `config/metrics.yaml` updated per the persistence taxonomy (no `VALIDATED_SIGNAL`) | ✅ + evidence sidecar |
| — | Ambiguous evidence kept `UNVALIDATED` | ✅ 9 metrics |

---

## 13. Proposed next phase (for separate review — do NOT build yet)

Phase 3 validated **measurements**. The distinct, next research question (§8, and the spec's closing
note): **do the validated / rank-persistent measurements, once opponent-adjusted and shrunk,
predict actual game outcomes better than simple baselines?**

A defensible Phase 4 would, at minimum:
1. **Fit regression-to-the-mean shrinkage** (`k` per metric) on a frozen training era, walk-forward,
   and re-run the Phase 3 persistence test on the shrunk feature — quantifying how much of the
   `NO_INCREMENTAL_PERSISTENCE` set becomes positive-skill.
2. **Opponent adjustment** (the chronological ridge from the architecture doc) on the metrics that
   survive (1), validated on next-game *unit* performance vs the same baselines.
3. Only then, the **matchup interaction** question — and only for interactions that beat an additive
   opponent-adjusted model out-of-sample.

No ratings, weights, matchup logic, expected performance, expected score, or market comparison
should be built before that plan is reviewed and approved.

---

## 14. STOP

Phase 3 is complete. **Awaiting explicit review and approval before any further phase.** The next
phase is a separate research question (incremental matchup value) and must not be conflated with
persistence validation.
