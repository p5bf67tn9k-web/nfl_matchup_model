"""Data-loading and data-shaping layer for matchup cards.

Every number in a matchup card traces back to an existing column in one of the
model's published outputs:

  outputs/weekly/weekly_summary.json       -- season / through_week / mode
  outputs/weekly/weekly_team_snapshot.csv  -- record, top strength/weakness,
                                               overall_confidence (current snapshot)
  outputs/weekly/weekly_changes.csv        -- per-(team,domain) index_value,
                                               rank_of_league, label, min_confidence
  outputs/rankings/team_rankings_weekly.csv -- full history of per-(team,domain)
                                               index_value / rank_of_league, used
                                               only as a fallback for a week that
                                               is no longer the "current" snapshot
  data/processed/schedules/season=YYYY/data.parquet -- venue/date logistics ONLY
                                               (stadium, location, gameday, weekday);
                                               betting columns in this table
                                               (spread_line, moneyline, total_line,
                                               result, ...) are never read.

This module computes exactly ONE derived value that is not a literal output
column: a domain-level percentile, obtained by applying the same rank ->
percentile mapping strength/team_strength.py already uses for metrics
(percentile = (n_teams - rank) / (n_teams - 1)) to the existing domain rank.
It is a deterministic, documented transform of an existing value, not an
independent statistic. Every other field is either read verbatim or is a plain
difference/ordering of two existing index values (Section 2/3 "gap").

Nothing here recomputes shrinkage, z-scores, domain indices, or ranks.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import polars as pl

from matchup.config import REPO_ROOT
from matchup.strength.config import DOMAINS

OUT = REPO_ROOT / "outputs"
DATA_PROCESSED = REPO_ROOT / "data" / "processed"

NA = "N/A"

# Section 2 / 3: the six football-relevant offense-vs-defense domain pairs,
# built from the nine existing domains (config/strength.yaml). Order matches
# the spec: away units first, then home units.
MATCHUP_COMPARISON_SPECS: tuple[tuple[str, str, str, str, str], ...] = (
    ("Away Passing Offense vs Home Passing Defense", "passing_offense", "away", "passing_defense", "home"),
    ("Away Rushing Offense vs Home Rushing Defense", "rushing_offense", "away", "rushing_defense", "home"),
    ("Away Pass Protection vs Home Pass Rush", "pass_protection", "away", "pass_rush", "home"),
    ("Home Passing Offense vs Away Passing Defense", "passing_offense", "home", "passing_defense", "away"),
    ("Home Rushing Offense vs Away Rushing Defense", "rushing_offense", "home", "rushing_defense", "away"),
    ("Home Pass Protection vs Away Pass Rush", "pass_protection", "home", "pass_rush", "away"),
)


class MatchupDataError(RuntimeError):
    """Required data for a matchup card could not be found or resolved."""


# --------------------------------------------------------------------------- #
# data shapes
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class DomainValue:
    domain: str
    label: str
    side: str  # "offense" | "defense" | "special"
    index_value: float | None
    rank: int | None
    n_teams: int | None
    percentile: float | None  # derived from rank -- see module docstring
    confidence: str | None
    source: str  # "weekly_snapshot" | "rankings_panel" | "missing"


@dataclass(frozen=True)
class TeamProfile:
    team: str
    season: int
    through_week: int
    games: int | None
    wins: int | None
    losses: int | None
    ties: int | None
    points_for: float | None
    points_against: float | None
    point_diff: float | None
    overall_confidence: str | None
    top_strength_domain: str | None
    top_strength_index: float | None
    top_weakness_domain: str | None
    top_weakness_index: float | None
    domains: dict[str, DomainValue]

    def domain(self, domain_id: str) -> DomainValue:
        if domain_id not in self.domains:
            raise MatchupDataError(f"unknown domain {domain_id!r}; valid domains: {sorted(DOMAINS)}")
        return self.domains[domain_id]


@dataclass(frozen=True)
class MatchupMeta:
    season: int
    requested_week: int
    displayed_through_week: int
    mode: str  # "preseason_baseline" | "in_season"
    is_baseline_display: bool  # True if the requested week hasn't been played yet
    data_source: str  # "weekly_snapshot" | "rankings_panel"
    generated_at: str | None
    stadium: str | None
    location: str | None
    gameday: str | None
    weekday: str | None


@dataclass(frozen=True)
class MatchupCardData:
    away: TeamProfile
    home: TeamProfile
    meta: MatchupMeta


@dataclass(frozen=True)
class UnitComparison:
    label: str
    unit_a_domain: str
    unit_a_team: str  # "away" | "home"
    unit_a_value: float | None
    unit_b_domain: str
    unit_b_team: str
    unit_b_value: float | None
    gap: float | None  # unit_a_value - unit_b_value; positive favors unit A's side


# --------------------------------------------------------------------------- #
# loading
# --------------------------------------------------------------------------- #
def _require_csv(path: Path) -> pl.DataFrame:
    if not path.exists():
        raise MatchupDataError(
            f"required output not found: {path}. Run `make weekly-research` "
            f"(or `make team-strength`) to generate it before creating a matchup card."
        )
    return pl.read_csv(path)


def _rank_percentile(rank: int | None, n_teams: int | None) -> float | None:
    """percentile = (n_teams - rank) / (n_teams - 1); identical mapping used for
    metric-level percentiles in strength/team_strength.py, applied to the
    existing domain rank. Returns None (not 0) when rank/n_teams is unknown."""
    if rank is None or n_teams is None or n_teams <= 1:
        return None
    return (n_teams - rank) / (n_teams - 1)


def load_weekly_summary(path: Path | None = None) -> dict:
    p = path or OUT / "weekly" / "weekly_summary.json"
    if not p.exists():
        raise MatchupDataError(
            f"required output not found: {p}. Run `make weekly-research` first."
        )
    return json.loads(p.read_text())


def _domains_from_weekly_changes(domain_changes: pl.DataFrame, team: str) -> dict[str, DomainValue]:
    sub = domain_changes.filter(pl.col("team") == team)
    n_teams = domain_changes.get_column("team").n_unique() if not domain_changes.is_empty() else None
    out: dict[str, DomainValue] = {}
    for dom, spec in DOMAINS.items():
        row = sub.filter(pl.col("domain") == dom)
        if row.is_empty():
            out[dom] = DomainValue(dom, spec["label"], spec["side"], None, None, n_teams, None, None, "missing")
            continue
        r = row.to_dicts()[0]
        rank = int(r["rank_of_league"]) if r["rank_of_league"] is not None else None
        out[dom] = DomainValue(
            domain=dom, label=r["label"], side=r["side"],
            index_value=r["index_value"], rank=rank, n_teams=n_teams,
            percentile=_rank_percentile(rank, n_teams),
            confidence=r["min_confidence"], source="weekly_snapshot",
        )
    return out


def _domains_from_rankings_panel(panel: pl.DataFrame, team: str) -> dict[str, DomainValue]:
    sub = panel.filter(pl.col("team") == team)
    n_teams = panel.get_column("team").n_unique() if not panel.is_empty() else None
    out: dict[str, DomainValue] = {}
    for dom, spec in DOMAINS.items():
        val_col, rank_col = f"index_value_{dom}", f"rank_of_league_{dom}"
        if sub.is_empty() or val_col not in sub.columns:
            out[dom] = DomainValue(dom, spec["label"], spec["side"], None, None, n_teams, None, None, "missing")
            continue
        row = sub.to_dicts()[0]
        rank = int(row[rank_col]) if row.get(rank_col) is not None else None
        out[dom] = DomainValue(
            domain=dom, label=spec["label"], side=spec["side"],
            index_value=row.get(val_col), rank=rank, n_teams=n_teams,
            percentile=_rank_percentile(rank, n_teams),
            confidence=None,  # not carried in the rankings panel
            source="rankings_panel",
        )
    return out


def _team_profile_from_snapshot(
    team: str, season: int, through_week: int,
    team_snapshot: pl.DataFrame, domain_changes: pl.DataFrame,
) -> TeamProfile:
    row = team_snapshot.filter(pl.col("team") == team)
    if row.is_empty():
        available = (
            sorted(team_snapshot.get_column("team").unique().to_list())
            if not team_snapshot.is_empty() else []
        )
        raise MatchupDataError(
            f"team {team!r} not found in weekly_team_snapshot.csv for "
            f"season={season} through_week={through_week}. Available teams: {available}"
        )
    r = row.to_dicts()[0]
    return TeamProfile(
        team=team, season=season, through_week=through_week,
        games=r.get("games"), wins=r.get("wins"), losses=r.get("losses"), ties=r.get("ties"),
        points_for=r.get("points_for"), points_against=r.get("points_against"),
        point_diff=r.get("point_diff"), overall_confidence=r.get("overall_confidence"),
        top_strength_domain=r.get("top_strength_domain"), top_strength_index=r.get("top_strength_index"),
        top_weakness_domain=r.get("top_weakness_domain"), top_weakness_index=r.get("top_weakness_index"),
        domains=_domains_from_weekly_changes(domain_changes, team),
    )


def _team_profile_from_rankings(team: str, season: int, through_week: int, panel: pl.DataFrame) -> TeamProfile:
    row = panel.filter(pl.col("team") == team)
    if row.is_empty():
        available = sorted(panel.get_column("team").unique().to_list()) if not panel.is_empty() else []
        raise MatchupDataError(
            f"team {team!r} not found in team_rankings_weekly.csv for "
            f"season={season} through_week={through_week}. Available teams: {available}"
        )
    return TeamProfile(
        team=team, season=season, through_week=through_week,
        games=None, wins=None, losses=None, ties=None,
        points_for=None, points_against=None, point_diff=None, overall_confidence=None,
        top_strength_domain=None, top_strength_index=None,
        top_weakness_domain=None, top_weakness_index=None,
        domains=_domains_from_rankings_panel(panel, team),
    )


def _schedule_lookup(season: int, week: int, away: str, home: str) -> dict:
    """Venue/date logistics ONLY. Never reads spread_line/moneyline/total_line/result."""
    p = DATA_PROCESSED / "schedules" / f"season={season}" / "data.parquet"
    if not p.exists():
        return {}
    cols = ["season", "week", "home_team", "away_team", "gameday", "weekday", "location", "stadium"]
    df = pl.read_parquet(p, columns=cols)
    row = df.filter(
        (pl.col("season") == season) & (pl.col("week") == week)
        & (pl.col("home_team") == home) & (pl.col("away_team") == away)
    )
    return row.to_dicts()[0] if not row.is_empty() else {}


def load_matchup_card_data(
    away: str, home: str, season: int, week: int,
    *,
    weekly_summary_path: Path | None = None,
    weekly_team_snapshot_path: Path | None = None,
    weekly_changes_path: Path | None = None,
    rankings_panel_path: Path | None = None,
) -> MatchupCardData:
    """Assemble everything a matchup card needs from existing outputs only.

    Resolution order for (season, week):
      1. If season matches the CURRENT weekly snapshot and the requested week is
         on or after it (i.e. it hasn't been played yet, or is exactly the
         current snapshot), use the snapshot's through_week -- it is always the
         richest available source (record, confidence, top strength/weakness).
         A future week therefore renders as a baseline display of the latest
         real snapshot, never as an error.
      2. Otherwise (a strictly earlier week in the current season, or a
         different season) fall back to outputs/rankings/team_rankings_weekly.csv,
         which retains full season/week history for domain index_value + rank
         (but not confidence or record -- those display as "N/A"), using the
         latest available through_week <= the requested week.
    """
    away, home = away.upper(), home.upper()
    if away == home:
        raise MatchupDataError(f"away and home team cannot be the same team ({away!r})")

    summary = load_weekly_summary(weekly_summary_path)
    snap_season, snap_week = summary["season"], summary["through_week"]

    if season == snap_season and week >= snap_week:
        team_snapshot = _require_csv(weekly_team_snapshot_path or OUT / "weekly" / "weekly_team_snapshot.csv")
        domain_changes = _require_csv(weekly_changes_path or OUT / "weekly" / "weekly_changes.csv")
        away_p = _team_profile_from_snapshot(away, season, snap_week, team_snapshot, domain_changes)
        home_p = _team_profile_from_snapshot(home, season, snap_week, team_snapshot, domain_changes)
        data_source = "weekly_snapshot"
        displayed_week = snap_week
        is_baseline_display = displayed_week == 0 and week >= 1
    else:
        panel = _require_csv(rankings_panel_path or OUT / "rankings" / "team_rankings_weekly.csv")
        panel_season = panel.filter(pl.col("season") == season)
        if panel_season.is_empty():
            raise MatchupDataError(
                f"no data available for season={season} in team_rankings_weekly.csv or "
                f"the current weekly snapshot (season={snap_season}, through_week={snap_week}). "
                f"Run `make team-strength` / `make weekly-research` for season {season} first."
            )
        available_weeks = sorted(panel_season.get_column("through_week").unique().to_list())
        eligible = [w for w in available_weeks if w <= week]
        if not eligible:
            raise MatchupDataError(
                f"no data available on or before week {week} for season={season}. "
                f"Weeks available: {available_weeks}"
            )
        displayed_week = max(eligible)
        panel_slice = panel_season.filter(pl.col("through_week") == displayed_week)
        away_p = _team_profile_from_rankings(away, season, displayed_week, panel_slice)
        home_p = _team_profile_from_rankings(home, season, displayed_week, panel_slice)
        data_source = "rankings_panel"
        is_baseline_display = displayed_week == 0 and week >= 1

    sched = _schedule_lookup(season, week, away, home)
    meta = MatchupMeta(
        season=season, requested_week=week, displayed_through_week=displayed_week,
        mode=summary.get("mode") if data_source == "weekly_snapshot" else (
            "preseason_baseline" if displayed_week == 0 else "in_season"
        ),
        is_baseline_display=is_baseline_display, data_source=data_source,
        generated_at=summary.get("generated_at"),
        stadium=sched.get("stadium"), location=sched.get("location"),
        gameday=sched.get("gameday"), weekday=sched.get("weekday"),
    )
    return MatchupCardData(away=away_p, home=home_p, meta=meta)


# --------------------------------------------------------------------------- #
# Section 2 / 3: matchup comparisons + key battles (existing domain values only)
# --------------------------------------------------------------------------- #
def compute_matchup_comparisons(data: MatchupCardData) -> list[UnitComparison]:
    """The six offense-vs-defense domain pairs. gap = unit_a - unit_b, both
    already-oriented existing domain index values (higher = better for that
    unit); positive gap favors unit A's side, negative favors unit B's side.
    This is a plain difference of two existing values -- no new metric."""
    teams = {"away": data.away, "home": data.home}
    out = []
    for label, dom_a, side_a, dom_b, side_b in MATCHUP_COMPARISON_SPECS:
        dv_a = teams[side_a].domain(dom_a)
        dv_b = teams[side_b].domain(dom_b)
        gap = (
            dv_a.index_value - dv_b.index_value
            if dv_a.index_value is not None and dv_b.index_value is not None
            else None
        )
        out.append(UnitComparison(
            label=label,
            unit_a_domain=dom_a, unit_a_team=side_a, unit_a_value=dv_a.index_value,
            unit_b_domain=dom_b, unit_b_team=side_b, unit_b_value=dv_b.index_value,
            gap=gap,
        ))
    return out


def identify_key_battles(
    comparisons: list[UnitComparison], *, k_min: int = 3, k_max: int = 5
) -> list[UnitComparison]:
    """The k_min-k_max comparisons with the largest measurable |gap|. Comparisons
    with a missing gap (N/A) are excluded, never treated as zero."""
    measurable = [c for c in comparisons if c.gap is not None]
    ranked = sorted(measurable, key=lambda c: abs(c.gap), reverse=True)
    return ranked[:k_max] if len(ranked) >= k_min else ranked


# --------------------------------------------------------------------------- #
# Section 4: team identity -- templated statements over existing fields only
# --------------------------------------------------------------------------- #
_ELITE_RANK = 5
_WEAK_RANK_FROM_BOTTOM = 5


def team_identity_statements(profile: TeamProfile) -> list[str]:
    """Short, data-driven bullet statements built only from fields already in
    the profile (top_strength/top_weakness + any other elite/weak domain rank).
    No narrative invention."""
    stmts: list[str] = []
    if profile.top_strength_domain and profile.top_strength_index is not None:
        dv = profile.domain(profile.top_strength_domain)
        rank_txt = f" (league rank {dv.rank}/{dv.n_teams})" if dv.rank and dv.n_teams else ""
        stmts.append(
            f"Strongest area: {dv.label} at {profile.top_strength_index:+.2f}{rank_txt}."
        )
    if profile.top_weakness_domain and profile.top_weakness_index is not None:
        dv = profile.domain(profile.top_weakness_domain)
        rank_txt = f" (league rank {dv.rank}/{dv.n_teams})" if dv.rank and dv.n_teams else ""
        stmts.append(
            f"Area of concern: {dv.label} at {profile.top_weakness_index:+.2f}{rank_txt}."
        )
    for dom_id, dv in sorted(profile.domains.items()):
        if dom_id in (profile.top_strength_domain, profile.top_weakness_domain):
            continue
        if dv.rank is None or dv.n_teams is None:
            continue
        if dv.rank <= _ELITE_RANK:
            stmts.append(f"Also top-{_ELITE_RANK} league-wide in {dv.label} (rank {dv.rank}/{dv.n_teams}).")
        elif dv.rank > dv.n_teams - _WEAK_RANK_FROM_BOTTOM:
            stmts.append(f"Also bottom-{_WEAK_RANK_FROM_BOTTOM} league-wide in {dv.label} (rank {dv.rank}/{dv.n_teams}).")
    return stmts
