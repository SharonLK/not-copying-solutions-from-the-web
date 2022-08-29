from dataclasses import dataclass
from typing import List

from entities.role import Role


@dataclass
class Project:
    duration: int
    score: int
    best_before: int
    required_roles: List[Role]
