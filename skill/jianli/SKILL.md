---
name: jianli
description: 当用户要深度探索职业优势、识别稳定行为模式、审计 AI 辅助项目能力所有权，或审查、重写、优化、定制简历/CV、匹配公司/岗位/JD 时使用。先把自然倾向转成可观察行为与有证据的职业能力，再核验事实、所有权和验证成熟度，建立职业证据库与母版，生成可防守的岗位定制简历和面试证据卡。适用于“我不知道自己的优势”“经历很杂”“哪些 AI 项目真正算我的能力”等问题。
---

# 简历证据库

先核事实，再定能力，最后写简历。

```text
具体经历
→ 深访发现的稳定行为
→ 可观察职业能力
→ 证据
→ 能力所有权级别
→ 可迁移问题结构
→ 目标 JD / Role Pack
→ 可防守简历表述
→ 面试追问证据
```

## 不可覆盖的核心契约

1. **Strengthen positioning. Never strengthen facts.**
2. **One career evidence base, many truthful tailored resumes.**
3. **Direct similarity > adjacent similarity > transferable capability > generic traits.**
4. 严格分层 `Employer / Client / Platform / Module / Contribution`。
5. 严格区分 `Public / Internal / Estimated` 数据与可归属结果。
6. 保持 `Core + Role Packs`：Core 拥有事实、能力所有权和防守性契约，Role Pack 只补岗位解释。

## 选择模式

### A. Deep Interview & Capability Discovery

当用户不知道优势、经历杂乱、想探索天赋，或不确定 AI 项目是否算个人能力时，先进入深访，不直接写简历。

必须分开：

1. **Natural Tendencies** — 内部定位假设，不直接写进 bullet；
2. **Work-ready Capabilities** — 有项目行为、证据和所有权支持；
3. **Capability Gaps / Claim Boundaries** — 当前证据不足或不能包装的能力。

读取 [深访方法](references/deep-interview-to-resume.md) 和 [深访模板](templates/deep-interview.md)。一次问一个核心问题，先要具体事件，再接受特质标签。

### B. Career Evidence Base / Master Resume

用于重建职业事实源或支持连续投递。先完成定位审计，再生成母版。母版保存所有可防守证据，不等于直接投递版本。

### C. JD Tailoring

用于已有公司、岗位或 JD。只从证据库中选择、排序和翻译，不为匹配关键词补写能力。

### D. Feedback Review

逐条判断第三方建议：`采纳 / 修改后采纳 / 不采纳 / 需要更多证据`，并说明筛选价值、真实性、岗位匹配和面试风险。

### E. Role Pack

完成 Core 审计后再加载岗位包。当前内置 [AI 产品经理岗位包](packs/ai-product-manager/PACK.md)。岗位包不得提升 Evidence Class、Ownership Level 或 Validation Maturity。

## 执行流程

### 1. 明确目标并保留源文件

确认目标岗位、职级、公司/行业、地区、语言、页数、文件格式及已有证据。保留原文件；缺失项标记“待确认”，先处理已知部分。必要时使用 [信息采集模板](templates/intake.md)。

### 2. 需要时先做深度访谈

从具体事件采集触发、约束、可观察动作、个人决策、他人/AI 贡献、结果、失败和反例。至少两个独立事件支持后，才把行为视为稳定模式。

执行转换：

```text
自然倾向 → 可观察行为 → 能力原语 → 项目证据 → 所有权 → 成熟度
```

不要把“好奇心、学习能力、责任心、沟通能力”直接变成高价值 bullet。读取 [能力原语库](references/capability-primitives.md)。

### 3. 建立 Fact Matrix

将重要事实分类为 `Verified / User-confirmed / External/Public / Estimated / Inferred / Unknown`，并核对动作归属、数字口径、0→1 边界、系统范围、上线状态和职称。

把 AI/他人贡献、能力所有权和验证成熟度写入 [Fact Matrix](templates/fact-matrix.md)。详细规则见 [事实与证据](references/fact-integrity-and-evidence.md)。

### 4. 审计能力所有权

对每个高强度 claim 记录最高可证明级别：

- `L0 Exposure`
- `L1 AI-assisted Output`
- `L2 Explain`
- `L3 Modify / Debug`
- `L4 Reproduce / Validate`
- `L5 Real-world Validated`

项目成熟度与个人所有权是两个维度。生产项目中的旁观经历不等于 L5；L4 能力也不等于生产结果。读取 [能力所有权规则](references/capability-ownership.md)，填写 [所有权矩阵](templates/capability-ownership-matrix.md)。

### 5. 审计 AI 辅助项目

对 Codex、Claude Code、Cursor 等项目检查：

```text
Explain → Modify → Debug → Reproduce → Validate
```

AI 生成结果不自动成为候选人能力资产。检查设计理由、替代方案、数据流、Agent 必要性、Rule/Workflow/Agent/Human 边界、成功指标、失败处理、核心调用链和 Bad Cases。

解释权不足时明确输出：

