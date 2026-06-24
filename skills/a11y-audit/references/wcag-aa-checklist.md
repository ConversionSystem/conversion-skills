---
type: reference
status: active
tags: [accessibility, wcag, a11y-audit]
confidential: false
---

# WCAG 2.1 AA Quick Reference

The checks the a11y-audit skill runs against, organized by the four WCAG principles: Perceivable, Operable, Understandable, Robust. Each check names its success criterion (number, name, level), the concrete thing to verify, the anti-pattern that trips it, and how to test it. Criterion numbers match WCAG 2.1. A check is pass, warn, fail, or N/A. N/A is excluded from the score, never counted as a pass.

Roughly a third of these are machine-checkable by axe-core or a similar tool. The rest need a human or a model reasoning over the rendered page. Never report a clean automated scan as a clean audit.

Severity guide for findings: Blocker (a keyboard or screen-reader user cannot finish the task), Serious (the task is possible but degraded or confusing), Moderate (real friction, not a hard block), Minor (cosmetic or edge-case).

## Perceivable
Users can perceive the content with whatever sense or assistive tech they use.

- 1.1.1 Non-text Content (A). Every meaningful image, icon, and chart has a text alternative that conveys its purpose; decorative images have empty `alt=""` so they are skipped. Anti-pattern: `alt="image"`, a filename as alt, a missing alt on a meaningful logo or product shot, an icon-only button with no accessible name. Test: read the alt for every `<img>`, `role="img"`, and CSS background that carries meaning; ask whether the alt would let a non-seeing user act on it.
- 1.3.1 Info and Relationships (A). Structure is in the markup, not just the visuals: headings are real headings, lists are real lists, form fields tie to labels, tables use header cells. Anti-pattern: bold text faking a heading, a `<div>` grid faking a table, a label sitting next to a field with no programmatic link. Test: inspect the accessibility tree or the DOM; confirm the visual structure exists in the semantics.
- 1.4.1 Use of Color (A). Color is never the only way to convey meaning. Anti-pattern: a required field marked only red, a link distinguished from body text by color alone, a chart legend keyed only by hue. Test: render in grayscale and confirm every state and distinction still reads.
- 1.4.3 Contrast (Minimum) (AA). Normal text is at least 4.5 to 1 against its background; large text (18pt, or 14pt bold) is at least 3 to 1. Anti-pattern: light-gray placeholder text, a pale call-to-action button, white text on a light hero image. Test: compute the ratio from the rendered foreground and background colors, including text over images and gradients. Inferred when read from CSS without rendering; measured when sampled from the live DOM or a tool.
- 1.4.4 Resize Text (AA). Text scales to 200 percent without loss of content or function. Anti-pattern: fixed-px containers that clip text, content that vanishes when zoomed. Test: zoom the browser to 200 percent and confirm nothing is cut off or overlapping.
- 1.4.5 Images of Text (AA). Real text is used instead of pictures of text, except logos. Anti-pattern: a headline or a price baked into a JPG. Test: select the text; if it will not select, it is an image.
- 1.4.10 Reflow (AA). Content reflows to a single column at a 320px-wide viewport with no horizontal scrolling. Anti-pattern: a fixed-width layout forcing two-axis scrolling on a phone. Test: set the viewport to 320px and check for horizontal overflow.
- 1.4.11 Non-text Contrast (AA). UI components (inputs, buttons, toggles) and meaningful graphics have at least 3 to 1 contrast against adjacent colors, including the focus indicator. Anti-pattern: a faint input border, a focus ring the same value as the background. Test: compute the ratio for control boundaries, states, and the focus outline.
- 1.4.12 Text Spacing (AA). No content is lost when line height, paragraph, letter, and word spacing are increased. Anti-pattern: tightly clipped buttons that hide text when spacing grows. Test: apply the WCAG spacing overrides and confirm nothing clips.

## Operable
Users can operate the interface, including with a keyboard alone.

- 2.1.1 Keyboard (A). Every interactive element is reachable and usable with the keyboard alone. Anti-pattern: a custom dropdown, modal, or slider that only responds to a mouse; a `<div>` with a click handler and no key handler or role. Test: unplug the mouse and Tab, Enter, Space, and arrow through the whole conversion path.
- 2.1.2 No Keyboard Trap (A). Focus can move into and back out of every component with the keyboard. Anti-pattern: a modal or embedded widget that swallows Tab and never lets focus leave. Test: Tab into each widget and confirm Tab and Shift+Tab get you back out.
- 2.2.2 Pause, Stop, Hide (A). Any moving, blinking, or auto-updating content lasting over five seconds can be paused, stopped, or hidden. Anti-pattern: an auto-advancing carousel with no pause control, an infinite marquee. Test: look for a pause control on any auto-playing motion.
- 2.3.3 Animation from Interactions (AAA but check at AA-grade for risk). Motion triggered by interaction is reduced or removed when the user has set a reduced-motion preference. Anti-pattern: large parallax or slide animations that ignore `prefers-reduced-motion`. Test: set the OS reduced-motion preference and confirm the page honors it via the media query.
- 2.4.1 Bypass Blocks (A). A skip link or landmark structure lets keyboard users jump past repeated navigation to the main content. Anti-pattern: 30 nav links a keyboard user must Tab through on every page with no skip link. Test: load the page and press Tab once; a skip-to-content link should appear.
- 2.4.2 Page Titled (A). The `<title>` describes the page topic or purpose. Anti-pattern: "Home" or "Untitled" on every page. Test: read the `<title>`.
- 2.4.3 Focus Order (A). Focus moves in an order that preserves meaning and operability, matching the visual and reading order. Anti-pattern: a positive `tabindex` that jumps focus around, a modal that drops focus to the page top. Test: Tab through and confirm the focus path follows the visual flow.
- 2.4.4 Link Purpose (In Context) (A). Link text describes its destination. Anti-pattern: "click here", "read more", "learn more" repeated with no context. Test: list every link by its text alone and ask whether each destination is clear.
- 2.4.6 Headings and Labels (AA). Headings and labels describe their topic or purpose, and heading levels nest without skipping. Anti-pattern: an H1 followed by an H4, generic labels like "Field 1". Test: extract the heading outline and confirm it nests cleanly and reads like a table of contents.
- 2.4.7 Focus Visible (AA). The keyboard focus indicator is always visible. Anti-pattern: `outline: none` with no replacement, a focus ring invisible against the background. Test: Tab through and confirm a clearly visible focus indicator on every interactive element.
- 2.5.8 Target Size (Minimum) (AA, WCAG 2.2). Touch and click targets are at least 24 by 24 CSS px, or have enough spacing. Anti-pattern: tiny close icons, links packed tight in a footer. Test: measure the rendered size of small interactive targets.

