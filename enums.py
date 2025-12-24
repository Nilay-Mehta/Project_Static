from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    INVENTORY = auto()
    GAME_OVER = auto()

class EntityType(Enum):
    PLAYER = auto()
    MUTANT = auto()
    RAIDER = auto()
    TRADER = auto()
    ITEM = auto()

class ItemType(Enum):
    WEAPON = auto()
    CONSUMABLE = auto()
    MATERIAL = auto()
    EQUIPMENT = auto()
    AMMO = auto()

class WeaponType(Enum):
    MELEE = auto()
    PISTOL = auto()
    RIFLE = auto()
    SHOTGUN = auto()

class HazardType(Enum):
    RADIATION = auto()
    TOXIC_GAS = auto()
    EXTREME_COLD = auto()
    SANDSTORM = auto()
