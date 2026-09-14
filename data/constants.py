import uuid
from random_username.generate import generate_username
import pygame, pymunk
from dataclasses import dataclass

from data.powerup_types import PowerUpType


__all__ = ["user_empty_state"]

_username_list = generate_username(1)

user_empty_state = {
    "id": str(uuid.uuid4()),
    "username": _username_list[0],
    "score": 0
}

SCREEN = {
    "WIDTH": 940,
    "HEIGHT": 400,
    "COLOR": pygame.Color(33, 20, 43)
}

COLLISION_TYPES = {
    'ball': 1,
    'brick': 2,
    'bottom': 3,
    'paddle': 4,
    'wall': 5,
    'powerup': 6
}

PADDLE = {
    "COLLISION_TYPE": COLLISION_TYPES["paddle"],
    "CATEGORY": 0b000010,
    "COLOR": pygame.Color(242, 236, 206),
    "RADIUS": 8,
    "DEFAULT_ENDPOINTS": ((-50, 0), (50,0))
}

BRICK = {
    "WIDTH": 25,
    "HEIGHT": 20,
    "COLOR": pygame.Color(252, 3, 165),
    "CATEGORY": 0b000100,
    "COLLISION_TYPE": COLLISION_TYPES['brick']
}

WALL = {
    "RADIUS": 2,
    "CATEGORY": 0b001000,
    "COLLISION_TYPE": COLLISION_TYPES["wall"],
    "COLOR": pygame.Color('gray')
}

BOTTOM = {
    "RADIUS": 2,
    "CATEGORY": 0b010000,
    "COLLISION_TYPE": COLLISION_TYPES["bottom"],
    "COLOR": pygame.Color('red')
}

BALL = {
    "RADIUS": 12.5,
    "CATEGORY": 0b000001,
    "COLOR": pygame.Color(148, 252, 20),
    "COLLISION_TYPE": COLLISION_TYPES["ball"]
}

POWERUP = {
    "RADIUS": 12.5,
    "CATEGORY": 0b100000,
    "COLLISION_TYPE": COLLISION_TYPES["powerup"]
}

ALL_CATEGORY = pymunk.ShapeFilter.ALL_CATEGORIES()


@dataclass(frozen=True)
class PowerupConfig:
    color: pygame.Color
    duration_ms: int = 0
    endpoints: tuple | None = None
    radius_delta: int | None = None

POWERUP_CONFIGS = {
    PowerUpType.NEW_BALL: PowerupConfig(color=pygame.Color(3, 252, 248)),
    PowerUpType.BIG_BALL: PowerupConfig(color=pygame.Color(115, 252, 3), duration_ms=3000, radius_delta=5),
    PowerUpType.BIG_PADDLE: PowerupConfig(color=pygame.Color(252, 173, 3), duration_ms=3000, endpoints=((-100, 0), (100, 0))),
}

PADDING, TOP_OFFSET, ROWS = 5, 50, 6