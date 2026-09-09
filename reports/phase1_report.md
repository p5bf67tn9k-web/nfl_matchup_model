# Phase 1 Report — Canonical Data Layer & Point-in-Time Engine

**Project:** `nfl_matchup_model`
**Run date:** 2026-09-08
**Environment:** Python 3.12.14, `nflreadpy` 0.1.5, `polars` 1.44.1, local Parquet + filesystem cache
**Scope:** infrastructure only. **No** player ratings, unit ratings, opponent adjustment, matchup
calculations, expected performance, or score logic was built. Normalization/shrinkage config is
scaffolded (empty).

---

## 0. TL;DR

* The canonical Parquet layer, the point-in-time engine, the ID crosswalk, the injury as-of
  fallback + its validation, the data dictionary, and the full leakage/reproducibility test suite
  are built and green. **50 tests pass.**
* **Injury fallback acceptance: PASS.** False-inclusion rate **0.0057%** (1 row in 17,479 across
  2022–2024) vs the 0.5% threshold. The conservative rule's real cost — *cutoff staleness* — is
  **0.72%** of injury rows and is reported transparently, not hidden.
* **ID crosswalk: PASS, no fallback matcher needed.** Zero unit-seasons exceed the 3% unmatched
  threshold; the worst is TE 2024 at **0.45%**, pooled TE **0.11%**. The Phase 0 "~9% pfr_id gap"
  was a property of the full historical player table, **not** the snap-playing population.
* **New leakage vector found and closed:** `nflfastR` play-by-play denormalizes the **final score,
  `result`, `total`, and the betting lines (`spread_line`, `total_line`, `vegas_wp*`)** onto every
  play row. These are now globally stripped by the as-of engine.
* **2026 live season:** confirmed unpublished for every in-season source; ingest degrades cleanly to
  `unavailable` manifests, and `team_state_asof(..., mode="live")` returns priors-only frames
  tagged `priors_only=True, low_confidence=True` with full coverage metadata.

---

## 1. What was built

### 1.1 Canonical data layer — `data/processed/`

`src/matchup/ingest/` + `src/matchup/store.py`. One wrapper per source; season-partitioned Parquet
(`<source>/season=YYYY/data.parquet`) with a `_manifest.json` sidecar per partition and a
top-level `_ingest_manifest.json`.

| Source | Point-in-time status | Partitions materialised | Rows |
|---|---|---|---|
| `pbp` | LIVE_SAFE | 2013–2025 (2026 unavailable) | 628,163 |
| `player_stats` (week) | LIVE_SAFE | 2013–2025 | 234,738 |
| `team_stats` (week) | LIVE_SAFE | 2013–2025 | 7,124 |
| `snap_counts` | LIVE_SAFE | 2013–2025 | 324,611 |
| `ngs_passing` / `ngs_receiving` / `ngs_rushing` | LIVE_SAFE | 2016–2025 | 5,933 / 14,731 / 6,059 |
| `pfr_pass` / `pfr_rush` / `pfr_rec` / `pfr_def` | LIVE_SAFE | 2018–2025 | 5,424 / 18,461 / 35,724 / 62,345 |
| `injuries` | LIVE_SAFE (`date_modified` / fallback) | 2013–2025 | 70,936 |
| `rosters_weekly` | LIVE_SAFE | 2013–2025 | 562,246 |
| `schedules` | REFERENCE_ONLY (fixture cols only in calendar) | 1999–2026 | 7,548 |
| `participation` | **POST_SEASON_ONLY** — ingested, blocked from feature frames | 2016–2025 | 478,989 |
| `players` | REFERENCE_ONLY (identity dimension) | single file | 24,826 |

