---
name: site-audit
description: Run a full site audit that fans out SEO, performance, conversion, and offer-fit specialists into one GO or NO-GO scorecard, triggered by /site-audit, "full site audit", "is this site ready", "audit the whole site", or "site readiness check"
---

# Site Audit
One orchestrated pass over a site: fan out the specialists, merge, judge, and return a GO or NO-GO with the blocking issues first. Draft only.

## When to use
- Before a launch, a redesign go-live, or a big ad spend, when you need one readiness verdict, not four separate reports.
- A prospect or client asks "is the site ready", and you want SEO, performance, and conversion judged together.
- After fixes, to re-run and confirm the blockers cleared.
- Not for a single lens: use `/seo-audit`, `/ads-landing`, or `/web-vitals` on their own.

## Inputs
- The site or page URL(s). The one thing you ask for if nothing is on disk.
- `Company/offers.md`, `Company/icp.md`, and the brand voice, for conversion and offer-fit judgment (agency: the active client's context).
- Optional connectors for measured performance and analytics; the default works from fetched pages.
- A prior `site-audit-{domain}-{date}/` for the re-run delta.

## Process
1. Resolve profile and output home. Solo/Team: `Projects/site-audit-{domain}-{date}/`. Agency: the active client's `Clients/{slug}/work/site-audit-{domain}-{date}/`, `confidential:true`.
2. Gather once. Fetch the in-scope pages, robots, and sitemap into `data/`. Record the offer and ICP from `Company/` (agency: the client).
3. Fan out specialists in parallel, each reading only its slice of `data/`:
   - the four `seo-audit` specialists (technical, onpage, performance, architecture),
   - the `web-vitals` lens for measured performance and accessibility (if `/web-vitals` is available, else the `seo-audit-performance` lens),
   - a conversion lens (message match, the single action, proof, friction, from `offers.md` and `icp.md`).
4. Merge. Assemble every specialist's findings into one scorecard, grouped by lens, severity-ranked. The main skill merges; specialists never call specialists.
5. Judge. Spawn the `judge` on every finding. Cut the ones it refutes (thin or uncited).
6. Decide. Compute a GO or NO-GO: NO-GO if any blocker (a Critical with cited evidence) survives the judge. List blockers first, then the ranked rest.
7. Write `final/site-audit.md` (`status:draft`) with the verdict, the blockers, the scorecard, and the quick wins. Write `data/baseline.json`. Append a ledger row (`site-readiness`) with source and confidence.

## Outputs
- `Projects/site-audit-{domain}-{date}/final/site-audit.md` (Agency: under the client workspace, `confidential:true`): GO or NO-GO, blockers first, the merged scorecard, quick wins.
- `data/baseline.json` for the re-run delta; the raw signals under `data/`.
- One appended ledger row (`site-readiness`) with source and confidence.

## Guardrails
- Draft-only. Never changes the live site, never publishes, never sends.
- The main skill merges; specialists return findings and stop. No specialist calls another.
- Cite or it does not exist. The judge cuts uncited findings before they reach the verdict.
- Agency firewall: read and write only the active client; outputs `confidential:true`.
- Never invent a number; label inferred versus measured.

## Red flags
- Returning a GO with a Critical, cited blocker still open.
- Merging specialist findings without running the judge, so a thin finding drives the verdict.
- A specialist reading another lens's data, or writing the final report.
- Scoring conversion before `offers.md` and `icp.md` are loaded.
- Finishing without `data/baseline.json`, so the re-run has nothing to diff.

## Verification
- [ ] Every lens ran and returned findings; none silently skipped.
- [ ] The judge ran on every finding; refuted ones are excluded from the verdict.
- [ ] The verdict is GO only if zero cited Critical blockers survive; blockers are listed first.
- [ ] Every finding cites a URL, a file, or a ledger row.
- [ ] `data/baseline.json` was written; a ledger row was appended with source and confidence.
- [ ] Output is `status:draft`; nothing was changed on the live site.
- [ ] Agency: stayed inside the active client; no sibling client was read; outputs `confidential:true`.

## Rationalizations
| Rationalization | Reality |
|---|---|
| "Most of the site is fine, call it GO." | One cited Critical is a NO-GO. A GO over an open blocker is the verdict that gets quoted when it breaks. |
| "The findings look right, skip the judge." | Unjudged findings are plausible, not proven. The judge is the difference between a report and a guess. |
| "I'll let the performance specialist also fix the schema." | Each specialist owns one lens. Cross-lane work is how findings get double-counted and the scorecard drifts. |
| "No baseline this run, I am short on time." | No baseline means the re-run cannot show what cleared. The whole point is the delta. |

## References
- `docs/orchestration.md` (the pattern and the roster)
- `agents/judge.md`, `agents/seo-audit-*.md`
