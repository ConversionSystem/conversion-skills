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

This skill runs in two modes. QUICK mode is the zero-infra default: it scans the page HTML and source for likely Core Web Vitals problems and flags them, needing nothing connected. DEEP mode is an optional accelerator: when a real performance artifact is provided (a Lighthouse JSON report, a PageSpeed Insights API response, or CrUX p75 field data), it parses that artifact for measured metrics. Deep mode never blocks the audit; if no artifact is present, run Quick and say so.

## Inputs
- Target URL (required). If the active context is a client engagement, the page belongs to the active client only, never a sibling.
- A measured-signals source, when available: the Preview connector or a Chrome DevTools connector listed in `_system/connectors.md`. Check there first.
- Company/strategy.md and Company/offers.md for the conversion metric this page is meant to move (signup, demo, purchase, lead).
- Any prior audit in `Projects/web-vitals-{domain}-{date}/` to chart against.
- Target thresholds if the team has set them; otherwise use the standard good marks (LCP under 2.5s, INP under 200ms, CLS under 0.1).
- DEEP mode artifact, optional. Read it only if one is present in the project data or handed to you. Any of three:
  - A Lighthouse JSON report. Pull lab LCP, INP (or TBT proxy), and CLS, plus the `audits` opportunities and diagnostics list (render-blocking resources, unsized images, unused bytes) with their estimated savings.
  - A PageSpeed Insights API response. Pull both the lab result (`lighthouseResult`) and the field result (`loadingExperience` / `originLoadingExperience`) when present.
  - CrUX p75 field data. Pull the real-user p75 for LCP, INP, and CLS, the metric a page is actually judged on.
  - In all three, LCP, INP, and CLS are the headline metrics; everything else is supporting detail for the fix list.

## Process
1. Resolve `{domain}` from the URL host (strip `www.`, keep the registrable name, e.g. `acme.com`) and `{date}` as today in YYYY-MM-DD. Create `Projects/web-vitals-{domain}-{date}/` with a `final/` subfolder. Agency: the project lives under the active client's workspace, not the root.
2. Check `_system/connectors.md` for a registered browser or DevTools connector (Preview or Chrome MCP). Record which one you have. This decides whether numbers are measured or inferred, and every number you write carries that label.
3. If a connector is registered, load the URL twice: once at a mobile viewport (375x812, throttled to a mid-tier phone and slow 4G) and once at desktop. Capture LCP, INP (or a TBT-based proxy on a cold load), CLS, total page weight, request count, and the render-blocking CSS and JS. Label these measured.
4. QUICK mode (the zero-infra default, run it whenever no artifact and no connector is present). Fetch the raw HTML and linked assets you can reach and scan the source for the likely Core Web Vitals offenders: render-blocking `<script>` and `<link rel=stylesheet>` in `<head>` (no `defer`/`async`), images with no `width`/`height` or no `loading=lazy` (layout-shift and lazy-load misses), large or uncompressed/legacy-format images (LCP and weight), web fonts with no `font-display`, and injected banners or ad slots above the fold (shift risk). Flag each with the vital it threatens. Estimate weight from asset sizes and reason about the likely LCP element. Label every one of these numbers inferred, not measured, in the report and the ledger.
4a. DEEP mode (optional accelerator, run only if a Lighthouse, PageSpeed Insights, or CrUX artifact is present). Parse the artifact named in Inputs. From Lighthouse JSON, read lab LCP/INP/CLS and the opportunities and diagnostics list with estimated savings. From a PSI response, read both the lab block and the field block. From CrUX, read the real-user p75 for LCP, INP, and CLS. Mark these numbers measured (field p75 from CrUX/PSI is the strongest grade of evidence; Lighthouse lab is measured-lab). Where the artifact and the Quick-mode scan disagree, trust the measured artifact and keep the scan finding only as a probable cause. A measured field p75 sets the confidence to `confirmed`; lab-only stays `inferred` for field behavior.
5. Image optimization: list the heaviest images, their dimensions versus displayed size, format (note where AVIF or WebP would cut bytes), and whether they lazy-load and carry width and height.
6. Mobile responsiveness: check viewport meta, tap target spacing, horizontal overflow, and text legibility at 375px. With a connector, screenshot mobile and desktop for evidence.
7. Accessibility basics: color contrast on primary text and the main call to action, alt text on meaningful images, form label associations, visible focus state, and a sane focus order through the conversion path. Note WCAG AA contrast failures by ratio.
8. Tie each finding to the conversion metric from step Inputs, and tie each fix to the specific vital it moves (LCP, INP, or CLS). Order findings by Core Web Vitals impact times user reach, not raw byte count: a field-data p75 that fails for most real users (Deep mode, CrUX/PSI) outranks a lab-only nit, which outranks a Quick-mode inferred risk. Name the metric each fix is expected to move and by roughly how much when the artifact gives you savings estimates.
9. Write `final/web-vitals-{domain}-{date}.md`: a header with URL, date, mode (Quick or Deep), the artifact name and type if Deep, connector used, and measured-or-inferred status, then the scorecard (the three CWV plus weight, requests, mobile, accessibility), then the prioritized fix table with columns issue, severity, evidence, fix, metric moved, est. impact.
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
- DEEP mode artifacts, all optional accelerators read only when present: a Lighthouse JSON report (lab LCP/INP/CLS plus opportunities and diagnostics), a PageSpeed Insights API response (lab plus field), and CrUX p75 field data (real-user p75 for LCP, INP, CLS). None is required; Quick mode runs with none.
- Company/strategy.md and Company/offers.md for the conversion metric each fix maps to.
- The seo-* skills for HTML-level findings, and site-audit, which can spawn this skill as a lens.
- Memory/kpi-ledger.md for the metric history this audit reads and appends to.
