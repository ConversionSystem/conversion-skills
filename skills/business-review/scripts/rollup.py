#!/usr/bin/env python3
"""business-review engine. Deterministic scorecard from the KPI ledger.

Optional. The skill runs this when Python 3 is available, else it follows the
prose Process by hand. Same scorecard either way. Shared parsing lives in
skills/_lib/ledger.py. Reads only; writes nothing; no credentials.

Usage:
  python3 rollup.py <path-to/Memory/kpi-ledger.md> [baseline.json]
"""
import sys
import os
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "_lib"))
import ledger  # noqa: E402


def main():
    args = sys.argv[1:]
    ledger_path = args[0] if args else "Memory/kpi-ledger.md"
    if not os.path.exists(ledger_path):
        print(json.dumps({"error": "ledger not found", "path": ledger_path}))
        return 1
    baseline = None
    if len(args) > 1 and os.path.exists(args[1]):
        baseline = json.load(open(args[1], encoding="utf-8"))
    rows = ledger.parse_ledger(ledger_path)
    cards = ledger.scorecard(rows, baseline)
    print(json.dumps({"rows": len(rows), "metrics": cards}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
