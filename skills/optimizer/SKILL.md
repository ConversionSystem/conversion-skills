---
name: optimizer
description: Audits and hygiene-fixes a growing vault to keep it fast cheap and trustworthy run on a schedule like monthly when asked to optimize the vault audit structure clean up dead links check freshness enforce budgets verify the firewall or run a vault audit
---

# Conversion Optimizer

Scheduled vault hygiene that audits structure, links, freshness, budgets, firewall, frontmatter, and conflicts, then ships a concrete fix for every finding with human approval.

## When to use
- On a schedule (monthly default) to keep the vault fast, cheap, and trustworthy.
- When the user says "optimize the vault", "run a vault audit", "clean up dead links", "check what's stale", "we're over the size budget", or "verify the firewall".
- After a large import, a profile switch (Solo/Team/Agency), or a burst of new files that may have drifted from the taxonomy.
- Before a review cycle, when trust in the vault's accuracy matters.

## Inputs
- Operator budgets and the escalation contact from `_system/config.md` (reads/writes/housekeeping caps; stop cleanly at a cap).
- Active profile (Solo / Team / Agency) from `_system/config.md` · decides which folders and firewall rules apply.
- Rules from `_system/rules.md` and the root router map in `CLAUDE.md` (canonical homes for facts).
- The full set of `.md` files across the vault (every top-level taxonomy folder).
- Prior role cache `_system/state/vault-roles.json` if present (for incremental discovery).
- Optional: a category filter (e.g., "links only") and a freshness threshold override (default `reviewed:` older than 90d).

## Process

### Phase 0 · Discover and classify (cache)
1. Enumerate every `.md` under the vault root. Read frontmatter + headings to assign each file a **role** by signal, not by hardcoded name (router, context doc, ledger, decision, daily, SOP, client file, content piece, template, inbox item, etc.).
2. Write the role map to `_system/state/vault-roles.json` (`{path, role, profile_scope, confidential, reviewed, mtime, size_lines}`). Reuse the cache for unchanged `mtime` to stay inside read budgets.
3. Record baseline metrics for the report: file count, total lines, files over budget, stale count, dead-link count, orphan count, firewall flags.

### Phase 1 · Run all categories with judgment (each ships a concrete fix)

**The nine audit frameworks (named, so each is checkable).** Every run sweeps all nine; a finding under any of them still ships a concrete fix (existing behavior, unchanged). Map them onto the categories below:
- **Router quality (CLAUDE.md)** - does each router actually route (canonical homes named, no dead branches, no facts that belong in a leaf). Runs inside C1/C4.
- **Wikilink and graph integrity** - broken links (target missing), orphans (no inbound links), missing entity links. Runs inside C2.
- **Compression of bloated notes** - notes that have outgrown their budget or repeat themselves get a propose-summarize/split. Runs inside C4.
- **Context-rot** - stale `reviewed:` dates past the threshold and facts that contradict the current ledger or world. Runs inside C3/C7.
- **Memory size budgets** - root `CLAUDE.md`, folder routers, context docs, and `Memory/` files held to their line/token caps. Runs inside C4.
- **Progressive disclosure** - detail sitting in a router that belongs in a leaf (and vice versa); push depth down, keep routers thin. Runs inside C1/C4.
- **General hygiene** - frontmatter completeness, kebab-case/ISO naming, and placeholder leftovers (`TODO`, `{slug}`, `lorem`, empty sections). Runs inside C1/C6.
- **Reflection and contradiction-merge** - surface conflicting facts across files and reconcile them by proposing a single canonical source, never auto-picking a winner. Runs inside C7.
- **Architecture and discoverability plus firewall integrity** - canonical-home violations, undiscoverable files (no router path to them), and cross-client leakage. Runs inside C1/C5.

