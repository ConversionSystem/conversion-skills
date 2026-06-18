# The Instruction Layer — how routing works

Conversion OS uses a **router pattern** so the AI always knows where to read and where to write.

## Root `CLAUDE.md` (the brain, ≤150 lines)
Read in full at the start of every session. It holds:
- a **startup read-routine** (what to load, in order);
- a **routing map** — the canonical home for every kind of information;
- memory, writing, update, naming, source-of-truth, and conflict-resolution rules;
- size budgets, security/confidentiality rules, human-approval rules, voice rules, and anti-patterns.

## Folder `CLAUDE.md` (one per top folder, ≤60 lines)
A local router shaped **Purpose → Read → Write → Never → Hand-off**, so when a task touches a folder, the AI loads just that folder's rules.

## The compounding memory engine
`Memory/kpi-ledger.md` is **append-only**. Every workflow that moves a metric appends one row:

```
| date | metric | baseline | current | target | source | confidence | note |
```

`confidence ∈ {confirmed, reported, inferred, stale}`. Prior rows are never edited or reordered, so progress is cumulative and auditable. `/business-review` rolls the whole ledger up against a baseline snapshot to prove the trend.

## Conventions
- Universal frontmatter on every file (`type, status, owner, date, reviewed, tags, confidential, source, generated`).
- kebab-case slugs, ISO dates, one concept per file.
- Generated rollups carry `generated: true` and are never hand-edited.
- The **Optimizer** keeps all of this honest: dead links, stale context, budget overruns, frontmatter errors, and firewall breaches each come with a concrete fix.
