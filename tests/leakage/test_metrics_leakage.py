"""Phase 2 leakage suite -- the poisoned-future-row canary extended to every
production metric layer, plus earliest_valid_season / NGS week-0 / CPOE-denominator
invariants.
"""
from __future__ import annotations

import polars as pl
import pytest

from matchup.metrics.build import game_metrics_from_asof, offline_provider
from matchup.metrics.external import ngs_player_week
from matchup.metrics.windows import window_metric
from matchup.normalize.normalize import normalize_windowed
from matchup.pointintime.asof import AsOf
from matchup.pointintime.calendar import build_game_calendar
from matchup.store import clear_cache

pytestmark = [pytest.mark.network]

FAMILIES = ["qb", "rb", "wr", "team_offense", "team_defense", "pass_protection",
            "pass_rush", "special_teams"]


def _kick(team, season, week):
    return (
        build_game_calendar()
        .filter((pl.col("season") == season) & (pl.col("week") == week)
                & ((pl.col("home_team") == team) | (pl.col("away_team") == team)))
        .get_column("kickoff_utc").item()
    )


@pytest.fixture(autouse=True)
def _clean():
    clear_cache()
    yield
    clear_cache()


@pytest.mark.parametrize("family", FAMILIES)
def test_every_game_metric_row_predates_target_kickoff(family):
    kick = _kick("KC", 2024, 10)
    gm = game_metrics_from_asof(AsOf(asof_utc=kick), family)
    if gm.is_empty() or "data_asof" not in gm.columns:
        pytest.skip(f"{family}: no rows")
    assert gm.filter(pl.col("data_asof") >= pl.lit(kick)).height == 0


@pytest.mark.parametrize("family", ["qb", "team_offense"])
def test_windowed_and_normalized_rows_predate_kickoff(family):
    kick = _kick("KC", 2024, 10)
    gm = game_metrics_from_asof(AsOf(asof_utc=kick), family)
    eid = "00-0033873" if family == "qb" else "KC"
    for w in ("season_to_date", "trailing_3", "trailing_5", "prior_season"):
        row = window_metric(family, gm, entity_id=eid, target_season=2024,
                            target_week=10, target_kickoff=kick, window=w)
        if row.is_empty():
            continue
        assert row["data_asof"].item() < kick
        metric = "epa_per_dropback" if family == "qb" else "epa_per_play"
        out = normalize_windowed(row, family, metric, asof_utc=kick,
                                 ref_game_metrics_provider=offline_provider(family))
        assert out["data_asof"].item() < kick
        assert max(out["ref_seasons"].item()) < 2024


def test_ngs_week_zero_excluded_from_metrics():
    kick = _kick("KC", 2024, 10)
    ao = AsOf(asof_utc=kick)
    for stat in ("passing", "receiving", "rushing"):
        df = ngs_player_week(ao, stat)
        if df.height:
            assert (df.get_column("week") > 0).all()
            assert (df.get_column("data_asof") < kick).all()


def test_earliest_valid_season_surfaced_on_windowed_rows():
    kick = _kick("KC", 2024, 10)
    gm = game_metrics_from_asof(AsOf(asof_utc=kick), "qb")
    row = window_metric("qb", gm, entity_id="00-0033873", target_season=2024,
                        target_week=10, target_kickoff=kick, window="season_to_date")
    assert row["earliest_valid_season"].item() == 1999
    ng = ngs_player_week(AsOf(asof_utc=kick), "passing")
    if ng.height:
        assert (ng.get_column("earliest_valid_season") == 2016).all()


def test_cpoe_denominator_is_attempts_with_cpoe_not_all_throws():
    kick = _kick("KC", 2024, 10)
    gm = game_metrics_from_asof(AsOf(asof_utc=kick), "qb")
    row = window_metric("qb", gm, entity_id="00-0033873", target_season=2024,
                        target_week=10, target_kickoff=kick, window="season_to_date").to_dicts()[0]
    assert row["cpoe_attempt_count"] <= row["throws"]
    assert 0.0 < row["cpoe_coverage_fraction"] <= 1.0
    # cpoe recomputed from summed components: cpoe_sum / cpoe_n
    assert abs(row["cpoe"] - row["cpoe_sum"] / row["cpoe_n"]) < 1e-9


def test_poisoned_future_row_canary_metrics(monkeypatch):
    """A fabricated future game + future-dated plays must not change any earlier
    game/windowed/normalized metric."""
    from matchup import store

    kick = _kick("KC", 2024, 10)
    ao = AsOf(asof_utc=kick)
    base = {f: game_metrics_from_asof(ao, f) for f in ("qb", "team_offense")}
    base_hash = {f: v.hash_rows().sum() for f, v in base.items()}
    base_win = window_metric("qb", base["qb"], entity_id="00-0033873", target_season=2024,
                             target_week=10, target_kickoff=kick, window="season_to_date")
    base_win_hash = base_win.hash_rows().sum()

    real = store.load_source

    def poisoned(source, seasons=None, columns=None, use_cache=True):
        df = real(source, seasons=seasons, columns=columns, use_cache=False)
        if df.is_empty():
            return df
        if source == "schedules":
            poison = df.filter(pl.col("game_id") == "2024_10_DEN_KC").with_columns(
                pl.lit("2024_99_KC_XX").alias("game_id"), pl.lit(99).alias("week"),
                pl.lit("2025-01-15").alias("gameday"),
            )
            return pl.concat([df, poison], how="diagonal_relaxed")
        if source == "pbp":
            poison = df.filter(pl.col("game_id") == "2024_05_KC_NO").with_columns(
                pl.lit("2024_99_KC_XX").alias("game_id"), pl.lit(99).alias("week"),
                pl.lit("2025-01-15").alias("game_date"),
            )
            return pl.concat([df, poison], how="diagonal_relaxed")
        return df

    clear_cache()
    for mod in ("matchup.store", "matchup.pointintime.calendar", "matchup.pointintime.asof"):
        monkeypatch.setattr(f"{mod}.load_source", poisoned) if mod != "matchup.store" \
            else monkeypatch.setattr(store, "load_source", poisoned)
    import matchup.metrics.build as mb
    monkeypatch.setattr(mb, "load_source", poisoned)
    mb._raw_pbp.cache_clear()
    mb._classified.cache_clear()

    ao2 = AsOf(asof_utc=kick)
    for f in ("qb", "team_offense"):
        assert game_metrics_from_asof(ao2, f).hash_rows().sum() == base_hash[f]
    win2 = window_metric("qb", game_metrics_from_asof(ao2, "qb"), entity_id="00-0033873",
                         target_season=2024, target_week=10, target_kickoff=kick,
                         window="season_to_date")
    assert win2.hash_rows().sum() == base_win_hash
