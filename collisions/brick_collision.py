import features
from data import state

def remove_brick(arbiter, space, data):
    brick_shape = arbiter.shapes[0]
    space.remove(brick_shape, brick_shape.body)

    brick_signal = features.isSecretBrick(brick_shape)
    if brick_signal == True:
        features.spawn_powerup(space, brick_shape.body.position)
    
    if brick_shape in state.brick_shapes:
        state.brick_shapes.remove(brick_shape)
    if len(state.brick_shapes) == 0 and not state.DID_USER_WIN:
        state.toggleWin() # DID_USER_WIN = True
        print('win')
