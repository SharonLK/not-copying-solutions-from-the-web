from typing import Dict, List, Set, TextIO, Tuple

from entities.contributor import Contributor
from entities.project import Project
from entities.role import Role
from solutions.mock_solution import MockSolver


def parse(stream: TextIO) -> Tuple[List[Contributor], List[Project]]:
    contributors: List[Contributor] = []
    projects: List[Project] = []

    num_contributors, num_projects = (int(s) for s in stream.readline().split())

    print(num_contributors, num_projects)

    for _ in range(num_contributors):
        split = stream.readline().split()

        name = split[0]
        skills: Set[Role] = set()
        for __ in range(int(split[1])):
            skill_split = stream.readline().split()
            skills.add(Role(skill_split[0], int(skill_split[1])))

        contributors.append(Contributor(name, skills))

    for _ in range(num_projects):
        split = stream.readline().split()

        requirements: List[Role] = []
        for __ in range(int(split[4])):
            requirement_spit = stream.readline().split()
            requirements.append(Role(requirement_spit[0], int(requirement_spit[1])))

        projects.append(Project(name=split[0], duration=int(split[1]), score=int(split[2]),
                                best_before=int(split[3]), required_roles=requirements))

    return contributors, projects


def print_output(solution: Dict[Project, List[Contributor]], stream: TextIO) -> None:
    stream.write(f'{len(solution)}\n')

    for project, contributors in solution.items():
        stream.write(f'{project.name}\n')
        contributors_names = ' '.join([contributor.name for contributor in contributors])
        stream.write(f'{contributors_names}\n')


if __name__ == '__main__':
    with open('data_sets/a_an_example.in.txt', 'r') as f:
        contributors, projects = parse(f)

    solver = MockSolver()
    solution = solver.solve(contributors, projects)

    with open('solution.out.txt', 'w') as f:
        print_output(solution, f)
