# Data Dictionary — canonical layer (`data/processed/`)

_Generated 2026-09-08T20:01:18+00:00 from `config/ingest.yaml`, `config/publish_lag.yaml`, and the ingested `_manifest.json` sidecars._

Every source below is materialised as season-partitioned Parquet at `data/processed/<source>/season=YYYY/data.parquet` with a `_manifest.json` sidecar (row count, column count, content SHA-256, point-in-time status, publish-lag assumption, source date range, ingest timestamp).

## Point-in-time status legend

| status | meaning |
|---|---|
| `LIVE_SAFE` | knowable before kickoff in real time during the season |
| `HISTORICAL_SAFE` | safe for backtest, not guaranteed available live |
| `POST_SEASON_ONLY` | published only after the season → blocked from prediction frames |
| `REFERENCE_ONLY` | benchmark / identity only → blocked from feature frames |
| `UNKNOWN` | timing unproven → blocked |

## `publish_lag_type` legend

| type | meaning |
|---|---|
| `empirical` | a real per-row publication timestamp exists and is used directly |
| `conservative_assumption` | **no** publication timestamp in the data; a deliberately cautious engineering guess (prefer false exclusion). NOT an exact release time. |
| `known` | timing structurally known (schedule fixtures) |
| `unknown` | timing cannot be reconstructed |

## Sources

### `pbp`