4. **C5 FIREWALL (Agency · run FIRST as a trust check):** scan for cross-client references (a file under `Clients/{a}/` naming or wikilinking `Clients/{b}/`), client material living outside its own `Clients/{slug}/` workspace, any `confidential:true` content leaked into shared folders, and credentials/secrets sitting in `Company/stack/`. Fix = quarantine to `Inbox/` with a flagged note, set `confidential:true`, and propose moving secrets out of `Company/stack/`. Report these before everything else.
5. **C1 Structure:** misplaced files (fact in the wrong canonical home per router), missing folder routers/profile folders, naming drift (non-kebab-case slugs, non-ISO dates), stale `Inbox/` items. Fix = move to canonical home, scaffold the missing router, rename to kebab-case/ISO, route aged Inbox items.
6. **C2 Links:** dead wikilinks (target missing), orphan notes (no inbound links), missing entity links (a known entity mentioned but unlinked). Fix = repoint/remove dead links, propose a backlink or archive for orphans, insert the entity wikilink.
7. **C3 Freshness:** `reviewed:` older than the threshold (default 90d), context docs with no date, dead projects (no activity / status not closed). Fix = flag for re-review, add the missing date, propose `status:` update or archive.
8. **C4 Budgets:** root `CLAUDE.md` >150 lines, folder `CLAUDE.md` >60, context docs >150, duplicated instructions across files, token bloat. Fix = propose a summarize/split (for any `CLAUDE.md`, **propose a diff only · never auto-edit**), dedupe repeated instruction blocks.
9. **C6 Frontmatter:** missing/invalid `type`/`status`/fewer than 2 `tags`, ledger column or format violations (`Memory/kpi-ledger.md`), missing `source`+`confidence` on ledger rows and decision files, slug↔client mismatches. Fix = add/repair frontmatter keys (hygiene only, never change meaning); for ledger column drift, propose the correction without rewriting prior rows.
10. **C7 Conflicts/Duplication:** contradicting facts across files, merge candidates surfaced from `Memory/lessons.md`. Fix = propose a merge or a single canonical source with the loser linked; never silently pick a winner on a meaning-bearing conflict.

### Phase 2 · Score
11. Score the vault 0–100 (or A–F) weighted with **firewall failures dominating**, then freshness/structure/budgets/links/frontmatter/conflicts. Each finding carries: category, severity, the **cited path(s)**, and a concrete proposed fix.

### Phase 3 · Walk every finding (one opening choice, then per-finding)
12. Present the count and score, then ONE opening choice: **bulk-apply / selective walk / save-all-to-plan / cancel.**
13. If selective walk, present each finding with its fix and three actions: **apply-now / save-to-plan / decline.** For any `CLAUDE.md` change, render the proposed diff and require explicit approval (no auto-edit, ever).
14. Saved-to-plan findings collect into the report's action list; declined findings are recorded as declined.

### Phase 4 · Apply approved fixes (smallest blast radius first)
15. Order approved fixes safest-first: frontmatter repairs and link repoints before renames/moves before merges. Respect write/housekeeping budgets; stop cleanly at a cap and note the remainder in the report.
16. **Before any delete or move:** grep the whole vault for inbound references to the target path; if any exist, downgrade to a repoint or route to `Inbox/` instead of deleting. Never delete without this check.
17. Refresh `_system/state/vault-roles.json` for touched files and recompute after-metrics.

### Phase 5 · Report
18. Write `Operations/reviews/{date}-vault-audit.md` (`generated:true`) with before/after metrics, the score, every finding with its cited path and disposition (applied/planned/declined), and an audit-trail note appended under `_system/audit/`.

