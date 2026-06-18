---
name: linkedin-writer
description: Draft LinkedIn posts in brand voice from an idea, lesson, result, or offer, with a hook-first main post and two variants, triggered by /linkedin-writer, "write a LinkedIn post", "draft a LinkedIn post", or "turn this into a LinkedIn post"
---

# LinkedIn Writer

Turn one source (an idea, a lesson, a result, or an offer) into a hook-first LinkedIn post in brand voice, plus two variants, written as drafts only.

## When to use
- You have a single idea worth one post and want it shaped for LinkedIn.
- A lesson in Memory/lessons.md is worth sharing publicly.
- A result or KPI move from Memory/kpi-ledger.md is post-worthy.
- You want to announce or re-angle an offer from Company/offers.md.
- You want a main post plus two variants to pick from or A/B over time.

## Inputs
- The source: an idea string, a lesson line, a result, or an offer name.
- Voice rules: Library/styles/brand-voice.md (agency profile: the active client's voice).
- Supporting facts (optional): Memory/kpi-ledger.md for any metric, Company/offers.md for offer terms, Company/icp.md for who reads this.
- A slug for the topic and today's date for the output folder.

## Process
1. Read Library/styles/brand-voice.md and load the voice rules. In the Agency profile, read the active client's voice from Clients/{slug}/ and write in that voice, never the agency's.
2. Resolve the source. If it points at a lesson, read the line in Memory/lessons.md. If it cites a result or metric, read the matching row in Memory/kpi-ledger.md and use the exact numbers and source. If it names an offer, read Company/offers.md. Never invent a metric, a quote, or a claim.
3. Read Company/icp.md to fix the reader: who they are, what they want, what they already tried.
4. Pick one idea. One post carries one idea and one call to action. Cut everything that is not that idea.
5. Write the hook as the first line. Make line one earn line two: a number, a sharp claim, a named mistake, or a question the reader is already asking. No throat-clearing.
6. Write the body: 4 to 10 short lines, one thought per line, white space between beats. Lead with the specific, back it with the number or the example, then the takeaway.
7. Write one call to action: comment a word, reply for the file, book a slot, read the case study. Pick one and only one.
8. Write two variants of the full post that keep the same idea and call to action but change the angle: variant A leads with the hard number or result, variant B leads with the story or the mistake. Each variant gets its own hook.
9. Pass each post through the voice rules: numbers over adjectives, verbs over nouns, terse lines, no banned words, no em-dashes. Rewrite any line that fails.
10. Mark the file confidential:true in the front matter for the Agency profile (a client deliverable). Solo and Team leave it standard.
11. If you cited a metric that has moved since its last ledger row, append a new row to Memory/kpi-ledger.md. Never edit a prior row.

## Outputs
- Content/{slug}-{date}/final/linkedin-post.md: the main hook-first post plus variant A and variant B, each labeled, each ready to copy. Front matter records the source, the voice used, and (Agency) confidential:true.
- Content/{slug}-{date}/brief.md: one block recording the source, the reader, the single idea, and the call to action, so the post is traceable.
- Memory/kpi-ledger.md: one appended row only when a cited metric has moved since its last row (columns: date, metric, baseline, current, target, source, confidence, note).

## Guardrails
- Draft only. Never post, publish, schedule, or send. The human posts.
- One idea, one call to action per post. If it needs two, it is two posts.
- Voice comes from Library/styles/brand-voice.md (Agency: the client's voice). Never the model's default voice.
- Provenance: cite the source for every number and every quote. Never invent a metric, a result, or a testimonial.
- Agency firewall: read only the active client. Never read a sibling client. Client outputs carry confidential:true.
- No em-dashes, no banned words. Numbers, not adjectives.

## References
- Library/styles/brand-voice.md
- Memory/lessons.md
- Memory/kpi-ledger.md
- Company/offers.md
- Company/icp.md
