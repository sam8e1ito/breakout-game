import features
from data import state
from store import db_utils

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
        scoreRow = db_utils.execute_read(
            """
            SELECT * FROM score WHERE id = ?
            """,
            (state.user['id'],)
        )

        highestScore = int(scoreRow[0]["score"])

        state.currentScore = state.currentScore + 1
        if int(state.currentScore) > int(highestScore):
            db_utils.log_highscore({**state.user, 'score': state.currentScore})
            state.user['score'] = state.currentScore
            print("db: ",db_utils.execute_read('SELECT * FROM score WHERE id = ?', (state.user['id'],)))
