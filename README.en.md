# Jianli v3.1.0

> Turn verified career evidence into recruiter-readable, job-specific, interview-defensible resumes.

Jianli is an open-source Skill built for Chinese job seekers. It combines three systems:

1. **Career Evidence Engine** — verifies facts, contribution, capability ownership, validation maturity, and claim defensibility;
2. **Recruiter Translation Engine** — converts verified evidence into clear project context, candidate action, observable behavior, value, and evidence;
3. **Resume Renderer** — delivers editable HTML, A4 print layouts, natural pagination, and PDF-ready output.

## Core principles

- Strengthen positioning. Never strengthen facts.
- One career evidence base, many truthful tailored resumes.
- Direct similarity > adjacent similarity > transferable capability > generic traits.
- Separate Employer / Client / Platform / Module / Contribution.
- Separate Public / Internal / Estimated data.
- Role Packs cannot override the Evidence Core.
- Internal truth controls wording, but internal audit language never leaks into the resume.
- Compression must never silently delete an independent project.

## v3.1.0 architecture

```text
Deep Interview
→ Fact / Evidence Audit
→ Capability Ownership
→ Career Evidence Base
→ Positioning and JD Matching
→ Claim Selection
→ Recruiter Translation
→ Resume Architecture
→ Renderer Pack
→ Print / PDF QA
→ Interview Evidence
```

## Internal versus external output

Internal fields such as evidence class, ownership level, personal boundary, missing evidence, maturity, and interview risk control claim strength. They are not rendered as recruiter-facing labels.

For example, an internal record may say that a candidate did not own the full lifecycle and lacks production validation. The resume should naturally state the exact owned scope and verified Demo or Offline Eval stage instead of exposing audit-report language.

## Independent project preservation

Every independent project keeps a stable source record. A tailored resume may:

- show it independently;
- group it under a platform while preserving its identity and contribution;
- omit it for a target JD with an internal recorded reason.

It may not merge separate actions, metrics, or outcomes into a synthetic project.

## Renderer Packs

- `clean-professional` — product, operations, business, and general Chinese applications;
- `high-density-technical` — AIPM, AI, Agent, engineering, and technical product roles.

Both are original, editable HTML templates with A4 print CSS, natural multi-page output, hidden print toolbars, and no default photo area.

## Install

Download or clone the repository, then copy:

```text
skill/jianli
```

to:

```text
Windows: %USERPROFILE%\.codex\skills\jianli
macOS/Linux: ~/.codex/skills/jianli
```

Invoke it with `$jianli`.

## Repository layout

```text
skill/jianli/
├── SKILL.md
├── references/
├── templates/
├── packs/
├── renderers/
├── checklists/
└── examples/
```

The project is licensed under the [MIT License](LICENSE).
