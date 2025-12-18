import dataclasses
import datetime


@dataclasses.dataclass
class TodoRecord:
    id: int
    user_id: int
    title: str
    deadline: datetime.date
    priority: int
