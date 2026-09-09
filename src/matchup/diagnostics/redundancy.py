"""Descriptive metric overlap within logical groups.

Purpose: understand the measurement space. NOT for selecting, combining, or
dropping metrics -- that decision belongs to the later predictive-validation
phase and must use out-of-sample prediction, not correlation.
"""
from __future__ import annotations

import polars as pl

from matchup.diagnostics.reliability import _agg_rates, _corr, _entity_season_games

# taxonomy groups within which overlap is most interesting to inspect
_GROUPS = {
    "qb": {
        "efficiency": ["epa_per_dropback", "dropback_success_rate", "yards_per_attempt"],
        "accuracy": ["completion_pct", "cpoe"],
        "style": ["adot"],
        "outcome_noise": ["interception_rate", "explosive_pass_rate", "sack_rate"],
    },
    "rb": {
        "efficiency": ["rush_epa_per_att", "rush_success_rate", "yards_per_carry"],
        "outcome_noise": ["explosive_rush_rate", "fumble_lost_rate"],
    },
    "wr": {
        "efficiency": ["epa_per_target", "target_success_rate", "yards_per_target", "catch_rate"],
        "style": ["adot"],
        "outcome_noise": ["explosive_rec_rate"],
    },
    "team_offense": {
        "core_efficiency": ["epa_per_play", "success_rate", "pass_epa_per_dropback",
                            "rush_epa_per_play", "early_down_epa_per_play"],
        "style": ["proe"],
        "outcome_noise": ["explosive_pass_rate", "explosive_rush_rate"],
    },
    "team_defense": {
        "core_efficiency": ["epa_per_play", "success_rate", "pass_epa_per_dropback",
                            "rush_epa_per_play", "early_down_epa_per_play"],
        "outcome_noise": ["explosive_pass_rate", "explosive_rush_rate"],
    },
    "pass_protection": {"protection": ["sack_rate_allowed", "qb_hit_rate_allowed"]},
    "pass_rush": {"rush": ["sack_rate_generated", "qb_hit_rate_generated"]},
}


def build_redundancy_report(seasons: list[int] | None = None) -> pl.DataFrame:
    seasons = seasons or list(range(2016, 2025))
    rows: list[dict] = []
    for family, groups in _GROUPS.items():
        gm = _entity_season_games(family, seasons)
        if gm.is_empty():
            continue
        season_lvl = _agg_rates(
            gm.join(
                gm.group_by(["entity_id", "season"]).agg(pl.len().alias("n")).filter(pl.col("n") >= 8),
                on=["entity_id", "season"],
            ),
            family,
        )
        for group, metrics in groups.items():
            present = [m for m in metrics if m in season_lvl.columns]
            for i in range(len(present)):
                for j in range(i + 1, len(present)):
                    a = season_lvl.get_column(present[i]).to_numpy().astype(float)
                    b = season_lvl.get_column(present[j]).to_numpy().astype(float)
                    pear, spear, n = _corr(a, b)
                    rows.append({
                        "family": family, "group": group,
                        "metric_a": present[i], "metric_b": present[j],
                        "pearson": pear, "spearman": spear, "n_entity_seasons": n,
                        "seasons": f"{seasons[0]}-{seasons[-1]}",
                        "note": "descriptive overlap only; do NOT select/combine on this",
                    })
    return pl.DataFrame(rows).sort([pl.col("pearson").abs().fill_null(0)], descending=True)
