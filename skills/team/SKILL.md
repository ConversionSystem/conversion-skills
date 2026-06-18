---
name: team
description: Roll Conversion OS across a team with sync setup, person seats, AI access scoping, offboarding, and access audits · use when adding a teammate, choosing a sync method, scoping who sees which clients, removing someone, or reviewing team permissions.
---

# Conversion Team OS

Rolls the OS across a team with real, layered permissions · choosing a sync method, seating people, scoping what the AI loads per person, offboarding cleanly, and auditing access against reality. Team and Agency profiles only.

## When to use

- The operator wants to share one vault across machines or people and asks which sync method to use.
- Adding a teammate or contractor (seat), or changing what clients a person works on.
- Regenerating per-person AI access after editing an `access.md`.
- Removing someone from the team (offboard).
- Reviewing whether stated access matches reality (audit), ideally quarterly.

If the vault is currently a Solo profile, first confirm the operator wants to activate Team (adds `Team/`, `Pipeline/` stays, updates root `CLAUDE.md` routing) or Agency (also activates firewalled `Clients/{slug}/`). Never silently switch profiles.

Rollout note worth saying to a fresh team vault: run it solo for 2-3 weeks, then add the most curious teammate before the most senior one. Top-down mandates stall; visible value spreads.

## Inputs

- Active profile from `_system/config.md` (must be Team or Agency).
- The escalation contact and operator budgets in `_system/config.md`.
- For a seat: person name, role (owner | member | contractor), full-time vs contractor, and which clients/projects they touch.
- For sync: team size, whether edit history matters, whether realtime co-edit is needed, whether encryption-at-rest is required, and git comfort level.
- Existing `Team/{person}/access.md` files and client/project `team:` arrays for scope and audit.

## Process

**Phase A · SYNC (recommend one method, honestly).**
1. Read `_system/config.md` to confirm profile and read team size.
2. Walk these three options as a decision tree and recommend exactly ONE; state its tradeoffs out loud, then give setup steps:
   - **Shared drive + git** · any synced folder (iCloud/Dropbox/Drive) for the live files, a git repo underneath for full history and rollback. Best when history and auditability matter and the team is git-comfortable. Tradeoff: not realtime, merge conflicts on simultaneous edits to the same file.
   - **Realtime co-edit** · a folder-level collaborative-sync tool layered on the vault so two people can edit live. Best for small teams (roughly 3 or fewer) that edit together often. Tradeoff: weaker history than git, another dependency, free tiers are seat-capped.
   - **Encrypted sync** · an end-to-end-encrypted self-hosted sync for privacy-first or multi-device-solo setups. Best when encryption-at-rest is a hard requirement. Tradeoff: more setup, fewer collaborators, you own recovery.
3. Never layer two whole-vault sync mechanisms on the same folder. Git underneath a synced drive is the one allowed pairing (git is history, the drive is transport).
4. Write the chosen method, rationale, and setup checklist into `_system/connectors.md` (transport/sync section). If a recurring git-commit cadence is wanted, note it as an OPTIONAL cron upgrade · do not require it.

**Phase B · SEAT (add a person).**
1. Confirm the four facts: name, role, full-time vs contractor, clients/projects touched. For contractors, confirm each client on the list explicitly · never infer.
2. Create `Team/{slug}/` with three files (kebab-case slug):
   - `profile.md` · role, strengths, working style, contact norms.
   - `access.md` · clients/projects + role (owner | member | contractor).
   - `tasks.md` · empty task list, universal frontmatter.
   All three carry universal frontmatter (`type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated`).
3. Append a row for the person to `_system/permissions.md` (person, role, clients/projects, storage-ACL status, sync-access status).
4. On Team/Agency, pair AI-scoping with storage-layer ACLs: set the matching shared-drive / repo permission so the person can only reach their folders at the storage layer too, and turn on who-read/who-wrote logging to `_system/audit/`.
5. Add the person to the relevant `Projects/{slug}/` (and Agency `Clients/{slug}/`) `team:` arrays.
6. Regenerate their AI scope (Phase C) and hand them the onboarding checklist.

