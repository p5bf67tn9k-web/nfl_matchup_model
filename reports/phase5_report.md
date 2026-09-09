# Phase 5 — Matchup Interaction Validation

**Verdict: `STOP_NO_RELIABLE_MATCHUP_SIGNAL`**

Pre-registered in [`config/phase5_validation.yaml`](../config/phase5_validation.yaml) (frozen,
`schema_version: 1`) before any 2019–2025 result was inspected. All numbers below are reproducible
with `make phase5-validation` (bootstrap 1000 iterations, seed 20260908). Outputs in
[`outputs/phase5/`](../outputs/phase5/).

---

## 1. Executive summary

Phase 5 asked one question:

> Do measurements of two opposing units interact in a predictable way, such that the combination of
> Team A's shrunk unit measurement (`A`) and Team B's opposing-unit shrunk measurement (`B`)
> predicts Team A's **future** unit performance better than the additive model `A + B` (no
> interaction term)?

**Answer: no — not for any of the nine pre-registered unit-vs-unit matchups that could be tested.**

* The interaction term (`M4`: `Y ~ A_c + B_c + A_c·B_c`) never beat the additive model (`M3`:
  `Y ~ A + B`). Across all 9 matchups × {H2, H4}, `interaction_skill = 1 − RMSE(M4)/RMSE(M3)` ranged
  from **−0.0016 to +0.0006** (economic floor: +0.01). 0 of 18 tests were FDR-significant at
  q = 0.10 (all one-sided p ≥ 0.21; median p ≈ 0.79).
* The additive opponent term (`M3` vs `M1`: `Y ~ A`) also added essentially nothing:
  `skill(M3 vs M1)` ranged from **−0.002 to +0.005**, with confidence intervals straddling zero at
  all but one cell.
* What *does* replicate is the Phase 4 finding: a unit's **own** shrunk measurement predicts its
  own future performance. `skill(M1 vs league mean)` was **+0.03 to +0.13** with the 95% CI lower
  bound above zero at both horizons for all 9 matchups.

Every resolved matchup is therefore classified **`UNIT_ONLY`**: the unit measurement carries
signal; the opponent measurement adds no reliable incremental value, additively or interactively,
to predicting that unit's future performance in this experiment.

This is a **null result, and a valid one.** It does not say matchups are irrelevant to football
outcomes. It says: *when the target is a unit's own forward EPA/success-rate aggregate, and the
predictors are the two units' shrunk season-to-date measurements, a linear interaction between them
does not improve out-of-sample prediction over simply using the unit's own measurement.*

---

## 2. The one question, and what this phase is

Phase 5 occupies exactly one segment of the intended architecture:

```
shrunk unit estimate  ──▶  [ matchup interaction ]  ──▶  expected unit performance
```

It does **not** touch game prediction, point spread, margin, win probability, team ratings,
composites, 0–100 scores, or any market data. The models are ordinary least squares with ≤ 4
coefficients. There is no feature selection on the evaluation period, no ensembling, no tree model,
no neural net. (All of these are explicitly forbidden by the spec and by
`config/phase5_validation.yaml`.)

---

## 3. What Phase 5 does NOT establish

* **Not** that matchups don't matter in football. Coaches game-plan around specific matchups; that
  is not in question. Phase 5 tests one narrow statistical form of "matchup value."
* **Not** that a different target (e.g. single-play distributions, situational splits, pressure
  rate on specific down-and-distance) would show the same null. Only the pre-registered
  unit-performance aggregates were tested.
* **Not** that a non-linear or higher-order interaction is absent — only that the pre-registered
  centred bilinear term `A_c·B_c` (and the raw `A·B`) does not help.
* **Not** a statement about game-level prediction, which is a later phase with its own target and
  its own validation.
* A `UNIT_ONLY` status **does not** mean the unit measurement is validated for matchup or
  game prediction — only that, among {unit, +opponent additive, +opponent interaction}, the unit
  term is the only one that carries out-of-sample signal for this target.

---

## 4. Pipeline position & feature provenance

