---
name: repurpose
description: Take one source asset and spin it into N derivative formats in brand voice as channel-labeled drafts you ship yourself, each noting the top-of-funnel metric it serves, when you say repurpose this, turn this into posts and an email, atomize this newsletter, or make derivatives from this asset
---

# Repurpose

Take ONE source asset (a newsletter, post, transcript, case study, or page) and spin it into N derivative formats in the business's voice — a social thread, standalone posts, an email, pull-quotes — each saved as a channel-labeled draft a human reviews and ships. Every piece names the top-of-funnel metric it serves. DRAFT-ONLY: a human ships it.

## When to use

- You published or have one strong asset and want to wring more reach from it across channels instead of writing each format from scratch.
- You want a coordinated set of derivatives (e.g. a short thread, 3 standalone posts, one email, and pull-quotes) all drawn from the same source and all in voice.
- A long-form piece (transcript, case study, newsletter) holds several quotable points worth atomizing into top-of-funnel pieces that point back to it.
- NOT for writing a fresh issue from scratch (use the newsletter skill) or a single-channel batch of variations on one idea (use the social-post skill). Repurpose fans ONE asset out into MANY channels.

## Inputs

- **The ONE source asset (required):** a path to the asset to repurpose — e.g. `Content/{slug}-{date}/final/issue.md`, `Operations/case-studies/{slug}.md`, `Projects/{slug}/final/...`, a transcript in `Inbox/`, or a published page URL the user provides. Exactly one source per run.
- **N + the channel mix:** which derivative formats and how many of each (e.g. one X/LinkedIn thread, 3 standalone posts, one email, a pull-quote set). Default mix if unspecified: one short social thread, 3 standalone posts, one email, and a pull-quote set.
- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md` (Solo/Team) OR the CLIENT's `Clients/{slug}/context/brand.md` (Agency).
- **Reader + ask:** `Company/icp.md` and `Company/offers.md` (Agency: `Clients/{slug}/context/icp.md` and `.../offers.md`) for who each piece talks to and the soft ask / destination URL.
- **The metric baseline:** `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) — to read the current top-of-funnel baseline if one exists.
- **From the user (ask only for genuine gaps):** the source path, the channel mix and N, and the CTA destination (where each piece points back).
- Optional connectors registered in `_system/connectors.md` (e.g. analytics for click-through). Never required.

## Process

