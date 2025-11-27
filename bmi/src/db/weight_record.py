import dataclasses

@dataclasses.dataclass
class WeightRecord:
    id: int
    user_id: int
    record_date: str
    height: float
    weight: float
    target_weight: float
