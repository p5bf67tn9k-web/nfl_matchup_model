# Phase 2 Report — Descriptive Metrics & Normalization

**Project:** `nfl_matchup_model`
**Run date:** 2026-09-08
**Environment:** Python 3.12.14, `nflreadpy` 0.1.5, `polars` 1.44.1
**Scope:** measurement only. **No** ratings, weights, opponent adjustment, matchup logic,
expected performance, expected score, model fitting, or feature selection. Nothing here claims
any metric is predictive.

---

## 0. TL;DR

* **84 tests pass** (50 from Phases 0/1 unchanged + 34 new). Ruff clean.
* **58 metrics implemented** across 8 pbp families + NGS/PFR join-throughs, every one
  `predictive_status: UNVALIDATED`. 8 metrics explicitly **deferred/rejected** with reasons.
* Every metric has an **exact definition** (numerator / denominator / eligible plays / exclusions /
  sacks-scrambles-spikes-kneels treatment) in `config/metrics.yaml` and `src/matchup/metrics/plays.py`,
  and at least one **hand-verified test** against the underlying play data (Mahomes Week 1 2024:
  20/28, 291 yds, 1 TD, **1 INT**, 2 sacks — matches the metric exactly).
* **Windowing** is on the entity's game sequence, never week arithmetic; the bye-spanning
  trailing-3 test passes.
* **Normalization** uses the 3 most recently *completed* seasons as of the prediction date — matches
  the spec's worked examples exactly (Wk1 2016 → 2013–15; Wk5 2022 → 2019–21; Wk1 2026 → 2023–25).
  No shrinkage `k`, no weights, no optimized combinations fitted.
* **`outputs/phase2/`**: `metric_registry.csv`, `metric_coverage.csv`, `metric_reliability.csv`
  (144 rows; 48 flagged `is_retrospective`), `metric_redundancy.csv` (41 pairs).
* **Poisoned-future-row canary extended** to every metric layer (raw game metric → windowed →
  normalized) — all leave earlier results byte-identical.
* **New data issue found & fixed:** `special_teams_play == 1` silently **excludes field goals and
  extra points** (6,382 of 7,548 ST plays). The correct ST-universe flag is `special == 1`.
* **No leakage problems** discovered in the metric layer.

---

## 1. What was built

```
src/matchup/metrics/
  plays.py        classify_plays(pbp) -> 10 documented boolean flags + carried numerics
  families.py     8 per-(entity, game) aggregation functions + FAMILY_SPECS (components + rate specs)
  windows.py      window_metric(...) over the game sequence; entity_season_aggregate(...)
  build.py        game_metrics_from_asof (production) / game_metrics_offline (reference & retro only)
  external.py     NGS + PFR player-week join-throughs (leak-safe, tagged)
  registry.py     config/metrics.yaml loader + coverage_table()
  _thresholds.py  explosive thresholds + min-sample constants (from config)
src/matchup/normalize/
  reference.py    completed_seasons_asof(date, n=3); season_is_completed(...)
  transforms.py   zscore / percentile_rank / league_relative (pure)
  normalize.py    build_reference_distribution / normalize_windowed (logs ref seasons; asserts completed)
src/matchup/diagnostics/
  reliability.py  odd/even + first/second-half + (retrospective) std-vs-rest
  redundancy.py   within-taxonomy pairwise correlation
config/metrics.yaml   full taxonomy, exact formulas, thresholds, window & normalization rules
```

### Play universe (verified against 2024 pbp, all games incl. postseason)

| flag | rule | note |
|---|---|---|
| `off_play` | `(pass==1 OR rush==1) AND two_point_attempt==0` | team EPA/play denominator; 0 null EPA |
| `is_dropback` | `qb_dropback==1 AND 2pt==0` | throws + sacks + scrambles; 0 null EPA |
| `is_pass_throw` | `(complete_pass OR incomplete_pass OR interception) AND 2pt==0 AND qb_spike==0` | actual forward-pass attempts (throwaways = incomplete) |
| `is_sack` / `is_scramble` | `sack==1` / `qb_scramble==1`, `2pt==0` | `pass==1` includes scrambles; `rush==1` does **not** |
| `is_designed_rush` | `rush==1 AND qb_kneel==0 AND 2pt==0` | excludes QB scrambles & kneels |
| `is_early_down` | `down IN (1, 2)` | |
| `is_explosive_pass` | `is_pass_throw AND complete AND yards_gained >= 20` | threshold = **config choice** |
| `is_explosive_rush` | `is_designed_rush AND yards_gained >= 10` | threshold = **config choice** |
| `has_cpoe` | `is_pass_throw AND cpoe not null` | ~93–95% of throws; CPOE metrics use this denominator (decision DE) |

