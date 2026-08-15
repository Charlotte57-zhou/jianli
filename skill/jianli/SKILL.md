---
name: jianli
description: 面向中文求职者的职业证据与简历交付 Skill。当用户要探索职业优势、审计 AI 辅助项目、梳理复杂经历、匹配岗位/JD、生成或修改简历，以及制作可编辑 HTML/PDF 简历时使用。先核验事实、能力所有权和项目阶段，再完成职业定位、招聘表达、信息架构、渲染与面试证据；保证内部审计语言不泄漏，压缩时不丢失独立项目。
---

# 简历证据库

将经过核验的职业证据，转化为招聘方看得懂、岗位匹配、面试可防守的定制简历。

```text
具体经历
→ 深访发现的稳定行为
→ 事实 / 证据 / 能力所有权审计
→ Career Evidence Base
→ 职业定位与 JD 匹配
→ Claim 选择
→ Recruiter Translation
→ Resume Architecture
→ Renderer Pack
→ Print / PDF QA
→ 面试追问证据
```

## 不可覆盖的最高原则

1. **Strengthen positioning. Never strengthen facts.**
2. **One career evidence base, many truthful tailored resumes.**
3. **Direct similarity > adjacent similarity > transferable capability > generic traits.**
4. `Employer / Client / Platform / Module / Contribution` 必须分层。
5. `Public / Internal / Estimated` 数据及个人可归属结果必须分开。
6. `Core + Role Packs` 保持不变；Role Pack 不能提升事实、所有权或验证阶段。
7. **Internal truth controls wording, but internal audit language never leaks into the resume.**
8. **压缩表达不等于删除证据。合并同类项时，独立项目不得静默消失。**

## 四层架构

### 1. Evidence Core

负责事实等级、项目层级、个人贡献、能力所有权、验证成熟度、职业证据库和 Claim Defensibility。

### 2. Role Intelligence

负责定位、JD 匹配、Role Packs 和可迁移问题结构。岗位意愿是输入，证据决定当前可防守定位。

### 3. Recruiter Translation

负责将内部判断转换为项目背景、个人动作、可观察行为、价值、结果证据和招聘方可读表述。读取 [招聘表达规则](references/recruiter-translation.md) 与 [招聘表达卡](templates/recruiter-translation-card.md)。

### 4. Resume Rendering

负责内容架构、HTML、A4、分页、视觉层级、编辑和打印。Renderer 不能决定项目取舍、修改事实或加强措辞。读取 [信息结构选择器](references/resume-architecture-selector.md) 和 [Renderer Packs](renderers/README.md)。

## 模式选择

### A. 深度访谈与能力发现

用户不知道优势、经历杂乱、想探索天赋，或不确定 AI 项目是否算个人能力时，先深访，不直接写简历。

分开：

1. **Natural Tendencies**：内部定位线索；
2. **Work-ready Capabilities**：有可观察行为、项目证据和所有权支持；
3. **Capability Gaps / Claim Boundaries**：当前证据不足的能力。

读取 [深访方法](references/deep-interview-to-resume.md)、[深访模板](templates/deep-interview.md) 和 [能力原语](references/capability-primitives.md)。一次问一个核心问题，至少两个独立事件支持后才视为稳定行为。

### B. 职业证据库与母版

用于重建事实源和支持连续投递。先定位审计，再建立母版。母版保存全部独立项目和可防守证据，不等于投递版。

### C. JD 定制

只从证据库选择、排序和翻译，不为匹配关键词补写事实。每次生成内部 [定制差异记录](templates/tailoring-delta.md)。

### D. 简历文件交付

当用户需要 HTML、A4 或 PDF 时，先完成内容架构，再复制合适的 Renderer。内容多时优先两页，不用极小字号或删除项目强塞一页。

### E. 反馈审查

逐条判断 `采纳 / 修改后采纳 / 不采纳 / 需要更多证据`，说明筛选价值、真实性、岗位匹配和面试风险。

### F. Role Pack

完成 Core 审计后加载岗位包。当前内置 [AIPM 岗位包](packs/ai-product-manager/PACK.md)。

## 执行流程

### 1. 明确目标与材料

确认目标岗位、职级、行业、地区、语言、页数、文件格式、已有简历和证据。保留源文件；缺失项标记待确认，先处理已知部分。使用 [信息采集模板](templates/intake.md)。

### 2. 必要时先深访

从具体事件采集触发、约束、动作、决策、他人/AI 贡献、结果、失败和反例：

```text
自然倾向 → 可观察行为 → 能力原语 → 项目证据 → 所有权 → 成熟度
```

不要把好奇心、学习能力、责任心或沟通能力直接写成高价值要点。

### 3. 建立 Fact Matrix

将重要事实分类为 `Verified / User-confirmed / External/Public / Estimated / Inferred / Unknown`，核对动作归属、数字口径、0→1、系统范围、上线状态和职称。填写 [Fact Matrix](templates/fact-matrix.md)，规则见 [事实与证据](references/fact-integrity-and-evidence.md)。

每个独立项目分配稳定项目 ID。不得因为问题相似而合并源记录。

### 4. 审计能力所有权

对高强度 claim 记录最高可证明级别：

- `L0 Exposure`
- `L1 AI-assisted Output`
- `L2 Explain`
- `L3 Modify / Debug`
- `L4 Reproduce / Validate`
- `L5 Real-world Validated`

项目成熟度和个人所有权是两个维度。读取 [能力所有权](references/capability-ownership.md)，填写 [所有权矩阵](templates/capability-ownership-matrix.md)。

### 5. 审计 AI 辅助项目

对 Codex、Claude Code、Cursor 等项目检查：