| Element | Value |
|---|---|
| Feature `A` | Team A's **corrected Phase 4 `shrunk_feature`** for the offensive metric — `shrunk = μ + n/(n+k)·(raw − μ)`, `k` chosen walk-forward from `{1,2,4,8,12,16}`, `season_to_date` window, strictly as-of the target kickoff. |
| Feature `B` | The **same shrunk_feature** computed for the *opposing* unit A actually faces in the target game (looked up via the team game sequence). |
| Target `Y` | Team A's **own** realised value of the offensive metric over the next *H* eligible games starting at the target game (Phase 3 target construction: raw components summed, rate recomputed; require the full horizon; same season; **never impute a missing game as zero**). |
| `M0` baseline | `baseline_league` — the Phase 3 as-of mean of the metric over the 3 completed reference seasons. |
| Windows | `season_to_date` only (the a-priori choice from Phase 3/4). |
| Weeks | 5–18 (primary persistence window). |
| Observation seasons | 2016–2025 built; **2016–2018 exist only to train the walk-forward models for OOS 2019**. |
| OOS evaluation seasons | 2019–2025 (7 seasons). |

Full per-matchup feature registry: [`outputs/phase5/phase5_feature_registry.csv`](../outputs/phase5/phase5_feature_registry.csv).

---

## 5. Matchup definitions & candidate universe

13 unit-vs-unit matchups were pre-registered
([`outputs/phase5/matchup_definitions.csv`](../outputs/phase5/matchup_definitions.csv)). The frozen
selection rule (§29): a matchup **resolves** only if **both** its offensive metric and its
opposing-unit metric are `SHRINKAGE_ADDS_VALUE` in the corrected Phase 4. Previously-rejected
metrics cannot re-enter.

**9 of 13 resolved.** The 4 that did not resolve were dropped because the opposing-unit metric
never entered the Phase 4 candidate universe (it is Phase 3 `NOT_RANK_PERSISTENT` /
`NO_INCREMENTAL_PERSISTENCE`), so it cannot be `SHRINKAGE_ADDS_VALUE`:

| Matchup | Offensive unit | Opposing unit | Why dropped |
|---|---|---|---|
| `rush_game_epa` | `team_offense.rush_epa_per_play` ✔ | `team_defense.rush_epa_per_play` | opposing metric not in Phase 4 universe (Phase 3 NOT_RANK_PERSISTENT) |
| `explosive_pass` | `team_offense.explosive_pass_rate` ✔ | `team_defense.explosive_pass_rate` | opposing metric not in Phase 4 universe |
| `explosive_rush` | `team_offense.explosive_rush_rate` | `team_defense.explosive_rush_rate` ✔ | offensive metric not in Phase 4 universe |
| `protection_vs_rush_sack` | `pass_protection.sack_rate_allowed` ✔ | `pass_rush.sack_rate_generated` | opposing metric not in Phase 4 universe |
| `receiving_vs_coverage` | — | — | deferred at pre-registration: no defensible coverage-quality measurement in the available data |

The 9 resolved matchups:

| Matchup | `A` (Team A unit) | `B` (opposing unit) |
|---|---|---|
| `pass_game_epa` | `team_offense.pass_epa_per_dropback` | `team_defense.pass_epa_per_dropback` |
| `pass_game_success` | `team_offense.pass_success_rate` | `team_defense.pass_success_rate` |
| `rush_game_success` | `team_offense.rush_success_rate` | `team_defense.rush_success_rate` |
| `overall_epa` | `team_offense.epa_per_play` | `team_defense.epa_per_play` |
| `overall_success` | `team_offense.success_rate` | `team_defense.success_rate` |
| `early_down_epa` | `team_offense.early_down_epa_per_play` | `team_defense.early_down_epa_per_play` |
| `protection_vs_rush_hit` | `pass_protection.qb_hit_rate_allowed` | `pass_rush.qb_hit_rate_generated` |
| `qb_vs_pass_defense_epa` | `qb.epa_per_dropback` | `team_defense.pass_epa_per_dropback` |
| `qb_vs_pass_defense_success` | `qb.dropback_success_rate` | `team_defense.pass_success_rate` |

Full table with statuses and reasons:
[`outputs/phase5/matchup_candidate_universe.csv`](../outputs/phase5/matchup_candidate_universe.csv).

---

## 6. Target construction

The target is always **Team A's own future** offensive metric — never a game score, margin, or
market outcome. For `qb_vs_pass_defense_*` the entity is the individual passer and the target is
that passer's forward dropback-EPA / dropback-success aggregate. Eligibility is inherited verbatim
from Phase 3/4: per-game minimum opportunities, full horizon required, same-season only, missing
opportunity is never zero — the observation is excluded for that horizon and the reason logged.

H2 and H4 are the primary status horizons. H1 (the single next game) is computed and reported as a
diagnostic only, because a single game's unit performance is irreducibly noisy for every predictor.

---

## 7. Point-in-time & leakage controls

