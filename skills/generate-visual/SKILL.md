---
name: generate-visual
description: Build an image prompt from your brand voice and use case then generate it through a registered image connector or hand back a precise prompt and brief, triggered by "generate visual", "make an image", "create a graphic", or "draft a hero image"
---

# Generate Visual

Turn a use case plus your brand into a ready image, or a precise prompt and brief when no image connector is wired up. Draft only.

## When to use
- You need a hero image, social graphic, thumbnail, diagram base, or illustration for a piece of content or a project asset.
- You want the visual to match brand voice, palette, and the audience for the use case.
- You have an image connector registered, or you want a tight prompt and brief to run by hand in an external tool.

## Inputs
- Use case in one line (where the image goes, what it must do).
- `Company/brand.md` for voice, palette, and visual rules. `Company/profile.md` and `Company/icp.md` for audience.
- Agency mode: the active client's `Clients/{slug}/brand.md` and `Clients/{slug}/goals.md`, never a sibling client.
- Target folder, the `Content/{slug}-{date}/` or `Projects/{slug}/` the image belongs to.
- `_system/connectors.md` to check for a registered image connector. Optional reference image as a file path.

## Process
1. Read `Company/brand.md` (agency: `Clients/{slug}/brand.md`) for voice, palette, tone, and any visual do-not list. Read `Company/icp.md` for who the image speaks to.
2. Pull the use case and the target folder. Confirm aspect ratio and dimensions from the use case (hero, square social, thumbnail, banner).
3. Check `_system/connectors.md` for a registered image connector and its permitted scope in `_system/permissions.md`.
4. Build the prompt: subject, composition, palette tied to brand, mood, style, what to exclude, plus the aspect ratio and dimensions. Keep it specific, numbers over adjectives.
5. If an image connector is registered and permitted, call it with the prompt. Write the returned image to the target folder under `data/`. Record the exact prompt alongside it.
6. If no connector is registered, skip generation. Write the prompt and a brief (use case, dimensions, palette, references, three direction notes) to the target folder so the user can run it in any external tool.
7. Solo and Team: write to `Content/{slug}-{date}/data/` or `Projects/{slug}/data/`. Agency: write under the active `Clients/{slug}/` asset folder, mark outputs `confidential: true`.
8. Append a ledger row only if the image ships against a tracked metric (for example a test variant). Otherwise no ledger row.

## Outputs
- Generated image at `Content/{slug}-{date}/data/visual-{label}.png` or `Projects/{slug}/data/visual-{label}.png` (agency: under `Clients/{slug}/`), when a connector ran.
- Prompt file `data/visual-{label}-prompt.md` holding the exact prompt, dimensions, palette, and references.
- Brief file `data/visual-{label}-brief.md` when no connector is registered, ready to run elsewhere.
- KPI ledger row in `Memory/kpi-ledger.md` only when the visual maps to a tracked metric.

## Guardrails
- Draft only. Never publish, post, send, or hand a visual to a client contact.
- Voice and palette come from `Company/brand.md` (agency: the client's brand file). Do not invent brand colors.
- Firewall (agency): read only the active client, never a sibling. Mark client outputs `confidential: true`.
- Provenance: if a reference image is used, cite its file path. Never claim a stock or third-party image is original.
- Image connectors are optional and registered in `_system/connectors.md`. Credentials live outside the vault, never in a written file.
- No connector means no generation. Output the prompt and brief instead, never a placeholder image.

## References
- `_system/connectors.md` for image connector registration and scope.
- `Company/brand.md` and `Library/styles/brand-voice.md` for voice and palette.
