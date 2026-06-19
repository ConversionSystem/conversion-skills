---
name: setup
description: Turn an empty folder into a personalized governed Conversion Skills vault with a 10-minute first win, triggered by setup conversion skills, initialize my vault, get started, onboard me, build my conversion skills, first-time setup, or scaffold my workspace.
---

# Conversion Skills Setup
Turns an empty (or partial) folder into a personalized, governed Conversion Skills vault that delivers a 10-minute first win, then deepens over time.

## When to use
- The vault is empty or missing its root `CLAUDE.md` and `_system/` and the user wants to get started.
- The user says "set up Conversion Skills", "initialize my vault", "onboard me", "build my workspace", or runs this on a fresh synced folder.
- An existing vault needs re-detection, profile selection, or a guided re-seed of thin context.
- Not for routine work once the vault exists · use the daily, content, or pipeline modules instead.

## Inputs
- Required: write access to the target folder (a synced folder is the zero-infra default).
- Strongly preferred (import-first): one or more website URL(s) to fetch, and any pasted/linked docs (deck, brand guide, pricing page, about page).
- Optional: one connector to read (e.g. a CRM, inbox, or analytics export) named in plain language.
- Profile choice: Solo, Team, or Agency (offered with a recommendation; user confirms).
- A handful of skippable interview answers to fill gaps the import could not.
- The contact who owns outbound approvals (captured into `_system/config.md`).

## Process
Phase 0 · PREFLIGHT (detect + profile)
1. Scan the target folder. Check for an existing vault by looking for root `CLAUDE.md`, `_system/config.md`, and the `Company/` tree.
2. If a vault exists: do NOT overwrite. Report what is present, offer to repair/extend missing pieces only, and confirm before writing. If absent: proceed as a fresh build.
3. Offer the three profiles of one architecture and recommend one from any signals already seen:
   - Solo · one operator; activates `Pipeline/`.
   - Team · multiple internal people; activates `Team/` and permission rows in `_system/permissions.md`.
   - Agency · serves external clients; activates `Clients/{slug}/` (firewalled) plus `Team/`.
   Confirm the choice before scaffolding.

