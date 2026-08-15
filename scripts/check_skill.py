#!/usr/bin/env python3
"""Validate the Jianli repository and installable Skill contract."""

from pathlib import Path
import re
import sys


REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skill" / "jianli"
VERSION = "3.1.0"
errors: list[str] = []


def require(base: Path, paths: list[str]) -> None:
    for rel in paths:
        if not (base / rel).is_file():
            errors.append(f"missing required file: {(base / rel).relative_to(REPO)}")


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"not UTF-8: {path.relative_to(REPO)}: {exc}")
        return ""


require(REPO, ["README.md", "README.en.md", "LICENSE", "CHANGELOG.md"])
require(
    SKILL,
    [
        "SKILL.md",
        "agents/openai.yaml",
        "references/core-architecture.md",
        "references/fact-integrity-and-evidence.md",
        "references/master-and-tailored-resume.md",
        "references/jd-keyword-matching.md",
        "references/transferable-capability-mapping.md",
        "references/quantification.md",
        "references/project-hierarchy.md",
        "references/visual-and-information-hierarchy.md",
        "references/resume-versioning-and-naming.md",
        "references/role-pack-system.md",
        "references/resume-optimization-playbook.md",
        "references/capability-ownership.md",
        "references/ai-assisted-project-audit.md",
        "references/capability-primitives.md",
        "references/deep-interview-to-resume.md",
        "references/recruiter-translation.md",
        "references/resume-bullet-compiler.md",
        "references/resume-architecture-selector.md",
        "templates/intake.md",
        "templates/fact-matrix.md",
        "templates/capability-library.md",
        "templates/master-resume-architecture.md",
        "templates/role-profile.md",
        "templates/jd-matrix.md",
        "templates/tailoring-brief.md",
        "templates/tailoring-delta.md",
        "templates/rewrite-plan.md",
        "templates/interview-evidence-card.md",
        "templates/version-ledger.md",
        "templates/deep-interview.md",
        "templates/capability-ownership-matrix.md",
        "templates/claim-defensibility-matrix.md",
        "templates/positioning-audit.md",
        "templates/validation-maturity.md",
        "templates/recruiter-translation-card.md",
        "checklists/final-resume-audit.md",
        "checklists/external-output-sanitization.md",
        "checklists/rendering-qa.md",
        "examples/before-after-snippets.md",
        "examples/capability-chain-example.md",
        "examples/recruiter-translation-example.md",
        "examples/acceptance-cases.md",
        "packs/README.md",
        "packs/_template/PACK.md",
        "packs/_template/evaluation-dimensions.md",
        "packs/_template/keywords.md",
        "packs/ai-product-manager/PACK.md",
        "packs/ai-product-manager/evaluation-dimensions.md",
        "packs/ai-product-manager/keywords.md",
        "packs/ai-product-manager/writing-guide.md",
        "packs/ai-product-manager/ai-coding.md",
        "packs/ai-product-manager/portfolio-and-links.md",
        "packs/ai-product-manager/case-study.md",
        "renderers/README.md",
        "renderers/clean-professional/RENDERER.md",
        "renderers/clean-professional/template.html",
        "renderers/high-density-technical/RENDERER.md",
        "renderers/high-density-technical/template.html",
    ],
)

skill_md = SKILL / "SKILL.md"
skill_text = read_utf8(skill_md) if skill_md.is_file() else ""
if skill_text:
    match = re.match(r"---\n(.*?)\n---\n", skill_text, flags=re.S)
    if not match:
        errors.append("SKILL.md: invalid YAML frontmatter")
    else:
        frontmatter = match.group(1)
        if not re.search(r"^name:\s+jianli\s*$", frontmatter, flags=re.M):
            errors.append("SKILL.md: name must be jianli")
        if not re.search(r"^description:\s*\S.+$", frontmatter, flags=re.M):
            errors.append("SKILL.md: description is missing")
        keys = re.findall(r"^([A-Za-z0-9_-]+):", frontmatter, flags=re.M)
        if keys != ["name", "description"]:
            errors.append("SKILL.md: frontmatter must contain only name and description")
    if len(skill_text.splitlines()) > 500:
        errors.append("SKILL.md: exceeds the 500-line budget")