* `A` and `B` are both built by the Phase 3/4 observation pipeline, which enforces
  `data_asof < target_kickoff_utc` with the per-source publish lag.
* Walk-forward: for OOS season *S*, every model is fit **only** on observations with target season
  `< S`, then predicts *S*. Model coefficients, and the training-set means used to centre `M4`, come
  strictly from prior seasons.
* The shrinkage `k` for each `shrunk_feature` row was itself chosen walk-forward in Phase 4.
* **Leakage canaries** (all green — see §13 and the test suite):
  * `future_row_poison` — the observation builder is deterministic and strictly as-of; a fabricated
    2026 game cannot enter the 2016–2025 evaluation or alter any existing row.
  * `test_walk_forward_is_chronological` — poisoning a later season leaves every earlier season's
    predictions byte-identical.
  * `test_opposing_unit_is_the_actual_opponent` — `B` is cross-checked against the team game
    sequence: it is the unit A actually plays.
  * `test_no_market_columns_anywhere` — no spread / total / moneyline / score columns anywhere in
    the Phase 5 frames.

---

## 8. Models

All ordinary least squares, fit walk-forward. OLS (not Ridge) was pre-registered because each model
has ≤ 4 predictors on ~1,800–2,850 rows — regularisation is unnecessary and would add a
hyperparameter.

| Model | Form | Question it answers |
|---|---|---|
| `M0` | predict `baseline_league` | the league-mean baseline |
| `M1` | `Y ~ 1 + A` | does the unit's own measurement help? |
| `M2` | `Y ~ 1 + B` | does the opponent's measurement alone help? |
| `M3` | `Y ~ 1 + A + B` | does adding the opponent **additively** help beyond `M1`? |
| `M4` (centered) | `Y ~ 1 + A_c + B_c + A_c·B_c`, `A_c = A − mean_A(train)` | **the primary question** — does the interaction help beyond `M3`? |
| `M4` (raw) | `Y ~ 1 + A + B + A·B` | reported alongside; not the status form |
| `M_rel` | `Y ~ 1 + (A − B)` | sensitivity only (§10) — matchup-relative feature |

**Primary comparison:** `interaction_skill = 1 − RMSE(M4_centered) / RMSE(M3_additive)`.

---

## 9. Walk-forward protocol

7 expanding-window folds (predict 2019 from 2016–2018, …, predict 2025 from 2016–2024). Predictions
are pooled across folds; scoring and the multiplier (Bayesian) cluster bootstrap — Exponential(1)
weights per `(entity_id × season)` cluster, 1000 iterations, seed 20260908 — are computed on the
pooled OOS predictions. One-sided bootstrap p-value = fraction of resamples with
`interaction_skill ≤ 0`.

---

## 10. Baseline results (M0 / M1 / M2 / M3)

Full table: [`outputs/phase5/phase5_baseline_results.csv`](../outputs/phase5/phase5_baseline_results.csv).

| Matchup | H | n | `skill(M1 vs league)` [CI lo] | `skill(M2 vs league)` | `skill(M3 vs M1)` [CI lo] |
|---|---|---|---|---|---|
| pass_game_epa | 2 | 2634 | **0.060** [0.041] | 0.006 | 0.002 [−0.001] |
| pass_game_epa | 4 | 2210 | **0.093** [0.062] | 0.007 | −0.001 [−0.002] |
| pass_game_success | 2 | 2634 | **0.067** [0.046] | 0.009 | 0.002 [−0.001] |
| pass_game_success | 4 | 2210 | **0.099** [0.066] | 0.010 | −0.001 [−0.003] |
| rush_game_success | 2 | 2634 | **0.031** [0.016] | 0.004 | −0.002 [−0.006] |
| rush_game_success | 4 | 2210 | **0.051** [0.024] | −0.004 | −0.002 [−0.003] |
| overall_epa | 2 | 2634 | **0.084** [0.060] | 0.009 | 0.004 [0.000] |
| overall_epa | 4 | 2210 | **0.128** [0.091] | 0.009 | −0.001 [−0.002] |
| overall_success | 2 | 2634 | **0.091** [0.064] | 0.011 | 0.001 [−0.002] |
| overall_success | 4 | 2210 | **0.133** [0.095] | 0.010 | −0.002 [−0.004] |
| early_down_epa | 2 | 2634 | **0.051** [0.034] | 0.008 | 0.002 [−0.001] |
| early_down_epa | 4 | 2210 | **0.080** [0.053] | 0.010 | −0.002 [−0.003] |
| protection_vs_rush_hit | 2 | 2634 | **0.084** [0.059] | 0.004 | 0.005 [0.002] |
| protection_vs_rush_hit | 4 | 2209 | **0.125** [0.087] | −0.000 | 0.001 [−0.001] |
| qb_vs_pass_defense_epa | 2 | 2352 | **0.053** [0.036] | 0.009 | 0.001 [−0.002] |
| qb_vs_pass_defense_epa | 4 | 1782 | **0.088** [0.057] | 0.020 | −0.002 [−0.003] |
| qb_vs_pass_defense_success | 2 | 2352 | **0.070** [0.048] | 0.010 | 0.001 [−0.002] |
| qb_vs_pass_defense_success | 4 | 1782 | **0.107** [0.072] | 0.017 | −0.002 [−0.003] |

