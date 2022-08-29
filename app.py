from typing import List, Tuple

from entities.contributor import Contributor
from entities.project import Project


def parse(lines: List[str]) -> Tuple[List[Contributor], List[Project]]:
    contributors: List[Contributor] = []
    projects: List[Project] = []

    num_contributors, num_projects = (int(s) for s in lines[0].split())

    print(num_contributors, num_projects)

    return contributors, projects


if __name__ == '__main__':
    with open('data_sets/a_an_example.in.txt', 'r') as f:
        parse(f.readlines())
