---
name: website-launch-kit
description: Build a launch kit for a website with the pre-launch checklist (content, SEO, analytics, performance, legal), the launch steps, and post-launch checks, when someone says launch a website, website go-live checklist, or pre-launch QA
---

# Website Launch Kit

Turns a website go-live into a tracked, repeatable checklist so nothing ships broken. Covers everything before, during, and after the launch.

## When to use
- A new website or a major redesign is about to go live.
- You want a written go-live plan with owners and a cutover sequence, not a mental list.
- You need a post-launch check so the first 48 hours after launch are watched, not assumed.
- A re-launch or a domain migration needs the same discipline as a first launch.

## Inputs
- Project slug (kebab-case, for example `acme-site-relaunch`).
- The site URL or staging URL, plus the target production domain.
- Hosting and DNS facts: where the site is hosted, who controls DNS, current TTL.
- Stack notes from `Company/stack.md` (CMS, analytics tool, forms, payment, email).
- Brand voice from `Library/styles/brand-voice.md` for any copy review.
- Optional: a launch date and the people who own each area.

## Process
1. Create the project folder if it does not exist: `Projects/{slug}/`. Confirm `brief.md` exists; if not, write a 5-line `Projects/{slug}/brief.md` stating the site, the goal of the launch, and the target date.
2. Read `Company/stack.md` and `_system/connectors.md` to learn the real tools in play (analytics, forms, CMS, host, DNS). Cite what you find; never assume a tool is connected.
3. Write the pre-launch checklist to `Projects/{slug}/final/launch-checklist.md` with these five sections, each as a checkbox list with an owner column:
   - Content: every page has final copy, headings reviewed against `Library/styles/brand-voice.md`, no lorem ipsum, images have alt text, links resolve, 404 page exists, favicon set.
   - SEO: title and meta description per page, one H1 per page, canonical tags, `robots.txt` allows the right paths, `sitemap.xml` generated and submitted, Open Graph and card tags, redirects mapped from old URLs to new.
   - Analytics: measurement tag fires on every page, key events defined (form submit, signup, purchase), consent banner wired if needed, a goal or conversion is set, real-time view confirms hits from a test visit.
   - Performance: Largest Contentful Paint under 2.5s on a mid-tier phone, images compressed and sized, render-blocking scripts deferred, caching and compression on, no console errors.
   - Legal: privacy policy and terms linked in the footer, cookie consent matches the analytics setup, contact details correct, any required accessibility statement present.
4. Write the launch steps to `Projects/{slug}/final/launch-steps.md` as a numbered cutover sequence: lower DNS TTL 24-48 hours ahead, freeze content, take a backup, deploy to production, point DNS or flip the host, force HTTPS, verify the certificate, warm the cache, then smoke-test the top 5 pages and the primary form or checkout.
5. Write the post-launch checks to `Projects/{slug}/final/post-launch.md`: a checklist for the first hour (pages load, forms submit, analytics records hits, no 5xx in logs), the first day (search engine can crawl, no broken redirects, Core Web Vitals sampled), and the first week (rankings stable, conversion events flowing, error rate flat).
6. Mark each item with a status box `[ ]`, an owner, and a one-line note. Leave items you cannot verify as unchecked with a note saying why.
7. Append one row to `Memory/kpi-ledger.md` recording the launch readiness as a metric (count of items passing out of total), using the exact columns. Never edit an existing row.
8. Note any item that touches a published or outbound surface (live copy, public redirects, the production domain) as DRAFT-ONLY: prepare it, but the human flips the switch.

## Outputs
- `Projects/{slug}/final/launch-checklist.md`: the five-section pre-launch checklist with owners.
- `Projects/{slug}/final/launch-steps.md`: the numbered cutover sequence.
- `Projects/{slug}/final/post-launch.md`: the first-hour, first-day, first-week checks.
- `Projects/{slug}/brief.md`: created if it was missing.
- One appended row in `Memory/kpi-ledger.md`: `| {date} | launch-readiness | 0/N | M/N | N/N | Projects/{slug}/final/launch-checklist.md | medium | pre-launch pass rate |`.

## Guardrails
- DRAFT-ONLY on anything that goes live: the kit prepares the launch, a human runs the cutover.
- VOICE: review copy against `Library/styles/brand-voice.md`. Do not invent new headlines silently.
- PROVENANCE: read tool facts from `Company/stack.md` and `_system/connectors.md`; cite them. Do not claim a tool is connected when it is not.
- Ledger is APPEND-ONLY: add the launch-readiness row, never edit prior rows.
- No metric without a source. If a performance number is not measured, mark it unverified, do not guess.

## References
- `Company/stack.md`
- `_system/connectors.md`
- `Library/styles/brand-voice.md`
- `Memory/kpi-ledger.md`
- `/a11y-audit` - run it on each launched page for a WCAG 2.1 AA accessibility pass before go-live.
