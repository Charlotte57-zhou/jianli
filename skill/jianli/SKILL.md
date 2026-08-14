---
name: jianli
description: 当用户要审查、重写、优化、定制或对比简历/CV，或针对公司、岗位、JD 制作投递版本时使用。先建立职业证据库与母版，再生成岗位定制简历和面试证据卡；优化招聘者理解、经历相似度、可信量化与可追问性，同时保持事实、归属、指标、职级、技术和上线状态真实。
---

# 简历证据库

先核事实，再写简历。

目标不是把经历“写得更厉害”，而是让正确的证据更快被招聘者看见：

> 原始经历 → 事实矩阵 → 职业证据库 → 母版 → JD 匹配 → 定制简历 → 面试证据卡

## 核心契约

1. **允许增强定位，不允许增强事实。**
2. 保留原文件；编辑时创建新版本。
3. 不把“参与”改成“主导”，不把公开数据改成个人成果。
4. 不把估算写成实测，不把 Demo/离线项目写成生产上线。
5. 不为匹配 JD 添加没有证据的技术、方法、职级、职责或指标。
6. 清楚区分雇主、客户、平台、项目、模块与候选人的个人贡献。
7. 无可靠 ROI 时，量化规模、复杂度、覆盖面、交付深度与验证强度。
8. 每份投递简历都应成为候选人希望展开的面试议程。

详细边界见 [事实与证据规则](references/fact-integrity-and-evidence.md)。Role Pack 只能补充岗位知识，不得覆盖本契约。

## 选择工作模式

### A. 职业证据库 / 母版

适用于暂无具体 JD、要重建经历库存，或计划连续投递多个岗位。

产出：事实矩阵、指标库、作品库、能力库、bullet 库和母版简历。母版是事实源，不一定直接投递。

### B. 公司 / 岗位 / JD 定制

适用于已有公司、岗位或 JD。

优先级固定为：

> 直接相似经历 > 相邻问题结构 > 有证据的可迁移能力 > 通用特质

只在语义等价且有候选人证据时复用 JD 关键词。

### C. 第三方建议评审

适用于评审招聘方、导师、朋友或其他 AI 给出的修改意见。

逐条给出：`采纳 / 修改后采纳 / 不采纳 / 需要更多证据`，并说明筛选价值、真实性、岗位匹配和面试风险。

### D. Role Pack

当 `packs/` 下存在目标岗位包时，完成通用事实审计后再加载。当前内置 [AI 产品经理岗位包](packs/ai-product-manager/PACK.md)。

没有对应岗位包时，优先依据用户提供的真实 JD 归纳临时岗位画像，不凭空发明招聘标准。

## 执行流程

### 1. 明确目标并保留源文件

确认以下已知信息；缺失项标记为“待确认”，先基于现有证据继续：

- 目标岗位、职级、公司/行业和地区；
- 简历语言、页数与文件格式；
- 母版还是定制版；
- 原简历、JD、项目材料、作品与反馈。

需要结构化收集时使用 [信息采集模板](templates/intake.md)。

### 2. 先做事实矩阵

对关键主张分类：

- `Verified`：可由文件、代码、数据、证书或运行结果核对；
- `User-confirmed`：用户明确确认；
- `External/Public`：外部公开背景；
- `Estimated`：有方法但未实测；
- `Inferred`：基于证据的推断；
- `Unknown`：仍缺证据。

重点核对：动作归属、数字口径、0→1 边界、系统范围、上线状态、职称和真实结果。使用 [事实矩阵](templates/fact-matrix.md)。

### 3. 建立可复用职业证据库

整理四类库存：

- **经历库**：角色、场景、项目/模块、动作、交付物、结果；
- **指标库**：定义、分母、时间点、来源、属性和安全写法；
- **作品库**：原型、PRD、报告、代码、测试、证书等；
- **能力与 bullet 库**：同一事实的业务、产品、技术、交付等真实表达。

能力迁移必须遵循：具体经历 → 问题结构 → 可迁移能力 → 目标场景。见 [能力迁移](references/transferable-capability-mapping.md) 和 [能力库模板](templates/capability-library.md)。

### 4. 建立岗位画像并做 JD 证据匹配

