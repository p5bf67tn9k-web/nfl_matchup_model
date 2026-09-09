"""Assign a Phase 3 persistence status from a metric's PRIMARY cells.

Primary cells = weeks 5-18, horizons 2 AND 4 (see the disclosed deviation in
config/phase3_validation.yaml), each at the metric's BEST window for that horizon
(best = highest skill_vs_league point estimate among windows meeting min data).

Taxonomy (spec sections 2, 20):
  VALIDATED_PERSISTENCE      cleared the pre-registered bar at BOTH primary horizons
  NO_INCREMENTAL_PERSISTENCE evaluable with enough data, clearly fails at BOTH
  INSUFFICIENT_DATA          evaluated but n < threshold
  UNVALIDATED                not evaluable, or ambiguous (cleared the bar at exactly
                             one horizon, or CI straddles the economic floor)

VALIDATED_PERSISTENCE means only that -- it does NOT mean the metric improves
matchup prediction (spec section 16).
"""
from __future__ import annotations

import numpy as np


def _cell_verdict(c: dict | None, rules: dict) -> str:
    if c is None:
        return "no_cell"
    if c["n"] < rules["insufficient_data_min_n"]:
        return "insufficient"
    floor = rules["economic_floor"]
    sk_l, sk_l_lo = c["skill_vs_league"], c["skill_vs_league_ci_lo"]
    sk_p, sk_p_lo = c["skill_vs_prior_season"], c["skill_vs_prior_season_ci_lo"]
    sp, sp_lo = c["spearman"], c["spearman_ci_lo"]

    def fin(x):
        return x is not None and np.isfinite(x)

    beats_league = fin(sk_l_lo) and sk_l_lo > 0 and fin(sk_l) and sk_l >= floor["min_skill_vs_league"]
    beats_prior = fin(sk_p_lo) and sk_p_lo > 0 and fin(sk_p) and sk_p > 0
    rank_ok = fin(sp_lo) and sp_lo > 0 and fin(sp) and abs(sp) >= floor["min_abs_spearman"]
    if beats_league and beats_prior and rank_ok:
        return "pass"
    clearly_fails = (
        (fin(sk_l_lo) and sk_l_lo <= 0) or (fin(sk_l) and sk_l < 0)
        or (fin(sk_p) and sk_p <= 0)
    ) and not (beats_league or beats_prior)
    return "fail" if clearly_fails else "ambiguous"


def _fmt(c: dict | None) -> str:
    if c is None:
        return "no cell"
    return (f"win={c.get('window')} n={c['n']} "
            f"skill_vs_league={c['skill_vs_league']:.3f}[{c['skill_vs_league_ci_lo']:.3f},{c['skill_vs_league_ci_hi']:.3f}] "
            f"skill_vs_prior={c['skill_vs_prior_season']:.3f}[{c['skill_vs_prior_season_ci_lo']:.3f}] "
            f"spearman={c['spearman']:.3f}[{c['spearman_ci_lo']:.3f}]")


def assign_status(primary_by_horizon: dict[int, dict | None], rules: dict) -> tuple[str, str]:
    horizons = sorted(primary_by_horizon)
    verdicts = {h: _cell_verdict(primary_by_horizon.get(h), rules) for h in horizons}
    evidence = " | ".join(f"H{h}: {_fmt(primary_by_horizon.get(h))}" for h in horizons)

    if all(v == "no_cell" for v in verdicts.values()):
        return "UNVALIDATED", f"not evaluable ({evidence})"
    if all(v in ("insufficient", "no_cell") for v in verdicts.values()):
        return "INSUFFICIENT_DATA", evidence
    if all(v == "pass" for v in verdicts.values()):
        return "VALIDATED_PERSISTENCE", evidence
    if all(v in ("fail", "insufficient", "no_cell") for v in verdicts.values()) and "fail" in verdicts.values():
        return "NO_INCREMENTAL_PERSISTENCE", evidence
    return "UNVALIDATED", f"ambiguous ({evidence})"


def assign_rank_persistence(
    rank_by_horizon: dict[int, dict | None], rules: dict
) -> tuple[str, str]:
    """Secondary classification -- reported alongside predictive_status, never
    changes it. Uses the best-by-spearman window per horizon."""
    floor = rules["economic_floor"]
    horizons = sorted(rank_by_horizon)

    def ok(c: dict | None) -> str:
        if c is None:
            return "no_cell"
        if c["n"] < rules["insufficient_data_min_n"]:
            return "insufficient"
        sp, lo = c["spearman"], c["spearman_ci_lo"]
        if lo is not None and lo > 0 and abs(sp) >= floor["min_abs_spearman"]:
            return "pass"
        return "fail"

    v = {h: ok(rank_by_horizon.get(h)) for h in horizons}
    ev = " | ".join(
        f"H{h}: spearman={ (rank_by_horizon.get(h) or {}).get('spearman') }"
        f"[{ (rank_by_horizon.get(h) or {}).get('spearman_ci_lo') }] "
        f"n={ (rank_by_horizon.get(h) or {}).get('n') } "
        f"win={ (rank_by_horizon.get(h) or {}).get('window') }"
        for h in horizons
    )
    if all(x in ("no_cell", "insufficient") for x in v.values()):
        return "INSUFFICIENT", ev
    if all(x == "pass" for x in v.values()):
        return "RANK_PERSISTENT", ev
    return "NOT_RANK_PERSISTENT", ev
