"""Phase 0 data-source & metric availability audit (READ-ONLY).

Pulls sample seasons from nflreadpy and records, for each source:
  - season / week coverage actually returned
  - row counts per sampled season
  - full column list + dtypes
  - null rates for a curated set of key fields
  - candidate date/time columns (for the point-in-time / as-of framework)

Writes:
  outputs/phase0/<source>.schema.json      full schema + profile per source
  outputs/phase0/summary.csv               one row per (source, season)
  outputs/phase0/keyfield_nulls.csv        null rates for key fields
  outputs/phase0/datecols.csv              candidate as-of columns per source

Nothing here builds ratings, matchups, or predictions.
"""

from __future__ import annotations

import json
import traceback
from datetime import date, datetime
from importlib.metadata import version as _pkg_version
from pathlib import Path

import nflreadpy as nfl
import polars as pl
from nflreadpy.config import update_config

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "phase0"
OUT.mkdir(parents=True, exist_ok=True)

update_config(
    cache_mode="filesystem",
    cache_dir=Path(ROOT / "data" / "raw" / "nflreadpy_cache"),
    cache_duration=7 * 86400,
    verbose=True,
)

# (name, callable, kwargs, sample_seasons)
SAMPLES_MAIN = [2016, 2020, 2024, 2025]
JOBS: list[tuple[str, object, dict, list[int]]] = [
    ("pbp", nfl.load_pbp, {}, SAMPLES_MAIN),
    ("player_stats_week", nfl.load_player_stats, {"summary_level": "week"}, SAMPLES_MAIN),
    ("team_stats_week", nfl.load_team_stats, {"summary_level": "week"}, SAMPLES_MAIN),
    ("snap_counts", nfl.load_snap_counts, {}, SAMPLES_MAIN),
    ("ngs_passing", nfl.load_nextgen_stats, {"stat_type": "passing"}, SAMPLES_MAIN),
    ("ngs_receiving", nfl.load_nextgen_stats, {"stat_type": "receiving"}, SAMPLES_MAIN),
    ("ngs_rushing", nfl.load_nextgen_stats, {"stat_type": "rushing"}, SAMPLES_MAIN),
    ("pfr_pass", nfl.load_pfr_advstats, {"stat_type": "pass", "summary_level": "week"}, [2018, 2020, 2024, 2025]),
    ("pfr_rush", nfl.load_pfr_advstats, {"stat_type": "rush", "summary_level": "week"}, [2018, 2024, 2025]),
    ("pfr_rec", nfl.load_pfr_advstats, {"stat_type": "rec", "summary_level": "week"}, [2018, 2024, 2025]),
    ("pfr_def", nfl.load_pfr_advstats, {"stat_type": "def", "summary_level": "week"}, [2018, 2024, 2025]),
    ("injuries", nfl.load_injuries, {}, [2016, 2020, 2024, 2025]),
    ("depth_charts", nfl.load_depth_charts, {}, [2016, 2020, 2024, 2025]),
    ("rosters_weekly", nfl.load_rosters_weekly, {}, [2016, 2020, 2024, 2025]),
    ("schedules", nfl.load_schedules, {}, None),  # loads all
    ("participation", nfl.load_participation, {}, [2016, 2019, 2022, 2023, 2024, 2025]),
    ("ftn_charting", nfl.load_ftn_charting, {}, [2022, 2024, 2025]),
    ("players", nfl.load_players, {}, None),
]

