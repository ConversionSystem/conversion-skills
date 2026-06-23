#!/usr/bin/env bash
# Flags credentials that must never live in the vault (esp. Company/ + stack).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PAT='AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(password|passwd|secret|api[_-]?key|token)[[:space:]]*[:=][[:space:]]*[A-Za-z0-9/_+.-]{12,}'
hits=0
while IFS= read -r f; do
  if grep -InE "$PAT" "$f" >/dev/null 2>&1; then
    echo "SECRET FAIL: possible credential in $f"; grep -InE "$PAT" "$f" | sed 's/^/    /'; hits=$((hits+1))
  fi
done < <(find examples skills templates -type f \( -name '*.md' -o -name '*.py' \) 2>/dev/null || true)
if [ "$hits" -gt 0 ]; then echo "Secret scan FAILED ($hits file(s))."; exit 1; fi
echo "Secret scan passed: no credentials found."
