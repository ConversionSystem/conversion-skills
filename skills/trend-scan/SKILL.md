---
name: trend-scan
description: Research what people are actually saying about a topic, competitor, or market over the last N days across public communities and rank it by engagement, triggers "trend scan", "what are people saying about X", "scan the market", "X vs Y sentiment", "what's the buzz on", "community research"
---

# Trend Scan

## When to use
- You want to know what real people are saying about a topic, competitor, or market right now, not what editorial pages claim.
- You need primary community signal (Reddit, Hacker News, YouTube, X, GitHub, prediction markets) before writing content, planning SEO, researching leads, or sizing an ad competitor.
- You want a head-to-head read on two entities (X vs Y) backed by what each one's community is actually posting.
- You need a dated, cited record of community sentiment to compare against a later scan.

## Inputs
- Topic, competitor, or market to scan (one entity, or two for comparison mode).
- Window in days: 7, 30 (default), or 90.
- Mode: single (default) or comparison (X vs Y).
- Optional focus angle (pricing, reliability, hiring, a specific feature).
- Active client slug if running under the agency firewall (writes to that client only).
- Optional connectors registered in `_system/connectors.md` for deeper or higher-volume sources. Absent connectors, the scan runs zero-infra on WebSearch and WebFetch.

## Process
1. Resolve scope. Read `Company/profile.md`, `Company/competitors.md`, and `Company/strategy.md` for context. If a client slug is set, read `Clients/{slug}/` for the active client only and never a sibling. Confirm the entity, the window (default 30 days), and the mode (single or comparison).
2. In comparison mode, resolve each entity separately first (canonical name, handles, subreddits, GitHub org, ticker or market where relevant), then run steps 3 to 6 once per entity before merging.
3. Check `_system/connectors.md`. If a community connector is registered (for example a higher-volume search or social API), use it. If not, run the zero-infra default: WebSearch and WebFetch scoped to each platform.
4. Gather per platform, filtered to the window:
   - Reddit: WebSearch `site:reddit.com {entity} {window terms}`, fetch top threads, capture subreddit, upvotes, comment counts, top comments.
   - Hacker News: WebSearch `site:news.ycombinator.com {entity}`, fetch threads, capture points and comment volume.
   - YouTube: WebSearch for recent videos, capture title, channel, view and comment signals from the visible page.
   - X: WebSearch and WebFetch public posts, capture reposts, likes, replies where shown.
   - GitHub: WebSearch issues, discussions, and repos, capture stars, issue volume, recency.
   - Prediction markets: WebSearch Polymarket, Kalshi, Manifold for any market tied to the entity, capture current odds and volume.
5. Rank by engagement. Score each item on its platform's native signal (upvotes, points, reposts, likes, stars, view and comment signals, market volume). Normalize within platform, then surface the highest-signal items overall. Record the source URL and the metric for every item; never invent a number.
6. Cluster the same story across platforms. Group items that describe the same event, complaint, launch, or claim into one theme even when they sit on different platforms. Name each cluster in plain language and note which platforms carried it and how loud each was.
7. Synthesize. For each major theme, write what people are saying, weave in 2 or more verbatim community quotes with attribution (handle or username, platform, date, link), then state the pattern and the implication for the business. In comparison mode, merge the per-entity themes into a head-to-head with a short verdict per dimension.
8. Write the deliverable. Create `Projects/trend-scan-{slug}-{date}/` (under the active client if a slug is set) and write `findings.md` with the sections below. Append one ledger row to `Memory/kpi-ledger.md`.

## Outputs
- `Projects/trend-scan-{slug}-{date}/findings.md` containing:
  - Scope: entity or entities, window, mode, date, platforms scanned, connectors used or "zero-infra".
  - Top signals: the highest-engagement items, each with platform, metric, and link.
  - Themes: clustered stories, each with what people are saying, 2 or more attributed verbatim quotes, the pattern, and the implication.
  - Comparison table (comparison mode only): head-to-head per dimension with a per-dimension verdict.
  - Implications for the business: 3 to 5 concrete reads, each tied to its sources.
  - Feeds: a short note on which skills to hand this to next (content-plan, seo-content, lead-research, ads-competitor).
  - Sources: every URL cited, grouped by platform.
- `Projects/trend-scan-{slug}-{date}/sources.md` listing all fetched URLs with their captured metric and fetch date.
- Ledger row appended to `Memory/kpi-ledger.md`:
  `| {date} | trend-scan-items-{slug} | {prior count or 0} | {items ranked} | {target or n/a} | Projects/trend-scan-{slug}-{date}/findings.md | reported | window {N}d, {platforms} |`

## Guardrails
- Draft only. Never send, publish, post, or contact anyone. The deliverable is research for the user to act on.
- Agency firewall: when a client slug is set, read and write that active client only, never a sibling client.
- Cite every claim with a source URL. Never invent a quote, a username, a metric, or an engagement number. If a metric is not visible, mark it "not shown" rather than guessing.
- Quotes must be verbatim and attributed (handle, platform, date, link). Do not paraphrase a quote and present it as a quote.
- Mark each item's confidence as confirmed, reported, inferred, or stale in line with what the source supports. Community engagement counts are reported, not confirmed.
- Respect the window. Drop items outside the requested N days, or label them clearly as older context.
- Connectors are optional. If none are registered, run the zero-infra default and say so. Never block on a missing connector.

## References
- `_system/connectors.md` for optional source connectors and their scope.
- `Company/profile.md`, `Company/competitors.md`, `Company/strategy.md` for entity and market context.
- `Clients/{slug}/` for active-client context under the agency firewall.
- `Memory/kpi-ledger.md` for the append-only metric ledger.
- `Library/styles/brand-voice.md` for the synthesis voice.
- Feeds content-plan, seo-content, lead-research, and ads-competitor.
