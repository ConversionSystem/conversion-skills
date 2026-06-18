---
name: connect
description: Connector layer that registers external tools, ingests inbound data into canonical homes, serves the vault to external agents within scope, audits every external read and write, and degrades gracefully when a connector is down · invoke for connect a tool, register a connector, ingest meetings or chat or email or CRM or calendar, serve the vault, token scope, MCP bus, connector offline, or audit external access.
---
# Conversion MCP / Connector Layer
Our own clean-room I/O bus that lets AI tools and agents read and write the OS across tools, workflows, and autonomous routines.

## When to use
- A new external tool or data source needs to be wired into the OS (CRM, calendar, chat, email, meeting recorder, ad platform, web service).
- External data needs ingesting and normalizing into the vault's canonical homes with provenance.
- An outside agent or workflow needs scoped read/write access to the vault.
- You need to confirm who or what touched the vault, and when, from outside.
- A connector is unreachable and the affected work must proceed on file data without silently going stale.

## Inputs
- Connector identity: name, purpose, the external system, and how it authenticates (the credential location, never the credential itself).
- Scope intent: which vault paths the connector may read and/or write, and at what cadence (manual, scheduled, served).
- For inbound: the raw export, paste, or live payload (transcript, message log, email thread, CRM record, calendar event).
- For outbound: the requesting agent's identity, the permission scope it claims, and the token reference.
- ToS and rate-limit notes for the external system.
- `_system/config.md` (operator budgets, escalation contact), `_system/permissions.md` (access scopes), `_system/connectors.md` (registry).

## Process
Phase 1 · REGISTER a connector
1. Read `_system/connectors.md`. If a row for this connector exists, update its `status`; otherwise append a new row. Keep one row per connector.
2. Connector table columns: `| connector | purpose | scope | tos/rate | status |`. `status` in {active, paused, draft, unavailable, revoked}. `scope` references concrete vault paths (e.g. `Pipeline/accounts/`, `Daily/`).
3. NEVER write credentials, tokens, API keys, or secrets into the vault. Record only a pointer to where the secret lives in the external secret manager (e.g. `secret-ref: kms/connectors/{name}`). If a secret value is ever supplied inline, refuse to persist it and escalate to the contact in `_system/config.md`.
4. Cross-check `_system/permissions.md`: the connector's declared scope must be representable as a permission entry. If it grants write or external-send rights, mark the registration `status:draft` and escalate for human approval before activating.
5. Record ToS and rate-limit terms in the `tos/rate` cell so later phases can respect them.

Phase 2 · INBOUND ingest
1. Identify the canonical home for each fact via the root router map. Meetings -> `Operations/meetings/`; tasks -> `Operations/tasks.md` or the relevant `Team/{person}/tasks.md`; CRM accounts/prospects -> `Pipeline/accounts/`, `Pipeline/prospects/`, deals -> `Pipeline/deals.md`; calendar/day notes -> `Daily/YYYY-MM-DD.md`; metrics -> `Memory/kpi-ledger.md`; decisions -> `Memory/decisions/`. One concept per file, kebab-case slugs, ISO dates.
2. Normalize the payload to the universal frontmatter on every written file: `type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated`. Set `source` to `connector:{name}` and `generated:true`.
3. For any KPI row, append (never edit) to `Memory/kpi-ledger.md` with exact columns `| date | metric | baseline | current | target | source | confidence | note |`; set `confidence` in {confirmed, reported, inferred, stale} based on payload reliability.
4. Agency firewall: if the entity belongs to a client, write only inside that `Clients/{slug}/` with `confidential:true`; never read a sibling client folder. If the owning entity is ambiguous, write to `Inbox/` and stop · never guess.
5. Outbound-looking artifacts pulled in (draft replies, emails, DMs) are stored `status:draft` only; the connector never sends.
6. Log the read in Phase 4.

Phase 3 · OUTBOUND serve
1. Resolve the requesting agent against `_system/permissions.md`. Serve only paths inside its granted scope; deny anything outside and log the denial.
2. Token scoping: each served session is bound to a token reference (held in the secret manager) carrying a read-only or read/write grant and a path prefix. A read-only token can never trigger a write path.
3. Writes from external agents follow the same canonical-home routing, universal frontmatter, append-only ledger, and firewall rules as Phase 2.
4. Hard gates still apply: an external agent may NOT autonomously send messages/email/DM, delete files, publish, change pricing/offers, edit permissions, or contact clients. Such requests are converted to `status:draft` outputs and escalated to the contact in `_system/config.md`.
5. Respect the connector's recorded rate limits and the operator budgets in `_system/config.md` (reads/writes/transcripts/emails/dms/housekeeping). Stop cleanly when a cap is hit.
6. Log every served read and write in Phase 4.

