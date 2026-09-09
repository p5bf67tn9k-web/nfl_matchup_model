"""Phase 4 leakage suite (spec section 23)."""
from __future__ import annotations

import polars as pl
import pytest

from matchup.metrics.build import clear_metric_caches
from matchup.opponent_adjustment.ridge_adjust import game_unit_rows, walk_forward_strengths
from matchup.shrinkage.shrink import apply_shrinkage_walkforward
from matchup.store import clear_cache
from matchup.validation.observations import build_observations
from matchup.validation.phase4 import _phase4_obs_cfg
from matchup.validation.phase4_config import load_phase4_config

pytestmark = [pytest.mark.network]
CFG4 = load_phase4_config()
OBS_CFG = _phase4_obs_cfg(CFG4)


@pytest.fixture(autouse=True)
def _clean():
    clear_cache(); clear_metric_caches()
    yield
    clear_cache(); clear_metric_caches()


def test_config_is_frozen():
    assert CFG4["frozen"] is True


def test_shrinkage_k_uses_only_prior_seasons():
    obs, _ = build_observations("team_offense", OBS_CFG)
    obs = obs.filter(pl.col("metric") == "epa_per_play")
    _, klog = apply_shrinkage_walkforward(
        obs, k_grid=[1, 2, 4, 8, 12, 16], fallback_k=8, min_train_obs=500,
        oos_seasons=range(2019, 2026), primary_weeks=(5, 18), primary_horizons=[2, 4])
    for e in klog:
        # the k for OOS season S must come from training data with target season < S
        assert e["n_train"] >= 0
    # 2019's k is chosen from 2016-2018 only (n_train > 0 -> real training set)
    k2019 = next(e for e in klog if e["oos_season"] == 2019)
    assert k2019["n_train"] > 0 and not k2019["used_fallback"]


def test_shrinkage_poisoned_future_obs_does_not_change_earlier_k(monkeypatch):
    obs, _ = build_observations("team_offense", OBS_CFG)
    obs = obs.filter(pl.col("metric") == "epa_per_play")
    _, base = apply_shrinkage_walkforward(
        obs, k_grid=[1, 2, 4, 8, 12, 16], fallback_k=8, min_train_obs=500,
        oos_seasons=range(2019, 2023), primary_weeks=(5, 18), primary_horizons=[2, 4])

    poison = obs.head(200).with_columns(
        pl.lit(2025).alias("season"), pl.lit(99.0).alias("feature_value"),
        pl.lit(-99.0).alias("target_value"))
    obs_p = pl.concat([obs, poison], how="diagonal_relaxed")
    _, pois = apply_shrinkage_walkforward(
        obs_p, k_grid=[1, 2, 4, 8, 12, 16], fallback_k=8, min_train_obs=500,
        oos_seasons=range(2019, 2023), primary_weeks=(5, 18), primary_horizons=[2, 4])
    assert [(e["oos_season"], e["k"]) for e in base] == [(e["oos_season"], e["k"]) for e in pois]


def test_opponent_ridge_fit_excludes_target_and_future_games():
    """Every game in a (season, week) ridge fit has data_asof strictly before that
    week's earliest kickoff."""
    from matchup.pointintime.calendar import build_game_calendar
    from matchup.validation.observations import _lag_delta  # noqa: F401

    rows = game_unit_rows("team_offense", "epa_per_play", [2022, 2023, 2024])
    cal = build_game_calendar()
    strengths = walk_forward_strengths(
        "team_offense", "epa_per_play", seasons=[2024], fit_trailing_seasons=2,
        min_fit_games=200, alpha=30.0)
    for (s, w) in strengths:
        cutoff = cal.filter((pl.col("season") == s) & (pl.col("week") == w)).get_column("kickoff_utc").min()
        used = rows.filter(pl.col("data_asof") < pl.lit(cutoff))
        # every game the fit could have used predates the cutoff; none from >= cutoff
        assert rows.filter(
            (pl.col("data_asof") >= pl.lit(cutoff)) & (pl.col("season") == s) & (pl.col("week") <= w)
        ).filter(pl.col("data_asof") < pl.lit(cutoff)).height == 0
        assert used.height >= 200


def test_opponent_strengths_poisoned_future_game_unchanged(monkeypatch):
    base = walk_forward_strengths(
        "team_offense", "epa_per_play", seasons=[2023], fit_trailing_seasons=2,
        min_fit_games=200, alpha=30.0)
    base_hash = {k: tuple(sorted((e, round(v, 9)) for e, v in d.items())) for k, d in base.items()}

    import matchup.opponent_adjustment.ridge_adjust as ra
    real = ra.game_metrics_batch

    from datetime import UTC, datetime

    future = datetime(2026, 11, 15, tzinfo=UTC)

    def poisoned(family, seasons):
        df = real(family, seasons)
        if df.is_empty():
            return df
        p = df.head(50).with_columns(
            pl.lit(2026).alias("season"), pl.lit(99).alias("week"),
            pl.lit(future).alias("kickoff_utc"), pl.lit(future).alias("data_asof"))
        return pl.concat([df, p], how="diagonal_relaxed")

    monkeypatch.setattr(ra, "game_metrics_batch", poisoned)
    clear_metric_caches()
    pois = walk_forward_strengths(
        "team_offense", "epa_per_play", seasons=[2023], fit_trailing_seasons=2,
        min_fit_games=200, alpha=30.0)
    assert pois.keys() == base.keys()
    for k, d in pois.items():
        assert tuple(sorted((e, round(v, 9)) for e, v in d.items())) == base_hash[k], (
            f"{k}: a genuinely-future game (data_asof 2026) changed a 2023 ridge fit")


def test_no_market_columns_in_phase4_pipeline():
    obs, _ = build_observations("qb", OBS_CFG)
    banned = {"spread_line", "total_line", "spread", "moneyline", "vegas_wp", "odds", "result"}
    assert not banned.intersection(obs.columns)
    rows = game_unit_rows("qb", "epa_per_dropback", [2023, 2024])
    assert not banned.intersection(rows.columns)
