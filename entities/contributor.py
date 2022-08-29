from dataclasses import dataclass
from typing import Dict


@dataclass
class Contributor:
    name: str
    skills: Dict[str, int]

    def get_skill_level(self, role: str) -> int:
        if role in self.skills:
            return self.skills[role]
        return 0
