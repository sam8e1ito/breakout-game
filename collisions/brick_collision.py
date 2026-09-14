import features
from data import state

def remove_brick(arbiter, space, data):
    brick_shape = arbiter.shapes[0]
    
    position = brick_shape.body.position
    is_secret = features.isSecretBrick(brick_shape)
    is_score = features.isScoreBrick(brick_shape)

    space.remove(brick_shape, brick_shape.body)

    if is_secret:
        features.spawn_powerup(space, position)

    if is_score:
        features.process_score()
    
    if brick_shape in state.brick_shapes:
        state.brick_shapes.remove(brick_shape)

    if len(state.brick_shapes) == 0 and not state.DID_USER_WIN:
        state.toggleWin()