required_skill_markers = [
    "Evidence Core",
    "Role Intelligence",
    "Recruiter Translation",
    "Resume Rendering",
    "L0 Exposure",
    "L1 AI-assisted Output",
    "L2 Explain",
    "L3 Modify / Debug",
    "L4 Reproduce / Validate",
    "L5 Real-world Validated",
    "Claim Defensibility",
    "Validation Maturity",
    "Internal truth controls wording, but internal audit language never leaks into the resume.",
    "压缩表达不等于删除证据",
    "先补项目解释权，不要继续强化简历 claim",
]
for marker in required_skill_markers:
    if marker not in skill_text:
        errors.append(f"SKILL.md: missing architecture marker: {marker}")

expected_chain = """具体经历
→ 深访发现的稳定行为
→ 事实 / 证据 / 能力所有权审计
→ Career Evidence Base
→ 职业定位与 JD 匹配
→ Claim 选择
→ Recruiter Translation
→ Resume Architecture
→ Renderer Pack
→ Print / PDF QA
→ 面试追问证据"""
if expected_chain not in skill_text:
    errors.append("SKILL.md: complete evidence-to-rendering chain is missing or out of order")

required_resource_links = [
    "references/deep-interview-to-resume.md",
    "references/capability-ownership.md",
    "references/ai-assisted-project-audit.md",
    "references/capability-primitives.md",
    "references/recruiter-translation.md",
    "references/resume-bullet-compiler.md",
    "references/resume-architecture-selector.md",
    "templates/recruiter-translation-card.md",
    "templates/tailoring-delta.md",
    "checklists/external-output-sanitization.md",
    "checklists/rendering-qa.md",
    "renderers/README.md",
    "renderers/clean-professional/RENDERER.md",
    "renderers/high-density-technical/RENDERER.md",
]
for rel in required_resource_links:
    if rel not in skill_text:
        errors.append(f"SKILL.md: resource not reachable: {rel}")

primitive_text = read_utf8(SKILL / "references" / "capability-primitives.md")
primitives = [
    "complex_workflow_decomposition",
    "relation_boundary_state_modeling",
    "anomaly_inconsistency_detection",
    "closure_validation",
    "business_product_technology_translation",
    "data_source_and_ownership_reasoning",
    "ai_native_product_building",
    "evaluation_and_bad_case_design",
    "cross_system_coordination",
    "evidence_based_iteration",
]
for primitive in primitives:
    if f"`{primitive}`" not in primitive_text:
        errors.append(f"capability-primitives.md: missing {primitive}")
        continue
    section_match = re.search(
        rf"### `{re.escape(primitive)}`\n(.*?)(?=\n### `|\n## Usage rules)",
        primitive_text,
        flags=re.S,
    )
    if not section_match:
        errors.append(f"capability-primitives.md: unreadable section for {primitive}")
        continue
    for field in (
        "Definition",
        "Observable behavior",
        "Typical evidence",
        "Common miswrite",
        "Transfers to",
        "Role mapping",
    ):
        if f"**{field}:**" not in section_match.group(1):
            errors.append(f"capability-primitives.md: {primitive} missing {field}")

ownership_text = read_utf8(SKILL / "references" / "capability-ownership.md")
for level in ("L0", "L1", "L2", "L3", "L4", "L5"):
    if level not in ownership_text:
        errors.append(f"capability-ownership.md: missing {level}")

audit_text = read_utf8(SKILL / "references" / "ai-assisted-project-audit.md")
for target in (
    "Fact Matrix",
    "Capability Library",
    "Claim Defensibility Matrix",
    "Interview Evidence Card",
    "Final Resume Audit",
):
    if target not in audit_text:
        errors.append(f"ai-assisted-project-audit.md: missing synchronization target: {target}")

