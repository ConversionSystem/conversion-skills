#!/usr/bin/env bash
# Fails if banned upstream/product terms appear on the Conversion OS surface.
# The whole shipped surface is scanned, including NOTICE. scripts/ hold the rule itself.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
BANNED='BenAI|benai|system3|Relay\.md|relay-fork|Plot\.md|naveedharri'
TARGETS=(skills templates examples docs agents .claude-plugin CLAUDE.md README.md SKILLS.md NOTICE)
hits=0
for t in "${TARGETS[@]}"; do
  [ -e "$t" ] || continue
  while IFS= read -r f; do
    if grep -InE "$BANNED" "$f" >/dev/null 2>&1; then
      echo "CLEANROOM FAIL: banned term in $f"
      grep -InE "$BANNED" "$f" | sed 's/^/    /'
      hits=$((hits+1))
    fi
  done < <(grep -rIl . "$t" 2>/dev/null || true)
done
if [ "$hits" -gt 0 ]; then echo "Clean-room lint FAILED ($hits file(s))."; exit 1; fi
echo "Clean-room lint passed: no banned terms on the product surface."
