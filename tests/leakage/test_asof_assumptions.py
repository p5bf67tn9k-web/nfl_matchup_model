"""Phase 0 point-in-time / as-of characterization tests.

These do NOT test model code (none exists yet). They pin the *data assumptions* the
architecture depends on, so that if nflverse changes a schema or a data regime, a
future build breaks loudly here instead of silently leaking or losing coverage.

All are marked `network` (need nflverse downloads; reuse the repo-local cache).
"""
from __future__ import annotations

import nflreadpy as nfl
import polars as pl
import pytest

from matchup.strength.results import latest_completed_week

pytestmark = [pytest.mark.network]


# --------------------------------------------------------------------------- #
# 1. The game calendar: schedules is the as-of anchor and gametime is ET.
# --------------------------------------------------------------------------- #
def test_schedules_have_kickoff_components_and_are_ET():
    """gameday + gametime must parse, and gametime must be Eastern.

    Cross-check: pbp.start_time (local) vs pbp.time_of_day (UTC) for a known game.
    2024_01_ARI_BUF kicked at 13:03 local == 17:03Z  => local is ET (EDT, -4).
    """
    sch = nfl.load_schedules(seasons=[2024])
    assert {"gameday", "gametime"}.issubset(sch.columns)
    parsed = sch.with_columns(
        pl.concat_str([pl.col("gameday"), pl.lit(" "), pl.col("gametime")])
        .str.to_datetime("%Y-%m-%d %H:%M", strict=False, time_zone="America/New_York")
        .alias("kickoff_et")
    )
    # essentially all regular/postseason games have a parseable kickoff
    frac_ok = parsed.get_column("kickoff_et").is_not_null().mean()
    assert frac_ok > 0.98, f"only {frac_ok:.3f} of games have a parseable kickoff"

    pbp = nfl.load_pbp(seasons=[2024]).filter(pl.col("game_id") == "2024_01_ARI_BUF")
    row = pbp.filter(pl.col("time_of_day").is_not_null()).head(1).to_dicts()[0]
    # local start_time hour 13 -> UTC hour 17 (== +4) confirms Eastern daylight time
    utc_hour = int(row["time_of_day"][11:13])
    local_hour = int(row["start_time"].split(", ")[1][:2])
    assert (utc_hour - local_hour) % 24 in (4, 5), (
        f"start_time {row['start_time']} vs time_of_day {row['time_of_day']} not an ET offset"
    )


def test_playoff_weeks_must_be_mapped_via_game_type_not_hardcoded():
    sch = nfl.load_schedules(seasons=[2024])
    gt_by_week = dict(
        sch.filter(pl.col("game_type") != "REG")
        .select("week", "game_type")
        .unique()
        .iter_rows()
    )
    # 18-game era: WC=19, DIV=20, CON=21, SB=22. If this shifts, week hardcoding is unsafe.
    assert gt_by_week.get(19) == "WC"
    assert gt_by_week.get(22) == "SB"
    reg_weeks = sch.filter(pl.col("game_type") == "REG").get_column("week")
    assert reg_weeks.max() == 18


# --------------------------------------------------------------------------- #
# 2. pbp core metrics: coverage and the fields we anchor as-of on.
# --------------------------------------------------------------------------- #
def test_pbp_has_stable_asof_fields_and_core_metric_coverage():
    pbp = nfl.load_pbp(seasons=[2016, 2025])
    for col in ("game_id", "game_date", "season", "week", "posteam", "defteam", "epa"):
        assert col in pbp.columns
    assert pbp.get_column("game_date").null_count() == 0

    # epa defined on the vast majority of rows (non-plays excluded)
    for season in (2016, 2025):
        s = pbp.filter(pl.col("season") == season)
        assert s.get_column("epa").is_not_null().mean() > 0.98

    # cpoe is only partially defined even on pass plays -> downstream must handle nulls
    passes = pbp.filter((pl.col("season") == 2025) & (pl.col("pass") == 1))
    cpoe_cov = passes.get_column("cpoe").is_not_null().mean()
    assert 0.5 < cpoe_cov < 0.95, f"cpoe coverage on pass plays unexpectedly {cpoe_cov:.3f}"


# --------------------------------------------------------------------------- #
# 3. NGS: week==0 is the season aggregate and must be excluded from weekly use.
# --------------------------------------------------------------------------- #
def test_ngs_week_zero_is_season_aggregate():
    ng = nfl.load_nextgen_stats(seasons=[2024], stat_type="passing")
    assert (ng.get_column("week") == 0).any(), "expected week==0 rows in NGS"
    wk0 = ng.filter(pl.col("week") == 0)
    wk_reg = ng.filter(pl.col("week") > 0)
    # a week-0 row's attempts should dwarf any single weekly row for the same player
    top_wk0 = wk0.get_column("attempts").max()
    top_wk = wk_reg.get_column("attempts").max()
    assert top_wk0 > 3 * top_wk, "week==0 does not look like a season aggregate"


