# Conversion Skills

**CONVERSION / SKILLS** · by Conversion System. Our toolkit: 99 Claude skills that run your growth and remember what moved. It powers Conversion OS, or runs on its own.

Every business runs on context. Who you are, what you sell, who you serve, what you decided, what moved the number. Most of it evaporates. Conversion Skills keeps it. Plain markdown in your own folder, versioned with git. The AI is the runtime. The files are the database. Git is the journal. No platform. No lock-in.

## Three profiles, one architecture
- **Solo.** One operator. Adds `Pipeline/` for deals.
- **Team.** People, roles, real permissions, an audit trail.
- **Agency.** Firewalled `Clients/{slug}/` workspaces. One client per task. No cross-client reads, proven by `scripts/check-firewall.sh`.

## The 8 modules
1. **Setup.** Empty folder to a governed vault in 10 minutes.
2. **Memory.** Persistent business memory and the append-only KPI ledger.
3. **Operator.** A daily run that pulls meetings, chat, email, CRM, and calendar, on a budget, drafts only.
4. **Optimizer.** Audits the vault and ships a fix per finding.
5. **Team OS.** Shared knowledge, role scoping, permissions.
6. **Client OS.** Firewalled per-client delivery for agencies.
7. **Connector layer.** Read and write the OS across tools, within scope, logged.
8. **Workflow Library.** 9 operating routines and 83 delivery skills across ads, SEO, sales, content, YouTube, creative, and design, all logging what moved.

## The ledger is the moat
`Memory/kpi-ledger.md` is append-only. Every run adds one row: date, metric, baseline, current, target, source, confidence, note. Nothing is erased. The monthly review rolls the whole ledger against a baseline and shows the trend. Cancelling loses the record. That is the point.

## Quickstart, zero infra
1. Point Claude at an empty folder.
2. Run `/setup`. Pick a profile. Paste your site, drop a few docs.
3. Ten minutes later: a populated vault, a seeded ledger, a first deliverable.

## Guides
Start with `docs/`.
- [docs/getting-started.md](docs/getting-started.md) · what you need, how to install, your first 10 minutes.
- [docs/commands.md](docs/commands.md) · all 99 commands, what each does, what it needs.
- [docs/daily-use.md](docs/daily-use.md) · the operating rhythm, with worked examples.
- [docs/setup-guide.md](docs/setup-guide.md) · the three profiles.
- [docs/connectors.md](docs/connectors.md) · connect tools and run the operator. Optional.
- [docs/confidentiality.md](docs/confidentiality.md) · ownership, the firewall, permissions, secrets.
- [docs/instruction-layer.md](docs/instruction-layer.md) · how routing and the ledger work.
- [docs/pricing.md](docs/pricing.md) · the five tiers. Fixed, named, refundable.
- [docs/README.md](docs/README.md) · the full index.

## Repo
```
skills/      99 skills (7 modules, 9 workflows, 83 delivery)
templates/   21 document templates Setup copies in
examples/    3 seeded vaults: solo, team, agency
scripts/     5 gates: clean-room, budgets, secrets, firewall, brand
assets/      brand-tokens.css
site/        the landing page, self-contained HTML
docs/        getting-started, commands, daily-use, setup, connectors, and more
BRAND.md     the Conversion System brand, enforced by scripts/check-brand.sh
```

## Receipts
99 skills. 5 gates green on every push. 0 em-dashes. 0 cross-client leaks (a planted leak was caught and removed in test V4).

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
