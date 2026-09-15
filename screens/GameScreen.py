import random
import sys
import pygame
import pymunk
import pymunk.pygame_util

from data import state, constants
from store import db_utils
import levels
import features
import classes
from collisions import *
import utils


class Game:
    def __init__(self, surface, username):
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 16)
        self.user = db_utils.get_user_db(username)
        state.user = self.user

        self.space = pymunk.Space()
        pymunk.pygame_util.positive_y_is_up = True
        self.draw_options = pymunk.pygame_util.DrawOptions(self.surface)

        self._setup_physics_world()
        self._setup_paddle()

        self.space.on_collision(constants.BALL["COLLISION_TYPE"], constants.BOTTOM['COLLISION_TYPE'], begin=ball_collision.remove_ball)
        self.space.on_collision(constants.PADDLE['COLLISION_TYPE'], constants.BALL["COLLISION_TYPE"], pre_solve=pre_solve.pre_solve)
        self.space.on_collision(constants.BRICK["COLLISION_TYPE"], constants.BALL['COLLISION_TYPE'], begin=brick_collision.remove_brick)
        self.space.on_collision(constants.POWERUP["COLLISION_TYPE"], constants.BOTTOM['COLLISION_TYPE'], begin=powerup_collision.on_powerup_missed)
        self.space.on_collision(constants.POWERUP["COLLISION_TYPE"], constants.PADDLE['COLLISION_TYPE'], begin=powerup_collision.on_powerup_collected)

        self.board = classes.Board(
            self.space, 
            self.paddle_body, 
            self.surface, 
            levels.generateLevel1, 
            levels.LEVELS
        )
        self.board.start()

        state.board = self.board
        state.space = self.space

    def _setup_physics_world(self):
        screen_h = self.surface.get_height()
        
        # Walls
        lwall = pymunk.Segment(self.space.static_body, (40, 40), (40, screen_h - 20), constants.WALL["RADIUS"])
        lwall.filter = pymunk.ShapeFilter(categories=constants.WALL["CATEGORY"])
        lwall.collision_type = constants.WALL["COLLISION_TYPE"]
        lwall.elasticity = 1.0
        lwall.color = constants.WALL["COLOR"]

        rwall = pymunk.Segment(self.space.static_body, (600, 40), (600, screen_h - 20), constants.WALL["RADIUS"])
        rwall.filter = pymunk.ShapeFilter(categories=constants.WALL["CATEGORY"])
        rwall.collision_type = constants.WALL["COLLISION_TYPE"]
        rwall.elasticity = 1.0
        rwall.color = constants.WALL['COLOR']

        twall = pymunk.Segment(self.space.static_body, (40, screen_h - 20), (600, screen_h - 20), constants.WALL['RADIUS'])
        twall.filter = pymunk.ShapeFilter(categories=constants.WALL["CATEGORY"])
        twall.collision_type = constants.WALL['COLLISION_TYPE']
        twall.elasticity = 1.0
        twall.color = constants.WALL["COLOR"]

        bottom = pymunk.Segment(self.space.static_body, (40, 40), (600, 40), constants.BOTTOM["RADIUS"])
        bottom.sensor = True
        bottom.collision_type = constants.BOTTOM['COLLISION_TYPE']
        bottom.color = constants.BOTTOM["COLOR"]
        bottom.filter = pymunk.ShapeFilter(categories=constants.BOTTOM["CATEGORY"])

        self.space.add(rwall, lwall, twall, bottom)

    def _setup_paddle(self):
        self.paddle_body = pymunk.Body(500, float('inf'))
        self.paddle_body.position = 300, 100

        self.paddle_shape = pymunk.Segment(
            self.paddle_body, 
            (-50, 0), (50, 0), 
            constants.PADDLE['RADIUS']
        )
        state.paddle_shape = self.paddle_shape

        self.paddle_shape.color = constants.PADDLE["COLOR"]
        self.paddle_shape.elasticity = 1.0
        self.paddle_shape.collision_type = constants.PADDLE["COLLISION_TYPE"]
        self.paddle_shape.filter = pymunk.ShapeFilter(categories=constants.PADDLE['CATEGORY'])

        move_joint = pymunk.GrooveJoint(self.space.static_body, self.paddle_body, (100, 100), (540, 100), (0, 0))
        self.space.add(self.paddle_body, self.paddle_shape, move_joint)

    def handle_event(self, event, state_obj):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.paddle_body.velocity = (-600, 0)
            elif event.key == pygame.K_d:
                self.paddle_body.velocity = (600, 0)
            elif event.key == pygame.K_UP:
                levels.processLevel('next')
            elif event.key == pygame.K_DOWN:
                levels.processLevel('back')
            elif event.key == pygame.K_SPACE:
                features.spawn_ball(
                    self.space, 
                    self.paddle_body.position + (0, 40), 
                    random.choice([(1, 10), (-1, 10)]),
                )
            elif event.key == pygame.K_ESCAPE:
                state_obj.current_screen = 'menu'

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                self.paddle_body.velocity = (0, 0)

    def draw(self, surface, font=None):
        screen_h = surface.get_height()
        ui_font = font if font else self.font

        self.space.debug_draw(self.draw_options)
        self.space.step(1.0 / 60)
        utils.update_powerup_timer()

        surface.blit(ui_font.render(f"{state.user['username']}", 1, pygame.Color('white')), (640, 20))
        surface.blit(ui_font.render(f"Your highest score: {state.user['score']}", 1, pygame.Color('white')), (640, 80))
        surface.blit(ui_font.render(f"Your current score: {state.currentScore}", 1, pygame.Color('white')), (640, 120))
        surface.blit(ui_font.render(f"Balls left: {state.FAIL_ATTEMPTS}", 1, pygame.Color('white')), (640, screen_h - 60))

        if getattr(state, 'DID_USER_WIN', False):
            surface.blit(
                ui_font.render("You won!", 1, pygame.Color("green")), 
                (280, screen_h / 2 - 10)
            )
        
        self.clock.tick(60)