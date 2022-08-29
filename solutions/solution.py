from abc import ABC
from typing import Dict, List

from entities.contributor import Contributor
from entities.project import Project


class Solution(ABC):
    def solve(self, contributors: List[Contributor], project: List[Project]) -> Dict[Contributor, List[Project]]:
        """Solves the given matching problem of contributors and projects to be done

        :param contributors: list of available contributors
        :param project: pool of possible projects
        :return: mapping from each contributor to the projects they will be working on
        """
        pass
