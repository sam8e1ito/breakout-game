import pymunk, random

from data import state, constants
from features import ball_feature, brick_feature

def space_has_shape(space, shape):
    return shape in space.shapes

GOLD = (255, 215, 0, 255)

class Board:
    secretCount = None
    scoreCount = 0

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
        while Board.secretCount > 0:
            for brick in state.brick_shapes:
                if Board.secretCount <= 0:
                    break

                if not getattr(brick, 'secret', False) and random.randint(0, 2) == 1:
                    brick.secret = True
                    Board.secretCount -= 1
    
    def _choose_score_bricks(self):
        while Board.scoreCount > 0:
            for brick in state.brick_shapes:
                if Board.scoreCount <= 0:
                    brick.color = constants.BRICK['COLOR']
                    break

                if not getattr(brick, 'score', False) and random.randint(0, 2) == 1:
                    brick.score = True
                    brick.color = GOLD
                    Board.scoreCount -= 1

    def _init_counts(self):
        Board.secretCount = int(len(state.brick_shapes) / 3)
        Board.scoreCount = int(len(state.brick_shapes) / 2)

    def start(self):
        if state.DID_USER_WIN:
            state.toggleWin()
        state.currentLevel = 1
        self.clearBoard()

        self._spawn_starting_ball()
        self.generate_level_fn(self.screen, self.space, state.brick_shapes)
        self._init_counts()
        self._choose_secret_bricks()
        self._choose_score_bricks()

    def reset(self):
        state.failAttempts = 3
        state.doesBallAlreadyExist = False

        if state.DID_USER_WIN:
            state.toggleWin()
        self.clearBoard()

        self._spawn_starting_ball()
        self.level_generators[state.currentLevel](self.screen, self.space, state.brick_shapes)
        self._init_counts()
        self._choose_secret_bricks()
        self._choose_score_bricks()