# Setup Guide — profiles & what gets built

Conversion OS is **one architecture with three deployment profiles**. The taxonomy, router pattern, and KPI ledger never change; the profile decides which folders activate.

## Solo
For a founder/operator. Activates `Pipeline/` (accounts, prospects, deals). No `Team/` or `Clients/`.
See `examples/solo-vault/`.

## Team
For a multi-person company. Adds `Team/{person}/` (profile + access + tasks) and `Company/departments/`, plus `_system/permissions.md`. AI-scoping is paired with storage-layer access control.
See `examples/team-vault/`.

## Agency
For consultants/agencies serving clients. Adds firewalled `Clients/{slug}/` workspaces (every file `confidential: true`) on top of the Team features. The firewall is enforced by `scripts/check-firewall.sh`.
See `examples/agency-vault/`.

## What Setup writes
- Root `CLAUDE.md` router (≤150 lines) + a router in every top folder (≤60).
- `_system/` — config (budgets, escalation contact, signature), rules, connectors, permissions.
- `Company/` — your identity (profile, brand, offers, icp, strategy, stack).
- `Memory/kpi-ledger.md` — seeded with your first baselines (each with `source` + `confidence`).
- Today's `Daily/` note, the templates this profile needs, and a first deliverable.

## Upgrading later
Profiles share one structure, so Solo → Team → Agency is additive: new folders are created, nothing is rebuilt.
