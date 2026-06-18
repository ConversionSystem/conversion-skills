---
name: wp-publish
description: Prepare an approved content draft for WordPress and push it as a WP draft post (never live) when a wordpress connector is enabled, otherwise output a ready-to-paste package with step-by-step instructions, recording the WP draft URL and id back to the content folder - triggers on /wp-publish, "publish to WordPress", "push this to WP", "send to WordPress as a draft", "prep this post for WordPress", "convert this to WordPress blocks", "load this into my blog"
---

# WordPress Publish

Takes an APPROVED content draft and turns it into a WordPress-ready package - mapped metadata, clean HTML/blocks, schema - then pushes it as a WP DRAFT post if a connector is enabled, or hands back a paste-ready package and steps if not. DRAFT-ONLY on the live site: a human hits Publish.

## When to use

- A blog post, article, or page draft has been approved and you want it staged inside WordPress (as a draft) or packaged for a clean paste into the editor.
- You want title, slug, meta description, categories, tags, featured-image placeholder, and schema mapped consistently before anything touches the CMS.
- NOT for writing or editing the content itself - draft and approve with the blog-post / newsletter / repurpose skills first; this skill only stages an already-approved draft. To re-stage an updated existing post, pair with the wp-refresh skill.

## Inputs

- **The approved draft (required):** a finished `status:draft`/`status:approved` content file, normally `Content/{slug}-{date}/final/post.md` (Solo/Team) or `Clients/{slug}/work/{slug}-{date}/final/post.md` (Agency). The skill stops if the content is not marked approved by the user.
- **Human approval (required):** explicit confirmation from the user that THIS content is approved to stage in WordPress. No approval, no push.
- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md` (Agency: the CLIENT's `Clients/{slug}/context/brand.md`) - to keep title/meta phrasing on-brand if they need tightening for length.
- **Connector registry:** `_system/connectors.md` - whether a `wordpress` connector row exists and its `status` (active vs paused/unavailable), its `scope`, and `secret-ref`. Never the credential itself.
- **SEO/taxonomy hints (if present):** any `data/` SEO notes in the content folder, an existing site category/tag list if one was previously ingested, and `Company/profile.md` for site URL and author identity (Agency: `Clients/{slug}/context/profile.md`).
- **From the user (ask only for genuine gaps):** target category/tags if not derivable, the canonical author, and the featured-image intent (none is generated here - only a placeholder).

## Process

1. **Resolve profile, locate the draft, and confirm approval.** Solo/Team: work in `Content/{slug}-{date}/`, ledger is `Memory/kpi-ledger.md`. Agency: resolve the active client, obey the FIREWALL (read/write only that client's `Clients/{slug}/`), work in `Clients/{slug}/work/{slug}-{date}/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill. Read the draft; if it is not user-approved, STOP and ask for approval before doing anything else.
2. **Load voice, then read the draft.** Read the voice files first, then the approved content. Confirm in one line what you found ("Post: 1,400-word teardown, approved 2026-06-18; voice: plain, numbers over adjectives") and ask only for genuine gaps (category, author, image intent).
3. **Map the WordPress fields.** Derive and record: `title` (<=60 chars where possible), `slug` (kebab-case, from the existing folder slug unless the user overrides), `meta_description` (<=155 chars, in voice, no invented claims), `categories`, `tags` (>=2), `excerpt`, canonical `author`, publish status `draft`, and a `featured_image` PLACEHOLDER reference only (alt text drafted; no image generated or uploaded). Flag any field you had to infer for the user to confirm.
4. **Convert markdown to clean WordPress HTML/blocks.** Produce semantic HTML (and a Gutenberg block-comment version) with proper headings (single H1 = the post title, body uses H2/H3), lists, blockquotes, code blocks, and real `<a>` links; strip editor cruft, smart-quote safely, and leave a clearly marked `<!-- featured image placeholder -->` and any in-body image placeholders with alt text. Preserve every link and number from the source exactly - invent nothing.
5. **Build the schema.** Draft JSON-LD (Article/BlogPosting as appropriate) with headline, author, datePublished left empty for the human, publisher, and canonical URL if known. Keep it as a separate block the human can paste or that the connector attaches; never fabricate dates or URLs.
6. **Decide the path - connector or package.** Read `_system/connectors.md`. If a `wordpress` connector row exists AND its `status` is `active` (enabled), go to step 7 (PUSH). Otherwise (no row, paused, draft, or unavailable) go to step 8 (PACKAGE). Either way, write the full staged package to the content folder first.
7. **PUSH as a WP draft (connector path).** Re-confirm the human approval from step 1 in one line, then push via the connector as `status: draft` ONLY - never published, scheduled, or live. Set title/slug/excerpt/meta/categories/tags/author and attach schema; the featured image stays a placeholder for the human to set. On success, capture the returned WP post `id` and draft preview URL. Log the external write per the connect skill's audit phase (`_system/audit/YYYY-MM-DD.md`). If the connector is unreachable, DEGRADE: mark it `unavailable` in `_system/connectors.md` and fall back to the PACKAGE path - never block.
8. **PACKAGE for paste (no-connector path).** Emit a paste-ready bundle (HTML body, block version, every mapped field, schema block, image placeholders) plus a short numbered step-by-step for the user to create the draft by hand in WordPress (new post -> paste -> set fields -> set featured image -> Save Draft, do NOT Publish). Leave the WP id/URL fields empty for the user to fill on save.
9. **Record provenance and the ledger row.** Write the WP draft `id`/URL (or "pending human save" for the package path) back into the content folder, write the staged files, and append the ledger row (see Outputs). Close with the one next action: a human reviews the WordPress draft and hits Publish.

