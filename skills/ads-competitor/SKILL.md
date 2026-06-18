---
name: ads-competitor
description: Analyze a competitor's public-library ads for angles, offers, formats, and cadence, then name the gap to take, citing every source · triggers on "competitor ads", "analyze competitor ads", "ad competitor analysis", "what ads are they running", "Meta ad library", "Google ads transparency", "find the gap in their ads".
---

# Ad Competitor

Analyze a competitor's live and recent ads from public ad libraries (Meta Ad Library, Google Ads Transparency Center, TikTok Creative Center, LinkedIn) for their angles, offers, formats, and cadence, then name the gap a human can take.

## When to use
- The user wants to know what a named competitor is advertising and where the opening is.
- A public ad-library URL, a pasted export, or screenshots of a competitor's ads are available, or the user can name the competitor and the platform to search.
- The user is planning new creative, entering a category, or pricing an offer and wants the field mapped first.
- Use before `/ads-creative`, before a launch, or as a recurring watch on a known rival.

## Inputs
- Competitor name and the platform(s) to read: meta, google, tiktok, or linkedin. If unstated, ask before proceeding.
- Source material placed in the project's `data/` folder: a copied ad-library listing, a CSV or JSON export, screenshots, or pasted ad copy. If none exists, a public ad-library URL or the competitor's page/advertiser name to look up, plus the country to view ads from (libraries are region-gated).
- The window to cover (e.g. last 30 days, currently active only) and how many ads to sample if the library is large.
- Company context: `Company/profile.md`, `Company/offers.md`, `Company/icp.md` for your own offer and audience, `Company/competitors.md` for prior notes on this rival, `Company/brand.md` for voice.
- Agency profile: the active client's `Clients/{slug}/context/` files in place of `Company/`, read only within that client's workspace.
- Brand voice from `Library/styles/brand-voice.md` (Solo/Team) or `Clients/{slug}/context/brand.md` (Agency) when judging messaging and drafting the gap angle.

## Process
1. **Resolve profile and output home.** Read `_system/config.md` to determine profile.
   - Solo/Team: create `Projects/ads-competitor-{competitor-slug}-{date}/` with `brief.md`, `data/`, and `final/`.
   - Agency: confirm the ACTIVE client, then work inside `Clients/{slug}/work/ads-competitor-{competitor-slug}-{date}/`. Operate only within that client's workspace, never read a sibling client. All outputs are `confidential:true`.
2. **Load context and sources.** Read your own profile, offers, ICP, prior competitor notes, and brand voice. Ingest every file in `data/`. If only a URL or advertiser name was given, record it in `brief.md` and capture each ad you read with its library link, the date seen, the country viewed from, and whether it is currently active. Public ad libraries only · no logins, no scraping behind a paywall, no private data.
3. **Inventory the ads.** Build one row per ad: ad id or library link · first-seen and last-seen dates (if shown) · active/inactive · platform · format (static image, video, carousel, text, lead form) · destination URL or landing surface · headline and primary copy verbatim (quote it, cite the link). Note runtime/longevity where the library shows it · long-running ads signal what is working for them.
4. **Classify angles.** Group the ads by the persuasion angle each one leads with (problem-agitate, social proof, price/discount, speed, authority, fear of missing out, comparison, founder story, guarantee). Count ads per angle. Mark which angles they lean on hardest and which they ignore.
5. **Map offers and hooks.** Extract every distinct offer, promotion, price point, and call to action they put in front of buyers (free trial, demo, discount, bundle, bonus, urgency device). Note the first line or visual hook of each ad · the part doing the stopping work. Quote, do not paraphrase, and cite each.
6. **Read format and production.** Tally format mix and production level (UGC vs polished, talking-head vs motion graphics, length bands for video, hook-in-first-3-seconds patterns). Note which formats carry the long-running ads.
7. **Read cadence.** From first-seen/last-seen dates and active counts, sketch how many ads they keep live, how often new creative appears, and how long ads survive. Flag bursts (launch or seasonal) versus steady-state. Label any cadence read `inferred` when the library only shows partial dates.
8. **Find the gap.** Cross the competitor's angle/offer/format coverage against your own offers, ICP, and brand voice. Name the openings: angles they neglect that fit your buyer, offers they cannot or will not match, formats they underuse, and proof you hold that they lack. Pick the single sharpest gap to take and say why it is takeable.
9. **Draft the takeaway.** Write 3 to 5 concrete, draft-only angle or hook directions you could test against this competitor, each tied to a gap and written in the business's voice (Agency: the client's). These are starting points for `/ads-creative`, not finished ads. Label every output `status:draft`.
10. **Write the report.** Write `final/ads-competitor-{competitor-slug}-{date}.md` with universal frontmatter (`status:draft`, `generated:true`, plus `confidential:true` for Agency): an executive summary, the ad inventory table, the angle counts, the offer/hook list, the format and cadence read, the gap analysis, and the drafted angle directions. Every claim carries its `source` (library link or filename). Never invent an ad, a date, or a spend figure · libraries rarely show spend, so do not estimate it.
11. **Append the ledger.** If you log a tracked metric (e.g. competitor active-ad count, distinct-offer count, dominant-angle share), add APPEND-ONLY rows to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), one row each, exact columns, `source` = library link, `confidence` = `confirmed` (counted from the library) or `inferred` (read from partial data). Never edit or reorder prior rows.

## Outputs
- `Projects/ads-competitor-{competitor-slug}-{date}/brief.md` (Solo/Team) or `Clients/{slug}/work/ads-competitor-{competitor-slug}-{date}/brief.md` (Agency) · competitor, platforms, window, country, sources.
- `…/final/ads-competitor-{competitor-slug}-{date}.md` · the analysis report (executive summary, ad inventory table, angle counts, offer/hook list, format and cadence read, gap analysis, 3 to 5 drafted angle directions), `status:draft`, `generated:true`, `confidential:true` for Agency.
- Raw sources (exports, screenshots, copied listings) retained under `…/data/`.
- Optional ledger rows appended to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency): one APPEND-ONLY row per tracked metric (e.g. active-ad count, distinct-offer count) with `source` and `confidence`.

## Guardrails
- DRAFT-ONLY: this skill observes and recommends. Never publish, launch, or send anything, never contact the competitor, and never apply a single angle as a live ad. Every direction is a human decision.
- PROVENANCE: cite the ad-library link or the source filename for every ad and every claim. Quote ad copy verbatim. Never invent ads, dates, longevity, or spend · libraries seldom expose spend, so label it unavailable rather than estimating. Mark any cadence or longevity read `inferred` when the data is partial.
- PUBLIC SOURCES ONLY: read only public ad libraries and material the user supplies. No logins to a competitor's account, no scraping behind authentication, no private or personal data.
- VOICE: load brand voice before drafting angle directions; write them in the business's voice (Agency: the client's voice).
- FIREWALL (Agency): operate only within the active client's `Clients/{slug}/` workspace, never read a sibling client, mark all outputs `confidential:true`.
- CONNECTORS: ad-library crawlers or APIs are OPTIONAL. Default to a provided export, a public library URL, or supplied screenshots. Only use a connector if it is registered in `_system/connectors.md` and the user has enabled it, and only to READ public data.
- LEDGER: append-only with the exact columns; confidence in {confirmed, reported, inferred, stale}; never edit or reorder prior rows.

## References
none
