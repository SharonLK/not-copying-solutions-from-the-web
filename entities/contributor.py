from dataclasses import dataclass
from typing import Set

from entities.role import Role

from entities.project import Project


@dataclass
class Contributor:
    name: str
    skills: Set[Role]

    def get_skill_level(self, role_name: str) -> int:
        for skill in self.skills:
            if skill.name == role_name:
                return skill.level

        return 0

    # returns -> potential skills to improve, value will be the next level
    def get_improvement_options_in(self, project: Project) -> Dict[str, int]:
        options = {}
        for role, required_skill_level in project.required_roles:
            if self.get_skill_level(role) == required_skill_level:
                options[role] = required_skill_level + 1
        return options
