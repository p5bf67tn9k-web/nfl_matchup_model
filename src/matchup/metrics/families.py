"""Per-(entity, game) descriptive metric tables from classified play-by-play.

Every function returns one row per (entity, game_id) with:
  * identity + game keys (season, week, team, game_id)
  * RAW ADDITIVE COMPONENTS (counts / sums) -- windowing simply sums these
  * SINGLE-GAME RATES -- for hand verification and reliability diagnostics
  * provenance: data_asof, pit_source

No windowing, no normalization, no cross-game logic, no predictive claim.
"""
from __future__ import annotations

import polars as pl


# ------------------------------------------------------------------ helpers -- #
def _rate(num: pl.Expr, den: pl.Expr) -> pl.Expr:
    return pl.when(den > 0).then(num / den).otherwise(None)


def _provenance(plays: pl.DataFrame) -> list[pl.Expr]:
    return [pl.col("data_asof").max().alias("data_asof"), pl.lit("pbp").alias("pit_source")]


_GAME_KEYS = ["game_id", "season", "week"]


# ============================================================== quarterback == #
def qb_game_metrics(plays: pl.DataFrame) -> pl.DataFrame:
    """One row per (passer, game). Denominators:
      * dropback metrics -> is_dropback  (throws + sacks + scrambles, no 2pt/spike/kneel)
      * throw metrics    -> is_pass_throw (complete | incomplete | interception)
      * CPOE             -> has_cpoe      (throws where nflfastR cpoe is defined)
    """
    if plays.is_empty():
        return plays
    p = plays.filter(pl.col("passer_player_id").is_not_null() & pl.col("is_dropback"))
    if p.is_empty():
        return p
    g = p.group_by(["passer_player_id", *_GAME_KEYS, pl.col("posteam").alias("team")]).agg(
        # raw components
        pl.col("is_dropback").sum().alias("dropbacks"),
        pl.col("is_pass_throw").sum().alias("throws"),
        (pl.col("is_pass_throw") & pl.col("complete_pass").fill_null(0).eq(1)).sum().alias("completions"),
        pl.col("is_sack").sum().alias("sacks"),
        pl.col("is_scramble").sum().alias("scrambles"),
        (pl.col("is_pass_throw") & pl.col("interception").fill_null(0).eq(1)).sum().alias("interceptions"),
        (pl.col("is_pass_throw") & pl.col("pass_touchdown").fill_null(0).eq(1)).sum().alias("pass_tds"),
        pl.col("epa").filter(pl.col("is_dropback")).sum().alias("epa_dropback_sum"),
        pl.col("success").filter(pl.col("is_dropback")).sum().alias("success_dropback_sum"),
        pl.col("passing_yards").filter(pl.col("is_pass_throw")).sum().alias("pass_yards"),
        pl.col("air_yards").filter(pl.col("is_pass_throw")).sum().alias("air_yards_sum"),
        pl.col("cpoe").filter(pl.col("has_cpoe")).sum().alias("cpoe_sum"),
        pl.col("has_cpoe").sum().alias("cpoe_n"),
        pl.col("is_explosive_pass").sum().alias("explosive_pass_n"),
        pl.col("qb_hit").filter(pl.col("is_dropback")).fill_null(0).sum().alias("qb_hits_taken"),
        *_provenance(p),
    )
    return g.with_columns(
        _rate(pl.col("epa_dropback_sum"), pl.col("dropbacks")).alias("epa_per_dropback"),
        _rate(pl.col("success_dropback_sum"), pl.col("dropbacks")).alias("dropback_success_rate"),
        _rate(pl.col("sacks"), pl.col("dropbacks")).alias("sack_rate"),
        _rate(pl.col("pass_yards"), pl.col("throws")).alias("yards_per_attempt"),
        _rate(pl.col("completions"), pl.col("throws")).alias("completion_pct"),
        _rate(pl.col("air_yards_sum"), pl.col("throws")).alias("adot"),
        _rate(pl.col("cpoe_sum"), pl.col("cpoe_n")).alias("cpoe"),
        _rate(pl.col("cpoe_n"), pl.col("throws")).alias("cpoe_coverage_fraction"),
        pl.col("cpoe_n").alias("cpoe_attempt_count"),
        _rate(pl.col("interceptions"), pl.col("throws")).alias("interception_rate"),
        _rate(pl.col("explosive_pass_n"), pl.col("throws")).alias("explosive_pass_rate"),
        pl.col("dropbacks").alias("n_opportunities"),
    ).rename({"passer_player_id": "entity_id"})


