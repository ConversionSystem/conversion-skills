# Orchestration

Some Conversion Skills are orchestrators: they spawn specialist subagents in parallel, merge the findings, and run the judge before anything ships. The pattern keeps a fan-out honest instead of merely plausible.

## The pattern
1. **Gather once.** The orchestrating skill collects the raw signals (fetched pages, exports, ledger rows) into the deliverable's `data/` folder.
2. **Fan out.** It spawns specialists, one per lens or one per client, each reading only its slice. Specialists run in parallel and return structured findings. They never write the final report.
3. **Merge.** The main skill (never a specialist) assembles the findings into one scorecard. Specialists never call specialists.
4. **Judge.** The `judge` agent tries to refute each finding against its cited evidence. Thin or uncited findings are cut.
5. **Decide.** The skill writes the draft report and, for a gate-style audit, a GO or NO-GO.

## The roster
- **judge** · adversarial reviewer, refutes a claim before it ships. Used by every client-facing skill.
- **seo-audit-{technical, onpage, performance, architecture}** · the four SEO lenses, spawned by `seo-audit`.
- **ads-audit-{google, meta, platforms}** · the paid-media lenses, spawned by `ads-audit`.
- **portfolio-client** · one per client, spawned by `portfolio-watch`. Reads only its client (the firewall, enforced).

## The rules
- The **main skill merges**. Specialists return findings and stop. Personas never call personas (no loops).
- **Cite or it does not exist.** Every finding names a URL, a file, or a ledger row. The judge cuts the rest.
- **Draft-only.** Orchestrators diagnose and recommend. A human applies, sends, or publishes.
- **Firewall.** A per-client specialist reads only its assigned client, never a sibling.

## Which skills orchestrate
- `seo-audit`, `ads-audit`, `site-audit` · fan out to lens specialists, then judge.
- `portfolio-watch` · fans out to one `portfolio-client` per client.
- `free-audit`, `case-study`, `business-review` · run the judge on every claim before it reaches a client.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
