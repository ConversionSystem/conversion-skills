# The Instruction Layer

Conversion OS uses a router pattern, so the AI always knows where to read and where to write.

## Root `CLAUDE.md`, the brain (150 lines or fewer)
Read in full at the start of every session. It holds:
- a startup read-routine (what to load, in order),
- a routing map (the one home for every kind of information),
- memory, writing, update, naming, source-of-truth, and conflict rules,
- size budgets, security and confidentiality rules, human-approval rules, voice rules, anti-patterns.

## Folder `CLAUDE.md`, one per top folder (60 lines or fewer)
A local router shaped Purpose, Read, Write, Never, Hand-off. When a task touches a folder, the AI loads that folder's rules and nothing else.

## The compounding ledger
`Memory/kpi-ledger.md` is append-only. Every run that moves a metric adds one row:

`date | metric | baseline | current | target | source | confidence | note`

`confidence` is one of confirmed, reported, inferred, stale. Prior rows are never edited or reordered, so progress is cumulative and auditable. `/business-review` rolls the whole ledger against a baseline and shows the trend.

## Conventions
- Universal frontmatter on every file: type, status, owner, date, reviewed, tags, confidential, source, generated.
- kebab-case slugs, ISO dates, one concept per file.
- Generated rollups carry `generated: true` and are never hand-edited.
- The Optimizer keeps this honest. Dead links, stale context, budget overruns, frontmatter errors, and firewall breaches each come with a fix.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
