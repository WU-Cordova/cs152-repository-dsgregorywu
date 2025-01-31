from dataclasses import dataclass
from character_type import CharacterType

@dataclass
class Character():
    name: str
    character_type: CharacterType
    health: int
    attack_power: int
    