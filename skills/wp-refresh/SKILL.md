---
name: wp-refresh
description: Refresh a decayed published post by fetching the live URL and diffing it against current company truth, newer ledger numbers, broken links, and outdated claims, then producing an updated draft and staging it as a WordPress draft revision when triggered by "refresh this post", "update an old article", "this post has gone stale", or "wp refresh"
---

# WordPress Refresh

Revive an existing published post that has decayed. Fetch the live page, diff it against current truth, and produce an updated draft of what to change plus the rewritten sections — never overwriting live automatically.

## When to use
- A published post has lost rankings, traffic, or conversions and you suspect content decay.
- Company facts, offers, pricing, or positioning have moved since the post was written.
- The post cites metrics, dates, or claims that are now stale, or links that now 404.
- Search intent for the target query has drifted and the post no longer matches it.
- You want a tracked, reviewable refresh draft before a human re-publishes.

## Inputs
- The live post URL (required). If only a slug or title is given, ask for the URL.
- `Company/profile.md`, `Company/brand.md`, `Company/offers.md`, `Company/icp.md`, `Company/strategy.md` — current truth to diff against.
- `Library/styles/brand-voice.md` + `Company/brand.md` — voice. Agency: `Clients/{slug}/context/brand.md`.
- `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) — newer numbers that may update stale figures in the post.
- Any existing `Content/{slug}-{date}/` folder and `data/baseline.json` for this post, if one exists from a prior publish.
- `_system/connectors.md` — to learn whether a wordpress connector is enabled and configured.

## Process
1. **Resolve scope.** Confirm the live URL. Derive a kebab-case `{slug}` from the post (reuse the existing content slug if a `Content/{slug}-*/` folder already exists; otherwise create one). Set `{date}` to today (ISO). Determine profile: Solo/Team vs Agency. Agency: confirm the ACTIVE client and operate only inside `Clients/{slug}/`.
2. **Fetch live.** Web-fetch the live URL. Capture the current title, headings, body, internal/external links, publish/update date, and any embedded metrics or claims. Save the captured snapshot to `Content/{slug}-{date}/data/live-fetch.md` with `source` set to the URL.
3. **Load current truth.** Read the Company context files and the ledger (or client `goals.md`). Build a short list of facts the post must now reflect: current offers, pricing, positioning, named results, product names.
4. **Diff against truth.** Produce a decay report covering: (a) outdated claims/metrics that disagree with current truth, (b) stale ledger numbers — replace only with values whose `confidence` is `confirmed` or `reported`, never `inferred`/`stale`, (c) broken or redirected links (test each external link via web fetch; flag non-200s), (d) intent drift — does the post still answer the query it targets, (e) freshness gaps — missing recent developments. Cite a source for every external fact; never invent metrics.
5. **Write the updated draft.** In the business's voice (Agency: the client's voice), write the refreshed sections — rewritten intro, updated stats with inline sources, fixed links, new/expanded sections, and a revised title/meta if intent drifted. Produce a clear change list (what to change and why) alongside the rewritten copy so a human can review the delta, not just the result.
6. **Stage the connector update (optional).** Read `_system/connectors.md`. If a wordpress connector is enabled, stage the refresh as a WordPress DRAFT or pending revision against the existing post — never push it live and never overwrite the published version. If no connector is enabled, note that the refresh is file-only and a human applies it manually. Record what was staged in `_system/audit/`.
7. **Update the ledger.** If a content-performance baseline exists for this post (`Content/{slug}-{date}/data/baseline.json` or a prior ledger row), append one ledger row noting the refresh. Never edit or reorder prior rows.

## Outputs
- `Content/{slug}-{date}/brief.md` — `status:draft`. The decay diagnosis and refresh scope.
- `Content/{slug}-{date}/data/live-fetch.md` — `generated:true`. Captured snapshot of the live post, `source` = live URL.
- `Content/{slug}-{date}/final/refresh.md` — `status:draft`. The change list plus the rewritten sections, in voice, with sources cited inline. Agency: written to `Clients/{slug}/...` mirror under the active client and marked `confidential:true`.
- Connector (optional, if enabled): a WordPress DRAFT/revision staged against the existing post; an audit note in `_system/audit/`.
- Ledger: if a content-performance baseline exists, one appended row in `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency): `| {date} | post-refresh:{slug} | {baseline} | {current} | {target} | {live URL} | {confidence} | refreshed decayed post |`.

## Guardrails
- DRAFT-ONLY: all outputs are `status:draft`. Never publish, never overwrite the live post, never push live. A connector may stage a WordPress DRAFT/revision only; a human approves and publishes the refresh.
- VOICE: load `Library/styles/brand-voice.md` + `Company/brand.md` (Agency: `Clients/{slug}/context/brand.md`) before writing; match the business's voice.
- FIREWALL (Agency): operate only inside the ACTIVE client's `Clients/{slug}/` workspace; never read a sibling client; client outputs are `confidential:true`.
- PROVENANCE: cite a source for every external fact and every replaced metric. Never invent numbers. Only adopt ledger values with `confidence` of `confirmed` or `reported`.
- Every `.md` written carries the universal frontmatter: type, status, owner, date, reviewed, tags (>=2), confidential, source, generated.
- Route outputs to canonical homes; kebab-case slugs; ISO dates. Append ledger rows only — never edit prior rows.

## References
none