# --------------------------------------------------------------------------- #
# 4. Injuries: date_modified is a trustworthy as-of stamp WHEN PRESENT,
#    but it is absent for the current/live season -> a fallback rule is required.
# --------------------------------------------------------------------------- #
def test_injuries_date_modified_precedes_kickoff_when_present():
    inj = nfl.load_injuries(seasons=[2023, 2024])
    sch = nfl.load_schedules(seasons=[2023, 2024])
    team_kick = (
        pl.concat(
            [
                sch.select("season", "week", pl.col("home_team").alias("team"), "gameday", "gametime"),
                sch.select("season", "week", pl.col("away_team").alias("team"), "gameday", "gametime"),
            ]
        )
        .with_columns(
            pl.concat_str([pl.col("gameday"), pl.lit(" "), pl.col("gametime")])
            .str.to_datetime("%Y-%m-%d %H:%M", strict=False, time_zone="America/New_York")
            .alias("kickoff_et")
        )
        .group_by("season", "week", "team")
        .agg(pl.col("kickoff_et").min().alias("kickoff_et"))
    )
    j = (
        inj.join(team_kick, on=["season", "week", "team"], how="left")
        .with_columns(pl.col("date_modified").dt.convert_time_zone("America/New_York").alias("dm_et"))
        .filter(pl.col("date_modified").is_not_null() & pl.col("kickoff_et").is_not_null())
    )
    leak_frac = (j.get_column("dm_et") > j.get_column("kickoff_et")).mean()
    assert leak_frac < 0.001, f"{leak_frac:.4f} of injury rows are stamped after kickoff"


def test_injuries_current_season_has_no_modification_timestamp():
    """Regression guard: if this ever starts passing, the live-season fallback rule
    can be revisited. Today, 2025 injuries have no date_modified."""
    inj = nfl.load_injuries(seasons=[2025])
    # current-season file omits date_modified entirely (or leaves it all-null)
    if "date_modified" not in inj.columns:
        return
    assert inj.get_column("date_modified").is_not_null().mean() < 0.01


# --------------------------------------------------------------------------- #
# 5. Depth charts: the schema regime break at 2025.
# --------------------------------------------------------------------------- #
def test_depth_charts_new_format_has_no_week_key():
    dc = nfl.load_depth_charts(seasons=[2020, 2025])
    old = dc.filter(pl.col("season").is_not_null())
    new = dc.filter(pl.col("season").is_null())
    assert len(old) > 0 and len(new) > 0
    # old format: weekly, no dt
    assert old.get_column("week").is_not_null().mean() > 0.99
    # new format: no season/week, but a dt timestamp we must join on
    assert new.get_column("week").is_null().mean() > 0.99
    assert new.get_column("dt").is_not_null().mean() > 0.99


# --------------------------------------------------------------------------- #
# 6. Participation: data-quality regime break at 2023 + not live-safe.
# --------------------------------------------------------------------------- #
def test_participation_route_coverage_jumps_at_2023():
    pa = nfl.load_participation(seasons=True).with_columns(
        pl.col("nflverse_game_id").str.slice(0, 4).cast(pl.Int32).alias("yr")
    )
    cov = dict(
        pa.group_by("yr")
        .agg((1 - pl.col("route").is_null().mean()).alias("route_cov"))
        .iter_rows()
    )
    assert cov[2021] < 0.6, "pre-2023 participation route coverage unexpectedly high"
    assert cov[2024] > 0.95, "2023+ participation route coverage unexpectedly low"


# --------------------------------------------------------------------------- #
# 7. Join keys we rely on.
# --------------------------------------------------------------------------- #
def test_pfr_advstats_join_on_nflverse_game_id():
    d = nfl.load_pfr_advstats(seasons=[2024], stat_type="def", summary_level="week")
    assert {"game_id", "pfr_player_id", "season", "week", "team", "opponent"}.issubset(d.columns)
    assert d.get_column("game_id").str.contains(r"^\d{4}_\d{2}_[A-Z]{2,3}_[A-Z]{2,3}$").mean() > 0.99


def test_players_crosswalk_pfr_id_partial():
    pls = nfl.load_players()
    assert pls.get_column("gsis_id").is_not_null().mean() > 0.99
    pfr_cov = pls.get_column("pfr_id").is_not_null().mean()
    assert 0.8 < pfr_cov < 0.99, f"pfr_id coverage {pfr_cov:.3f} outside expected band"


# --------------------------------------------------------------------------- #
# 8. Live 2026 pbp must never be ahead of the schedule's own completed-week
#    boundary. Whether the season hasn't started (source raises / returns
#    nothing) or is mid-season (source has real rows), the invariant is the
#    same: no pbp week may exceed `latest_completed_week`, the repository's
#    own point-in-time definition of "actually played" (matchup.strength.
#    results). This stays true regardless of run date or how far the season
#    has progressed -- unlike the old fixed "raises" expectation, which only
#    held before Week 1 kicked off.
# --------------------------------------------------------------------------- #
def test_2026_pbp_never_ahead_of_completed_schedule():
    try:
        pbp = nfl.load_pbp(seasons=[2026])
    except Exception:
        pbp = pl.DataFrame()  # source has nothing published yet -- also safe

    completed_through = latest_completed_week(2026)
    if not pbp.is_empty():
        reg = pbp.filter(pl.col("season_type") == "REG")
        if not reg.is_empty():
            assert reg.get_column("week").max() <= completed_through, (
                "2026 pbp reports a week beyond what the schedule considers "
                "completed -- a future-week leakage source has appeared"
            )

    sch = nfl.load_schedules(seasons=[2026])
    assert len(sch) > 0, "schedule for 2026 should exist even before the season starts"
