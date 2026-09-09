"""Descriptive stability of metrics. Retrospective diagnostics are flagged."""
from __future__ import annotations

import numpy as np
import polars as pl

from matchup.metrics.build import game_metrics_offline
from matchup.metrics.families import FAMILY_SPECS
from matchup.pointintime.calendar import build_game_calendar

_MIN_GAMES = {"qb": 8, "rb": 8, "wr": 8, "team_offense": 8, "team_defense": 8,
              "pass_protection": 8, "pass_rush": 8}
_STD_SPLIT_WEEK = 9  # weeks 1..9 vs 10.. for the retrospective STD-vs-rest split


def _spearman_brown(r: float) -> float:
    return (2 * r) / (1 + r) if r is not None and abs(r) < 1 else r


def _corr(a: np.ndarray, b: np.ndarray) -> tuple[float | None, float | None, int]:
    m = ~(np.isnan(a) | np.isnan(b))
    a, b = a[m], b[m]
    if a.size < 5:
        return None, None, int(a.size)
    pear = float(np.corrcoef(a, b)[0, 1])
    ar = a.argsort().argsort().astype(float)
    br = b.argsort().argsort().astype(float)
    spear = float(np.corrcoef(ar, br)[0, 1])
    return pear, spear, int(a.size)


def _entity_season_games(family: str, seasons: list[int]) -> pl.DataFrame:
    gm = game_metrics_offline(family, seasons)
    if gm.is_empty():
        return gm
    cal = build_game_calendar().select("game_id", "kickoff_utc")
    gm = gm.join(cal, on="game_id", how="left").sort(["entity_id", "season", "kickoff_utc"])
    return gm.with_columns(pl.int_range(pl.len()).over(["entity_id", "season"]).alias("gidx"))


def _agg_rates(df: pl.DataFrame, family: str) -> pl.DataFrame:
    spec = FAMILY_SPECS[family]
    comp = [c for c in spec["components"] if c in df.columns]
    g = df.group_by(["entity_id", "season"]).agg(
        [pl.col(c).sum().alias(c) for c in comp] + [pl.len().alias("n_games")]
    )
    exprs = []
    for name, (num, den) in spec["rates"].items():
        if num in g.columns and den in g.columns:
            exprs.append(
                pl.when(pl.col(den) > 0).then(pl.col(num) / pl.col(den)).otherwise(None).alias(name)
            )
    return g.with_columns(exprs)


def build_reliability_report(
    seasons: list[int] | None = None, families: list[str] | None = None
) -> pl.DataFrame:
    seasons = seasons or list(range(2016, 2025))
    families = families or list(FAMILY_SPECS)
    rows: list[dict] = []

    for family in families:
        min_g = _MIN_GAMES.get(family, 8)
        gm = _entity_season_games(family, seasons)
        if gm.is_empty():
            continue
        elig = (
            gm.group_by(["entity_id", "season"]).agg(pl.len().alias("n"))
            .filter(pl.col("n") >= min_g)
        )
        gm = gm.join(elig.select("entity_id", "season"), on=["entity_id", "season"])
        odd = _agg_rates(gm.filter(pl.col("gidx") % 2 == 1), family)
        even = _agg_rates(gm.filter(pl.col("gidx") % 2 == 0), family)
        first = _agg_rates(
            gm.join(elig, on=["entity_id", "season"]).filter(pl.col("gidx") < (pl.col("n") // 2)),
            family,
        )
        second = _agg_rates(
            gm.join(elig, on=["entity_id", "season"]).filter(pl.col("gidx") >= (pl.col("n") // 2)),
            family,
        )
        # retrospective STD-vs-rest
        std_part = _agg_rates(gm.filter(pl.col("week") <= _STD_SPLIT_WEEK), family)
        rest_part = _agg_rates(gm.filter(pl.col("week") > _STD_SPLIT_WEEK), family)

        for name in FAMILY_SPECS[family]["rates"]:
            for method, left, right, retro in (
                ("odd_even", odd, even, False),
                ("first_second_half", first, second, False),
                ("std_vs_rest_of_season", std_part, rest_part, True),
            ):
                if name not in left.columns or name not in right.columns:
                    continue
                j = left.select("entity_id", "season", pl.col(name).alias("a")).join(
                    right.select("entity_id", "season", pl.col(name).alias("b")),
                    on=["entity_id", "season"],
                )
                pear, spear, n = _corr(j.get_column("a").to_numpy(), j.get_column("b").to_numpy())
                rows.append({
                    "family": family, "metric": name, "method": method,
                    "n_pairs": n, "pearson": pear, "spearman": spear,
                    "spearman_brown_pearson": _spearman_brown(pear) if not retro else None,
                    "is_retrospective": retro,
                    "seasons": f"{seasons[0]}-{seasons[-1]}",
                    "note": "RETROSPECTIVE — uses future observations; never feeds production"
                    if retro else "descriptive stability only; not predictive value",
                })
    return pl.DataFrame(rows).sort(["family", "metric", "method"])
