# AI Product Manager — AI Coding Ownership

## Default interpretation

Prefer:

> AI-native product building and acceptance capability

Do not default to:

> independent full-stack development capability

The stronger engineering claim requires stronger code ownership evidence.

## Audit before wording

For Codex, Claude Code, Cursor, Copilot, or similar projects, record:

| Check | Evidence |
|---|---|
| Explain product flow, core call chain and data flow | |
| Explain personal decisions and AI contribution | |
| Modify a material behavior or contract | |
| Debug a concrete failure and verify the fix | |
| Reproduce the core path without prepared notes | |
| Design tests, Eval or acceptance checks | |

Map the result to L0–L5. A runnable generated artifact alone normally supports only L1 unless additional evidence exists.

## What AI Coding may prove for AI PM

- requirement-to-runnable-product translation;
- task decomposition and acceptance design;
- ability to inspect and correct AI-generated work;
- faster product experimentation;
- technical collaboration through concrete artifacts;
- AI-native product building and verification.

## What it does not automatically prove

- independent engineering ownership;
- production architecture expertise;
- security, performance, observability, or operations maturity;
- real-user value;
- measured business outcome.

## Safe wording ladder

- **L1:** 借助 AI Coding 完成可运行原型初版。
- **L2:** 能解释核心流程、产品决策与主要技术边界。
- **L3:** 能修改关键行为、定位故障并完成回归。
- **L4:** 能独立复现核心链路并设计验证与失败处理。
- **L5:** 在满足 L4 的基础上，经真实使用、试点或生产验证。

If explanation-right questions fail, use the Core stop message and build evidence before strengthening the claim.