Reading: the unit's own shrunk measurement reliably beats the league mean (bold, CI lower bound
> 0 in every cell). The opponent measurement alone (`M2`) barely moves RMSE (≤ 2%). Adding the
opponent additively to the unit model (`M3` vs `M1`) is a wash — the only cell with a CI lower
bound strictly above zero is `protection_vs_rush_hit` at H2 (+0.005 [0.002]), and it fails the
+0.01 economic floor and does not hold at H4.

---

## 11. Interaction results (M4 centered + raw)

Full table: [`outputs/phase5/phase5_interaction_results.csv`](../outputs/phase5/phase5_interaction_results.csv).

| Matchup | H | `interaction_skill` (centered) | `interaction_skill` (raw) | `M_rel` (A−B) vs additive |
|---|---|---|---|---|
| pass_game_epa | 2 | −0.0012 | −0.0012 | −0.029 |
| pass_game_epa | 4 | −0.0003 | −0.0003 | −0.027 |
| pass_game_success | 2 | −0.0004 | −0.0004 | −0.030 |
| pass_game_success | 4 | −0.0007 | −0.0007 | −0.029 |
| rush_game_success | 2 | +0.0004 | +0.0004 | −0.023 |
| rush_game_success | 4 | +0.0006 | +0.0006 | −0.019 |
| overall_epa | 2 | −0.0016 | −0.0016 | −0.029 |
| overall_epa | 4 | −0.0006 | −0.0006 | −0.023 |
| overall_success | 2 | −0.0005 | −0.0005 | −0.028 |
| overall_success | 4 | −0.0005 | −0.0005 | −0.023 |
| early_down_epa | 2 | −0.0004 | −0.0004 | −0.024 |
| early_down_epa | 4 | −0.0004 | −0.0004 | −0.020 |
| protection_vs_rush_hit | 2 | +0.0004 | +0.0004 | −0.030 |
| protection_vs_rush_hit | 4 | −0.0006 | −0.0006 | −0.033 |
| qb_vs_pass_defense_epa | 2 | +0.0000 | +0.0000 | −0.023 |
| qb_vs_pass_defense_epa | 4 | −0.0003 | −0.0003 | −0.018 |
| qb_vs_pass_defense_success | 2 | −0.0006 | −0.0006 | −0.023 |
| qb_vs_pass_defense_success | 4 | −0.0004 | −0.0004 | −0.020 |

The centered and raw interaction forms agree to four decimals. Every interaction point estimate is
within ±0.0016 of zero; the +0.01 economic floor is never approached. `M4c` fit quality (Pearson
`r` against the realised target) is 0.27–0.49 — driven entirely by the `A_c` main effect, identical
to `M3`.

**Matchup-relative feature (§10 sensitivity).** Replacing `A + B` with the single difference
feature `A − B` is *worse* by 2–3% RMSE in every cell (`M_rel` column above). Forcing the unit and
opponent coefficients to be equal and opposite — the implicit assumption behind "offense rank minus
defense rank" matchup framing — discards information. The data prefer keeping `A` and dropping `B`,
not differencing them.

---

## 12. Uncertainty

Full table: [`outputs/phase5/phase5_interaction_uncertainty.csv`](../outputs/phase5/phase5_interaction_uncertainty.csv).

