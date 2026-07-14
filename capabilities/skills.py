from pathlib import Path
from typing import Any

import frontmatter
from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.toolsets import FunctionToolset


def load_skill(skill_name: str) -> str:
    """
    Load a skill from the skills directory.
    """

    path = Path("skills") / f"{skill_name}.md"

    if not path.exists():
        return f"Skill '{skill_name}' not found."

    skill = frontmatter.load(path)

    return f"""
# {skill.metadata.get('name', skill_name)}

Description:
{skill.metadata.get('description', '')}

{skill.content}
"""


class Skills(AbstractCapability[Any]):
    """Provides dynamic skill loading."""

    def get_instructions(self) -> str:

        skills_dir = Path("skills")

        if not skills_dir.exists():
            return ""

        lines = [
            "Available skills (load them when relevant):",
            ""
        ]

        for filename in sorted(skills_dir.glob("*.md")):

            skill = frontmatter.load(filename)

            name = skill.metadata.get("name", filename.stem)
            description = skill.metadata.get(
                "description",
                "No description."
            )

            lines.append(f"- {name}: {description}")

        return "\n".join(lines)

    def get_toolset(self) -> FunctionToolset:

        toolset = FunctionToolset()
        toolset.add_function(load_skill)

        return toolset