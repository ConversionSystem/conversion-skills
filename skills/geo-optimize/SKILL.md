---
name: geo-optimize
description: Optimize a page or topic to get cited by AI answer engines and generative search (GEO) with an extractable-claims audit, an improvement draft, and a checklist when you say geo optimize, optimize for AI search, get cited by ChatGPT or Perplexity, generative engine optimization, or AI answer visibility
---

# GEO Optimize

Audit a page or topic for how well AI assistants and generative search engines can read, trust, and quote it, then draft the rewrite and checklist that make it citable.

## When to use
- A page ranks fine in classic search but never gets cited or summarized by AI assistants.
- You are publishing a new pillar/answer page and want it built to be quoted from day one.
- A topic matters to your buyers and you want to own the AI-generated answer for it.
- Leadership asks whether your content shows up when prospects ask an AI assistant.

## Inputs
- The target URL or, for a not-yet-published topic, the draft and its working slug.
- `Company/icp.md` — who is asking the AI, the questions they ask, and the language they use.
- `Company/brand.md` + `Library/styles/brand-voice.md` — voice for any rewritten copy. Agency: `Clients/{slug}/context/brand.md` and that client's voice.
- `Company/offers.md` and `Company/profile.md` — entity facts (who you are, what you sell) the model must get right.
- Optional: existing `Content/{slug}-{date}/` brief, prior GEO audits, any AI-citation tracking export if available.

## Process
1. **Resolve profile and home.** Determine Solo/Team vs Agency. Solo/Team work routes to `Content/{slug}-{date}/`; Agency work routes inside the active client's `Clients/{slug}/` workspace only (firewall — never read a sibling client). Pick or confirm the kebab-case `{slug}` and ISO `{date}`; create `Content/{slug}-{date}/` (or the client equivalent) with `brief.md`, `data/`, and `final/` if missing.
2. **Load context first.** Read `Company/icp.md`, `Company/brand.md`, `Library/styles/brand-voice.md`, `Company/offers.md`, and `Company/profile.md` (Agency: the client equivalents). Capture the buyer's real questions and the entity facts that must stay accurate.
3. **Capture the source.** Fetch the live URL (web fetch) or read the draft. Save the captured text/structure to `Content/{slug}-{date}/data/source.md` with `source` and the fetch date so the audit is reproducible.
4. **Derive the question set.** From the ICP and topic, list the 8–15 natural-language questions a buyer would ask an AI assistant about this topic. Save to `data/questions.md`. These are the prompts the page should be able to answer in a quotable way.
5. **Score the GEO signals.** Assess the page against each signal, rate it (strong / partial / missing), and note the specific gap:
   - Extractable claims — are key answers stated as self-contained, lift-out sentences, not buried in narrative?
   - Structured Q&A — are buyer questions used as headings with direct answers underneath?
   - Quotable stats — are there concrete, attributable numbers a model can cite (with a source)?
   - Citations and sources — does the page cite primary sources, and is it itself citable (clear claims a model can attribute)?
   - Entity clarity — is it unambiguous who/what the page is about (names, definitions, "X is a …" framing)?
   - Schema markup — is there structured data (FAQ, Article, Organization, How-To) that machine-reads the content?
   - Answer-first structure — does each section lead with the answer before the explanation?
   - Freshness and specificity — dates, versions, and specifics that signal current, trustworthy content.
   Record the scored table in `data/geo-assessment.md`.
6. **Draft the improvements.** Write a status:draft improvement document that, for each weak signal, gives the concrete fix and rewritten copy in the business's (Agency: the client's) voice: extractable-claim rewrites, a Q&A block mapped to the question set, stat callouts with sources, an entity/definition paragraph, and a recommended schema block (as a draft snippet, not deployed). Keep every external fact sourced; never invent metrics.
7. **Build the checklist.** Produce an ordered, do-this GEO checklist (claims, Q&A, stats, entity, schema, freshness, internal links) the owner can work through before publishing.
8. **Tie to a visibility metric.** Define the metric this targets — AI-citation count / share of AI answers if trackable, otherwise a tracked proxy (presence in AI answers for the question set, sampled monthly). If a baseline can be measured now, record it; otherwise mark the baseline as to-be-measured. Append one ledger row (see Outputs).
9. **Write the brief.** Summarize scope, the question set, top gaps, the chosen metric, and the publish-by-human next step in `brief.md`.

## Outputs
- `Content/{slug}-{date}/data/source.md` — captured source text/structure with `source` + fetch date (generated:true).
- `Content/{slug}-{date}/data/questions.md` — the buyer question set the page must answer.
- `Content/{slug}-{date}/data/geo-assessment.md` — scored signal table with per-signal gaps.
- `Content/{slug}-{date}/final/geo-improvements.md` — the improvement draft (rewrites + draft schema snippet), `status: draft`.
- `Content/{slug}-{date}/final/geo-checklist.md` — the ordered pre-publish GEO checklist, `status: draft`.
- `Content/{slug}-{date}/brief.md` — scope, gaps, metric, next step.
- Agency: all of the above under `Clients/{slug}/...` with `confidential: true`.
- KPI ledger row (Solo/Team → `Memory/kpi-ledger.md`; Agency → `Clients/{slug}/goals.md`), APPEND-ONLY, exact columns:
  `| date | metric | baseline | current | target | source | confidence | note |`
  e.g. `| 2026-06-18 | ai-citations:{slug} | to-be-measured | to-be-measured | cited in AI answers for 6/12 questions | geo-optimize audit | inferred | baseline pending first AI-answer sample |`
- All new `.md` files carry universal frontmatter: `type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated`.

## Guardrails
- DRAFT-ONLY: every output is `status: draft`. Never publish, deploy schema, push to a live site, or edit the live page. A connector may only push a DRAFT; going live is a separate human-approved act.
- VOICE: load brand voice before writing any copy; write as the business (Agency: the client). Never use a sibling client's voice or content.
- FIREWALL (Agency): operate only within the active client's `Clients/{slug}/` workspace; never read another client; mark client outputs `confidential: true`.
- PROVENANCE: cite a source for every external fact and every stat suggested for the page; never invent metrics. When a baseline is set or a visibility number moves, append a ledger row with `source` + `confidence`; never edit or reorder prior rows.
- Route outputs to the canonical `Content/{slug}-{date}/` (or client) home; kebab-case slugs; ISO dates.

## References
none
