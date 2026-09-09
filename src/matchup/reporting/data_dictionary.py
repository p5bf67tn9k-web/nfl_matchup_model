"""Generate reports/data_dictionary.md from the config + the ingested manifests.

Config is the single source of truth; this keeps the human doc in sync with what
the pipeline actually does.
"""
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from matchup.config import REPO_ROOT, load_ingest, load_publish_lag

ATTRIBUTION = """\
## Attribution & licensing

All data is retrieved through **nflverse** (`nflreadpy`).

* **nflverse data** is released under **CC-BY-SA 4.0**. Attribute to *nflverse*.
* **Advanced stats** (`pfr_*` sources) are derived from **Pro Football Reference**
  (2018+) and surfaced via nflverse. Attribute to *Pro Football Reference via nflverse*.
* **Next Gen Stats** (`ngs_*`) are **NFL Next Gen Stats**, surfaced via nflverse.
* **Participation** data (2023+) is courtesy of **FTN Data via nflverse**
  (CC-BY-SA 4.0) and is *not* used in the model (POST_SEASON_ONLY).
* **Betting lines / scores** in `schedules` are market / results data and are
  **never** used as model inputs (REFERENCE_ONLY).

This project is independent of any betting model and is not optimized for betting
ROI or agreement with any sportsbook market.
"""


def _manifests_for(source: str) -> list[dict]:
    d = Path(REPO_ROOT / load_ingest().output_root) / source
    out = []
    for man in sorted(d.glob("**/_manifest.json")):
        out.append(json.loads(man.read_text()))
    return out


def _coverage_line(mans: list[dict]) -> str:
    ok = [m for m in mans if m.get("status") == "ok"]
    un = [m for m in mans if m.get("status") == "unavailable"]
    seasons = sorted(m["season"] for m in ok if m.get("season") is not None)
    rows = sum(m.get("row_count", 0) for m in ok)
    flat = [m for m in ok if m.get("season") is None]
    if seasons:
        span = f"{seasons[0]}–{seasons[-1]} ({len(seasons)} partitions)"
    elif flat:
        span = "single file (no season key)"
    else:
        span = "none"
    un_txt = ""
    if un:
        un_txt = f"; unavailable: {sorted(str(m['season']) for m in un)}"
    return f"{span}, {rows:,} rows{un_txt}"


def build_markdown() -> str:
    ing = load_ingest()
    pit = load_publish_lag()
    now = datetime.now(UTC).isoformat(timespec="seconds")

    lines: list[str] = []
    lines.append("# Data Dictionary — canonical layer (`data/processed/`)")
    lines.append("")
    lines.append(f"_Generated {now} from `config/ingest.yaml`, `config/publish_lag.yaml`, "
                 f"and the ingested `_manifest.json` sidecars._")
    lines.append("")
    lines.append("Every source below is materialised as season-partitioned Parquet at "
                 "`data/processed/<source>/season=YYYY/data.parquet` with a `_manifest.json` "
                 "sidecar (row count, column count, content SHA-256, point-in-time status, "
                 "publish-lag assumption, source date range, ingest timestamp).")
    lines.append("")
    lines.append("## Point-in-time status legend")
    lines.append("")
    lines.append("| status | meaning |")
    lines.append("|---|---|")
    lines.append("| `LIVE_SAFE` | knowable before kickoff in real time during the season |")
    lines.append("| `HISTORICAL_SAFE` | safe for backtest, not guaranteed available live |")
    lines.append("| `POST_SEASON_ONLY` | published only after the season → blocked from prediction frames |")
    lines.append("| `REFERENCE_ONLY` | benchmark / identity only → blocked from feature frames |")
    lines.append("| `UNKNOWN` | timing unproven → blocked |")
    lines.append("")
    lines.append("## `publish_lag_type` legend")
    lines.append("")
    lines.append("| type | meaning |")
    lines.append("|---|---|")
    lines.append("| `empirical` | a real per-row publication timestamp exists and is used directly |")
    lines.append("| `conservative_assumption` | **no** publication timestamp in the data; a deliberately cautious engineering guess (prefer false exclusion). NOT an exact release time. |")
    lines.append("| `known` | timing structurally known (schedule fixtures) |")
    lines.append("| `unknown` | timing cannot be reconstructed |")
    lines.append("")
    lines.append("## Sources")
    lines.append("")

    for name, spec in ing.sources.items():
        p = pit.sources.get(name)
        mans = _manifests_for(name)
        lines.append(f"### `{name}`")
        lines.append("")
        lines.append(f"* **loader:** `nflreadpy.{spec.loader}("
                     + ", ".join(f"{k}={v!r}" for k, v in spec.kwargs.items())
                     + ")`")
        lines.append(f"* **grain:** {p.grain if p else '?'}")
        lines.append(f"* **join key:** `{p.join if p else '?'}`")
        lines.append(f"* **point-in-time status:** `{p.point_in_time_status.value if p else '?'}`")
        lag = "n/a" if not p or p.publish_lag_days is None else f"{p.publish_lag_days} day(s)"
        lines.append(f"* **publish-lag assumption:** {lag} "
                     f"(`{p.publish_lag_type if p else '?'}`)")
        if p and p.earliest_valid_season is not None:
            lines.append(f"* **earliest valid season:** {p.earliest_valid_season}")
        if p and p.fallback_rule:
            lines.append(f"* **as-of fallback rule:** `{p.fallback_rule}`")
        if p and p.reference_only_columns:
            lines.append("* **REFERENCE_ONLY columns (stripped before any feature frame):** "
                         + ", ".join(f"`{c}`" for c in p.reference_only_columns))
        lines.append(f"* **materialised coverage:** {_coverage_line(mans)}")
        if p and p.rationale:
            lines.append(f"* **notes:** {' '.join(p.rationale.split())}")
        lines.append("")

    lines.append(ATTRIBUTION)
    return "\n".join(lines)


def write_data_dictionary(path: Path | None = None) -> Path:
    path = path or (REPO_ROOT / "reports" / "data_dictionary.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_markdown())
    return path
