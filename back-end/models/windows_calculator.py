from dataclasses import dataclass
from typing import List

from models import Base


@dataclass
class Calculation(Base):
    rooms_per_level: List[int]
    level_count: int
    rooms_state: List[bool]
