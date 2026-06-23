---
name: web-vitals
description: Audit a live page's Core Web Vitals, page weight, mobile responsiveness, image optimization, and accessibility basics, then write a prioritized fix list tied to a conversion metric. Triggers on /web-vitals, "web vitals", "audit page performance", "LCP INP CLS", "page speed audit", "is this page slow".
---

# Web Vitals

## When to use
- A live page feels slow, janky, or converts below its traffic, and you need runtime evidence, not guesses.
- You want Core Web Vitals (LCP, INP, CLS) plus page weight, render-blocking resources, mobile fit, image hygiene, and accessibility basics in one pass.
- site-audit spawned this skill as a performance and accessibility lens.
- You need the runtime experience the seo-* skills miss; they read HTML, this measures what a browser does with it.

Do not use to rewrite the page or push fixes live. This skill is draft only. For HTML-level meta, headings, and crawlability, use the seo-* skills.

## Inputs
- Target URL (required). If the active context is a client engagement, the page belongs to the active client only, never a sibling.
- A measured-signals source, when available: the Preview connector or a Chrome DevTools connector listed in `_system/connectors.md`. Check there first.
- Company/strategy.md and Company/offers.md for the conversion metric this page is meant to move (signup, demo, purchase, lead).
- Any prior audit in `Projects/web-vitals-{domain}-{date}/` to chart against.
- Target thresholds if the team has set them; otherwise use the standard good marks (LCP under 2.5s, INP under 200ms, CLS under 0.1).

## Process
1. Resolve `{domain}` from the URL host (strip `www.`, keep the registrable name, e.g. `acme.com`) and `{date}` as today in YYYY-MM-DD. Create `Projects/web-vitals-{domain}-{date}/` with a `final/` subfolder. Agency: the project lives under the active client's workspace, not the root.
2. Check `_system/connectors.md` for a registered browser or DevTools connector (Preview or Chrome MCP). Record which one you have. This decides whether numbers are measured or inferred, and every number you write carries that label.
3. If a connector is registered, load the URL twice: once at a mobile viewport (375x812, throttled to a mid-tier phone and slow 4G) and once at desktop. Capture LCP, INP (or a TBT-based proxy on a cold load), CLS, total page weight, request count, and the render-blocking CSS and JS. Label these measured.
4. If no connector is registered, fetch the raw HTML and linked assets you can reach. Estimate weight from asset sizes, flag render-blocking tags in `<head>`, and reason about likely LCP element and layout shift. Label every one of these numbers inferred, not measured, in the report and the ledger.
5. Image optimization: list the heaviest images, their dimensions versus displayed size, format (note where AVIF or WebP would cut bytes), and whether they lazy-load and carry width and height.
6. Mobile responsiveness: check viewport meta, tap target spacing, horizontal overflow, and text legibility at 375px. With a connector, screenshot mobile and desktop for evidence.
7. Accessibility basics: color contrast on primary text and the main call to action, alt text on meaningful images, form label associations, visible focus state, and a sane focus order through the conversion path. Note WCAG AA contrast failures by ratio.
8. Tie each finding to the conversion metric from step Inputs. Order findings by severity (critical, high, medium, low) using user impact times reach, not raw byte count.
9. Write `final/web-vitals-{domain}-{date}.md`: a header with URL, date, connector used, and measured-or-inferred status, then the scorecard (the three CWV plus weight, requests, mobile, accessibility), then the prioritized fix table with columns issue, severity, evidence, fix, est. impact.
10. Append the ledger row(s). Update any prior baseline note in the project folder so a re-run charts movement.

## Outputs
- `Projects/web-vitals-{domain}-{date}/final/web-vitals-{domain}-{date}.md`: scorecard plus the prioritized fix list (issue, severity, evidence, fix, est. impact), each fix tied to a conversion metric.
- Mobile and desktop screenshots in the project folder when a connector was available.
- Memory/kpi-ledger.md, append-only, one row per measured metric:
  - `| 2026-06-23 | page-performance | <baseline or -> | <current> | <target> | web-vitals (Preview/Chrome connector) | confirmed | LCP/INP/CLS summary |`
  - Use the relevant CWV name (lcp, inp, cls) when logging a single vital. Set confidence to `confirmed` only with a connector and a measured number; use `inferred` when the value came from fetched HTML; `stale` if reusing an old reading.

## Guardrails
- Draft only. Never edit, deploy, or otherwise touch the live site; produce a fix list someone else applies.
- Never invent a metric. If you did not measure it, label it inferred and say what a connector would confirm.
- A measured row needs a real connector reading. No connector means no `confirmed` confidence, full stop.
- Agency firewall: audit the active client's page only, never a sibling client's. Keep the project inside the active client's workspace.
- Cite the source of every number (which connector, which tool, which fetched asset) in the report.
- Accessibility notes flag likely issues for a human to confirm; they are not a legal compliance sign-off.

## References
- `_system/connectors.md` for the registered browser or DevTools connector (Preview or Chrome MCP).
- Company/strategy.md and Company/offers.md for the conversion metric each fix maps to.
- The seo-* skills for HTML-level findings, and site-audit, which can spawn this skill as a lens.
- Memory/kpi-ledger.md for the metric history this audit reads and appends to.
