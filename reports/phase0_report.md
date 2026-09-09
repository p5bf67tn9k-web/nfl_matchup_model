# Phase 0 Report — Data-Source & Metric Availability Audit

**Project:** `nfl_matchup_model` — independent, auditable NFL matchup strength & performance model
**Run date:** 2026-09-08
**Environment:** Python 3.12.14 (Homebrew), `nflreadpy` 0.1.5, `polars` 1.44.1, local filesystem cache
**Scope:** READ-ONLY. No ratings, matchups, expected performance, or score models were built.

---

## 0. TL;DR — what the audit changed

The architecture is sound, but the audit found **six discrepancies** between the architecture
document and the real data. None is fatal; three require design changes before Phase 1.

| # | Discrepancy | Severity | Action |
|---|---|---|---|
| D-1 | `depth_charts` has a **schema regime break at 2025** — the new ESPN "by date" format has NULL `season`/`week` and only a `dt` timestamp. | High | Drop `depth_charts` from the MVP; use `snap_counts` + `schedules` QB names instead. Decision needed. |
| D-2 | `load_injuries` **drops the `date_modified` column entirely for the 2025 (current) season.** The as-of anchor the doc assumed does not exist for live prediction. | High | Add a "Saturday 23:59 ET of game week" fallback rule; validate it retroactively on 2022–2024. Decision needed. |
| D-3 | **No 2026 in-season data exists yet.** `nflreadpy` hard-errors (`Season must be between 1999 and 2025`) for `load_pbp`/`load_snap_counts`/`load_nextgen_stats`/`load_pfr_advstats`/`load_injuries`/`load_rosters_weekly`/`load_participation`/`load_ftn_charting` on season 2026. Only `load_schedules` and `load_depth_charts` return 2026 rows. | Medium | Ingest layer must catch the range error and degrade to priors. Live 2026 Weeks 1–4 run on 2025 priors only. |
| D-4 | `injuries.report_status` is **~40–55% NULL from 2016 onward** (the "Probable" tier was removed in 2016; many practice-report players get no game-status designation). | Medium | Lean on `practice_status` (well populated: Full / DNP / Limited), not `report_status`, for the availability signal. |
| D-5 | Architecture doc mischaracterized `participation`. Reality: **all seasons 2016–2025 are in one file**; 2016–2022 is sparse on routes/pressure/coverage (`defense_coverage_type` is 0% for 2016–17); **2023+ is complete but FTN-sourced and released only after the postseason** → not live-safe. | Low | Net effect unchanged (exclude from MVP). Correct the data dictionary. |
| D-6 | `cpoe` is **NULL on 15–21% of pass plays** (sacks, scrambles, throwaways, spikes), not just non-pass plays. Doc listed CPOE as "AVAILABLE / RELIABLE" without the caveat. | Low | Aggregate CPOE over *attempts-with-CPOE* only; document the denominator. |

