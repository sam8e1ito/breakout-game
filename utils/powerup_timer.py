from data import constants, state
import pygame


def update_powerup_timer():
    now = pygame.time.get_ticks()

    if state.paddle_boost_end_time is not None and now >= state.paddle_boost_end_time:
        state.paddle_shape.unsafe_set_endpoints(*constants.PADDLE["DEFAULT_ENDPOINTS"])
        state.space.reindex_shapes_for_body(state.paddle_shape.body)
        state.paddle_boost_end_time = None

    if state.ball_boost_end_time is not None and now >= state.ball_boost_end_time:
        ball_shape = state.main_ball[0]
        ball_shape.unsafe_set_radius(constants.BALL["RADIUS"])
        state.space.reindex_shapes_for_body(ball_shape.body)
        state.ball_boost_end_time = None
