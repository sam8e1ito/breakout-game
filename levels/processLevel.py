import random
from data import state
from .level1 import generateLevel1
from .level2 import generateLevel2

LEVELS = {
    1: generateLevel1,
    2: generateLevel2,
}

def processLevel(action):
    delta = 1 if action == 'next' else -1
    target = state.currentLevel + delta

    if target not in LEVELS:
        return state.currentLevel

    state.board.reset()
    state.currentLevel = target
    return target
