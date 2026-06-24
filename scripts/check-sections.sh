#!/usr/bin/env bash
# Heavy and high-stakes skills must carry the discipline sections:
# Red flags (self-detectors), Verification (observable exit criteria), Rationalizations (excuse to reality).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
HEAVY="site-audit seo-audit ads-audit business-review pipeline-review churn-watch free-audit optimizer operator client win-loss portfolio-watch crm-mining copy-optimize monitor grill hiring-signals a11y-audit"
REQUIRED=("## Red flags" "## Verification" "## Rationalizations")
fail=0
for slug in $HEAVY; do
  f="skills/$slug/SKILL.md"
  if [ ! -f "$f" ]; then echo "SECTIONS FAIL: missing $f"; fail=$((fail+1)); continue; fi
  for sec in "${REQUIRED[@]}"; do
    grep -qF "$sec" "$f" || { echo "SECTIONS FAIL: $slug missing '$sec'"; fail=$((fail+1)); }
  done
done
if [ "$fail" -gt 0 ]; then echo "Section check FAILED ($fail)."; exit 1; fi
echo "Section check passed: discipline sections present on all heavy skills."
