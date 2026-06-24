---
name: find-skill
description: Map a plain-English goal to the right Conversion Skill across the full catalog, match by what the skill does not just keyword, return the best one to three with their exact commands, triggers which skill do I use, find a skill, what command for this, how do I do X here, is there a skill for
---

# Find Skill

## When to use
You know what you want done but not which of the 100-plus skills does it. Use this when a plain-English goal needs to land on the right command, when two skills sound alike and you need the one that fits, or when you are not sure a skill for the job even exists. It reads the catalog and recommends; it never runs the skill it points you to.

## Inputs
- The goal in plain words (what you want done, and for whom if it matters).
- The artifact you have or want: a URL, a CSV export, a draft, a transcript, a prospect name, an idea.
- Optional context that narrows the match: is this for a client (which one), is there a vault yet, do you have the input the skill needs.

## Process
1. READ the catalog. Pull the full skill list from `SKILLS.md` and `docs/commands.md`. These two files are the only source of truth for what exists; a command not listed there does not exist and must not be recommended.
2. PARSE the goal. Name the job to be done in one line: the object (a page, a lead, an ad account, a post), the action (audit, draft, research, score, plan), and the intended outcome. If the goal is genuinely ambiguous, ask one clarifying question and stop until it is answered.
3. MATCH by capability. Compare the parsed job to what each skill actually does in its catalog description, not just its name. A goal of "figure out why this page doesn't rank" matches the audit skill by function even though it shares no words with it. Rank candidates by how squarely the skill's job covers the goal.
4. RECOMMEND the best 1 to 3. For each, give: the exact `/command` from the catalog, a one-line why-this-fits, what it needs as input, what it produces, and the draft-only note (it writes a draft, a human sends or publishes). Put the strongest fit first.
5. ORDER a chain if the goal needs several steps. When one skill's output feeds the next, give the sequence, for example `/setup` then `/lead-research` then `/email-personalize`. Name what passes between them.
6. HANDLE a miss. If nothing in the catalog fits, say so plainly, name the closest skill and why it falls short, and point to `/skill-author` to build a new one. Never invent a command to cover the gap.

## Outputs
- A short ranked recommendation in the reply: 1 to 3 skills, each with its exact `/command`, the why-this-fits line, its input, its output, and the draft-only note.
- A step order when the goal is multi-skill, naming what hands off between steps.
- When nothing fits: a plain "no skill covers this", the closest existing skill, and a pointer to `/skill-author`.
- No file is written. This skill recommends only.

## Guardrails
- Read-only. This skill reads `SKILLS.md` and `docs/commands.md` and recommends; it writes nothing and runs nothing.
- Recommend only skills that appear in the catalog. Never invent, rename, or guess a `/command`. If you cannot cite it from the catalog, it does not exist.
- Ask exactly one clarifying question when the goal is ambiguous, then wait. Do not stack questions or guess past a real fork.
- Always carry the draft-only note into the recommendation so the user knows the pointed-to skill produces a draft, never a sent or published action.
- Agency firewall: if the goal is for one client, the recommendation stands, but note that the recommended skill reads only that `Clients/{slug}/` folder.
- Recommend the fewest skills that cover the goal. Three is the ceiling; one clean fit beats three loose ones.

## References
- `SKILLS.md` for the full catalog and each skill's job, the source of truth for what exists.
- `docs/commands.md` for the grouped command reference, what each needs, and what it produces.
- `/skill-author` for the build-a-new-skill path when nothing fits.
- `/setup` as the usual first step in any chain when no vault exists yet.
