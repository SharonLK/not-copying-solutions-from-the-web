from dataclasses import dataclass
from typing import Dict


@dataclass
class Project:
    duration: int
    score: int
    best_before: int
    required_roles: Dict[str, int]
