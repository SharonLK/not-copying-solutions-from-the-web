from typing import Dict, List

from entities.contributor import Contributor
from entities.project import Project


class Solution:
    def __init__(self, mapping: Dict[Project, List[Contributor]] = None):
        self._mapping = mapping
        if self._mapping is None:
            self._mapping = dict()

    def get_mapping(self) -> Dict[Project, List[Contributor]]:
        return self._mapping

    def _allowed_matching(self, contributor: Contributor, potential_project: Project) -> bool:
        for project, contributors in self._mapping.items():
            if contributor.name in [c.name for c in contributors]:
                if potential_project.best_before >= project.best_before - project.duration and \
                        project.best_before >= potential_project.best_before - potential_project.duration:
                    return False

        return True

    def available_contributors_for_project(self, project: Project, contributors: List[Contributor]) \
            -> List[Contributor]:
        available_contributors: List[Contributor] = []
        for contributor in contributors:
            if self._allowed_matching(contributor, project):
                available_contributors.append(contributor)

        return available_contributors

    def match_to_project(self, project: Project, contributors: List[Contributor]) -> None:
        self._mapping[project] = contributors
