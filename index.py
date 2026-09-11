import random
import pygame
import pymunk
import pymunk.pygame_util
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import state, constants
from store import db_utils
import levels
import features
import classes
from collisions import *
import utils

screen = pygame.display.set_mode((constants.SCREEN["WIDTH"], constants.SCREEN["HEIGHT"]))

def main():
    global board, paddle_body, paddle_shape
    db_utils.init_db()

    user = classes.User.init_user()
    print(user)

    pygame.init()
    pygame.display.set_caption('Breakout Game')

    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont("Arial", 16)

    space = pymunk.Space()
    pymunk.pygame_util.positive_y_is_up = True
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    lwall = pymunk.Segment(
        space.static_body, (40, 40),
        (40, screen.get_height() - 20), 
        constants.WALL["RADIUS"]
    )
    lwall.filter = pymunk.ShapeFilter(categories=constants.WALL["CATEGORY"])
    lwall.collision_type = constants.WALL["COLLISION_TYPE"]
    lwall.elasticity = 1.0
    lwall.color = constants.WALL["COLOR"]

    rwall = pymunk.Segment(
        space.static_body, 
        (screen.get_width() - 40, 40), 
        (screen.get_width() - 40, screen.get_height() - 20), 
        constants.WALL["RADIUS"]
    )
    rwall.filter = pymunk.ShapeFilter(categories=constants.WALL["CATEGORY"])
    rwall.collision_type = constants.WALL["COLLISION_TYPE"]
    rwall.elasticity = 1.0
    rwall.color = constants.WALL['COLOR']

    twall = pymunk.Segment(
        space.static_body, 
        (40, screen.get_height() - 20), 
        (screen.get_width() - 40, screen.get_height() - 20), 
        constants.WALL['RADIUS']
    )
    twall.filter = pymunk.ShapeFilter(categories=constants.WALL["CATEGORY"])
    twall.collision_type = constants.WALL['COLLISION_TYPE']
    twall.elasticity = 1.0
    twall.color = constants.WALL["COLOR"]


    bottom = pymunk.Segment(
        space.static_body, 
        (40, 40), 
        (screen.get_width() - 40, 40), 
        constants.BOTTOM["RADIUS"]
    )
    bottom.sensor = True
    bottom.collision_type = constants.BOTTOM['COLLISION_TYPE']
    bottom.color = constants.BOTTOM["COLOR"]
    bottom.filter = pymunk.ShapeFilter(categories=constants.BOTTOM["CATEGORY"])

    space.add(rwall, lwall, twall, bottom)

    space.on_collision(constants.BALL["COLLISION_TYPE"], constants.BOTTOM['COLLISION_TYPE'], begin=ball_collision.remove_ball)

    paddle_body = pymunk.Body(500, float('inf'))
    paddle_body.position = 300, 100

    paddle_shape = pymunk.Segment(
        paddle_body, 
        (-50, 0), (50,0), 
        constants.PADDLE['RADIUS'])
    state.paddle_shape = paddle_shape

    paddle_shape.color = constants.PADDLE["COLOR"]
    paddle_shape.elasticity = 1.0
    paddle_shape.collision_type = constants.PADDLE["COLLISION_TYPE"]
    paddle_shape.filter = pymunk.ShapeFilter(categories=constants.PADDLE['CATEGORY'])

    space.on_collision(constants.PADDLE['COLLISION_TYPE'], constants.BALL["COLLISION_TYPE"], pre_solve=pre_solve.pre_solve)
    space.on_collision(constants.BRICK["COLLISION_TYPE"], constants.BALL['COLLISION_TYPE'], begin=brick_collision.remove_brick)

    space.on_collision(constants.POWERUP["COLLISION_TYPE"], constants.BOTTOM['COLLISION_TYPE'], begin=powerup_collision.on_powerup_missed)
    space.on_collision(constants.POWERUP["COLLISION_TYPE"], constants.PADDLE['COLLISION_TYPE'], begin=powerup_collision.on_powerup_collected)

    move_joint = pymunk.GrooveJoint(space.static_body, paddle_body, (100, 100), (screen.get_width() - 100, 100), (0, 0))
    space.add(paddle_body, paddle_shape, move_joint)

    board = classes.Board(
        space, 
        paddle_body, 
        screen, 
        levels.generateLevel1, 
        levels.LEVELS
    )
    board.start()

    state.board = board
    state.space = space

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                paddle_body.velocity = (-600, 0)
            elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                paddle_body.velocity = (0, 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                paddle_body.velocity = (600, 0)
            elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                paddle_body.velocity = (0, 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                levels.processLevel('next')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                levels.processLevel('back')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                features.spawn_ball(
                    space, 
                    paddle_body.position + (0, 40), 
                    random.choice([(1, 10), (-1, 10)]),
                )

        screen.fill(constants.SCREEN["COLOR"])
        space.debug_draw(draw_options)
        space.step(1.0 / 60)
        utils.update_powerup_timer()

        screen.blit(font.render("fps: " + str(clock.get_fps()), 1, pygame.Color("white")), (0, 0))
        if state.DID_USER_WIN:
            screen.blit(
                font.render(
                    "You won!",
                    1, 
                    pygame.Color("green")
                ), 
                (screen.get_width() / 2 - 40, screen.get_height() / 2 -10)
            )


        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()
    db_utils.close_db()
