---
name: seo-competitor-pages
description: Find and dissect the pages that rank for your target queries and write a beat-each-one plan, triggers include "competitor pages", "who outranks me", "SERP analysis", "how to beat the top result"
---
# SEO Competitor Pages

Pull the pages ranking for your target queries, score their intent coverage, depth, and structure, then write a concrete plan to beat each one. Cite every source. Draft only.

## When to use
- You picked target queries (from `/seo-plan` or a keyword list) and need to know who you are up against.
- A page stalled on page two and you want to see what the top results do differently.
- Before drafting a new page, so the brief reflects what already ranks instead of a guess.

## Inputs
- 1 to 10 target queries. Pull from `Projects/{slug}/brief.md`, a `/seo-plan` output, or ask the user.
- The SERP results for each query. Default: a pasted or exported results list (top 10 URLs per query) from a manual search or a search-data export. Optional connector: a SERP or rank-tracking tool registered in `_system/connectors.md`.
- Page content for the ranking URLs. Default: pasted page text or a saved export. Optional connector: a crawler registered in `_system/connectors.md`.
- Your own page for the query, if one exists, so the gap is measured against you.
- `Company/profile.md`, `Company/icp.md`, and `Company/offers.md` for relevance scoring.
- Voice from `Library/styles/brand-voice.md` (agency: the active client's).

## Process
1. Resolve target queries and confirm search intent for each: informational, commercial, transactional, or navigational. Note the dominant intent the SERP rewards (the format most of the top results share).
2. For each query, record the ranking URLs in order. If a connector is registered, pull them; otherwise use the provided export or the described manual search. Capture URL, title, and rank. Never invent rankings.
3. For each ranking page, gather the content (connector crawl, export, or pasted text). Capture word count, heading outline (H1 to H3), media count, schema present, internal and external link counts, last-updated date if shown, and the entities or subtopics covered.
4. Score each page 1 to 5 on four axes: intent match (does it answer the searcher's actual job), depth (coverage of subtopics versus the SERP set), structure (skimmable headings, tables, jump links, answer-first), and trust signals (author, dates, citations, original data). Record the source for every data point.
5. Build the subtopic matrix: list every subtopic any top page covers down the rows, queries across the columns, mark who covers what. The gaps the leaders all miss are your wedge.
6. For each competitor page, write a beat-this line: the one thing they lack (a missing subtopic, weak structure, stale data, thin proof) and the concrete move to outrank it.
7. Synthesize a page spec to beat the set: the intent to serve, the heading outline, the must-cover subtopics, the proof and original data to add, internal links to place, and word-count range anchored to the SERP, not padded.
8. Solo/Team: write outputs under `Projects/{slug}/`. Agency: write under `Clients/{slug}/Projects/{slug}/` for the active client only, never read a sibling, mark client outputs `confidential:true`.
9. If a tracked metric moves (for example a target page's rank for a query), append one row to `Memory/kpi-ledger.md`. Never edit prior rows.

## Outputs
- `Projects/{slug}/data/competitor-pages.md` (agency: `Clients/{slug}/Projects/{slug}/data/competitor-pages.md`): per-query ranking table, per-page scorecards, and the source for every figure.
- `Projects/{slug}/data/subtopic-matrix.md` (agency path mirrors above): subtopics by query with coverage marks and the identified gaps.
- `Projects/{slug}/final/beat-plan.md` (agency path mirrors above): the beat-this line per competitor plus the page spec to outrank the set.
- A new row in `Memory/kpi-ledger.md` only when a tracked metric moves, exact columns `| date | metric | baseline | current | target | source | confidence | note |`.

## Guardrails
- DRAFT-ONLY. Produce files for review. Never publish a page, change a sitemap, or contact a competitor or client.
- PROVENANCE. Cite the URL and method (connector, export, or manual search) for every ranking and figure. Never invent a rank, a word count, or a metric. Mark unverifiable claims as `inferred`.
- VOICE from `Library/styles/brand-voice.md` (agency: the client's).
- FIREWALL (agency). Operate on the active client only, never read a sibling client, set `confidential:true` on client outputs.
- CONNECTORS are optional. Default to a provided export or a described manual search. Register any SERP tool or crawler in `_system/connectors.md`. Keep credentials out of the vault.
- Respect target sites: read public pages only, no scraping behind logins or paywalls, honor rate limits described by the connector.

## References
- `Company/profile.md`, `Company/icp.md`, `Company/offers.md` for relevance scoring.
- `_system/connectors.md` for any SERP or crawler setup.
- `/seo-plan` for target queries, `/seo-content` and `/seo-page` for turning the beat plan into a draft.
