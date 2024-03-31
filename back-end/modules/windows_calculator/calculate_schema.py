from dataclasses import dataclass
from typing import List

from models import Base


@dataclass
class GetRoomsNumbersReq(Base):
    rooms_per_level: List[int]
    level_count: int
    rooms_state: List[List[bool]]


@dataclass
class GetRoomsNumbersRes(Base):
    rooms: List[int]
    rooms_count: int