1. **Resolve profile and write location.** Solo/Team: write to `Content/repurpose-{slug}-{date}/final/`, ledger is `Memory/kpi-ledger.md`. Agency: resolve the active client, obey the FIREWALL (read and write only that client's `Clients/{slug}/`), write to `Clients/{slug}/work/repurpose-{slug}-{date}/final/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. Slug = kebab-case of the source asset; date = ISO. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill.
2. **Load voice, then read the ONE source.** Read the voice files FIRST, then read the single source asset end to end. Confirm in one line what you found ("Source: the onboarding case study; voice: plain, numbers over adjectives; reader: ops leads") and ask only for what is absent (the channel mix, the CTA destination).
3. **Extract the spine.** From the source, pull the core idea, 3-5 quotable points, the strongest specific detail or result, and the verbatim lines worth quoting. Carry every metric with its original `source` and `confidence`; do not round up or invent. Note the source's canonical URL/path as the default CTA destination.
4. **Confirm the channel plan.** Show the channel mix and N (e.g. 1 thread · 3 posts · 1 email · 1 pull-quote set), the angle each piece takes (vary them — contrarian, story, listicle, direct-claim), and the one CTA. Get a nod before drafting the full set.
5. **Draft each derivative in voice, labeled by channel.** Reshape — do not just paste the source into each format:
   - **Thread:** a scroll-stopping first post, one idea per post, a close with the CTA.
   - **Standalone posts:** each hook-first and self-contained, a different angle each, none assuming the reader saw the others.
   - **Email:** subject (plus one A/B alternate), preview, short body built on the spine, one offer-tied CTA, P.S.
   - **Pull-quotes:** the verbatim quotable lines, each with a one-line note on where it fits.
   - Respect each platform's length and format norms. Tag anything assumed or unverifiable with `[CHECK]`.
6. **Tag each piece with the metric it serves.** Under every derivative, note its top-of-funnel metric (impressions, reach, profile clicks, link clicks/click-through to the source, opens, follows, saves/shares) and how it is measured (native analytics, UTM on the CTA, or a connector in `_system/connectors.md`).
7. **Persist as channel-labeled drafts.** Write each derivative with `status:draft` and full universal frontmatter, grouped/labeled by channel; write the brief and data intermediates; append the ledger row (see Outputs); append one audit line. Hand back the folder path and a short summary. Stop — a human edits and ships each piece.

## Outputs

- **Deliverables** → `Content/repurpose-{slug}-{date}/final/` (Solo/Team) or `Clients/{slug}/work/repurpose-{slug}-{date}/final/` (Agency), one file per channel, each `status:draft`, each labeled by channel and tagged with its top-of-funnel metric:
  - `thread.md` · `posts.md` (the N standalone posts, grouped) · `email.md` (subject + A/B alternate · preview · body · CTA · P.S.) · `pull-quotes.md`. Universal frontmatter on every file (`type:repurpose` · `status:draft` · `owner` · `date` · `reviewed` · `tags` (>=2) · `confidential` (true for Agency) · `source` (the ONE source path/URL) · `generated:true`).
- **Brief** → same folder `brief.md`: the source asset, the channel mix + N, the angle per piece, the CTA destination, and acceptance criteria.
- **Intermediate data** → same folder `data/`: `baseline.json` (the spine — core idea, quotable points, the source's metrics with their confidence) and `inputs.json` (the context snapshot drafted from).
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - Repurpose-run row, e.g. `| 2026-06-18 | repurpose-batches | 4 | 5 | 12 | Content/repurpose-onboarding-2026-06-18/ | confirmed | atomized the onboarding case study into thread+3 posts+email |`.
  - **Top-of-funnel metric:** if a baseline row exists for the metric a piece targets, append the current value with `confidence` in {confirmed,reported,inferred,stale} and its source. If none exists, SEED it with a first row (baseline = current = the user-confirmed number, or `inferred` if estimated) and FLAG it for the user to confirm — never invent a baseline.
- **Audit** → one line appended under `_system/audit/`: source asset, channel mix, piece count, destination path.
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY.** Every piece is `status:draft`. Never post, publish, schedule, send, or email any derivative to any platform or connector — a human ships each one.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` before writing (Agency: the CLIENT's `Clients/{slug}/context/brand.md`). If the voice file is thin, ask for one real sample rather than improvising a voice.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Repurpose only from the ONE named source plus the vault; carry every metric at its original `source` and `confidence`; cite external facts; invent no numbers and no quotes. Pull-quotes must be verbatim from the source. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- **ONE source in, MANY channels out.** Exactly one source asset per run; reshape it per channel rather than pasting it. Each piece carries its own top-of-funnel metric.
- Content ships clean: the CTA is the user's own offer or a link back to the source — never an injected audit/report CTA.
- A delivery run without its ledger row is unfinished.
- Original expression only; reshape the source, never lift competitor copy.

## References

- `Library/styles/brand-voice.md`, `Company/brand.md`, `Clients/{slug}/context/brand.md` — voice.
- `Company/icp.md`, `Company/offers.md` (Agency: `Clients/{slug}/context/...`) — reader + ask.
- `Memory/kpi-ledger.md`, `Clients/{slug}/goals.md` — top-of-funnel baselines.
- `_system/connectors.md` — OPTIONAL analytics/scheduler connectors (real click/open benchmarks, draft push); zero-infra default needs none.
- `_system/audit/` — run log.