# ================================================================= rushing == #
def rb_game_metrics(plays: pl.DataFrame) -> pl.DataFrame:
    """One row per (rusher, game). Denominator = is_designed_rush (excludes QB
    scrambles and kneels). Receiving components come from receiving plays where
    the rusher is the receiver."""
    if plays.is_empty():
        return plays
    r = plays.filter(pl.col("rusher_player_id").is_not_null() & pl.col("is_designed_rush"))
    if r.is_empty():
        return r
    g = r.group_by(["rusher_player_id", *_GAME_KEYS, pl.col("posteam").alias("team")]).agg(
        pl.col("is_designed_rush").sum().alias("carries"),
        pl.col("rushing_yards").sum().alias("rush_yards"),
        pl.col("epa").sum().alias("rush_epa_sum"),
        pl.col("success").sum().alias("rush_success_sum"),
        (pl.col("rush_touchdown").fill_null(0).eq(1)).sum().alias("rush_tds"),
        pl.col("is_explosive_rush").sum().alias("explosive_rush_n"),
        pl.col("first_down").fill_null(0).sum().alias("rush_first_downs"),
        pl.col("fumble_lost").fill_null(0).sum().alias("fumbles_lost"),
        *_provenance(r),
    )
    return g.with_columns(
        _rate(pl.col("rush_epa_sum"), pl.col("carries")).alias("rush_epa_per_att"),
        _rate(pl.col("rush_success_sum"), pl.col("carries")).alias("rush_success_rate"),
        _rate(pl.col("rush_yards"), pl.col("carries")).alias("yards_per_carry"),
        _rate(pl.col("explosive_rush_n"), pl.col("carries")).alias("explosive_rush_rate"),
        _rate(pl.col("fumbles_lost"), pl.col("carries")).alias("fumble_lost_rate"),
        pl.col("carries").alias("n_opportunities"),
    ).rename({"rusher_player_id": "entity_id"})


# =============================================================== receiving == #
def wr_game_metrics(plays: pl.DataFrame) -> pl.DataFrame:
    """One row per (receiver, game). Denominator = is_pass_throw targeting the
    receiver (targets). Per-target EPA is QB/scheme-entangled -- documented as
    DESCRIPTIVE only. Target/air-yards SHARES are added later from player_stats."""
    if plays.is_empty():
        return plays
    t = plays.filter(pl.col("receiver_player_id").is_not_null() & pl.col("is_pass_throw"))
    if t.is_empty():
        return t
    g = t.group_by(["receiver_player_id", *_GAME_KEYS, pl.col("posteam").alias("team")]).agg(
        pl.len().alias("targets"),
        (pl.col("complete_pass").fill_null(0).eq(1)).sum().alias("receptions"),
        pl.col("receiving_yards").fill_null(0).sum().alias("rec_yards"),
        pl.col("air_yards").sum().alias("air_yards_sum"),
        pl.col("yards_after_catch").fill_null(0).sum().alias("yac_sum"),
        pl.col("epa").sum().alias("target_epa_sum"),
        pl.col("success").sum().alias("target_success_sum"),
        (pl.col("pass_touchdown").fill_null(0).eq(1)).sum().alias("rec_tds"),
        pl.col("first_down").fill_null(0).sum().alias("rec_first_downs"),
        pl.col("is_explosive_pass").sum().alias("explosive_rec_n"),
        *_provenance(t),
    )
    return g.with_columns(
        _rate(pl.col("receptions"), pl.col("targets")).alias("catch_rate"),
        _rate(pl.col("rec_yards"), pl.col("targets")).alias("yards_per_target"),
        _rate(pl.col("rec_yards"), pl.col("receptions")).alias("yards_per_reception"),
        _rate(pl.col("air_yards_sum"), pl.col("targets")).alias("adot"),
        _rate(pl.col("target_epa_sum"), pl.col("targets")).alias("epa_per_target"),
        _rate(pl.col("target_success_sum"), pl.col("targets")).alias("target_success_rate"),
        _rate(pl.col("explosive_rec_n"), pl.col("targets")).alias("explosive_rec_rate"),
        pl.col("targets").alias("n_opportunities"),
    ).rename({"receiver_player_id": "entity_id"})


