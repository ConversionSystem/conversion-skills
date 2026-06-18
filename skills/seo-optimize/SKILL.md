---
name: seo-optimize
description: Optimizes a specific page for a target query by drafting an improved title, meta, headings, internal links, schema, and content-gap fixes when you say optimize this page for, improve SEO on, rank this page for, or on-page SEO
---

# SEO Optimize

Take one specific page and one target query, and produce an improved on-page draft plus an apply-it-yourself checklist, written to a canonical home as a draft for a human to apply.

## When to use
- You have a live (or drafted) page and a single target query you want it to rank for, and you want concrete on-page improvements.
- Triggers: "optimize this page for {query}", "improve SEO on {url}", "rank this page for {keyword}", "on-page SEO for {page}", "fix the title and meta on {page}".
- Use this for a single page against a single primary query. For a whole-site or multi-page audit, use the audit skill instead.

## Inputs
- Target page: a URL, or a path to an existing draft (e.g. a `Content/{slug}-{date}/final/` page or a `Projects/{slug}/final/` page).
- Target query: the primary keyword/phrase the page should rank for. Optionally 2-4 secondary queries.
- Current position (optional): known rank for the target query, and the target rank.
- Business context: `Company/icp.md` (intent and audience), `Company/brand.md` and `Library/styles/brand-voice.md` (voice). Agency: `Clients/{slug}/context/icp.md` and `Clients/{slug}/context/brand.md`.
- Optional: `_system/connectors.md` may register a paid rank-tracking or keyword tool as an OPTIONAL upgrade; default to fetched public pages and on-page reasoning.

## Process
1. Load context first. Read `Company/icp.md` for searcher intent and audience, then `Company/brand.md` + `Library/styles/brand-voice.md` for voice. Agency profile: read the ACTIVE client's `Clients/{slug}/context/icp.md` and `Clients/{slug}/context/brand.md` only; never read a sibling client.
2. Capture the page. Fetch the target URL (or read the draft file). Record the current title tag, meta description, H1, H2/H3 outline, word count, internal links present, and any existing schema. Note the page's apparent primary topic.
3. Define intent for the target query. Classify the query intent (informational, commercial, transactional, navigational) and the job the searcher is trying to do, grounded in `Company/icp.md`. State what a satisfying result must answer.
4. Diagnose the gap. Compare the page against the intent: where does the current title/meta/H1 fail to match the query, what subtopics or questions the intent implies are missing or thin, where the structure buries the answer.
5. Draft the on-page improvements in the business's (or client's) voice:
   - Title tag (<=60 chars, target query near the front, no clickbait).
   - Meta description (<=155 chars, includes the query and a reason to click).
   - H1 (single, query-aligned).
   - H2/H3 outline (reordered/expanded to cover intent; mark which are new).
   - Internal links: 3-8 specific suggestions with anchor text and the destination page, drawn from the vault's existing content where known.
   - Schema suggestion: recommend the appropriate type (e.g. Article, FAQPage, Product, HowTo, BreadcrumbList) and the key fields to populate. Suggest only; do not assert it is installed.
   - Content gaps vs intent: a prioritized list of subtopics, questions, and proof points to add, each tied to the searcher job.
6. Build the apply checklist. A human-runnable checklist of every change (old -> new for title/meta/H1, structural edits, links to add, schema to add) so a person can apply it without re-reading the analysis.
7. Cite sources. For any external fact, competitor observation, or claimed search behavior, cite the fetched source URL. Never invent metrics or positions.
8. Write outputs to the canonical home and append the ledger row (see Outputs). Everything is `status:draft`; a human applies the changes and a human publishes.

## Outputs
- On-page draft + checklist, `status:draft`, written to:
  - Solo/Team: `Content/{slug}-{date}/final/seo-optimize-{page-slug}.md` (use the existing content folder if the page lives in one; otherwise create `Content/{page-slug}-{date}/`). For a project page, use `Projects/{slug}/final/seo-optimize-{page-slug}.md`.
  - Agency: `Clients/{slug}/final/seo-optimize-{page-slug}.md` inside the ACTIVE client workspace, `confidential:true`.
  - Universal frontmatter on the file: `type: seo-optimization · status: draft · owner · date · reviewed · tags: [seo, on-page, ...] (>=2) · confidential · source: {target URL or file path} · generated: true`.
- File body sections: Target query & intent · Current page snapshot · Gap analysis · Drafted title/meta/H1 · Revised outline · Internal link suggestions · Schema suggestion · Content gaps · Apply checklist · Sources.
- Ledger row, APPEND-ONLY, exact columns `| date | metric | baseline | current | target | source | confidence | note |`:
  - Solo/Team: append to `Memory/kpi-ledger.md`.
  - Agency: append to `Clients/{slug}/goals.md`.
  - Row form: `metric` = `rank: {target query}`; `baseline` = known position or `unset`; `current` = known position or `unset`; `target` = desired position (e.g. `top 3`); `source` = the rank source or `inferred`; `confidence` in {confirmed, reported, inferred, stale}; `note` = page slug + that this is an optimization draft.
  - Never edit or reorder existing rows.

## Guardrails
- DRAFT-ONLY: output is `status:draft`. Never publish, push live, or edit the production page. A human applies the changes; publishing is a separate human-approved act.
- VOICE: load `Library/styles/brand-voice.md` + `Company/brand.md` (Agency: the client's `brand.md`) before drafting; write title, meta, and copy in that voice.
- FIREWALL (Agency): read and write only the ACTIVE client's `Clients/{slug}/` workspace; never read a sibling client; client outputs are `confidential:true`.
- PROVENANCE: cite a source for every external fact or competitor observation. Never invent rankings, traffic, or metrics. When a baseline is set or a position moves, append a ledger row with source + confidence.
- No required database or paid vendor. Work from fetched public pages by default; treat any paid rank/keyword tool as an OPTIONAL upgrade only if registered in `_system/connectors.md`.
- Route outputs to canonical homes; kebab-case slugs; ISO dates.

## References
- `Company/icp.md`, `Company/brand.md`, `Library/styles/brand-voice.md` (Agency: `Clients/{slug}/context/icp.md`, `Clients/{slug}/context/brand.md`)
- `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency)
- `_system/connectors.md` (optional paid-tool upgrades)