KEY_FIELDS: dict[str, list[str]] = {
    "pbp": ["game_id", "game_date", "season", "week", "posteam", "defteam", "epa", "cpoe",
            "success", "pass", "rush", "qb_dropback", "sack", "qb_hit", "air_yards",
            "yards_after_catch", "passer_player_id", "rusher_player_id", "receiver_player_id",
            "start_time", "time_of_day"],
    "player_stats_week": ["player_id", "season", "week", "position", "passing_epa", "attempts",
                          "targets", "carries", "target_share", "air_yards_share"],
    "team_stats_week": ["team", "season", "week"],
    "snap_counts": ["game_id", "pfr_game_id", "season", "week", "player", "pfr_player_id",
                    "position", "offense_snaps", "offense_pct", "defense_snaps", "defense_pct"],
    "ngs_passing": ["player_gsis_id", "season", "week", "avg_time_to_throw",
                    "completion_percentage_above_expectation", "aggressiveness"],
    "ngs_receiving": ["player_gsis_id", "season", "week", "avg_separation", "avg_cushion",
                      "avg_yac_above_expectation"],
    "ngs_rushing": ["player_gsis_id", "season", "week", "rush_yards_over_expected",
                    "efficiency", "percent_attempts_gte_eight_defenders"],
    "pfr_pass": ["pfr_id", "season", "week", "times_pressured", "times_pressured_pct",
                 "times_hurried", "times_hit", "times_blitzed", "on_tgt_pct", "bad_throw_pct"],
    "pfr_rush": ["pfr_id", "season", "week", "ybc_att", "yac_att", "brk_tkl"],
    "pfr_rec": ["pfr_id", "season", "week", "ybc_r", "yac_r", "drop_pct", "adot"],
    "pfr_def": ["pfr_id", "season", "week", "tgt", "cmp", "yds", "rat", "m_tkl", "prss", "sk"],
    "injuries": ["season", "week", "gsis_id", "report_primary_injury", "report_status",
                 "practice_status", "date_modified"],
    "depth_charts": ["season", "week", "gsis_id", "position", "depth_team", "formation",
                     "depth_position", "dt"],
    "rosters_weekly": ["season", "week", "gsis_id", "status", "position", "depth_chart_position",
                       "game_type"],
    "schedules": ["game_id", "season", "week", "gameday", "gametime", "weekday", "home_team",
                  "away_team", "home_score", "away_score", "result", "spread_line", "total_line",
                  "roof", "surface", "away_rest", "home_rest"],
    "participation": ["nflverse_game_id", "season", "week", "play_id", "offense_formation",
                      "offense_personnel", "defenders_in_box", "number_of_pass_rushers",
                      "offense_players", "defense_players"],
    "ftn_charting": ["nflverse_game_id", "season", "week", "n_offense_backfield",
                     "n_pass_rushers", "is_play_action", "is_screen_pass", "is_rpo"],
    "players": ["gsis_id", "pfr_id", "position", "status"],
}

DATE_HINTS = ("date", "time", "day", "dt", "modified", "updated", "created", "timestamp", "kickoff")


def profile_frame(name: str, df: pl.DataFrame, seasons_req) -> dict:
    cols = df.columns
    schema = {c: str(dt) for c, dt in df.schema.items()}

    # season / week coverage
    cov: dict = {}
    if "season" in cols:
        s = df.get_column("season").drop_nulls()
        cov["season_min"] = int(s.min()) if len(s) else None
        cov["season_max"] = int(s.max()) if len(s) else None
    if "week" in cols:
        w = df.get_column("week").drop_nulls()
        cov["week_min"] = int(w.min()) if len(w) else None
        cov["week_max"] = int(w.max()) if len(w) else None
        cov["has_week_zero"] = bool((df.get_column("week") == 0).any())

    # per-season row counts
    per_season = {}
    if "season" in cols:
        g = df.drop_nulls("season").group_by("season").len().sort("season")
        for row in g.iter_rows(named=True):
            per_season[int(row["season"])] = int(row["len"])
        n_null_season = int(df.get_column("season").is_null().sum())
        if n_null_season:
            per_season["_null_season_rows"] = n_null_season

    # candidate as-of columns
    date_cols = {}
    for c in cols:
        lc = c.lower()
        if any(h in lc for h in DATE_HINTS):
            col = df.get_column(c)
            non_null = int(col.drop_nulls().len())
            sample = col.drop_nulls().head(3).to_list()
            date_cols[c] = {
                "dtype": str(col.dtype),
                "non_null": non_null,
                "null_pct": round(100 * (1 - non_null / max(len(df), 1)), 2),
                "sample": [str(x) for x in sample],
            }

    # key-field null rates
    kf = {}
    for f in KEY_FIELDS.get(name, []):
        if f in cols:
            col = df.get_column(f)
            nn = int(col.drop_nulls().len())
            kf[f] = {"present": True, "null_pct": round(100 * (1 - nn / max(len(df), 1)), 2)}
        else:
            kf[f] = {"present": False, "null_pct": None}

    return {
        "source": name,
        "seasons_requested": seasons_req,
        "n_rows": len(df),
        "n_cols": len(cols),
        "coverage": cov,
        "rows_per_season": per_season,
        "columns": cols,
        "schema": schema,
        "candidate_asof_columns": date_cols,
        "key_fields": kf,
    }


