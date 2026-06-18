---
name: seo-sitemap
description: Generate or validate an XML sitemap and robots.txt from a site's URLs with structure, priority, lastmod, and exclusions, plus a validation checklist. Triggers on "build a sitemap", "sitemap.xml", "robots.txt", "validate my sitemap", "sitemap audit".
---

# SEO Sitemap

Build or check an XML sitemap and a matching robots.txt from the site's URL list, then write a validation checklist. Draft only, files land in the project folder for the user to upload.

## When to use
- A new site or section needs a sitemap.xml and a robots.txt before launch.
- Search Console reports sitemap errors, missing pages, or "couldn't fetch".
- A migration, redesign, or bulk publish changed the URL set and the old sitemap is stale.
- You want exclusions checked so thin, duplicate, or private pages stay out of the index.

## Inputs
- Site root URL and the canonical host (http vs https, www vs bare). Required.
- A URL list: a crawl export, a CMS page list, an existing sitemap, or a pasted set of paths. Required.
- Optional per-URL signals: lastmod date, change cadence, relative priority, noindex flag, redirect or 404 status.
- Exclusion rules: paths to keep out (admin, cart, search results, tag pages, staging, query-string duplicates).
- Existing robots.txt, if any, for diff and reconciliation.
- Voice from `Library/styles/brand-voice.md` (agency: the active client's). Applies to any human-readable notes in the checklist.

## Process
1. Read the inputs. Resolve the canonical host and confirm one scheme and one host variant. Flag any URL that does not match so it gets normalized or dropped.
2. Normalize the URL list: strip tracking query strings, collapse trailing-slash variants to one form, lowercase the host, dedupe. Record every change in the checklist so nothing is silently lost.
3. Classify each URL. Keep indexable 200-status canonical pages. Move to an exclusions list anything noindex, redirected, 404, paginated past page one, parameter duplicates, or matched by an exclusion rule. Note the reason per URL.
4. Assign metadata. Set `lastmod` from the provided date or the source export, in W3C date format (date-only is fine). Set `changefreq` and `priority` from cadence signals or sensible defaults (home and top hubs higher, deep leaf pages lower). Treat both as hints, not promises, and say so in the checklist.
5. Decide the sitemap shape. One `urlset` file under 50,000 URLs and 50 MB uncompressed. Past either limit, split into themed child sitemaps and write a `sitemapindex` that lists them. Plan filenames now.
6. Generate the sitemap XML. Use the `http://www.sitemaps.org/schemas/sitemap/0.9` namespace, one `<url>` per kept page, XML-escape every loc, and order URLs for readable diffs.
7. Generate robots.txt. State allow and disallow groups, keep crawlable content reachable, block the excluded private paths, and add a `Sitemap:` line with the absolute sitemap URL. If a robots.txt was supplied, produce a diff and call out any rule that would block a page you just included.
8. Validate. Run the checklist in Outputs against the generated files: well-formed XML, count and size within limits, no excluded URL present, no included URL blocked by robots, every loc absolute and canonical-host, lastmod parseable.
9. Write outputs to the correct location. Solo and Team: `Projects/{slug}/final/`. Agency: `Clients/{slug}/Projects/{slug}/final/`, with `confidential: true` on each file. Leave the files as drafts for the user to review and upload. Never publish, push, or submit to any search engine.
10. If a tracked SEO metric (indexed pages, sitemap URL count, coverage errors) has a fresh number from the source, append one row to `Memory/kpi-ledger.md`. Never edit a prior row.

## Outputs
- `Projects/{slug}/final/sitemap.xml` (or `sitemap-index.xml` plus child files when split). Agency: same names under `Clients/{slug}/Projects/{slug}/final/`, `confidential: true`.
- `Projects/{slug}/final/robots.txt` (or the agency path), with the `Sitemap:` line and a diff block if an existing file was supplied.
- `Projects/{slug}/final/sitemap-checklist.md`: the validation results, the normalized-vs-original URL diff, the exclusions list with a reason per URL, and the metadata defaults used. Agency path mirrors the above with `confidential: true`.
- One appended row in `Memory/kpi-ledger.md` only when a sitemap or coverage metric has a confirmed or reported number. Columns exactly: | date | metric | baseline | current | target | source | confidence | note |.

## Guardrails
- DRAFT-ONLY. Write files to `final/` for the user. Never publish, push to a host, or submit a sitemap to Search Console, Bing, or any engine.
- PROVENANCE. Cite the source export for the URL list. Never invent a URL, a lastmod, or a coverage number. `priority` and `changefreq` are labeled as hints, not measured facts.
- Use the canonical host and scheme on every loc. One host variant only. A URL blocked by robots.txt must not appear in the sitemap, and a page in the sitemap must not be blocked by robots.
- VOICE from `Library/styles/brand-voice.md`; for agency work use the client's voice on any human-readable notes.
- FIREWALL (agency): the active client only. Never read a sibling client. Client outputs carry `confidential: true`.
- External crawlers, log analyzers, and Search Console exports are OPTIONAL connectors registered in `_system/connectors.md`. Default to a provided export or a described manual step. Credentials never live in the vault.

## References
- `_system/connectors.md` for any crawler or Search Console export setup.
- `Library/styles/brand-voice.md` for note voice.
- `Memory/kpi-ledger.md` for the append-only metric log.
