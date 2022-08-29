from dataclasses import dataclass


@dataclass
class Role:
    name: str
    level: int

    def __hash__(self) -> int:
        return hash(self.name) * 3 + hash(self.level) * 23
