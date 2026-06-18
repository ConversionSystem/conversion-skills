---
name: blog-post
description: Drafts one long-form blog post optimized for a target search query and the ICP with a search-intent title, an intro that earns the read, scannable sourced H2/H3 sections, internal-link and schema suggestions, and one offer-tied CTA, written to Content as a draft - triggers on /blog-post, "write a blog post", "draft an article", "write a post targeting {query}", "rank an article for {keyword}", "long-form SEO content"
---

# Blog Post

Drafts one long-form, publish-ready blog post built to match a single target query AND the ICP's intent, in the business's voice and grounded in real material, with internal-link and schema suggestions and one offer-tied CTA. DRAFT-ONLY: a human publishes it.

## When to use

- You have a target query (or topic) and you want a complete long-form article that matches search intent and speaks to the ICP, not thin filler.
- You have seo-audit/seo-optimize output, a content-plan slot, or a keyword you want an article to own, and you want the post drafted end-to-end.
- NOT for optimizing an existing live page against one query (use the seo-optimize skill) and NOT for a periodic broadcast to your list (use the newsletter skill). Pairs with the repurpose skill to spin the post into social/email after it ships.

## Inputs

- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md`. Agency profile: the CLIENT's `Clients/{slug}/context/brand.md` instead.
- **Reader & intent:** `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) — who the post is for and the job they are trying to do.
- **The one CTA:** `Company/offers.md` (Agency: `Clients/{slug}/context/offers.md`) — the offer the single CTA ties to.
- **Search signal (if any):** existing seo-audit or seo-optimize output for the topic in `Content/{slug}-{date}/` or `Projects/{slug}/`, a `content-plan` slot, or the user-supplied target query and 2-4 secondary queries.
- **Internal-link inventory:** existing shipped pages/posts in `Content/`, `Projects/`, and `Company/` the new post can link to (for internal-link suggestions).
- **The metric baseline:** `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) — to read any current traffic/ranking/conversion baseline.
- **From the user (ask only for genuine gaps):** the target query, the publish intent, and which offer the CTA points to.

## Process

1. **Resolve profile and write location.** Solo/Team: write to `Content/blog-{slug}-{date}/final/`, ledger is `Memory/kpi-ledger.md`. Agency: resolve the active client, obey the FIREWALL (read only that client's `Clients/{slug}/`), write to `Clients/{slug}/work/blog-{slug}-{date}/final/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill.
2. **Load voice, then context.** Read the voice files first, then ICP, offers, any seo-audit/seo-optimize output for the topic, and the internal-link inventory. Confirm in one line what you found ("Voice: plain, numbers over adjectives; reader: ops leads at 20-100-person agencies; query: 'how to reduce churn'; CTA: the free audit") and ask only for what is absent (the target query, the offer).
3. **Define search intent and angle.** Classify the target query's intent (informational, commercial, transactional, navigational) and state the job the searcher is doing, grounded in `Company/icp.md`. Define what a satisfying result must answer and the post's distinct angle vs. generic results — concrete, with a point of view, not a roundup of the obvious.
4. **Outline and confirm.** Show the working title, the H2/H3 skeleton (each section mapped to a subtopic the intent implies), where the single CTA lands, and the internal links and schema you will suggest — before writing the full draft. One post, one primary CTA.
5. **Write the title and intro.** Title: search-intent-matching, target query near the front, ~60 chars, no clickbait. Intro: earns the read in the first lines — name the reader's problem and the payoff, no warm-up throat-clearing.
6. **Write the body in voice.** Scannable H2/H3 sections, each with specifics and at least one concrete example, number, or worked detail rather than generalities. Every number real and traceable to its source; cite any external fact with its source URL; invent no metrics. Use the business's (Agency: the client's) voice throughout.
7. **Add link, schema, and CTA layers.**
   - **Internal links:** 3-8 specific suggestions with anchor text and the destination page, drawn from the vault's existing content.
   - **Schema suggestion:** recommend the appropriate type (e.g. Article, FAQPage, HowTo, BreadcrumbList) and the key fields to populate — suggest only; do not assert it is installed.
   - **CTA:** one offer-tied CTA from `Company/offers.md` (Agency: the client's offers), placed where the reader has earned the ask. Never append an audit/report CTA into the body.
8. **Instrument.** Add a `## Metrics to track` block tied to a traffic/conversion metric: target query rank and/or organic sessions for the post, and the post's conversion to the CTA offer, each with a benchmark band and the one decision it drives.
9. **Persist as a draft.** Write the deliverable with `status:draft` and full universal frontmatter, write the brief and data intermediates, and append the ledger row (see Outputs). Close with the next action (a human reviews and publishes; pair with the repurpose skill).

## Outputs

- **Deliverable** → `Content/blog-{slug}-{date}/final/post.md` (Solo/Team) or `Clients/{slug}/work/blog-{slug}-{date}/final/post.md` (Agency), `status:draft`, with: search-intent title · intro · scannable H2/H3 body with specifics and examples · internal-link suggestions (anchor + destination) · schema suggestion · one offer-tied CTA · `## Metrics to track` · sources. Universal frontmatter on the file (type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated). `type: blog-post`; Agency files are `confidential:true`.
- **Brief** → same folder `brief.md`: target query + intent, secondary queries, audience, the angle, the one action/CTA, and acceptance criteria.
- **Intermediate data** → same folder `data/`: `baseline.json` (target query, intent, the KPI being moved, and current baseline if known) and `inputs.json` (the context snapshot drafted from, including the internal-link inventory used).
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - **Rank:** `metric` = `rank: {target query}`; `baseline`/`current` = known position or `unset`; `target` = desired position (e.g. `top 3`); `source` = rank source or `inferred`; `confidence` in {confirmed, reported, inferred, stale}; `note` = post slug + that this is a draft.
  - **Traffic:** if an organic-sessions baseline for the post/topic exists, append the current value with its source and confidence. If none exists, SEED a first row (baseline = current = the user-confirmed number, or `inferred` if estimated) and FLAG it for the user to confirm — never invent a baseline.
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY.** Produce `status:draft`. Never publish, push live, or post the article autonomously — a human publishes it. A connector may only push a DRAFT (e.g. a draft post), never go live.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` before writing (Agency: the CLIENT's `Clients/{slug}/context/brand.md`). If the voice file is thin, ask for one real sample rather than improvising a voice.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Every result and number is real and traceable to `goals.md`/`Memory/`/a user-named source; cite external facts with their source URL; invent no metrics, rankings, or traffic. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- One post, one primary CTA; specifics and examples over generalities; match search intent and the ICP, not just the keyword.
- Content ships clean: the CTA is the user's own offer — never append an audit/report CTA into the body.
- No required database or paid vendor; work from provided exports and fetched public pages. Treat any paid keyword/rank tool or platform connector as an OPTIONAL upgrade only if registered in `_system/connectors.md`.
- A delivery run without its ledger row is unfinished.
- Original expression only; no lifted articles or competitor copy.

## References

- `Company/icp.md`, `Company/brand.md`, `Library/styles/brand-voice.md`, `Company/offers.md` (Agency: `Clients/{slug}/context/icp.md`, `Clients/{slug}/context/brand.md`, `Clients/{slug}/context/offers.md`)
- `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency)
- `_system/connectors.md` — OPTIONAL keyword/rank tools and platform draft-push connectors; zero-infra default needs none.
