---
name: youtube-thumbnail-generate
description: Draft a YouTube thumbnail concept (composition, text, faces, contrast) and either generate the image via a registered image connector or write a precise designer brief, triggered by "youtube thumbnail", "thumbnail concept", or "make a thumbnail"
---

# YouTube Thumbnail

Turn a video topic into a click-worthy thumbnail concept, then produce the image (if an image connector is wired) or a tight brief a designer can build from. Draft only.

## When to use
- A video, talk, or short needs a thumbnail and you want a concept before anyone opens a design tool.
- You have a title or hook and need matching art direction (layout, headline text, face, color).
- You want a designer brief precise enough to hand off without a meeting.

## Inputs
- Video topic, working title, or hook (required). Pull from the relevant `Content/{slug}-{date}/brief.md` or `Projects/{slug}/brief.md` if it exists.
- Audience and the one promise the thumbnail must telegraph.
- Brand color and type cues from `Company/brand.md` and `Library/styles/brand-voice.md`.
- Optional: a face photo path, a product shot path, or reference thumbnails.
- Connector check: read `_system/connectors.md` to see if an image connector row exists with `status: active`.

## Process
1. Read `Company/brand.md` for color, type, and visual rules. Read the source `brief.md` for the topic, audience, and promise.
2. Read `_system/connectors.md`. Note whether an active image connector is registered. If none, you will output a brief, not an image.
3. Define the single idea the thumbnail sells in 5 words or fewer. One idea, not three.
4. Draft the concept:
   - Composition: subject placement, left/right text zone, focal point, depth.
   - Text: 2 to 4 words, large, readable at 120px wide. Give the exact words.
   - Face: expression and crop (if a face is used), or state "no face".
   - Contrast: foreground vs background separation, color pairing, and the one element the eye lands on first.
   - Safe zones: keep text clear of the bottom-right timestamp overlay.
5. Write 3 concept variants (A, B, C) so there is a choice, each one line of rationale.
6. Produce the deliverable:
   - If an active image connector exists, send the chosen concept (composition, exact text, color, face crop, 1280x720) to it and save the returned image to the project `final/` folder. Log the external call to `_system/audit/`.
   - If no connector exists, write a precise designer brief: dimensions (1280x720, 16:9), exact text, font weight, hex colors, subject and crop, layered z-order, and 2 reference links if available.
7. For Solo and Team, write under the relevant `Content/{slug}-{date}/` or `Projects/{slug}/`. For Agency, write only inside the active `Clients/{slug}/` context, mark outputs `confidential: true`, and use the client's voice from their `Library/styles/brand-voice.md`.

## Outputs
- `Content/{slug}-{date}/data/thumbnail-concept.md` (Solo/Team) or `Clients/{slug}/Projects/{slug}/data/thumbnail-concept.md` (Agency): the 3 variants, chosen concept, and either the designer brief or the generated image path.
- If generated: the image file in the matching `final/` folder (for example `final/thumbnail-a.png`), plus an audit line in `_system/audit/` for the connector call.
- No `kpi-ledger.md` row at draft stage. Append a row to `Memory/kpi-ledger.md` only later, when a published thumbnail's click rate is measured against a baseline.

## Guardrails
- Draft only. Never publish, upload, or set the thumbnail on any platform.
- Never invent a metric, quote, or claim for the thumbnail text. If the text states a number, cite its source in the concept file.
- Use only the brand color and type from `Company/brand.md` (Agency: the client's). No stock faces of real people without a provided, cleared photo path.
- Credentials for any image connector live in a secret manager, never in the vault. If no connector is active, output a brief and say so plainly.
- Agency firewall: read only the active client, never a sibling.

## References
- `Company/brand.md`, `Library/styles/brand-voice.md`
- `_system/connectors.md`, `_system/audit/`
