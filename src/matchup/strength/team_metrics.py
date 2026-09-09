"""Per-(team, season, week) season-to-date unit metrics, shrunk and normalized.

For every team and every week W it played, aggregate that team's REGULAR-SEASON
games in weeks 1..W (season-to-date), recompute each rate from summed components,
shrink it toward the 3-completed-prior-season league mean (frozen Phase 4
constants), and express it as a z-score vs that historical reference.

Strictly PIT-safe for research: "team through week W" uses only weeks <= W.
Every underlying number (raw value, sample size, reference mean/sd, shrunk value)
is kept in the output so nothing is hidden behind the index.
"""
from __future__ import annotations

import functools

import numpy as np
import polars as pl

from matchup.metrics.build import game_metrics_batch, game_metrics_offline
from matchup.metrics.families import FAMILY_SPECS
from matchup.metrics.windows import entity_season_aggregate
from matchup.normalize.reference import completed_seasons_asof, min_opportunities_for
from matchup.pointintime.calendar import build_game_calendar
from matchup.strength.config import (
    STRENGTH_METRICS,
    load_strength_config,
    metric_bare,
    metric_family,
    orient_sign,
)

_HIST_SEASON_FLOOR = 2013  # earliest ingested pbp season


@functools.lru_cache(maxsize=1)
def _week1_kickoffs() -> dict[int, object]:
    cal = build_game_calendar()
    g = cal.group_by("season").agg(pl.col("kickoff_utc").min().alias("k"))
    return {int(r["season"]): r["k"] for r in g.iter_rows(named=True)}


def reference_seasons_for(season: int) -> list[int]:
    """The 3 completed seasons before `season`'s week 1 (Phase 2/3 rule)."""
    k1 = _week1_kickoffs().get(season)
    if k1 is None:
        return [s for s in range(season - 3, season) if s >= _HIST_SEASON_FLOOR]
    return completed_seasons_asof(k1)


@functools.lru_cache(maxsize=64)
def _historical_reference(family: str, season: int) -> pl.DataFrame:
    """team-season distribution of each rate over the reference seasons ->
    (metric_bare, ref_mean, ref_sd, ref_n, ref_seasons)."""
    refs = reference_seasons_for(season)
    if not refs:
        return pl.DataFrame()
    gm = game_metrics_offline(family, refs)
    if gm.is_empty():
        return pl.DataFrame()
    season_lvl = entity_season_aggregate(family, gm)
    mo = min_opportunities_for(family)
    season_lvl = season_lvl.filter(pl.col("n_opportunities") >= mo)
    rows = []
    for m in FAMILY_SPECS[family]["rates"]:
        if m not in season_lvl.columns:
            continue
        v = season_lvl.get_column(m).drop_nulls().to_numpy()
        rows.append({
            "metric_bare": m,
            "ref_mean": float(np.mean(v)) if v.size else float("nan"),
            "ref_sd": float(np.std(v, ddof=1)) if v.size >= 2 else float("nan"),
            "ref_n": int(v.size),
            "ref_seasons": ",".join(str(s) for s in refs),
        })
    return pl.DataFrame(rows)


def _family_season_to_date(family: str, seasons: tuple[int, ...]) -> pl.DataFrame:
    """Cumulative (season-to-date) rates for every (team, season, week-played)."""
    gm = game_metrics_batch(family, seasons)
    if gm.is_empty():
        return pl.DataFrame()
    spec = FAMILY_SPECS[family]
    comps = [c for c in spec["components"] if c in gm.columns]
    opp = spec["opportunity"]
    gm = gm.filter(pl.col("week").is_between(1, 18)).sort(
        ["season", "entity_id", "week", "game_id"]
    )
    gm = gm.with_columns(
        [pl.col(c).cum_sum().over(["season", "entity_id"]).alias(c) for c in comps]
        + [pl.int_range(1, pl.len() + 1).over(["season", "entity_id"]).alias("n_games")]
    )
    rate_exprs = [
        pl.when(pl.col(den) > 0).then(pl.col(num) / pl.col(den)).otherwise(None).alias(name)
        for name, (num, den) in spec["rates"].items()
        if num in gm.columns and den in gm.columns
    ]
    gm = gm.with_columns(rate_exprs).with_columns(pl.col(opp).alias("n_opportunities"))
    keep = ["season", "entity_id", "week", "n_games", "n_opportunities",
            *[m for m in spec["rates"] if m in gm.columns]]
    return gm.select(keep)


