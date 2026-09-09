"""Secondary analysis: NGS / PFR measurement-source ablation (spec section 11).

Combining a pbp metric with an NGS/PFR metric into ONE feature needs a fitted
combiner, which is forbidden in Phase 3. So the ablation is limited to:

  (1) each NGS/PFR metric's own SEASON-TO-SEASON persistence (prior completed
      season -> next season), pooled across all available season pairs, with
      coverage / earliest-valid-season made explicit;
  (2) the same season-to-season persistence for the corresponding pbp metric,
      computed BOTH on the full sample and on the NGS/PFR-covered subset, so the
      sample restriction is explicit.

Season-to-season (rather than in-season trailing) is used because the NGS weekly
files carry no usable opportunity weights; a season aggregate is the cleanest
comparable unit.
"""
from __future__ import annotations

import numpy as np
import polars as pl

from matchup.metrics.build import game_metrics_offline
from matchup.metrics.windows import entity_season_aggregate
from matchup.store import load_source

# (external source, id col, week filter, metrics, corresponding pbp family+metric, pbp id)
_NGS = [
    ("ngs_passing", "player_gsis_id",
     {"avg_time_to_throw": None, "aggressiveness": None,
      "completion_percentage_above_expectation": ("qb", "cpoe")}),
    ("ngs_receiving", "player_gsis_id",
     {"avg_separation": None, "avg_yac_above_expectation": None}),
    ("ngs_rushing", "player_gsis_id",
     {"rush_yards_over_expected_per_att": ("rb", "rush_epa_per_att"), "efficiency": None}),
]
_SEASONS = list(range(2016, 2026))


def _spearman(a: np.ndarray, b: np.ndarray) -> float:
    m = ~(np.isnan(a) | np.isnan(b))
    a, b = a[m], b[m]
    if a.size < 10:
        return float("nan")
    return float(np.corrcoef(a.argsort().argsort(), b.argsort().argsort())[0, 1])


def _skill_vs_mean(feat: np.ndarray, targ: np.ndarray) -> tuple[float, int]:
    m = ~(np.isnan(feat) | np.isnan(targ))
    feat, targ = feat[m], targ[m]
    if feat.size < 10:
        return float("nan"), int(feat.size)
    base = np.full_like(targ, targ.mean())
    r_f = np.sqrt(np.mean((feat - targ) ** 2))
    r_b = np.sqrt(np.mean((base - targ) ** 2))
    return (1 - r_f / r_b if r_b > 0 else float("nan")), int(feat.size)


def _season_pairs(df: pl.DataFrame, metric: str, id_col: str) -> pl.DataFrame:
    a = df.select(id_col, "season", pl.col(metric).alias("prior"))
    b = df.select(id_col, (pl.col("season") - 1).alias("season"), pl.col(metric).alias("next"))
    return a.join(b, on=[id_col, "season"], how="inner").drop_nulls()


def build_external_ablation() -> pl.DataFrame:
    rows: list[dict] = []

    # NGS season aggregates (mean of weekly values -> a season summary)
    for src, idc, metrics in _NGS:
        raw = load_source(src, seasons=_SEASONS)
        if raw.is_empty():
            continue
        raw = raw.filter(pl.col("week") > 0)
        agg = raw.group_by([idc, "season"]).agg(
            [pl.col(m).mean().alias(m) for m in metrics if m in raw.columns]
            + [pl.len().alias("n_weeks")]
        )
        n_player_seasons = agg.height
        for m, pbp_ref in metrics.items():
            if m not in agg.columns:
                continue
            pairs = _season_pairs(agg.filter(pl.col("n_weeks") >= 4), m, idc)
            sk, n = _skill_vs_mean(pairs.get_column("prior").to_numpy(), pairs.get_column("next").to_numpy())
            sp = _spearman(pairs.get_column("prior").to_numpy(), pairs.get_column("next").to_numpy())
            rows.append({
                "ablation": "external_source_own_persistence", "source": src, "metric": m,
                "unit": "season_to_season", "n_pairs": n, "n_player_seasons": n_player_seasons,
                "earliest_valid_season": 2016 if src.startswith("ngs") else 2018,
                "spearman": sp, "skill_vs_league_mean": sk,
                "corresponds_to_pbp": f"{pbp_ref[0]}.{pbp_ref[1]}" if pbp_ref else None,
            })

            # matched pbp metric: full sample vs NGS-covered subset
            if pbp_ref:
                fam, pm = pbp_ref
                pbp_gm = game_metrics_offline(fam, _SEASONS)
                pbp_season = entity_season_aggregate(fam, pbp_gm)
                covered_ids = set(agg.filter(pl.col("n_weeks") >= 4).get_column(idc).to_list())
                for label, sub in (
                    ("full", pbp_season),
                    ("ngs_covered_subset", pbp_season.filter(pl.col("entity_id").is_in(list(covered_ids)))),
                ):
                    pr = _season_pairs(sub, pm, "entity_id")
                    sk2, n2 = _skill_vs_mean(pr.get_column("prior").to_numpy(), pr.get_column("next").to_numpy())
                    sp2 = _spearman(pr.get_column("prior").to_numpy(), pr.get_column("next").to_numpy())
                    rows.append({
                        "ablation": "pbp_metric_sample_restriction", "source": "pbp",
                        "metric": f"{fam}.{pm}", "unit": f"season_to_season/{label}",
                        "n_pairs": n2, "n_player_seasons": sub.height,
                        "earliest_valid_season": 1999,
                        "spearman": sp2, "skill_vs_league_mean": sk2,
                        "corresponds_to_pbp": f"{fam}.{pm}",
                    })
    return pl.DataFrame(rows)