# ========================================================= team offense/def == #
def _team_unit_metrics(plays: pl.DataFrame, side: str) -> pl.DataFrame:
    """side='offense' -> group by posteam; side='defense' -> group by defteam
    (metrics framed as 'allowed'). Same formulas, mirrored perspective."""
    if plays.is_empty():
        return plays
    team_col = "posteam" if side == "offense" else "defteam"
    p = plays.filter(pl.col("off_play") & pl.col(team_col).is_not_null())
    if p.is_empty():
        return p
    db = pl.col("is_dropback")
    dr = pl.col("is_designed_rush")
    ed = pl.col("is_early_down") & pl.col("off_play")
    g = p.group_by([pl.col(team_col).alias("entity_id"), *_GAME_KEYS]).agg(
        pl.col("off_play").sum().alias("plays"),
        pl.col("epa").sum().alias("epa_sum"),
        pl.col("success").sum().alias("success_sum"),
        db.sum().alias("dropbacks"),
        pl.col("epa").filter(db).sum().alias("pass_epa_sum"),
        pl.col("success").filter(db).sum().alias("pass_success_sum"),
        dr.sum().alias("designed_rushes"),
        pl.col("epa").filter(dr).sum().alias("rush_epa_sum"),
        pl.col("success").filter(dr).sum().alias("rush_success_sum"),
        ed.sum().alias("early_down_plays"),
        pl.col("epa").filter(ed).sum().alias("early_down_epa_sum"),
        pl.col("is_explosive_pass").sum().alias("explosive_pass_n"),
        pl.col("is_explosive_rush").sum().alias("explosive_rush_n"),
        pl.col("xpass").mean().alias("xpass_mean"),
        (db.cast(pl.Float64) - pl.col("xpass")).filter(pl.col("xpass").is_not_null()).sum().alias("proe_sum"),
        pl.col("xpass").is_not_null().sum().alias("proe_n"),
        *_provenance(p),
    )
    return g.with_columns(
        _rate(pl.col("epa_sum"), pl.col("plays")).alias("epa_per_play"),
        _rate(pl.col("success_sum"), pl.col("plays")).alias("success_rate"),
        _rate(pl.col("pass_epa_sum"), pl.col("dropbacks")).alias("pass_epa_per_dropback"),
        _rate(pl.col("pass_success_sum"), pl.col("dropbacks")).alias("pass_success_rate"),
        _rate(pl.col("rush_epa_sum"), pl.col("designed_rushes")).alias("rush_epa_per_play"),
        _rate(pl.col("rush_success_sum"), pl.col("designed_rushes")).alias("rush_success_rate"),
        _rate(pl.col("early_down_epa_sum"), pl.col("early_down_plays")).alias("early_down_epa_per_play"),
        _rate(pl.col("explosive_pass_n"), pl.col("dropbacks")).alias("explosive_pass_rate"),
        _rate(pl.col("explosive_rush_n"), pl.col("designed_rushes")).alias("explosive_rush_rate"),
        _rate(pl.col("proe_sum"), pl.col("proe_n")).alias("proe"),
        pl.col("plays").alias("n_opportunities"),
        pl.lit(side).alias("side"),
    )


