---
name: title-generation
description: Generate click-optimized title variants for a video, post, or page with the angle each takes and the one to test first, triggered by /title-generation, "write titles", "headline options", or "what should I call this"
---

# Title Generation

Draft a set of titles for a video, post, or page, optimized for the click against a named target audience, with the angle each variant takes and a clear pick to test first.

## When to use
- A piece of content (video, blog post, landing page, email subject) needs a title and you want options, not one guess.
- A published piece is under-performing on click rate and you want fresh angles to test.
- You have a working title but want to pressure-test it against alternatives before locking it.

## Inputs
- The content itself or a tight summary: topic, the promise, the payoff a reader gets.
- Target audience. Pull from `Company/icp.md`. For an agency client, pull from `Clients/{slug}/icp.md` instead.
- Surface and format: YouTube title, blog H1, landing-page hero, email subject line. Each has a different length budget and click logic.
- Voice rules from `Library/styles/brand-voice.md`. For an agency client, the client's voice from `Clients/{slug}/brand-voice.md`.
- Optional: a working title, past winners, or a list of words the brand avoids.

## Process
1. Read the inputs. Confirm surface, format, and length budget (YouTube around 60 characters before truncation, email subject around 40, blog H1 flexible). If the audience is thin, read `Company/icp.md` (or `Clients/{slug}/icp.md` for an agency client) and name the one reader you are writing to.
2. Name the core promise in one sentence: what the reader gets and why they should care now. Everything keys off this.
3. List 5 to 7 angles to attack the click from. Cover a spread, for example: the specific outcome, the named pain, the number or proof, the contrarian take, the curiosity gap, the "how to" direct, the status or identity hook. Note which angles fit the audience and which feel forced.
4. Draft 10 to 14 title variants across those angles. Keep each inside the length budget. Use numbers over adjectives, verbs over nouns. Honor the brand voice and the avoid-words list. No clickbait the content cannot pay off.
5. Tag every variant with its angle and a one-line read on who it pulls and what it risks.
6. Score each on a 1 to 5 click pull and a 1 to 5 honesty-to-content. Drop anything that scores high on pull but low on honesty.
7. Pick one to test first. Say why it wins for this audience on this surface, and name the runner-up to test against it.
8. Write the file. For Solo or Team, write to `Content/{slug}-{date}/final/titles.md` when the piece lives in `Content/`, or to `Projects/{slug}/final/titles.md` when it lives in `Projects/`. For an agency client, write to `Clients/{slug}/Projects/{project}/final/titles.md` with `confidential: true` in the frontmatter.
9. If this title replaces a live one and you have a click-rate baseline, append one row to `Memory/kpi-ledger.md` recording the metric, baseline, and target. Never edit a prior row.

## Outputs
- A titles file at `Content/{slug}-{date}/final/titles.md` or `Projects/{slug}/final/titles.md` (Solo or Team), or `Clients/{slug}/Projects/{project}/final/titles.md` with `confidential: true` (Agency). It contains: the core promise, the angle list, the scored variants with their tags, the pick to test first with the runner-up, and the source of the audience read.
- One appended row in `Memory/kpi-ledger.md` only when a live title is being replaced and a click-rate baseline exists, using the exact columns: | date | metric | baseline | current | target | source | confidence | note |.

## Guardrails
- Draft only. Never publish, schedule, or push a title live. Hand the file to the user.
- Every variant must be payable by the actual content. If the title promises a number, a result, or a claim, the content has to deliver it. No invented metrics or quotes.
- Voice comes from `Library/styles/brand-voice.md` (the client's voice for an agency client). Honor the avoid-words list.
- Agency firewall: read only the active client. Never read a sibling client's folder. Client outputs carry `confidential: true`.
- Provenance: cite where the audience read came from. When a metric moves because a title changed, append a ledger row, never overwrite one.

## References
- `Company/icp.md` and `Library/styles/brand-voice.md` (Solo or Team)
- `Clients/{slug}/icp.md` and `Clients/{slug}/brand-voice.md` (Agency)
- `Memory/kpi-ledger.md`
