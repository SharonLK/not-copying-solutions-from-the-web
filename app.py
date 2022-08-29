from typing import Dict, List, TextIO, Tuple

from entities.contributor import Contributor
from entities.project import Project


def parse(stream: TextIO) -> Tuple[List[Contributor], List[Project]]:
    contributors: List[Contributor] = []
    projects: List[Project] = []

    num_contributors, num_projects = (int(s) for s in stream.readline().split())

    print(num_contributors, num_projects)

    for _ in range(num_contributors):
        split = stream.readline().split()

        name = split[0]
        skills: Dict[str, int] = dict()
        for __ in range(int(split[1])):
            skill_split = stream.readline().split()

            skills[skill_split[0]] = int(skill_split[1])

        contributors.append(Contributor(name, skills))

    for _ in range(num_projects):
        split = stream.readline().split()

        requirements: Dict[str, int] = dict()
        for __ in range(int(split[4])):
            requirement_spit = stream.readline().split()
            requirements[requirement_spit[0]] = int(requirement_spit[1])

        projects.append(Project(duration=int(split[1]), score=int(split[2]),
                                best_before=int(split[3]), required_roles=requirements))

    return contributors, projects


if __name__ == '__main__':
    with open('data_sets/a_an_example.in.txt', 'r') as f:
        problem = parse(f)

        print(problem)
