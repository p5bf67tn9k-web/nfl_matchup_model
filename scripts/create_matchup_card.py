#!/usr/bin/env python
"""Generate a matchup card (PNG + PDF) from the existing team-strength model.

    python scripts/create_matchup_card.py --away NE --home SEA --season 2026 --week 1

Writes outputs/matchups/{season}_week{week}_{AWAY}_{HOME}.{png,pdf} by default.
This script performs no strength calculation -- it renders the model's
existing outputs. See src/matchup/visualization/data.py for the exact
source columns.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from matchup.visualization.data import MatchupDataError
from matchup.visualization.matchup_card import create_matchup_card


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--away", required=True, help="away team abbreviation, e.g. NE")
    p.add_argument("--home", required=True, help="home team abbreviation, e.g. SEA")
    p.add_argument("--season", type=int, required=True)
    p.add_argument("--week", type=int, required=True)
    p.add_argument("--output-dir", type=Path, default=None,
                    help="default: outputs/matchups/")
    args = p.parse_args(argv)

    try:
        png_path, pdf_path = create_matchup_card(
            args.away, args.home, args.season, args.week, output_dir=args.output_dir,
        )
    except MatchupDataError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(f"wrote {png_path}")
    print(f"wrote {pdf_path}")


if __name__ == "__main__":
    main()
