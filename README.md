# Conversion OS

**An AI-powered operating system that gives Claude a permanent, governed memory of your business — and a daily autonomous operator that keeps it current.**

Conversion OS is markdown-first and owned by you. No required database, no platform lock-in: your business is a folder of plain `.md` files, versioned with git, that the AI reads from and writes back to. The AI is the runtime, the files are the database, git is the journal. You can run the whole thing on **zero infra** — just Claude + a synced folder.

## One architecture, three profiles
- **Solo** — a founder/operator. Adds `Pipeline/` for sales context.
- **Team** — adds `Team/` (people, roles, permissions) and storage-layer access control.
- **Agency** — adds firewalled `Clients/{slug}/` workspaces for client delivery.

## The 8 modules
1. **Conversion OS Setup** — guided wizard; 10-minute first win, then deepen.
2. **Conversion Memory** — persistent business memory + the append-only KPI ledger.
3. **Conversion Operator** — daily autonomous operator (meetings, Slack, email, CRM, calendar).
4. **Conversion Optimizer** — audit & hygiene (dedupe, dead links, stale/conflicting context).
5. **Conversion Team OS** — shared knowledge, role-based permissions, departments.
6. **Conversion Client OS** — firewalled per-client workspaces for agencies.
7. **Conversion MCP / Connector Layer** — read/write the OS across tools and agents.
8. **Conversion Workflow Library** — reusable prompts, SOPs, automations, routines.

## The moat: compounding memory
`Memory/kpi-ledger.md` is append-only. Every workflow appends a provenance-stamped, confidence-rated row — nothing is erased, so progress is cumulative and auditable. Monthly reviews roll the whole ledger up against a baseline to prove the OS is making the business measurably better.

## Quickstart (zero infra)
1. Point Claude at an empty folder.
2. Run **Conversion OS Setup** (`/setup`). Pick a profile, paste your website + drop a few docs.
3. In ~10 minutes you get a populated, governed vault, a seeded ledger, and your first deliverable.

## Repo layout
```
skills/      the 8 modules + the Workflow Library (Claude skills)
templates/   document skeletons Setup copies into a new vault
examples/    seeded demo vaults (solo / team / agency)
scripts/     clean-room lint, size-budget check, secret scan (CI gates)
_system/     default rules/connectors/permissions shipped with the OS
docs/        guides
```

See `NOTICE` for attribution. This is an original, clean-room work by Conversion System.
