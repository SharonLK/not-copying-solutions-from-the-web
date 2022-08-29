from dataclasses import dataclass
from typing import Set, Dict, List

from entities.contributor import Contributor


@dataclass
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    required_roles: Dict[str, int]
    contributors: Set[Contributor]
    contributor_to_assigned_role: Dict[Contributor, str]

    def get_relative_score(self):
        return self.score / self.duration

    def add_contributor(self, contributor: Contributor, role: str):
        self.contributors.add(contributor)
        self.contributor_to_assigned_role.contributor = role
        if self.required_roles[role] == contributor.get_skill_level(role):
            contributor.upgrade(role)

    def assign_contributors(self, contributors: List[Contributor]):
        for role, required_skill in self.required_roles:
            sorted_qualified_contributors = list(filter(lambda x: x.get_skill_level(role) >= required_skill,
                                                        sorted(contributors,
                                                               key=lambda x: x.get_skill_level(role))))
            min_level_contributors = list(filter(
                lambda x: x.get_skill_level(role) - required_skill == sorted_qualified_contributors[0].get_skill_level(
                    role), sorted_qualified_contributors))

            min_level_contributors.sort(key=lambda x: x.get_relative_skill_level(role))
            self.add_contributor(min_level_contributors[0], role)
            contributors.remove(min_level_contributors[0])
