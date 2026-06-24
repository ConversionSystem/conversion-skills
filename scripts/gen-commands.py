#!/usr/bin/env python3
"""Generate docs/commands.md from the skills. Accurate by construction, kept in sync."""
import glob, yaml, sys, os

os.chdir(os.path.join(os.path.dirname(__file__), '..'))

# slug -> category. Categories render in this order.
GROUPS = [
    ("Core modules", [
        "setup", "memory", "operator", "optimizer", "team", "client", "connect"]),
    ("Daily operations", [
        "daily", "weekly-review", "business-review", "pipeline-update",
        "meeting-capture", "project-update", "content-plan", "sop-create", "exec-dashboard", "monitor"]),
    ("SEO and visibility", [
        "site-audit", "web-vitals", "a11y-audit", "seo-audit", "seo-optimize", "seo-schema", "seo-programmatic", "seo-compare", "geo-optimize",
        "seo-content", "seo-technical", "seo-sitemap", "seo-hreflang", "seo-images", "seo-plan", "seo-competitor-pages"]),
    ("Paid ads", [
        "ads-audit", "ads-plan", "ads-google", "ads-meta", "ads-linkedin", "ads-tiktok", "ads-microsoft",
        "ads-youtube", "ads-budget", "ads-creative", "ads-competitor", "ads-landing"]),
    ("Sales and pipeline", [
        "lead-research", "lead-qualify", "lead-enrich", "crm-mining", "pipeline-review", "win-loss",
        "linkedin-writer", "linkedin-post-engagers", "sales-rep-analyzer", "free-audit", "hiring-signals"]),
    ("Content and publishing", [
        "email-sequence", "email-personalize", "social-post", "newsletter", "blog-post",
        "landing-page", "repurpose", "wp-publish", "wp-refresh", "copy-optimize"]),
    ("YouTube", [
        "youtube-ideation", "youtube-brief", "youtube-outline", "youtube-scripting",
        "youtube-packaging", "title-generation", "youtube-thumbnail-generate"]),
    ("Creative and media", [
        "infographic", "excalidraw", "gif-creator", "video", "generate-visual", "audio-transcriber"]),
    ("Design", [
        "taste", "redesign", "minimalist-ui", "brutalist-ui", "soft-ui", "stitch", "output-enforcement"]),
    ("Retention and proof", [
        "customer-onboarding", "churn-watch", "case-study", "testimonial", "portfolio-watch"]),
    ("Build and utilities", [
        "mcp-builder", "agent-builder", "deep-research", "fact-checker", "humanizer", "file-organizer",
        "prompt-master", "process-interviewer", "decision-toolkit", "n8n", "n8n-prd-generator",
        "course-creator", "website-launch-kit", "frontend-slides", "trend-scan", "doubt-check", "skill-author",
        "find-skill", "grill"]),
]

NOTES = {
    "Core modules": "Needs: `/setup` needs only an empty folder. The rest need a vault. Produces: the vault, the memory ledger, daily runs, audits, team and client structure, connectors.",
    "Daily operations": "Needs: a vault. Produces: daily notes, weekly and monthly reviews, an updated pipeline, an HTML dashboard. Each run that moves a metric appends one ledger row.",
    "SEO and visibility": "Needs: a vault and a target URL. Produces: drafts and prioritized findings in `Projects/` or `Content/`, plus ledger rows. Draft only. Never touches the live site.",
    "Sales and pipeline": "Needs: a vault and `Pipeline/` data, or a CRM export. Produces: prospect profiles, fit verdicts, pipeline analysis. No outreach is sent.",
    "Content and publishing": "Needs: a vault, your offers, your ICP, and your brand voice. Produces: drafts in `Content/`. Draft only. `wp-publish` and `wp-refresh` stage WordPress drafts, never live.",
    "Retention and proof": "Needs: a vault and customer or client data. Produces: onboarding plans, churn-risk lists, case studies drawn from the ledger, testimonials, a portfolio roll-up.",
    "Paid ads": "Needs: an ad-account export or a described setup, plus your offers and ICP. Produces: campaign plans, account structures, creative drafts, and prioritized audit findings in `Projects/` or `Content/`. Draft only. Never changes budgets, bids, or live campaigns.",
    "YouTube": "Needs: a channel niche, audience, and goal. Produces: ideas, briefs, outlines, scripts, titles, and thumbnail concepts in `Content/`. Draft only.",
    "Creative and media": "Needs: a source and, for images or video, an optional generation connector. Produces: infographics, diagrams, gifs, video packages, images, and transcripts. Draft only. Without a connector you get a build-ready brief.",
    "Design": "Needs: a page, a screen, or a brief. Produces: design specs and scored critiques in `Projects/`. Draft only.",
    "Build and utilities": "Needs: a described job. Produces: MCP servers, agent briefs, research reports, automations, prompts, decisions, and decks in `Projects/` or `Library/`. Code and configs are drafts. Credentials never in a file.",
}

# load skill descriptions
desc = {}
for f in sorted(glob.glob('skills/*/SKILL.md')):
    parts = open(f).read().split('---', 2)
    m = yaml.safe_load(parts[1]) or {}
    desc[m['name']] = m['description'].replace('|', r'\|')

placed = set()
total = len(desc)

lines = []
lines.append("# Command Reference")
lines.append("")
lines.append(f"_{total} commands. Generated by `scripts/gen-commands.py`. Do not hand-edit._")
lines.append("")
lines.append("Every command is a Claude skill. Type the command, or describe what you want in plain words and Conversion Skills routes to the right one. Every command is draft only on anything outbound: it writes drafts, a human sends and publishes.")
lines.append("")
lines.append("New here? Read `docs/getting-started.md` first, then run `/setup`.")
lines.append("")

for group, slugs in GROUPS:
    present = [s for s in slugs if s in desc]
    if not present:
        continue
    lines.append(f"## {group}")
    lines.append("")
    lines.append(NOTES.get(group, ""))
    lines.append("")
    lines.append("| Command | What it does |")
    lines.append("|---------|--------------|")
    for s in present:
        lines.append(f"| `/{s}` | {desc[s]} |")
        placed.add(s)
    lines.append("")

leftover = sorted(set(desc) - placed)
if leftover:
    lines.append("## Other")
    lines.append("")
    lines.append("| Command | What it does |")
    lines.append("|---------|--------------|")
    for s in leftover:
        lines.append(f"| `/{s}` | {desc[s]} |")
    lines.append("")

open('docs/commands.md', 'w').write("\n".join(lines).rstrip() + "\n")
print(f"  OK: docs/commands.md written ({total} commands, {len(leftover)} ungrouped)")
