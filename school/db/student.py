import dataclasses

@dataclasses.dataclass
class Student:
    id: int
    name: str
    birthday: str
    clazz: str
