"""Loader for the pre-registered config/phase3_validation.yaml."""
from __future__ import annotations

import functools

import yaml

from matchup.config import CONFIG_DIR


@functools.lru_cache(maxsize=1)
def load_phase3_config() -> dict:
    cfg = yaml.safe_load((CONFIG_DIR / "phase3_validation.yaml").read_text())
    assert cfg.get("frozen") is True, "phase3_validation.yaml must be frozen before running"
    return cfg


def season_phase(week: int, cfg: dict | None = None) -> str:
    cfg = cfg or load_phase3_config()
    for name, (lo, hi) in cfg["season_phase_buckets"].items():
        if lo <= week <= hi:
            return name
    return "other"