maturity_text = read_utf8(SKILL / "templates" / "validation-maturity.md")
for stage in (
    "Concept",
    "Prototype",
    "Runnable Demo / POC",
    "Offline Eval",
    "Structured User Interview / Expert Review",
    "Pilot / Real User Usage",
    "Production",
    "Measured Business Outcome",
):
    if stage not in maturity_text:
        errors.append(f"validation-maturity.md: missing stage: {stage}")

claim_text = read_utf8(SKILL / "templates" / "claim-defensibility-matrix.md")
for field in (
    "Evidence strength",
    "Ownership level",
    "Can explain?",
    "Can modify/debug?",
    "Real user validation?",
    "Production validation?",
    "Interview risk",
    "Safe wording",
):
    if field not in claim_text:
        errors.append(f"claim-defensibility-matrix.md: missing field: {field}")

translation_text = read_utf8(SKILL / "references" / "recruiter-translation.md")
internal_fields = {
    "evidence_class",
    "ownership_level",
    "claim_risk",
    "personal_boundary",
    "missing_evidence",
    "validation_maturity",
    "interview_risk",
    "unsupported_scope",
}
external_fields = {
    "candidate_identity",
    "contact",
    "education",
    "skills",
    "recruiter_readable_claim",
    "project_context",
    "candidate_action",
    "observable_behavior",
    "scale",
    "evidence",
    "value",
    "target_role_language",
    "links",
}
for field in internal_fields:
    if f"`{field}`" not in translation_text:
        errors.append(f"recruiter-translation.md: missing internal field: {field}")
for field in external_fields - {"candidate_identity", "contact", "education", "skills", "links"}:
    if f"`{field}`" not in translation_text:
        errors.append(f"recruiter-translation.md: missing external field: {field}")

preservation_sources = [
    SKILL / "SKILL.md",
    SKILL / "references" / "core-architecture.md",
    SKILL / "references" / "project-hierarchy.md",
    SKILL / "references" / "resume-bullet-compiler.md",
    SKILL / "templates" / "tailoring-delta.md",
    SKILL / "checklists" / "final-resume-audit.md",
]
for path in preservation_sources:
    text = read_utf8(path)
    if "独立项目" not in text:
        errors.append(f"{path.relative_to(REPO)}: missing independent-project preservation rule")

renderer_field_pattern = re.compile(r'data-resume-field="([a-z_]+)"')
renderer_names = ("clean-professional", "high-density-technical")
renderer_fields_seen: set[str] = set()
for renderer in renderer_names:
    renderer_dir = SKILL / "renderers" / renderer
    html_path = renderer_dir / "template.html"
    html = read_utf8(html_path)
    for marker in (
        "<!doctype html>",
        "@page",
        "size: A4",
        "@media print",
        'contenteditable="true"',
        "window.print()",
        "localStorage",
    ):
        if marker not in html:
            errors.append(f"renderer {renderer}: missing HTML contract marker: {marker}")
    fields = set(renderer_field_pattern.findall(html))
    renderer_fields_seen.update(fields)
    for field in fields - external_fields:
        errors.append(f"renderer {renderer}: non-external field: {field}")
    for field in internal_fields:
        if field in html:
            errors.append(f"renderer {renderer}: internal field leaked: {field}")
    for phrase in ("个人边界：", "待验证：", "不包装为", "不是 Owner", "我没有负责"):
        if phrase in html:
            errors.append(f"renderer {renderer}: internal audit phrase leaked: {phrase}")
    if re.search(r"photo|照片", html, flags=re.I):
        errors.append(f"renderer {renderer}: default photo area detected")
    if not fields:
        errors.append(f"renderer {renderer}: no external data fields")

if not {"recruiter_readable_claim", "project_context", "candidate_action", "evidence"}.issubset(renderer_fields_seen):
    errors.append("renderers: required recruiter-facing fields are not reachable")

for pack_dir in (SKILL / "packs").iterdir() if (SKILL / "packs").is_dir() else []:
    if not pack_dir.is_dir() or pack_dir.name.startswith(".") or pack_dir.name == "_template":
        continue
    for rel in ("PACK.md", "evaluation-dimensions.md", "keywords.md"):
        if not (pack_dir / rel).is_file():
            errors.append(f"pack {pack_dir.name}: missing {rel}")