def main() -> None:
    summary_rows = []
    keyfield_rows = []
    datecol_rows = []
    errors = {}

    for name, fn, kwargs, seasons in JOBS:
        print(f"\n=== {name} ===", flush=True)
        try:
            if name == "players":
                df = fn(**kwargs)
            elif seasons is None:
                df = fn(seasons=True, **kwargs)
            else:
                df = fn(seasons=seasons, **kwargs)
            prof = profile_frame(name, df, seasons)
            (OUT / f"{name}.schema.json").write_text(json.dumps(prof, indent=2, default=str))

            for season, cnt in (prof["rows_per_season"] or {name: prof["n_rows"]}).items():
                summary_rows.append({
                    "source": name, "season": season, "rows": cnt,
                    "n_cols": prof["n_cols"],
                    "season_min": prof["coverage"].get("season_min"),
                    "season_max": prof["coverage"].get("season_max"),
                    "week_min": prof["coverage"].get("week_min"),
                    "week_max": prof["coverage"].get("week_max"),
                    "has_week_zero": prof["coverage"].get("has_week_zero"),
                })
            for f, meta in prof["key_fields"].items():
                keyfield_rows.append({"source": name, "field": f, **meta})
            for c, meta in prof["candidate_asof_columns"].items():
                datecol_rows.append({"source": name, "column": c, "dtype": meta["dtype"],
                                     "null_pct": meta["null_pct"], "sample": " | ".join(meta["sample"])})
            print(f"  rows={prof['n_rows']:,} cols={prof['n_cols']} "
                  f"seasons={prof['coverage'].get('season_min')}-{prof['coverage'].get('season_max')} "
                  f"weeks={prof['coverage'].get('week_min')}-{prof['coverage'].get('week_max')} "
                  f"wk0={prof['coverage'].get('has_week_zero')}")
        except Exception as e:  # noqa: BLE001
            errors[name] = f"{type(e).__name__}: {e}"
            print(f"  ERROR: {e}")
            traceback.print_exc()

    if summary_rows:
        pl.DataFrame(summary_rows).sort(["source", "season"]).write_csv(OUT / "summary.csv")
    if keyfield_rows:
        pl.DataFrame(keyfield_rows).write_csv(OUT / "keyfield_nulls.csv")
    if datecol_rows:
        pl.DataFrame(datecol_rows).write_csv(OUT / "datecols.csv")

    meta = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "run_date": date.today().isoformat(),
        "nflreadpy_version": _pkg_version("nflreadpy"),
        "polars_version": pl.__version__,
        "current_season_season_logic": nfl.get_current_season(),
        "current_season_roster_logic": nfl.get_current_season(roster=True),
        "errors": errors,
    }
    (OUT / "run_meta.json").write_text(json.dumps(meta, indent=2, default=str))
    print("\n\nDONE. meta:", json.dumps(meta, indent=2, default=str))


if __name__ == "__main__":
    main()
