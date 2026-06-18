#!/usr/bin/env bash
# Enforces size budgets: root vault CLAUDE.md <=150, folder CLAUDE.md <=60, context docs <=150.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
fail=0
while IFS= read -r f; do
  lines=$(wc -l < "$f" | tr -d ' ')
  # a vault-root router sits directly under a vault dir (…/CLAUDE.md with no parent CLAUDE.md sibling folder)
  case "$f" in
    */solo-vault/CLAUDE.md|*/team-vault/CLAUDE.md|*/agency-vault/CLAUDE.md|./CLAUDE.md)
      max=150 ;;
    *)
      max=60 ;;
  esac
  if [ "$lines" -gt "$max" ]; then echo "BUDGET FAIL: $f has $lines lines (max $max)"; fail=$((fail+1)); fi
done < <(find . -name CLAUDE.md -not -path '*/.git/*')
# context docs (Company/*.md) <=150
while IFS= read -r f; do
  lines=$(wc -l < "$f" | tr -d ' ')
  if [ "$lines" -gt 150 ]; then echo "BUDGET WARN: context doc $f has $lines lines (max 150)"; fi
done < <(find . -path '*/Company/*.md' -not -name CLAUDE.md -not -path '*/.git/*')
if [ "$fail" -gt 0 ]; then echo "Budget check FAILED."; exit 1; fi
echo "Budget check passed."
