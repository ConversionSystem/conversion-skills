#!/usr/bin/env bash
# Conversion System brand gate. Fails on any em-dash or any blocklist word on the
# shipped surface. Implements the guidelines badge: 0 em-dashes, 0 partnerships.
# BRAND.md is scanned for em-dashes but exempt from the blocklist scan (it names the list).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
SURFACE=(skills templates docs agents site README.md SKILLS.md BRAND.md GLOSSARY.md examples .claude-plugin assets NOTICE)
fail=0

# (a) em-dash (U+2014). En-dash (U+2013) in ranges is allowed and not matched here.
if grep -rIl '—' "${SURFACE[@]}" >/dev/null 2>&1; then
  echo "BRAND FAIL: em-dash found (brand mandates 0):"
  grep -rIno '—' "${SURFACE[@]}" 2>/dev/null | head -50 | sed 's/^/    /'
  fail=$((fail+1))
fi

# (b) blocklist words and phrases (skip BRAND.md, which documents the list)
WORDS='partner|journey|unlock|empower|transformative|holistic|seamless|synergize|ecosystem|scalable|reimagined|elevate|solutions'
PHRASES=("best-in-class" "world-class" "cutting-edge" "let's chat" "we'd love to" "circle back" "touch base" "north star" "hop on a quick call" "thought leadership" "drive value" "10x your")
while IFS= read -r f; do
  [ "$(basename "$f")" = "BRAND.md" ] && continue
  if grep -IinwE "$WORDS" "$f" >/dev/null 2>&1; then
    echo "BRAND FAIL: blocklist word in $f"; grep -IinwE "$WORDS" "$f" | sed 's/^/    /'; fail=$((fail+1))
  fi
  for p in "${PHRASES[@]}"; do
    if grep -Iin -F -i -- "$p" "$f" >/dev/null 2>&1; then
      echo "BRAND FAIL: blocklist phrase '$p' in $f"; fail=$((fail+1))
    fi
  done
done < <(grep -rIl . "${SURFACE[@]}" 2>/dev/null || true)

if [ "$fail" -gt 0 ]; then echo "Brand check FAILED."; exit 1; fi
echo "Brand check passed: 0 em-dashes, 0 blocklist terms on the surface."
