"""Loader for config/phase4_validation.yaml + candidate-universe resolution."""
from __future__ import annotations

import functools

import polars as pl
import yaml

from matchup.config import CONFIG_DIR, REPO_ROOT


@functools.lru_cache(maxsize=1)
def load_phase4_config() -> dict:
    cfg = yaml.safe_load((CONFIG_DIR / "phase4_validation.yaml").read_text())
    assert cfg.get("frozen") is True, "phase4_validation.yaml must be frozen before running"
    return cfg


def resolve_candidates(cfg: dict | None = None) -> pl.DataFrame:
    """Materialise the frozen selection rule against outputs/phase3/metric_status.csv.
    One row per candidate: metric, family, reason."""
    cfg = cfg or load_phase4_config()
    sel = cfg["candidate_selection"]
    st = pl.read_csv(REPO_ROOT / "outputs" / "phase3" / "metric_status.csv")

    rp = st.filter(
        (pl.col("rank_persistence") == "RANK_PERSISTENT")
        & (pl.col("primary_n_h4") >= sel["min_primary_n"])
    )
    rows = [
        {
            "metric": r["metric"], "family": r["family"],
            "reason": f"Phase 3 RANK_PERSISTENT ({r['predictive_status']}), "
                      f"spearman_h4={r['spearman_h4']:.3f}, primary_n_h4={r['primary_n_h4']}",
        }
        for r in rp.iter_rows(named=True)
    ]
    for m in sel["named_additions"]:
        fam = m.split(".")[0]
        rows.append({"metric": m, "family": fam,
                     "reason": "named in the Phase 4 spec (NGS style-trait with demonstrated "
                               "season-to-season persistence in the Phase 3 external ablation)"})
    return pl.DataFrame(rows).unique(subset=["metric"]).sort(["family", "metric"])
