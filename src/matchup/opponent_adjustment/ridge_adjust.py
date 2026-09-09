"""Game-level ridge opponent adjustment + walk-forward alpha selection.

Speed: for a fixed design X, ridge coefficients for many alphas come from one
normal-equation build (X'X, X'y) plus a small linear solve per alpha, so the
per-week design is built once and reused across the alpha grid.
"""
from __future__ import annotations

from datetime import datetime

import numpy as np
import polars as pl

from matchup.metrics.build import game_metrics_batch
from matchup.pointintime.calendar import build_game_calendar, build_team_game_sequence
from matchup.validation.observations import _lag_delta


def game_unit_rows(family: str, metric: str, seasons: list[int]) -> pl.DataFrame:
    """One row per (entity, game): the entity's single-game ``metric`` value, the
    opponent (opposing TEAM), home flag, kickoff, production ``data_asof``."""
    gm = game_metrics_batch(family, tuple(sorted(seasons)))
    if gm.is_empty() or metric not in gm.columns:
        return pl.DataFrame()
    seq = build_team_game_sequence().select(
        "game_id", pl.col("team").alias("_team"), "opponent", "is_home"
    )
    team_col = "team" if "team" in gm.columns else "entity_id"
    j = gm.join(seq, left_on=["game_id", team_col], right_on=["game_id", "_team"], how="left")
    return j.select(
        "entity_id", "game_id", "season", "week", pl.col(metric).alias("y"),
        "opponent", pl.col("is_home").cast(pl.Int8).fill_null(0).alias("home"),
        "kickoff_utc", "data_asof",
    ).drop_nulls(["y", "opponent"])


class _Design:
    """One-hot design (entity, opponent, home) with cached normal equations."""

    def __init__(self, rows: pl.DataFrame, *, permute_opponents: bool = False, seed: int = 0):
        ent = rows.get_column("entity_id").to_list()
        opp = rows.get_column("opponent").to_list()
        if permute_opponents:
            opp = list(np.random.default_rng(seed).permutation(opp))
        home = rows.get_column("home").to_numpy().astype(float)
        y = rows.get_column("y").to_numpy().astype(float)

        self.ent_levels = sorted(set(ent))
        opp_levels = sorted(set(opp))
        ei = {e: i for i, e in enumerate(self.ent_levels)}
        oi = {o: i for i, o in enumerate(opp_levels)}
        n, p = len(y), len(self.ent_levels) + len(opp_levels) + 1
        X = np.zeros((n, p))
        rr = np.arange(n)
        X[rr, [ei[e] for e in ent]] = 1.0
        X[rr, [len(self.ent_levels) + oi[o] for o in opp]] = 1.0
        X[:, -1] = home
        Xc = np.hstack([np.ones((n, 1)), X])           # + intercept
        self.XtX = Xc.T @ Xc
        self.Xty = Xc.T @ y
        self.p = Xc.shape[1]
        self.n_ent = len(self.ent_levels)

    def strengths(self, alpha: float) -> dict[str, float]:
        reg = alpha * np.eye(self.p)
        reg[0, 0] = 0.0                                 # do not penalise the intercept
        beta = np.linalg.solve(self.XtX + reg, self.Xty)
        s = beta[0] + beta[1 : 1 + self.n_ent]          # intercept + entity coefs
        s = s - s.mean()
        return dict(zip(self.ent_levels, s, strict=True))


def _week_cutoffs(seasons: list[int]) -> dict[int, list[tuple[int, datetime]]]:
    cal = build_game_calendar()
    out: dict[int, list[tuple[int, datetime]]] = {}
    for s in seasons:
        wk = (cal.filter(pl.col("season") == s).group_by("week")
              .agg(pl.col("kickoff_utc").min().alias("k")).sort("week"))
        out[s] = [(int(r["week"]), r["k"]) for r in wk.iter_rows(named=True)]
    return out


def walk_forward_strengths(
    family: str, metric: str, *, seasons: list[int], fit_trailing_seasons: int,
    min_fit_games: int, alpha: float, permute_opponents: bool = False, seed: int = 0,
) -> dict[tuple[int, int], dict[str, float]]:
    rows = game_unit_rows(family, metric, list(range(min(seasons) - fit_trailing_seasons, max(seasons) + 1)))
    if rows.is_empty():
        return {}
    cutoffs = _week_cutoffs(seasons)
    out: dict[tuple[int, int], dict[str, float]] = {}
    for s in seasons:
        for w, cutoff in cutoffs[s]:
            train = rows.filter(
                (pl.col("data_asof") < pl.lit(cutoff))
                & (pl.col("season") > s - 1 - fit_trailing_seasons)
            )
            if train.height < min_fit_games:
                continue
            out[(s, w)] = _Design(train, permute_opponents=permute_opponents,
                                  seed=seed + s * 100 + w).strengths(alpha)
    return out


def select_alpha(
    family: str, metric: str, *, train_seasons: list[int], alpha_grid: list[float],
    fit_trailing_seasons: int, min_fit_games: int, primary_weeks: tuple[int, int],
) -> tuple[float, dict[float, float]]:
    """Pick alpha minimising pooled next-game (H1) RMSE of the adjusted strength
    over ``train_seasons`` (all strictly before the OOS period)."""
    rows = game_unit_rows(
        family, metric,
        list(range(min(train_seasons) - fit_trailing_seasons, max(train_seasons) + 1)),
    )
    if rows.is_empty():
        return alpha_grid[len(alpha_grid) // 2], {}
    plo, phi = primary_weeks
    cutoffs = _week_cutoffs(train_seasons)
    pooled: dict[float, list[tuple[float, float]]] = {a: [] for a in alpha_grid}
    for s in train_seasons:
        for w, cutoff in cutoffs[s]:
            if not (plo <= w <= phi):
                continue
            prior = rows.filter(
                (pl.col("data_asof") < pl.lit(cutoff))
                & (pl.col("season") > s - 1 - fit_trailing_seasons)
            )
            nxt = rows.filter((pl.col("season") == s) & (pl.col("week") == w))
            if prior.height < min_fit_games or nxt.is_empty():
                continue
            d = _Design(prior)
            yv = nxt.get_column("y").to_numpy()
            yc = yv - yv.mean()
            ents = nxt.get_column("entity_id").to_list()
            for a in alpha_grid:
                st = d.strengths(a)
                for e, yy in zip(ents, yc, strict=True):
                    if e in st:
                        pooled[a].append((st[e], yy))
    scored = {a: float(np.sqrt(np.mean((np.array(p)[:, 0] - np.array(p)[:, 1]) ** 2)))
              for a, p in pooled.items() if len(p) >= 50}
    if not scored:
        return alpha_grid[len(alpha_grid) // 2], {}
    return min(scored, key=scored.get), scored


def _lag(family: str):  # kept for callers/tests
    return _lag_delta(family)
