# 核心架构

## 产品模型

Jianli 不是一次性润色器，而是三个系统的组合：

> Career Evidence Engine + Recruiter Translation Engine + Resume Renderer

```text
具体经历
→ 深访与稳定行为
→ 事实 / 证据 / 能力所有权审计
→ 职业证据库与定位
→ Role Pack / JD 匹配
→ Claim 选择
→ 招聘表达层
→ 简历信息结构
→ Renderer Pack
→ 打印 / PDF 检查
→ 面试证据验证
```

## 四层所有权

### Evidence Core

负责：

- facts and evidence classes;
- Employer / Client / Platform / Module / Contribution boundaries;
- capability primitives and ownership levels;
- AI-assisted project audit;
- validation maturity;
- positioning audit;
- claim defensibility;
- JD similarity and transferability;
- quantification, versioning, information hierarchy, and interview evidence.

### Role Intelligence

负责 JD 匹配、Role Packs、岗位定位和可迁移能力映射。

### Recruiter Translation

负责把通过审计的证据转换为招聘方可读的项目背景、个人动作、可观察行为、价值与证据。它不能修改事实或提升措辞边界。

### Resume Rendering

负责 HTML、A4、分页、视觉层级、编辑和打印。Renderer 只读取正式简历字段，不能访问内部审计字段。

Role Packs own:

- role-specific hiring dimensions;
- vocabulary and evidence emphasis;
- portfolio strategy;
- role-specific writing and red flags.

Role Packs cannot raise Evidence Class, Ownership Level, or Validation Maturity.

## 两条硬隔离

1. **Internal truth controls wording, but internal audit language never leaks into the resume.**
2. **压缩表达不等于删除证据。合并同类项时，独立项目不得静默消失。**

每个独立项目必须进入以下一种去向：独立展示、归组后仍可识别、有理由地不展示并记录于内部定制差异。职业证据库和母版永远保留原始项目单元。

## Independent axes

Do not collapse:

- fact truth into capability ownership;
- candidate ownership into project maturity;
- project maturity into business outcome;
- natural tendency into work-ready capability;
- JD relevance into claim defensibility.

## Unit of decision

The primary decision unit is one important claim. For every claim ask:

1. What happened and what is the source?
2. What did the candidate personally own?
3. How far was the project validated?
4. What capability primitive does it prove?
5. Which problem structures can it transfer to?
6. Can the wording survive the likely interview path?
7. Can it be translated without exposing internal audit language?
8. If compressed, where does the original independent project remain visible or recorded?