有 Role Pack 时加载；没有时从真实 JD 归纳：核心职责、招聘维度、必备证据、关键词、常见指标、作品期待和风险项。

对每项 JD 要求记录：重要度、直接证据、相邻证据、可迁移证据、缺口、放置位置和决策。使用 [JD 矩阵](templates/jd-matrix.md)，规则见 [JD 关键词匹配](references/jd-keyword-matching.md)。

### 5. 定位、取舍与改写

先写一句内部定位：

> 目标身份 + 最相关经历 + 差异点 + 证明

然后决定哪些内容前置、压缩、删除或保留。每个版块都问：

> 它是否帮助目标招聘者决定发出面试邀请？

bullet 通常组合以下 3–4 项，不强套单一公式：

- 问题/业务背景；
- 候选人动作；
- 范围/复杂度；
- 协作/交付；
- 结果/验证。

量化优先使用可归属的规模、复杂度、交付和验证数字；结果类数字必须可测且可归因。见 [可信量化](references/quantification.md)。

大型项目需先理清雇主、客户、平台、项目和个人贡献，见 [项目层级](references/project-hierarchy.md)。版式只服务信息优先级，见 [视觉与信息层级](references/visual-and-information-hierarchy.md)。

### 6. 做面试议程测试

检查最显眼的 5 个主张：如果面试 70% 时间围绕它们展开，是否对候选人有利？

若不利，重新排序、缩短、删除或替换。为核心主张生成 [面试证据卡](templates/interview-evidence-card.md)：结论、个人动作、证据、边界、失败/权衡和可追问点。

### 7. 交付与审计

至少交付：

1. 本轮目标与证据边界；
2. 关键取舍及原因；
3. 新版简历或明确修改稿；
4. 待确认事实；
5. 版本名与下一步使用建议。

最终运行 [简历审计清单](checklists/final-resume-audit.md)，确认事实、关键词、数字、层级、上线状态、视觉重点和面试可辩护性。

推荐投递文件名：`姓名-公司-岗位-简历.pdf`。内部版本规则见 [版本与命名](references/resume-versioning-and-naming.md)。

## 按需读取

只加载当前任务需要的文件：

| 场景 | 读取 |
|---|---|
| 全流程或模式选择 | [架构](references/core-architecture.md)、[优化流程](references/resume-optimization-playbook.md) |
| 母版与定制版 | [母版/定制关系](references/master-and-tailored-resume.md)、[母版模板](templates/master-resume-architecture.md)、[定制简报](templates/tailoring-brief.md) |
| 事实、数字或归属风险 | [事实规则](references/fact-integrity-and-evidence.md)、[可信量化](references/quantification.md)、[项目层级](references/project-hierarchy.md) |
| JD 匹配 | [关键词规则](references/jd-keyword-matching.md)、[JD 矩阵](templates/jd-matrix.md) |
| 跨行业/跨岗位 | [能力迁移](references/transferable-capability-mapping.md)、[岗位画像模板](templates/role-profile.md) |
| 版式和信息顺序 | [视觉层级](references/visual-and-information-hierarchy.md) |
| 参考改写 | [前后对比示例](examples/before-after-snippets.md) |
| 新岗位包 | [Role Pack 规则](references/role-pack-system.md)、[岗位包模板](packs/_template/PACK.md) |

## AI 产品经理岗位包

当目标是 AI 产品经理、Agent 产品经理、LLM 应用产品经理或企业 AI 产品岗位时，读取 [PACK.md](packs/ai-product-manager/PACK.md)，再按需读取其招聘维度、关键词、写作、AI Coding、作品链接和匿名案例。

表达顺序优先为：

> 用户/业务问题 → 产品判断 → 为什么用或不用 AI → 个人决策 → 技术机制 → 评测与边界

明确区分已实现原型、离线评测、设计假设、非目标和未观察到的生产结果。

## 禁止项

- 编造经历、学历、职级、技术、指标或结果；
- 用关键词堆砌替代证据匹配；
- 用模糊“能力强”掩盖领域缺口；
- 把同一母版无差别投给所有岗位；
- 为显得量化而虚构百分比或 ROI；
- 只给润色句子，却不处理定位、证据和信息层级。
