# Glossary

Canonical terms for Conversion Skills. Skills reference these, they do not redefine them.

- **Vault** · the user's folder of markdown that Claude treats as memory. Conversion Skills builds it; the user owns it.
- **Profile** · Solo, Team, or Agency. One architecture, three shapes.
- **Ledger** · `Memory/kpi-ledger.md`, append-only. One row per metric moved: date, metric, baseline, current, target, source, confidence, note.
- **Receipt** · a proof block: a number, a verb-context, a named source with a date range. Names or it did not happen.
- **Firewall** · the agency rule, read and write only the active `Clients/{slug}/`, never a sibling. Enforced by `scripts/check-firewall.sh`.
- **Draft-only** · Conversion Skills never sends, publishes, deletes, or contacts a client on its own. Outbound is `status: draft` and escalated to the contact in `_system/config.md`.
- **Confidence** · on a ledger row or a finding: confirmed, reported, inferred, or stale.
- **Router** · the `CLAUDE.md` at the vault root and in each folder. The map.
- **Operator** · the daily run that reads the vault, pulls connectors within budget, and synthesizes the day.
- **Gate** · a CI check that fails the build: clean-room, budgets, secrets, firewall, brand, sections.
- **Judge** · the reusable adversarial reviewer that tries to refute a claim before it ships.
- **Fan-out** · an orchestrated skill that spawns specialists, merges their findings, and runs the judge.
- **Progressive disclosure** · keep a `SKILL.md` short and push depth into references files loaded on demand.
- **Information hierarchy** · the order of detail, in-skill step versus in-skill reference versus external reference.
- **Completion criterion** · the observable condition that says a skill's job is done.
- **Premature completion** · stopping before the completion criterion is met.
- **Model-invoked versus user-invoked** · a skill Claude triggers on a matching task versus one a person types.
- **Discipline sections** · Red flags, Verification, Rationalizations, required on heavy skills.
- **Heavy skill** · a high-stakes skill the sections gate enforces.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
