"""As-of accessors: the ONLY sanctioned way for downstream code to read source data.

Every accessor:
  * refuses non-admissible sources (POST_SEASON_ONLY / REFERENCE_ONLY / UNKNOWN)
  * strips REFERENCE_ONLY columns
  * drops NGS week==0 season-aggregate rows
  * returns only rows with ``data_asof`` strictly before the target kickoff
  * stamps every row with ``data_asof`` and provenance (``pit_source``, ``pit_status``)
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import polars as pl

from matchup.config import load_publish_lag
from matchup.pointintime.availability import available_asof
from matchup.pointintime.calendar import build_game_calendar, build_team_game_sequence
from matchup.pointintime.status import assert_admissible
from matchup.store import load_source

_NGS_SOURCES = {"ngs_passing", "ngs_receiving", "ngs_rushing"}
_PFR_SOURCES = {"pfr_pass", "pfr_rush", "pfr_rec", "pfr_def"}
_WEEK_TEAM_COL = {
    "player_stats": "team",
    "team_stats": "team",
    "ngs_passing": "team",
    "ngs_receiving": "team",
    "ngs_rushing": "team",
}
# canonical name of the team column in each week-grained source's raw file
_RAW_TEAM_COL = {
    "player_stats": "team",
    "team_stats": "team",
    "ngs_passing": "team_abbr",
    "ngs_receiving": "team_abbr",
    "ngs_rushing": "team_abbr",
}


def _strip_reference_columns(df: pl.DataFrame, source: str) -> pl.DataFrame:
    cfg = load_publish_lag()
    banned = set(cfg.get(source).reference_only_columns) | set(cfg.globally_stripped_columns)
    drop = [c for c in banned if c in df.columns]
    return df.drop(drop) if drop else df


def _drop_ngs_week_zero(df: pl.DataFrame, source: str) -> pl.DataFrame:
    if source in _NGS_SOURCES and "week" in df.columns:
        return df.filter(pl.col("week") > 0)
    return df


def _stamp(df: pl.DataFrame, source: str) -> pl.DataFrame:
    st = load_publish_lag().get(source).point_in_time_status.value
    return df.with_columns(
        pl.lit(source).alias("pit_source"),
        pl.lit(st).alias("pit_status"),
    )


@dataclass
class AsOf:
    """A frozen view of the world as of ``asof_utc``.

    ``mode`` = "backtest" (default) or "live". In "live" mode only LIVE_SAFE
    sources are admissible.

    ``history_seasons`` bounds how many prior seasons of heavy stat frames are
    loaded (default 4 -> the target season plus the 3 completed prior seasons the
    normalization window needs, decision DG). The game calendar / team sequence
    are always full so ``team_game_index`` stays stable.
    """

    asof_utc: datetime
    mode: str = "backtest"
    history_seasons: int = 4

    def __post_init__(self) -> None:
        if self.asof_utc.tzinfo is None:
            raise ValueError("asof_utc must be timezone-aware (UTC)")
        self._calendar = build_game_calendar()
        self._team_seq = build_team_game_sequence()
        target_year = self.asof_utc.year
        # asof in Jan/Feb belongs to the prior league season
        if self.asof_utc.month <= 6:
            target_year -= 1
        self._season_lo = target_year - self.history_seasons
        self._season_hi = target_year
        self._seasons = list(range(self._season_lo, self._season_hi + 1))

    # -- infra views (not feature sources) --------------------------------- #
    @property
    def calendar(self) -> pl.DataFrame:
        return self._calendar

    @property
    def team_sequence(self) -> pl.DataFrame:
        return self._team_seq

    def prior_games(self, team: str) -> pl.DataFrame:
        """This team's games strictly before ``asof_utc``, chronological."""
        return self._team_seq.filter(
            (pl.col("team") == team) & (pl.col("kickoff_utc") < pl.lit(self.asof_utc))
        ).sort("kickoff_utc")

    # -- generic source access ------------------------------------------- #
    def _read(self, source: str) -> pl.DataFrame:
        assert_admissible(source, mode=self.mode)
        raw = load_source(source, seasons=self._seasons)
        if raw.is_empty():
            return raw
        raw = _strip_reference_columns(raw, source)
        raw = _drop_ngs_week_zero(raw, source)
        if source in _RAW_TEAM_COL and _RAW_TEAM_COL[source] != "team":
            raw = raw.rename({_RAW_TEAM_COL[source]: "team"})
        out = available_asof(
            raw, source, self.asof_utc,
            calendar=self._calendar, team_seq=self._team_seq,
            team_col=_WEEK_TEAM_COL.get(source, "team"),
        )
        return _stamp(out, source)

    # -- named accessors ------------------------------------------------- #
    def pbp(self, team: str | None = None) -> pl.DataFrame:
        df = self._read("pbp")
        if team is not None and not df.is_empty():
            df = df.filter((pl.col("posteam") == team) | (pl.col("defteam") == team))
        return df

    def player_week(self, team: str | None = None) -> pl.DataFrame:
        df = self._read("player_stats")
        return df.filter(pl.col("team") == team) if team and not df.is_empty() else df

    def team_week(self, team: str | None = None) -> pl.DataFrame:
        df = self._read("team_stats")
        return df.filter(pl.col("team") == team) if team and not df.is_empty() else df

    def snap_counts(self, team: str | None = None) -> pl.DataFrame:
        df = self._read("snap_counts")
        return df.filter(pl.col("team") == team) if team and not df.is_empty() else df

    def ngs(self, stat_type: str, team: str | None = None) -> pl.DataFrame:
        df = self._read(f"ngs_{stat_type}")
        return df.filter(pl.col("team") == team) if team and not df.is_empty() else df

    def pfr(self, stat_type: str, team: str | None = None) -> pl.DataFrame:
        df = self._read(f"pfr_{stat_type}")
        return df.filter(pl.col("team") == team) if team and not df.is_empty() else df

    def injuries(self, team: str | None = None) -> pl.DataFrame:
        df = self._read("injuries")
        return df.filter(pl.col("team") == team) if team and not df.is_empty() else df

    def rosters(self, team: str | None = None) -> pl.DataFrame:
        df = self._read("rosters_weekly")
        return df.filter(pl.col("team") == team) if team and not df.is_empty() else df


