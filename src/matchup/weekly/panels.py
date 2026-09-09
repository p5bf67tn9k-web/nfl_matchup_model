"""Assemble the weekly snapshot tables from the per-metric frame."""
from __future__ import annotations

import polars as pl

from matchup.strength.results import team_record_through_week
from matchup.strength.team_strength import team_strength_snapshot


def _domains_wide(domains: pl.DataFrame) -> pl.DataFrame:
    if domains.is_empty():
        return pl.DataFrame()
    return domains.pivot(
        values=["index_value", "rank_of_league"], index="team", on="domain",
    )


def build_weekly_snapshot(metrics_long: pl.DataFrame, season: int, through_week: int) -> dict:
    """Returns {team_snapshot, domain_changes, metric_detail} for one week."""
    cur = team_strength_snapshot(metrics_long, season, through_week)
    prev = team_strength_snapshot(metrics_long, season, max(through_week - 1, 0))
    pre = team_strength_snapshot(metrics_long, season, 0)
    if cur["domains"].is_empty():
        return {"team_snapshot": pl.DataFrame(), "domain_changes": pl.DataFrame(),
                "metric_detail": pl.DataFrame()}

    dc = cur["domains"].select(
        "team", "domain", "side", "label", "index_value", "rank_of_league",
        "n_metrics_used", "n_metrics_defined", "min_confidence",
    ).join(
        prev["domains"].select(
            "team", "domain",
            pl.col("index_value").alias("index_prev_week"),
            pl.col("rank_of_league").alias("rank_prev_week"),
        ),
        on=["team", "domain"], how="left",
    ).join(
        pre["domains"].select(
            "team", "domain", pl.col("index_value").alias("index_preseason"),
        ),
        on=["team", "domain"], how="left",
    ).with_columns(
        (pl.col("index_value") - pl.col("index_prev_week")).alias("delta_vs_prev_week"),
        (pl.col("index_value") - pl.col("index_preseason")).alias("delta_vs_preseason"),
        (pl.col("rank_prev_week") - pl.col("rank_of_league")).alias("rank_change_vs_prev_week"),
        pl.lit(season).alias("season"), pl.lit(through_week).alias("through_week"),
    ).sort(["domain", "rank_of_league"])

    # per-team snapshot
    wide = _domains_wide(cur["domains"])
    rec = team_record_through_week(season, through_week)
    if rec.is_empty():
        rec = pl.DataFrame({"team": sorted(cur["domains"].get_column("team").unique().to_list())})
        rec = rec.with_columns(
            *[pl.lit(None, dtype=pl.Int64).alias(c)
              for c in ("games", "wins", "losses", "ties", "points_for", "points_against", "point_diff")],
            pl.lit(None, dtype=pl.Float64).alias("win_pct"),
        )

    idx_side = cur["domains"].select("team", "domain", "side", "index_value")
    strengths = (
        idx_side.filter(pl.col("index_value").is_not_null())
        .sort("index_value", descending=True)
        .group_by("team", maintain_order=True).first()
        .select("team", pl.col("domain").alias("top_strength_domain"),
                pl.col("index_value").alias("top_strength_index"))
    )
    weaknesses = (
        idx_side.filter(pl.col("index_value").is_not_null())
        .sort("index_value")
        .group_by("team", maintain_order=True).first()
        .select("team", pl.col("domain").alias("top_weakness_domain"),
                pl.col("index_value").alias("top_weakness_index"))
    )
    conf = cur["domains"].group_by("team").agg(
        pl.col("min_confidence").alias("_c"),
    )
    order = {"none": 0, "low": 1, "prior_season_only": 2, "medium": 3, "high": 4}
    conf = conf.with_columns(
        pl.col("_c").map_elements(
            lambda xs: min(xs, key=lambda x: order.get(x, 0)), return_dtype=pl.String,
        ).alias("overall_confidence"),
    ).drop("_c")

    ts = (
        rec.join(wide, on="team", how="right")
        .join(strengths, on="team", how="left")
        .join(weaknesses, on="team", how="left")
        .join(conf, on="team", how="left")
        .with_columns(pl.lit(season).alias("season"), pl.lit(through_week).alias("through_week"))
        .sort("team")
    )

    md = cur["metrics"].select(
        "season", "through_week", "team", "metric", "family", "direction", "phase3_status",
        "n_games", "n_opportunities", "raw_value", "ref_mean", "ref_sd", "ref_seasons",
        "k", "shrunk_value", "z_raw", "z_shrunk", "oriented_z_shrunk",
        "rank_of_league", "percentile", "confidence", "in_index",
    ).join(
        prev["metrics"].select(
            "team", "metric", pl.col("shrunk_value").alias("shrunk_prev_week"),
        ),
        on=["team", "metric"], how="left",
    ).join(
        pre["metrics"].select(
            "team", "metric", pl.col("shrunk_value").alias("shrunk_preseason"),
        ),
        on=["team", "metric"], how="left",
    ).with_columns(
        (pl.col("shrunk_value") - pl.col("shrunk_prev_week")).alias("delta_shrunk_vs_prev_week"),
        (pl.col("shrunk_value") - pl.col("shrunk_preseason")).alias("delta_shrunk_vs_preseason"),
    ).sort(["team", "metric"])

    return {"team_snapshot": ts, "domain_changes": dc, "metric_detail": md}


def movers(domain_changes: pl.DataFrame, side: str, *, n: int = 6) -> dict:
    """Biggest week-over-week index risers / fallers on the overall domain for a side."""
    dom = {"offense": "offense_overall", "defense": "defense_overall"}[side]
    d = domain_changes.filter(
        (pl.col("domain") == dom) & pl.col("delta_vs_prev_week").is_not_null()
    ).sort("delta_vs_prev_week", descending=True)
    return {
        "risers": d.head(n).select("team", "index_value", "delta_vs_prev_week",
                                   "rank_of_league", "rank_change_vs_prev_week").to_dicts(),
        "fallers": d.tail(n).reverse().select("team", "index_value", "delta_vs_prev_week",
                                              "rank_of_league", "rank_change_vs_prev_week").to_dicts(),
    }
