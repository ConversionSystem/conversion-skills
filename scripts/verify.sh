#!/usr/bin/env bash
# One command, full confidence: the six gates, the agent files, and the bundled engine.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"

echo "== gates =="
"$ROOT/scripts/sync-skills.sh"

echo "== agents validate =="
python3 - <<'PY'
import glob, sys
bad = 0
files = sorted(glob.glob('agents/*.md'))
for f in files:
    parts = open(f).read().split('---', 2)
    if len(parts) < 3:
        bad += 1; print("  agent missing frontmatter:", f); continue
    fm = parts[1]
    for k in ('name:', 'description:', 'tools:'):
        if k not in fm:
            bad += 1; print(f"  {f} missing {k}")
print(f"  {len(files)} agents checked, {bad} problems")
sys.exit(1 if bad else 0)
PY

echo "== bundled-engine smoke test =="
python3 skills/business-review/scripts/rollup.py examples/solo-vault/Memory/kpi-ledger.md \
  | python3 -c "import sys,json; d=json.load(sys.stdin); assert d['metrics'], 'no metrics'; print(f\"  engine ok: {len(d['metrics'])} metrics from {d['rows']} rows\")"

echo "== eval corpus =="
python3 "$ROOT/scripts/eval.py" validate

echo "== verify passed =="
