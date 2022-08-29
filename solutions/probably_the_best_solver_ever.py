from typing import Dict, List

import networkx as nx

from entities.contributor import Contributor
from entities.project import Project
from entities.solution import Solution
from solutions.solver import Solver


class ProbablyTheBestSolverEver(Solver):
    def _best_matching(self, project: Project, contributors: List[Contributor]) -> List[Contributor]:
        graph = nx.Graph()
        graph.add_nodes_from([c for c in contributors])
        graph.add_nodes_from([role for role in project.required_roles])

        for c in contributors:
            for role in project.required_roles:
                if c.get_skill_level(role.name) >= role.level:
                    graph.add_edge(c, role)

        edges = nx.matching.maximal_matching(graph)

        if not len(edges) == len(project.required_roles):
            return []

        contributors_by_order = []
        for role in project.required_roles:
            for edge in edges:
                if role == edge[1]:
                    contributors_by_order.append(edge[0])
                    break

        return contributors_by_order

    def solve(self, contributors: List[Contributor], projects: List[Project]) -> Dict[Project, List[Contributor]]:
        solution = Solution()

        print('Initializing available projects')
        available_projects = [p for p in projects]

        while True:
            changed = False

            for project in available_projects:
                available = solution.available_contributors_for_project(project, contributors)
                chosen = self._best_matching(project, available)

                if len(chosen) == len(project.required_roles):
                    print(f'Successfully found matching for project {project.name}')

                    solution.match_to_project(project, chosen)
                    changed = True
                    available_projects.remove(project)
                    break

            # chosen = random.choices(projects, weights=[1] * len(projects))

            if not changed:
                break

        print(f'Returning solution')
        return solution.get_mapping()