def _family_preseason(family: str, seasons: tuple[int, ...]) -> pl.DataFrame:
    """week-0 baseline: each team's PRIOR full regular season value (raw)."""
    prev = tuple(sorted({s - 1 for s in seasons}))
    gm = game_metrics_offline(family, list(prev))
    if gm.is_empty():
        return pl.DataFrame()
    gm = gm.filter(pl.col("week").is_between(1, 18))
    sl = entity_season_aggregate(family, gm)  # one row per (entity_id, season)
    rates = [m for m in FAMILY_SPECS[family]["rates"] if m in sl.columns]
    out = sl.select(
        (pl.col("season") + 1).alias("season"),
        pl.col("entity_id"),
        pl.lit(0).alias("week"),
        pl.col("n_games"),
        pl.col("n_opportunities"),
        *rates,
    )
    return out.filter(pl.col("season").is_in(list(seasons)))


def build_team_metrics_weekly(seasons: list[int]) -> pl.DataFrame:
    """Long frame: one row per (season, team, week, metric).

    week 0 = preseason baseline (prior full season, shrunk).
    week >=1 = season-to-date through that week.

    Columns: season, team, week, metric, family, direction, n_games,
    n_opportunities, raw_value, ref_mean, ref_sd, ref_n, ref_seasons, k,
    shrunk_value, z_raw, z_shrunk, oriented_z_shrunk, in_index, phase3_status.
    """
    seasons_t = tuple(sorted(seasons))
    families = sorted({m["family"] for m in STRENGTH_METRICS.values()})
    wanted = {}  # family -> [bare metric names]
    for full in STRENGTH_METRICS:
        wanted.setdefault(metric_family(full), []).append(metric_bare(full))

    frames = []
    for fam in families:
        std = _family_season_to_date(fam, seasons_t)
        pre = _family_preseason(fam, seasons_t)
        parts = [df for df in (pre, std) if not df.is_empty()]
        if not parts:
            continue
        wide = pl.concat(parts, how="diagonal_relaxed")
        bares = [b for b in wanted[fam] if b in wide.columns]
        long = wide.unpivot(
            index=["season", "entity_id", "week", "n_games", "n_opportunities"],
            on=bares, variable_name="metric_bare", value_name="raw_value",
        ).rename({"entity_id": "team"})
        for season in seasons_t:
            ref = _historical_reference(fam, season)
            if ref.is_empty():
                continue
            sub = long.filter(pl.col("season") == season).join(ref, on="metric_bare", how="left")
            frames.append(sub.with_columns(pl.lit(fam).alias("family")))

    if not frames:
        return pl.DataFrame()
    df = pl.concat(frames, how="diagonal_relaxed")

    df = df.with_columns((pl.col("family") + "." + pl.col("metric_bare")).alias("metric"))
    k_map = {f: STRENGTH_METRICS[f]["k"] for f in STRENGTH_METRICS}
    dir_map = {f: STRENGTH_METRICS[f]["direction"] for f in STRENGTH_METRICS}
    idx_map = {f: STRENGTH_METRICS[f]["in_index"] for f in STRENGTH_METRICS}
    p3_map = {f: STRENGTH_METRICS[f]["phase3"] for f in STRENGTH_METRICS}
    sign_map = {f: orient_sign(f) for f in STRENGTH_METRICS}

    df = df.with_columns(
        pl.col("metric").replace_strict(k_map, default=None).alias("k"),
        pl.col("metric").replace_strict(dir_map, default=None).alias("direction"),
        pl.col("metric").replace_strict(idx_map, default=None).alias("in_index"),
        pl.col("metric").replace_strict(p3_map, default=None).alias("phase3_status"),
        pl.col("metric").replace_strict(sign_map, default=0).alias("_sign"),
    )
    n = pl.col("n_games").cast(pl.Float64).clip(lower_bound=0.0)
    df = df.with_columns(
        (pl.col("ref_mean") + n / (n + pl.col("k")) * (pl.col("raw_value") - pl.col("ref_mean")))
        .alias("shrunk_value"),
    ).with_columns(
        ((pl.col("raw_value") - pl.col("ref_mean")) / pl.col("ref_sd")).alias("z_raw"),
        ((pl.col("shrunk_value") - pl.col("ref_mean")) / pl.col("ref_sd")).alias("z_shrunk"),
    ).with_columns(
        (pl.col("_sign") * pl.col("z_shrunk")).alias("oriented_z_shrunk"),
    )
    return df.select(
        "season", "team", "week", "metric", "family", "metric_bare", "direction",
        "n_games", "n_opportunities", "raw_value", "ref_mean", "ref_sd", "ref_n",
        "ref_seasons", "k", "shrunk_value", "z_raw", "z_shrunk", "oriented_z_shrunk",
        "in_index", "phase3_status",
    ).sort(["season", "week", "team", "metric"])


def confidence_label(n_games: int, week: int) -> str:
    cfg = load_strength_config()["confidence"]
    if week == 0:
        return "prior_season_only"
    if n_games >= cfg["high_min_games"]:
        return "high"
    if n_games >= cfg["medium_min_games"]:
        return "medium"
    return "low"
