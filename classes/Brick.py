import pymunk
from data import constants

class Brick:
    def __init__(self, space, brick_shapes, coords, color=None):
        self.w, self.h = constants.BRICK["WIDTH"], constants.BRICK["HEIGHT"]
        self.space = space
        self.collision_type = constants.BRICK['COLLISION_TYPE']
        self.x, self.y = coords
        
        self.color = color if color is not None else constants.BRICK['COLOR']

        self.brick_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.brick_body.position = self.x, self.y

        self.brick_shape = pymunk.Poly.create_box(self.brick_body, (self.w, self.h))
        self.brick_shape.elasticity = 1.0
        self.brick_shape.color = self.color
        self.brick_shape.group = 1
        self.brick_shape.collision_type = self.collision_type
        self.brick_shape.filter = pymunk.ShapeFilter(categories=constants.BRICK["CATEGORY"])

        self.brick_shape.secret = False
        self.brick_shape.score = False
        self.brick_shape.color = self.color

        space.add(self.brick_body, self.brick_shape)
        brick_shapes.append(self.brick_shape)