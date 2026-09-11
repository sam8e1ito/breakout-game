import pymunk, random

from data import state, constants
from features import ball_feature

def space_has_shape(space, shape):
    return shape in space.shapes

class Board:
    count = None

    def __init__(self, space, paddle_body, screen, generate_level_fn, level_generators):
        self.space = space
        self.paddle_body = paddle_body
        self.ball_radius = constants.BALL['RADIUS']
        self.collision_types = constants.COLLISION_TYPES
        self.generate_level_fn = generate_level_fn
        self.screen = screen
        self.w, self.h = constants.BRICK['WIDTH'], constants.BRICK['HEIGHT']
        self.brick_color = constants.BRICK['COLOR']
        self.padding = constants.PADDING
        self.rows = constants.ROWS
        self.top_offset = constants.TOP_OFFSET
        self.level_generators = level_generators

    def clearBoard(self):
        for b in state.brick_shapes:
            if space_has_shape(self.space, b):
                self.space.remove(b, b.body)
        state.brick_shapes.clear()

        for s in list(self.space.shapes):
            if s.body.body_type == pymunk.Body.DYNAMIC and s.body not in [self.paddle_body]:
                self.space.remove(s.body, s)

    def _spawn_starting_ball(self):
        ball_feature.spawn_ball(
            self.space,
            self.paddle_body.position + (0, 40), 
            random.choice([(1, 10), (-1, 10)])
        )

    def _choose_secret_bricks(self):
        while Board.count > 0:
            for i in range(0, len(state.brick_shapes)):
                is_secret = Board.count > 0 and random.randint(0,2) == 1
                if is_secret == True:
                    state.brick_shapes[i].user_data = {'secret': True}
                    Board.count -= 1


    def _init_count(self):
        Board.count = int(len(state.brick_shapes) / 3)

    def start(self):
        if state.DID_USER_WIN:
            state.toggleWin()
        state.currentLevel = 1
        self.clearBoard()

        self._spawn_starting_ball()
        self.generate_level_fn(self.screen, self.space, state.brick_shapes)
        self._init_count()
        self._choose_secret_bricks()

    def reset(self):
        state.failAttempts = 3
        state.doesBallAlreadyExist = False

        if state.DID_USER_WIN:
            state.toggleWin()
        self.clearBoard()

        self._spawn_starting_ball()
        self.level_generators[state.currentLevel](self.screen, self.space, state.brick_shapes)
        self._init_count()
        self._choose_secret_bricks()