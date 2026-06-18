---
name: course-creator
description: Builds a course from a topic and audience into the outcome, module map, per-lesson objectives, and the assets each lesson needs, triggered by "create a course", "course creator", "build a curriculum", or "turn this into a course"
---

# Course Creator

Turn a topic and a target audience into a structured course: the one outcome learners reach, a module map, each lesson's objective, and the list of assets every lesson needs. Draft only.

## When to use
- The user asks to "create a course", "build a curriculum", or "turn this topic into a course" for a defined audience.
- A proven offer, playbook, or body of content should be packaged into a teachable sequence with clear modules and lessons.
- An existing course needs a re-cut: new outcome, new audience, or a tighter module map built from the same source material.

## Inputs
- Topic and audience from the user · the subject to teach and exactly who it is for (role, level, the result they want).
- `Company/icp.md` · audience pains, triggers, objections, and the words they use, to ground the outcome and lesson framing when the audience overlaps the ICP.
- `Company/offers.md` · the offer this course supports or sells, so the outcome ties to a real result.
- `Library/styles/brand-voice.md` · tone and voice constraints for any drafted titles, objectives, or copy.
- `Library/playbooks/` and existing `Content/{slug}-{date}/` directories · source material, frameworks, and prior teaching to draw module content from.
- `Memory/kpi-ledger.md` · any learning or funnel KPI the course is meant to move (completions, activations, upsells).
- Optional user input: desired length, delivery format (text, video, cohort, self-paced), module count, or a prior course to re-cut.

## Process
1. Lock the audience and outcome. From the user's topic and audience, write one sentence naming who the learner is and the single concrete result they can do or have by the end. Pull pain and language from `Company/icp.md` when the audience overlaps the ICP; do not invent an audience the user did not name.
2. Set the proof of completion. Decide how a learner shows they reached the outcome (a built artifact, a passed check, a shipped result). State it as a number or a verb, not an adjective. This anchors every module backward from the end.
3. Map modules. Break the path from zero to the outcome into 3-7 modules, each a milestone that moves the learner one clear step closer. Name each module by the capability it delivers, and reject any module that does not trace to the outcome.
4. Write lesson objectives. Inside each module, list lessons. Give every lesson one objective in the form "after this lesson the learner can ___" using an action verb. Keep each lesson to a single idea; split anything that needs two verbs.
5. List assets per lesson. For each lesson, name the assets needed to teach it: script or written walkthrough, slides or diagram, worksheet or template, example or dataset, exercise, and any check. Mark each asset as needed and not yet built.
6. Sequence and size. Order modules and lessons so each depends only on what came before. Estimate length per lesson and per module, sized to the user's format and time window. Flag any prerequisite the learner must bring.
7. Set targets. Tie the course to the one KPI it should move (completion rate, activation, upsell) with a measurable target and exactly how it gets measured. Targets are concrete numbers.
8. Present the outline for approval. Summarize the outcome, proof of completion, module map, lesson objectives, asset list, and KPI target. Get human confirmation before writing files.
9. Scaffold the course. Create `Content/{slug}-{date}/` with a kebab-case slug and ISO date (use `Projects/{slug}/` instead when the course is a client or one-off deliverable). Write `brief.md` with universal frontmatter and the full outline, write `data/baseline.json` capturing the starting KPI values and measurement source, and create an empty `final/` directory for the eventual built lessons.
10. Log the plan. Append one summarizing row to `Memory/kpi-ledger.md` recording the target for the KPI this course is meant to move. Never edit or reorder prior rows.

## Outputs
- One course directory under `Content/{slug}-{date}/` (or `Projects/{slug}/` for client or one-off work), containing:
  - `brief.md` · the course outline with universal frontmatter (`type:course-outline`, `status:draft`, `owner`, `date`, `reviewed`, `tags` >=2, `confidential`, `source`, `generated:false`), the audience and outcome, the proof of completion, the module map, each lesson's objective, the per-lesson asset list, sequence and sizing, and the KPI target with its measurement.
  - `data/baseline.json` · starting KPI values and the measurement source for this course.
  - `final/` · empty directory for the eventual built lessons and assets.
- One appended row in `Memory/kpi-ledger.md` using the exact columns `| date | metric | baseline | current | target | source | confidence | note |`, recording the course KPI target, with `confidence` in {confirmed,reported,inferred,stale}.
- A course outline summary returned to the user: outcome, proof of completion, modules, lesson objectives, assets, and KPI target.

## Guardrails
- Draft-only. Never publish, sell, or enroll; the brief is written `status:draft` and all built lessons stay in `final/` for human action.
- Truth-sourced only. The outcome and audience trace to what the user gave plus `Company/icp.md` and `Company/offers.md`; never invent audiences, results, or completion metrics. If truth files are missing, surface the gap rather than guessing.
- Every module and lesson traces to the one outcome; cut anything that does not move the learner toward it.
- Human-approval gate before scaffolding files (Process step 8) and before any future publishing or enrollment step.
- KPI ledger is append-only with the exact column order; never edit, reorder, or overwrite prior rows. Generated rollups carry `generated:true` and are not hand-edited.
- Use kebab-case slugs and ISO dates for all `Content/{slug}-{date}/` and `Projects/{slug}/` directories; route facts to their canonical homes.
- Respect the Agency client firewall: only the active client, never read sibling `Clients/{slug}/` directories, and route anything ambiguous to `Inbox/`.

## References
none
