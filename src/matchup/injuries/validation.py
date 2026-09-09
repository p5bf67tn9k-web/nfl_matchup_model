"""Retroactive validation of the injury as-of fallback rule on 2022-2024.

We have real ``date_modified`` timestamps for these seasons, so we can measure what
the conservative fallback would have gotten wrong if it had been used instead.

Definitions (all restricted to rows with a non-null ``date_modified`` and a
resolvable game kickoff):

  false_inclusion   -- ``date_modified >= kickoff_utc``. The fallback treats the whole
                       weekly report as knowable pre-kickoff, but this row's
                       information did not exist until kickoff or later. THIS IS THE
                       ACCEPTANCE GATE: rate must be < 0.5%.

  cutoff_staleness  -- ``fallback_cutoff <= date_modified < kickoff_utc``. A genuine
                       pre-game update that the frozen fallback cutoff would MISS
                       (the model would use a stale earlier value). Not leakage, but
                       the real cost of the conservative rule. Reported, not gated.

  false_exclusion   -- ``date_modified < kickoff_utc`` (genuinely available) yet the
                       fallback cutoff lands at/after kickoff so the rule would drop
                       the whole report. Should be ~0 (there is a kickoff-1h floor).
"""
from __future__ import annotations

import json
from datetime import UTC, datetime

import polars as pl

from matchup.config import REPO_ROOT
from matchup.injuries.asof_rule import injury_asof_cutoff_expr
from matchup.pointintime.calendar import build_team_game_sequence
from matchup.store import load_source

VALIDATION_SEASONS = [2022, 2023, 2024]
FALSE_INCLUSION_THRESHOLD = 0.005

OUT_DIR = REPO_ROOT / "outputs" / "phase1"


def _prepare(seasons: list[int]) -> pl.DataFrame:
    inj = load_source("injuries", seasons=seasons)
    if "date_modified" not in inj.columns:
        raise RuntimeError("injuries partitions lack date_modified; cannot validate")
    seq = build_team_game_sequence(seasons=seasons).select(
        "season", "week", "team", "kickoff_utc", "game_id"
    )
    j = inj.join(seq, on=["season", "week", "team"], how="left")
    j = j.with_columns(
        pl.col("date_modified").dt.convert_time_zone("UTC").alias("dm_utc"),
    ).with_columns(
        injury_asof_cutoff_expr("kickoff_utc"),
    )
    return j.filter(pl.col("dm_utc").is_not_null() & pl.col("kickoff_utc").is_not_null())


def run_validation(seasons: list[int] | None = None, *, write: bool = True) -> dict:
    seasons = seasons or VALIDATION_SEASONS
    j = _prepare(seasons)

    j = j.with_columns(
        (pl.col("dm_utc") >= pl.col("kickoff_utc")).alias("false_inclusion"),
        (
            (pl.col("dm_utc") >= pl.col("injury_asof_cutoff"))
            & (pl.col("dm_utc") < pl.col("kickoff_utc"))
        ).alias("cutoff_staleness"),
        (pl.col("injury_asof_cutoff") >= pl.col("kickoff_utc")).alias("false_exclusion"),
    )

    per_season = (
        j.group_by("season")
        .agg(
            pl.len().alias("rows"),
            pl.col("false_inclusion").sum().alias("false_inclusion_n"),
            pl.col("cutoff_staleness").sum().alias("cutoff_staleness_n"),
            pl.col("false_exclusion").sum().alias("false_exclusion_n"),
            pl.col("game_id").filter(pl.col("false_inclusion")).n_unique().alias("fi_games"),
        )
        .with_columns(
            (pl.col("false_inclusion_n") / pl.col("rows")).alias("false_inclusion_rate"),
            (pl.col("cutoff_staleness_n") / pl.col("rows")).alias("cutoff_staleness_rate"),
        )
        .sort("season")
    )

    total_rows = j.height
    fi = int(j.get_column("false_inclusion").sum())
    cs = int(j.get_column("cutoff_staleness").sum())
    fe = int(j.get_column("false_exclusion").sum())
    fi_rate = fi / total_rows if total_rows else 0.0

    examples = (
        j.filter(pl.col("false_inclusion"))
        .select("season", "week", "team", "game_id", "gsis_id", "report_status",
                "practice_status", "dm_utc", "kickoff_utc")
        .sort("dm_utc")
        .head(10)
        .to_dicts()
    )
    stale_examples = (
        j.filter(pl.col("cutoff_staleness"))
        .select("season", "week", "team", "game_id", "gsis_id", "report_status",
                "dm_utc", "injury_asof_cutoff", "kickoff_utc")
        .sort(pl.col("kickoff_utc") - pl.col("dm_utc"))
        .head(10)
        .to_dicts()
    )

    summary = {
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "seasons": seasons,
        "rows_evaluated": total_rows,
        "false_inclusion_n": fi,
        "false_inclusion_rate": fi_rate,
        "false_inclusion_threshold": FALSE_INCLUSION_THRESHOLD,
        "passes_acceptance": fi_rate < FALSE_INCLUSION_THRESHOLD,
        "cutoff_staleness_n": cs,
        "cutoff_staleness_rate": cs / total_rows if total_rows else 0.0,
        "false_exclusion_n": fe,
        "affected_games_false_inclusion": int(
            j.filter(pl.col("false_inclusion")).get_column("game_id").n_unique()
        ),
        "per_season": per_season.to_dicts(),
        "false_inclusion_examples": examples,
        "cutoff_staleness_examples": stale_examples,
    }

    if write:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        per_season.write_csv(OUT_DIR / "injury_asof_validation.csv")
        (OUT_DIR / "injury_asof_validation.json").write_text(
            json.dumps(summary, indent=2, default=str)
        )
    return summary
