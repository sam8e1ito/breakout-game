import random
from data import state
from .level1 import generateLevel1
from .level2 import generateLevel2

LEVELS = {
    1: generateLevel1,
    2: generateLevel2,
}

# space, , ball_radius, screen, box_size, box_color, padding, rows, top_offset, collision_types
def processLevel(action):
    delta = 1 if action == 'next' else -1
    target = state.currentLevel + delta

    if target not in LEVELS:
        return state.currentLevel

    state.board.reset()
    state.FAIL_ATTEMPTS = 3
    state.currentLevel = target
    return target
