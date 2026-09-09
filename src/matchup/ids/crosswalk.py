"""gsis_id <-> pfr_id crosswalk and coverage measurement (decision DD).

Phase 1 accepts the ~9% pfr_id gap. Requirement: never silently drop unmatched
rows; report unmatched snap share by season and unit; the 3% per-unit-season
threshold triggers building a name+team+season fallback matcher (NOT built unless
exceeded).
"""
from __future__ import annotations

import polars as pl

from matchup.store import load_source

_POS_GROUP = {
    "QB": "QB",
    "RB": "RB", "FB": "RB", "HB": "RB",
    "WR": "WR",
    "TE": "TE",
    "T": "OL", "G": "OL", "C": "OL", "OL": "OL", "OT": "OL", "OG": "OL", "LS": "OL",
    "DE": "DL", "DT": "DL", "NT": "DL", "DL": "DL",
    "EDGE": "EDGE", "OLB": "EDGE",
    "LB": "LB", "ILB": "LB", "MLB": "LB",
    "CB": "DB", "S": "DB", "SS": "DB", "FS": "DB", "DB": "DB", "NB": "DB",
    "K": "ST", "P": "ST",
}


def position_group(pos: str | None) -> str:
    if not pos:
        return "UNK"
    return _POS_GROUP.get(pos.strip().upper(), "OTHER")


def build_crosswalk() -> pl.DataFrame:
    """One row per player with the ID mappings we rely on."""
    players = load_source("players")
    cols = [c for c in ["gsis_id", "pfr_id", "esb_id", "espn_id", "display_name",
                        "position", "status"] if c in players.columns]
    xw = players.select(cols).filter(pl.col("gsis_id").is_not_null())
    return xw


def resolve_gsis_from_pfr(pfr_ids: pl.Series | list[str]) -> pl.DataFrame:
    """Map pfr_id -> gsis_id. Unmatched inputs come back with a null gsis_id
    (never dropped)."""
    xw = build_crosswalk().select("pfr_id", "gsis_id").filter(pl.col("pfr_id").is_not_null())
    left = pl.DataFrame({"pfr_id": list(pfr_ids)})
    return left.join(xw.unique(subset=["pfr_id"]), on="pfr_id", how="left")


def crosswalk_coverage_report() -> pl.DataFrame:
    """Unmatched share by (source, season, unit).

    For snap_counts the weight is snaps; for pfr_* sources the weight is row count.
    'unit' is the position group. Emitted to outputs/phase1/id_crosswalk_coverage.csv.
    """
    xw = build_crosswalk().select("pfr_id", "gsis_id").filter(
        pl.col("pfr_id").is_not_null()
    ).unique(subset=["pfr_id"])
    matched = set(xw.get_column("pfr_id").to_list())

    rows: list[dict] = []

    snaps = load_source("snap_counts")
    if not snaps.is_empty():
        s = snaps.with_columns(
            (pl.col("offense_snaps").fill_null(0)
             + pl.col("defense_snaps").fill_null(0)
             + pl.col("st_snaps").fill_null(0)).alias("snaps"),
            pl.col("pfr_player_id").is_in(list(matched)).alias("matched"),
            pl.col("position").map_elements(position_group, return_dtype=pl.Utf8).alias("unit"),
        )
        agg = s.group_by(["season", "unit"]).agg(
            pl.col("snaps").sum().alias("total_weight"),
            pl.col("snaps").filter(~pl.col("matched")).sum().alias("unmatched_weight"),
            pl.len().alias("rows"),
            pl.col("matched").not_().sum().alias("unmatched_rows"),
        )
        for r in agg.iter_rows(named=True):
            tw = r["total_weight"] or 0
            rows.append({
                "source": "snap_counts", "season": r["season"], "unit": r["unit"],
                "weight_kind": "snaps",
                "total_weight": tw, "unmatched_weight": r["unmatched_weight"] or 0,
                "unmatched_share": round((r["unmatched_weight"] or 0) / tw, 5) if tw else None,
                "rows": r["rows"], "unmatched_rows": r["unmatched_rows"],
            })

    for src in ["pfr_pass", "pfr_rush", "pfr_rec", "pfr_def"]:
        d = load_source(src)
        if d.is_empty():
            continue
        d = d.with_columns(
            pl.col("pfr_player_id").is_in(list(matched)).alias("matched"),
        )
        agg = d.group_by("season").agg(
            pl.len().alias("rows"),
            pl.col("matched").not_().sum().alias("unmatched_rows"),
        )
        for r in agg.iter_rows(named=True):
            rows.append({
                "source": src, "season": r["season"], "unit": "ALL",
                "weight_kind": "rows",
                "total_weight": r["rows"], "unmatched_weight": r["unmatched_rows"],
                "unmatched_share": round(r["unmatched_rows"] / r["rows"], 5) if r["rows"] else None,
                "rows": r["rows"], "unmatched_rows": r["unmatched_rows"],
            })

    return pl.DataFrame(rows).sort(["source", "season", "unit"])
