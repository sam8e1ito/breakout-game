import pygame, sys, uuid
from data import constants, state
from store import db_utils
from screens import (
    MenuScreen, 
    MenuStart, 
    MenuStats, 
    MenuMechanics,
    Game
)
from classes import User
from utils import generate_guest

pygame.init()
db_utils.init_db()

screen = pygame.display.set_mode((constants.SCREEN["WIDTH"], constants.SCREEN["HEIGHT"]))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)
smallFont = pygame.font.SysFont(None, 16)

all_users = db_utils.get_users()

def ensure_user():
    global all_users
    if len(all_users) == 0:
        generate_guest()
        all_users.append(state.user)
        
ensure_user()

menu_screen = MenuScreen(screen.get_width())
menu_start = MenuStart((screen.get_width(), screen.get_height()), all_users)
menu_stats = MenuStats((screen.get_width(), screen.get_height()), all_users)
menu_mechanics = MenuMechanics((screen.get_width(), screen.get_height()))

game = Game(screen, state.user)
SPAWN_ASTEROID_EVENT = pygame.USEREVENT + 1

previous_screen = state.current_screen

while state.running:
    if state.current_screen != previous_screen:
        fresh_users = db_utils.get_users()

        if state.current_screen == 'menu_start':
            menu_start.refresh_users(fresh_users)
        elif state.current_screen == 'menu_stats':
            menu_stats.refresh_users(fresh_users)

        previous_screen = state.current_screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            db_utils.close_db()
            pygame.quit()
            sys.exit()

        # event handler
        if state.current_screen == 'menu':
            menu_screen.handle_event(event, state)

        elif state.current_screen == 'menu_start':
            menu_start.handle_event(event, state)

        elif state.current_screen == 'menu_stats':
            menu_stats.handle_event(event, state)

        elif state.current_screen == 'menu_mechanics':
            menu_mechanics.handle_event(event, state)

        elif state.current_screen == 'game':
            game.handle_event(event, state, SPAWN_ASTEROID_EVENT)

            

    screen.fill(constants.SCREEN['COLOR'])

    if state.current_screen == 'menu':
        menu_screen.draw(screen, font)
    elif state.current_screen == 'menu_start':
        menu_start.draw(screen, font)
    elif state.current_screen == 'menu_stats':
        menu_stats.draw(screen, font)
    elif state.current_screen == 'menu_mechanics':
        menu_mechanics.draw(screen, font)
    elif state.current_screen == 'game':
        game.draw(screen, font)
    
    screen.blit(smallFont.render("fps: " + str(int(clock.get_fps())), 1, pygame.Color("white")), (10, screen.get_height() - 20))

    pygame.display.flip()
    clock.tick(60)