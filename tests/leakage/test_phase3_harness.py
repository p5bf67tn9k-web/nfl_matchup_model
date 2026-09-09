"""Phase 3 walk-forward harness leakage suite (spec section 14)."""
from __future__ import annotations

import numpy as np
import polars as pl
import pytest

from matchup.metrics.build import clear_metric_caches, game_metrics_batch
from matchup.store import clear_cache
from matchup.validation.config import load_phase3_config
from matchup.validation.observations import _lag_delta, build_observations

pytestmark = [pytest.mark.network]

CFG = load_phase3_config()
HIST = tuple(range(CFG["seasons"]["history_available_from"], CFG["seasons"]["eval_end"] + 1))


@pytest.fixture(autouse=True)
def _clean():
    clear_cache(); clear_metric_caches()
    yield
    clear_cache(); clear_metric_caches()


def test_config_is_frozen():
    assert CFG["frozen"] is True


def test_every_feature_game_predates_target_kickoff():
    """For each candidate target game, the games that feed the feature (the first
    `a` in kickoff order, a = searchsorted(kickoff, target_kick - lag)) all have
    data_asof strictly before the target kickoff; the first EXCLUDED game does not."""
    gm = game_metrics_batch("team_offense", HIST).sort(["entity_id", "kickoff_utc"])
    lag = _lag_delta("team_offense")
    checked = 0
    for _, sub in gm.group_by("entity_id"):
        kick = sub.get_column("kickoff_utc").to_numpy()
        asof = sub.get_column("data_asof").to_numpy()
        for t in range(len(kick)):
            if not (2019 <= int(sub.get_column("season")[t]) <= CFG["seasons"]["eval_end"]):
                continue
            avail_cut = np.datetime64(kick[t]) - np.timedelta64(int(lag.total_seconds()), "s")
            a = int(np.searchsorted(kick, avail_cut, side="left"))
            assert np.all(asof[:a] < kick[t]), "a feeding game has data_asof >= target kickoff"
            if a < len(kick):
                assert asof[a] >= kick[t], "an available game was wrongly excluded"
            checked += 1
    assert checked > 500


def test_no_target_row_leaks_into_a_feature():
    """Every observation's feature window closes strictly before the target
    kickoff: max(feature game data_asof) < target kickoff."""
    obs, _ = build_observations("qb", CFG)
    assert not obs.is_empty()
    d = obs.with_columns(
        pl.col("feat_data_asof").str.to_datetime(strict=False),
        pl.col("target_kickoff").str.to_datetime(strict=False),
    )
    assert d.filter(pl.col("feat_data_asof") >= pl.col("target_kickoff")).height == 0


_OBS_KEYS = ["entity_id", "target_game_id", "metric", "window", "horizon"]


def test_poisoned_future_game_does_not_change_earlier_observations(monkeypatch):
    base, _ = build_observations("team_offense", CFG)
    base = base.filter(pl.col("season") <= 2023).sort(_OBS_KEYS)

    from matchup import store
    real = store.load_source

    def poisoned(source, seasons=None, columns=None, use_cache=True):
        df = real(source, seasons=seasons, columns=columns, use_cache=False)
        if df.is_empty():
            return df
        if source == "schedules":
            p = df.filter(pl.col("game_id") == "2024_10_DEN_KC").with_columns(
                pl.lit("2026_10_KC_ZZ").alias("game_id"), pl.lit(2026).alias("season"),
                pl.lit(10).alias("week"), pl.lit("2026-11-15").alias("gameday"),
            )
            return pl.concat([df, p], how="diagonal_relaxed")
        if source == "pbp":
            p = df.filter(pl.col("game_id") == "2024_10_DEN_KC").with_columns(
                pl.lit("2026_10_KC_ZZ").alias("game_id"), pl.lit(2026).alias("season"),
                pl.lit(10).alias("week"), pl.lit("2026-11-15").alias("game_date"),
            )
            return pl.concat([df, p], how="diagonal_relaxed")
        return df

    for mod in ("matchup.store", "matchup.pointintime.calendar", "matchup.pointintime.asof",
                "matchup.metrics.build"):
        target = store if mod == "matchup.store" else __import__(mod, fromlist=["load_source"])
        monkeypatch.setattr(target, "load_source", poisoned)
    clear_cache(); clear_metric_caches()

    pois, _ = build_observations("team_offense", CFG)
    pois = pois.filter(pl.col("season") <= 2023).sort(_OBS_KEYS)

    # the observation SET is identical (no new/removed earlier observations)
    assert pois.select(_OBS_KEYS).equals(base.select(_OBS_KEYS))
    # and every numeric value is unchanged to within floating-point noise
    # (parallel group-by sums are not bit-reproducible when row counts shift)
    j = base.join(pois, on=_OBS_KEYS, suffix="_p")
    for col in ("feature_value", "target_value", "baseline_league"):
        d = (j.get_column(col) - j.get_column(f"{col}_p")).abs().max()
        assert d < 1e-9, f"{col} changed by {d} after injecting a future game"


def test_no_market_columns_anywhere_in_observations():
    obs, _ = build_observations("qb", CFG)
    banned = {"spread_line", "total_line", "spread", "total", "moneyline", "vegas_wp",
              "home_score", "away_score", "result", "odds"}
    assert not banned.intersection(obs.columns)
