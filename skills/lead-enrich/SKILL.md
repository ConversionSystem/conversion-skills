---
name: lead-enrich
description: Enrich a prospect or account with firmographic and contact context from public sources and write the enriched fields back to its Pipeline file with a confidence note and cited sources, triggered by "enrich this lead", "enrich this account", "fill in this prospect", "add company context", or "enrich the prospect file"
---

# Lead Enrich

Add firmographic and professional-context fields · company size, funding, tech, key roles, recent news · to an existing prospect or account file from public sources, with per-field confidence and cited sources. Draft only · no outreach.

## When to use
- A prospect or account file in `Pipeline/` is thin and needs firmographic + contact context before qualification or outreach planning.
- You have a target's name/domain and want company size, funding, tech stack, decision-maker roles, and recent news pulled into one file.
- A teammate (or you) asks "fill this in" or "what do we actually know about this account?"
- Agency: a prospect/account inside the ACTIVE client engagement needs enrichment for that client's own pipeline.
- Distinct from `lead-research` (builds a profile from scratch) and `lead-qualify` (scores fit): this skill ADDS fields to a file that already exists, leaving the verdict and outreach to those skills.

## Inputs
- An existing target file: `Pipeline/prospects/{slug}.md` or `Pipeline/accounts/{slug}.md` (Solo/Team), OR the active client's equivalent under `Clients/{slug}/` (Agency). If only raw identifiers are given, point the user at `lead-research` to create the file first; do not silently create a full profile here.
- `Company/icp.md` · to know which firmographic fields actually matter (Agency: `Clients/{slug}/context/icp.md`). Optional but recommended.
- `_system/connectors.md` · to check which OPTIONAL enrichment connectors are registered (none are required; web fetch of public pages is the default).
- `_system/config.md` · active profile (Solo/Team vs Agency) and ledger location.
- `_system/permissions.md` · to confirm the user has authorized storing the data being collected.

## Process
1. **Resolve profile and locate the file.** Read `_system/config.md` for the active profile. Solo/Team: target lives in `Pipeline/prospects/{slug}.md` or `Pipeline/accounts/{slug}.md`, ledger at `Memory/kpi-ledger.md`. Agency: operate only inside the ACTIVE client's `Clients/{slug}/` workspace, ledger at `Clients/{slug}/goals.md`; never read a sibling client. If the named file does not exist, stop and recommend `lead-research`; do not invent a profile.
2. **Confirm scope and authorization.** Check `_system/permissions.md` for what data the user has authorized storing. Collect only professional, business-context information; never collect private or personal contact details the user has not authorized. If a field is out of scope, skip it and note why.
3. **Check connectors, default to public.** Read `_system/connectors.md`. Use an OPTIONAL enrichment connector only if it is already registered; otherwise enrich from public web pages by web fetch. Never require a paid data vendor and never name one as required.
4. **Gather firmographics from public sources.** Fetch the target's own pages (homepage, about, careers, pricing, newsroom/blog) and public mentions (press, public filings, job boards, public social posts) for: company size/headcount band, location/HQ, industry/segment, business model, funding/ownership signals, and visible tech/stack signals. Record the source URL and access date for every value.
5. **Gather contact-role context.** Identify relevant decision-maker and influencer ROLES with a public source for each (title, why they matter). Capture only business-context professional information from public pages; do not store private emails, phone numbers, or personal data the user has not authorized.
6. **Gather recent news/signals.** Note dated, time-bound signals · funding, hiring, launches, leadership changes, expansion · each with a source URL and date.
7. **Tag every field with confidence.** Mark each enriched value `confirmed` (direct from a primary source), `reported` (third-party stated it), `inferred` (deduced from signals), or `stale` (last known, possibly outdated). Never fabricate a value to fill a blank · leave it `unknown`.
8. **Respect ToS and gates.** Do not access or scrape any source whose terms of service forbid it, and never access gated, private, or login-walled data. If a source is off-limits, skip it and record the gap.
9. **Write fields back into the file.** Update the existing target file: fill or refresh an `## Enrichment · {date}` section with the firmographic fields, contact-role context, recent signals, a per-field confidence note, and a `## Sources` block (URL + access date for every fact). Update `reviewed` in frontmatter to today; never overwrite a prior `## Qualification` block or another skill's section.
10. **Append a ledger row only if a baseline moves.** If enrichment sets or moves a tracked metric (e.g. an account crossing into ICP size band, or first enrichment of a pipeline account), append one APPEND-ONLY ledger row. Otherwise make no ledger change.

## Outputs
- **Updated target file:** `Pipeline/prospects/{slug}.md` or `Pipeline/accounts/{slug}.md` (Solo/Team) OR the active client's equivalent under `Clients/{slug}/` (Agency, `confidential: true`). The file gains/refreshes an `## Enrichment · {date}` section (firmographics, contact-role context, recent signals · each value carrying a confidence tag), a per-field confidence note, and a `## Sources` section (URL + access date per fact). Frontmatter `reviewed` set to today; universal frontmatter preserved (`type`, `status`, `owner`, `date`, `reviewed`, `tags` [>=2], `confidential`, `source`, `generated:true`).
- **Ledger row (only when a baseline is set or moved):** appended to `Memory/kpi-ledger.md` (Solo/Team) OR `Clients/{slug}/goals.md` (Agency) with the exact columns:
  `| {date} | {metric} | {baseline} | {current} | {target} | {target-file-path} | {confidence} | enriched {slug} |`
  Append-only; confidence in {confirmed, reported, inferred, stale}; never edit or reorder prior rows.
- A short summary returned to the user: what was filled in, per-field confidence highlights, and any fields left `unknown`.

## Guardrails
- DRAFT-ONLY: enrich a file only. NEVER contact, email, message, queue, or schedule outreach to the lead · a human takes any next step.
- AUTHORIZATION + ToS: never scrape a source whose ToS forbids it; never access gated, private, or login-walled data; never store data the user has not authorized in `_system/permissions.md`. Collect professional/business-context information only.
- PROVENANCE: cite a source URL + access date for every external field; never invent headcount, funding, tech, or contacts. Unverifiable values stay `unknown`; each filled value carries a confidence tag.
- PUBLIC-ONLY by default: enrich from public pages; use an OPTIONAL connector only if already registered in `_system/connectors.md`. No required paid vendor.
- FIREWALL (Agency): read and write only the ACTIVE client's `Clients/{slug}/` workspace; never read a sibling client; mark all client outputs `confidential: true`.
- LEDGER: append-only with the exact columns `| date | metric | baseline | current | target | source | confidence | note |`. Never edit or reorder existing rows; append only when a baseline actually moves.
- VOICE: any human-facing note text follows `Library/styles/brand-voice.md` and `Company/brand.md` (Agency: the client's `Clients/{slug}/context/brand.md`).
- Keep slugs kebab-case and all dates ISO (YYYY-MM-DD); write back only to the existing canonical file.

## References
- `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) · which firmographic fields matter.
- `_system/connectors.md` · registry of OPTIONAL enrichment connectors (none required).
- `_system/permissions.md` · what data the user has authorized collecting and storing.
- `_system/config.md` · active profile and ledger location.
- `Memory/kpi-ledger.md` (Agency: `Clients/{slug}/goals.md`) · append-only KPI ledger.
