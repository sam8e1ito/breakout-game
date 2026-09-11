import pymunk
from pymunk import Vec2d

from data import state, constants

class Ball:
    def __init__(self, space, position, direction, autospawn):
        self.space = space
        self.position = position
        self.direction = direction
        self.radius = constants.BALL['RADIUS']
        self.collision_type = constants.BALL['COLLISION_TYPE']

        self.ball_body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, self.radius))
        self.ball_body.position = position

        self.ball_shape = pymunk.Circle(self.ball_body, self.radius)
        state.main_ball = self.ball_shape, self.ball_body, True
        self.ball_shape.color = constants.BALL['COLOR']
        self.ball_shape.elasticity = 1.0
        self.ball_shape.filter = pymunk.ShapeFilter(categories=constants.BALL['CATEGORY'])
        self.ball_shape.collision_type = self.collision_type
        self.ball_shape.autospawn = autospawn


        self.ball_body.apply_impulse_at_local_point(Vec2d(*self.direction))
        self.ball_body.velocity_func = self.constant_velocity

        space.add(self.ball_body, self.ball_shape)

    def constant_velocity(self, body, gravity, damping, dt):
        body.velocity = body.velocity.normalized() * 400