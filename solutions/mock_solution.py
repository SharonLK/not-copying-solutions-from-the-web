from typing import Dict, List, Set

from entities.contributor import Contributor
from entities.project import Project
from solutions.solver import Solver


class MockSolver(Solver):
    def solve(self, contributors: List[Contributor], projects: List[Project]) \
            -> Dict[Project, List[Contributor]]:
        options = {}
        projects.sort(key=lambda x: x.get_relative_score())
        for p in projects:
            p.assign_contributors(contributors)
            options[p] = list(p.contributor_to_assigned_role.keys())
        return options
