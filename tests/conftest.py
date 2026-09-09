"""Shared pytest fixtures. Configures nflreadpy to use the repo-local filesystem cache
so `network`-marked tests reuse the Phase 0 audit downloads."""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session", autouse=True)
def _nflreadpy_cache():
    from nflreadpy.config import update_config

    update_config(
        cache_mode="filesystem",
        cache_dir=Path(ROOT / "data" / "raw" / "nflreadpy_cache"),
        cache_duration=7 * 86400,
        verbose=False,
    )
