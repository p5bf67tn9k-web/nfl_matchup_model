"""Phase 0 targeted probes (READ-ONLY). Plain-text output only."""
from pathlib import Path

import nflreadpy as nfl
import polars as pl
from nflreadpy.config import update_config

ROOT = Path(__file__).resolve().parents[1]
update_config(cache_mode="filesystem", cache_dir=Path(ROOT / "data/raw/nflreadpy_cache"),
              cache_duration=7 * 86400, verbose=False)


def kv(d):
    for k, v in d.items():
        print(f"    {k}: {v}")


print("=" * 30, "DEPTH CHARTS", "=" * 30)
dc = nfl.load_depth_charts(seasons=[2016, 2020, 2024, 2025])
print("rows:", len(dc))
print("season counts:", dict(dc.group_by("season").len().sort("season").iter_rows()))
ns = dc.filter(pl.col("season").is_null())
nn = dc.filter(pl.col("season").is_not_null())
print("NULL-season rows:", len(ns))
print("  dt non-null:", ns.get_column("dt").drop_nulls().len(), "of", len(ns))
print("  dt min/max:", ns.get_column("dt").drop_nulls().min(), "/", ns.get_column("dt").drop_nulls().max())
print("  week non-null frac:", round(ns.get_column("week").drop_nulls().len() / len(ns), 3))
print("  game_type values:", ns.get_column("game_type").value_counts().sort("count", descending=True).head(6).to_dicts())
print("  sample null-season row:")
kv(ns.select("season", "week", "game_type", "dt", "club_code", "team", "full_name", "position",
             "depth_position", "pos_abb", "pos_rank", "formation").head(1).to_dicts()[0])
print("  OLD-format (non-null season) sample:")
kv(nn.select("season", "week", "game_type", "dt", "club_code", "team", "full_name", "position",
             "depth_position", "pos_abb", "pos_rank", "formation").head(1).to_dicts()[0])
print("  non-null-season 'dt' non-null frac:", round(nn.get_column("dt").drop_nulls().len() / len(nn), 3))

print("\n" + "=" * 30, "PARTICIPATION", "=" * 30)
pa = nfl.load_participation(seasons=True)
pa = pa.with_columns(pl.col("nflverse_game_id").str.slice(0, 4).cast(pl.Int32).alias("yr"))
print("year counts:", dict(pa.group_by("yr").len().sort("yr").iter_rows()))
print("was_pressure null frac:", round(pa.get_column("was_pressure").null_count() / len(pa), 3))
print("route null frac:", round(pa.get_column("route").null_count() / len(pa), 3))
print("defense_coverage_type null frac:", round(pa.get_column("defense_coverage_type").null_count() / len(pa), 3))
print("sample row:")
kv(pa.select("nflverse_game_id", "play_id", "possession_team", "offense_personnel",
             "number_of_pass_rushers", "was_pressure", "route", "defense_man_zone_type",
             "defense_coverage_type").head(1).to_dicts()[0])

print("\n" + "=" * 30, "INJURIES", "=" * 30)
inj = nfl.load_injuries(seasons=True)
rep = inj.group_by("season").agg(
    pl.len().alias("rows"),
    pl.col("date_modified").is_null().mean().round(3).alias("dm_null"),
    pl.col("report_status").is_null().mean().round(3).alias("rep_status_null"),
).sort("season")
for r in rep.iter_rows(named=True):
    print("  ", r)
print("report_status values:", inj.get_column("report_status").value_counts().sort("count", descending=True).to_dicts())
print("practice_status values:", inj.get_column("practice_status").value_counts().sort("count", descending=True).head(8).to_dicts())
print("sample rows:")
for row in inj.filter(pl.col("season") == 2024).select(
        "season", "week", "gsis_id", "report_primary_injury", "report_status",
        "practice_status", "date_modified").head(4).to_dicts():
    print("  ", row)

print("\n" + "=" * 30, "SCHEDULES", "=" * 30)
sc = nfl.load_schedules(seasons=[2016, 2020, 2024, 2025, 2026])
rep = sc.group_by("season").agg(
    pl.len().alias("g"),
    pl.col("spread_line").is_null().mean().round(3).alias("spread_null"),
    pl.col("total_line").is_null().mean().round(3).alias("total_null"),
    pl.col("gametime").is_null().mean().round(3).alias("gametime_null"),
    pl.col("temp").is_null().mean().round(3).alias("temp_null"),
    pl.col("home_score").is_null().mean().round(3).alias("score_null"),
).sort("season")
for r in rep.iter_rows(named=True):
    print("  ", r)
print("2026 week-1 sample:")
for row in sc.filter((pl.col("season") == 2026) & (pl.col("week") == 1)).select(
        "game_id", "gameday", "gametime", "weekday", "away_team", "home_team",
        "spread_line", "total_line", "away_qb_name", "home_qb_name").head(4).to_dicts():
    print("  ", row)

print("\n" + "=" * 30, "NGS WEEK SEMANTICS", "=" * 30)
ng = nfl.load_nextgen_stats(seasons=[2024], stat_type="passing")
print("2024 week counts:", dict(ng.group_by("week").len().sort("week").iter_rows()))
print("week0 count:", len(ng.filter(pl.col("week") == 0)))
print("season_type values:", ng.get_column("season_type").value_counts().to_dicts())
print("week0 sample:")
kv(ng.filter(pl.col("week") == 0).select(
    "player_display_name", "season", "week", "season_type", "attempts", "pass_yards").head(1).to_dicts()[0])
print("week1 sample:")
kv(ng.filter(pl.col("week") == 1).select(
    "player_display_name", "season", "week", "season_type", "attempts", "pass_yards").head(1).to_dicts()[0])

print("\n" + "=" * 30, "PBP AS-OF FIELDS", "=" * 30)
pbp = nfl.load_pbp(seasons=[2024])
for row in pbp.select("game_id", "game_date", "start_time", "time_of_day", "week",
                      "home_team", "away_team").head(3).to_dicts():
    print("  ", row)
print("game_date dtype:", pbp.schema["game_date"], "| null frac:",
      round(pbp.get_column("game_date").null_count() / len(pbp), 4))
print("time_of_day null frac:", round(pbp.get_column("time_of_day").null_count() / len(pbp), 4))
