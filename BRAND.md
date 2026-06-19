# Conversion System Brand

The brand for Conversion Skills. Parent brand: Conversion System, an AI agency. This file is the source of truth. If a surface disagrees with this file, the surface is wrong. Enforced by `scripts/check-brand.sh`.

Version 3.0 · applies the Conversion System Brand Guidelines (v2.0, May 2026).

## The mark

`CONVERSION / SYSTEM`. Inter Tight Bold, all caps, one Orange slash between the two words. The slash is the cut, the work done between a visitor and a customer. It is not decoration. The descriptor `an AI agency` sits to the right in small caps.

Variants: primary (`CONVERSION / SYSTEM an AI agency`), reverse (on Ink), announcement (on Indigo), compact (`CS / 26`), favicon 32px (`C/S`), stacked (`CONVERSION SYSTEM` over `EST. 2024 · CHEYENNE WY`), stamp (`CS // OPERATOR`, `CS // INVOICE 2026.04.001`).

Misuse, never: gradients, drop shadows, AI illustration behind the mark, a tilted slash, a recolored slash, teal, or any purple that is not Indigo. The mark is type. Treat it as type.

## Three typefaces

- **Inter Tight** does the work. Headlines, body, UI. Most of the brand. (fonts.google.com)
- **JetBrains Mono** is for receipts. Numbers, prices, KPIs, page references, invoice fields. The sound of a printer. (fonts.google.com)
- **Instrument Serif**, italic, one place only: a real client pull-quote, in quote marks. A witness, not a brand voice. (fonts.google.com)

## Six colors, one job each

If you cannot name the color's job, do not use it.

| token | name | hex | job |
|-------|------|-----|-----|
| `--cs-paper` | Paper | `#ffffff` | ground |
| `--cs-ink` | Ink | `#0a0a0a` | body text, dark surfaces |
| `--cs-indigo` | Indigo | `#1a0f6a` | the brand anchor: wordmark, big surfaces |
| `--cs-orange` | Orange | `#ff5a1f` | the verb: the action, the price, the win |
| `--cs-court` | Court | `#ff7a3a` | callout (warm, large text only) |
| `--cs-solar` | Solar | `#ffd91a` | data |
| `--cs-cobalt` | Cobalt | `#1f4cff` | supporting links |

Utility: Paper-2 `#f4f4f0` (card backgrounds), Mute `#5e5e5e` and Dim `#8a8a8a` (secondary text and labels, never on Indigo).

Discipline. Orange is the verb. Use it once per page, twice maximum. It marks the action, the price, the win. If everything is Orange, nothing is Orange. Indigo is the brand. It anchors the page. Do not dilute it with tints.

## How we talk

Posture: a contractor who has done the job 200 times and is mildly annoyed you asked. Confident. Terse. Slightly mean to the competition. No flattery. No hedging. No second sentence when one will do.

Tone dial: Warmth 2/10 · Specificity 10/10 · Hedge 0/10 · Receipts 10/10.

Eight rules:

1. **Numbers, not adjectives.** Replace every adjective with a measurement. "Conversion went from 1.4% to 3.1% in 8 weeks", not "significantly improved conversion".
2. **Verbs, not nouns.** "We rebuilt their checkout. Bookings doubled." Not "conversion rate optimization implementation".
3. **Receipts over promises.** Every claim has a name, a number, a date range. If you cannot give all three, do not make the claim.
4. **No partner talk.** We are a vendor. Use vendor, contractor, the team you hired, we.
5. **No marketing words.** See the blocklist below.
6. **Sign your work.** Every blog post, case study, and email carries a real human byline that links to LinkedIn.
7. **Say what you mean.** If a target was missed, write that. Honesty is cheaper than reputation management.
8. **No em-dashes.** They are a tell. Use commas, periods, parentheses. En-dashes in numeric and date ranges are fine.

## The blocklist

If you type one of these, delete the sentence and write the actual verb, the actual noun, the actual number.

partner · journey · unlock · empower · transformative · holistic · seamless · synergize · ecosystem · best-in-class · world-class · cutting-edge · scalable · reimagined · elevate · solutions · let's chat · we'd love to · circle back · touch base · north star · 10x · hop on a quick call · thought leadership · drive value

## Components

- **Buttons.** Orange primary. Solid Ink secondary. Outline tertiary. Two button styles per page, maximum. ("Send a brief", "See what we ship", "Read the contract").
- **Receipt (the proof block).** Three parts: a number (JetBrains Mono, large), a verb-context, a named client with a date range. `2.2x · qualified leads, 11 weeks · Riverbed Dental · Mar 2025 to May 2025`. No anonymous "a leading SaaS company". Names or it did not happen.
- **Comparison row.** Trait | Most agencies | Conversion System.
- **Byline.** `By Angel Castro · AI & Automation Lead · linkedin.com/in/anglcstr`.
- **Email signature** (plain text):
  ```
  Angel Castro · AI & Automation Lead
  Conversion System · an AI agency
  angel@conversionsystem.com · linkedin.com/in/anglcstr
  ```

## The house

Conversion System is the parent, an AI agency for mid-market B2B (conversionsystem.com). Products and sub-brands sit underneath, each with its own visual language. The parent never appears on a product surface.

- **Kyra**, product, an AI receptionist for local service businesses (meetkyra.com).
- **Studio**, service line, six-week conversion sprints, fixed price, a named team.
- **Audit**, the free conversion audit, the lead-gen tool that feeds Studio.
- **Conversion OS**, the self-serve business OS, the flagship operators run their own business on.
- **Conversion Skills** (this repo): the 99-skill toolkit and marketplace for operators and agencies. It powers and complements Conversion OS, and carries the agency Client OS and delivery skills. Parent-branded for now; product wordmark `CONVERSION / SKILLS`.

Shared across the house: the hiring bar, the pricing philosophy (fixed, named, refundable), the stance on AI as a tool not the product. Not shared: typefaces, color palettes, component kits, voice, logo systems.

## Enforcement

- `scripts/check-brand.sh` fails the build on any em-dash or any blocklist word across the shipped surface. This file is exempt from the blocklist scan because it names the blocklist.
- `scripts/lint-cleanroom.sh` keeps foreign product names off every shipped file.
- Both run inside `scripts/sync-skills.sh`, which CI runs on every push. The badge is 0 em-dashes, 0 partnerships.

Tokens and the wordmark snippet live in `assets/brand-tokens.css`.
