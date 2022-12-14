from typing import Dict, List

from entities.contributor import Contributor
from entities.project import Project
from solutions.solver import Solver


class MockSolver(Solver):
    def solve(self, contributors: List[Contributor], projects: List[Project]) \
            -> Dict[Project, List[Contributor]]:
        return dict()
