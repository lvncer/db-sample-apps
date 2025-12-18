import dataclasses


@dataclasses.dataclass
class User:
    id: int
    name: str
    birthday: str
    experience: int
    progress: int
