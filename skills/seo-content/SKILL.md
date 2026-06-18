---
name: seo-content
description: Write or optimize a content piece for a target query and its search intent with structure, depth, internal links, and a schema suggestion, triggered by "write SEO content", "optimize this article for", "rank for this keyword", or "match search intent"
---

# SEO Content

Write a new piece or rework an existing one so it answers a target query and the intent behind it, then tie the draft to a traffic and conversion metric. Draft only, you publish.

## When to use
- You have a target query (or a small cluster) and want a piece built to rank and convert.
- An existing page ranks on page two, or ranks but converts poorly, and you want it restructured.
- The content plan handed you a brief and you need the full draft, not just an outline.
- You want internal links and a schema type chosen for you before you hand the page to a writer or to wp-publish.

## Inputs
- Target query, plus 2-5 secondary queries if you have them.
- Read intent: informational, commercial, navigational, or transactional. If unstated, infer it from the query and say which you picked.
- The offer or page this content should push toward (from Company/offers/, used for the internal link and the call to action).
- Voice from Library/styles/brand-voice.md (agency: the active client's voice file).
- Optional: an existing URL or markdown file to optimize rather than write fresh.
- Optional: a SERP export, a competitor page, or a keyword export. Treat these as a provided file or a described setup, see _system/connectors.md. Never invent search volume or ranking positions.

## Process
1. Set the slug and date. Solo or Team: create Content/{slug}-{date}/ with brief.md, data/, final/. Agency: create Clients/{slug}/Content/{query-slug}-{date}/ with the same three, and set confidential:true on every file.
2. Write brief.md: target query, secondary queries, the intent you read, the single conversion action, the metric you expect to move, and any source files dropped in data/.
3. Read the intent honestly. Match the format to it: a how-to for informational, a comparison or buyer's guide for commercial, a product or pricing page for transactional. State the format and why in one line.
4. Pull depth signals from data/ if present (SERP export, competitor page, keyword export). List the subtopics a ranking page covers. Where you have no data, write "no data" rather than guessing a number.
5. Draft the outline: one H1 carrying the query in plain words, H2s answering the main sub-questions, H3s for the specifics. Front-load the direct answer in the first 60 to 80 words so a reader and a generative engine both get it fast.
6. Write the body in the voice file. Numbers over adjectives, verbs over nouns. Answer the query, then go one level deeper than the competitor subtopics from step 4.
7. Choose internal links: 2-5 links to existing vault pages or known site URLs, each with descriptive anchor text, at least one pointing at the offer or conversion page from the brief. List anchor plus destination so a person can place them.
8. Suggest one schema type that fits the format (Article, FAQPage, HowTo, Product, or BreadcrumbList) and write a short note on what fields it needs. This is a suggestion in the draft, not emitted markup, hand it to seo-schema if you want the block built.
9. Write the conversion action into the page: one clear next step tied to the offer, placed where intent peaks.
10. If optimizing an existing piece, keep what ranks, mark added and cut sections, and note the before state so the metric move is attributable.
11. Append one row to Memory/kpi-ledger.md for the metric this piece targets (organic sessions, ranking position, or assisted conversions), baseline = current state, confidence per the source (confirmed, reported, inferred, or stale). Never edit a prior row.

## Outputs
- Solo or Team: Content/{slug}-{date}/final/{slug}.md (the draft), Content/{slug}-{date}/final/links.md (anchor plus destination list), Content/{slug}-{date}/final/schema-note.md (the suggested type and fields), Content/{slug}-{date}/brief.md.
- Agency: the same files under Clients/{slug}/Content/{query-slug}-{date}/, each with confidential:true.
- One appended row in Memory/kpi-ledger.md for the target traffic or conversion metric.

## Guardrails
- Draft only. Never publish, push to a CMS, or schedule. Hand the file to wp-publish or the user.
- Voice from the brand-voice file (agency: the client's). No invented metrics, search volume, or ranking positions, cite the source file when you state one.
- Firewall (agency): read only the active client, never a sibling, mark every output confidential:true.
- Provenance: cite SERP, competitor, and keyword sources by file. Append a ledger row when the target metric moves, never overwrite a row.
- Schema is a suggestion in the draft, not emitted markup, building it is seo-schema's job.

## References
- Library/styles/brand-voice.md
- Company/offers/ (for the conversion action and internal link target)
- Memory/kpi-ledger.md (append-only)
- _system/connectors.md (optional SERP, crawler, or keyword export setup)