def team_offense_game_metrics(plays: pl.DataFrame) -> pl.DataFrame:
    return _team_unit_metrics(plays, "offense")


def team_defense_game_metrics(plays: pl.DataFrame) -> pl.DataFrame:
    return _team_unit_metrics(plays, "defense")


# ================================================ pass protection / pass rush = #
def pass_protection_game_metrics(plays: pl.DataFrame) -> pl.DataFrame:
    """Per (posteam, game): sack/QB-hit rate ALLOWED + a documented-approximate
    run-block indicator. NOT a lineman-level rating (decision #7: OL is team-derived)."""
    if plays.is_empty():
        return plays
    p = plays.filter(pl.col("posteam").is_not_null() & (pl.col("is_dropback") | pl.col("is_designed_rush")))
    if p.is_empty():
        return p
    g = p.group_by([pl.col("posteam").alias("entity_id"), *_GAME_KEYS]).agg(
        pl.col("is_dropback").sum().alias("dropbacks"),
        pl.col("is_sack").sum().alias("sacks_allowed"),
        pl.col("qb_hit").filter(pl.col("is_dropback")).fill_null(0).sum().alias("qb_hits_allowed"),
        pl.col("is_designed_rush").sum().alias("designed_rushes"),
        # APPROX run-block: share of designed runs stuffed at/behind LOS (yards_gained <= 0)
        (pl.col("is_designed_rush") & (pl.col("yards_gained") <= 0)).sum().alias("rush_stuffed_n"),
        *_provenance(p),
    )
    return g.with_columns(
        _rate(pl.col("sacks_allowed"), pl.col("dropbacks")).alias("sack_rate_allowed"),
        _rate(pl.col("qb_hits_allowed"), pl.col("dropbacks")).alias("qb_hit_rate_allowed"),
        _rate(pl.col("rush_stuffed_n"), pl.col("designed_rushes")).alias("rush_stuffed_rate_approx"),
        pl.col("dropbacks").alias("n_opportunities"),
    )


def pass_rush_game_metrics(plays: pl.DataFrame) -> pl.DataFrame:
    """Per (defteam, game): sacks / QB hits / TFL generated (pbp). PFR pressure
    join-through is added separately (2018+)."""
    if plays.is_empty():
        return plays
    p = plays.filter(pl.col("defteam").is_not_null() & pl.col("is_dropback"))
    if p.is_empty():
        return p
    g = p.group_by([pl.col("defteam").alias("entity_id"), *_GAME_KEYS]).agg(
        pl.col("is_dropback").sum().alias("opp_dropbacks"),
        pl.col("is_sack").sum().alias("sacks"),
        pl.col("qb_hit").fill_null(0).sum().alias("qb_hits"),
        *_provenance(p),
    )
    return g.with_columns(
        _rate(pl.col("sacks"), pl.col("opp_dropbacks")).alias("sack_rate_generated"),
        _rate(pl.col("qb_hits"), pl.col("opp_dropbacks")).alias("qb_hit_rate_generated"),
        pl.col("opp_dropbacks").alias("n_opportunities"),
    )


