"""Ingestion: nflverse -> immutable raw cache -> canonical season-partitioned parquet."""
from matchup.ingest.runner import (
    SourceResult,
    configure_cache,
    ingest_all,
    ingest_source,
    processed_path,
)

__all__ = [
    "SourceResult",
    "configure_cache",
    "ingest_all",
    "ingest_source",
    "processed_path",
]