Phase 4 · AUDIT
1. Append one line per external read or write to a dated log in `_system/audit/` (e.g. `_system/audit/YYYY-MM-DD.md`), never editing prior lines.
2. Each entry records: timestamp (ISO) · actor (human vs agent, with id) · connector · operation (read/write/deny) · path(s) touched · scope/token ref · result. Human and agent access must be distinguishable.
3. Secrets, token values, and confidential payload bodies are never written to the audit log · reference paths and ids only.

Phase 5 · DEGRADE gracefully
1. If a connector is unreachable, do not block. Mark the affected section or file `source:unavailable(connector:{name})` and proceed on existing file data.
2. Set the connector's `status` to `unavailable` in `_system/connectors.md`.
3. Log the outage and the degraded read in `_system/audit/`. On recovery, re-ingest, restore `source` provenance, and set `status` back to `active`.

Setup ladder (zero-infra first, upgrades optional)
- Level 0 (default, no infra): manual paste/import. Operator pastes an export; this skill normalizes and routes it. Connector row `status:active`, `scope` documented, no secrets stored.
- Level 1 (scheduled): an external scheduler/cron pulls on a cadence into `Inbox/` for routing. Optional upgrade.
- Level 2 (served): a long-running endpoint exposes the vault to external agents under token scope. Optional upgrade; requires the permission entries and audit logging above.

## Outputs
- Registry row appended/updated in `_system/connectors.md` (`| connector | purpose | scope | tos/rate | status |`).
- Permission entries reconciled in `_system/permissions.md` (write/send scopes left `status:draft` pending approval).
- Inbound facts written to canonical homes per the router map (`Operations/meetings/`, `Pipeline/accounts/`, `Pipeline/prospects/`, `Pipeline/deals.md`, `Daily/YYYY-MM-DD.md`, `Memory/decisions/`, `Clients/{slug}/`, or `Inbox/` when ambiguous), each carrying universal frontmatter with `source:connector:{name}` and `generated:true`.
- KPI rows appended to `Memory/kpi-ledger.md` with `source` and `confidence` set (append-only).
- Audit lines appended to `_system/audit/YYYY-MM-DD.md` (one per external read/write/deny).
- Degraded sections marked `source:unavailable(connector:{name})` with connector `status:unavailable`.
- Draft-only artifacts for any outbound-looking content (`status:draft`), with an escalation note to the contact in `_system/config.md`.

## Guardrails
- Approval gates: never autonomously send external messages/email/DM, delete files, publish content, change pricing/offers, edit permissions, or contact clients · for both this skill and any external agent it serves. Outbound is drafted `status:draft` and escalated to `_system/config.md`.
- Secrets: NEVER store credentials, tokens, or API keys in the vault; keep them in the secret manager and reference only. Refuse and escalate if a secret is supplied inline. Audit logs reference ids, never secret values.
- Firewall (agency): never read a sibling `Clients/{slug}/`; every client file `confidential:true`; ambiguous entity routes to `Inbox/`, never guessed.
- Append-only: `Memory/kpi-ledger.md` and `_system/audit/` are append-only · never edit, reorder, or delete prior rows/lines.
- Frontmatter: every written `.md` carries the universal frontmatter; `source` + `confidence` required on KPI rows and decision files.
- Routing: facts go to canonical homes (root router map), one concept per file, kebab-case slugs, ISO dates.
- Budgets + ToS: respect per-connector rate limits and the operator budgets in `_system/config.md`; stop cleanly at any cap.
- Token scoping: external access is bound to a scoped token; read-only tokens can never reach a write path; deny and log anything outside scope.

## References
- `_system/connectors.md` (connector registry)
- `_system/permissions.md` (access scopes for outbound serve)
- `_system/config.md` (operator budgets, escalation contact)
- `_system/audit/` (read/write logs)
- Root `CLAUDE.md` (router map for canonical homes)
