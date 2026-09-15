from data import constants, state
import random
import pygame

def get_random_coords():
    start,end = 40,600
    random_coords = (random.randrange(start + 20, end - 20), constants.SCREEN['HEIGHT'] - 20)
    return random_coords

def damage_user():
    state.DAMAGE_TAKEN += 1

def should_spawn():
    random_num = random.randint(0,2)
    if random_num == 1:
        return True
    return False

def track_asteroid():
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 5000)