Total ≈ 205 MB. `depth_charts` and `ftn_charting` are **not** ingested (decisions DA / #11).
Seasonal sources start at 2013 to give a 2016 walk-forward prediction three completed prior
seasons for normalization (decision DG).

Each `_manifest.json` records: `row_count`, `column_count`, `content_sha256`, `status`
(`ok`/`unavailable`), `unavailable_reason`, `source_data_min_date`/`max_date`,
`point_in_time_status`, `publish_lag_days`, `publish_lag_type`, `nflreadpy_version`,
`polars_version`, `ingested_at`. Only `ingested_at` varies between runs (see §8).

### 1.2 Point-in-time engine — `src/matchup/pointintime/`

* **`calendar.py`** — `build_game_calendar()`: one row per game, **fixture columns only**
  (no scores, no lines), with a timezone-aware `kickoff_utc` built from `gameday` + `gametime`
  (US Eastern, verified in Phase 0) → UTC. `kickoff_time_estimated` flags the 259 historical games
  with a null/unparseable `gametime` (a conservative 13:00 ET is substituted). `2026` fixtures are
  present (272 games, 0 estimated).
  `build_team_game_sequence()`: one row per (team, game), chronologically ordered, with
  `team_game_index` (overall, stable — computed on the full calendar) and
  `team_game_index_season` (contiguous across byes and the regular/postseason boundary).
* **`publish_lag.py` / `availability.py`** — `config/publish_lag.yaml` is the single source of
  truth. A stat row for game G is knowable at `kickoff_utc(G) + assumed_game_duration (4h) +
  publish_lag_days`. Game-grained sources join on `game_id`; week-grained sources join on
  (season, week, team) → the team's game.
* **`status.py`** — enforces the point-in-time contract: `assert_admissible(source, mode)` blocks
  POST_SEASON_ONLY / REFERENCE_ONLY / UNKNOWN from any feature frame; `mode="live"` additionally
  blocks HISTORICAL_SAFE.
* **`asof.py`** — `AsOf(asof_utc, mode)` — the **only** sanctioned way to read source data
  downstream. Every accessor: refuses non-admissible sources, strips REFERENCE_ONLY + globally
  banned columns, drops NGS `week==0` season aggregates, filters to `data_asof < asof_utc`, and
  stamps every row with `data_asof`, `pit_source`, `pit_status`.
  `team_state_asof(team, season, week)` returns the full leak-checked bundle plus a `coverage`
  block (`priors_only`, `low_confidence`, `prior_seasons_supplying_data`,
  `sources_with/without_target_season_data`, `history_window`).

### 1.3 ID crosswalk — `src/matchup/ids/crosswalk.py`

`gsis_id ↔ pfr_id` from `load_players`; `resolve_gsis_from_pfr()` never drops unmatched inputs
(null `gsis_id` returned); `crosswalk_coverage_report()` → `outputs/phase1/id_crosswalk_coverage.csv`.

### 1.4 Injury as-of handling — `src/matchup/injuries/`

* **`asof_rule.py`** — `injury_asof_cutoff()` (scalar + polars expr) and
  `resolve_availability_status()` (documented precedence for the
  report_status / practice_status / roster_status triple; **null `report_status` ⇒ UNKNOWN,
  never healthy**).
* **`validation.py`** — `run_validation()` → `outputs/phase1/injury_asof_validation.{csv,json}`.

### 1.5 Generated docs & CLI

* `reports/data_dictionary.md` — generated from config + manifests (`matchup data-dictionary`).
* Attribution / licensing block (nflverse CC-BY-SA, PFR, NGS, FTN) in the data dictionary and README.
* `src/matchup/cli.py` — `ingest`, `calendar`, `crosswalk`, `validate-injuries`, `team-state`,
  `data-dictionary`. `Makefile` wraps them (`make phase1`).

---

## 2. What was tested — 50 tests, all green

`.venv/bin/python -m pytest -q` → **50 passed**.

### 2.1 Phase 0 characterization tests (`tests/leakage/test_asof_assumptions.py`) — 11, all still green

Unchanged from Phase 0; pin the nflverse data assumptions.

### 2.2 Point-in-time engine leakage suite (`tests/leakage/test_pointintime_engine.py`) — 17

| Test | Result |
|---|---|
| `test_no_row_is_dated_at_or_after_target_kickoff` (KC·2024·7, PHI·2023·1, SF·2022·20, BUF·2021·5, DET·2024·14) | **PASS** — 0 rows with `data_asof ≥ kickoff` in any accessor for any sample game |
| `test_every_stat_frame_carries_provenance` (×5) | **PASS** — every stat frame carries `data_asof`, `pit_source`, `pit_status == LIVE_SAFE` |
| `test_current_season_slice_stops_before_the_bye_and_target` | **PASS** — KC 2024 in-season data = weeks 1–5 only (wk 6 bye, wk 7 target excluded); the **week-7 injury report is included** (knowable pre-kickoff) |
| `test_bye_week_rolling_uses_game_sequence_not_week_arithmetic` | **PASS** — season game index contiguous across the wk-6 bye; "last 3 games" before wk 7 = weeks 3,4,5 |
| `test_playoff_games_sort_after_regular_season` | **PASS** — postseason `kickoff_utc` > all regular-season; a divisional-round view sees all 17 regular-season games |
| `test_ngs_week_zero_never_returned` | **PASS** |
| `test_reference_only_and_market_columns_never_reach_a_feature_frame` | **PASS** — `home_score`, `away_score`, `result`, `total`, `spread_line`, `total_line`, `vegas_wp*` absent from every accessor frame and the calendar |
| `test_point_in_time_status_enforcement` | **PASS** — `participation`, `players`, `schedules` raise `PointInTimeViolation` in both backtest and live mode |
| `test_poisoned_future_row_canary` | **PASS** — injecting a fabricated future game + future-dated plays leaves every as-of frame for an earlier game byte-for-byte identical (row-hash compared) |

### 2.3 Unit tests (`tests/unit/test_calendar_and_rules.py`) — 19

Kickoff ET→UTC (EDT and EST), null-gametime fallback; injury cutoff hand cases (Sunday → preceding
Saturday 23:59 ET; Monday → that week's Saturday; Thu/Fri/Sat → kickoff−24h; Wednesday 2026 opener
→ preceding Saturday; always strictly pre-kickoff); publish-lag arithmetic; availability-status
resolution precedence incl. dirty whitespace and "null ≠ healthy". **All PASS.**

### 2.4 Reproducibility (`tests/reproducibility/test_ingest_deterministic.py`) — 3

Re-ingesting `ngs_passing`, `pfr_pass`, `team_stats` produces **byte-identical** Parquet
(`content_sha256` unchanged) and a manifest differing only in `ingested_at`. Also verified
**cross-process** by hand: `shasum` identical before/after a fresh `python -m matchup.cli ingest`.
**All PASS.**

---

## 3. Injury fallback validation results

`outputs/phase1/injury_asof_validation.{csv,json}` — evaluated on **17,479** injury rows (2022–2024,
with a real `date_modified` and a resolvable kickoff).

| Season | Rows | False inclusion | Cutoff staleness | False exclusion |
|---|---|---|---|---|
| 2022 | 5,665 | 0 (0.00%) | 29 (0.51%) | 0 |
| 2023 | 5,599 | 0 (0.00%) | 25 (0.45%) | 0 |
| 2024 | 6,215 | 1 (0.016%) | 71 (1.14%) | 0 |
| **All** | **17,479** | **1 (0.0057%)** | **125 (0.72%)** | **0** |

* **`false_inclusion`** (`date_modified ≥ kickoff_utc` — information that did not exist pre-game):
  **1 row → 0.0057% ≪ 0.5% threshold. ACCEPTANCE CRITERION MET.**
  The single case: BAL Week 1 2024, a player already ruled **Out**, whose report row was finalized
  ~3h after a Thursday-night kickoff. 1 affected game. Harmless in practice (status did not change).
* **`cutoff_staleness`** (`fallback_cutoff ≤ date_modified < kickoff` — a genuine pre-game update
  the frozen Saturday-23:59 cutoff would *miss*): **125 rows → 0.72%.** Not leakage — the model
  would carry a slightly stale value (typically a Sunday-morning Questionable→Out or a practice
  upgrade). This is the real, disclosed cost of the conservative rule. It is **higher in 2024
  (1.14%)** — worth watching as report-update behavior evolves.
* **`false_exclusion`**: 0 (the kickoff−1h floor guarantees the cutoff is always pre-game).

**Interpretation:** the fallback is safe to use for the 2025+ / live season where `date_modified`
is absent. It will occasionally be *stale* (~0.7% of rows), never *ahead of reality*. Injuries
remain an **AVAIL-ADJ candidate**, not a trusted predictive input, pending Phase-3+ walk-forward
validation.

---

## 4. ID crosswalk coverage

`outputs/phase1/id_crosswalk_coverage.csv`. Unmatched = `pfr_player_id` with no `gsis_id` mapping.

* **Unit-seasons exceeding the 3% threshold: 0.** No fallback matcher required (decision DD).
* Worst unit-seasons (snap-weighted): TE 2024 **0.45%**, TE 2023 0.43%, WR 2019 0.29%, WR 2025 0.28%.
* Pooled across all seasons: TE **0.11%**, WR 0.07%, OL 0.04%, DB/DL/RB ≤ 0.04%, QB/LB/EDGE/ST 0.00%.
* PFR sources (row-weighted): max **0.13%** unmatched in any season (`pfr_rush` 2025, 3 rows).

**Finding:** the Phase 0 concern about a "~9% pfr_id gap" was measuring the full `load_players`
table, which is dominated by historical / practice-squad / never-played entries. Among players who
actually take snaps, the crosswalk is **>99.5% complete**. Unmatched rows are logged, never dropped.

---

## 5. Point-in-time assumptions (as encoded in `config/publish_lag.yaml`)

| Source | `publish_lag_days` | `publish_lag_type` | Notes |
|---|---|---|---|
| `pbp` | 1 | `conservative_assumption` | no publication timestamp in the data; 1 day is a cautious floor |
| `player_stats`, `team_stats` | 1 | `conservative_assumption` | derived from pbp |
| `snap_counts` | 1 | `conservative_assumption` | PFR-sourced; per-game release time not stamped |
| `ngs_*` | 1 | `conservative_assumption` | nightly in-season per nflverse schedule, but no per-row timestamp; `week==0` = season aggregate, dropped |
| `pfr_*` | 3 | `conservative_assumption` | charting data, lands a few days post-game; 2018 floor |
| `injuries` | 0 | `empirical` (+ fallback) | `date_modified` used directly when present (2010–2024); conservative fallback rule for 2025+ |
| `rosters_weekly` | 2 | `conservative_assumption` | transaction timing not stamped per row |
| `schedules` | 0 | `known` | fixtures published months ahead; scores/lines are REFERENCE_ONLY |
| `participation` | `null` | `unknown` | POST_SEASON_ONLY |

The engine adds a fixed **4-hour assumed game duration** before applying the lag. Every value that
is not `empirical` or `known` is an explicit **conservative engineering assumption**, documented
as such, chosen to prefer false exclusion over false inclusion. None is claimed to be an exact
historical release time; where true timing cannot be reconstructed from the data we say so
(`publish_lag_type: unknown`).

Global column strip (applied to **every** source before it can enter a feature frame):
`spread_line`, `total_line`, moneylines, spread/total odds, `vegas_wp`, `vegas_home_wp`,
`vegas_wpa`, `vegas_home_wpa`, `home_score`, `away_score`, `result`, `total`, `overtime`.

---

## 6. Sources that remain unsafe / blocked

| Source | Status | Why |
|---|---|---|
| `participation` | **POST_SEASON_ONLY** | 2023+ FTN feed released only after the playoffs; 2016–2022 legacy feed is sparse (routes/pressure ~38%, coverage-type 0% in 2016–17). Ingested for future research; the as-of engine refuses it. |
| `ftn_charting` | not ingested | decision #11 (deferred); 2022+ only |
| `depth_charts` | not ingested | decision DA — schema regime break at 2025 (new ESPN by-date format, null season/week) |
| `schedules` score / line columns | **REFERENCE_ONLY** | market + results data; project rule bans them as inputs |
| `players.status` | current-state only | not a historical field; crosswalk use only |
| ESPN Total QBR | unavailable | no `load_espn_qbr` in `nflreadpy` 0.1.5 (Phase 0 finding) |

---

## 7. Unresolved limitations

1. **Publish lags are conservative guesses, not measurements.** For the seven stat sources without
   a per-row publication timestamp, availability timing is an assumption. It is safe (biased toward
   exclusion) but means a Thursday-game prediction may withhold prior-week PFR/NGS data that was in
   fact available. Quantifying true lags would need scraping nflverse release timestamps — out of
   scope, flagged.
2. **Injury cutoff staleness ~0.72%** (rising to 1.14% in 2024). The live fallback will carry stale
   injury values for a small fraction of players. Acceptable for an AVAIL-ADJ input; revisit if
   injuries are ever promoted to a stronger role.
3. **Week-grained sources are dropped on bye weeks.** A `rosters_weekly` / `player_stats` row for a
   (season, week, team) with no game joins to a null kickoff and is excluded (conservative). Roster
   carry-forward across a bye is a Phase 2 concern.
4. **`team_game_index` is global but `AsOf` loads only `history_seasons=4` of stat data.** For a
   prediction in the first ingested season (2013) the trailing-3-season normalization window is
   truncated. Irrelevant to the 2016+ model era; logged in the `coverage` block regardless.
5. **`nflfastR` EPA/CPOE/WP remain full-history model outputs** (decision #2, measurement
   assumption). Non-Vegas `wp`/`wpa` columns are retained; only the spread-derived `vegas_*` and
   final-outcome columns are stripped.
6. **2026 in-season data does not exist yet**, so the live path is verified only structurally
   (degrades to priors, tags `low_confidence`). End-to-end live behavior can't be tested until
   Week 1 data lands (~mid-Sept 2026).
7. **`participation` is materialised but unused.** ~479k rows of storage for a source the engine
   blocks. Deliberate (keeps the option open) but worth noting.
8. **No CI yet.** Tests are `network`-marked and run locally against the cache; wiring them into CI
   (with a cached fixture or a slim data pull) is deferred.

---

## 8. Acceptance criteria — status

| # | Criterion | Status |
|---|---|---|
| 1 | All Phase 0 tests remain green | ✅ 11/11 |
| 2 | New leakage suite passes (data_asof<kickoff, poisoned-row canary, bye-week, playoff order, NGS week 0, Vegas exclusion, PIT status enforcement) | ✅ 17/17 |
| 3 | Injury fallback validation completed; false-inclusion rate < 0.5% | ✅ **0.0057%** (1 / 17,479) |
| 4 | ID crosswalk coverage measured by unit-season; ≤ 3% ⇒ accept, else build fallback matcher | ✅ **0 unit-seasons > 3%** (worst 0.45%) — accepted, no matcher |
| 5 | Every as-of source has an explicit PIT status + publish-lag assumption | ✅ `config/publish_lag.yaml` |
| 6 | Cached `(team, season, week)` query returns as-of data within the performance target | ✅ cold **0.45 s**, warm 0.15–0.75 s (target < 2 s) |
| 7 | 2026 Week 1 ingest succeeds despite unavailable sources; produces labeled priors-only/low-confidence frames | ✅ `unavailable` manifests; `coverage.priors_only=True, low_confidence=True` |
| 8 | Two ingests against the same cache ⇒ byte-identical Parquet apart from manifest timestamps | ✅ verified in-process (3 sources) and cross-process (`shasum`) |
| 9 | No rating / matchup / expected-performance / score logic beyond scaffolding | ✅ `config/metrics.yaml` + `config/normalization.yaml` are empty scaffolds; no such code exists |
| 10 | Phase 1 report lists all required items | ✅ this document |

---

## 9. Files created in Phase 1

```
Makefile
config/
  ingest.yaml            # which sources/seasons the canonical layer materialises
  publish_lag.yaml       # per-source PIT status + publish-lag assumptions + global column strip
  metrics.yaml           # SCAFFOLD (empty)
  normalization.yaml     # SCAFFOLD (empty) — encodes decision DG
src/matchup/
  config.py              # pydantic loaders for the config files
  store.py               # canonical-layer reader (+ key-dtype normalization, caching)
  cli.py                 # ingest / calendar / crosswalk / validate-injuries / team-state / data-dictionary
  ingest/runner.py       # source wrappers, deterministic parquet writes, manifests, unavailable-season handling
  pointintime/
    calendar.py          # game_calendar, team_game_sequence, kickoff_expr
    publish_lag.yaml→availability.py  # is_available / available_asof / injury cutoff expr
    status.py            # PIT status enforcement
    asof.py              # AsOf accessors + team_state_asof + coverage metadata
  ids/crosswalk.py       # gsis<->pfr crosswalk + coverage report
  injuries/
    asof_rule.py         # conservative fallback cutoff + availability-status resolution
    validation.py        # retroactive 2022-2024 harness
  reporting/data_dictionary.py   # generates reports/data_dictionary.md
tests/
  conftest.py
  leakage/test_pointintime_engine.py       # 17 engine leakage tests
  unit/test_calendar_and_rules.py          # 19 unit tests
  reproducibility/test_ingest_deterministic.py  # 3 reproducibility tests
data/processed/**        # 193 parquet partitions + manifests (~205 MB, gitignored)
outputs/phase1/
  id_crosswalk_coverage.csv
  injury_asof_validation.{csv,json}
reports/
  data_dictionary.md     # generated
  phase1_report.md        # this file
```

---

## 10. Proposed Phase 2 scope — descriptive metrics & normalization scaffolding

**Do not start until explicitly approved.**

**Objective.** From the point-in-time frames, compute **descriptive per-play and per-player
metrics** and a **normalization layer** — still *no ratings, no weights, no matchup logic*. This is
the "measure things correctly and leak-free" phase; whether any metric has predictive value is a
Phase 3+ question.

### In scope
1. **`metrics/` module** — pure functions from an `AsOf` bundle to tidy metric frames:
   * QB per-dropback: EPA, success, CPOE (over attempts-with-CPOE only, carrying
     `cpoe_attempt_count` + `cpoe_coverage_fraction` per decision DE), sack rate, aDOT, YPA.
   * Rushing: EPA/att, success, YPC; RB receiving basics.
   * Team offense/defense: EPA/play (overall/pass/rush), success rate, early-down EPA, neutral pace,
     explosive rate — **as descriptive rolling / season-to-date aggregates**, computed on the
     team's *game sequence* (not week arithmetic).
   * NGS join-throughs (time to throw, separation, RYOE) at the player-week grain.
   * PFR pressure/coverage aggregates (2018+), with `earliest_valid_season` enforced.
2. **Windowing utilities** — season-to-date (expanding), trailing-N-games, prior-season, on the
   `team_game_index` sequence. Every output row carries `data_asof`, `n_games`, `window`.
3. **Normalization layer** (`normalize/`) — z-score / percentile / league-relative, computed
   **only** against the trailing 3 completed seasons available at the prediction date (decision DG),
   with the reference seasons logged per fit. **No shrinkage constants fitted** — the
   empirical-Bayes `k` estimation is scaffolded but frozen-empty.
4. **Split-half reliability report** — for each descriptive metric, how stable is it
   (odd vs even games, season-to-date at week W vs rest-of-season)? This tells us which metrics are
   even *candidates* for a rating in Phase 3. Output: `outputs/phase2/metric_reliability.csv`.
5. **Populate `config/metrics.yaml`** with each metric's source, formula, direction,
   `earliest_valid_season`, and proposed role (SIGNAL / DESCRIPTIVE / AVAIL_ADJ) — all
   `predictive_status: UNVALIDATED`.
6. **Tests:** leak-safety of every metric (extends the poisoned-row canary to metric outputs);
   hand-verified small-sample examples for each aggregate; window-boundary tests (bye weeks,
   season boundaries, playoffs); NGS/PFR `earliest_valid_season` enforcement; normalization
   reference-window correctness (never current/future season).

### Explicitly NOT in Phase 2
Player ratings, unit ratings, metric weights, composite scores, opponent adjustment, matchup
interactions, expected performance, expected score, any model fitting, any feature selection.

### Phase 2 acceptance (draft)
* All 50 Phase 0/1 tests still green.
* Every descriptive metric has a leak test and a hand-verified example.
* `metric_reliability.csv` produced for the full 2016–2025 span.
* Normalization never references the current incomplete or any future season (tested).
* `config/metrics.yaml` populated; `predictive_status` is `UNVALIDATED` for every entry.
* No rating/matchup/score logic exists.

---

## 11. Stop.

Phase 1 is complete and all acceptance criteria are met. **Awaiting explicit approval of the
Phase 2 scope in §10 before building anything in `metrics/` or `normalize/`.**
