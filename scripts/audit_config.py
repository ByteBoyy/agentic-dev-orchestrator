#!/usr/bin/env python3
"""Audit the repository's agent configuration without invoking a model."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_AGENTS = {
    "explorer",
    "architect",
    "backend-implementer",
    "frontend-implementer",
    "code-reviewer",
    "verifier",
}
REQUIRED_SKILLS = {"plan", "orchestrate", "review", "handoff", "ship"}
REQUIRED_PLAN_SECTIONS = {
    "Progress",
    "Surprises & Discoveries",
    "Decision Log",
    "Outcomes & Retrospective",
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"missing YAML frontmatter: {path.relative_to(ROOT)}")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def main() -> int:
    errors: list[str] = []

    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    if not claude.startswith("@AGENTS.md"):
        errors.append("CLAUDE.md must import @AGENTS.md first")

    agents: set[str] = set()
    for path in sorted((ROOT / ".claude/agents").glob("*.md")):
        try:
            data = frontmatter(path)
            if not data.get("name") or not data.get("description"):
                errors.append(f"agent missing name/description: {path.relative_to(ROOT)}")
            agents.add(data.get("name", ""))
        except ValueError as error:
            errors.append(str(error))

    skills: set[str] = set()
    for path in sorted((ROOT / ".claude/skills").glob("*/SKILL.md")):
        try:
            data = frontmatter(path)
            if not data.get("name") or not data.get("description"):
                errors.append(f"skill missing name/description: {path.relative_to(ROOT)}")
            skills.add(data.get("name", ""))
        except ValueError as error:
            errors.append(str(error))

    missing_agents = REQUIRED_AGENTS - agents
    missing_skills = REQUIRED_SKILLS - skills
    if missing_agents:
        errors.append(f"missing agents: {', '.join(sorted(missing_agents))}")
    if missing_skills:
        errors.append(f"missing skills: {', '.join(sorted(missing_skills))}")

    plan_text = (ROOT / "plans/0001-bootstrap-orchestrator.md").read_text(
        encoding="utf-8"
    )
    for section in REQUIRED_PLAN_SECTIONS:
        if f"## {section}" not in plan_text:
            errors.append(f"bootstrap plan missing section: {section}")

    forbidden = list(ROOT.glob(".claude/commands/*.md"))
    if forbidden:
        errors.append("legacy command files found; use project skills")

    if errors:
        print("configuration audit failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"configuration audit passed: {len(agents)} agents, {len(skills)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
