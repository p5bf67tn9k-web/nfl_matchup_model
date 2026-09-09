"""Play classification -- the foundation of every pbp-derived metric.

``classify_plays`` takes an as-of play-by-play frame and adds a fixed set of
documented boolean flags plus the numeric fields metrics consume. It performs NO
aggregation and makes NO predictive claim.

Exact play-universe rules (verified against 2024 pbp, all games incl. postseason)
--------------------------------------------------------------------------------
nflfastR ``pass`` and ``rush`` partition all "real" offensive snaps and are
mutually exclusive:
  * ``pass == 1``  -> forward-pass attempts, sacks, AND QB scrambles
  * ``rush == 1``  -> designed runs only (NOT scrambles, NOT kneels)
  * ``pass + rush`` excludes kneels, spikes, kickoffs, punts, FGs, XPs, no-plays
  * every ``pass==1 | rush==1`` row has a non-null ``epa`` (0 nulls in 2024)

Flags produced (``PLAY_FLAG_COLUMNS``)
--------------------------------------
off_play          (pass==1 | rush==1) & two_point_attempt==0
                  -> the offensive-play denominator for team EPA/play etc.
is_dropback       qb_dropback==1 & two_point_attempt==0
                  -> QB dropback denominator (throws + sacks + scrambles)
is_pass_throw     (complete_pass==1 | incomplete_pass==1 | interception==1)
                  & two_point_attempt==0 & qb_spike==0
                  -> actual forward-pass attempts (throwaways counted as incomplete)
is_sack           sack==1 & two_point_attempt==0
is_scramble       qb_scramble==1 & two_point_attempt==0
is_designed_rush  rush==1 & qb_kneel==0 & two_point_attempt==0
is_early_down     down in (1, 2)
is_explosive_pass is_pass_throw & complete_pass==1 & yards_gained >= EXPLOSIVE_PASS_YARDS
is_explosive_rush is_designed_rush & yards_gained >= EXPLOSIVE_RUSH_YARDS
has_cpoe          is_pass_throw & cpoe is not null   (~95% of throws in 2024)

Explicitly EXCLUDED from every offensive rate metric
---------------------------------------------------
  * kneel-downs (qb_kneel==1)         -- clock plays
  * spikes (qb_spike==1)              -- clock plays
  * two-point conversions             -- different scoring model / no comparable EPA
  * plays with null epa               -- pre-snap penalties that wipe the down, etc.

Explosive thresholds are a documented CHOICE, not a standard. Common alternatives:
15 (pass) / 12 (rush) [Sharp], 16+ EPA-positive, air-yards based. Configurable via
``config/metrics.yaml`` -> ``thresholds``.
"""
from __future__ import annotations

import polars as pl

from matchup.config import CONFIG_DIR
from matchup.metrics._thresholds import load_thresholds

_t = load_thresholds()
EXPLOSIVE_PASS_YARDS: int = _t["explosive_pass_yards"]
EXPLOSIVE_RUSH_YARDS: int = _t["explosive_rush_yards"]

PLAY_FLAG_COLUMNS = [
    "off_play",
    "is_dropback",
    "is_pass_throw",
    "is_sack",
    "is_scramble",
    "is_designed_rush",
    "is_early_down",
    "is_explosive_pass",
    "is_explosive_rush",
    "has_cpoe",
]

# numeric / id fields carried through for downstream aggregation
_CARRY = [
    "play_id", "game_id", "season", "week", "posteam", "defteam", "data_asof",
    "down", "ydstogo", "yardline_100",
    "epa", "success", "cpoe", "air_yards", "yards_gained",
    "passing_yards", "rushing_yards", "receiving_yards", "yards_after_catch",
    "pass_touchdown", "rush_touchdown", "interception", "first_down",
    "qb_hit", "sack", "fumble_lost", "complete_pass", "incomplete_pass",
    "xpass", "pass_oe",
    "passer_player_id", "rusher_player_id", "receiver_player_id",
    "two_point_attempt", "qb_spike", "qb_kneel", "qb_dropback", "qb_scramble",
    "pass", "rush", "pass_attempt", "rush_attempt",
]


def _b(expr: pl.Expr) -> pl.Expr:
    """Coerce a possibly-null 0/1 float flag to a strict boolean."""
    return (expr.fill_null(0) == 1)


def classify_plays(pbp: pl.DataFrame) -> pl.DataFrame:
    """Add ``PLAY_FLAG_COLUMNS`` to an as-of pbp frame. Pure; no aggregation."""
    if pbp.is_empty():
        return pbp

    carry = [c for c in _CARRY if c in pbp.columns]
    df = pbp.select(carry)

    two_pt = _b(pl.col("two_point_attempt"))
    off_play = (_b(pl.col("pass")) | _b(pl.col("rush"))) & ~two_pt

    df = df.with_columns(
        off_play.alias("off_play"),
        (_b(pl.col("qb_dropback")) & ~two_pt).alias("is_dropback"),
        (
            (_b(pl.col("complete_pass")) | _b(pl.col("incomplete_pass"))
             | _b(pl.col("interception")))
            & ~two_pt & ~_b(pl.col("qb_spike"))
        ).alias("is_pass_throw"),
        (_b(pl.col("sack")) & ~two_pt).alias("is_sack"),
        (_b(pl.col("qb_scramble")) & ~two_pt).alias("is_scramble"),
        (_b(pl.col("rush")) & ~_b(pl.col("qb_kneel")) & ~two_pt).alias("is_designed_rush"),
        pl.col("down").is_in([1, 2]).alias("is_early_down"),
    )
    df = df.with_columns(
        (
            pl.col("is_pass_throw") & _b(pl.col("complete_pass"))
            & (pl.col("yards_gained") >= EXPLOSIVE_PASS_YARDS)
        ).alias("is_explosive_pass"),
        (
            pl.col("is_designed_rush") & (pl.col("yards_gained") >= EXPLOSIVE_RUSH_YARDS)
        ).alias("is_explosive_rush"),
        (pl.col("is_pass_throw") & pl.col("cpoe").is_not_null()).alias("has_cpoe"),
    )
    return df


def thresholds_doc() -> str:
    return (CONFIG_DIR / "metrics.yaml").read_text()
