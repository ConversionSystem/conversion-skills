---
name: ads-creative
description: Drafts ad creative in brand voice with hooks, primary text, headlines, and variants per platform and format, triggered by "write ad copy", "ad creative", or "draft ads"
---

# Ad Creative

Drafts ad creative in the brand voice across platforms and formats, with hooks, primary text, headlines, descriptions, and tested variants. Draft only, written to file, never posted.

## When to use
- You need ad copy for a launch, an offer, a campaign, or a single placement.
- You want several angles to test, not one safe version.
- You are briefing a designer or a media buyer and need the words first.
- You ran /ads-plan or /ads-audit and now need the creative those flagged.

## Inputs
- The offer and the audience: Company/offers/, Company/icp/, Company/profile.md.
- The voice: Library/styles/brand-voice.md (Agency: the active client's voice file under Clients/{slug}/).
- Target platform and format (Meta, Google, LinkedIn, TikTok, YouTube, Microsoft), supplied by you or read from the campaign brief.
- Any proof to cite: case studies in Operations/case-studies/, metrics in Memory/kpi-ledger.md, testimonials in Operations/.
- Optional connectors registered in _system/connectors.md (a competitor ad export, an analytics export). Default to a provided export or run without them.

## Process
1. Read the voice file first. If Library/styles/brand-voice.md is missing, stop and say so. Copy never ships without a voice to match. Agency: read the active client's voice file, never a sibling client's.
2. Read the offer, the ICP, and the profile so the copy names the buyer, the pain, and the promise in concrete terms. Pull any proof you can cite. Never invent a metric; if a number appears, it must trace to Memory/kpi-ledger.md or a named source.
3. Confirm the platform and format. For each, note the character ceilings and the count of assets a campaign expects (for example, Meta primary text plus headline plus description; Google responsive search with 15 headlines and 4 descriptions; LinkedIn intro plus headline). Write to the limits, not over them.
4. Draft 3 to 5 distinct angles, not 5 rewrites of one. Cover at minimum: a pain-led hook, a proof-led hook, an offer-led hook, and a curiosity or pattern-break hook. State the angle above each block so the buyer knows what is being tested.
5. For each angle and format, write the full asset set: hook or primary text, headline variants, description variants, and the call to action. Keep verbs first, numbers over adjectives, one idea per line. Run the brand check: no em-dashes, no blocklist words.
6. Add a short test note per angle: what it tests, what a win looks like, which metric in Memory/kpi-ledger.md it should move. Do not predict results.
7. Write the file. Solo/Team: Content/{slug}-{date}/final/ad-creative.md. Agency: Clients/{slug}/Content/{slug}-{date}/final/ad-creative.md with confidential:true in the frontmatter. Save the brief and any inputs alongside in the same folder under brief.md and data/.
8. If a tracked metric moves because this creative shipped later, that is logged by the skill that confirms the result, not here. This skill drafts only.

## Outputs
- Content/{slug}-{date}/final/ad-creative.md (Agency: Clients/{slug}/Content/{slug}-{date}/final/ad-creative.md, confidential:true): angles, full asset sets per platform and format, character counts, call to action, and per-angle test notes.
- Content/{slug}-{date}/brief.md: the offer, audience, platform, and format the draft was built from.
- No ledger row. This skill writes copy, it does not move a metric. A row is appended later by the skill that confirms a live result.

## Guardrails
- DRAFT-ONLY: write copy to file. Never publish, post, schedule, boost, or change a budget or a bid.
- VOICE: match Library/styles/brand-voice.md (Agency: the active client's voice). No copy without a voice file present.
- FIREWALL (Agency): the active client only. Never read a sibling client. Client outputs carry confidential:true.
- PROVENANCE: cite every claim. Never invent a metric, a result, or a quote. A number must trace to Memory/kpi-ledger.md or a named source.
- BRAND: no em-dashes anywhere. No blocklist words. Numbers over adjectives, verbs over nouns, terse.

## References
- Library/styles/brand-voice.md
- _system/connectors.md
- Memory/kpi-ledger.md
