"""Load config/metrics.yaml and produce the metric coverage / sample-size table."""
from __future__ import annotations

import functools

import polars as pl
import yaml

from matchup.config import CONFIG_DIR
from matchup.metrics.build import game_metrics_offline
from matchup.metrics.families import FAMILY_SPECS
from matchup.metrics.windows import entity_season_aggregate


@functools.lru_cache(maxsize=1)
def load_registry() -> dict:
    return yaml.safe_load((CONFIG_DIR / "metrics.yaml").read_text())


def registered_metrics() -> pl.DataFrame:
    reg = load_registry()
    rows = []
    for m in reg["metrics"]:
        rows.append({
            "name": m["name"],
            "family": m["family"],
            "taxonomy": m["taxonomy"],
            "source": m["source"],
            "direction": m["direction"],
            "grain": m["grain"],
            "earliest_valid_season": m["earliest_valid_season"],
            "proposed_role": m["proposed_role"],
            "predictive_status": m["predictive_status"],
        })
    return pl.DataFrame(rows)


def coverage_table(seasons: list[int] | None = None) -> pl.DataFrame:
    """Per (family, metric): season coverage, entity-season sample sizes, missingness,
    for the pbp-derived families (which can be built offline)."""
    seasons = seasons or list(range(2016, 2025))
    rows = []
    for family, spec in FAMILY_SPECS.items():
        gm = game_metrics_offline(family, seasons)
        if gm.is_empty():
            continue
        season_lvl = entity_season_aggregate(family, gm)
        for metric in spec["rates"]:
            if metric not in season_lvl.columns:
                continue
            col = season_lvl.get_column(metric)
            per_season = season_lvl.group_by("season").agg(
                pl.len().alias("entity_seasons"),
                pl.col(metric).is_null().mean().alias("null_frac"),
                pl.col("n_opportunities").median().alias("median_opps"),
            ).sort("season")
            rows.append({
                "family": family,
                "metric": metric,
                "seasons_present": f"{seasons[0]}-{seasons[-1]}",
                "n_entity_seasons": int(col.len()),
                "null_frac_overall": round(float(col.is_null().mean()), 4),
                "min_entity_seasons_in_a_season": int(per_season.get_column("entity_seasons").min()),
                "median_opportunities": float(season_lvl.get_column("n_opportunities").median()),
            })
    return pl.DataFrame(rows).sort(["family", "metric"])
