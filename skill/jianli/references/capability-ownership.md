# Capability Ownership

## Purpose

Fact integrity answers **whether something happened**. Capability ownership answers **how deeply the candidate can personally explain, change, reproduce, and validate it**.

Keep three axes separate:

1. **Evidence Class** — what supports the claim;
2. **Ownership Level** — what the candidate can personally do;
3. **Validation Maturity** — how far the project or outcome has been validated.

A mature project does not automatically prove high candidate ownership. High candidate ownership does not imply production validation.

## Capability Ownership Ladder

| Level | Name | Minimum observable standard | Typical safe wording |
|---|---|---|---|
| L0 | Exposure | Saw, learned, reviewed, or participated without independent explanation | 接触、了解、参与 |
| L1 | AI-assisted Output | Produced an artifact with AI assistance, but explanation and modification remain limited | 借助 AI 完成初版/原型 |
| L2 | Explain | Can explain the core flow, design logic, concepts, own decisions, and boundaries without reading prepared material | 理解并可解释、负责定义部分方案 |
| L3 | Modify / Debug | Can change key behavior, locate faults, compare traces, and complete debugging | 修改、调试、迭代关键链路 |
| L4 | Reproduce / Validate | Can independently reproduce the core path, design checks, explain alternatives, and handle failures | 独立复现核心链路并设计验证 |
| L5 | Real-world Validated | Meets L4 and the capability has credible real-user, pilot, production, or measured-outcome evidence | 在真实使用/试点/生产中验证 |

## Promotion rules

- Assign the **highest level supported by observable evidence**, not the level implied by the project title.
- L1 does not become L2 merely because the generated artifact runs.
- L2 requires explanation of decisions and boundaries, not memorized terminology.
- L3 requires a concrete modification or debugging episode.
- L4 requires independent reproduction and validation design, not repeating an existing command list.
- L5 requires L4 ownership plus external validation. If the project reached production but the candidate only observed it, keep ownership below L5 and record production under Validation Maturity.

## Claim gates

| Claim pattern | Minimum level | Additional evidence |
|---|---:|---|
| 接触/参与某技术或项目 | L0 | role and scope boundary |
| 借助 AI 完成原型 | L1 | artifact and AI contribution boundary |
| 设计某流程/机制 | L2 | rationale, alternatives, own decision |
| 独立修改/调试关键功能 | L3 | change or debugging evidence |
| 独立构建/复现并验证核心链路 | L4 | reproduction and validation evidence |
| 生产验证/真实业务结果 | L5 | real-user/production evidence and attributable outcome |

Do not infer “independent full-stack development” from AI-assisted product output. For AI product roles, prefer the narrower capability actually proven, such as **AI-native product building and acceptance**.

## Ownership audit output

For every high-intensity claim record:

- claimed capability;
- evidence class and source;
- ownership level and promotion evidence;
- validation maturity;
- what the candidate can explain;
- what the candidate can modify/debug;
- what can be reproduced without notes;
- boundary and safe wording;
- next action required to raise the level.

Use [capability-ownership-matrix.md](../templates/capability-ownership-matrix.md).