## Outputs
- `Operations/reviews/{date}-vault-audit.md` · the audit report (`generated:true`), with before/after metrics, score, and per-finding dispositions citing paths.
- `_system/state/vault-roles.json` · refreshed role/discovery cache.
- An audit-trail entry under `_system/audit/` recording the run, budgets consumed, and fixes applied.
- In-place hygiene edits to approved files only (frontmatter repairs, link repoints, renames, moves, dedupes) · meaning unchanged.
- Proposed `CLAUDE.md` diffs (never applied automatically) recorded in the report for the user to accept.
- No KPI-ledger rows are appended by this module (it audits the ledger's format but does not write metrics into it).

## Guardrails
- **Approval gates:** never autonomously delete files, publish, send external messages, change pricing/offers, or edit permissions. Every fix is walked and approved; the opening bulk-apply still routes each fix through the same apply order.
- **Never auto-edit any `CLAUDE.md`** · propose a diff via the walk and require explicit acceptance.
- **Never delete without grepping inbound references** first; prefer repoint or route-to-`Inbox/` over deletion.
- **Firewall (Agency):** never read a sibling `Clients/{slug}/` to "resolve" a finding; report cross-client leaks first as trust failures; keep every client file `confidential:true`; ambiguous entity → `Inbox/`, never guess.
- **Append-only ledger:** never edit, reorder, or delete prior rows in `Memory/kpi-ledger.md`; only flag format violations for the user.
- **Hygiene only, never change meaning:** repair structure/frontmatter/links; never rewrite the substance of a note. Meaning-bearing conflicts are proposed as merges, not auto-resolved.
- **Every finding cites a path.** No path, no finding.
- **Frontmatter:** enforce the universal keys (`type`, `status`, `owner`, `date`, `reviewed`, `tags`≥2, `confidential`, `source`, `generated`) and the `source`+`confidence` requirement on ledger rows and decision files.
- **Budgets:** read from `_system/config.md`; stop cleanly when a reads/writes/housekeeping cap is hit and record the remainder in the report.

## Red flags
- Scoring a category or writing a finding with no `path:` cited, the skill's own "no path, no finding" rule broken mid-run.
- Editing a `CLAUDE.md` directly instead of rendering a diff and waiting for explicit acceptance.
- Deleting or moving a file without first grepping the vault for inbound references to that path.
- Reading a sibling `Clients/{slug}/` to "resolve" a firewall finding, the cross-client leak you are supposed to report.
- Rewriting a note's substance under the banner of hygiene, or auto-picking a winner on a meaning-bearing conflict instead of proposing a merge.
- Editing, reordering, or backfilling prior rows in `Memory/kpi-ledger.md` rather than just flagging the format violation.
- Blowing past a reads/writes/housekeeping cap from `_system/config.md` instead of stopping cleanly and noting the remainder.

## Verification
- [ ] Every finding cites at least one file path; zero pathless findings shipped.
- [ ] Firewall (Agency) ran FIRST and any cross-client leak is reported before all other categories, with no sibling `Clients/` read to resolve it.
- [ ] Score is recorded with firewall failures weighted to dominate, and before/after metrics are both captured.
- [ ] No `CLAUDE.md` was auto-edited; every proposed `CLAUDE.md` change exists only as a diff awaiting acceptance.
- [ ] No delete or move happened without a prior inbound-reference grep; targets with inbound links were downgraded to repoint or routed to `Inbox/`.
- [ ] Only walked-and-approved fixes were applied; declined findings are recorded as declined, planned findings collected in the action list.
- [ ] Nothing was published, sent, or deleted autonomously, and no prior `Memory/kpi-ledger.md` row was edited or reordered.
- [ ] All nine named frameworks were swept (router quality, graph integrity, compression, context-rot, memory budgets, progressive disclosure, general hygiene, contradiction-merge, architecture/discoverability plus firewall), each finding still carrying a concrete fix.
- [ ] The report `Operations/reviews/{date}-vault-audit.md` is `generated:true` with per-finding disposition, and an audit-trail entry under `_system/audit/` records budgets consumed.

## Rationalizations
| Rationalization | Reality |
|---|---|
| "The dead link is obviously safe to delete, skip the grep." | Skip the grep and you orphan whatever pointed at it. Every delete and move greps inbound references first, no exceptions. |
| "This `CLAUDE.md` is 30 lines over, I'll just trim it inline." | Auto-editing a router is how the vault silently loses its routing map. Render the diff, get explicit acceptance, never touch it otherwise. |
| "Two files contradict, I'll keep the newer one and move on." | Picking a winner on a meaning-bearing conflict changes substance, not hygiene. Propose a merge with the loser linked and let the human decide. |
| "I'll just peek at the other client's folder to confirm the leak." | Reading sibling `Clients/{slug}/` is the exact firewall breach you exist to catch. Report the cross-client reference and stop; never open the sibling. |
| "I hit the write cap but there are only three fixes left, push them through." | A cap is a hard stop, not a suggestion. Apply nothing past it, note the remainder in the report, and let the next run finish the job. |

## References
- `_system/config.md` · operator budgets, active profile, escalation contact.
- `_system/rules.md` and root `CLAUDE.md` · routing map and canonical homes.
- `_system/state/vault-roles.json` · discovery/role cache (read + write).
- `Memory/kpi-ledger.md`, `Memory/lessons.md` · ledger format check and merge-candidate source.
- `Operations/reviews/` and `_system/audit/` · report and audit-trail destinations.
