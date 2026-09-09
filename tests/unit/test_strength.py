"""Unit tests for the team-strength research layer."""
from __future__ import annotations

import numpy as np
import polars as pl
import pytest

from matchup.strength.config import DOMAINS, STRENGTH_METRICS, orient_sign
from matchup.strength.team_metrics import confidence_label
from matchup.strength.team_strength import team_strength_snapshot


def test_config_is_coherent():
    for full, spec in STRENGTH_METRICS.items():
        assert "." in full
        assert spec["direction"] in {"higher_better", "lower_better", "neutral"}
        assert spec["k"] > 0
    for dom, spec in DOMAINS.items():
        assert spec["side"] in {"offense", "defense", "special"}
        assert spec["label"].endswith("Index")
        for m in spec["metrics"]:
            assert m in STRENGTH_METRICS, f"{dom} references unknown metric {m}"
            assert STRENGTH_METRICS[m]["in_index"], f"{m} in a domain but in_index=false"


def test_orientation_signs():
    assert orient_sign("team_offense.epa_per_play") == 1        # higher better
    assert orient_sign("team_defense.epa_per_play") == -1       # lower better (allowed)
    assert orient_sign("pass_protection.sack_rate_allowed") == -1
    assert orient_sign("pass_rush.sack_rate_generated") == 1
    assert orient_sign("team_offense.proe") == 0                # neutral -> excluded


def test_confidence_label():
    assert confidence_label(0, 0) == "prior_season_only"
    assert confidence_label(1, 1) == "low"
    assert confidence_label(4, 5) == "medium"
    assert confidence_label(9, 10) == "high"


def _synthetic_metrics_long() -> pl.DataFrame:
    """4 teams, 1 season, weeks 0..6, two in-index metrics with known z-scores."""
    rows = []
    metrics = {
        "team_offense.epa_per_play": (1, True),
        "team_defense.epa_per_play": (-1, True),
    }
    rng = np.random.default_rng(0)
    for team, base in zip("ABCD", [0.2, 0.1, -0.1, -0.2], strict=True):
        for wk in range(7):
            for metric, (sign, in_idx) in metrics.items():
                raw = base + rng.normal(0, 0.02)
                ref_mean, ref_sd, k = 0.0, 0.1, 8
                n = max(wk, 1)
                shrunk = ref_mean + n / (n + k) * (raw - ref_mean)
                rows.append({
                    "season": 2025, "team": team, "week": wk, "metric": metric,
                    "family": metric.split(".")[0], "metric_bare": metric.split(".")[1],
                    "direction": "higher_better" if sign > 0 else "lower_better",
                    "n_games": n, "n_opportunities": n * 60, "raw_value": raw,
                    "ref_mean": ref_mean, "ref_sd": ref_sd, "ref_n": 30,
                    "ref_seasons": "2022,2023,2024", "k": k, "shrunk_value": shrunk,
                    "z_raw": (raw - ref_mean) / ref_sd,
                    "z_shrunk": (shrunk - ref_mean) / ref_sd,
                    "oriented_z_shrunk": sign * (shrunk - ref_mean) / ref_sd,
                    "in_index": in_idx, "phase3_status": "VALIDATED_PERSISTENCE",
                })
    return pl.DataFrame(rows)


def test_index_is_mean_of_member_oriented_z():
    ml = _synthetic_metrics_long()
    snap = team_strength_snapshot(ml, 2025, 6)
    dom = snap["domains"]
    off = dom.filter((pl.col("team") == "A") & (pl.col("domain") == "offense_overall"))
    # offense_overall has 3 defined members but only epa_per_play is present here
    members = snap["metrics"].filter(
        (pl.col("team") == "A") & (pl.col("metric") == "team_offense.epa_per_play")
    )
    assert off.get_column("index_value").item() == pytest.approx(
        members.get_column("oriented_z_shrunk").item(), rel=1e-9
    )
    assert off.get_column("n_metrics_used").item() == 1
    assert off.get_column("n_metrics_defined").item() == 3


def test_snapshot_ranks_best_team_first():
    ml = _synthetic_metrics_long()
    snap = team_strength_snapshot(ml, 2025, 6)
    off = snap["domains"].filter(pl.col("domain") == "offense_overall").sort("rank_of_league")
    assert off.get_column("team").to_list()[0] == "A"   # highest oriented z
    assert off.get_column("team").to_list()[-1] == "D"


def test_preseason_snapshot_uses_week_zero():
    ml = _synthetic_metrics_long()
    snap = team_strength_snapshot(ml, 2025, 0)
    assert not snap["domains"].is_empty()
    assert snap["metrics"].get_column("week").max() == 0
    assert set(snap["metrics"].get_column("confidence").unique()) == {"prior_season_only"}


@pytest.mark.network
def test_real_pipeline_shapes_and_orientation():
    from matchup.strength.team_metrics import build_team_metrics_weekly

    ml = build_team_metrics_weekly([2024, 2025])
    assert not ml.is_empty()
    assert ml.get_column("week").min() == 0
    # a strong offense should have positive oriented z on offense epa, a strong
    # defense negative raw z but positive oriented z
    d = ml.filter((pl.col("metric") == "team_defense.epa_per_play") & (pl.col("week") == 0))
    good = d.sort("oriented_z_shrunk", descending=True).head(1)
    assert good.get_column("z_shrunk").item() < 0        # allowed less EPA than average
    assert good.get_column("oriented_z_shrunk").item() > 0
