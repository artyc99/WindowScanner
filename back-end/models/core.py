from dataclasses import dataclass

from . import ConfigI


@dataclass(frozen=True)
class Config(ConfigI):
    host: str
    port: int
