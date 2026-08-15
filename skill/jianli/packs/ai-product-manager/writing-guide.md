# AI Product Manager — Writing Guide

## Recruiter-first, evidence-controlled sequence

Write in this order:

> User/business problem → Why AI → What does not use AI → AI boundary → Product mechanism → Human control → Validation → Evidence → Technical proof

## Two-layer communication

### Layer 1 — Recruiter-readable

Answer who has the problem, why it matters, what the product changes, what the candidate owned, and how far it was validated.

### Layer 2 — Technical proof

Add only supported mechanisms such as Agent, tools, MCP, state, permissions, structured outputs, Eval, Bad Cases, and failure handling.

Do not begin a project bullet by stacking Agent, MCP, Harness, Tool Calling, and Eval. These terms should explain a product decision after the problem and boundary are clear.

## Claim pattern

```text
For [user/problem], the candidate [owned action/decision] to build [artifact/mechanism],
separating [Rule/Workflow/Agent/Human boundary],
validated at [actual maturity stage], with [supported evidence].
```

Known limitations remain in the internal audit unless normal hiring language is needed to describe an actual stage. Write “完成可运行 Demo 与离线评测”, not an audit label such as “不是生产”.

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
