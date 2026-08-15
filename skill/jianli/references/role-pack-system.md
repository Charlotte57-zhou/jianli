# Role Pack System

## Purpose

A generic resume engine needs role-specific depth without becoming a giant prompt.

Role Packs provide that depth.

## Pack contract

A pack may specify:

- hiring dimensions;
- recurring JD terminology;
- preferred evidence;
- typical metric types;
- project-writing patterns;
- portfolio expectations;
- common resume mistakes;
- interview follow-up risks.
- capability-primitive relevance;
- expected ownership and maturity for strong role claims;
- role-specific explanation-right questions.

A pack must not:

- invent candidate facts;
- override evidence classes;
- raise capability ownership or validation maturity;
- convert personality labels into work-ready capabilities;
- force unsupported keywords;
- force every candidate into the same layout;
- claim market universality without actual JD research.
- expose internal audit fields in recruiter-facing output;
- let a Renderer alter wording or facts;
- remove an independent project without a recorded tailoring decision.

Role Packs map proven evidence into [Recruiter Translation](recruiter-translation.md). Content architecture is then selected through [Resume Architecture Selector](resume-architecture-selector.md). Renderer choice happens last.

## Load order

1. Root `SKILL.md`
2. Core evidence references
3. Relevant Role Pack
4. Actual target JDs
5. Candidate evidence

Actual candidate evidence and actual JD text outrank generic pack guidance.

## When no pack exists

Derive a temporary role profile from 5–20 target JDs when possible.

Capture:

- hiring dimensions;
- top responsibilities;
- tools/methods;
- expected outcomes;
- common keywords;
- portfolio signals;
- minimum credibility evidence.

Use `templates/role-profile.md`.

## Creating a new pack

Copy `packs/_template/`.

A useful pack should answer:

- What does this role actually get hired to do?
- What evidence proves that?
- What does a recruiter look for in 10 seconds?
- What does a hiring manager inspect deeply?
- Which metrics are credible?
- Which links/portfolio artifacts matter?
- What claims are commonly overused or misleading?
- Which capability primitives matter and what evidence proves them?
- What ownership and validation maturity does a strong claim require?
- What should a candidate be able to explain under interview pressure?