```text
Explain → Modify → Debug → Reproduce → Validate
```

检查设计理由、替代方案、数据流、Agent 必要性、Rule/Workflow/Agent/Human 边界、成功指标、失败处理、调用链和 Bad Cases。解释权不足时输出：

> 先补项目解释权，不要继续强化简历 claim。

读取 [AI 辅助项目审计](references/ai-assisted-project-audit.md)。

### 6. 标记 Validation Maturity

```text
Concept → Prototype → Runnable Demo / POC → Offline Eval
→ Structured User Interview / Expert Review → Pilot / Real User Usage
→ Production → Measured Business Outcome
```

简历不得越级。使用 [验证成熟度模板](templates/validation-maturity.md)。

### 7. 能力抽象与职业定位

把证据写入 [Capability Library](templates/capability-library.md)，能力必须遵循：

```text
Capability → Observable Behavior → Evidence
```

完成 [定位审计](templates/positioning-audit.md)，输出最强定位、相邻定位、不建议定位、核心垂直能力、横向能力和最大证据缺口。

### 8. 建立 Career Evidence Base 与 Master Resume

母版保存全部独立项目、指标、作品、能力、表述和面试证据。读取 [母版架构](templates/master-resume-architecture.md) 和 [母版与定制简历](references/master-and-tailored-resume.md)。

### 9. 匹配 JD / Role Pack

先比较直接相似，再比较相邻问题结构和能力迁移。使用 [JD 矩阵](templates/jd-matrix.md)。Role Pack 只决定证据优先级和岗位语言。

### 10. 运行 Claim Defensibility Matrix

记录 Evidence Class / Strength、Ownership Level、Explain/Modify/Debug、真实用户/生产验证、Interview Risk 和 Safe Wording。优先选择：

> 高 JD 相关性 × 高证据强度 × 高能力所有权 × 低面试穿透风险

硬边界不能被评分抵消。使用 [防守矩阵](templates/claim-defensibility-matrix.md)。

### 11. 招聘表达与要点编译

不要从原始经历直接润色。使用 [简历要点编译器](references/resume-bullet-compiler.md)：

```text
事实 → 个人动作 → 可观察行为 → 能力 → 价值 → 证据 → JD → 招聘表述
```

内部层可以保存风险、边界和缺失证据；正式层只输出招聘方可读字段。通过 [正式输出清理](checklists/external-output-sanitization.md) 后才能进入 Renderer。

### 12. 审计独立项目去向

压缩时每个母版项目必须：

1. 独立展示；
2. 归组但仍保留子项目名称与独立贡献；
3. 有意不展示，并在内部定制差异记录原因。

禁止跨项目拼接动作、数字或结果。项目层级见 [Project Hierarchy](references/project-hierarchy.md)。

### 13. 选择信息架构与 Renderer

先根据岗位、职级、内容密度、项目数量、作品集和页数选择信息架构，再选择：

- [clean-professional](renderers/clean-professional/RENDERER.md)：产品、运营、业务和多数中文社招；
- [high-density-technical](renderers/high-density-technical/RENDERER.md)：AIPM、AI、Agent、研发和技术产品。

默认不显示证件照区域。复制模板为用户专属文件，不修改 Renderer 源文件。

### 14. Print / PDF QA

实际打开 HTML 并检查 A4、页数、空白页、标题孤立、要点拆页、链接溢出、中文字体、工具栏隐藏、最小字号和文本复制。执行 [渲染检查](checklists/rendering-qa.md)。内容过多时使用两页。

### 15. 面试证据与最终交付

对最显眼的 3–5 个 claim 生成 [Interview Evidence Card](templates/interview-evidence-card.md)。最后执行 [Final Resume Audit](checklists/final-resume-audit.md)。

除非用户明确要求审计报告，对外只交付正式简历文件及必要使用说明；事实矩阵、风险、边界和定制差异保持内部。

## 禁止项

- 编造经历、职级、技能、数字、客户、上线或业务结果；
- 把参与写成主导，把团队成果写成个人成果；
- 把公开或估算数据写成个人系统结果；
- 把 Demo、Offline Eval 或生产背景升级成更强结果；
- 用 AI 生成物推导独立开发能力；
- 直接把人格标签写成核心能力；
- 让内部审计字段或审计报告式语言进入正式简历；
- 因合并同类项让独立项目静默消失；
- 跨独立项目拼接事实、动作、数字或结果；
- 让 Renderer 修改内容逻辑、事实或 positioning；
- 默认生成空证件照框；
- 用极小字号强行压成一页。

## 按需读取

| 场景 | 读取 |
|---|---|
| 深访与能力探索 | [深访方法](references/deep-interview-to-resume.md)、[能力原语](references/capability-primitives.md) |
| 所有权与 AI 项目 | [能力所有权](references/capability-ownership.md)、[AI 项目审计](references/ai-assisted-project-audit.md) |
| 定位、母版和项目保全 | [核心架构](references/core-architecture.md)、[母版与定制](references/master-and-tailored-resume.md)、[项目层级](references/project-hierarchy.md) |
| JD 与岗位知识 | [能力迁移](references/transferable-capability-mapping.md)、[JD 规则](references/jd-keyword-matching.md)、[AIPM Pack](packs/ai-product-manager/PACK.md) |
| 招聘表达 | [招聘表达](references/recruiter-translation.md)、[要点编译器](references/resume-bullet-compiler.md) |
| HTML / PDF | [信息结构选择](references/resume-architecture-selector.md)、[Renderer Packs](renderers/README.md)、[渲染检查](checklists/rendering-qa.md) |
| 最终交付 | [正式输出清理](checklists/external-output-sanitization.md)、[最终审计](checklists/final-resume-audit.md) |