* **loader:** `nflreadpy.load_pbp()`
* **grain:** play
* **join key:** `game_id`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 1 day(s) (`conservative_assumption`)
* **earliest valid season:** 1999
* **materialised coverage:** 2013–2025 (13 partitions), 628,163 rows; unavailable: ['2026']
* **notes:** nflfastR play-by-play typically refreshes within ~24h of a game, but rows carry no publication timestamp (game_date is the play's date, time_of_day is the play clock, neither is a release time). 1 day is a conservative floor; true availability for the very first games of a Sunday slate may be a few hours, but we do not rely on that.

### `player_stats`

* **loader:** `nflreadpy.load_player_stats(summary_level='week')`
* **grain:** player-week
* **join key:** `['season', 'week', 'team']`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 1 day(s) (`conservative_assumption`)
* **earliest valid season:** 1999
* **materialised coverage:** 2013–2025 (13 partitions), 234,738 rows; unavailable: ['2026']
* **notes:** Derived from pbp; same reasoning as pbp. No publication timestamp.

### `team_stats`

* **loader:** `nflreadpy.load_team_stats(summary_level='week')`
* **grain:** team-week
* **join key:** `['season', 'week', 'team']`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 1 day(s) (`conservative_assumption`)
* **earliest valid season:** 1999
* **materialised coverage:** 2013–2025 (13 partitions), 7,124 rows; unavailable: ['2026']
* **notes:** Derived from pbp; rebuildable. No publication timestamp.

### `snap_counts`

* **loader:** `nflreadpy.load_snap_counts()`
* **grain:** player-game
* **join key:** `game_id`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 1 day(s) (`conservative_assumption`)
* **earliest valid season:** 2012
* **materialised coverage:** 2013–2025 (13 partitions), 324,611 rows; unavailable: ['2026']
* **notes:** Sourced from Pro Football Reference. The nflverse update schedule says snaps refresh several times daily in-season, but a full game's snap counts are not timestamped in the data. 1 day is the stated project assumption; treat as conservative, not exact.

### `ngs_passing`

* **loader:** `nflreadpy.load_nextgen_stats(stat_type='passing')`
* **grain:** player-week
* **join key:** `['season', 'week', 'team']`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 1 day(s) (`conservative_assumption`)
* **earliest valid season:** 2016
* **materialised coverage:** 2016–2025 (10 partitions), 5,933 rows; unavailable: ['2026']
* **notes:** NFL Next Gen Stats weekly player files update nightly in-season per the nflverse schedule, but rows carry no publication timestamp. week == 0 rows are SEASON AGGREGATES and are dropped by the as-of engine.

### `ngs_receiving`

* **loader:** `nflreadpy.load_nextgen_stats(stat_type='receiving')`
* **grain:** player-week
* **join key:** `['season', 'week', 'team']`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 1 day(s) (`conservative_assumption`)
* **earliest valid season:** 2016
* **materialised coverage:** 2016–2025 (10 partitions), 14,731 rows; unavailable: ['2026']
* **notes:** NFL Next Gen Stats weekly player files update nightly in-season per the nflverse schedule, but rows carry no publication timestamp. week == 0 rows are SEASON AGGREGATES and are dropped by the as-of engine.

### `ngs_rushing`

* **loader:** `nflreadpy.load_nextgen_stats(stat_type='rushing')`
* **grain:** player-week
* **join key:** `['season', 'week', 'team']`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 1 day(s) (`conservative_assumption`)
* **earliest valid season:** 2016
* **materialised coverage:** 2016–2025 (10 partitions), 6,059 rows; unavailable: ['2026']
* **notes:** NFL Next Gen Stats weekly player files update nightly in-season per the nflverse schedule, but rows carry no publication timestamp. week == 0 rows are SEASON AGGREGATES and are dropped by the as-of engine.

### `pfr_pass`

* **loader:** `nflreadpy.load_pfr_advstats(stat_type='pass', summary_level='week')`
* **grain:** player-week
* **join key:** `game_id`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 3 day(s) (`conservative_assumption`)
* **earliest valid season:** 2018
* **materialised coverage:** 2018–2025 (8 partitions), 5,424 rows; unavailable: ['2026']
* **notes:** Pro Football Reference advanced (charting) stats. Populated a few days after games and only from 2018. 3 days is the stated project assumption; no publication timestamp exists in the data. Any feature built on this cannot exist before 2018.

### `pfr_rush`

* **loader:** `nflreadpy.load_pfr_advstats(stat_type='rush', summary_level='week')`
* **grain:** player-week
* **join key:** `game_id`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 3 day(s) (`conservative_assumption`)
* **earliest valid season:** 2018
* **materialised coverage:** 2018–2025 (8 partitions), 18,461 rows; unavailable: ['2026']
* **notes:** Pro Football Reference advanced (charting) stats. Populated a few days after games and only from 2018. 3 days is the stated project assumption; no publication timestamp exists in the data. Any feature built on this cannot exist before 2018.

### `pfr_rec`

* **loader:** `nflreadpy.load_pfr_advstats(stat_type='rec', summary_level='week')`
* **grain:** player-week
* **join key:** `game_id`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 3 day(s) (`conservative_assumption`)
* **earliest valid season:** 2018
* **materialised coverage:** 2018–2025 (8 partitions), 35,724 rows; unavailable: ['2026']
* **notes:** Pro Football Reference advanced (charting) stats. Populated a few days after games and only from 2018. 3 days is the stated project assumption; no publication timestamp exists in the data. Any feature built on this cannot exist before 2018.

### `pfr_def`

* **loader:** `nflreadpy.load_pfr_advstats(stat_type='def', summary_level='week')`
* **grain:** player-week
* **join key:** `game_id`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 3 day(s) (`conservative_assumption`)
* **earliest valid season:** 2018
* **materialised coverage:** 2018–2025 (8 partitions), 62,345 rows; unavailable: ['2026']
* **notes:** Pro Football Reference advanced (charting) stats. Populated a few days after games and only from 2018. 3 days is the stated project assumption; no publication timestamp exists in the data. Any feature built on this cannot exist before 2018.

### `injuries`

* **loader:** `nflreadpy.load_injuries()`
* **grain:** player-team-week-report
* **join key:** `['season', 'week', 'team']`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 0 day(s) (`empirical`)
* **earliest valid season:** 2009
* **as-of fallback rule:** `injuries_asof`
* **materialised coverage:** 2013–2025 (13 partitions), 70,936 rows; unavailable: ['2026']
* **notes:** When date_modified is present (2010-2024) it is a real UTC timestamp and is the primary historical as-of filter (date_modified < kickoff_utc). It is ABSENT for the 2025+ / live season, where the conservative fallback rule applies: Thu/Fri/Sat game -> cutoff = kickoff_utc - 24h Sun/Mon/Tue/Wed -> cutoff = 23:59:59 America/New_York of the Saturday before kickoff report_status == null means UNKNOWN, never HEALTHY. Availability signal is built from practice_status + roster status + report_status(when present). Injuries remain an AVAIL-ADJ candidate, NOT a trusted predictive input, until later walk-forward validation.

### `rosters_weekly`

* **loader:** `nflreadpy.load_rosters_weekly()`
* **grain:** player-team-week
* **join key:** `['season', 'week', 'team']`
* **point-in-time status:** `LIVE_SAFE`
* **publish-lag assumption:** 2 day(s) (`conservative_assumption`)
* **earliest valid season:** 2002
* **materialised coverage:** 2013–2025 (13 partitions), 562,246 rows; unavailable: ['2026']
* **notes:** Weekly roster snapshots. Transaction timing is not stamped per row. 2 days is conservative; a mid-week signing may not be reflected until the following weekly file.

### `participation`

* **loader:** `nflreadpy.load_participation()`
* **grain:** play
* **join key:** `nflverse_game_id`
* **point-in-time status:** `POST_SEASON_ONLY`
* **publish-lag assumption:** n/a (`unknown`)
* **earliest valid season:** 2016
* **materialised coverage:** 2016–2025 (10 partitions), 478,989 rows; unavailable: ['2026']
* **notes:** 2016-2022: sparse legacy NGS-derived feed (routes/pressure/coverage < 45% populated; defense_coverage_type 0% in 2016-17). 2023+: complete FTN feed BUT released only after the postseason. Ingested to the canonical layer for future research; the as-of engine REFUSES to serve it into any live or historical prediction frame.

### `schedules`

* **loader:** `nflreadpy.load_schedules()`
* **grain:** game
* **join key:** `game_id`
* **point-in-time status:** `REFERENCE_ONLY`
* **publish-lag assumption:** 0 day(s) (`known`)
* **earliest valid season:** 1999
* **REFERENCE_ONLY columns (stripped before any feature frame):** `away_score`, `home_score`, `result`, `total`, `overtime`, `away_moneyline`, `home_moneyline`, `spread_line`, `away_spread_odds`, `home_spread_odds`, `total_line`, `under_odds`, `over_odds`
* **materialised coverage:** 1999–2026 (28 partitions), 7,548 rows
* **notes:** Fixtures (teams, kickoff, venue, roof, rest) are published months ahead -> LIVE_SAFE and used to build game_calendar. Scores and betting lines are post-hoc / market data and are NEVER admitted to a feature frame (project rule). The as-of engine only ever exposes the fixture columns.

### `players`

* **loader:** `nflreadpy.load_players()`
* **grain:** player
* **join key:** `gsis_id`
* **point-in-time status:** `REFERENCE_ONLY`
* **publish-lag assumption:** 0 day(s) (`known`)
* **materialised coverage:** single file (no season key), 24,826 rows
* **notes:** Slowly-changing identity / crosswalk dimension (names, positions, draft, ID mappings). Used only for player identity resolution, never as a time-varying feature source. NOTE: a player's `status` field is current-state and must not be read as historical.

## Attribution & licensing

All data is retrieved through **nflverse** (`nflreadpy`).

* **nflverse data** is released under **CC-BY-SA 4.0**. Attribute to *nflverse*.
* **Advanced stats** (`pfr_*` sources) are derived from **Pro Football Reference**
  (2018+) and surfaced via nflverse. Attribute to *Pro Football Reference via nflverse*.
* **Next Gen Stats** (`ngs_*`) are **NFL Next Gen Stats**, surfaced via nflverse.
* **Participation** data (2023+) is courtesy of **FTN Data via nflverse**
  (CC-BY-SA 4.0) and is *not* used in the model (POST_SEASON_ONLY).
* **Betting lines / scores** in `schedules` are market / results data and are
  **never** used as model inputs (REFERENCE_ONLY).

This project is independent of any betting model and is not optimized for betting
ROI or agreement with any sportsbook market.