def as_of_for_game(
    game_id: str, *, mode: str = "backtest", history_seasons: int = 4
) -> AsOf:
    cal = build_game_calendar()
    row = cal.filter(pl.col("game_id") == game_id)
    if row.is_empty():
        raise KeyError(f"game_id {game_id!r} not in calendar")
    kickoff = row.get_column("kickoff_utc").item()
    return AsOf(asof_utc=kickoff, mode=mode, history_seasons=history_seasons)


def team_state_asof(
    team: str, season: int, week: int, *, mode: str = "backtest"
) -> dict[str, pl.DataFrame]:
    """Everything the model may know about ``team`` before its (season, week) game.

    Returns a dict of leak-checked frames. Raises if the game is not on the calendar.
    """
    cal = build_game_calendar()
    row = cal.filter(
        (pl.col("season") == season)
        & (pl.col("week") == week)
        & ((pl.col("home_team") == team) | (pl.col("away_team") == team))
    )
    if row.is_empty():
        raise KeyError(f"{team} has no game in {season} week {week}")
    kickoff = row.get_column("kickoff_utc").item()
    game_id = row.get_column("game_id").item()

    ao = AsOf(asof_utc=kickoff, mode=mode)
    frames = {
        "prior_games": ao.prior_games(team),
        "pbp": ao.pbp(team),
        "player_week": ao.player_week(team),
        "team_week": ao.team_week(team),
        "snap_counts": ao.snap_counts(team),
        "ngs_passing": ao.ngs("passing", team),
        "ngs_receiving": ao.ngs("receiving", team),
        "ngs_rushing": ao.ngs("rushing", team),
        "pfr_pass": ao.pfr("pass", team),
        "pfr_def": ao.pfr("def", team),
        "injuries": ao.injuries(team),
        "rosters": ao.rosters(team),
    }

    # -- coverage metadata (decision DC) ---------------------------------- #
    stat_sources = [k for k in frames if k != "prior_games"]
    seasons_seen: set[int] = set()
    have_target, missing_target = [], []
    for name in stat_sources:
        f = frames[name]
        if "season" in f.columns and f.height:
            ss = set(f.get_column("season").drop_nulls().to_list())
            seasons_seen |= ss
            (have_target if season in ss else missing_target).append(name)
        else:
            missing_target.append(name)

    priors_only = len(have_target) == 0
    coverage = {
        "mode": mode,
        "target_season": season,
        "target_week": week,
        "priors_only": priors_only,
        "low_confidence": bool(priors_only or week <= 4),
        "prior_seasons_supplying_data": sorted(seasons_seen),
        "sources_with_target_season_data": sorted(have_target),
        "sources_without_target_season_data": sorted(missing_target),
        "history_window": [ao._season_lo, ao._season_hi],
    }

    return {
        "target_game_id": game_id,
        "target_kickoff_utc": kickoff,
        "coverage": coverage,
        **frames,
    }
