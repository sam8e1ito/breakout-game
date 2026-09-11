from data import state

def remove_ball(arbiter, space, data):
    ball_shape = arbiter.shapes[0]
    space.remove(ball_shape, ball_shape.body)
    try:
        if ball_shape.autospawn == False:
            state.doesBallAlreadyExist = False
            state.FAIL_ATTEMPTS -= 1
    except AttributeError:
        return
    