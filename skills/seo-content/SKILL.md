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
10. SCORE: E-E-A-T and AI-citation-readiness. Two short rubrics, run on the draft before it leaves your hands. Write both into brief.md as a scorecard.
   - E-E-A-T, score each dimension 0 to 5 and name the evidence in the draft that earns the score:
     - Experience: first-hand detail, original screenshots or numbers, lived specifics a writer who never did the thing could not produce. 0 = generic and interchangeable, 5 = clearly first-hand.
     - Expertise: a named author with credentials or a bio, and depth a non-expert could not fake. 0 = no author and surface-level, 5 = credentialed author plus depth.
     - Authoritativeness: citations to primary sources, and links other authorities in the space would also make. 0 = no sources, 5 = primary sources plus links a peer would endorse.
     - Trust: accuracy, transparency about method, no unsupported claims, clear sourcing on every factual statement. 0 = unsourced claims, 5 = every claim sourced and the method stated.
   - AI-citation-readiness, a second short check, is the page built so an answer engine can quote it. Score 0 to 5 against five marks: a direct answer near the top, each factual claim tied to a source, scannable headings, self-contained passages that still make sense when quoted alone, and structured data where it fits. Note which marks are missing.
   - For each rubric, write the score and the specific gaps to close to raise it: the named section to rewrite, the source to add, the author bio to attach, the passage to make self-contained. Gaps are concrete edits, not adjectives. Cite, never invent: if a claim has no source, the fix is to find one or cut the claim, not to fabricate a citation.
11. If optimizing an existing piece, keep what ranks, mark added and cut sections, and note the before state so the metric move is attributable.
12. Append one row to Memory/kpi-ledger.md for the metric this piece targets (organic sessions, ranking position, or assisted conversions), baseline = current state, confidence per the source (confirmed, reported, inferred, or stale). Never edit a prior row.

## Outputs
- Solo or Team: Content/{slug}-{date}/final/{slug}.md (the draft), Content/{slug}-{date}/final/links.md (anchor plus destination list), Content/{slug}-{date}/final/schema-note.md (the suggested type and fields), Content/{slug}-{date}/brief.md.
- A scorecard in brief.md: the E-E-A-T score per dimension (Experience, Expertise, Authoritativeness, Trust, each 0 to 5) and the AI-citation-readiness score (0 to 5), each with the specific gaps to close to raise it.
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
