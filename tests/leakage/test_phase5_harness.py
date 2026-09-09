"""Phase 5 leakage / integrity suite (spec section 26)."""
from __future__ import annotations

import polars as pl
import pytest

from matchup.metrics.build import clear_metric_caches
from matchup.store import clear_cache
from matchup.validation.phase5 import (
    build_matchup_observations,
    future_row_poison_check,
    load_phase5_config,
    resolve_matchup_universe,
)

pytestmark = [pytest.mark.network]
CFG5 = load_phase5_config()
_PAIRS = {d["name"]: d for d in CFG5["matchup_definitions"]}


@pytest.fixture(autouse=True)
def _clean():
    clear_cache(); clear_metric_caches()
    yield
    clear_cache(); clear_metric_caches()


def test_config_is_frozen():
    assert CFG5["frozen"] is True


def test_no_previously_rejected_metric_resolves():
    """Every resolved matchup uses two SHRINKAGE_ADDS_VALUE units from Phase 4."""
    u = resolve_matchup_universe()
    assert u.filter(pl.col("resolved")).height >= 2
    for r in u.filter(pl.col("resolved")).iter_rows(named=True):
        assert r["off_shrinkage_status"] == "SHRINKAGE_ADDS_VALUE"
        assert r["def_shrinkage_status"] == "SHRINKAGE_ADDS_VALUE"


def test_matchup_observations_are_well_formed():
    m = build_matchup_observations(_PAIRS["overall_epa"])
    assert not m.is_empty()
    assert m.get_column("season").min() >= 2016
    assert m.get_column("season").max() <= 2025
    # team-vs-team matchup: A never faces itself
    assert (m.get_column("entity_id") != m.get_column("opp_entity")).all()
    # A, B and the target are always present (never zero-imputed)
    for c in ("A", "B", "target_value", "mu_A"):
        assert m.get_column(c).null_count() == 0
    # one row per (entity, target game, horizon)
    assert m.select("entity_id", "target_game_id", "horizon").is_duplicated().sum() == 0


def test_no_market_columns_anywhere():
    banned = {"spread_line", "total_line", "spread", "moneyline", "vegas_wp", "odds",
              "result", "total", "away_score", "home_score"}
    for name in ("overall_epa", "qb_vs_pass_defense_epa", "protection_vs_rush_hit"):
        m = build_matchup_observations(_PAIRS[name])
        assert not banned.intersection(m.columns)


def test_opposing_unit_is_the_actual_opponent():
    """B must be the unit A plays in the target game -- cross-check against the
    team game sequence."""
    from matchup.pointintime.calendar import build_team_game_sequence

    m = build_matchup_observations(_PAIRS["overall_epa"])
    seq = build_team_game_sequence().select(
        pl.col("game_id"), pl.col("team"), pl.col("opponent"))
    j = m.join(seq, left_on=["target_game_id", "entity_id"],
               right_on=["game_id", "team"], how="inner")
    assert (j.get_column("opp_entity") == j.get_column("opponent")).all()


def test_future_row_poison_canary():
    for name in ("overall_epa", "pass_game_success"):
        r = future_row_poison_check(_PAIRS[name])
        assert r["status"] == "pass"


@pytest.mark.slow
def test_end_to_end_runs_and_emits_one_verdict(tmp_path, monkeypatch):
    import matchup.validation.phase5 as p5

    monkeypatch.setattr(p5, "OUT", tmp_path)
    out = p5.run_phase5(bootstrap_iters=60)
    assert out["verdict"] in {"APPROVE_PHASE_5", "REVISE_PHASE_5", "STOP_NO_RELIABLE_MATCHUP_SIGNAL"}
    for f in ("phase5_status.csv", "phase5_baseline_results.csv",
              "phase5_interaction_results.csv", "phase5_negative_controls.csv",
              "phase5_fdr.csv", "phase5_summary.json"):
        assert (tmp_path / f).exists()
