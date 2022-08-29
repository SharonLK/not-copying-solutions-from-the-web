from dataclasses import dataclass
from typing import Set, Dict

from entities.role import Role

from entities.project import Project


@dataclass
class Contributor:
    name: str
    skills: Dict[str, int]

    def get_skill_level(self, role_name: str) -> int:
        for skill, level in self.skills:
            if skill.role_name == role_name:
                return skill.level
        return 0

    def get_relative_skill_level(self, role) -> int:
        """
        returns how good a contributor in a given role compared to his other abilities
        Example: cont {CSS: 5, HTML: 7, C++: 9)
        cont.get_relative_skill_level(CSS) = 3
        cont.get_relative_skill_level(HTML) = 2
        cont.get_relative_skill_level(C++) = 1
        :param role: the role to test
        :return: position of his ability compared to his other abilities
        """
        sorted_skill_levels = list(sorted(self.skills.items(), key=lambda item: item[1]))
        relative_rank = 0
        for level in sorted_skill_levels:
            relative_rank += 1
            if level == self.get_skill_level(role):
                return relative_rank
        return relative_rank

    # returns -> potential skills to improve, value will be the next level
    def get_improvement_options_in(self, project: Project) -> Dict[str, int]:
        options = {}
        for role, required_skill_level in project.required_roles:
            if self.get_skill_level(role) == required_skill_level:
                options[role] = required_skill_level + 1
        return options

    def upgrade(self, role):
        self.skills[role.name] += 1
