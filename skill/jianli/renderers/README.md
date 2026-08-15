# Renderer Packs

Renderer Pack 只负责视觉呈现，不负责事实核验、岗位定位、项目选择或措辞强化。

## 使用顺序

```text
职业证据库
→ 招聘表达卡
→ 正式简历字段
→ 信息结构选择
→ Renderer
→ 打印与 PDF 检查
```

## 正式字段白名单

内置模板的 `data-resume-field` 只能使用：

- `candidate_identity`
- `contact`
- `education`
- `skills`
- `recruiter_readable_claim`
- `project_context`
- `candidate_action`
- `observable_behavior`
- `scale`
- `evidence`
- `value`
- `target_role_language`
- `links`

事实矩阵、风险、所有权、缺失证据、验证阶段和内部边界不能作为 Renderer 字段。它们只能在上游决定哪些内容可用以及措辞强度。

## 内置包

### clean-professional

中文求职默认方案。单栏、简洁、工作与项目并重，适合产品、运营、业务和多数社招场景。

### high-density-technical

高密度单栏方案。项目证据与技术机制优先，适合 AIPM、AI、Agent、研发和技术产品岗位。

## 共同契约

- 默认不显示证件照区域；
- HTML 文字可选择、可编辑、可复制；
- 使用 A4 和打印样式；
- 工具栏打印时隐藏；
- 内容过多时允许自然扩展为两页；
- 不复制外部模板代码、品牌素材或专有资源；
- 不在模板中写入候选人的真实个人信息。