## Outputs

- **Staged package** → `Content/{slug}-{date}/final/wordpress/` (Solo/Team) or `Clients/{slug}/work/{slug}-{date}/final/wordpress/` (Agency):
  - `post.html` - clean semantic HTML body.
  - `post.blocks.html` - Gutenberg block-comment version.
  - `schema.json` - JSON-LD (Article/BlogPosting), human-completed dates/URL.
  - `fields.md` - mapped WordPress fields (title · slug · meta_description · excerpt · categories · tags · author · status:draft · featured_image placeholder + alt), with any inferred field flagged. Universal frontmatter on the file (type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated); `status:draft`. Agency files are `confidential:true`.
  - `paste-steps.md` - the by-hand step-by-step (package path), or a one-line "pushed via connector" note (connector path).
- **WP result record** → same folder `wp-draft.md`: WordPress post `id`, draft preview URL, push timestamp, connector used (or "manual paste - pending human save"), and the explicit "draft only - human publishes" status. Empty id/URL allowed only on the package path.
- **Brief** → same folder `brief.md`: which approved draft was staged, the path chosen (connector vs package), fields mapped, acceptance criteria.
- **Intermediate data** → same folder `data/`: `mapping.json` (source draft -> WP field map + slug/category/tag decisions) and `inputs.json` (the context snapshot staged from).
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - Staged row, e.g. `| 2026-06-18 | wp-drafts-staged | 7 | 8 | 24 | Content/{slug}-2026-06-18/final/wordpress/ | confirmed | onboarding teardown staged as WP draft, awaiting human publish |`. If the metric does not yet exist, SEED it with a first row (baseline = current = the user-confirmed count, or `inferred` if estimated) and FLAG it - never invent a baseline.
- **Audit** (connector path only) → one line appended to `_system/audit/YYYY-MM-DD.md` recording the external write (actor · connector:wordpress · operation:write-draft · path · WP id · result).
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY on the live site.** A connector may only create/update a WordPress DRAFT post - never publish, schedule, set to live, or change a post's status to published. Publishing is a separate human-approved act. The skill never autonomously goes live.
- **Confirm approval before any push.** Require explicit human approval that THIS content is approved; re-confirm immediately before a connector push. No approval, no staging beyond local files.
- **Connector gate.** Push only if a `wordpress` connector is registered AND `status:active` in `_system/connectors.md`. Otherwise output the paste package. Never assume a connector exists; never invent credentials. Read secrets only by `secret-ref` - never write a credential into the vault.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` first (Agency: the CLIENT's `Clients/{slug}/context/brand.md`); keep any tightened title/meta on-brand.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Preserve every link, number, and claim from the approved draft exactly; invent no metrics, dates, URLs, or image content (placeholder + alt text only). Cite any external fact. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- **Degrade, never block.** If the connector is unreachable, mark it `unavailable`, fall back to the paste package, and log the outage - the user can still ship by hand.
- **Append-only.** `Memory/kpi-ledger.md` / `Clients/{slug}/goals.md` and `_system/audit/` are append-only - never edit, reorder, or delete prior rows/lines.
- A delivery run without its ledger row is unfinished.
- Original mapping and HTML only; no lifted markup or boilerplate from another site.

## References

- `_system/connectors.md` - the OPTIONAL `wordpress` connector (registry row, scope, `secret-ref`, status); zero-infra default needs none and uses the paste package.
- `_system/audit/` - external write log for any connector push.
- `references/wp-mapping.md` - field map (markdown -> WP fields), block conversion notes, and the JSON-LD Article/BlogPosting skeleton.
- The connect skill - registers/serves the `wordpress` connector and owns the audit + degrade phases this skill defers to.
- The wp-refresh skill - re-stage and update an already-published post from an updated draft.
