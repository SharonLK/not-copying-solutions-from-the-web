from typing import Dict, List

from entities.contributor import Contributor
from entities.project import Project
from solutions.solver import Solver


class MockSolver(Solver):
    def solve(self, contributors: List[Contributor], projects: List[Project]) \
            -> Dict[Contributor, List[Project]]:
        res = {}
        projects.sort(key=lambda x: x.get_relative_score(), reverse=True)
        for contributor in contributors:

        return dict()
