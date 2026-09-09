"""Phase 0 probe batch 2: core metric null rates + join keys (READ-ONLY)."""
from pathlib import Path

import nflreadpy as nfl
import polars as pl
from nflreadpy.config import update_config

ROOT = Path(__file__).resolve().parents[1]
update_config(cache_mode="filesystem", cache_dir=Path(ROOT / "data/raw/nflreadpy_cache"),
              cache_duration=7 * 86400, verbose=False)


def nullrates(df, cols, by="season"):
    present = [c for c in cols if c in df.columns]
    missing = [c for c in cols if c not in df.columns]
    agg = [pl.len().alias("rows")] + [pl.col(c).is_null().mean().round(3).alias(c) for c in present]
    out = df.group_by(by).agg(agg).sort(by)
    for r in out.iter_rows(named=True):
        print("  ", r)
    if missing:
        print("   MISSING COLUMNS:", missing)


print("=" * 25, "PBP core metric null rates by season", "=" * 25)
pbp = nfl.load_pbp(seasons=[2016, 2020, 2024, 2025])
nullrates(pbp, ["epa", "cpoe", "success", "qb_dropback", "qb_epa", "air_yards",
                "yards_after_catch", "qb_hit", "sack", "pass_oe", "xpass",
                "passer_player_id", "rusher_player_id", "receiver_player_id"])
print("pass plays only - cpoe null:")
nullrates(pbp.filter(pl.col("pass") == 1), ["cpoe", "air_yards"])

print("\n" + "=" * 25, "SNAP COUNTS", "=" * 25)
sc = nfl.load_snap_counts(seasons=[2016, 2024, 2025])
nullrates(sc, ["game_id", "pfr_player_id", "player", "position", "offense_snaps",
               "offense_pct", "defense_snaps", "defense_pct", "team"])
print("  cols:", sc.columns)
print("  sample:", sc.head(2).to_dicts())

print("\n" + "=" * 25, "PFR ADVSTATS join keys", "=" * 25)
for st in ["pass", "def"]:
    d = nfl.load_pfr_advstats(seasons=[2024], stat_type=st, summary_level="week")
    idcols = [c for c in d.columns if "id" in c.lower() or c in ("pfr_id", "gsis_id")]
    print(f"  {st}: id-ish cols = {idcols}")
    print(f"  {st}: cols = {d.columns}")
    print(f"  {st}: sample = {d.select(idcols + ['season','week']).head(2).to_dicts()}")

print("\n" + "=" * 25, "PLAYERS crosswalk", "=" * 25)
pls = nfl.load_players()
idc = [c for c in pls.columns if c.endswith("_id") or c.endswith("_gsis_id")]
print("  id cols:", idc)
sub = pls.select([c for c in ["gsis_id", "pfr_id", "esb_id", "espn_id", "position",
                              "status", "display_name"] if c in pls.columns])
print("  non-null frac:")
for c in sub.columns:
    print(f"    {c}: {round(1 - sub.get_column(c).null_count()/len(sub), 3)}")

print("\n" + "=" * 25, "NGS join key", "=" * 25)
ng = nfl.load_nextgen_stats(seasons=[2024], stat_type="passing")
print("  id cols:", [c for c in ng.columns if "id" in c.lower()])
print("  player_gsis_id null frac:", round(ng.get_column("player_gsis_id").null_count()/len(ng), 3))

print("\n" + "=" * 25, "PBP playoff week numbering vs schedules", "=" * 25)
sch = nfl.load_schedules(seasons=[2024])
print("  2024 weeks in schedule:", sorted(set(sch.get_column("week").to_list())))
print("  2024 game_type x week:")
for r in sch.group_by("game_type", "week").len().sort("week").iter_rows(named=True):
    print("   ", r)