pack_text = "\n".join(
    read_utf8(path) for path in (SKILL / "packs" / "ai-product-manager").glob("*.md")
)
for marker in (
    "Rule / Workflow / Agent / Human",
    "Bad Case",
    "Capability Ownership",
    "Validation Maturity",
    "AI-native product building",
    "Why AI",
    "What should not use AI",
    "Human Control",
    "Technical Proof",
    "Recruiter Translation",
):
    if marker not in pack_text:
        errors.append(f"AI Product Manager pack: missing marker: {marker}")

example_text = read_utf8(SKILL / "examples" / "acceptance-cases.md")
for case_number in range(1, 9):
    if f"Case {case_number}" not in example_text:
        errors.append(f"acceptance-cases.md: missing Case {case_number}")

translation_example = read_utf8(SKILL / "examples" / "recruiter-translation-example.md")
external_example_match = re.search(
    r"## 招聘表达\n(.*?)(?=\n## )", translation_example, flags=re.S
)
if not external_example_match:
    errors.append("recruiter-translation-example.md: missing external output example")
else:
    external_example = external_example_match.group(1)
    for phrase in ("个人边界：", "不是 Owner", "不包装为", "待验证："):
        if phrase in external_example:
            errors.append(f"recruiter translation example: internal phrase leaked: {phrase}")

delta_text = read_utf8(SKILL / "templates" / "tailoring-delta.md")
for marker in (
    "独立展示 / 归组展示 / 有意不展示",
    "没有项目因为合并同类项而静默消失",
    "没有跨项目拼接数字、动作或结果",
):
    if marker not in delta_text:
        errors.append(f"tailoring-delta.md: missing project coverage marker: {marker}")

openai_yaml = SKILL / "agents" / "openai.yaml"
if openai_yaml.is_file():
    metadata = read_utf8(openai_yaml)
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf'^\s*{key}:\s*".+"\s*$', metadata, flags=re.M):
            errors.append(f"agents/openai.yaml: missing quoted {key}")
    if "$jianli" not in metadata:
        errors.append("agents/openai.yaml: default_prompt must mention $jianli")

link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
phone_pattern = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
text_files = [
    path
    for path in REPO.rglob("*")
    if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts
]
for path in text_files:
    if path.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".html"} and path.name not in {
        "LICENSE",
        ".gitignore",
    }:
        continue
    text = read_utf8(path)
    for line_number, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            errors.append(f"trailing whitespace: {path.relative_to(REPO)}:{line_number}")
    if path.suffix.lower() == ".md":
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if path_part and not (path.parent / path_part).resolve().exists():
                errors.append(f"broken link: {path.relative_to(REPO)} -> {target}")
    for match in email_pattern.findall(text):
        errors.append(f"possible personal email: {path.relative_to(REPO)} -> {match}")
    for match in phone_pattern.findall(text):
        errors.append(f"possible personal phone: {path.relative_to(REPO)} -> {match}")

for doc in (REPO / "README.md", REPO / "README.en.md", REPO / "CHANGELOG.md"):
    if doc.is_file() and VERSION not in read_utf8(doc):
        errors.append(f"{doc.name}: missing version {VERSION}")

license_text = read_utf8(REPO / "LICENSE") if (REPO / "LICENSE").is_file() else ""
if "MIT License" not in license_text:
    errors.append("LICENSE: MIT License marker missing")

if errors:
    print("Jianli check failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

runtime_files = sum(1 for path in SKILL.rglob("*") if path.is_file())
print("Jianli check passed.")
print(f"Version: {VERSION}")
print(f"Repository: {REPO}")
print(f"Runtime files: {runtime_files}")
print(f"SKILL.md lines: {len(skill_text.splitlines())}")
print(f"Capability primitives: {len(primitives)}")
print(f"Renderer packs: {len(renderer_names)}")
print(f"External fields used: {len(renderer_fields_seen)}")
print("Architecture chain: reachable")
print("Internal/external isolation: clear")
print("Independent-project preservation: reachable")
print("Privacy patterns: clear")
