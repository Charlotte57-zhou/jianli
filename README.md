# Jianli v2.1.0 · 简历证据库

> **先核事实，再定能力，最后写简历。**

`jianli` 是面向中文求职者的开源 Agent Skill。它不会把人格标签包装成能力，也不会把 AI 生成的项目直接包装成候选人的独立开发能力。

它完成的是一条更长、但更可防守的链路：

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

## v2.1.0 解决什么问题

普通简历优化常停在“这件事做没做过”。但在 AI Coding 普及后，更重要的问题是：

> **候选人到底掌握到什么程度？能否解释、修改、Debug、复现和验证？**

因此 v2.1.0 在事实核验之外新增五个核心判断：

1. **稳定行为模式**：优势来自重复行为，不来自自我贴标签；
2. **Capability Ownership**：区分接触、AI 辅助输出、解释、修改、复现和真实验证；
3. **Validation Maturity**：区分 Concept、Demo、Offline Eval、Pilot、Production 和业务结果；
4. **Career Positioning Audit**：岗位定位由证据决定，不由愿望自动决定；
5. **Claim Defensibility**：优先选择相关、证据强、所有权高且面试风险低的 claim。

## 核心原则保持不变

1. **Strengthen positioning. Never strengthen facts.**
2. **One career evidence base, many truthful tailored resumes.**
3. **Direct similarity > adjacent similarity > transferable capability > generic traits.**
4. `Employer / Client / Platform / Module / Contribution` 必须分层。
5. `Public / Internal / Estimated` 数据必须区分。
6. `Core + Role Packs` 架构不变。

## Capability Ownership Ladder

| Level | 含义 | 简历边界 |
|---|---|---|
| L0 Exposure | 接触、看过、参与过 | 不写成掌握或独立负责 |
| L1 AI-assisted Output | 借助 AI 产出结果，解释和修改有限 | 可写 AI 辅助产出，不写独立开发 |
| L2 Explain | 可脱离资料解释流程、逻辑和关键决策 | 可写理解、定义或设计过的明确范围 |
| L3 Modify / Debug | 可修改关键行为并定位故障 | 可写修改、调试和迭代 |
| L4 Reproduce / Validate | 可独立复现核心链路并设计验证 | 可写独立构建/复现的真实范围 |
| L5 Real-world Validated | 满足 L4，且经真实使用、试点或生产验证 | 可写对应范围内的真实验证 |

项目上线不代表候选人自动达到 L5；候选人达到 L4，也不代表项目已经产生生产价值。

## AI 辅助项目怎么审计

对于 Codex、Claude Code、Cursor 等项目，不按“用了什么工具”判断能力，而按以下链路检查：

```text
Explain → Modify → Debug → Reproduce → Validate
```

候选人还要能回答：

- 为什么这样设计，为什么不用其他方案？
- 核心数据流和调用链是什么？
- Agent 为什么存在？
- Rule / Workflow / Agent / Human 边界是什么？
- 成功指标和主要 Bad Case 是什么？
- 失败或证据不足时怎么办？

解释权不足时，Skill 会提示：

> **先补项目解释权，不要继续强化简历 claim。**

## Deep Interview & Capability Discovery

当用户说：

- “我不知道自己的优势”；
- “帮我探索天赋和能力”；
- “我的经历很杂，不知道怎么定位”；
- “做了很多 AI 项目，哪些真正算我的能力？”

`jianli` 不会立刻写简历，而是先拆成：

1. **Natural Tendencies**：自然倾向，只作为内部定位假设；
2. **Work-ready Capabilities**：可由工作或项目证明的职业能力；
3. **Capability Gaps / Claim Boundaries**：当前不能包装或证据不足的能力。

转换方式：

```text
“容易发现哪里不对”
→ 比较来源、状态和预期约束
→ anomaly_inconsistency_detection
→ 实际缺陷 / 对账 / Bad Case 证据
→ L2/L3（取决于解释和 Debug 证据）
```

“好奇心强、学习能力强、责任心强、沟通能力强”不会直接成为核心 bullet。

## Claim Defensibility Matrix

每个重要 claim 都记录：

