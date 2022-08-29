from dataclasses import dataclass
from typing import Dict

from entities.contributor import Contributor


@dataclass
class Project:
    duration: int
    score: int
    best_before: int
    required_roles: Dict[str, int]

    def get_relative_score(self):
        return self.score / self.best_before
