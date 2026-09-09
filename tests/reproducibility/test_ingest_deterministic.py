"""Reproducibility: two ingests against the same cache produce byte-identical
parquet, and the manifest differs only in ``ingested_at``."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest

from matchup.config import load_ingest
from matchup.ingest import ingest_source, processed_path
from matchup.store import clear_cache

pytestmark = [pytest.mark.network]

# small, fast sources
_SOURCES = ["ngs_passing", "pfr_pass", "team_stats"]


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@pytest.mark.parametrize("source", _SOURCES)
def test_reingest_is_byte_identical(source, tmp_path):
    cfg = load_ingest()
    part_dir = processed_path(source, _first_ok_season(source), cfg).parent
    parquet = part_dir / "data.parquet"
    manifest = part_dir / "_manifest.json"
    assert parquet.exists(), "run `matchup ingest` before the reproducibility test"

    sha_before = _sha(parquet)
    man_before = json.loads(manifest.read_text())

    backup = tmp_path / "backup.parquet"
    shutil.copy(parquet, backup)

    clear_cache()
    ingest_source(source, cfg)

    sha_after = _sha(parquet)
    man_after = json.loads(manifest.read_text())

    assert sha_after == sha_before, f"{source}: parquet bytes changed on re-ingest"
    assert man_after["content_sha256"] == man_before["content_sha256"]

    differing = {k for k in man_after if man_after[k] != man_before.get(k)}
    assert differing <= {"ingested_at"}, f"{source}: manifest changed beyond ingested_at: {differing}"


def _first_ok_season(source: str) -> int:
    from matchup.store import available_partitions

    return available_partitions(source)[0]
