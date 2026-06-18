---
name: fact-checker
description: Verify claims against sources and assign a verdict, evidence, and confidence to each, used when you say "fact-check this", "verify these claims", or "check the sources"
---

# Fact Checker

Take a set of claims, test each one against its sources, and record the verdict, the evidence, and a confidence level. No claim gets a verdict without a cited source.

## When to use
- A draft, report, or proposal makes factual or numeric assertions that need checking before it goes out.
- You receive claims from a third party (a vendor, a prospect, a competitor page) and want to know which ones hold up.
- A document under review cites metrics, dates, or statements you want traced back to a source.
- Before anything outbound or published, to catch invented numbers or unsupported claims.

## Inputs
- The claims to check: a list, or a document whose assertions you extract first.
- Sources: links, files in the vault, pasted text, or `_system/connectors.md` tools the user has enabled.
- Optional: the path to the doc under review, if you want results appended there instead of a new file.
- `Company/` and `Memory/` for context on what the business already treats as established fact.

## Process
1. Gather the claims. If given a document, read it and pull each distinct factual or numeric assertion into a numbered list. If given a list, use it as is.
2. For each claim, identify candidate sources. Prefer sources the user supplied. Fall back to files under `Company/`, `Memory/kpi-ledger.md`, and `Memory/decisions/`. Use enabled connectors from `_system/connectors.md` only when the user has turned them on.
3. Read each candidate source and locate the exact passage, number, or statement that bears on the claim. Quote it.
4. Assign a verdict from this fixed set: Supported, Partly supported, Unsupported, Contradicted, Unverifiable (no source found).
5. Assign a confidence from this fixed set: High, Medium, Low. Base it on how directly the source speaks to the claim and how reliable the source is.
6. If no source supports a claim, mark it Unverifiable and say so plainly. Never assert a verdict without a citation.
7. Note any claim where sources disagree, and record both sides with their citations.
8. Write the result. By default create a new file at `Projects/{slug}/data/fact-check-{date}.md`. If the user points to a doc under review, append a "Fact check" section to that file instead.
9. If the check confirms or corrects a metric tracked in the KPI ledger, append a new row to `Memory/kpi-ledger.md` (never edit a prior row).

## Outputs
- `Projects/{slug}/data/fact-check-{date}.md`: a table with columns | claim | verdict | confidence | source | evidence quote | note |, one row per claim, plus a one-line summary count by verdict.
- Or, when appending, a "Fact check" section added to the doc under review at its existing path, same table.
- Optional appended row in `Memory/kpi-ledger.md` when a tracked metric is confirmed or corrected, using the exact ledger columns.

## Guardrails
- PROVENANCE: every verdict carries a citation. No source means the verdict is Unverifiable, never a guess.
- Never invent a metric, date, or quote. If a source does not say it, the claim is not supported.
- Quote the evidence so the reader can check it without reopening the source.
- DRAFT-ONLY: the fact-check file is a draft for the user to review, not an outbound artifact.
- FIREWALL: when checking client material, read only the active client's folder under `Clients/{slug}/`.
- Record source disagreement rather than picking a winner silently.
- Append to the ledger, never edit prior rows.

## References
- `Memory/kpi-ledger.md` for tracked metrics and their existing sources.
- `_system/connectors.md` for any enabled external lookup tools.
- `Library/styles/brand-voice.md` for the voice of any written summary.
