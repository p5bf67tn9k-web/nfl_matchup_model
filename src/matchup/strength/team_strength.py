"""Domain strength INDICES from the per-metric frame.

A domain index is an equal-weight mean of its member metrics' oriented, shrunk
z-scores (oriented: +z if higher-is-better, -z if lower-is-better). It is a
transparent research index expressed in reference-standard-deviation units -- NOT
points, NOT a probability, NOT a calibrated rating. The member metrics are always
carried alongside it.
"""
from __future__ import annotations

import polars as pl

from matchup.strength.config import DOMAINS
from matchup.strength.results import team_record_through_week
from matchup.strength.team_metrics import confidence_label


def _latest_through_week(metrics_long: pl.DataFrame, season: int, through_week: int) -> pl.DataFrame:
    """Each (team, metric)'s most recent row with week <= through_week
    (week 0 = preseason baseline; used when through_week == 0 or a team is on a
    bye with no earlier in-season game)."""
    d = metrics_long.filter((pl.col("season") == season) & (pl.col("week") <= max(through_week, 0)))
    if d.is_empty():
        return d
    return (
        d.sort(["team", "metric", "week"])
        .group_by(["team", "metric"], maintain_order=True)
        .last()
    )


def _domain_index(snap: pl.DataFrame) -> pl.DataFrame:
    """snap = one row per (team, metric) with oriented_z_shrunk. Returns one row
    per (team, domain) with the index + member detail counts."""
    rows = []
    idx_members = snap.filter(pl.col("in_index"))
    for team in snap.get_column("team").unique().sort():
        t = idx_members.filter(pl.col("team") == team)
        for dom, spec in DOMAINS.items():
            mem = t.filter(pl.col("metric").is_in(spec["metrics"]))
            vals = mem.get_column("oriented_z_shrunk").drop_nulls()
            rows.append({
                "team": team, "domain": dom, "side": spec["side"], "label": spec["label"],
                "index_value": float(vals.mean()) if len(vals) else None,
                "n_metrics_used": len(vals),
                "n_metrics_defined": len(spec["metrics"]),
                "min_confidence": _worst_conf(mem),
            })
    return pl.DataFrame(rows)


def _worst_conf(mem: pl.DataFrame) -> str:
    order = {"low": 0, "prior_season_only": 1, "medium": 2, "high": 3}
    if mem.is_empty():
        return "none"
    labels = [
        confidence_label(int(r["n_games"] or 0), int(r["week"]))
        for r in mem.iter_rows(named=True)
    ]
    return min(labels, key=lambda x: order.get(x, 0))


def team_strength_snapshot(
    metrics_long: pl.DataFrame, season: int, through_week: int
) -> dict[str, pl.DataFrame]:
    """Full-league snapshot for one (season, through_week).

    Returns {"metrics": per-(team,metric) detail with cross-sectional rank/pct,
             "domains": per-(team,domain) index with rank,
             "record": per-team W-L + points}.
    """
    snap = _latest_through_week(metrics_long, season, through_week)
    if snap.is_empty():
        return {"metrics": pl.DataFrame(), "domains": pl.DataFrame(), "record": pl.DataFrame()}

    # cross-sectional rank / percentile within this snapshot, per metric.
    # orient so rank 1 = best; percentile in [0,1], higher = better.
    snap = snap.with_columns(
        pl.col("oriented_z_shrunk").rank("min", descending=True).over("metric").alias("rank_of_league"),
        (pl.col("oriented_z_shrunk").rank("average").over("metric") - 1)
        .truediv((pl.col("oriented_z_shrunk").count().over("metric") - 1).clip(lower_bound=1))
        .alias("percentile"),
        pl.struct("n_games", "week").map_elements(
            lambda s: confidence_label(int(s["n_games"] or 0), int(s["week"])),
            return_dtype=pl.String,
        ).alias("confidence"),
        pl.lit(through_week).alias("through_week"),
    ).with_columns(
        # neutral-direction metrics (e.g. proe) have no "better" direction: blank the rank
        pl.when(pl.col("direction") == "neutral").then(None)
        .otherwise(pl.col("rank_of_league")).alias("rank_of_league"),
        pl.when(pl.col("direction") == "neutral").then(None)
        .otherwise(pl.col("percentile")).alias("percentile"),
    )

    domains = _domain_index(snap).with_columns(
        pl.col("index_value").rank("min", descending=True).over("domain").alias("rank_of_league"),
        pl.lit(season).alias("season"), pl.lit(through_week).alias("through_week"),
    )
    rec = team_record_through_week(season, through_week)
    return {"metrics": snap, "domains": domains, "record": rec}