**Good news the audit confirmed:**
- `pbp` schema is **stable 2016 → 2025** (372 columns, `epa` defined on >98% of rows).
- `pfr_advstats` carries the nflverse `game_id` → **clean joins, no fragile date-matching** (the doc's worry was unfounded).
- `snap_counts` is **0% null** on all snap/percentage fields for sampled seasons — a solid aggregation-weight backbone.
- `injuries.date_modified`, *when present* (2010–2024), precedes kickoff for **99.99%** of rows (1 of 17,479 in 2022–24) → a trustworthy as-of stamp for the historical backtest.

---

## 1. Files created

```
nfl_matchup_model/
├── .gitignore                         # excludes .venv, data/, caches
├── pyproject.toml                     # deps pinned; py>=3.12; pytest markers (network, slow)
├── README.md
├── config/
│   └── data_sources.yaml              # VERIFIED source registry: coverage, join keys, as-of anchors, caveats
├── scripts/
│   ├── phase0_audit.py                # main audit: schema + coverage + null rates + date-col detection
│   ├── phase0_probe.py                # depth_charts / participation / injuries / schedules / NGS deep-dive
│   ├── phase0_probe2.py               # pbp metric null-rates + join-key verification
│   └── phase0_probe3.py               # 2026 live-season readiness + participation-by-season + injury leakage check
├── src/matchup/
│   ├── __init__.py                    # package stub only
│   └── _version.py
├── tests/
│   ├── conftest.py                    # points nflreadpy at the repo-local cache
│   └── leakage/
│       └── test_asof_assumptions.py   # 11 characterization tests (all passing)
├── outputs/phase0/
│   ├── summary.csv                    # rows/season, season & week coverage, has_week_zero — per source
│   ├── keyfield_nulls.csv             # presence + null% for every curated key field
│   ├── datecols.csv                   # every candidate as-of / timestamp column found, with samples
│   ├── run_meta.json                  # versions, current-season logic, error log (0 errors)
│   └── <source>.schema.json           # full column list + dtypes + profile, one per source (19 files)
└── reports/
    └── phase0_report.md               # this document
```

Environment: a `.venv` (Python 3.12) was created and `nflreadpy, polars, pyarrow, pandas, numpy,
scipy, scikit-learn, pydantic, pyyaml, pytest, ruff` installed. Downloaded nflverse data (~84 MB)
is cached under `data/raw/nflreadpy_cache/` (gitignored).

---

## 2. Data sources verified

All 19 source variants loaded successfully (`run_meta.json` → `"errors": {}`). Full detail in
`config/data_sources.yaml` and `outputs/phase0/*.schema.json`.

| Source | Seasons returned | Grain | Join key(s) | As-of anchor | Verdict |
|---|---|---|---|---|---|
| `load_pbp` | 1999–2025 | play | `game_id`, `play_id` | game calendar (`game_date` 0% null) | **RELIABLE**. Backbone. Stable schema 2016–25. |
| `load_player_stats` (week) | 1999–2025 | player-week | `player_id`,`season`,`week` | game calendar | **RELIABLE**. Off+def+kick combined file. |
| `load_team_stats` (week) | 1999–2025 | team-week | `team`,`season`,`week` | game calendar | RELIABLE (rebuildable from pbp). |
| `load_snap_counts` | 2012–2025 | player-game | `game_id`,`pfr_player_id` | game calendar | **RELIABLE**. 0% null. Has `team`,`opponent`,`game_type`. |
| `load_nextgen_stats` ×3 | 2016–2025 | player-week | `player_gsis_id`,`season`,`week` | game calendar | **RELIABLE w/ caveats**: `week==0` = season aggregate; min-attempt thresholds drop low-volume players. |
| `load_pfr_advstats` ×4 | **2018**–2025 | player-week | `game_id`,`pfr_player_id` | game calendar (publish lag ~3d) | **LIMITED**: single-source charting; 2018 floor. Clean `game_id` join. |
| `load_injuries` | 2009–2025 | player-team-week | `season`,`week`,`team`,`gsis_id` | `date_modified` (2010–2024) / **fallback for 2025+** | **LIMITED**: see D-2, D-4. |
| `load_depth_charts` | 2001–2024 old fmt / 2025+ new fmt | mixed | — | mixed (`dt` for new fmt) | **LIMITED — schema break, see D-1.** |
| `load_rosters_weekly` | 2002–2025 | player-team-week | `season`,`week`,`gsis_id` | game calendar | RELIABLE for roster membership. |
| `load_schedules` | 1999–**2026** | game | `game_id` | schedule (known in advance) | **RELIABLE**. THE game calendar. `gametime` = ET (verified). |
| `load_participation` | 2016–2025 | play | `nflverse_game_id`,`play_id` | **not live-safe** | **EXCLUDED from MVP — see D-5.** |
| `load_ftn_charting` | 2022–2025 | play | `nflverse_game_id`,`play_id` | game calendar (`date_pulled` present) | **EXCLUDED from MVP** (decision #11). |
| `load_players` | n/a | player | `gsis_id` ↔ `pfr_id` (91%) ↔ `espn_id` (67%) | n/a | RELIABLE w/ 91% pfr_id crosswalk (D-6-adjacent). |

### The game calendar / timezone (verified)

`schedules` has `gameday` (`YYYY-MM-DD` string) + `gametime` (`HH:MM` string). Cross-checking
`pbp.start_time` (local, `"9/8/24, 13:03:02"`) against `pbp.time_of_day` (UTC,
`"2024-09-08T17:03:02Z"`) for `2024_01_ARI_BUF` confirms **local = US Eastern** (13:03 → 17:03Z, a
+4 EDT offset). Phase 1 will construct a tz-aware kickoff as
`America/New_York` from `gameday + gametime`. ~98%+ of games parse; the rest are TBD-time
placeholders resolved closer to gameday.

### Playoff week numbering (verified)

2024: regular weeks 1–18, then `WC`=19, `DIV`=20, `CON`=21, `SB`=22. This shifts with the
17→18-game change (2021). **Weeks must be mapped through `game_type`, never hardcoded.** Regular-
season weeks also have fewer than 16 games due to byes (verified: week 12 of 2024 had 13 games).

---

## 3. Metrics verified — availability & proposed role

Per the new requirement, every metric carries **three** tags:
- **Availability** (verified this run): `RELIABLE` / `LIMITED` / `NOT AVAILABLE`
- **Proposed role**: `SIGNAL` (predictive input candidate) / `DESCRIPTIVE` (report colour only) / `AVAIL-ADJ` (roster/availability adjustment)
- **Predictive status**: `UNVALIDATED` for **everything** — no metric has earned its place yet. Phase 2+ walk-forward validation decides. Intuitive ≠ predictive.

### 3.1 Quarterback

| Metric | Source | Availability | Proposed role | Predictive status |
|---|---|---|---|---|
| dropback EPA/play, success rate, YPA, comp% | pbp | RELIABLE (≥98%) | SIGNAL | UNVALIDATED |
| CPOE | pbp | **LIMITED** — null on 15–21% of pass plays (D-6) | SIGNAL | UNVALIDATED |
| sack rate, QB-hit rate taken | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| INT rate | pbp | RELIABLE (low frequency) | DESCRIPTIVE (likely) | UNVALIDATED |
| explosive pass rate (≥20 yд) | pbp | LIMITED (noisy small-sample) | DESCRIPTIVE | UNVALIDATED |
| avg time to throw, aggressiveness, air-yards-to-sticks | NGS passing (2016+) | RELIABLE (qualified QBs) | SIGNAL | UNVALIDATED |
| completion % above expectation (NGS) | NGS passing | RELIABLE (qualified QBs) | SIGNAL | UNVALIDATED |
| times pressured / pressure→sack | PFR pass (2018+) | LIMITED (single-source, 2018 floor) | SIGNAL | UNVALIDATED |
| bad-throw %, on-target % | PFR pass (2018+) | LIMITED | DESCRIPTIVE | UNVALIDATED |
| rushing/scramble EPA | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| EPA when pressured vs clean | PFR/participation | LIMITED / NOT LIVE-SAFE | DESCRIPTIVE | UNVALIDATED |
| Total QBR | *not in nflreadpy 0.1.5* | **NOT AVAILABLE** (no `load_espn_qbr`) | — | — |

> **Discrepancy:** the architecture doc listed ESPN Total QBR via `load_espn_qbr`. **That function
> does not exist in `nflreadpy` 0.1.5.** QBR is out unless we add a separate ingestion path (not
> recommended for MVP).

### 3.2 WR / TE

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| targets, receptions, yards, TD, first downs, aDOT, YAC | pbp / player_stats | RELIABLE | SIGNAL/DESC | UNVALIDATED |
| target share, air-yards share, WOPR | player_stats | RELIABLE | SIGNAL | UNVALIDATED |
| per-target EPA | pbp | RELIABLE (QB-entangled) | SIGNAL | UNVALIDATED |
| avg separation, avg cushion, YAC over expected | NGS receiving (2016+) | LIMITED (min-target threshold) | SIGNAL | UNVALIDATED |
| drops, drop % | PFR rec (2018+) | LIMITED | DESCRIPTIVE | UNVALIDATED |
| explosive reception rate | pbp | LIMITED (noisy) | DESCRIPTIVE | UNVALIDATED |
| **yards per route run, targets per route run, route participation** | participation | **NOT AVAILABLE (live)** — routes only ~37% pre-2023; 2023+ not live-safe | — | — |
| slot vs wide role | participation | **NOT AVAILABLE (live)** | — | — |

### 3.3 RB

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| carries, rush yards, YPC, rush success rate, rush EPA | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| rush yards over expected, efficiency | NGS rushing (2018+ for RYOE) | LIMITED (threshold) | SIGNAL | UNVALIDATED |
| yards before/after contact, broken tackles | PFR rush (2018+) | LIMITED | SIGNAL/DESC | UNVALIDATED |
| receiving work (targets, rec EPA) | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| explosive run rate | pbp | LIMITED (noisy) | DESCRIPTIVE | UNVALIDATED |
| fumble rate | pbp | LIMITED (very low freq) | DESCRIPTIVE | UNVALIDATED |
| pass-blocking | — | NOT AVAILABLE | — | — |

### 3.4 Offensive line — **team-derived only (decision #7)**

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| team sack rate allowed, QB-hit rate allowed | pbp | RELIABLE (QB-confounded) | SIGNAL | UNVALIDATED |
| team pressure rate allowed | PFR pass agg (2018+) | LIMITED | SIGNAL | UNVALIDATED |
| team adjusted line yards / yds before contact (run block) | pbp-derived | LIMITED (approx) | SIGNAL | UNVALIDATED |
| line continuity (Wk-1 starters available, snaps together) | snap_counts + rosters | RELIABLE (2012+) | SIGNAL / AVAIL-ADJ | UNVALIDATED |
| penalties by lineman | pbp | LIMITED (noisy) | DESCRIPTIVE | UNVALIDATED |
| individual pass/run-block grades, pressures allowed per lineman | — | **NOT AVAILABLE** (PFF/ESPN only) | — | — |

### 3.5 DL / pass rush

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| sacks, QB hits, TFL (player & team) | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| pressures, hurries, hits (player) | PFR def (2018+) | LIMITED | SIGNAL | UNVALIDATED |
| team pressure rate generated | PFR def agg / (participation, not live) | LIMITED | SIGNAL | UNVALIDATED |
| pass-rush win rate, get-off | — | NOT AVAILABLE | — | — |

### 3.6 Linebackers — **team-derived only (decision #7)**

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| tackles, assists, TFL | pbp | RELIABLE (counts; low quality signal) | DESCRIPTIVE | UNVALIDATED |
| missed tackles, missed-tackle % | PFR def (2018+) | LIMITED | SIGNAL/DESC | UNVALIDATED |
| coverage targets / yards allowed when targeted | PFR def (2018+) | LIMITED (attribution noise) | DESCRIPTIVE | UNVALIDATED |
| run-fit / gap integrity | — | NOT AVAILABLE | — | — |

### 3.7 Defensive backs — **team-derived only (decision #7)**

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| def targets, completions allowed, yards allowed, passer rating allowed | PFR def (2018+) | LIMITED (charting attribution, garbage time) | DESCRIPTIVE | UNVALIDATED |
| PBU, INT (player) | pbp / PFR def | LIMITED (low freq) | DESCRIPTIVE | UNVALIDATED |
| team pass-D EPA, explosive pass allowed | pbp | RELIABLE (team) | SIGNAL | UNVALIDATED |
| completion % allowed vs expected (per defender) | — | NOT AVAILABLE | — | — |
| separation allowed, man/zone coverage rate (live) | participation | NOT AVAILABLE (live) | — | — |

### 3.8 Team offense / defense

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| EPA/play overall / pass / rush, dropback EPA, success rate | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| early-down EPA, `xpass` / pass-rate-over-expected | pbp (`xpass` ~24% null on defined plays) | RELIABLE–LIMITED | SIGNAL | UNVALIDATED |
| neutral pace / plays per game | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| explosive rate (pass/run) for/against | pbp | LIMITED (noisy) | DESCRIPTIVE | UNVALIDATED |
| opponent-adjusted EPA (offense/defense) | pbp + ridge | RELIABLE *given method* | SIGNAL | UNVALIDATED (decision #9: prove it adds value) |
| red-zone / 3rd-down / 3rd-and-long efficiency | pbp splits | LIMITED (small sample) | DESCRIPTIVE | UNVALIDATED |
| team pressure rate for/against | PFR (2018+) | LIMITED | SIGNAL | UNVALIDATED |

### 3.9 Special teams (needed for the eventual score layer)

| Metric | Source | Availability | Role | Pred. status |
|---|---|---|---|---|
| FG% by distance, made/miss | pbp | RELIABLE | SIGNAL | UNVALIDATED |
| punt / kickoff / return EPA | pbp | RELIABLE | SIGNAL | UNVALIDATED |

---

## 4. Metrics rejected (this phase)

Rejected = **not available reliably enough to build on**, or **not obtainable via `nflreadpy` 0.1.5**.

| Metric / capability | Reason |
|---|---|
| ESPN Total QBR (`load_espn_qbr`) | **Function does not exist in `nflreadpy` 0.1.5.** Would need a separate scraper. Out for MVP. |
| Yards per route run, targets per route run, route participation | Requires `participation.route`; only ~37% populated pre-2023, and 2023+ is not released until after the postseason (not live-safe). |
| Man/zone & coverage-type rates for/against | `participation.defense_coverage_type` 0% for 2016–17, ~38% for 2018–22, and only ~49% even in the not-live-safe 2023+ feed. |
| Individual OL pass/run-block grades, pressures allowed per lineman | Not in any free source (PFF/ESPN proprietary). Confirmed by decision #7 — OL is team-derived. |
| Individual LB/DB coverage grades, per-defender CPOE / separation allowed | No per-defender expected-completion or tracking data in free sources. |
| Pass-rush win rate / run-block win rate / get-off | ESPN proprietary, not in `nflreadpy`. |
| "Performance vs pressure" QB splits as an MVP signal | Depends on `participation.was_pressure` (not live-safe) or thin PFR splits; sample sizes too small for a stable weekly rating. Keep DESCRIPTIVE only. |
| Weather-adjusted metrics | `schedules.temp`/`wind` 26–36% null historically, 100% null for future games. Usable as a coarse flag only, not a modelled adjustment, for MVP. |
| Depth-chart-derived "starter role" as a primary weight | `depth_charts` schema break (D-1) + ESPN ordering noise. Use `snap_counts` instead. |

---

## 5. Leakage risks discovered

| Risk | Detail (verified) | Mitigation for Phase 1 |
|---|---|---|
| **L-1 Injuries have no as-of stamp for the live season** | `load_injuries(seasons=[2025])` returns a frame with **no `date_modified` column at all**; 2024 has it. | Fallback rule: a (season, week) injury report is knowable as of **Saturday 23:59 America/New_York** of that game week (Thu/Fri games: use kickoff − 24h). Validate retroactively on 2022–2024 where `date_modified` exists. |
| **L-2 Injury reports get amended after kickoff** | When `date_modified` exists (2010–2024), only **1 of 17,479** rows (2022–24) is stamped after its game's kickoff — but it is non-zero. | Hard filter `date_modified < kickoff_et` in the historical backtest; the fallback rule handles live. |
| **L-3 `report_status` sparsity invites wrong "healthy" inferences** | ~40–55% NULL since 2016. NULL ≠ "active"; it often means "on the practice report, no game designation." | Treat NULL `report_status` as *unknown*, derive the availability signal primarily from `practice_status` + `rosters_weekly.status` + game-day `inactives` where available. |
| **L-4 NGS `week==0` season-aggregate rows** | Verified: a `week==0` row holds full-season totals (Herbert: 504 attempts). Joining without filtering pulls end-of-season data into every week. | `filter(week >= 1)` at ingestion; never use `week==0` except as an explicit season-total cross-check. |
| **L-5 `depth_charts` new format is a rolling snapshot** | 2025+ rows have a `dt` that ranges from **2025-08-03 to 2026-03-14** with no week key. A naive load mixes an March-2026 snapshot into a September-2025 prediction. | If used at all: join by `dt <= kickoff_et`, taking the latest snapshot per team before kickoff. Otherwise exclude (recommended). |
| **L-6 Participation 2023+ is post-season release** | Data-quality jump at 2023 is real and tempting; the FTN feed is published only after the playoffs. | Excluded from MVP. If ever added, gate behind an explicit `as_of_safe=False` flag and never in the live path. |
| **L-7 Opponent-adjustment feedback** | Ridge adjusted-EPA uses opponent strength, which itself depends on all games including future ones if fit on the full season. | Refit walk-forward on `week < W` only; opponent ratings taken as-of the same cutoff. Covered by the architecture, restated here. |
| **L-8 EPA/CPOE/WP are full-history model outputs** | Confirmed as a *measurement* assumption (decision #2). Not a per-game leak, but a subtle one: the models "know" later seasons' scoring environment. | Documented. Phase 8 sensitivity: refit EPA on past-only data and compare. |
| **L-9 `schedules` Vegas lines** | `spread_line`/`total_line` 0% null 2016–2025 — trivially available and tempting. | Project rule: **never an input.** Allowed only in the validation benchmark table. A lint test can assert these columns never enter a feature frame. |
| **L-10 Playoff/bye week gaps** | Weeks are not contiguous per team (byes) and playoff week numbers vary. Rolling "last 3 games" ≠ "last 3 week numbers". | Rolling windows must operate on a team's ordered *game* sequence, not on `week` arithmetic. |
| **L-11 `pfr_advstats` publish lag** | Charting data lands ~2–3 days after games. For a Thursday game, the prior week's PFR file may not be complete. | Per-source publish-lag constant in the `pointintime` config; a feature is only "available" if `kickoff_et > prior_game_date + lag`. |
| **L-12 Cross-season player identity** | `pfr_id` crosswalk is 91% — 9% of `snap_counts` / `pfr_advstats` rows won't map to `gsis_id`. Silently dropping them biases unit aggregates toward well-mapped (usually veteran) players. | Log every unmatched row; decide (Decision D-4) whether to build a name+team+season fallback matcher or accept + monitor the loss. |

---

## 6. Architecture changes recommended

1. **`pointintime` becomes the first thing built in Phase 1**, not a convention. It owns:
   - `game_calendar`: one row per game with a **tz-aware `kickoff_utc`** derived from `schedules`
     (`gameday` + `gametime` as `America/New_York`), plus `game_type`, rest days, `season`, `week`.
   - `team_game_sequence`: each team's games in chronological order with an integer `team_game_index`
     (so "rolling 3 games" is well-defined across byes and playoffs — L-10).
   - `source_publish_lag`: per-source constant (`pbp`≈1d, `snap_counts`≈1d, `ngs`≈1d, `pfr`≈3d,
     `player_stats`≈1d) used to compute each feature row's `data_asof`.
   - `as_of(entity, kickoff_utc)` accessors that every downstream module must call.

2. **Ingest layer must tolerate "season not yet published."** `nflreadpy` raises
   `ValueError: Season must be between 1999 and 2025` (or a 404) for 2026. Wrap every loader; on that
   error, return an empty frame with the right schema and a logged warning, so the live pipeline
   degrades to priors instead of crashing (D-3).

3. **Drop `depth_charts` from the MVP** (D-1). Projected-starter identification for the MVP comes from:
   `schedules.away_qb_name`/`home_qb_name` (QB), `rosters_weekly` (roster membership), and trailing
   `snap_counts` shares (everyone else). Revisit a depth-chart normalizer post-MVP only if a gap appears.

4. **Injuries: implement the L-1 fallback rule now**, with a retroactive validation harness on
   2022–2024 (compare "what the fallback rule would have known" vs "what `date_modified` says was known").
   Availability signal = `practice_status` + `report_status`(when present) + `rosters_weekly.status`.

5. **Every feature carries an `earliest_valid_season`.** PFR-derived features → 2018; NGS-derived →
   2016; anything else → 2016 (MVP core). The walk-forward harness must skip folds where a feature
   isn't yet defined, or fall back to a coarser metric. Add this to `config/`.

6. **Canonical storage**: keep `nflreadpy`'s filesystem cache as the immutable raw layer
   (`data/raw/nflreadpy_cache/`), and write our own **partitioned parquet** to `data/processed/`
   (one dataset per source, partitioned by season). Record the `nflverse` release tag / download
   date in a sidecar `_manifest.json` per pull for reproducibility. **No DuckDB yet** (decision #5) —
   polars over parquet is enough; the `data/processed/` layout is DuckDB-ready if that changes.

7. **`config/` gets three files** (config-as-data, decision #8):
   `data_sources.yaml` (done), `metrics.yaml` (metric → source, formula, direction, `earliest_valid_season`,
   role), `normalization.yaml` (baseline era, shrinkage `k`, frozen params + `frozen_on` date).

8. **CPOE aggregation denominator is explicit** (D-6): CPOE ratings are computed over
   *pass attempts where `cpoe` is non-null*, and the coverage fraction is itself logged as a
   quality indicator on the QB rating.

9. **NGS ingestion filters `week >= 1`** and **maps playoff weeks via `schedules.game_type`** — never
   trust the raw `week` integer for ordering.

10. **QBR is removed** from the metric set (no `load_espn_qbr`). If it's wanted later it's a separate
    ingestion project with its own leakage review.

No change to the four-layer architecture, the additive-in-EPA matchup engine, the
validation-first acceptance philosophy, or the MVP scope. The changes are all in the **data /
point-in-time foundation**.

---

## 7. Tests created

`tests/leakage/test_asof_assumptions.py` — 11 characterization tests, **all passing**, marked
`network` (reuse the repo-local cache). They pin data assumptions so a future nflverse change
breaks loudly:

| Test | Pins |
|---|---|
| `test_schedules_have_kickoff_components_and_are_ET` | `gameday`+`gametime` parse for >98% of games; `gametime` is US Eastern (UTC cross-check). |
| `test_playoff_weeks_must_be_mapped_via_game_type_not_hardcoded` | WC=19 / SB=22 in the 18-game era; regular season max week = 18. |
| `test_pbp_has_stable_asof_fields_and_core_metric_coverage` | `game_id/game_date/epa/...` present 2016 & 2025; `epa` >98% non-null; `cpoe` 50–95% on pass plays. |
| `test_ngs_week_zero_is_season_aggregate` | `week==0` rows exist and hold season totals (must be filtered). |
| `test_injuries_date_modified_precedes_kickoff_when_present` | <0.1% of 2023–24 injury rows stamped after kickoff. |
| `test_injuries_current_season_has_no_modification_timestamp` | 2025 injuries lack a usable `date_modified` → live fallback required. |
| `test_depth_charts_new_format_has_no_week_key` | Old fmt weekly + no `dt`; new fmt (2025+) NULL week + `dt` present. |
| `test_participation_route_coverage_jumps_at_2023` | `route` coverage <60% in 2021, >95% in 2024. |
| `test_pfr_advstats_join_on_nflverse_game_id` | PFR carries a well-formed nflverse `game_id`. |
| `test_players_crosswalk_pfr_id_partial` | `gsis_id` ~100%, `pfr_id` 80–99% (currently 91%). |
| `test_2026_in_season_sources_not_yet_available` | `load_pbp(2026)` raises; `load_schedules(2026)` succeeds. |

Run: `.venv/bin/python -m pytest tests/leakage -q` → `11 passed`.

> These are **data** tests, not model tests. The model-logic leakage suite (rolling-window
> correctness, "poisoned future row" canary, `data_asof < kickoff` invariant) is built in Phase 1
> alongside the `pointintime` module.

---

## 8. Remaining decisions (need your call before Phase 1)

| ID | Decision | Recommendation |
|---|---|---|
| **DA** | `depth_charts`: drop from MVP (use `snap_counts` + `schedules` QB names), or invest now in an old/new format normalizer? | **Drop from MVP.** Add later only if a concrete gap appears. |
| **DB** | Live-season injury as-of rule: accept "**Saturday 23:59 America/New_York of the game week**" (Thu/Fri games: kickoff − 24h) as the `data_asof` for rows lacking `date_modified`? | **Accept**, with the retroactive 2022–2024 validation harness as a Phase 1 deliverable. |
| **DC** | Live 2026 Weeks 1–4 (zero in-season data): produce priors-only predictions flagged low-confidence, or start formal live prediction at Week 5? | **Produce them, flagged.** Formal accuracy tracking starts Week 5. |
| **DD** | `pfr_id` 9% crosswalk gap: accept the join loss (log unmatched), or build a name+team+season fallback matcher in Phase 1? | **Accept + log** for MVP. Build the matcher only if unmatched snap share exceeds ~3% for any unit. |
| **DE** | CPOE nulls on 15–21% of pass plays: aggregate CPOE over attempts-with-CPOE only (recommended), or attempt an imputation? | **Attempts-with-CPOE only**, with the coverage fraction logged as a QB-rating quality flag. |
| **DF** | Storage: `nflreadpy` filesystem cache as raw layer + our own season-partitioned parquet in `data/processed/`, manifest sidecar, no DuckDB yet — confirm? | **Confirm** (matches decision #5). |
| **DG** | Baseline era: use 2006–2015 pbp **only** for league-relative normalization baselines (flagged `era=pre_core`), model era strictly 2016+ — confirm? | **Confirm** (matches decision #1). |
| **DH** | QBR removed (no `load_espn_qbr`) — accept, or authorize a separate QBR ingestion path? | **Accept removal** for MVP. |

---

## 9. Proposed Phase 1 plan — canonical data layer + point-in-time engine

**Objective.** A reproducible, leak-safe canonical data layer and an `as_of` engine that can
answer "what was knowable about team/player X before kickoff of game G?" — for both historical
walk-forward and live 2026 use. **No ratings, matchups, performance, or score models.**

### 1.1 Inputs
- `nflreadpy` sources marked RELIABLE / LIMITED in §2 (exclude `participation`, `ftn_charting`, `depth_charts`*).
- Decisions DA–DH resolved.

### 1.2 Work items
1. **`ingest/`** — one wrapper per source: pulls via `nflreadpy`, writes season-partitioned parquet
   to `data/processed/<source>/season=YYYY/`, plus `_manifest.json` (download timestamp, nflreadpy
   version, row count). Tolerates "season not yet published" (returns typed-empty + warning).
2. **`pointintime/game_calendar`** — build `game_calendar` (tz-aware `kickoff_utc`, `game_type`,
   rest, `season`, `week`) and `team_game_sequence` (chronological `team_game_index`).
3. **`pointintime/publish_lag`** — `config/publish_lag.yaml`; function
   `is_available(source, event_date, kickoff_utc)`.
4. **`pointintime/as_of`** — accessors:
   `pbp_asof(team, kickoff)`, `player_week_asof(player, kickoff)`, `snaps_asof(...)`,
   `ngs_asof(...)`, `pfr_asof(...)`, `injuries_asof(team, kickoff)` (with the DB fallback rule),
   `roster_asof(...)`. Each returns only rows with `data_asof < kickoff` and stamps `data_asof`.
5. **`ids/`** — `gsis_id ↔ pfr_id` crosswalk from `load_players`; `resolve_player()` with logged
   unmatched rate per (season, unit).
6. **Injuries fallback + validation** — implement DB rule; harness comparing fallback-knowable vs
   `date_modified`-knowable on 2022–2024; report false-inclusion / false-exclusion rates.
7. **`data_dictionary.md`** (generated from `config/`) + attribution block (nflverse CC-BY-SA,
   FTN, PFR) in `reports/`.
8. **Leakage test suite** (`tests/leakage/`, model-level this time):
   - `data_asof < kickoff_utc` holds for every row from every `as_of` accessor.
   - "Poisoned future row" canary: inject a fabricated Week 18 game; assert no `as_of` result for an
     earlier week changes.
   - Rolling windows operate on `team_game_index`, not `week` arithmetic (bye-week test case).
   - Vegas-line columns (`spread_line`, `total_line`, moneylines) never appear in an `as_of` frame.
   - NGS `week==0` never returned by `ngs_asof`.
   - Playoff-week ordering test (2021+ 18-game season).
9. **Reproducibility test** — two ingest runs from cache produce byte-identical `data/processed/`
   parquet (modulo manifest timestamps).

### 1.3 Outputs
- `data/processed/<source>/…` partitioned parquet + manifests.
- `src/matchup/pointintime/` (`game_calendar`, `as_of`, `publish_lag`), `src/matchup/ingest/`, `src/matchup/ids/`.
- `config/publish_lag.yaml`, `config/metrics.yaml` (skeleton), updated `config/data_sources.yaml`.
- `reports/data_dictionary.md`, attribution notes.
- `outputs/phase1/injury_asof_validation.csv`, `outputs/phase1/id_crosswalk_coverage.csv`.

### 1.4 Tests / acceptance criteria
- All Phase 0 characterization tests still green.
- New leakage suite green, including the poisoned-row canary.
- `injuries_asof` fallback validated: on 2022–2024, false-inclusion rate (rows the fallback would
  wrongly treat as known pre-kickoff) **< 0.5%**.
- ID crosswalk: unmatched snap share **< 3%** per unit-season, or the fallback matcher (DD) is built.
- Given any `(team, season, week)` in 2016–2025, every `as_of` accessor returns a non-empty,
  leak-checked frame in **< 2 s** from cache.
- For 2026 Week 1: ingest runs without error, `as_of` accessors return priors-only frames flagged
  `low_confidence=True`.
- Reproducibility test passes.

### 1.5 Leakage checks specific to Phase 1
- L-1/L-2 (injuries): fallback rule + retroactive validation.
- L-4 (NGS week 0): filtered at `ngs_asof`.
- L-9 (Vegas lines): lint test.
- L-10 (bye/playoff weeks): `team_game_index` + test.
- L-11 (PFR lag): `publish_lag.yaml` + `is_available`.
- L-12 (IDs): coverage logging.

### 1.6 Explicitly NOT in Phase 1
Player ratings, unit ratings, opponent adjustment, matchup calculations, expected performance,
expected score, reporting of matchups. Normalization/shrinkage constants are *scaffolded* in
`config/normalization.yaml` but not fitted.

---

## 10. Do not proceed to Phase 1 until explicitly approved.

Awaiting: sign-off on §6 architecture changes and decisions DA–DH in §8.