**Excluded from every offensive rate metric:** kneel-downs, spikes, two-point conversions, plays with
null EPA.

---

## 2. Full test count & results

```
$ .venv/bin/python -m pytest -q
84 passed
```

| Suite | Tests | Purpose |
|---|---|---|
| `tests/leakage/test_asof_assumptions.py` | 11 | Phase 0 nflverse data assumptions (unchanged) |
| `tests/leakage/test_pointintime_engine.py` | 17 | Phase 1 point-in-time engine (unchanged) |
| `tests/unit/test_calendar_and_rules.py` | 19 | Phase 1 calendar / injury rule (unchanged) |
| `tests/reproducibility/test_ingest_deterministic.py` | 3 | Phase 1 byte-identical ingest (unchanged) |
| **`tests/unit/test_metrics_definitions.py`** | **8** | hand-verified metric definitions vs play data |
| **`tests/unit/test_windows.py`** | **7** | window boundaries: bye, season, playoff, provenance |
| **`tests/unit/test_normalization.py`** | **8** | reference window matches spec; transforms; never current/future season |
| **`tests/leakage/test_metrics_leakage.py`** | **11** | poisoned-row canary at every metric layer; `data_asof<kickoff`; NGS wk0; `earliest_valid_season`; CPOE denominator |

**All Phase 0/1 tests remain green (criterion 1).**

### Leakage test results (criterion 3)

| Test | Result |
|---|---|
| every game-metric row `data_asof < target_kickoff` (8 families) | **PASS** — 0 offending rows |
| windowed + normalized rows `data_asof < kickoff`, `max(ref_seasons) < target_season` | **PASS** |
| NGS `week==0` excluded from metrics; NGS rows `data_asof < kickoff` | **PASS** |
| `earliest_valid_season` surfaced on windowed rows (pbp→1999, NGS→2016) | **PASS** |
| CPOE denominator = attempts-with-CPOE, not all throws; `cpoe = cpoe_sum/cpoe_n` | **PASS** |
| **poisoned-future-row canary** (fabricated future game + future-dated plays) leaves every raw / windowed / normalized metric byte-identical | **PASS** |

---

## 3. Metric coverage table (`outputs/phase2/metric_coverage.csv`)

Entity-seasons and typical opportunity volume, 2016–2024, pbp families
(offline aggregate; not the min-sample-filtered reference set):

| family | entity-seasons | median opportunities | null-frac range |
|---|---|---|---|
| qb | 990 | 42 dropbacks (all entity-seasons, incl. backups) | 0.00–0.06 (CPOE highest: throws w/o cpoe) |
| rb | 3,011 | 7 carries (long tail of low-volume backs) | 0.00 |
| wr | 4,569 | 21 targets (long tail) | 0.00–0.04 (`yards_per_reception`: 0-reception games) |
| team_offense / team_defense | 288 (32 teams × 9 seasons) | ~1,107 plays | 0.00 |
| pass_protection / pass_rush | 288 | ~645 dropbacks | 0.00 |
| special_teams | 288 | ~231 ST plays | 0.00 |

`earliest_valid_season`: pbp families 1999 (EPA-quality 2006+), NGS 2016, PFR join-throughs 2018.
NGS families are missing-not-at-random below the NGS attempt threshold (documented, not imputed).

---

## 4. Reliability report (`outputs/phase2/metric_reliability.csv`)

**Descriptive stability only. This does NOT establish predictive value.** 144 rows: for each
(family, metric) — `odd_even`, `first_second_half`, and `std_vs_rest_of_season`
(the last flagged `is_retrospective=True`, isolated from all production paths).

### Odd/even split-half, Spearman-Brown adjusted (2016–2024)