## Understandable
Users can understand the content and how the interface behaves.

- 3.1.1 Language of Page (A). The `<html>` element carries a valid `lang` attribute. Anti-pattern: no `lang`, or `lang="en"` on a French page, so screen readers use the wrong pronunciation. Test: check the `lang` attribute on `<html>`.
- 3.2.1 On Focus (A). Moving focus to an element does not trigger an unexpected context change. Anti-pattern: a select that submits the form the moment it receives focus. Test: Tab onto each control and confirm nothing navigates or submits on focus alone.
- 3.2.2 On Input (A). Changing a setting does not auto-trigger a context change unless the user was warned. Anti-pattern: a dropdown that reloads the page on selection with no submit. Test: change each input and confirm the page does not jump without a warning.
- 3.3.1 Error Identification (A). Form errors are described in text and the field at fault is named. Anti-pattern: a red border with no message, "an error occurred" with no field named. Test: submit the form with bad input and read the error output.
- 3.3.2 Labels or Instructions (A). Every input has a visible, programmatically associated label, and any required format is stated. Anti-pattern: a placeholder used as the only label (it vanishes on type), a field with no label at all. Test: confirm each field has a `<label for>`, an `aria-label`, or `aria-labelledby`, not a placeholder standing in for one.
- 3.3.3 Error Suggestion (AA). When an error is detected and a fix is known, the page suggests it. Anti-pattern: "invalid date" with no format hint. Test: trigger a known error and check for a correction hint.
- 3.3.4 Error Prevention (Legal, Financial, Data) (AA). Submissions that are legal, financial, or data-changing are reversible, checked, or confirmable. Anti-pattern: a one-click irreversible purchase with no review step. Test: confirm a review, undo, or confirmation step exists on high-stakes submissions.

## Robust
Content works reliably across browsers, devices, and assistive tech.

- 4.1.2 Name, Role, Value (A). Every UI component exposes a name, a role, and its current state to assistive tech. Anti-pattern: a `<div>` button with no `role` or accessible name, a custom toggle that never reports checked or expanded. Test: inspect the accessibility tree; confirm each control announces what it is, what it is for, and its state.
- 4.1.3 Status Messages (AA). Status updates (form success, search result counts, cart changes) are announced without moving focus, via a live region. Anti-pattern: "Added to cart" appears visually but is silent to a screen reader. Test: confirm dynamic status text sits in an `aria-live` region or an appropriate role, and that it announces on change.

## Landmarks and structure (cross-cutting, mostly 1.3.1 and 4.1.2)
- One `<main>`, a `<nav>`, a `<header>`, and a `<footer>` as ARIA landmarks so screen-reader users can jump between regions. Anti-pattern: a page of nested `<div>`s with no landmarks. Test: list the landmark roles and confirm the main content sits in `<main>`.
- ARIA only where native HTML cannot do the job, and never breaking native semantics. Anti-pattern: `role="button"` on an `<a>`, redundant or conflicting roles, `aria-hidden="true"` on a focusable element. Test: confirm each ARIA role and property is valid, necessary, and not hiding something still in the tab order.

## How to test, in order
1. Static pass (fetched HTML): `lang`, `<title>`, heading outline, alt text, label associations, link text, landmarks, ARIA validity. Label results inferred.
2. Rendered pass (live DOM via the Preview connector or a Chrome MCP, if registered): Tab through the full conversion path for keyboard operability, focus order, no trap, and a visible focus ring. Label measured.
3. Contrast pass: sample rendered foreground and background colors on body text, the primary call to action, form fields, and the focus indicator; compute each ratio against 4.5 to 1 (or 3 to 1 for large text and UI components). Measured from the live DOM, inferred from CSS.
4. Motion pass: set `prefers-reduced-motion` and confirm the page honors it.
5. Automated pass (axe-core, if registered): run it for the machine-checkable criteria, then reconcile against the manual passes above. Never let a clean automated result stand in for the manual checks.