| Matchup | H | `interaction_skill` | 95% CI | one-sided p (`skill ≤ 0`) |
|---|---|---|---|---|
| pass_game_epa | 2 | −0.0012 | [−0.0032, −0.0002] | 0.986 |
| pass_game_epa | 4 | −0.0003 | [−0.0012, +0.0006] | 0.735 |
| pass_game_success | 2 | −0.0004 | [−0.0012, +0.0002] | 0.917 |
| pass_game_success | 4 | −0.0007 | [−0.0022, +0.0006] | 0.869 |
| rush_game_success | 2 | +0.0004 | [−0.0014, +0.0020] | 0.291 |
| rush_game_success | 4 | +0.0006 | [−0.0018, +0.0028] | 0.304 |
| overall_epa | 2 | −0.0016 | [−0.0037, −0.0005] | 1.000 |
| overall_epa | 4 | −0.0006 | [−0.0022, +0.0009] | 0.746 |
| overall_success | 2 | −0.0005 | [−0.0016, +0.0007] | 0.786 |
| overall_success | 4 | −0.0005 | [−0.0036, +0.0028] | 0.604 |
| early_down_epa | 2 | −0.0004 | [−0.0011, +0.0003] | 0.882 |
| early_down_epa | 4 | −0.0004 | [−0.0009, −0.0001] | 0.992 |
| protection_vs_rush_hit | 2 | +0.0004 | [−0.0005, +0.0013] | 0.211 |
| protection_vs_rush_hit | 4 | −0.0006 | [−0.0019, +0.0008] | 0.855 |
| qb_vs_pass_defense_epa | 2 | +0.0000 | [−0.0005, +0.0006] | 0.449 |
| qb_vs_pass_defense_epa | 4 | −0.0003 | [−0.0012, +0.0006] | 0.725 |
| qb_vs_pass_defense_success | 2 | −0.0006 | [−0.0016, +0.0003] | 0.860 |
| qb_vs_pass_defense_success | 4 | −0.0004 | [−0.0020, +0.0009] | 0.712 |

Four cells have a CI strictly below zero (the interaction *hurts* slightly, consistent with
estimating a spurious extra coefficient). No cell has a CI above zero.

---

## 13. Negative controls

Full table: [`outputs/phase5/phase5_negative_controls.csv`](../outputs/phase5/phase5_negative_controls.csv).

| Control | Method | Expectation | Result |
|---|---|---|---|
| `randomized_opposing_unit` | permute `B` across training rows (break the A↔B pairing), refit `M4`, predict the real test rows; 20 permutations | `interaction_skill` → ~0 | randomized mean −0.0009 to +0.0000 across all matchups/horizons — indistinguishable from the real `interaction_skill` (which is itself ~0) |
| `randomized_matchup_pairing` | permute `B` across all rows within season (break the true off/def pairing, preserve marginals), full walk-forward; 20 permutations | real `interaction_skill` ≫ randomized | real − randomized mean ∈ [−0.0012, +0.0016] — no separation |
| `future_row_poison` | inject a fabricated 2026 game, assert every earlier row/prediction is unchanged | byte-identical | **pass** for all matchups |

The first two controls behave exactly as expected **under the null hypothesis**: there is no real
interaction signal for the randomisation to destroy, so scrambling the pairing changes nothing.
Had the real `interaction_skill` been meaningfully positive, `randomized_matchup_pairing` would
have collapsed it; it did not, because there was nothing to collapse.

---

## 14. Multiple comparisons (Benjamini–Hochberg FDR)

Full table: [`outputs/phase5/phase5_fdr.csv`](../outputs/phase5/phase5_fdr.csv).

18 tests (9 resolved matchups × {H2, H4}), one-sided p-values from the cluster bootstrap, FDR
controlled at q = 0.10.

* Smallest p-value: **0.211** (`protection_vs_rush_hit`, H2).
* **0 of 18** tests significant before or after FDR correction.
* Median p ≈ 0.79; 13 of 18 have p ≥ 0.70.

No multiple-comparison adjustment is even relevant — nothing is significant at the raw level.

---

## 15. Stability analysis

Full table: [`outputs/phase5/phase5_stability.csv`](../outputs/phase5/phase5_stability.csv).

Per-OOS-season `interaction_skill` for each matchup/horizon:

* Fraction of the 7 seasons with positive `interaction_skill`: 0.14 – 0.86 (i.e. sign is a
  coin-flip, matchup-dependent, with no matchup consistently positive).
* Per-season range is tiny: min ≈ −0.010, max ≈ +0.008, centred on zero.
* No matchup shows a monotone trend or a run of same-sign seasons that would suggest a real but
  small effect.

The instability is exactly what a zero effect observed through noise looks like.

---

## 16. Status taxonomy assignment

Full table: [`outputs/phase5/phase5_status.csv`](../outputs/phase5/phase5_status.csv).

