# Conversion Skills landing page

One self-contained page. No build step, no framework, no dependency. Brand: Inter Tight, JetBrains Mono, the six colors, the wordmark with the Orange slash. The copy source of truth is `docs/sales-page.md`. Enforced by `scripts/check-brand.sh` like the rest of the surface.

## Preview
Open `index.html` in a browser. Fonts load from Google Fonts; offline it falls back to system fonts.

## Deploy
- GitHub Pages: serve from the `v2` branch, the `/site` folder.
- Vercel or Netlify: point at this folder, no build command, output `.`.
- Any static host: upload `index.html`.

By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr
