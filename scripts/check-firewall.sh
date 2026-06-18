#!/usr/bin/env bash
# Agency firewall gate: no cross-client references; no confidential client
# material outside a Clients/ workspace.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
fail=0
while IFS= read -r clientsdir; do
  vault="$(dirname "$clientsdir")"
  slugs="$(find "$clientsdir" -mindepth 1 -maxdepth 1 -type d ! -name '_archive' -exec basename {} \;)"
  for slug in $slugs; do
    for other in $slugs; do
      [ "$other" = "$slug" ] && continue
      hits="$(grep -rInE "(^|[^a-z0-9-])${other}([^a-z0-9-]|$)" "$clientsdir/$slug" 2>/dev/null || true)"
      if [ -n "$hits" ]; then
        echo "FIREWALL FAIL: client '$slug' references sibling '$other'"
        echo "$hits" | sed 's/^/    /'; fail=$((fail+1))
      fi
    done
  done
  # confidential client material must not live outside Clients/
  while IFS= read -r f; do
    case "$f" in *"/Clients/"*) ;; *) echo "FIREWALL FAIL: confidential file outside Clients/: $f"; fail=$((fail+1));; esac
  done < <(grep -rIl '^confidential: true' "$vault" 2>/dev/null || true)
done < <(find examples -type d -name Clients)
if [ "$fail" -gt 0 ]; then echo "Firewall check FAILED ($fail)."; exit 1; fi
echo "Firewall check passed: no cross-client leakage."
