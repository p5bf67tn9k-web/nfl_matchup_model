"""Typed loaders for config/*.yaml. Config is data, not code."""
from __future__ import annotations

import functools
from enum import Enum
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "config"


def _read_yaml(name: str) -> dict[str, Any]:
    return yaml.safe_load((CONFIG_DIR / name).read_text())


# --------------------------------------------------------------------------- #
# point-in-time status
# --------------------------------------------------------------------------- #
class PITStatus(str, Enum):
    LIVE_SAFE = "LIVE_SAFE"
    HISTORICAL_SAFE = "HISTORICAL_SAFE"
    POST_SEASON_ONLY = "POST_SEASON_ONLY"
    REFERENCE_ONLY = "REFERENCE_ONLY"
    UNKNOWN = "UNKNOWN"

    @property
    def admissible_to_feature_frame(self) -> bool:
        """Only LIVE_SAFE and HISTORICAL_SAFE may enter a prediction feature frame.

        HISTORICAL_SAFE is admissible only in backtest mode (enforced by the caller);
        the as-of engine additionally blocks it from live frames.
        """
        return self in (PITStatus.LIVE_SAFE, PITStatus.HISTORICAL_SAFE)


LagType = Literal["empirical", "conservative_assumption", "known", "unknown"]


class SourcePIT(BaseModel):
    name: str
    grain: str
    join: str | list[str]
    point_in_time_status: PITStatus
    earliest_valid_season: int | None = None
    publish_lag_days: int | None = None
    publish_lag_type: LagType
    rationale: str = ""
    fallback_rule: str | None = None
    reference_only_columns: list[str] = Field(default_factory=list)


class PublishLagConfig(BaseModel):
    assumed_game_duration_hours: int
    kickoff_fallback_local_time: str
    timezone: str
    globally_stripped_columns: list[str] = Field(default_factory=list)
    sources: dict[str, SourcePIT]

    def get(self, source: str) -> SourcePIT:
        if source not in self.sources:
            raise KeyError(
                f"source {source!r} has no point-in-time contract in config/publish_lag.yaml"
            )
        return self.sources[source]


@functools.lru_cache(maxsize=1)
def load_publish_lag() -> PublishLagConfig:
    raw = _read_yaml("publish_lag.yaml")
    defaults = raw["defaults"]
    sources = {
        name: SourcePIT(name=name, **body) for name, body in raw["sources"].items()
    }
    return PublishLagConfig(
        assumed_game_duration_hours=defaults["assumed_game_duration_hours"],
        kickoff_fallback_local_time=defaults["kickoff_fallback_local_time"],
        timezone=defaults["timezone"],
        globally_stripped_columns=defaults.get("globally_stripped_columns", []),
        sources=sources,
    )


# --------------------------------------------------------------------------- #
# ingest config
# --------------------------------------------------------------------------- #
class IngestSource(BaseModel):
    name: str
    loader: str
    seasons: list[int] | Literal["all", "none"]
    partition_by: Literal["season", "none"]
    kwargs: dict[str, Any] = Field(default_factory=dict)

    def season_list(self, hard_max: int) -> list[int]:
        if self.seasons in ("all", "none"):
            return []
        lo, hi = self.seasons
        return list(range(lo, min(hi, hard_max) + 1))


class IngestConfig(BaseModel):
    output_root: str
    cache_root: str
    sources: dict[str, IngestSource]
    live_seasons_probe: list[int]


@functools.lru_cache(maxsize=1)
def load_ingest() -> IngestConfig:
    raw = _read_yaml("ingest.yaml")
    sources = {
        name: IngestSource(name=name, **body) for name, body in raw["sources"].items()
    }
    return IngestConfig(
        output_root=raw["output_root"],
        cache_root=raw["cache_root"],
        sources=sources,
        live_seasons_probe=raw["live_seasons_probe"],
    )
