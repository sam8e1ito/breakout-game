from data import constants
from features import asteroid_feature
import pymunk
from pymunk import Vec2d
import random

class Asteroid:
    def __init__(self, space):
        self.space = space

        self.w, self.h = constants.ASTEROID['SIZE']
        self.position = asteroid_feature.get_random_coords()
        self.collision_type = constants.ASTEROID['COLLISION_TYPE']
        self.color = random.choice(constants.ASTEROID['COLORS'])

        self.asteroid_body = pymunk.Body(1, pymunk.moment_for_box(1, (self.w, self.h)))
        self.asteroid_body.position = self.position

        self.random_velocity = random.randint(100, 401)
        self.asteroid_body.velocity = Vec2d(0,-self.random_velocity)

        self.asteroid_shape = pymunk.Poly.create_box(self.asteroid_body, (self.w, self.h))
        self.asteroid_shape.elasticity = 0.8
        self.asteroid_shape.color = self.color
        self.asteroid_shape.collision_type = self.collision_type
        self.asteroid_shape.filter = pymunk.ShapeFilter(
            categories=constants.ASTEROID['CATEGORY'],
            mask=constants.PADDLE['CATEGORY'] | constants.BOTTOM['CATEGORY']
        )

        self.asteroid_body._velocity_func = self.constant_velocity
        space.add(self.asteroid_body, self.asteroid_shape)

    def constant_velocity(self, body, gravity, damping, dt):
        pymunk.Body.update_velocity(body, gravity, damping, dt)
        if body.velocity.length > 0:
            body.velocity = body.velocity.normalized() * self.random_velocity
        else:
            body.velocity = Vec2d(0,-self.random_velocity)

def spawn_asteroid(space):
    print('spawned')
    return Asteroid(space)