def build_team_strength_weekly(metrics_long: pl.DataFrame) -> dict[str, pl.DataFrame]:
    """Stack snapshots for every (season, week) present -> historical panels.

    Adds week-over-week and vs-preseason deltas on the domain index.
    """
    dom_frames, met_frames = [], []
    for season in metrics_long.get_column("season").unique().sort():
        wks = (
            metrics_long.filter((pl.col("season") == season) & (pl.col("week") >= 1))
            .get_column("week").unique().sort().to_list()
        )
        for w in [0, *wks]:
            s = team_strength_snapshot(metrics_long, int(season), int(w))
            if not s["domains"].is_empty():
                dom_frames.append(s["domains"])
            if not s["metrics"].is_empty():
                met_frames.append(
                    s["metrics"].with_columns(pl.lit(int(w)).alias("through_week"))
                )
    if not dom_frames:
        return {"domains": pl.DataFrame(), "metrics": pl.DataFrame()}

    dom = pl.concat(dom_frames, how="diagonal_relaxed").sort(
        ["season", "domain", "team", "through_week"]
    )
    dom = dom.with_columns(
        (pl.col("index_value") - pl.col("index_value").shift(1).over(["season", "domain", "team"]))
        .alias("delta_vs_prev_week"),
        (pl.col("index_value") - pl.col("index_value").first().over(["season", "domain", "team"]))
        .alias("delta_vs_preseason"),
    )
    met = pl.concat(met_frames, how="diagonal_relaxed").sort(
        ["season", "metric", "team", "through_week"]
    )
    met = met.with_columns(
        (pl.col("shrunk_value") - pl.col("shrunk_value").shift(1).over(["season", "metric", "team"]))
        .alias("delta_shrunk_vs_prev_week"),
    )
    return {"domains": dom, "metrics": met}


def build_rankings_weekly(domains_panel: pl.DataFrame) -> pl.DataFrame:
    """Wide-ish ranking table: one row per (season, through_week, team) with each
    domain index + rank as columns, plus record columns joined in by the caller."""
    if domains_panel.is_empty():
        return pl.DataFrame()
    piv = domains_panel.pivot(
        values=["index_value", "rank_of_league"],
        index=["season", "through_week", "team"],
        on="domain",
    )
    return piv.sort(["season", "through_week", "team"])


_INDEX_FORMULA = """\
Every domain index = arithmetic mean of its member metrics' oriented, shrunk z-scores.
  z_shrunk(metric) = (shrunk_value - ref_mean) / ref_sd
  shrunk_value     = ref_mean + n_games/(n_games + k) * (raw_value - ref_mean)
  oriented         = +z_shrunk if higher-is-better, -z_shrunk if lower-is-better
  ref_mean/ref_sd  = mean/SD of team-season values over the 3 completed prior seasons
                     (min-opportunity filtered)
  k                = frozen Phase 4 walk-forward shrinkage constant per metric (config/strength.yaml)
Units are reference standard deviations. The index is NOT points, NOT a probability, NOT a
definitive rating. The member metrics are always shown alongside it."""


def index_formula_text() -> str:
    return _INDEX_FORMULA
