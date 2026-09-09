"""Tests for the matchup-card presentation layer.

These tests use small synthetic fixture files (not the real generated
outputs) so they run without `make weekly-research`/network access, and so
missing-data / ordering behavior can be constructed deterministically. Domain
ids are pulled from the REAL config/strength.yaml (matchup.strength.config)
since the visualization layer must use the repo's existing domain structure.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

from matchup.strength.config import DOMAINS
from matchup.visualization.data import (
    MatchupDataError,
    compute_matchup_comparisons,
    identify_key_battles,
    load_matchup_card_data,
    team_identity_statements,
)
from matchup.visualization.matchup_card import build_figure
from matchup.visualization.styles import fmt_index, fmt_percentile, fmt_rank

DOMAIN_IDS = list(DOMAINS.keys())
SEASON = 2099
WEEK = 1


def _write_summary(tmp_path: Path, *, through_week: int = WEEK, mode: str = "in_season") -> Path:
    p = tmp_path / "weekly_summary.json"
    p.write_text(json.dumps({
        "season": SEASON, "through_week": through_week, "mode": mode,
        "generated_at": "2099-01-01T00:00:00+00:00",
    }))
    return p


def _write_team_snapshot(tmp_path: Path, teams: dict[str, dict]) -> Path:
    p = tmp_path / "weekly_team_snapshot.csv"
    cols = ["team", "games", "wins", "losses", "ties", "points_for", "points_against",
            "point_diff", "overall_confidence", "top_strength_domain", "top_strength_index",
            "top_weakness_domain", "top_weakness_index", "season", "through_week"]
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for team, extra in teams.items():
            row = {"team": team, "games": 1, "wins": 1, "losses": 0, "ties": 0,
                   "points_for": 24, "points_against": 17, "point_diff": 7,
                   "overall_confidence": "low", "season": SEASON, "through_week": WEEK}
            row.update(extra)
            w.writerow(row)
    return p


def _write_domain_changes(tmp_path: Path, team_domain_values: dict[str, dict[str, float | None]]) -> Path:
    """team_domain_values: {team: {domain_id: index_value_or_None}}. Any domain not
    present for a team is simply omitted (-> missing/N/A downstream)."""
    p = tmp_path / "weekly_changes.csv"
    cols = ["team", "domain", "side", "label", "index_value", "rank_of_league",
            "n_metrics_used", "n_metrics_defined", "min_confidence", "season", "through_week"]
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for team, dom_vals in team_domain_values.items():
            for dom_id in DOMAIN_IDS:
                if dom_id not in dom_vals or dom_vals[dom_id] is None:
                    continue
                value = dom_vals[dom_id]
                # rank: better (higher) value -> better rank among the fixture teams
                peers = sorted(
                    (t for t in team_domain_values if dom_id in team_domain_values[t]
                     and team_domain_values[t][dom_id] is not None),
                    key=lambda t: team_domain_values[t][dom_id], reverse=True,
                )
                rank = peers.index(team) + 1
                w.writerow({
                    "team": team, "domain": dom_id, "side": DOMAINS[dom_id]["side"],
                    "label": DOMAINS[dom_id]["label"], "index_value": value,
                    "rank_of_league": rank, "n_metrics_used": 2, "n_metrics_defined": 2,
                    "min_confidence": "low", "season": SEASON, "through_week": WEEK,
                })
    return p


def _default_fixture(tmp_path: Path, *, away="AAA", home="BBB",
                      away_vals: dict | None = None, home_vals: dict | None = None):
    away_vals = away_vals if away_vals is not None else {d: 0.5 for d in DOMAIN_IDS}
    home_vals = home_vals if home_vals is not None else {d: -0.3 for d in DOMAIN_IDS}
    summary_path = _write_summary(tmp_path)
    snap_path = _write_team_snapshot(tmp_path, {
        away: {"top_strength_domain": "passing_offense", "top_strength_index": away_vals.get("passing_offense"),
               "top_weakness_domain": "rushing_defense", "top_weakness_index": away_vals.get("rushing_defense")},
        home: {"top_strength_domain": "pass_rush", "top_weakness_domain": "pass_protection",
               "top_strength_index": home_vals.get("pass_rush"),
               "top_weakness_index": home_vals.get("pass_protection")},
    })
    changes_path = _write_domain_changes(tmp_path, {away: away_vals, home: home_vals})
    return summary_path, snap_path, changes_path


# --------------------------------------------------------------------------- #
# team selection
# --------------------------------------------------------------------------- #
def test_load_matchup_card_data_unknown_team_raises_clearly(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    with pytest.raises(MatchupDataError, match="ZZZ"):
        load_matchup_card_data(
            "ZZZ", "BBB", SEASON, WEEK,
            weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
            weekly_changes_path=changes_path,
        )


def test_load_matchup_card_data_same_team_raises(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    with pytest.raises(MatchupDataError, match="cannot be the same team"):
        load_matchup_card_data(
            "AAA", "aaa", SEASON, WEEK,
            weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
            weekly_changes_path=changes_path,
        )


def test_load_matchup_card_data_resolves_teams_case_insensitively(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    data = load_matchup_card_data(
        "aaa", "bbb", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    assert data.away.team == "AAA"
    assert data.home.team == "BBB"


# --------------------------------------------------------------------------- #
# domain retrieval
# --------------------------------------------------------------------------- #
def test_all_nine_domains_present_on_both_teams(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    assert set(data.away.domains.keys()) == set(DOMAIN_IDS)
    assert set(data.home.domains.keys()) == set(DOMAIN_IDS)
    assert len(DOMAIN_IDS) == 9


def test_domain_values_match_source_exactly(tmp_path):
    away_vals = {d: (0.1 * i) for i, d in enumerate(DOMAIN_IDS)}
    home_vals = {d: -(0.1 * i) for i, d in enumerate(DOMAIN_IDS)}
    summary_path, snap_path, changes_path = _default_fixture(
        tmp_path, away_vals=away_vals, home_vals=home_vals,
    )
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    for dom_id in DOMAIN_IDS:
        assert data.away.domain(dom_id).index_value == pytest.approx(away_vals[dom_id])
        assert data.home.domain(dom_id).index_value == pytest.approx(home_vals[dom_id])


def test_domain_percentile_derived_from_rank_consistently(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    dv = data.away.domain("passing_offense")
    assert dv.rank == 1  # AAA has the higher value in the default fixture
    assert dv.n_teams == 2
    assert dv.percentile == pytest.approx((2 - 1) / (2 - 1))  # = 1.0, best of 2


def test_unknown_domain_raises(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    with pytest.raises(MatchupDataError, match="unknown domain"):
        data.away.domain("not_a_real_domain")


# --------------------------------------------------------------------------- #
# ordering (Section 2/3: comparisons + key battles)
# --------------------------------------------------------------------------- #
def test_key_battles_ordered_by_descending_absolute_gap(tmp_path):
    away_vals = dict.fromkeys(DOMAIN_IDS, 0.0)
    home_vals = dict.fromkeys(DOMAIN_IDS, 0.0)
    # make the six comparison-relevant domains have distinct, known gaps
    away_vals["passing_offense"], home_vals["passing_defense"] = 2.0, 0.0   # gap 2.0
    away_vals["rushing_offense"], home_vals["rushing_defense"] = 0.5, 0.0   # gap 0.5
    away_vals["pass_protection"], home_vals["pass_rush"] = 0.1, 1.0         # gap -0.9
    home_vals["passing_offense"], away_vals["passing_defense"] = 0.2, 0.0   # gap 0.2
    home_vals["rushing_offense"], away_vals["rushing_defense"] = 0.05, 0.0  # gap 0.05
    home_vals["pass_protection"], away_vals["pass_rush"] = 0.0, 0.0         # gap 0.0

    summary_path, snap_path, changes_path = _default_fixture(
        tmp_path, away_vals=away_vals, home_vals=home_vals,
    )
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    comparisons = compute_matchup_comparisons(data)
    battles = identify_key_battles(comparisons, k_min=3, k_max=5)

    gaps = [abs(b.gap) for b in battles]
    assert gaps == sorted(gaps, reverse=True)
    assert gaps[0] == pytest.approx(2.0)
    assert len(battles) == 5  # 6 measurable comparisons, capped at k_max


def test_compute_matchup_comparisons_is_deterministic(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    c1 = compute_matchup_comparisons(data)
    c2 = compute_matchup_comparisons(data)
    assert [c.gap for c in c1] == [c.gap for c in c2]
    assert [c.label for c in c1] == [c.label for c in c2]


# --------------------------------------------------------------------------- #
# missing-data behavior
# --------------------------------------------------------------------------- #
def test_missing_domain_value_yields_none_gap_and_is_excluded_from_battles(tmp_path):
    away_vals = dict.fromkeys(DOMAIN_IDS, 0.3)
    home_vals = dict.fromkeys(DOMAIN_IDS, -0.1)
    del away_vals["passing_offense"]  # simulate a missing metric/domain for AAA

    summary_path, snap_path, changes_path = _default_fixture(
        tmp_path, away_vals=away_vals, home_vals=home_vals,
    )
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    assert data.away.domain("passing_offense").index_value is None

    comparisons = compute_matchup_comparisons(data)
    away_passing_vs_home_def = next(
        c for c in comparisons if c.label == "Away Passing Offense vs Home Passing Defense"
    )
    assert away_passing_vs_home_def.gap is None

    battles = identify_key_battles(comparisons)
    assert all(b.label != "Away Passing Offense vs Home Passing Defense" for b in battles)


def test_missing_index_value_formats_as_na():
    assert fmt_index(None) == "N/A"
    assert fmt_rank(None, 32) == "N/A"
    assert fmt_rank(5, None) == "N/A"
    assert fmt_percentile(None) == "N/A"


def test_missing_output_file_raises_clear_error(tmp_path):
    missing = tmp_path / "does_not_exist.json"
    with pytest.raises(MatchupDataError, match="not found"):
        load_matchup_card_data(
            "AAA", "BBB", SEASON, WEEK, weekly_summary_path=missing,
        )


def test_team_identity_statements_only_reference_present_domains(tmp_path):
    away_vals = dict.fromkeys(DOMAIN_IDS, 0.0)
    away_vals["passing_offense"] = 1.5
    away_vals["rushing_defense"] = -1.5
    summary_path, snap_path, changes_path = _default_fixture(tmp_path, away_vals=away_vals)
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    stmts = team_identity_statements(data.away)
    assert stmts  # at least strength/weakness statements generated
    assert any("Passing-Offense" in s for s in stmts)


# --------------------------------------------------------------------------- #
# rendering smoke test (figure builds and can be saved; no visual assertions)
# --------------------------------------------------------------------------- #
def test_build_figure_renders_and_saves(tmp_path):
    summary_path, snap_path, changes_path = _default_fixture(tmp_path)
    data = load_matchup_card_data(
        "AAA", "BBB", SEASON, WEEK,
        weekly_summary_path=summary_path, weekly_team_snapshot_path=snap_path,
        weekly_changes_path=changes_path,
    )
    fig = build_figure(data)
    out_png, out_pdf = tmp_path / "card.png", tmp_path / "card.pdf"
    fig.savefig(out_png)
    fig.savefig(out_pdf)
    assert out_png.exists() and out_png.stat().st_size > 1000
    assert out_pdf.exists() and out_pdf.stat().st_size > 1000
    with out_png.open("rb") as f:
        assert f.read(8) == b"\x89PNG\r\n\x1a\n"
