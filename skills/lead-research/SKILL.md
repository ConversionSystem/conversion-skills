---
name: lead-research
description: Research a target account or prospect from public sources and write a fit-scored profile with outreach hooks, triggered by "research this lead", "research this account", "look up this prospect", "build a prospect profile", or "who are they and how do we get in"
---

# Lead Research

Build a sourced, fit-scored profile of a target account or prospect from public information, with current signals and 2-3 specific outreach hooks. Draft only · a human runs the outreach.

## When to use
- A new account, company, or named person enters the pipeline and needs a profile before any outreach.
- You want to qualify fit against your ICP before spending time on a deal.
- A teammate (or you) asks "who are they, are they a fit, and what do we open with?"
- Agency: a client engagement needs target accounts researched for the client's own outreach.

## Inputs
- Target identifier: company name + domain, and/or a person's name + role/company. At least one is required.
- `Company/icp.md` · the ideal-customer profile to score fit against (Solo/Team). Agency: the active client's ICP at `Clients/{slug}/context/icp.md`.
- `Company/offers.md` · what you sell, to anchor hooks to a real offer (Agency: `Clients/{slug}/context/offers.md`).
- `_system/connectors.md` · to check whether any OPTIONAL enrichment connectors are registered (none are required).
- Optional operator context: target's website URL, a specific deal/opportunity, or named people to prioritize.

## Process
1. **Resolve the target and confirm profile mode.** Derive a kebab-case `{slug}` from the company name (e.g. "Northwind Logistics" -> `northwind-logistics`). Solo/Team -> output goes to `Pipeline/`. Agency: if this research is for a client engagement, set the active client and route ALL output into that client's workspace; otherwise treat as house pipeline. Decide account vs prospect: company-led research = `accounts/`, named-person-led research = `prospects/`.
2. **Load context first.** Read the ICP, offers, and brand context for the correct owner (house vs active client). If the ICP file is missing, note the gap and score fit as `inferred` against whatever profile exists; do not invent ICP criteria.
3. **Gather from public sources (web fetch by default).** Fetch the target's own pages · homepage, about, product/pricing, careers, blog/newsroom · plus public mentions (press, public social posts, public filings, job boards). Record the URL and access date for every fact. Use only OPTIONAL connectors that are already registered in `_system/connectors.md`; never require a paid data vendor. Do not access anything gated, private, or login-walled.
4. **Build the company picture.** Capture what they do, who they serve, size/segment signals, business model, and recent direction. Keep claims tied to a cited source; mark anything uncertain as `inferred`.
5. **Score fit vs ICP.** Compare the target against each ICP dimension. Give a plain verdict (strong / partial / weak fit) with 2-4 reasons, each citing the evidence. State disqualifiers explicitly if present.
6. **Identify signals and triggers.** Note time-bound buying signals · hiring, funding, launches, leadership changes, expansion, public pain, tech/stack changes, content themes. Each signal needs a source and a date.
7. **Map key people.** List relevant decision-makers and influencers with role, why they matter, and a public source. Capture only business-context professional information from public pages; do not collect private contact details.
8. **Draft 2-3 outreach hooks.** Each hook ties a specific, cited signal to a specific line from `offers.md` · concrete, not generic. Mark each hook `status:draft`. Do NOT write, send, queue, or schedule any outreach.
9. **Write the profile** to the canonical path with full universal frontmatter and a `## Sources` section listing every URL + access date. Append a KPI ledger row only when this research sets or moves a tracked baseline (e.g. a new qualified account added to the pipeline metric).

## Outputs
- **Prospect profile (person-led):** `Pipeline/prospects/{slug}.md` (Solo/Team) OR `Clients/{slug}/prospects/{prospect-slug}.md` (Agency, `confidential:true`).
- **Account profile (company-led):** `Pipeline/accounts/{slug}.md` (Solo/Team) OR `Clients/{slug}/accounts/{account-slug}.md` (Agency, `confidential:true`).
- Each profile includes: universal frontmatter (`type:lead-profile`, `status:draft`, `owner`, `date`, `reviewed`, `tags` [>=2], `confidential`, `source`, `generated:true`); company summary; fit-vs-ICP verdict with reasons; signals/triggers (dated, sourced); key people + roles; 2-3 draft outreach hooks; and a `## Sources` section.
- **Ledger row (only when a baseline is set or moved):** appended to `Memory/kpi-ledger.md` (Solo/Team) OR `Clients/{slug}/goals.md` (Agency) using the exact columns `| date | metric | baseline | current | target | source | confidence | note |`. Append-only; never edit or reorder prior rows. Confidence in {confirmed, reported, inferred, stale}.

## Guardrails
- DRAFT-ONLY: produce a profile and draft hooks at `status:draft`. NEVER publish, send, post, email, queue, or schedule outreach. A human ships it.
- VOICE: load `Library/styles/brand-voice.md` + `Company/brand.md` first (Agency: the client's `Clients/{slug}/context/brand.md`); write hooks in that voice.
- FIREWALL (Agency): write only into the ACTIVE client's `Clients/{slug}/` workspace; never read a sibling client; client outputs are `confidential:true`. Solo/Team writes to `Pipeline/`.
- PROVENANCE: cite a source for every external fact; never invent metrics, headcounts, funding, or contacts. When a baseline is set or moves, append a ledger row with source + confidence.
- PUBLIC-ONLY: use public pages and already-registered OPTIONAL connectors only. No gated, private, or login-walled data; no required paid vendor. Collect professional/business-context information only.
- Route outputs to canonical homes; kebab-case slugs; ISO dates; universal frontmatter on the file.

## References
- `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) · fit scoring criteria.
- `Company/offers.md` (Agency: `Clients/{slug}/context/offers.md`) · anchor for outreach hooks.
- `_system/connectors.md` · registry of OPTIONAL enrichment connectors (none required).
- `Memory/kpi-ledger.md` (Agency: `Clients/{slug}/goals.md`) · append-only KPI ledger.
