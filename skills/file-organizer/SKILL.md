---
name: file-organizer
description: Sort a messy folder into the vault's correct homes by classifying each file, proposing routes from the root router map, and moving only on approval. Triggers on "organize this folder", "clean up my files", "sort my inbox", "route these files", "where does this file go".
---

# File Organizer

Take a folder of loose files and move each one to its correct vault home. Classify, propose a route per the root router map, move on your approval, and report what landed where.

## When to use
- You dropped a batch of files into Inbox/ or a Downloads folder and want them filed.
- You have stray files scattered across the vault that belong in proper homes.
- After an import, export, or hand-off, and the new files need sorting.
- You want a dry run of where files would go before anything moves.

## Inputs
- Source folder path (default: `Inbox/`).
- Optional scope filter (file types, date range, or a name pattern).
- The root router map in `CLAUDE.md` (the routing table that maps content kinds to vault homes).
- The vault taxonomy and any overrides in `_system/rules/`.
- Active client context if any files are client-bound (firewall applies).

## Process
1. Read the root router map in `CLAUDE.md` and the taxonomy notes in `_system/rules/`. These define every valid destination. If no router map exists, build the proposal from the standard taxonomy and flag that `CLAUDE.md` has no routing table.
2. List every file in the source folder (default `Inbox/`), recursively. Skip `.git/`, `_system/audit/`, and any path the rules mark do-not-touch.
3. Classify each file by name, extension, and a short content peek (first lines for text, frontmatter for markdown). Assign a kind: company doc, profile, brand, offer, ICP, strategy, market, competitor, KPI or metric note, decision, lesson, pipeline item, client file, project asset, content draft, SOP or process, meeting or review note, daily note, library template or playbook or prompt, or unknown.
4. Map each kind to a destination home using the router map. Examples: a brand reference goes to `Company/brand/`, a reusable template goes to `Library/templates/`, an SOP goes to `Operations/sops/`, a client-bound file goes to `Clients/{slug}/` (only the active client), a project asset goes to `Projects/{slug}/data/` or `Projects/{slug}/final/`.
5. For client files, enforce the firewall: route only to the active client's folder. If a file names a different client, hold it and ask. Never cross client boundaries.
6. Mark every file as confident or needs-review. Anything you cannot classify gets routed to a holding spot, not deleted, and is listed for the user.
7. Present the full routing table: each file, its detected kind, its proposed destination, and a confidence flag. Wait for approval. No move happens before this.
8. On approval, move the approved files with `git mv` so history is preserved. Create any missing destination folders first. Files flagged needs-review stay put unless the user approves them by name.
9. Re-list the source folder and confirm what remains. Write an audit line per move to `_system/audit/` with timestamp, source path, destination path, and the kind.
10. Report the final tally: moved, held, and skipped, with counts and paths.

## Outputs
- Files moved to their vault homes via `git mv` (history preserved), only those you approved.
- An audit record appended to `_system/audit/file-organizer-{date}.md`: one row per move with source, destination, kind, and timestamp.
- A run summary written to `Operations/tasks.md` (or printed if you decline) listing moved, held for review, and skipped, with counts.
- Unclassified files left in place or moved to a clearly named holding folder under the source, listed by path for your decision.

## Guardrails
- Never delete a file. Files only move, and only to a route you confirmed.
- No move without approval. The routing table is a proposal until you say go.
- FIREWALL: client files route only to the active client. A file naming another client is held and surfaced, never moved across the boundary.
- Use `git mv` so every move is versioned and reversible.
- PROVENANCE: classification is based on the file's own name and content, never invented. Low-confidence guesses are flagged, not silently filed.
- Respect do-not-touch paths in `_system/rules/` and skip `_system/audit/` and `.git/`.
- The KPI ledger is append-only. If a file looks like ledger data, hold it for the user rather than editing any prior rows.

## References
- `CLAUDE.md` root router map
- `_system/rules/` for overrides and do-not-touch paths
- Vault taxonomy (Company, Memory, Pipeline, Clients, Projects, Content, Operations, Daily, Library, Inbox)
