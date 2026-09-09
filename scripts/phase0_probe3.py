"""Phase 0 probe batch 3: 2026 live-season readiness + participation-by-season columns."""
from pathlib import Path

import nflreadpy as nfl
import polars as pl
from nflreadpy.config import update_config

ROOT = Path(__file__).resolve().parents[1]
update_config(cache_mode="filesystem", cache_dir=Path(ROOT / "data/raw/nflreadpy_cache"),
              cache_duration=7 * 86400, verbose=False)

print("=" * 25, "2026 LIVE-SEASON DATA AVAILABILITY (run date 2026-09-08)", "=" * 25)
for name, fn, kw in [
    ("pbp", nfl.load_pbp, {}),
    ("player_stats", nfl.load_player_stats, {"summary_level": "week"}),
    ("snap_counts", nfl.load_snap_counts, {}),
    ("ngs_passing", nfl.load_nextgen_stats, {"stat_type": "passing"}),
    ("pfr_pass", nfl.load_pfr_advstats, {"stat_type": "pass", "summary_level": "week"}),
    ("injuries", nfl.load_injuries, {}),
    ("depth_charts", nfl.load_depth_charts, {}),
    ("rosters_weekly", nfl.load_rosters_weekly, {}),
    ("ftn_charting", nfl.load_ftn_charting, {}),
    ("participation", nfl.load_participation, {}),
]:
    try:
        df = fn(seasons=[2026], **kw)
        wk = sorted(set(df.get_column("week").drop_nulls().to_list())) if "week" in df.columns else "n/a"
        print(f"  {name:14s} rows={len(df):>7}  weeks={wk}")
    except Exception as e:  # noqa: BLE001
        print(f"  {name:14s} ERROR: {type(e).__name__}: {e}")

print("\n" + "=" * 25, "PARTICIPATION: key-field non-null frac by season", "=" * 25)
pa = nfl.load_participation(seasons=True).with_columns(
    pl.col("nflverse_game_id").str.slice(0, 4).cast(pl.Int32).alias("yr"))
fields = ["offense_personnel", "defenders_in_box", "number_of_pass_rushers",
          "was_pressure", "route", "time_to_throw", "defense_man_zone_type", "defense_coverage_type"]
out = pa.group_by("yr").agg(
    [pl.len().alias("rows")] + [(1 - pl.col(f).is_null().mean()).round(3).alias(f) for f in fields]
).sort("yr")
for r in out.iter_rows(named=True):
    print("  ", r)

print("\n" + "=" * 25, "INJURIES: does any row have date_modified AFTER its game kickoff?", "=" * 25)
inj = nfl.load_injuries(seasons=[2022, 2023, 2024])
sch = nfl.load_schedules(seasons=[2022, 2023, 2024]).select(
    "season", "week", "home_team", "away_team", "gameday", "gametime")
# build a naive game-week earliest kickoff per (season, week, team)
long = pl.concat([
    sch.select("season", "week", pl.col("home_team").alias("team"), "gameday", "gametime"),
    sch.select("season", "week", pl.col("away_team").alias("team"), "gameday", "gametime"),
]).with_columns(
    pl.concat_str([pl.col("gameday"), pl.lit(" "), pl.col("gametime")])
    .str.to_datetime("%Y-%m-%d %H:%M", strict=False, time_zone="America/New_York")
    .alias("kickoff_et")
).group_by("season", "week", "team").agg(pl.col("kickoff_et").min().alias("kickoff_et"))
j = inj.join(long, on=["season", "week", "team"], how="left")
j = j.with_columns(pl.col("date_modified").dt.convert_time_zone("America/New_York").alias("dm_et"))
tot = j.filter(pl.col("date_modified").is_not_null() & pl.col("kickoff_et").is_not_null())
after = tot.filter(pl.col("dm_et") > pl.col("kickoff_et"))
print(f"  rows with both timestamps: {len(tot)}")
print(f"  rows where date_modified > kickoff (LEAKAGE if used naively): {len(after)} "
      f"({round(100*len(after)/max(len(tot),1),2)}%)")
print("  examples:")
for r in after.select("season", "week", "team", "gsis_id", "report_status", "dm_et", "kickoff_et").head(5).to_dicts():
    print("   ", r)