# ================================================================ special === #
def special_teams_game_metrics(plays_raw: pl.DataFrame) -> pl.DataFrame:
    """Per (posteam, game): FG% and special-teams EPA/play. Takes the RAW as-of
    pbp frame (not classified), since ST plays are outside the pass/rush universe.
    ST universe = nflfastR ``special == 1`` (kickoff, punt, field_goal, extra_point;
    0 null EPA in 2024). Requires: special, field_goal_attempt, field_goal_result,
    posteam, epa, game keys, data_asof."""
    need = {"special", "posteam", "epa", "game_id", "season", "week"}
    if plays_raw.is_empty() or not need.issubset(plays_raw.columns):
        return pl.DataFrame()
    st = plays_raw.filter(
        (pl.col("special").fill_null(0) == 1) & pl.col("posteam").is_not_null()
    )
    if st.is_empty():
        return pl.DataFrame()
    g = st.group_by([pl.col("posteam").alias("entity_id"), "game_id", "season", "week"]).agg(
        pl.len().alias("st_plays"),
        pl.col("epa").sum().alias("st_epa_sum"),
        (pl.col("field_goal_attempt").fill_null(0) == 1).sum().alias("fg_attempts"),
        ((pl.col("field_goal_attempt").fill_null(0) == 1) & (pl.col("field_goal_result") == "made"))
        .sum().alias("fg_made"),
        pl.col("data_asof").max().alias("data_asof"),
        pl.lit("pbp").alias("pit_source"),
    )
    return g.with_columns(
        _rate(pl.col("st_epa_sum"), pl.col("st_plays")).alias("st_epa_per_play"),
        _rate(pl.col("fg_made"), pl.col("fg_attempts")).alias("fg_pct"),
        pl.col("st_plays").alias("n_opportunities"),
    )


