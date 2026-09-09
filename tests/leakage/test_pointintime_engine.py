"""Phase 1 model-level leakage suite (acceptance criterion 2).

Covers:
  * data_asof < kickoff_utc for every row of every as-of accessor
  * poisoned future-row canary
  * bye-week rolling correctness
  * playoff ordering
  * NGS week==0 exclusion
  * REFERENCE_ONLY (Vegas line / score) exclusion
  * point-in-time status enforcement
"""
from __future__ import annotations

import polars as pl
import pytest

from matchup.config import load_publish_lag
from matchup.pointintime.asof import AsOf, team_state_asof
from matchup.pointintime.calendar import build_game_calendar, build_team_game_sequence
from matchup.pointintime.status import PointInTimeViolation
from matchup.store import clear_cache

pytestmark = [pytest.mark.network]

# (team, season, week) -- non-bye games spanning early season, midseason, playoffs
SAMPLE_GAMES = [
    ("KC", 2024, 7),    # KC week 6 bye -> tests the bye
    ("PHI", 2023, 1),   # season opener: no in-season prior games
    ("SF", 2022, 20),   # divisional round
    ("BUF", 2021, 5),
    ("DET", 2024, 14),
]

_STAT_ACCESSORS = [
    "pbp", "player_week", "team_week", "snap_counts",
    "ngs_passing", "ngs_receiving", "ngs_rushing",
    "pfr_pass", "pfr_def", "injuries", "rosters",
]


@pytest.fixture(autouse=True)
def _clean():
    clear_cache()
    yield
    clear_cache()


@pytest.mark.parametrize(("team", "season", "week"), SAMPLE_GAMES)
def test_no_row_is_dated_at_or_after_target_kickoff(team, season, week):
    st = team_state_asof(team, season, week)
    kickoff = st["target_kickoff_utc"]
    offenders = {}
    for name, frame in st.items():
        if isinstance(frame, pl.DataFrame) and "data_asof" in frame.columns and frame.height:
            n = frame.filter(pl.col("data_asof") >= pl.lit(kickoff)).height
            if n:
                offenders[name] = n
    assert not offenders, f"{team} {season} wk{week}: rows dated >= kickoff: {offenders}"


@pytest.mark.parametrize(("team", "season", "week"), SAMPLE_GAMES)
def test_every_stat_frame_carries_provenance(team, season, week):
    st = team_state_asof(team, season, week)
    for name in ("pbp", "snap_counts", "ngs_passing", "injuries"):
        f = st[name]
        if f.height:
            assert {"data_asof", "pit_source", "pit_status"}.issubset(f.columns)
            assert (f.get_column("pit_status") == "LIVE_SAFE").all()


def test_current_season_slice_stops_before_the_bye_and_target():
    # KC 2024: week 6 bye, week 7 target -> in-season prior data is weeks 1-5 only
    st = team_state_asof("KC", 2024, 7)
    for name in ("pbp", "snap_counts", "ngs_passing", "player_week", "pfr_def"):
        f = st[name].filter(pl.col("season") == 2024)
        weeks = set(f.get_column("week").to_list())
        assert weeks == {1, 2, 3, 4, 5}, f"{name}: {sorted(weeks)}"
    # the injury report for the target week 7 IS knowable pre-kickoff
    inj_weeks = set(st["injuries"].filter(pl.col("season") == 2024).get_column("week").to_list())
    assert 7 in inj_weeks and 6 not in inj_weeks


def test_bye_week_rolling_uses_game_sequence_not_week_arithmetic():
    seq = build_team_game_sequence().filter(
        (pl.col("team") == "KC") & (pl.col("season") == 2024)
    ).sort("kickoff_utc")
    weeks = seq.get_column("week").to_list()
    idx = seq.get_column("team_game_index_season").to_list()
    assert weeks[:7] == [1, 2, 3, 4, 5, 7, 8], "expected a week-6 bye gap"
    assert idx == list(range(len(idx))), "season game index must be contiguous across the bye"

    # 'last 3 games' before the week-7 game = weeks 3,4,5 (spanning the bye)
    st = team_state_asof("KC", 2024, 7)
    prior = st["prior_games"].filter(pl.col("season") == 2024).sort("kickoff_utc")
    assert prior.get_column("week").to_list()[-3:] == [3, 4, 5]