- Evidence Class / Strength；
- Ownership Level；
- Validation Maturity；
- Can Explain / Modify / Debug；
- Real User / Production Validation；
- Interview Risk；
- Safe Wording。

选择原则：

> **高 JD 相关性 × 高证据强度 × 高能力所有权 × 低面试穿透风险**

这不是用总分掩盖硬边界：没有生产证据就不写生产结果，低于 L4 就不默认写独立开发。

## Career Positioning Audit

生成 Master Resume 前，Skill 必须给出：

- 当前最强、最可证实的岗位定位；
- 次优相邻定位；
- 不建议强行包装的定位；
- 核心垂直能力；
- 横向可迁移能力；
- 最大证据缺口和下一步证明动作。

用户可以决定想去哪里，但简历不能假装证据已经到达那里。

## AI 产品经理 Role Pack

内置岗位包重点覆盖：

- 复杂业务系统 AI 化；
- Rule / Workflow / Agent / Human 边界；
- 高可信、高风险流程；
- 异常调查与决策支持；
- Evidence / Responsibility / Human Confirmation；
- Eval / Bad Case；
- AI-assisted engineering ownership；
- 真实用户验证成熟度；
- 项目解释权。

AI Coding 默认优先写：

> **AI 原生产品构建与验收能力**

而不是默认写“独立全栈开发能力”。

## 30 秒安装

下载 Release 中的 `jianli-skill-v2.1.0.zip`，解压后将 `jianli` 文件夹放到：

```text
Windows: %USERPROFILE%\.codex\skills\jianli
macOS/Linux: ~/.codex/skills/jianli
```

重新打开 Codex 后使用 `$jianli`。

从源码安装时，将 `skill/jianli/` 复制到 Skills 目录。

## 直接复制这些提示词

### 深访探索能力

```text
请使用 $jianli 进入 Deep Interview & Capability Discovery。一次问我一个问题，从具体经历识别稳定行为、能力原语、所有权级别和能力边界。先完成定位审计，不要直接写简历。
```

### 审计 AI Coding 项目

```text
请使用 $jianli 审计我的 AI 辅助项目。按 Explain、Modify、Debug、Reproduce、Validate 检查，区分我的贡献、AI 贡献、Ownership Level 和 Validation Maturity，再给安全简历表述。
```

### 针对 JD 定制

```text
请使用 $jianli 分析这份 JD。先做 JD Evidence Matrix 和 Claim Defensibility Matrix，再从母版中生成可防守的定制简历。没有证据或所有权不足的关键词不要添加。
```

### AI 产品经理

```text
请使用 $jianli 和 AI 产品经理 Role Pack。重点检查复杂业务 AI 化、Rule/Workflow/Agent/Human 边界、Eval/Bad Case、项目解释权和真实用户验证成熟度。
```

## v2.1.0 目录

```text
jianli/
├── README.md
├── README.en.md
├── CHANGELOG.md
├── LICENSE
├── scripts/check_skill.py
└── skill/jianli/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    │   ├── capability-ownership.md
    │   ├── ai-assisted-project-audit.md
    │   ├── capability-primitives.md
    │   ├── deep-interview-to-resume.md
    │   └── ...
    ├── templates/
    │   ├── deep-interview.md
    │   ├── capability-ownership-matrix.md
    │   ├── claim-defensibility-matrix.md
    │   ├── positioning-audit.md
    │   ├── validation-maturity.md
    │   └── ...
    ├── checklists/final-resume-audit.md
    ├── examples/
    └── packs/ai-product-manager/
```

## 自检

```bash
python scripts/check_skill.py
```

自检覆盖：必需文件、frontmatter、渐进式链接、完整链路、L0–L5、十个能力原语、AI PM 边界、UTF-8、Markdown 断链、行尾空格及明显电话/邮箱模式。

## 贡献边界

欢迎贡献新 Role Pack、匿名案例和能力原语映射。请保持：

- 不写候选人真实姓名、电话、邮箱或雇主敏感信息；
- 不把社区经验写成官方招聘标准；
- 不把 AI 输出、Demo、Offline Eval 或生产背景升级成更强的个人能力与业务结果；
- 不削弱 Core 的事实、所有权和成熟度边界。

## License

[MIT](LICENSE)
