import pygame
import sys
from classes import Button

class MenuScreen:
    def __init__(self, screen_width):
        center_x = screen_width / 2
        self.buttons = {
            "start": Button("Start", (center_x, 130), pygame.Color(245, 176, 130)),
            "stats": Button("Stats", (center_x, 200), pygame.Color(219, 203, 191)),
            "mechanics": Button("Game Mechanics", (center_x, 270), pygame.Color(81, 207, 104)),
            "quit": Button("Quit", (center_x, 340), pygame.Color(237, 97, 78)),
        }

    def handle_event(self, event, state):
        if self.buttons["start"].is_clicked(event):
            state.current_screen = 'menu_start'
        elif self.buttons['stats'].is_clicked(event):
            state.current_screen = 'menu_stats'
        elif self.buttons['mechanics'].is_clicked(event):
            state.current_screen = 'menu_mechanics'
        elif self.buttons["quit"].is_clicked(event):
            pygame.quit()
            sys.exit()

    def draw(self, surface, font):
        pygame.display.set_caption('Breakout Game - Menu')
        title_surf = font.render("Breakout Game", True, pygame.Color('white'))
        title_rect = title_surf.get_rect(center=(surface.get_width() / 2, 50))
        surface.blit(title_surf, title_rect)

        for btn in self.buttons.values():
            btn.draw(surface, font)