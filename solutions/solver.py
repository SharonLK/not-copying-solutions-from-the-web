from abc import ABC
from typing import Dict, List

from entities.contributor import Contributor
from entities.project import Project


class Solver(ABC):
    def solve(self, contributors: List[Contributor], projects: List[Project]) \
            -> Dict[Project, List[Contributor]]:
        """Solves the given matching problem of contributors and projects to be done

        Note the in the output, the order of contributors for each project defines the order of matching to the
        required roles. For example, in the list is
            [Contributor('Anna', {'C++': 1}), Contributor('Bob', {'Python': 3})]

        Then Anna is matched to the first role and Bob is matched to the second role.

        :param contributors: list of available contributors
        :param projects: pool of possible projects
        :return: mapping from each project to the contributors matched for each role
        """
        pass
