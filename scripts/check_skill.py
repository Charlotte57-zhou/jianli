#!/usr/bin/env python3
"""Validate the open-source repository and installable Jianli Skill."""

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
        "checklists/final-resume-audit.md",
        "examples/before-after-snippets.md",
        "packs/README.md",
        "packs/_template/PACK.md",
        "packs/_template/evaluation-dimensions.md",
        "packs/_template/keywords.md",
        "packs/ai-product-manager/PACK.md",
        "packs/ai-product-manager/evaluation-dimensions.md",
        "packs/ai-product-manager/keywords.md",
        "packs/ai-product-manager/writing-guide.md",
    ],
)

skill_md = SKILL / "SKILL.md"
if skill_md.is_file():
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        errors.append("SKILL.md: invalid YAML frontmatter")
    else:
        frontmatter = match.group(1)
        if not re.search(r"^name:\s+jianli\s*$", frontmatter, flags=re.M):
            errors.append("SKILL.md: name must be jianli")
        if not re.search(r"^description:\s*\S.+$", frontmatter, flags=re.M):
            errors.append("SKILL.md: description is missing")
    line_count = len(text.splitlines())
    if line_count > 500:
        errors.append(f"SKILL.md: {line_count} lines exceeds the 500-line budget")

openai_yaml = SKILL / "agents" / "openai.yaml"
if openai_yaml.is_file():
    metadata = openai_yaml.read_text(encoding="utf-8")
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

link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for markdown in REPO.rglob("*.md"):
    for target in link_pattern.findall(markdown.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_part = target.split("#", 1)[0]
        if path_part and not (markdown.parent / path_part).resolve().exists():
            errors.append(f"broken link: {markdown.relative_to(REPO)} -> {target}")

if errors:
    print("Jianli check failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

runtime_files = sum(1 for path in SKILL.rglob("*") if path.is_file())
print("Jianli check passed.")
print(f"Repository: {REPO}")
print(f"Runtime files: {runtime_files}")
print(f"SKILL.md lines: {len(skill_md.read_text(encoding='utf-8').splitlines())}")
