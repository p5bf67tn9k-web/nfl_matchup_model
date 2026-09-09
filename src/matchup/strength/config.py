"""Loader for config/strength.yaml."""
from __future__ import annotations

import functools

import yaml

from matchup.config import CONFIG_DIR


@functools.lru_cache(maxsize=1)
def load_strength_config() -> dict:
    return yaml.safe_load((CONFIG_DIR / "strength.yaml").read_text())


@functools.lru_cache(maxsize=1)
def _cfg() -> dict:
    return load_strength_config()


# metric name -> {family, direction, k, in_index, phase3}
STRENGTH_METRICS: dict[str, dict] = _cfg()["metrics"]
# domain name -> {side, label, metrics: [...]}
DOMAINS: dict[str, dict] = _cfg()["domains"]


def metric_family(metric: str) -> str:
    return STRENGTH_METRICS[metric]["family"]


def metric_bare(metric: str) -> str:
    """`team_offense.epa_per_play` -> `epa_per_play`."""
    return metric.split(".", 1)[1]


def orient_sign(metric: str) -> int:
    """+1 if higher is better, -1 if lower is better, 0 if neutral."""
    d = STRENGTH_METRICS[metric]["direction"]
    return {"higher_better": 1, "lower_better": -1, "neutral": 0}[d]


def families_used() -> list[str]:
    return sorted({m["family"] for m in STRENGTH_METRICS.values()})