Phase 1 · IMPORT-FIRST (infer, don't interrogate)
4. Ask for website URL(s) and any docs up front. Fetch and read them. Infer company profile, brand voice, offers, pricing signals, and ICP from the pages.
5. If the user offers one connector, read only what is needed to enrich context (read-only; never send anything). Park anything ambiguous in `Inbox/`.
6. Build a draft of `Company/profile.md`, `Company/brand.md`, `Company/offers.md`, `Company/icp.md`, and `Company/strategy.md` in memory so the interview only CONFIRMS, never re-asks what was already inferred.

Phase 2 · MINIMAL INTERVIEW (skippable gap-fill)
7. Ask only for gaps the import left, each skippable:
   - Founder / business one-liner.
   - Offers + pricing (confirm or correct what was inferred).
   - ICP (who you serve, one sentence).
   - Brand voice (a few adjectives or "match the site").
   - Top goal for the next 90 days (used as the first KPI target).
8. Capture the outbound-approval contact and basic operator budgets for `_system/config.md`. Default budgets if the user skips.

Phase 3 · SILENT SCAFFOLD (write the locked taxonomy)
9. Create the locked top-level taxonomy for the chosen profile. Always create: `CLAUDE.md` (root router), `_system/` (`config.md`, `rules.md`, `connectors.md`, `permissions.md`, `hooks/`, `audit/`, `state/`), `Company/` (`profile.md`, `brand.md`, `offers.md`, `icp.md`, `strategy.md`, `market.md`, `competitors.md`, `stack.md`, `departments/`), `Memory/` (`kpi-ledger.md`, `decisions/`, `lessons.md`, `glossary.md`), `Projects/{slug}/`, `Content/{slug}-{date}/`, `Operations/` (`sops/`, `processes/`, `meetings/`, `reviews/`, `tasks.md`), `Daily/`, `Library/` (`playbooks/`, `templates/`, `prompts/`, `styles/`), `Inbox/`.
   - Solo also creates `Pipeline/` (`accounts/`, `prospects/`, `deals.md`).
   - Team also creates `Team/{person}/` (`profile.md`, `access.md`, `tasks.md`) and adds rows to `_system/permissions.md`.
   - Agency also creates `Clients/{slug}/` (firewalled, every file `confidential:true`) and `Team/{person}/`, and keeps `Pipeline/` for prospects.
10. Write the root `CLAUDE.md` router (<=150 lines) mapping every concept to its canonical home, and a per-folder `CLAUDE.md` router (<=60 lines) in each top-level folder.
11. Write `_system/config.md` (profile, owner, outbound-approval contact, operator budgets for reads/writes/transcripts/emails/dms/housekeeping), `_system/rules.md` (guardrails: human-approval gates, firewall, route-to-canonical, append-only ledger), and seed `_system/connectors.md` and `_system/permissions.md`.
12. Seed `Company/*` from confirmed answers and imports. Write only what is known · no bracket placeholders; omit empty sections entirely. One concept per file, kebab-case slugs, ISO dates.
13. Seed `Memory/kpi-ledger.md` with the exact header row, then append the user's first baseline rows (each with `source` and `confidence`); use the top goal as the `target`.
14. Create today's Daily note at `Daily/YYYY-MM-DD.md` (use the current date).
15. Copy only the templates this profile needs from the plugin's templates into `Library/templates/` (e.g. daily note, KPI row, decision record, SOP, content brief; plus client and team templates for Agency/Team).
16. Put universal frontmatter on every `.md` written: `type`, `status`, `owner`, `date`, `reviewed`, `tags` (>=2), `confidential`, `source`, `generated`.

Phase 4 · FIRST DELIVERABLE + REPORT CARD
17. Produce one immediately useful artifact now · a 7-day growth plan written to `Projects/` (or a first daily brief appended to today's `Daily/` note) grounded in the seeded context.
18. Produce a report card rating each context area solid / thin / missing (`Company/profile`, `brand`, `offers`, `icp`, `strategy`, `market`, `competitors`, KPI baselines, pipeline/clients/team as applicable) so the user knows exactly what to deepen next.
19. Hand off: point to the root `CLAUDE.md`, name the thin areas, and suggest the next module to run. Stop cleanly.

## Outputs
- `CLAUDE.md` · root router (<=150 lines).
- One `CLAUDE.md` router per top-level folder (<=60 lines each).
- `_system/config.md`, `_system/rules.md`, `_system/connectors.md`, `_system/permissions.md` (+ `hooks/`, `audit/`, `state/` dirs).
- `Company/profile.md`, `brand.md`, `offers.md`, `icp.md`, `strategy.md`, and any of `market.md` / `competitors.md` / `stack.md` that have real content; `departments/` dir.
- `Memory/kpi-ledger.md` with header + first baseline rows appended (each with `source` + `confidence`); `Memory/decisions/`, `lessons.md`, `glossary.md`.
- `Daily/YYYY-MM-DD.md` · today's note.
- `Library/templates/` · the templates this profile needs, copied from the plugin.
- Profile-specific trees: Solo → `Pipeline/` (`accounts/`, `prospects/`, `deals.md`); Team → `Team/{person}/` + `_system/permissions.md` rows; Agency → `Clients/{slug}/` (firewalled, `confidential:true`) + `Team/{person}/`.
- First deliverable: a 7-day growth plan in `Projects/{slug}/` or a first brief in today's `Daily/` note.
- A report card (solid / thin / missing per context area) returned to the user.
- Ledger rows appended: first baseline KPI rows in `Memory/kpi-ledger.md`.

## Guardrails
- Human-approval gates: never autonomously send external messages/email/DM, delete files, publish content, change pricing/offers, edit permissions, or contact clients. Any outbound is drafted `status:draft` and escalated to the contact in `_system/config.md`.
- Existing-vault safety: never overwrite an existing vault; detect first, repair only missing pieces, confirm before writing.
- Firewall (Agency): never read a sibling `Clients/{slug}/`; every client file is `confidential:true`. Ambiguous entity → file to `Inbox/`, never guess.
- KPI ledger is APPEND-ONLY with exact columns `| date | metric | baseline | current | target | source | confidence |  note |`; `confidence` in {confirmed, reported, inferred, stale}. Never edit, reorder, or delete prior rows.
- Universal frontmatter on every `.md` (`type`, `status`, `owner`, `date`, `reviewed`, `tags` >=2, `confidential`, `source`, `generated`); `source` + `confidence` required on ledger rows and decision files.
- Route every fact to its canonical home per the root router; one concept per file; kebab-case slugs; ISO dates.
- Size budgets: root `CLAUDE.md` <=150 lines, folder `CLAUDE.md` <=60, context docs <=150.
- No bracket placeholders and no invented facts · omit empty sections; mark unknowns as thin/missing in the report card instead.
- Respect operator budgets in `_system/config.md` (reads/writes/transcripts/emails/dms/housekeeping); stop cleanly when a cap is hit.

## References
- `Library/templates/` source templates from the plugin (daily note, KPI row, decision record, SOP, content brief, plus client and team templates for Agency/Team).
