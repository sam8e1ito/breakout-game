
import random, pygame

from data import state, constants
from features import spawn_ball
from classes.PowerUp import Powerup
from data.powerup_types import PowerUpType

def random_powerup():
    return random.choice(list(constants.POWERUP_CONFIGS))

def spawn_powerup(space, position):
    return Powerup(space, position, random_powerup())


def processPowerup(powerup_type: PowerUpType, space, arbiter):
    config = constants.POWERUP_CONFIGS[powerup_type]

    if powerup_type == PowerUpType.NEW_BALL:
        state.doesBallAlreadyExist = False
        spawn_ball(
            space,
            arbiter.shapes[1].body.position + (0, 40),
            random.choice([(1, 10), (-1, 10)]),
            True,
        )

    elif powerup_type == PowerUpType.BIG_PADDLE:
        paddle_shape = arbiter.shapes[1]
        paddle_shape.unsafe_set_endpoints(*config.endpoints)
        state.paddle_boost_end_time = pygame.time.get_ticks() + config.duration_ms

    elif powerup_type == PowerUpType.BIG_BALL:
        try:
            ball_shape = state.main_ball[0]
            if state.main_ball[2] is True:
                ball_shape.unsafe_set_radius(constants.BALL["RADIUS"] + config.radius_delta)
                state.ball_boost_end_time = pygame.time.get_ticks() + config.duration_ms
        except AttributeError:
            import traceback; traceback.print_exc()
            return
