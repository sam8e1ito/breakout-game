from typing import TYPE_CHECKING, Union, Literal
from random_username.generate import generate_username

if TYPE_CHECKING:
    from classes import Board
    from classes import User
    
brick_shapes = []
brick_positions = []
currentLevel = 1
DID_USER_WIN = False
board: "Board | None" = None
space = None

def toggleWin():
    global DID_USER_WIN
    DID_USER_WIN = not DID_USER_WIN

FAIL_ATTEMPTS = 3
doesBallAlreadyExist = False

paddle_boost_end_time = None
paddle_shape = None

main_ball = None
ball_boost_end_time = None

user: "User | None" = None
currentScore = 0

type Screen = Union[
    Literal['menu'], 
    Literal['menu_start'], 
    Literal['menu_stats'], 
    Literal['menu_mechanics'], 
    Literal['game']
]
current_screen: Screen = 'menu'
running = True
