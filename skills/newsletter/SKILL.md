---
name: newsletter
description: Draft one newsletter issue in brand voice from recent wins, lessons, and content, built on a single clear idea and a teardown or specific story with one offer-tied CTA, written to Content as a draft - triggers on /newsletter, "write a newsletter", "draft this week's newsletter", "newsletter issue", "broadcast email to my list", "email my subscribers", "monthly update"
---

# Newsletter

Drafts one send-ready newsletter issue around a single idea, told through a teardown or a specific story (more valuable than a tips list), in the business's voice and grounded in real material from the vault. DRAFT-ONLY: a human ships it.

## When to use

- You want to send a periodic broadcast to your whole list (this week's issue, the monthly update) and want it drafted from real wins, lessons, and recent content rather than filler.
- You have a specific story, teardown, or result worth one issue and one clear takeaway.
- NOT for automated triggered flows (welcome, nurture, drip) - use the email-sequence skill for those. Pairs with the repurpose skill (turn an issue into social posts, or a strong post into an issue).

## Inputs

- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md`. Agency profile: the CLIENT's `Clients/{slug}/context/brand.md` instead.
- **Reader:** `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`).
- **The one CTA / soft ask:** `Company/offers.md` (Agency: `Clients/{slug}/context/offers.md`).
- **Substance (real material only):** recent `Daily/` notes, `Memory/lessons.md`, `Memory/decisions/`, `Operations/case-studies/`, and shipped `Content/` issues - the actual wins, lessons, and stories to build the issue on.
- **The metric baseline:** `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) - to read the current subscriber/open baseline if one exists.
- **From the user (ask only for genuine gaps):** the one idea or story, the send date, and which offer the CTA points to.

## Process

1. **Resolve profile and write location.** Solo/Team: write to `Content/{slug}-{date}/final/`, ledger is `Memory/kpi-ledger.md`. Agency: resolve the active client, obey the FIREWALL (read only that client's `Clients/{slug}/`), write to `Clients/{slug}/work/{slug}-{date}/final/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill.
2. **Load voice, then context.** Read the voice files first, then ICP, offers, and the source material. Confirm in one line what you found ("Voice: plain, numbers over adjectives; reader: ops leads at 20-100-person agencies; CTA: the free audit") and ask only for what is absent (the idea, the send date).
3. **Pick the ONE idea.** One issue = one clear idea. If two topics compete, cut one or hold it for next time.
4. **Choose the vehicle - teardown or specific story over a tips list.** Build the body as either a teardown (walk through one real thing and what it shows) or a specific story (a short narrative to one transferable lesson). A generic listicle is the fallback only when no real story or teardown exists; prefer concrete over generic every time.
5. **Outline and confirm.** Show the subject angle, the section skeleton, and the single CTA before writing the full draft. One issue, one primary CTA.
6. **Draft in voice.** Write subject (plus one A/B alternate), preview text that extends the subject, the body (teardown or story), one CTA tied to `Company/offers.md` (Agency: the client's offers), and a P.S. that earns the next open. Every number real and traceable to its source; invent no results and no list sizes.
7. **Instrument.** Add a `## Metrics to track` block: open rate (driven by the subject) and clicks (driven by the one CTA), each with a benchmark band and the one decision it drives.
8. **Persist as a draft.** Write the deliverable with `status:draft` and full universal frontmatter, write the data intermediates, and append the ledger row (see Outputs). Close with the next action (a human schedules the send; pair with the repurpose skill).

## Outputs

- **Deliverable** → `Content/{slug}-{date}/final/issue.md` (Solo/Team) or `Clients/{slug}/work/{slug}-{date}/final/issue.md` (Agency), `status:draft`, with: subject + A/B alternate · preview · body (teardown or story) · one offer-tied CTA · P.S. · `## Metrics to track`. Universal frontmatter on the file (type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated). Agency files are `confidential:true`.
- **Brief** → same folder `brief.md`: idea, audience, send date, the one action, acceptance criteria.
- **Intermediate data** → same folder `data/`: `baseline.json` (idea/themes covered + the KPI) and `inputs.json` (the context snapshot drafted from).
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - Issue-shipped row, e.g. `| 2026-06-18 | newsletter-issues | 12 | 13 | 24 | Content/{slug}-2026-06-18/ | confirmed | June issue, the onboarding teardown |`.
  - **Subscribers/opens:** if a baseline row exists, append the current value with `confidence` in {confirmed,reported,inferred,stale} and its source. If none exists, SEED the metric with a first row (baseline = current = the user-confirmed number, or `inferred` if estimated) and FLAG it for the user to confirm - never invent a baseline.
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY.** Produce `status:draft`. Never send, schedule, publish, or email the issue autonomously - a human ships it.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` before writing (Agency: the CLIENT's `Clients/{slug}/context/brand.md`). If the voice file is thin, ask for one real sample rather than improvising a voice.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Every result, story detail, and list size is real and traceable to `goals.md`/`Memory/`/`Daily/` or a user-named source; cite external facts; invent no metrics. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- One idea, one primary CTA per issue. A teardown or specific story beats a tips list.
- Content ships clean: never append an audit/report CTA into the issue body; the CTA is the user's own offer.
- A delivery run without its ledger row is unfinished.
- Original expression only; no lifted newsletters or competitor copy.

## References

- `references/structure.md` - issue skeletons (teardown, story+lesson, update/launch, roundup).
- `_system/connectors.md` - OPTIONAL ESP/list connectors (real open/subscriber benchmarks, draft push); zero-infra default needs none.