# ==================================================================== specs == #
# For each family: the entity grain, the additive component columns (summed across
# a window), and the rate specs (rate_name -> (numerator_component, denominator_component))
# recomputed from the summed components. `opportunity` names the denominator that
# defines n_opportunities for a window.
FAMILY_SPECS: dict[str, dict] = {
    "qb": {
        "fn": qb_game_metrics,
        "grain": "player",
        "components": [
            "dropbacks", "throws", "completions", "sacks", "scrambles", "interceptions",
            "pass_tds", "epa_dropback_sum", "success_dropback_sum", "pass_yards",
            "air_yards_sum", "cpoe_sum", "cpoe_n", "explosive_pass_n", "qb_hits_taken",
        ],
        "opportunity": "dropbacks",
        "rates": {
            "epa_per_dropback": ("epa_dropback_sum", "dropbacks"),
            "dropback_success_rate": ("success_dropback_sum", "dropbacks"),
            "sack_rate": ("sacks", "dropbacks"),
            "yards_per_attempt": ("pass_yards", "throws"),
            "completion_pct": ("completions", "throws"),
            "adot": ("air_yards_sum", "throws"),
            "cpoe": ("cpoe_sum", "cpoe_n"),
            "cpoe_coverage_fraction": ("cpoe_n", "throws"),
            "interception_rate": ("interceptions", "throws"),
            "explosive_pass_rate": ("explosive_pass_n", "throws"),
        },
        "extra": {"cpoe_attempt_count": "cpoe_n"},
    },
    "rb": {
        "fn": rb_game_metrics,
        "grain": "player",
        "components": [
            "carries", "rush_yards", "rush_epa_sum", "rush_success_sum", "rush_tds",
            "explosive_rush_n", "rush_first_downs", "fumbles_lost",
        ],
        "opportunity": "carries",
        "rates": {
            "rush_epa_per_att": ("rush_epa_sum", "carries"),
            "rush_success_rate": ("rush_success_sum", "carries"),
            "yards_per_carry": ("rush_yards", "carries"),
            "explosive_rush_rate": ("explosive_rush_n", "carries"),
            "fumble_lost_rate": ("fumbles_lost", "carries"),
        },
    },
    "wr": {
        "fn": wr_game_metrics,
        "grain": "player",
        "components": [
            "targets", "receptions", "rec_yards", "air_yards_sum", "yac_sum",
            "target_epa_sum", "target_success_sum", "rec_tds", "rec_first_downs",
            "explosive_rec_n",
        ],
        "opportunity": "targets",
        "rates": {
            "catch_rate": ("receptions", "targets"),
            "yards_per_target": ("rec_yards", "targets"),
            "yards_per_reception": ("rec_yards", "receptions"),
            "adot": ("air_yards_sum", "targets"),
            "epa_per_target": ("target_epa_sum", "targets"),
            "target_success_rate": ("target_success_sum", "targets"),
            "explosive_rec_rate": ("explosive_rec_n", "targets"),
        },
    },
    "team_offense": {
        "fn": team_offense_game_metrics,
        "grain": "team",
        "components": [
            "plays", "epa_sum", "success_sum", "dropbacks", "pass_epa_sum",
            "pass_success_sum", "designed_rushes", "rush_epa_sum", "rush_success_sum",
            "early_down_plays", "early_down_epa_sum", "explosive_pass_n",
            "explosive_rush_n", "proe_sum", "proe_n",
        ],
        "opportunity": "plays",
        "rates": {
            "epa_per_play": ("epa_sum", "plays"),
            "success_rate": ("success_sum", "plays"),
            "pass_epa_per_dropback": ("pass_epa_sum", "dropbacks"),
            "pass_success_rate": ("pass_success_sum", "dropbacks"),
            "rush_epa_per_play": ("rush_epa_sum", "designed_rushes"),
            "rush_success_rate": ("rush_success_sum", "designed_rushes"),
            "early_down_epa_per_play": ("early_down_epa_sum", "early_down_plays"),
            "explosive_pass_rate": ("explosive_pass_n", "dropbacks"),
            "explosive_rush_rate": ("explosive_rush_n", "designed_rushes"),
            "proe": ("proe_sum", "proe_n"),
        },
    },
    "team_defense": {
        "fn": team_defense_game_metrics,
        "grain": "team",
        "components": [
            "plays", "epa_sum", "success_sum", "dropbacks", "pass_epa_sum",
            "pass_success_sum", "designed_rushes", "rush_epa_sum", "rush_success_sum",
            "early_down_plays", "early_down_epa_sum", "explosive_pass_n",
            "explosive_rush_n", "proe_sum", "proe_n",
        ],
        "opportunity": "plays",
        "rates": {
            "epa_per_play": ("epa_sum", "plays"),
            "success_rate": ("success_sum", "plays"),
            "pass_epa_per_dropback": ("pass_epa_sum", "dropbacks"),
            "pass_success_rate": ("pass_success_sum", "dropbacks"),
            "rush_epa_per_play": ("rush_epa_sum", "designed_rushes"),
            "rush_success_rate": ("rush_success_sum", "designed_rushes"),
            "early_down_epa_per_play": ("early_down_epa_sum", "early_down_plays"),
            "explosive_pass_rate": ("explosive_pass_n", "dropbacks"),
            "explosive_rush_rate": ("explosive_rush_n", "designed_rushes"),
        },
    },
    "pass_protection": {
        "fn": pass_protection_game_metrics,
        "grain": "team",
        "components": [
            "dropbacks", "sacks_allowed", "qb_hits_allowed", "designed_rushes",
            "rush_stuffed_n",
        ],
        "opportunity": "dropbacks",
        "rates": {
            "sack_rate_allowed": ("sacks_allowed", "dropbacks"),
            "qb_hit_rate_allowed": ("qb_hits_allowed", "dropbacks"),
            "rush_stuffed_rate_approx": ("rush_stuffed_n", "designed_rushes"),
        },
    },
    "pass_rush": {
        "fn": pass_rush_game_metrics,
        "grain": "team",
        "components": ["opp_dropbacks", "sacks", "qb_hits"],
        "opportunity": "opp_dropbacks",
        "rates": {
            "sack_rate_generated": ("sacks", "opp_dropbacks"),
            "qb_hit_rate_generated": ("qb_hits", "opp_dropbacks"),
        },
    },
    "special_teams": {
        "fn": special_teams_game_metrics,   # NOTE: consumes RAW pbp, not classified
        "grain": "team",
        "raw_pbp": True,
        "components": ["st_plays", "st_epa_sum", "fg_attempts", "fg_made"],
        "opportunity": "st_plays",
        "rates": {
            "st_epa_per_play": ("st_epa_sum", "st_plays"),
            "fg_pct": ("fg_made", "fg_attempts"),
        },
    },
}
