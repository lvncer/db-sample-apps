import dataclasses


@dataclasses.dataclass
class User:
    id: int
    name: str
    birthday: str
    height: float
    target_weight: float
