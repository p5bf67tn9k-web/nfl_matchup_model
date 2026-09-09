"""Load metric thresholds from config/metrics.yaml (with documented defaults)."""
from __future__ import annotations

import functools

import yaml

from matchup.config import CONFIG_DIR

_DEFAULTS = {
    "explosive_pass_yards": 20,
    "explosive_rush_yards": 10,
    "min_dropbacks_game": 10,
    "min_carries_game": 5,
    "min_targets_game": 2,
    "min_dropbacks_season_ref": 200,   # QB league-reference eligibility
    "min_carries_season_ref": 50,
    "min_targets_season_ref": 30,
    "min_team_plays_season_ref": 200,
}


@functools.lru_cache(maxsize=1)
def load_thresholds() -> dict:
    raw = yaml.safe_load((CONFIG_DIR / "metrics.yaml").read_text()) or {}
    out = dict(_DEFAULTS)
    out.update(raw.get("thresholds", {}) or {})
    return out
