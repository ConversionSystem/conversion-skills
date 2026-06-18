# Setup Guide

One architecture, three profiles. The taxonomy, the router pattern, and the KPI ledger never change. The profile decides which folders turn on.

## Solo
One operator. Turns on `Pipeline/` (accounts, prospects, deals). No `Team/`, no `Clients/`. See `examples/solo-vault/`.

## Team
A multi-person company. Adds `Team/{person}/` (profile, access, tasks) and `Company/departments/`, plus `_system/permissions.md`. AI scoping is paired with storage-layer access control. See `examples/team-vault/`.

## Agency
Serving clients. Adds firewalled `Clients/{slug}/` workspaces (every file `confidential: true`) on top of the Team features. The firewall is enforced by `scripts/check-firewall.sh`. See `examples/agency-vault/`.

## What Setup writes
- Root `CLAUDE.md` router (60 lines or fewer at the folder level, 150 or fewer at the root).
- `_system/`: config (budgets, escalation contact, signature), rules, connectors, permissions.
- `Company/`: your identity (profile, brand, offers, icp, strategy, stack).
- `Memory/kpi-ledger.md`: seeded with your first baselines, each with `source` and `confidence`.
- Today's `Daily/` note, the templates this profile needs, and a first deliverable.

## Upgrading
Profiles share one structure, so Solo to Team to Agency is additive. New folders get created. Nothing is rebuilt.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
