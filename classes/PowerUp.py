import pymunk
from pymunk import Vec2d
import random

from data import constants
from data.powerup_types import PowerUpType

class Powerup:
    def __init__(self, space, position, powerup_type: PowerUpType):
        config = constants.POWERUP_CONFIGS[powerup_type]

        self.space = space
        self.position = position
        self.radius = constants.POWERUP['RADIUS']
        self.collision_type = constants.POWERUP['COLLISION_TYPE']

        self.ball_body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, self.radius))
        self.ball_body.position = position

        self.ball_shape = pymunk.Circle(self.ball_body, self.radius)
        self.ball_shape.color = config.color
        self.ball_shape.elasticity = 0.8
        self.ball_shape.collision_type = self.collision_type
        self.ball_shape.powerup_type = powerup_type
        self.ball_shape.filter = pymunk.ShapeFilter(
            categories=constants.POWERUP["CATEGORY"],
            mask=constants.PADDLE["CATEGORY"] | constants.BOTTOM["CATEGORY"],
        )
        self.ball_body.apply_impulse_at_local_point(Vec2d(0, -10))
        self.ball_body.velocity_func = self.constant_velocity
        space.add(self.ball_body, self.ball_shape)

    def constant_velocity(self, body, gravity, damping, dt):
        body.velocity = body.velocity.normalized() * 200


def random_powerup():
    return random.choice(list(PowerUpType))


def spawn_powerup(space, position, ball_radius, collision_types):
    return Powerup(space, position, ball_radius, collision_types, random_powerup())