> 先补项目解释权，不要继续强化简历 claim。

读取 [AI 辅助项目审计](references/ai-assisted-project-audit.md)。

### 6. 标记 Validation Maturity

为每个项目记录真实达到的最高阶段：

```text
Concept → Prototype → Runnable Demo / POC → Offline Eval
→ Structured User Interview / Expert Review → Pilot / Real User Usage
→ Production → Measured Business Outcome
```

简历不得越级。使用 [验证成熟度模板](templates/validation-maturity.md)。

### 7. 抽象能力并做 Career Positioning Audit

将证据写入 [Capability Library](templates/capability-library.md)，保留能力原语、所有权、成熟度、已证明领域、迁移结构和边界。

在母版前运行 [定位审计](templates/positioning-audit.md)，输出：

- 当前最强、最可证实的岗位定位；
- 次优相邻定位；
- 不建议强行包装的定位；
- 核心垂直能力与横向可迁移能力；
- 最大证据缺口及下一步证明动作。

岗位定位由证据决定。用户目标是输入，不是自动升级身份的依据。

### 8. 建立 Career Evidence Base 与 Master Resume

整理经历、指标、作品、能力、bullet 和面试证据。母版结构见 [Master Resume 模板](templates/master-resume-architecture.md)，母版与定制关系见 [Master vs Tailored](references/master-and-tailored-resume.md)。

### 9. 匹配 JD / Role Pack

先比较直接相似，再比较相邻问题结构和有证据的能力原语。对 JD 要求记录重要度、候选人证据、所有权、成熟度、缺口和决策，使用 [JD 矩阵](templates/jd-matrix.md)。

Role Pack 只决定哪些证据更重要、如何翻译和展示，不改变 Core 的事实判断。

### 10. 运行 Claim Defensibility Matrix

为每个高可见 claim 记录：

- Evidence Class / Strength；
- Ownership Level；
- Can Explain / Modify / Debug；
- Real User / Production Validation；
- Interview Risk；
- Safe Wording。

优先选择：

> 高 JD 相关性 × 高证据强度 × 高能力所有权 × 低面试穿透风险

硬边界不能被评分抵消。生产 claim 没有生产证据、独立开发 claim 低于 L4 时，必须降级或删除。使用 [Claim Defensibility Matrix](templates/claim-defensibility-matrix.md)。

### 11. 生成可防守简历与面试证据

bullet 优先组合问题背景、个人动作、范围/复杂度、交付和验证，不强套公式。大型项目先分清 Employer/Client/Platform/Module/Contribution，见 [项目层级](references/project-hierarchy.md)。

对最显眼的 3–5 个 claim 生成 [Interview Evidence Card](templates/interview-evidence-card.md)，验证解释权、替代方案、调试、失败处理和边界。如果面试 70% 时间围绕这些 claim 展开，应该对候选人有利。

### 12. 最终审计与交付

运行 [Final Resume Audit](checklists/final-resume-audit.md)。至少交付：定位结论、证据与边界、能力所有权矩阵、Claim Defensibility Matrix、新版简历、面试证据卡、待确认项和下一步证明动作。

## 按需读取

| 场景 | 读取 |
|---|---|
| 深访与优势探索 | [深访方法](references/deep-interview-to-resume.md)、[深访模板](templates/deep-interview.md)、[能力原语](references/capability-primitives.md) |
| 所有权与 AI 项目 | [能力所有权](references/capability-ownership.md)、[AI 项目审计](references/ai-assisted-project-audit.md)、[所有权矩阵](templates/capability-ownership-matrix.md) |
| 定位与母版 | [定位审计](templates/positioning-audit.md)、[核心架构](references/core-architecture.md)、[母版模板](templates/master-resume-architecture.md) |
| JD 与可迁移能力 | [能力迁移](references/transferable-capability-mapping.md)、[JD 规则](references/jd-keyword-matching.md)、[JD 矩阵](templates/jd-matrix.md) |
| Claim 与验证边界 | [防守矩阵](templates/claim-defensibility-matrix.md)、[成熟度](templates/validation-maturity.md)、[事实规则](references/fact-integrity-and-evidence.md) |
| AI 产品经理 | [AI PM Pack](packs/ai-product-manager/PACK.md) 及其按需引用 |
| 端到端示例 | [能力链示例](examples/capability-chain-example.md) |
| 最终交付 | [简历审计](checklists/final-resume-audit.md)、[面试证据卡](templates/interview-evidence-card.md)、[版本命名](references/resume-versioning-and-naming.md) |

## 禁止项

- 直接把人格标签写成核心简历能力；
- 用 AI 生成物推导独立开发能力；
- 用 Demo 或 Offline Eval 推导真实用户价值；
- 用生产项目成熟度替代个人能力所有权；
- 用高 JD 相关性掩盖弱证据或高穿透风险；
- 编造经历、职级、技术、数字、客户、上线或业务结果；
- 用 Role Pack 覆盖 Core 的事实和能力边界。
