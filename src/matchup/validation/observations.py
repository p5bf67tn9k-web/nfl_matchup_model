"""Build the per-(entity, target game) persistence observation table for a family.

One output row per (family, entity_id, target_game_id, metric, window, horizon):
  feature_value        the window's raw metric, strictly as-of the target kickoff
                       (games with data_asof < target_kickoff, i.e. production
                       publish-lag respected)
  target_value         the entity's ACTUAL metric over the next `horizon` ELIGIBLE
                       games starting at the target game (raw components summed,
                       rate recomputed). Missing opportunity != zero: if fewer than
                       `horizon` eligible games remain in the season -> row excluded
                       for that horizon (reason logged).
  baseline_league      mean of the metric over the 3 completed reference seasons
  baseline_prior       the entity's most recent completed-season value (or null)
  baseline_raw_t3      the raw trailing-3 feature value
  feat_n_games / feat_opp_n / target_opp_n / season / week / season_phase
"""
from __future__ import annotations

from datetime import timedelta

import numpy as np
import polars as pl

from matchup.config import load_publish_lag
from matchup.metrics.build import game_metrics_batch
from matchup.metrics.families import FAMILY_SPECS
from matchup.metrics.windows import _FAMILY_SOURCE, entity_season_aggregate
from matchup.normalize.reference import completed_seasons_asof, min_opportunities_for
from matchup.validation.config import load_phase3_config, season_phase


def _lag_delta(family: str) -> timedelta:
    pit = load_publish_lag()
    src = pit.get(_FAMILY_SOURCE[family])
    return timedelta(hours=pit.assumed_game_duration_hours, days=src.publish_lag_days or 0)


def _reference_means(family: str, cfg: dict) -> dict[int, dict[str, float]]:
    """{eval_season -> {metric -> league mean over its 3 completed ref seasons}}."""
    spec = FAMILY_SPECS[family]
    hist = list(range(cfg["seasons"]["history_available_from"], cfg["seasons"]["eval_end"] + 1))
    gm_all = game_metrics_batch(family, tuple(hist))
    season_lvl = entity_season_aggregate(family, gm_all)
    mo = min_opportunities_for(family)
    out: dict[int, dict[str, float]] = {}
    from matchup.pointintime.calendar import build_game_calendar

    cal = build_game_calendar()
    for s in range(cfg["seasons"]["eval_start"], cfg["seasons"]["eval_end"] + 1):
        # reference seasons = 3 completed as of that season's week 1
        wk1 = cal.filter(pl.col("season") == s).get_column("kickoff_utc").min()
        ref_seasons = completed_seasons_asof(wk1, calendar=cal)
        sub = season_lvl.filter(
            pl.col("season").is_in(ref_seasons) & (pl.col("n_opportunities") >= mo)
        )
        out[s] = {"_ref_seasons": ref_seasons}
        for m in spec["rates"]:
            col = sub.get_column(m).drop_nulls() if m in sub.columns else pl.Series([], dtype=pl.Float64)
            out[s][m] = float(col.mean()) if len(col) else float("nan")
            out[s][f"{m}__sd"] = float(col.std(ddof=1)) if len(col) >= 2 else float("nan")
    return out


def _prior_season_values(family: str, cfg: dict) -> pl.DataFrame:
    """(entity_id, for_season, metric...) -> the entity's value in for_season-1
    if it met the min-opportunity bar that season."""
    spec = FAMILY_SPECS[family]
    hist = list(range(cfg["seasons"]["history_available_from"], cfg["seasons"]["eval_end"] + 1))
    gm_all = game_metrics_batch(family, tuple(hist))
    season_lvl = entity_season_aggregate(family, gm_all)
    mo = min_opportunities_for(family)
    season_lvl = season_lvl.filter(pl.col("n_opportunities") >= mo)
    return season_lvl.select(
        "entity_id",
        (pl.col("season") + 1).alias("for_season"),
        *[pl.col(m).alias(f"prior_{m}") for m in spec["rates"] if m in season_lvl.columns],
    )