def test_playoff_games_sort_after_regular_season():
    cal = build_game_calendar().filter(pl.col("season") == 2023)
    reg_max = cal.filter(pl.col("game_type") == "REG").get_column("kickoff_utc").max()
    post_min = cal.filter(pl.col("game_type") != "REG").get_column("kickoff_utc").min()
    assert post_min > reg_max

    # a divisional-round as-of view sees the full 18-game regular season
    st = team_state_asof("SF", 2022, 20)
    reg = st["prior_games"].filter(
        (pl.col("season") == 2022) & (pl.col("game_type") == "REG")
    )
    assert reg.height == 17  # SF played 17 regular-season games (17-game season, 1 bye)


def _kickoff(team: str, season: int, week: int):
    return (
        build_game_calendar()
        .filter(
            (pl.col("season") == season)
            & (pl.col("week") == week)
            & ((pl.col("home_team") == team) | (pl.col("away_team") == team))
        )
        .get_column("kickoff_utc")
        .item()
    )


def test_ngs_week_zero_never_returned():
    ao = AsOf(asof_utc=_kickoff("KC", 2024, 10))
    for stat in ("passing", "receiving", "rushing"):
        f = ao.ngs(stat)
        if f.height:
            assert (f.get_column("week") > 0).all()


def test_reference_only_and_market_columns_never_reach_a_feature_frame():
    cfg = load_publish_lag()
    banned = set(cfg.get("schedules").reference_only_columns) | set(cfg.globally_stripped_columns)
    # the specific pbp leak vectors Phase 1 discovered
    banned |= {"home_score", "away_score", "result", "total", "spread_line", "total_line",
               "vegas_wp", "vegas_home_wp", "vegas_wpa", "vegas_home_wpa"}
    st = team_state_asof("DET", 2024, 14)
    for name, f in st.items():
        if isinstance(f, pl.DataFrame):
            leaked = banned.intersection(f.columns)
            assert not leaked, f"{name} leaked banned columns {sorted(leaked)}"
    assert not banned.intersection(build_game_calendar().columns)


def test_point_in_time_status_enforcement():
    kickoff = _kickoff("KC", 2024, 10)
    ao = AsOf(asof_utc=kickoff, mode="backtest")
    for blocked in ("participation", "players", "schedules"):
        with pytest.raises(PointInTimeViolation):
            ao._read(blocked)

    # live mode is at least as strict as backtest
    ao_live = AsOf(asof_utc=kickoff, mode="live")
    for blocked in ("participation", "players", "schedules"):
        with pytest.raises(PointInTimeViolation):
            ao_live._read(blocked)


def test_poisoned_future_row_canary(monkeypatch):
    """Injecting a fabricated future game + future-dated plays must not change any
    as-of result for an earlier game."""
    from matchup import store

    baseline = team_state_asof("KC", 2024, 7)
    base_hashes = {
        k: v.hash_rows().sum()
        for k, v in baseline.items()
        if isinstance(v, pl.DataFrame) and v.height
    }

    real_load = store.load_source.__wrapped__ if hasattr(store.load_source, "__wrapped__") else store.load_source

    def poisoned_load(source, seasons=None, columns=None, use_cache=True):
        df = real_load(source, seasons=seasons, columns=columns, use_cache=False)
        if df.is_empty():
            return df
        if source == "schedules":
            poison = df.filter(pl.col("game_id") == "2024_07_KC_SF").with_columns(
                pl.lit("2024_99_KC_SF").alias("game_id"),
                pl.lit(99).alias("week"),
                pl.lit("2024-12-25").alias("gameday"),
            )
            return pl.concat([df, poison], how="diagonal_relaxed")
        if source == "pbp":
            poison = df.filter(pl.col("game_id") == "2024_05_KC_NO").with_columns(
                pl.lit("2024_99_KC_SF").alias("game_id"),
                pl.lit(99).alias("week"),
                pl.lit("2024-12-25").alias("game_date"),
            )
            return pl.concat([df, poison], how="diagonal_relaxed")
        return df

    clear_cache()
    monkeypatch.setattr(store, "load_source", poisoned_load)
    # calendar/asof import load_source by name from the module, so patch there too
    monkeypatch.setattr("matchup.pointintime.calendar.load_source", poisoned_load)
    monkeypatch.setattr("matchup.pointintime.asof.load_source", poisoned_load)

    poisoned = team_state_asof("KC", 2024, 7)
    for k, h in base_hashes.items():
        pv = poisoned[k]
        assert pv.hash_rows().sum() == h, f"{k} changed after injecting a future game"
