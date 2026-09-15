from data import state
from features import asteroid_feature

def _remove_asteroid(space, key, asteroid_shape):
    if asteroid_shape.body in space.bodies:
        space.remove(asteroid_shape, asteroid_shape.body)

def paddle_hit_by_asteroid(arbiter, space, data):
    asteroid_shape = arbiter.shapes[0]
    space.add_post_step_callback(_remove_asteroid, asteroid_shape, asteroid_shape)
    asteroid_feature.damage_user()
    return False

def asteroid_missed(arbiter, space, data):
    asteroid_shape = arbiter.shapes[0]
    space.add_post_step_callback(_remove_asteroid, asteroid_shape, asteroid_shape)
    return False