def build_observations(family: str, cfg: dict | None = None) -> pl.DataFrame:
    cfg = cfg or load_phase3_config()
    if family not in FAMILY_SPECS:
        raise KeyError(family)
    spec = FAMILY_SPECS[family]
    comp_cols = [c for c in spec["components"] if c]
    rate_specs = spec["rates"]
    opp_col = spec["opportunity"]

    hist = list(range(cfg["seasons"]["history_available_from"], cfg["seasons"]["eval_end"] + 1))
    gm = game_metrics_batch(family, tuple(hist))
    if gm.is_empty():
        return pl.DataFrame()

    per_game_min = cfg["target"]["per_game_min_opportunities"][family]
    min_feat_games = cfg["feature"]["min_feature_games"]
    min_feat_opp = cfg["feature"]["min_feature_opportunities"][family]
    horizons = cfg["horizons"]
    eval_lo, eval_hi = cfg["seasons"]["eval_start"], cfg["seasons"]["eval_end"]
    lag = _lag_delta(family)

    gm = gm.sort(["entity_id", "kickoff_utc"]).with_columns(
        (pl.col(opp_col) >= per_game_min).alias("eligible")
    )

    ref_means = _reference_means(family, cfg)
    prior = _prior_season_values(family, cfg)

    rows: list[dict] = []
    exclusions: list[dict] = []
    for entity_id, sub in gm.group_by("entity_id", maintain_order=True):
        entity_id = entity_id[0] if isinstance(entity_id, tuple) else entity_id
        kick = sub.get_column("kickoff_utc").to_numpy()
        season = sub.get_column("season").to_numpy()
        week = sub.get_column("week").to_numpy()
        gid = sub.get_column("game_id").to_list()
        team = sub.get_column("team").to_list() if "team" in sub.columns else [None] * len(gid)
        elig = sub.get_column("eligible").to_numpy()
        comps = {c: sub.get_column(c).to_numpy().astype(float) for c in comp_cols}
        asof = sub.get_column("data_asof").to_numpy()
        n = len(kick)

        prior_e = prior.filter(pl.col("entity_id") == entity_id)

        for t in range(n):
            s_t, w_t = int(season[t]), int(week[t])
            if not (eval_lo <= s_t <= eval_hi):
                continue
            if not (1 <= w_t <= 18):
                continue
            target_kick = kick[t]
            avail_cut = np.datetime64(target_kick) - np.timedelta64(int(lag.total_seconds()), "s")
            a = int(np.searchsorted(kick, avail_cut, side="left"))  # games available as-of
            if a == 0:
                continue

            avail_idx = np.arange(a)
            std_idx = avail_idx[season[avail_idx] == s_t]
            prior_idx = avail_idx[season[avail_idx] == s_t - 1]
            windows = {
                "season_to_date": std_idx,
                "trailing_3": avail_idx[-3:] if a >= 3 else np.array([], int),
                "trailing_5": avail_idx[-5:] if a >= 5 else np.array([], int),
                "prior_season": prior_idx,
            }

            # ---- targets: eligible games from t onward, same season -----------
            fwd = np.arange(t, n)
            fwd = fwd[(season[fwd] == s_t) & elig[fwd]]
            target_vals: dict[int, dict] = {}
            for h in horizons:
                excluded = len(fwd) < h
                exclusions.append({
                    "family": family, "entity_id": entity_id, "target_game_id": gid[t],
                    "season": s_t, "week": w_t, "season_phase": season_phase(w_t, cfg),
                    "horizon": h, "excluded": excluded,
                    "n_eligible_remaining": len(fwd),
                })
                if excluded:
                    target_vals[h] = {"_excluded": f"only {len(fwd)} eligible games remain"}
                    continue
                gi = fwd[:h]
                csum = {c: comps[c][gi].sum() for c in comp_cols}
                tv = {}
                for m, (num, den) in rate_specs.items():
                    tv[m] = csum[num] / csum[den] if csum.get(den, 0) > 0 else None
                tv["_opp_n"] = float(csum.get(opp_col, np.nan))
                tv["_n_games"] = h
                target_vals[h] = tv

            # ---- baseline C: raw trailing-3 --------------------------------
            t3 = windows["trailing_3"]
            bl_raw_t3 = {}
            if len(t3) == 3:
                cs = {c: comps[c][t3].sum() for c in comp_cols}
                for m, (num, den) in rate_specs.items():
                    bl_raw_t3[m] = cs[num] / cs[den] if cs.get(den, 0) > 0 else None

            # ---- baseline B: prior season -------------------------------
            pr = prior_e.filter(pl.col("for_season") == s_t)
            prior_row = pr.to_dicts()[0] if pr.height else {}

            rm = ref_means.get(s_t, {})

            for wname, widx in windows.items():
                if len(widx) < min_feat_games[wname]:
                    continue
                cs = {c: comps[c][widx].sum() for c in comp_cols}
                feat_opp = float(cs.get(opp_col, np.nan))
                if feat_opp < min_feat_opp:
                    continue
                feat = {}
                for m, (num, den) in rate_specs.items():
                    feat[m] = cs[num] / cs[den] if cs.get(den, 0) > 0 else None
                for m in rate_specs:
                    if feat[m] is None:
                        continue
                    for h in horizons:
                        tvh = target_vals[h]
                        if "_excluded" in tvh or tvh.get(m) is None:
                            continue
                        rows.append({
                            "family": family, "entity_id": entity_id, "team": team[t],
                            "target_game_id": gid[t], "season": s_t, "week": w_t,
                            "season_phase": season_phase(w_t, cfg),
                            "metric": m, "window": wname, "horizon": h,
                            "feature_value": float(feat[m]),
                            "target_value": float(tvh[m]),
                            "baseline_league": float(rm.get(m, np.nan)),
                            "baseline_league_sd": float(rm.get(f"{m}__sd", np.nan)),
                            "baseline_prior": (float(prior_row[f"prior_{m}"])
                                               if prior_row.get(f"prior_{m}") is not None else None),
                            "baseline_raw_t3": (float(bl_raw_t3[m])
                                                if bl_raw_t3.get(m) is not None else None),
                            "feat_n_games": len(widx),
                            "feat_opp_n": feat_opp,
                            "target_opp_n": tvh["_opp_n"],
                            "feat_data_asof": str(asof[widx].max()),
                            "target_kickoff": str(target_kick),
                        })
    obs = pl.DataFrame(rows, infer_schema_length=None) if rows else pl.DataFrame()
    exc = pl.DataFrame(exclusions, infer_schema_length=None) if exclusions else pl.DataFrame()
    return obs, exc
