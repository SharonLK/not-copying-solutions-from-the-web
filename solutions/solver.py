from abc import ABC
from typing import Dict, List

from entities.contributor import Contributor
from entities.project import Project


class Solver(ABC):
    def solve(self, contributors: List[Contributor], projects: List[Project]) \
            -> Dict[Contributor, List[Project]]:
        """Solves the given matching problem of contributors and projects to be done

        :param contributors: list of available contributors
        :param projects: pool of possible projects
        :return: mapping from each contributor to the projects they will be working on
        """
        pass
