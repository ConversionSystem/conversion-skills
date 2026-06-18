---
name: seo-images
description: Image SEO for a page or an image set covering alt text, file naming, compression targets, dimensions, and image structured data, draft only. Triggers /seo-images, "alt text", "image SEO", "compress images", "name my image files", "image schema".
---

# SEO Images

Audit and rewrite the images on a page (or a whole set) so search and assistive tech can read them: descriptive alt text, clean file names, compression targets, correct dimensions, and ImageObject markup. Draft only, you apply the changes.

## When to use

- A page loads slowly and images are the weight.
- Alt text is missing, duplicated, or stuffed with keywords.
- File names look like `IMG_4821.jpg` instead of words.
- You want product or article images eligible for image results and rich previews.
- A re-run to chart how many images got fixed since the last pass.

Pairs with `/seo-audit` (which flags image issues) and `/seo-page` (on-page work where images live).

## Inputs

- The page URL or the image set in scope (a folder, a list of files, or a single page).
- `Company/profile.md` for site URL and brand, `Company/offers.md` for product names that should appear in product-image alt text and file names.
- `Library/styles/brand-voice.md` for tone of the alt copy (agency: the client's voice file).
- Optional: an existing export from a crawler or a Core Web Vitals tool listing image weights, registered in `_system/connectors.md`. Default to the page HTML plus the files themselves.

Ask only for what is absent: which page or files, and the intended use of each image (decorative, content, product, hero) if it cannot be read from context.

## Process

1. **Resolve mode and output location.**
   - Solo/Team (default), YOUR site: read `Company/`, write to `Projects/{site}-images-{date}/`.
   - No vault (standalone): do not stop. Ask for the URL or file list, skip workspace reads, write to a flat `./conversion-images-{date}/`, store `baseline.json` there, omit the `goals.md` and `Daily/` writes, then offer `/setup`.
   - Agency: read `Clients/{slug}/CLAUDE.md`, obey the firewall (no sibling-client reads), write to `Clients/{slug}/work/images-{date}/`, mark outputs `confidential:true`.
2. **Re-run check.** Glob the mode's `*-images-*/`. If a prior run exists, load `data/baseline.json` (which images were fixed, which props were placeholders) and lead with what is newly added or fixed.
3. **Inventory the images.** From the page HTML or the file list, build a row per image: current file name, current alt, format, dimensions (rendered vs intrinsic), file size, and inferred role (decorative, content, product, hero). Note which images carry no alt attribute and which are purely decorative (`alt=""` is correct for those).
4. **Draft alt text.** One line per image, describes what is in the image and its purpose on the page, in the brand voice. 125 characters or fewer. No "image of" or "picture of". Decorative images get empty alt. Product images name the product from `offers.md`. Never repeat the same alt across images. Never keyword-stuff.
5. **Draft file names.** Lowercase, words separated by hyphens, no spaces or underscores, describes the subject (`blue-running-shoe-side.jpg` not `IMG_4821.jpg`). Note the old name next to the new so you can rename and update references.
6. **Set compression and dimension targets.** Per `references/image-targets.md`: recommend a modern format (WebP or AVIF with a fallback), a size budget per role (for example hero under 200 KB, content under 100 KB, thumbnail under 30 KB), the intrinsic dimensions to export at, and `width`/`height` attributes plus `loading="lazy"` for below-the-fold images to hold layout and cut shifting. Flag any image served larger than it renders.
7. **Draft ImageObject markup where it earns a result.** For product and article hero images, emit a `<script type="application/ld+json">` ImageObject (or the `image` property nested in the page's existing Product or Article node), filled with `contentUrl`, `width`, `height`, and `caption`. Real values only, a missing dimension is a marked placeholder. Markup must match the visible image. Pairs with `/seo-schema`.
8. **Write the deliverable** (paths in Outputs). End with the instruction to test rendered pages in the Rich Results Test and to re-check page weight after compression.

## Outputs

To the mode's folder:
- `brief.md`: scope (page or file set), owner, acceptance criteria.
- `final/images.md`: one row per image with old vs new file name, new alt text, format and size target, export dimensions, and any ImageObject block in a code fence with where to paste it.
- `data/baseline.json`: the coverage map (image -> fixed alt, fixed name, hit size target, schema present or placeholder), so the re-run charts progress.
- Ledger row appended to `goals.md`, exact format `- YYYY-MM-DD | {goal-id} | {value} | {note}`, e.g. `- 2026-06-18 | images-fixed | 12 | 12 of 18 images, 3 alt placeholders`. If no `images-fixed` goal exists, create the definition (unit `count`, direction `up`) and flag it for confirmation. Standalone omits this.
- If a measured metric moves (for example total image weight on the page), append a row to `Memory/kpi-ledger.md` with a source and a confidence value. Never edit a prior row.
- One activity line to today's `Daily/` note under `## Activity` (not in standalone).

## Guardrails

- Draft only. Never rename a live file, edit production HTML, recompress and overwrite an original, or change anything on the site. You hand back instructions and markup.
- Real values only. Never invent dimensions, file sizes, or caption facts. A missing fact is a marked placeholder the user fills.
- Markup must match the visible image. No ImageObject for an image not on the page.
- Voice from `Library/styles/brand-voice.md` (agency: the client's). Alt copy reads like the brand, not like a keyword list.
- Firewall (agency): read only the active client's context, outputs `confidential:true`, never read a sibling client.
- Provenance: cite the page or export the weights came from, append a ledger row when a metric moves.
- Zero-API by default. Generated from the page HTML plus the files; a crawler or Core Web Vitals export is an optional connector, credentials never in the vault.

## References

- `references/image-targets.md`: format choice, per-role size budgets, dimension and lazy-loading rules, alt-text length and pattern.
