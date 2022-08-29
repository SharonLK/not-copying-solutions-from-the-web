from dataclasses import dataclass
from typing import List

from entities.role import Role


@dataclass
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    required_roles: List[Role]

    def __hash__(self) -> int:
        return hash(self.name) * 3 + hash(self.duration) * 5 + hash(self.score) * 7 + \
               hash(self.best_before) * 23 + hash(tuple(self.required_roles))
