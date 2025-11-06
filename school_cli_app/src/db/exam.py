import dataclasses

@dataclasses.dataclass
class Exam:
    id: int
    subject: str
    score: int