| Status | Count | Matchups |
|---|---|---|
| `MATCHUP_INTERACTION_ADDS_VALUE` | 0 | — |
| `MATCHUP_ADDITIVE_ONLY` | 0 | — |
| `UNIT_ONLY` | 9 | pass_game_epa, pass_game_success, rush_game_success, overall_epa, overall_success, early_down_epa, protection_vs_rush_hit, qb_vs_pass_defense_epa, qb_vs_pass_defense_success |
| `NO_INCREMENTAL_MATCHUP_VALUE` | 0 | — |
| `INSUFFICIENT_DATA` | 0 | — |
| `UNVALIDATED` | 4 | rush_game_epa, explosive_pass, explosive_rush, protection_vs_rush_sack (dropped at candidate selection — never tested) |

`UNIT_ONLY` decision rule (both primary horizons must hold): `skill(M1 vs league)` CI lower bound
> 0 at H2 **and** H4, and neither `M3` (additive) nor `M4` (interaction) clears its economic floor
with a CI lower bound > 0. All 9 resolved matchups meet this cleanly.

---

## 17. Interpretation

**Observed result.** For nine unit-vs-unit matchups, over 2019–2025 out-of-sample seasons, adding
the opposing unit's shrunk season-to-date measurement to a model of a unit's own future
EPA/success-rate aggregate — either additively or as a centred bilinear interaction — produced no
reliable reduction in RMSE relative to using the unit's own shrunk measurement alone. The unit's
own measurement did carry signal (3–13% RMSE reduction vs the league mean).

**Football interpretation (not a validated claim).** Over a 2–4 game forward window, a team's own
recent offensive efficiency is a far stronger guide to its near-future offensive efficiency than
the quality of the *specific* defenses on its upcoming schedule — at least at the resolution of
season-to-date team aggregates. Defensive quality varies less across the league than offensive
quality (the `M2`-alone skill is uniformly ~1%), schedules over 2–4 games are not lopsided enough
for opponent identity to dominate, and any true "good offense exploits bad defense more than
expected" effect is too small to survive shrinkage + walk-forward + a 7-season sample.

**Untested hypotheses (explicitly not claims).** (a) A matchup interaction might exist at
finer resolution — specific personnel groupings, coverage schemes, or down-and-distance splits —
that this team-aggregate target cannot see. (b) The interaction might matter for *variance* or
*tail* outcomes even if not for the mean. (c) It might matter for *single-game* prediction (a
different target and phase) even though it does not for 2–4 game persistence. None of these were
tested here and none should be assumed.

No causal language is warranted anywhere in this phase.

---

## 18. Final recommendation

**`STOP_NO_RELIABLE_MATCHUP_SIGNAL`.**

There is **insufficient evidence that matchup interactions add reliable predictive value** for
future unit performance, under the pre-registered experiment. Zero of nine testable matchups
reached `MATCHUP_INTERACTION_ADDS_VALUE`; zero reached `MATCHUP_ADDITIVE_ONLY`. The interaction
term is statistically indistinguishable from zero, unstable across seasons, and not separated from
its randomised-pairing control.

Per the spec, this is a valid and useful scientific outcome, arrived at without optimising toward a
desired result. Concretely, for the next phase:

* The "matchup interaction" layer of the architecture, **as a linear `A × B` term on shrunk team
  aggregates**, is not supported by evidence and should not be carried forward as a validated
  component.
* The unit measurement → future unit performance link (`UNIT_ONLY`, replicating Phase 4) is the
  only part of this segment with out-of-sample support.
* Any future attempt at matchup value should change the target (situational / play-level), the
  resolution (personnel / scheme), or the estimand (variance / tails) — and be pre-registered
  afresh — rather than re-run this same design hoping for a different number.

Phase 5 ends here. No ratings, composites, expected scores, game predictions, or dashboards have
been built. Phase 6 is **not** started.

---

### Reproducibility

```bash
make phase5-validation      # ~1 min; writes outputs/phase5/*.csv + phase5_summary.json
make test                   # 131 tests (17 new for Phase 5), ruff clean
```

* Pre-registration: [`config/phase5_validation.yaml`](../config/phase5_validation.yaml) (frozen)
* Code: [`src/matchup/validation/phase5.py`](../src/matchup/validation/phase5.py)
* Tests: `tests/unit/test_phase5.py` (10), `tests/leakage/test_phase5_harness.py` (7)
* Bootstrap: multiplier cluster (Exponential(1) weights per `entity_id × season`), 1000 iterations,
  seed 20260908 — deterministic.
