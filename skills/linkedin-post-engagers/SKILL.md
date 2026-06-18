---
name: linkedin-post-engagers
description: Turn a LinkedIn post URL or an export of who reacted and commented into a prioritized outreach list scored against your ICP, each person carrying a personalized hook earned from a real signal · triggers on "who engaged with this post", "LinkedIn post engagers", "score the people who liked my post", "outreach list from a LinkedIn post", "warm leads from LinkedIn", "rank the commenters", "build prospects from engagement"
---

# LinkedIn Post Engagers
Take a LinkedIn post (a URL or an export of who reacted and commented) and build a prioritized outreach list scored against `Company/icp` · each person earns one personalized hook drawn from a real signal (their comment, role, or recent activity), written to `Pipeline/prospects/`. No outreach is sent.

## When to use
- A post landed well and you want to work the people who engaged before the signal goes cold.
- You have an export of reactions and comments and need it ranked, not left as a raw name dump.
- A campaign or launch post drew the right audience and you want the highest-fit accounts surfaced first.
- You want each prospect to come with a specific reason to reach out, not a generic template.
- Before a sales push, to convert passive engagement into a ranked "who to message first" queue.

## Inputs
- A LinkedIn post URL, or an export of who engaged (CSV/JSON) · typically dropped in `Inbox/`. Map its columns to: name, headline/title, company, profile URL, engagement type (reaction kind, comment), comment text, engagement date.
- A LinkedIn connector registered in `_system/connectors.md` (OPTIONAL) · used only to pull the engager list and public profile fields when no export is provided. If absent, work from the provided export or a precise brief and note the limitation. Credentials never live in the vault.
- `Company/icp.md` · the scoring rubric (segment, role, company size, trigger fit).
- `Company/offers.md` and `Company/strategy.md` · to frame the hook and judge relevance.
- `Library/styles/brand-voice.md` and `Company/brand.md` · voice for any drafted hook (Agency: `Clients/{slug}/context/`).
- `Memory/kpi-ledger.md` · for current prospecting baselines and targets.
- Agency profile: read only the ACTIVE client's `Clients/{slug}/` workspace; never read a sibling client.

## Process
1. **Identify profile and source.** Determine the active profile. Locate the engager source: a provided export in `Inbox/` (or the path given), or a post URL to pull via the LinkedIn connector if registered. If neither the connector nor an export is available, stop and ask for an export · do not fabricate an engager list.
2. **Normalize the engager list.** Parse the source and map each person to standard fields (name, headline, company, profile URL, engagement type, comment text, engagement date). Keep the raw engagement signal verbatim · a comment is the richest hook and must be preserved exactly. Flag rows with missing company or title as gaps to enrich, never as values to invent.
3. **Dedupe and filter.** Collapse duplicate people (someone who both reacted and commented is one record, strongest signal kept). Drop obvious non-prospects per the ICP (competitors, current customers already in `Pipeline/`, clear out-of-segment). Cross-check `Pipeline/prospects/` so existing records are updated, not duplicated.
4. **Score against ICP.** Read `Company/icp.md` and score each person on a transparent rubric: role/seniority fit × segment/company fit × engagement strength (a thoughtful comment > a reaction > a passive like) × recency. Record the component scores so the ranking is auditable, not a black box.
5. **Earn a hook per person.** For each scored prospect, derive ONE personalized hook from a real, cited signal · their actual comment, a specific line in their headline, their company's stated focus, or recent public activity. The hook names the signal ("you flagged X in your comment on the post") and connects it to one offer or idea. Never invent a quote, a role, or a shared event. If no real signal exists beyond a bare reaction, mark the hook `signal:thin` and keep it honest.
6. **Rank and segment.** Produce one ordered list, highest-fit first. Tier into A (strong fit, strong signal · work now), B (fit or signal, not both · nurture), C (weak · skip or watch). State the cutoffs used.
7. **Write prospect profiles.** For each A and B prospect, write a profile file to `Pipeline/prospects/` (Agency: `Clients/{slug}/pipeline/prospects/`) with the fields below. C-tier may be listed in the summary roll-up without individual files.
8. **Draft the hook (optional, draft-only).** Where requested, draft the opening message in the business's voice (Agency: the client's). Load brand-voice and brand files first. Every draft carries `status:draft`. Never send, message, connect, or contact anyone on LinkedIn or elsewhere.
9. **Update the ledger.** Append one or more rows recording engagers processed and qualified prospects added, citing the post or export as source with a confidence rating. Never edit or reorder prior rows.

## Outputs
- **Prospect profiles** · one file per A/B prospect at `Pipeline/prospects/{name-slug}.md` (Agency: `Clients/{slug}/pipeline/prospects/{name-slug}.md`). Full frontmatter; `generated:true`; fields: name · headline · company · profile URL · ICP score (with components) · tier · engagement signal (verbatim) · personalized hook · `signal:` strength · suggested next move · source post. Agency outputs `confidential:true`.
- **Prioritized outreach list** · Solo/Team: `Pipeline/linkedin-engagers-{date}.md`. Agency: `Clients/{slug}/pipeline/linkedin-engagers-{date}.md`. A ranked table of `name · company · score · tier · hook` plus counts by tier and the scoring/cutoff notes.
- **Hook drafts (optional)** · `Pipeline/outreach/{name-slug}-{date}.md` (Agency: `Clients/{slug}/outreach/{name-slug}-{date}.md`). Each `status:draft`; Agency `confidential:true`.
- **Ledger row** · appended to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), exact columns:
  `| date | metric | baseline | current | target | source | confidence | note |`
  Append `engagers-processed` (count) and `prospects-qualified` (count), each citing the post URL or export filename as source, confidence in {confirmed, reported, inferred, stale}. Counts from a clean export = reported; figures inferred from a partial pull = inferred.

## Guardrails
- DRAFT-ONLY: build lists, profiles, and message drafts only. Never send a message, connection request, or any contact on LinkedIn or off it. A human ships every touch.
- FIREWALL (Agency): operate inside the ACTIVE client's `Clients/{slug}/` only; never read a sibling client; all client outputs are `confidential:true`.
- VOICE: write any hook in the business's voice (Agency: the client's voice) · load brand-voice and brand files before drafting.
- PROVENANCE: every hook rests on a cited, real signal. Never invent a comment, quote, title, company, or shared moment. A bare reaction is marked `signal:thin`, not dressed up.
- CONNECTOR: the LinkedIn connector is optional and used read-only to pull the engager list; respect platform terms; credentials stay outside the vault. With no connector and no export, ask rather than guess.
- LEDGER INTEGRITY: append-only; never edit or reorder prior rows; use only the locked columns and confidence vocabulary.
- State the scoring rubric and tier cutoffs so the ranking is reproducible and auditable.

## References
- `_system/rules.md`, `_system/config.md`, `_system/connectors.md` · profile, routing, optional LinkedIn connector.
- `Company/icp.md`, `Company/offers.md`, `Company/strategy.md` · fit, framing, and hook relevance.
- `Library/styles/brand-voice.md`, `Company/brand.md` · voice for drafted hooks.
