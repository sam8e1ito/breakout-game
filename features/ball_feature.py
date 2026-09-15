import classes
from data import state, constants

def spawn_ball(space, position, direction, autospawn=False):
    if state.FAIL_ATTEMPTS != 0 and state.DAMAGE_TAKEN != 5:
        if state.doesBallAlreadyExist == False:
            if autospawn != True:
                state.doesBallAlreadyExist = True
            ball = classes.Ball(
                space, 
                position, 
                direction,
                autospawn
            )