**Phase C · SCOPE (regenerate what the AI loads).**
1. For the named person (or all people), read their `Team/{slug}/access.md`.
2. Generate the machine-local AI load-scope from the `clients`/`projects` list (an ignore/allow set telling the operator which folders to load for that seat).
3. State the honest limit every time: scoping controls what the AI loads, not what a human can open in the files. Hard confidentiality needs a storage-layer partition (separate repo/drive permission per the Phase B ACL), not scoping alone. Never describe scoping as encryption or as hard access control.

**Phase D · OFFBOARD (remove a person cleanly).**
1. Reassign open tasks from their `Team/{slug}/tasks.md` · ask who inherits each.
2. If they owned any client/project, ask for the new `owner:` and reassign.
3. Remove them from every `team:` array (Projects, Agency Clients) and delete their row from `_system/permissions.md`.
4. Archive `Team/{slug}/` to `_system/state/archive/team-{slug}/` and log the offboarding as a decision in `Memory/decisions/`.
5. Remind the operator (do not do it autonomously): revoke sync access (remove the collaborator / member or rotate the encrypted-sync credential per their method) and revoke any client-tool access noted in stack files.

**Phase E · AUDIT (access vs reality).**
1. Build a table: person × clients/projects from each `Team/{slug}/access.md` and `_system/permissions.md`, versus the actual `team:` arrays across `Projects/` (and Agency `Clients/`).
2. Flag every mismatch as a finding (over-access, orphaned access, missing ACL, scoping-without-storage-partition).
3. Recommend running this quarterly; record the run as a decision in `Memory/decisions/`.

## Outputs

- `_system/connectors.md` · chosen sync method, rationale, setup checklist (SYNC).
- `Team/{slug}/profile.md`, `Team/{slug}/access.md`, `Team/{slug}/tasks.md` · new seat (SEAT).
- `_system/permissions.md` · one appended/edited row per person (SEAT, OFFBOARD).
- `_system/audit/` · who-read/who-wrote logging enabled and entries (SEAT, ongoing).
- Updated `team:` arrays in `Projects/{slug}/` and Agency `Clients/{slug}/` (SEAT, OFFBOARD).
- Machine-local AI load-scope per person (SCOPE).
- `_system/state/archive/team-{slug}/` · archived seat (OFFBOARD).
- Decision files in `Memory/decisions/` for offboarding and audit runs, each with `source` + `confidence`.
- No KPI-ledger rows are appended by this module.

## Guardrails

- **Approval gates:** never autonomously edit permissions, contact a teammate, send any external message, delete files, or revoke tool/sync access. Permission and offboarding changes are drafted and escalated to the contact in `_system/config.md`; sync/tool revocation is a reminder to a human, not an action.
- **Firewall (Agency):** never read across sibling `Clients/{slug}/` folders; every client file stays `confidential:true`. An ambiguous person-to-client mapping goes to `Inbox/` · never guess.
- **Honest framing:** AI context-scoping is never marketed as encryption or hard access control. Real confidentiality requires the storage-layer partition; always pair scoping with an ACL and say so.
- **Append-only & canonical homes:** `_system/audit/` is append-only; route each fact to its one canonical file (one concept per file). kebab-case slugs, ISO dates, universal frontmatter on every `.md`.
- **Budgets:** respect operator reads/writes/housekeeping caps in `_system/config.md`; stop cleanly when a cap is hit.

## References

- `references/sync-options.md` · sync decision tree and per-method setup steps.
- `references/seats.md` · `access.md` template and machine-local AI load-scope generation.
- `references/checklists.md` · seat onboarding and offboarding checklists.
- `references/confidentiality.md` · the storage-layer hard-partition pattern that scoping alone cannot provide.
