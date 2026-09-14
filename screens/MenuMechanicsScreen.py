import pygame
from classes import Button
from data import constants

class MenuMechanics:
    def __init__(self, screen_size):
        self.screen_width, self.screen_height = screen_size
        
        self.buttons = {
            "back": Button("Back", (100, 50), size=(100, 40), color=pygame.Color(219, 203, 191)),
        }

        self.scroll_y = 0
        self.scroll_speed = 25
        self.content_height = 700
        self.max_scroll = max(0, self.content_height - (self.screen_height - 100))
        
        self.content_surface = pygame.Surface((self.screen_width, self.content_height))

    def handle_event(self, event, state):
        if self.buttons["back"].is_clicked(event):
            state.current_screen = 'menu'
            
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y -= event.y * self.scroll_speed
            self.scroll_y = max(0, min(self.scroll_y, self.max_scroll))

    def _render_content(self, font):
        self.content_surface.fill(pygame.Color(constants.SCREEN['COLOR']))

        lines = [
            "1. Controls:",
            "   - Move Paddle: Left / Right Arrow keys or Mouse",
            "",
            "2. Scoring & Rules:",
            "   - Destroy golden bricks to earn points.",
            "   - Don't let the ball fall past your paddle!",
            "",
            "3. Power-ups:",
            "   - Multi-ball: Spawns extra active balls.",
            "   - Paddle Extend: Temporarily increases paddle width.",
            "   - Big-ball: Temporarily increases ball radius."
        ]

        y_offset = 20
        for line in lines:
            text_surf = font.render(line, True, pygame.Color('white'))
            self.content_surface.blit(text_surf, (100, y_offset))
            y_offset += 40

    def draw(self, surface, font):
        self._render_content(font)
        pygame.display.set_caption('Breakout Game - Game Mechanics Menu')

        header_height = 80
        surface.blit(self.content_surface, (0, header_height - self.scroll_y))

        header_rect = pygame.Rect(0, 0, self.screen_width, header_height)
        pygame.draw.rect(surface, pygame.Color(constants.SCREEN['COLOR']), header_rect)

        title_surf = font.render("Game Mechanics", True, pygame.Color('yellow'))
        title_rect = title_surf.get_rect(center=(self.screen_width / 2, 50))
        surface.blit(title_surf, title_rect)

        for btn in self.buttons.values():
            btn.draw(surface, font)