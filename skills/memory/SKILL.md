---
name: memory
description: Persistent business memory operations · append KPI ledger rows, record decisions, capture lessons, define glossary terms, and retrieve what we know about a metric or what moved; invoke when logging results or asking what do we know about X.
---

# Conversion Memory

The persistent, compounding memory layer of the vault and the read/write operations on it.

## When to use
- A workflow (or the user) reports a metric that moved and needs it logged to the KPI ledger.
- A choice was made that future work must respect · record it as a decision.
- A durable, reusable insight emerged · capture it as a lesson.
- A term needs a canonical, shared definition · define it in the glossary.
- Before stating any metric or fact, retrieve its latest known value.
- Two facts disagree and the conflict must be resolved and logged.
- The user asks "what do we know about X", "what moved", "did we already decide this", or "what's our latest number for Y".

## Inputs
- Metric name, baseline, current, target, source, confidence ({confirmed, reported, inferred, stale}), note · for ledger appends.
- Decision context, the decision itself, rationale, confidence · for decision records.
- A lesson statement and its trigger/context · for lessons.
- A term and its definition · for glossary.
- A query string (metric, topic, or "what moved") · for retrieval.
- Two or more conflicting facts with their dates/confidence · for conflict resolution.

## Process
1. **Classify the request** as one of: append-metric, record-decision, capture-lesson, define-term, retrieve, or resolve-conflict. If ambiguous, ask once; if still unclear, file a note to `Inbox/` and stop.
2. **APPEND a KPI row** (`Memory/kpi-ledger.md`): Read the file. Confirm the header columns are exactly `| date | metric | baseline | current | target | source | confidence | note |`. Require `source` and `confidence` to be present; reject if `confidence` is not in {confirmed, reported, inferred, stale}. Append one new row to the bottom with today's ISO date. NEVER edit, reorder, or delete any prior row. If the metric is new, set baseline = current.
3. **RECORD a decision** (`Memory/decisions/YYYY-MM-DD-{slug}.md`): First scan `Memory/decisions/` for prior or contradicting decisions on the same subject. If found, link them and note whether this supersedes or conflicts. Write a new file with universal frontmatter (`source` + `confidence` REQUIRED) and sections: Context, Decision, Rationale, Confidence, Supersedes/Related. Use a kebab-case slug.
4. **CAPTURE a lesson** (`Memory/lessons.md`): Append a dated bullet · what happened, the lesson, and where it applies. Never rewrite earlier lessons.
5. **DEFINE a term** (`Memory/glossary.md`): If the term exists, surface the existing definition and ask before overwriting; otherwise append the term and definition in alphabetical position.
6. **RETRIEVE**: For a metric, scan `Memory/kpi-ledger.md` from the bottom up and return the latest row for that metric. When multiple sources exist, prefer the row with higher confidence and a named `source`. For decisions/lessons/terms, read the relevant file and return the canonical entry with its date and confidence.
7. **RESOLVE a conflict**: When two facts disagree, the one with the newer `reviewed`/`date` and higher `confidence` wins. Record the contradiction as a dated entry in `Memory/lessons.md` and flag it for the Optimizer to review. Do not silently delete the losing fact.
8. **Stay within budget**: respect read/write caps in `_system/config.md` and stop cleanly when a cap is hit.

## Outputs
- Appended row(s) in `Memory/kpi-ledger.md` (append-only).
- New decision file at `Memory/decisions/YYYY-MM-DD-{slug}.md` with required `source` + `confidence`.
- Appended lesson bullet(s) in `Memory/lessons.md`, including any logged contradiction.
- New or surfaced term in `Memory/glossary.md`.
- For retrieval: the latest ledger row or canonical entry returned inline (no file written).

## Guardrails
- KPI ledger is APPEND-ONLY: never edit, reorder, or delete prior rows; exact column order enforced; `source` + `confidence` required on every row.
- `source` + `confidence` REQUIRED on every decision file; universal frontmatter on all new `.md` files (type, status, owner, date, reviewed, tags (>=2), confidential, source, generated).
- Route every fact to its canonical home; one concept per file; kebab-case slugs; ISO dates.
- Ambiguous entity or subject → file to `Inbox/`, never guess.
- Conflicts are logged, not hidden · newer + higher-confidence wins, loser retained, Optimizer flagged.
- No external sends, deletes, or pricing/permission changes; this skill only reads and appends within `Memory/`.
- Honor operator budgets in `_system/config.md`; stop cleanly at caps.

## References
none