| bucket | metrics (SB-adjusted pearson) |
|---|---|
| **high (≥0.70)** | `wr.adot` 0.92 · `team_offense.proe` 0.87 · `pass_protection.qb_hit_rate_allowed` 0.77 · `team_offense.epa_per_play` 0.77 · `team_offense.success_rate` 0.77 · `team_offense.pass_success_rate` 0.73 · `qb.cpoe_coverage_fraction` 0.73 |
| **moderate (0.55–0.70)** | `team_offense.early_down_epa_per_play` 0.71 · `team_offense.pass_epa_per_dropback` 0.71 · `wr.yards_per_reception` 0.66 · `qb.adot` 0.65 · `qb.epa_per_dropback` 0.64 · `pass_protection.sack_rate_allowed` 0.64 · `qb.dropback_success_rate` 0.62 · `qb.sack_rate` 0.59 · `qb.yards_per_attempt` 0.57 · `rb.yards_per_carry` 0.57 · `rb.rush_success_rate` 0.57 · `team_defense.success_rate` 0.55 |
| **low (0.35–0.55)** | most `team_defense` metrics (`epa_per_play` 0.49, `pass_epa_per_dropback` 0.46, `early_down` 0.45) · `qb.completion_pct` 0.47 · `qb.cpoe` 0.46 · `team_*.explosive_*` 0.34–0.53 · `rb.rush_epa_per_att` 0.38 · `wr.catch_rate` 0.53 |
| **noise (<0.35)** | `qb.interception_rate` 0.18 · `special_teams.fg_pct` 0.14 · `pass_rush.sack_rate_generated` 0.24 · `pass_rush.qb_hit_rate_generated` 0.34 · `wr.epa_per_target` 0.26 · `wr.target_success_rate` 0.28 |

**Descriptive observations (not predictive claims):**
- Team **offense** efficiency metrics are markedly more self-consistent than team **defense** ones
  (offense `epa_per_play` SB 0.77 vs defense 0.49). Consistent with the analytics literature.
- **Pass rush pressure generation** (`sack_rate_generated`, `qb_hit_rate_generated`) is among the
  noisiest team metrics; **pressure allowed** (`qb_hit_rate_allowed`) is one of the most stable.
- `proe` and `wr.adot` are near-traits (usage/scheme), not quality — very high stability.
- Explosive-play rates, INT rate, fumble rate, FG% are low-signal at the season level.

---

## 5. Redundancy report (`outputs/phase2/metric_redundancy.csv`)

**Descriptive overlap only. Metrics are NOT selected, combined, or dropped on this basis** — that
decision requires out-of-sample prediction and belongs to Phase 3+.

Within-taxonomy Pearson, entity-seasons 2016–2024 (min 8 games):

| pair | r |
|---|---|
| `team_offense.epa_per_play` ↔ `pass_epa_per_dropback` | **0.96** |
| `team_defense.epa_per_play` ↔ `pass_epa_per_dropback` | 0.94 |
| `team_offense.epa_per_play` ↔ `early_down_epa_per_play` | 0.93 |
| `team_offense.epa_per_play` ↔ `success_rate` | 0.90 |
| `qb.epa_per_dropback` ↔ `dropback_success_rate` | 0.88 |
| `qb.completion_pct` ↔ `qb.cpoe` | 0.82 |
| `qb.epa_per_dropback` ↔ `yards_per_attempt` | 0.81 |
| `wr.epa_per_target` ↔ `yards_per_target` | 0.80 |

The team EPA family is largely one dimension dominated by the passing game; QB EPA / success /
YPA move together; CPOE adds only partial information beyond raw completion %.

---

## 6. Every metric implemented (58)

**QB (14, source pbp unless noted):** `epa_per_dropback`, `dropback_success_rate`, `cpoe`,
`cpoe_coverage_fraction`, `sack_rate`, `yards_per_attempt`, `completion_pct`, `adot`,
`interception_rate`, `explosive_pass_rate`, `ngs_avg_time_to_throw` (ngs), `ngs_aggressiveness`
(ngs), `ngs_cpoe` (ngs), `pfr_pass.pressure_rate_faced` (pfr, 2018+).

**RB (6):** `rush_epa_per_att`, `rush_success_rate`, `yards_per_carry`, `explosive_rush_rate`,
`fumble_lost_rate`, `ngs_ryoe_per_att` (ngs, 2018+).

**WR/TE (12):** `targets`, `catch_rate`, `yards_per_target`, `epa_per_target`, `target_success_rate`,
`adot`, `explosive_rec_rate`, `target_share` (player_stats), `air_yards_share` (player_stats),
`wopr` (player_stats), `ngs_avg_separation` (ngs), `ngs_yac_above_expectation` (ngs).

**Team offense (9):** `epa_per_play`, `success_rate`, `pass_epa_per_dropback`, `rush_epa_per_play`,
`early_down_epa_per_play`, `proe`, `explosive_pass_rate`, `explosive_rush_rate`, `plays`.

**Team defense (7):** `epa_per_play`, `success_rate`, `pass_epa_per_dropback`, `rush_epa_per_play`,
`early_down_epa_per_play`, `explosive_pass_rate`, `explosive_rush_rate` (all "allowed" framing).

