from dataclasses import dataclass
from typing import Set

from entities.role import Role


@dataclass
class Contributor:
    name: str
    skills: Set[Role]

    def get_skill_level(self, role_name: str) -> int:
        for skill in self.skills:
            if skill.name == role_name:
                return skill.level

        return 0
