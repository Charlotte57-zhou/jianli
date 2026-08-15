# Changelog

## 3.1.0 — 2026-08-15

This release establishes the three-engine product architecture: Career Evidence Engine, Recruiter Translation Engine, and Resume Renderer. `v3.1.0` is used because the repository already published a `v3.0.0` tag; the tag is not reused or rewritten.

### Added

- Four-layer architecture: Evidence Core, Role Intelligence, Recruiter Translation, and Resume Rendering.
- Hard internal/external output isolation: internal truth controls wording, while internal audit language is excluded from recruiter-facing output.
- Recruiter Translation reference and card.
- Resume Bullet Compiler with B2B, AI product, technical product, 0→1, and transfer patterns.
- Resume Architecture Selector based on role, seniority, density, project count, portfolio, and page count.
- Original `clean-professional` and `high-density-technical` editable HTML Renderer Packs.
- External Output Sanitization and Rendering QA checklists.
- Internal Tailoring Delta for project order, wording, JD terminology, rejected keywords, transfer bridges, and risk downgrades.
- Anonymous translation, leakage-filtering, and eight-case acceptance examples.

### Changed

- Rewrote the Chinese README around user problems, recruiter translation, project preservation, AIPM, and real HTML/PDF delivery.
- Upgraded the AIPM Role Pack to lead with problem, why AI, non-AI boundary, product mechanism, human control, validation, and evidence before technical terms.
- Extended Final Resume Audit to cover recruiter comprehension, internal-language leakage, project coverage, Renderer boundaries, and print QA.
- Expanded repository validation for Renderer structure, external-field allowlists, internal-field leakage, project-preservation markers, version consistency, links, privacy, and HTML print contracts.

### Hard rules

- Internal truth controls wording, but internal audit language never leaks into the resume.
- Compression does not delete evidence: grouping similar items cannot silently remove an independent project.
- Renderer Packs cannot alter facts, positioning, wording strength, or project selection.
- No default photo area; content overflow expands naturally to two pages instead of unreadably small type.

## 2.1.0 — 2026-08-15

Capability-ownership architecture upgrade. This requested architecture version follows the project's v2.x capability line even though the earlier open-source packaging release used tag `v3.0.0`.

### Added

- Deep Interview & Capability Discovery mode.
- L0–L5 Capability Ownership Ladder.
- AI-assisted project audit for Codex, Claude Code, Cursor, and similar tools.
- Claim Defensibility Matrix.
- ten cross-industry capability primitives.
- Career Positioning Audit before the Master Resume.
- eight-stage Validation Maturity model.
- project explanation-right gate.
- templates for deep interview, ownership, claim defensibility, positioning, and maturity.

### Changed

- Extended the architecture from fact audit and JD tailoring into a complete episode-to-interview evidence chain.
- Added AI/other contribution, ownership, and maturity to the Fact Matrix.
- Added primitives, ownership, maturity, transfer structures, and boundaries to the Capability Library.
- Upgraded Interview Evidence Cards and Final Resume Audit.
- Upgraded all AI Product Manager Role Pack surfaces.
- Changed default AI Coding positioning to **AI-native product building and acceptance** rather than independent full-stack development.
- Expanded repository checks for architecture reachability, required primitives, privacy patterns, links, UTF-8, and whitespace.

### Preserved

- Strengthen positioning. Never strengthen facts.
- One career evidence base, many truthful tailored resumes.
- Direct similarity > adjacent similarity > transferable capability > generic traits.
- Employer / Client / Platform / Module / Contribution hierarchy.
- Public / Internal / Estimated data separation.
- Core + Role Packs architecture.

## 3.0.0 — 2026-08-14

- Renamed the Skill to `jianli` and published the first open-source repository structure.
- Separated repository documentation from the installable runtime package.

## 2.0.0 — 2026-08-14

- Introduced the general-purpose Core + Role Pack architecture.
- Added Career Evidence Base, Master Resume, JD tailoring, and interview evidence.

## 1.0.0 — 2026-08-14

- Initial evidence-first resume workflow.
