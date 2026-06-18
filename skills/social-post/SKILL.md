---
name: social-post
description: Draft hook-first social posts in brand voice as N variants per platform from an idea, lesson, published asset, or metric win, written as drafts you ship yourself when you say draft a social post, write a LinkedIn post, turn this into posts, or make social variants
---

# Social Post

Turn a single source into hook-first social post variants in the business's voice, saved as drafts a human reviews and posts. Every batch ties to a top-of-funnel metric and records how that metric is measured.

## When to use
- You have a raw idea, angle, or hot take and want it shaped into posts.
- You want to amplify a lesson from `Memory/lessons.md` into social-ready language.
- You published an asset (blog post, case study, newsletter, landing page) and want top-of-funnel posts that drive back to it.
- A metric moved (a win, a milestone, a result) and you want to talk about it without inventing numbers.
- You need several angles to A/B or to schedule across a week, per platform.

## Inputs
- Source (one of): a plain idea/angle from the user; a lesson reference like `Memory/lessons.md#some-lesson`; a published asset path (e.g. `Content/{slug}-{date}/final/...`, `Operations/case-studies/...`, `Projects/{slug}/final/...`); or a metric win (point at the ledger row).
- Platforms requested (e.g. LinkedIn, X, Threads, Instagram caption). Default to LinkedIn + X if unspecified.
- N = variants per platform. Default N=3.
- Voice files: `Library/styles/brand-voice.md` + `Company/brand.md` (Solo/Team) OR `Clients/{slug}/context/brand.md` (Agency).
- Optional: target audience from `Company/icp.md` (or `Clients/{slug}/context/icp.md`), the CTA/destination URL, and any existing `Content/{slug}-{date}/brief.md`.
- Optional connectors registered in `_system/connectors.md` (e.g. analytics for follow-through rate). Never required.

## Process
1. Confirm scope: which source, which platforms, and N variants per platform. If the user only gave a vague idea, restate it as a one-line angle and proceed.
2. Load voice FIRST. Solo/Team: read `Library/styles/brand-voice.md` then `Company/brand.md`. Agency: read `Clients/{slug}/context/brand.md` for the ACTIVE client only and write in the CLIENT's voice. Pull audience cues from the relevant `icp.md` if present.
3. Resolve the source into raw material:
   - Idea: use the angle as-is; do not embellish with facts.
   - Lesson: read the referenced block in `Memory/lessons.md` and carry its claim and any cited source.
   - Published asset: read the asset, extract 3-5 quotable points, and note its canonical URL/path as the CTA destination.
   - Metric win: read the exact ledger row (`Memory/kpi-ledger.md` Solo/Team, or `Clients/{slug}/goals.md` Agency). Use ONLY the numbers in that row, with its `source` and `confidence`. Never round up, never invent a metric.
4. Pick the destination folder. Reuse the source's `Content/{slug}-{date}/` if it came from one; otherwise create `Content/{slug}-{date}/` with a kebab-case slug and ISO date. Agency: nest under the active client only if your taxonomy firewalls there; otherwise keep client work confidential per the firewall rule.
5. Choose the top-of-funnel metric this batch targets (e.g. impressions, profile clicks, reach, link clicks/click-through to the asset, follows, saves/shares). State how it is measured and where (native platform analytics, UTM on the CTA link, or a connector in `_system/connectors.md`).
6. Draft N variants per platform, each hook-first:
   - Line 1 is a scroll-stopping hook (no throat-clearing, no "I'm excited to share").
   - Body delivers one idea with a concrete proof point or specific detail; respect platform length and format norms.
   - End with one clear CTA tied to the chosen metric (read, reply, follow, click) and the destination URL when applicable.
   - Vary the angle across variants (contrarian, story, listicle, direct-claim) rather than rewording the same hook.
   - Keep all external facts and any metric strictly to what step 3 surfaced; mark anything assumed with a `[CHECK]` tag.
7. Write the output file(s) with full frontmatter and `status:draft`. Group variants per platform under clear headings; label each variant with its angle and the hook.
8. If a metric win seeded the batch, confirm the ledger already holds that row; do not duplicate it. Append a ledger row ONLY when this skill establishes or moves a baseline (e.g. you set the top-of-funnel target for this campaign and it was not recorded before).
9. Append a one-line entry to `_system/audit/` noting source, platforms, variant count, and destination path.
10. Hand back the path and a short summary. Stop. A human edits and posts.

## Outputs
- `Content/{slug}-{date}/final/social-posts.md` (Solo/Team) OR the active client's firewalled `Clients/{slug}/.../social-posts.md` (Agency) · all variants, grouped by platform, each `status:draft`, with full universal frontmatter (`type:social-post`, `status:draft`, `owner`, `date`, `reviewed`, `tags` (>=2), `confidential` (true for Agency client work), `source` (the resolved source path/ref), `generated:true`).
- `Content/{slug}-{date}/brief.md` if none existed: records the source, chosen platforms, N, the top-of-funnel metric, and how it is measured.
- Ledger row (only if a baseline/target is newly set), appended to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), exact columns: `| date | metric | baseline | current | target | source | confidence | note |`. Append-only; never edit prior rows.
- Audit line appended under `_system/audit/`.

## Guardrails
- DRAFT-ONLY: every variant is `status:draft`. Never post, publish, schedule, or send to any platform or connector. A human ships it.
- VOICE: load voice files before writing; Solo/Team uses the business voice, Agency uses the CLIENT's voice from `Clients/{slug}/context/brand.md`.
- FIREWALL (Agency): write only into the ACTIVE client's workspace; never read a sibling client; client outputs are `confidential:true`.
- PROVENANCE: cite the source for any external fact; never invent metrics. Use only the numbers in the referenced ledger row, at its stated confidence. Tag unverified claims `[CHECK]`.
- LEDGER: append-only with the exact columns; never edit or reorder prior rows. Only append when a baseline or target is genuinely set or moved.
- Route to canonical homes; kebab-case slugs; ISO dates.

## References
- `Library/styles/brand-voice.md`, `Company/brand.md`, `Clients/{slug}/context/brand.md`
- `Memory/lessons.md`, `Memory/kpi-ledger.md`, `Clients/{slug}/goals.md`
- `Company/icp.md` (or `Clients/{slug}/context/icp.md`), `_system/connectors.md`, `_system/audit/`
