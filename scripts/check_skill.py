#!/usr/bin/env python3
"""Validate the Jianli repository and its installable Skill contract."""

from pathlib import Path
import re
import sys


REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skill" / "jianli"
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
        "templates/intake.md",
        "templates/fact-matrix.md",
        "templates/capability-library.md",
        "templates/master-resume-architecture.md",
        "templates/role-profile.md",
        "templates/jd-matrix.md",
        "templates/tailoring-brief.md",
        "templates/rewrite-plan.md",
        "templates/interview-evidence-card.md",
        "templates/version-ledger.md",
        "templates/deep-interview.md",
        "templates/capability-ownership-matrix.md",
        "templates/claim-defensibility-matrix.md",
        "templates/positioning-audit.md",
        "templates/validation-maturity.md",
        "checklists/final-resume-audit.md",
        "examples/before-after-snippets.md",
        "examples/capability-chain-example.md",
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
    "Deep Interview & Capability Discovery",
    "L0 Exposure",
    "L1 AI-assisted Output",
    "L2 Explain",
    "L3 Modify / Debug",
    "L4 Reproduce / Validate",
    "L5 Real-world Validated",
    "Claim Defensibility Matrix",
    "Career Positioning Audit",
    "Validation Maturity",
    "先补项目解释权，不要继续强化简历 claim",
]
for marker in required_skill_markers:
    if marker not in skill_text:
        errors.append(f"SKILL.md: missing architecture marker: {marker}")

expected_chain = """具体经历
→ 深访发现的稳定行为
→ 可观察职业能力
→ 证据
→ 能力所有权级别
→ 可迁移问题结构
→ 目标 JD / Role Pack
→ 可防守简历表述
→ 面试追问证据"""
if expected_chain not in skill_text:
    errors.append("SKILL.md: complete episode-to-interview chain is missing or out of order")

required_resource_links = [
    "references/deep-interview-to-resume.md",
    "references/capability-ownership.md",
    "references/ai-assisted-project-audit.md",
    "references/capability-primitives.md",
    "templates/deep-interview.md",
    "templates/capability-ownership-matrix.md",
    "templates/claim-defensibility-matrix.md",
    "templates/positioning-audit.md",
    "templates/validation-maturity.md",
    "examples/capability-chain-example.md",
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
    section = section_match.group(1)
    for field in (
        "Definition",
        "Observable behavior",
        "Typical evidence",
        "Common miswrite",
        "Transfers to",
        "Role mapping",
    ):
        if f"**{field}:**" not in section:
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

example_text = read_utf8(SKILL / "examples" / "capability-chain-example.md")
for marker in (
    "Stable behavior decision",
    "Capability primitives",
    "Ownership Level",
    "Validation Maturity",
    "Career Positioning Audit",
    "JD mapping",
    "Claim Defensibility",
    "Interview evidence",
):
    if marker not in example_text:
        errors.append(f"capability-chain-example.md: missing marker: {marker}")

openai_yaml = SKILL / "agents" / "openai.yaml"
if openai_yaml.is_file():
    metadata = read_utf8(openai_yaml)
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s*{key}:\s*\".+\"\s*$", metadata, flags=re.M):
            errors.append(f"agents/openai.yaml: missing quoted {key}")
    if "$jianli" not in metadata:
        errors.append("agents/openai.yaml: default_prompt must mention $jianli")

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
):
    if marker not in pack_text:
        errors.append(f"AI Product Manager pack: missing marker: {marker}")

link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
phone_pattern = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
text_files = [
    path
    for path in REPO.rglob("*")
    if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts
]
for path in text_files:
    if path.suffix.lower() not in {".md", ".py", ".yaml", ".yml"} and path.name not in {
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
    if doc.is_file() and "2.1.0" not in read_utf8(doc):
        errors.append(f"{doc.name}: missing version 2.1.0")

if errors:
    print("Jianli check failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

runtime_files = sum(1 for path in SKILL.rglob("*") if path.is_file())
print("Jianli check passed.")
print(f"Repository: {REPO}")
print(f"Runtime files: {runtime_files}")
print(f"SKILL.md lines: {len(skill_text.splitlines())}")
print(f"Capability primitives: {len(primitives)}")
print("Architecture chain: reachable")
print("Privacy patterns: clear")
