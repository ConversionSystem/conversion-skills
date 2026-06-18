---
name: deep-research
description: Run a multi-source research task, fan out, read sources, verify key claims, and write a cited report with per-claim confidence, for "deep research", "research this", "fact-check this topic", or "find sources on"
---

# Deep Research

Fan out across many sources, read them, verify the load-bearing claims, and write a cited report where every claim carries a confidence note. Cite everything, invent nothing.

## When to use
- You need a fact-checked, multi-source brief before a decision, a pitch, or a piece of content.
- A claim, number, or vendor assertion needs verification against independent sources.
- You are mapping a market, a competitor, or a topic and want sourced evidence, not vibes.
- Do not use for single-source lookups or for anything where you already hold the answer in the vault. Check Memory/ and Company/ first.

## Inputs
- The research question, refined to one sentence. If it is underspecified (no scope, no region, no timeframe), ask 2 or 3 narrowing questions first, then proceed with the tightened version.
- Optional: a deadline date, a depth target (number of sources), and any must-include or must-exclude sources.
- Optional connectors from `_system/connectors.md` if web fetch or search is wired up. None are required; you can run with manual source paste.

## Process
1. Read `_system/rules` and `Library/styles/brand-voice.md` so the report obeys voice and guardrails.
2. Scope. Restate the question in one sentence, then decompose it into 5 search angles that cover the question from different directions (definition, current state, counter-evidence, numbers, primary sources). Write the angles to `Projects/{slug}/brief.md`.
3. Search. Run one search pass per angle, 5 in total. Collect every result URL with its title and a one-line reason it matters. Save the raw list to `Projects/{slug}/data/search-results.md`.
4. Fetch. Deduplicate URLs, drop low-trust and duplicate domains, then fetch the top 15 sources. For each, extract the falsifiable claims (a claim you could prove wrong with evidence). Save extracted claims with their source URL and access date to `Projects/{slug}/data/claims.md`.
5. Verify. For each key claim, run a 3-vote adversarial check: try three times to refute it from independent sources. A claim is killed only when 2 of 3 votes refute it. Record the votes and the surviving verdict in `Projects/{slug}/data/verification.md`.
6. Synthesize. Merge claims that say the same thing, rank by confidence, and write the report to `Projects/{slug}/final/report.md`. Every claim gets an inline source citation and a confidence tag: high, medium, or low, with one line on why. Open with a 5-line summary, close with open questions and gaps.
7. If a finding changes a tracked number or a standing decision, append it: a row to `Memory/kpi-ledger.md` for a metric, or a note under `Memory/decisions/` for a decision. Never edit prior ledger rows.

## Outputs
- `Projects/{slug}/brief.md` · the question, the 5 angles, and scope.
- `Projects/{slug}/data/search-results.md` · raw result list with reasons.
- `Projects/{slug}/data/claims.md` · extracted claims with source and access date.
- `Projects/{slug}/data/verification.md` · 3-vote results per key claim.
- `Projects/{slug}/final/report.md` · the cited report, claims ranked by confidence, each tagged high, medium, or low.
- Optional: one appended row in `Memory/kpi-ledger.md` (columns: date, metric, baseline, current, target, source, confidence, note) and/or a note in `Memory/decisions/` when a finding moves a number or a decision.

## Guardrails
- PROVENANCE: cite every claim with its source URL and access date. Never invent a metric, a quote, or a statistic. If a claim cannot be sourced, mark it unverified and say so.
- Confidence is mandatory. Every claim in the report carries high, medium, or low with a one-line reason. Low-confidence claims are flagged, not hidden.
- Independence: the 3 verification votes must draw on independent sources. Three citations of the same press release count as one.
- DRAFT-ONLY: the report is a research draft for review, not an outbound or published asset. Anything published runs through the relevant publishing skill.
- FIREWALL: if the question concerns an active client, read and write only within that client's folder under `Clients/{slug}/`. No cross-client reads.
- Record the access date for every source. A claim with no date and no source does not enter the report.

## References
- `_system/rules` for voice and guardrail rules.
- `Library/styles/brand-voice.md` for voice.
- `_system/connectors.md` for optional search and fetch connectors.
- `Memory/kpi-ledger.md` for the append-only ledger format.