**Pass protection (3, team-derived, decision #7):** `sack_rate_allowed`, `qb_hit_rate_allowed`,
`rush_stuffed_rate_approx` (documented approximation).

**Pass rush (3):** `sack_rate_generated`, `qb_hit_rate_generated`, `pfr_pressure_rate` (pfr, 2018+).

**DL/DB (PFR join-through, 2018+) (2):** `pfr_def.missed_tackle_pct`, `pfr_def.yards_allowed_per_target`.

**Special teams (2):** `fg_pct` (not distance-adjusted), `st_epa_per_play`.

All have `direction`, `taxonomy`, `earliest_valid_season`, `proposed_role`
(`descriptive` / `availability_adjustment` / `candidate_signal`), and `predictive_status: UNVALIDATED`.
`candidate_signal` means "worth testing in Phase 3", **not** a claim of signal.

---

## 7. Metrics rejected / deferred (8, documented in `config/metrics.yaml` → `deferred_metrics`)

| deferred | reason |
|---|---|
| yards per route run / targets per route run | needs `participation.route` — POST_SEASON_ONLY / sparse pre-2023 |
| man/zone & coverage-scheme rates (for & against) | `participation.defense_coverage_type` not live-safe / 0% pre-2018 |
| OL run-block: yards before contact, blown blocks | no free source (only the approximate stuffed-rate is implemented) |
| individual OL / LB / DB ratings | decision #7 — team-derived only |
| QB EPA when pressured vs clean | needs FTN (2022+) or participation; small samples |
| red-zone / third-down / third-and-long efficiency | small-sample situational splits; deferred until they earn inclusion |
| distance-adjusted FG / kicker leg | deferred to the score layer (Phase 6+) |
| ESPN Total QBR | no `load_espn_qbr` in `nflreadpy` 0.1.5 (Phase 0) |

---

## 8. Newly discovered data / leakage problems

1. **`special_teams_play == 1` excludes field goals and extra points** (6,382 vs 7,548 ST plays).
   The correct ST-universe flag is `special == 1` (kickoff + punt + field_goal + extra_point,
   0 null EPA). **Fixed** in `special_teams_game_metrics`; covered by
   `test_special_teams_fg_from_special_flag`.
2. **`qb_dropback` (21,140) ≠ `pass_attempt` (20,082) + `sack` (1,392).** nflfastR's `pass_attempt`
   already includes sacks and spikes; the clean throw denominator is
   `complete | incomplete | interception`. Documented in `plays.py` and every affected metric.
3. **CPOE coverage is ~93–95% on actual throws** (season level) — better than the Phase 0
   "15–21% null on `pass==1`" figure, which was over the broader universe that includes
   sacks/scrambles. Companion fields `cpoe_attempt_count` / `cpoe_coverage_fraction` carry it.
4. **`pass` includes scrambles, `rush` does not** — a deliberate nflfastR choice we adopt
   (scrambles are pass-game plays). Verified; documented.
5. **No leakage problems** in the metric layer: the poisoned-future-row canary passes at every
   layer, and the offline reference provider is guarded by a `season_is_completed` assertion
   inside `normalize_windowed`.

---

## 9. Known limitations

1. **Normalization reference = full-season entity distributions**, but the value being normalized is
   a shorter window (e.g. trailing-3). Variance differs; the z-score is therefore approximate for
   short windows. Documented; the reference method is the production choice (matches decision DG's
   worked examples). An alternative (window-matched reference) is a Phase 3 option.
2. **`game_metrics_offline` reads raw pbp (no as-of filtering).** It is only ever called with
   completed prior seasons (for reference distributions) or clearly-labelled retrospective
   diagnostics; `normalize_windowed` re-asserts each reference season is completed. It must never
   be wired into a production feature path.
3. **Player game sequence = games with ≥1 eligible opportunity.** A QB who was active but did not
   drop back (rare) is absent from that window; a traded player's sequence correctly follows the
   player, not a team.
4. **`rush_stuffed_rate_approx` is an approximation**, not a real run-blocking measure (no
   yards-before-contact / blown-block data for free). Labelled everywhere.
5. **PFR join-throughs (2018+) and NGS (2016+) are not yet windowed** — Phase 2 surfaces them at
   the player-week grain with provenance; window aggregation of external metrics is Phase 3.
6. **`std_vs_rest_of_season` reliability is retrospective** and flagged as such; it is computed for
   information only and is not importable into any production path.
7. **`team_stats` source is unused** so far — team metrics are computed from pbp for auditability;
   `team_stats` remains available as a cross-check.

---

## 10. Phase 2 acceptance criteria — status

| # | Criterion | Status |
|---|---|---|
| 1 | All 50 Phase 0/1 tests remain green | ✅ |
| 2 | Every metric: exact definition, source, provenance, earliest_valid_season, PIT handling, ≥1 hand-verified test | ✅ `config/metrics.yaml` + `plays.py` + `test_metrics_definitions.py` |
| 3 | Every production metric passes the Phase 2 poisoned-future-row test | ✅ |
| 4 | Every rolling metric uses game sequence, not week arithmetic | ✅ `windows.py`; bye-spanning test passes |
| 5 | Normalization never references current-incomplete or future seasons | ✅ tested |
| 6 | Normalization reference seasons logged | ✅ `ref_seasons`, `ref_n`, `ref_mean`, `ref_sd`, `ref_min_opportunities` on every normalized row |
| 7 | `outputs/phase2/metric_reliability.csv` exists | ✅ 144 rows |
| 8 | Metric redundancy/correlation report exists | ✅ `metric_redundancy.csv`, 41 pairs |
| 9 | `config/metrics.yaml` populated | ✅ 58 metrics + taxonomy + thresholds + rules |
| 10 | Every metric `predictive_status = UNVALIDATED` | ✅ verified in `registered_metrics()` |
| 11 | No predictive model fitting | ✅ none exists |
| 12 | No player/unit ratings | ✅ none exist |
| 13 | No matchup logic | ✅ none exists |
| 14 | No expected-performance / score logic | ✅ none exists |
| 15 | No sportsbook data in the metric pipeline | ✅ globally stripped upstream (Phase 1); no line/score column reachable |
| 16 | Retrospective diagnostics isolated from production | ✅ `is_retrospective` flag; separate function; never imported by `metrics/` or `normalize/` |
| 17 | Final report documents all required items | ✅ this document |

---

## 11. Proposed Phase 3 — predictive-validation architecture

**This is where predictive value is decided, for the first time, and only out-of-sample.**

### 11.1 Objective
Build the **chronological walk-forward harness** and use it to answer, per metric and per window:
*does this descriptive measurement, computed strictly as-of, predict the corresponding actual
future football outcome better than a naive baseline?* No ratings yet — this validates the
**measurements** as candidate inputs.

### 11.2 Design
- **Walk-forward loop:** for season S in 2019→latest, for week W in 5→last: build the as-of view at
  each game's kickoff, compute every windowed+normalized metric, then observe the actual outcome of
  that game (and the next N games) for the same entity. Never shuffle. Weeks 1–4 held out (burn-in).
- **Targets** (the thing each metric is tested against — the *actual*, as-of-unknown value):
  * QB metric → that QB's actual EPA/dropback (and CPOE, sack rate) in the target game / next 4 games
  * team-unit metric → that unit's actual EPA/play etc. in the target game
  * pass-protection metric → actual sack rate allowed in the target game
- **Baselines each metric must beat** (skill score `1 − RMSE/RMSE_baseline`, and rank correlation):
  1. league mean for that season-to-date
  2. the entity's own prior-season value
  3. the entity's raw trailing-3-game value (un-normalized) — *does the windowing/normalization add anything?*
- **Per-metric outputs:** OOS RMSE, MAE, Spearman(rating_t, outcome_{t+1..t+4}), calibration slope,
  skill vs each baseline, by window and by season-phase (early / mid / late).
- **Ablations:** normalized vs raw; each window vs the others; NGS/PFR-augmented vs pbp-only
  (2018+ subset).
- **Leakage tests extended:** the walk-forward harness gets its own poisoned-row canary and a
  "no target leaks into features" assertion (`feature.data_asof < target.kickoff` for every row).

### 11.3 Deliverables
- `src/matchup/validation/` — walk-forward harness, baselines, scoring.
- `outputs/phase3/metric_predictive_value.csv` — per (metric, window, target horizon): skill vs
  each baseline, correlation, calibration, n.
- `reports/phase3_report.md` — which measurements carry out-of-sample signal, which don't, and
  which are dominated by a simpler baseline. **`config/metrics.yaml` `predictive_status` updated**
  from `UNVALIDATED` to `VALIDATED_SIGNAL` / `NO_INCREMENTAL_SIGNAL` / `INSUFFICIENT_DATA` per
  metric, with the evidence.

### 11.4 Still NOT in Phase 3
Player ratings, unit ratings, metric weights, composite scores, opponent adjustment, matchup
interactions, expected performance, expected score, betting comparison. Phase 3 validates inputs;
it does not build the model.

---

## 12. STOP

Phase 2 is complete; all 17 acceptance criteria are met. **Awaiting explicit approval of the
Phase 3 architecture in §11 before building `src/matchup/validation/` or touching any
`predictive_status` value.**
