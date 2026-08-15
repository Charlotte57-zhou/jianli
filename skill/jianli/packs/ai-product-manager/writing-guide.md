# AI Product Manager — Writing Guide

## Evidence-first sequence

Write in this order:

> User/business problem → Product judgment → Why use or not use AI → Personal decision → Rule/Workflow/Agent/Human boundary → Artifact → Validation maturity → Limitation

## Two-layer communication

### Layer 1 — Recruiter-readable

Answer who has the problem, why it matters, what the product changes, what the candidate owned, and how far it was validated.

### Layer 2 — Technical proof

Add only supported mechanisms such as Agent, tools, MCP, state, permissions, structured outputs, Eval, Bad Cases, and failure handling.

## Claim pattern

```text
For [user/problem], the candidate [owned action/decision] to build [artifact/mechanism],
separating [Rule/Workflow/Agent/Human boundary],
validated at [actual maturity stage], with [known limitation].
```

## AI-assisted project wording

Preferred when supported:

> 借助 AI Coding 将需求转化为可运行产品，能够解释核心链路、修改关键行为、定位故障并通过测试或 Eval 验收。

Do not write “independent full-stack development” unless L4+ engineering ownership is proven.

## High-trust / high-risk workflows

Surface:

- evidence source and missing-evidence behavior;
- responsibility owner;
- human confirmation before consequential action;
- failure state and recheck;
- what the Agent recommends versus executes.

## Personal AI projects

Personal projects are valid at their real maturity level. Name Concept, Prototype, Demo/POC, Offline Eval, Expert Review, Pilot, Production, or Measured Outcome precisely. Never imply the next stage.
