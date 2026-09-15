import pygame
from classes import Button
from data import constants

class MenuStats:
    def __init__(self, screen_size, users):
        self.screen_width, self.screen_height = screen_size
        self.buttons = {
            "back": Button("Back", (100, 50), size=(100, 40)),
        }
        self.users = users or []
        
        self.scroll_y = 0
        self.scroll_speed = 25
        self.header_height = 80
        self.content_height = max(100, len(self.users) * 40 + 40)
        self.max_scroll = max(0, self.content_height - (self.screen_height - 100))
        
        self.content_surface = pygame.Surface((self.screen_width, self.content_height))


        self.refresh_users(users or [])

    def refresh_users(self, users):
        self.users = users or []
        self.content_height = max(100, len(self.users) * 40 + 40)
        self.max_scroll = max(0, self.content_height - (self.screen_height - 100))
        self.scroll_y = max(0, min(self.scroll_y, self.max_scroll))
        self.content_surface = pygame.Surface((self.screen_width, self.content_height))

    def handle_event(self, event, state):
        if self.buttons["back"].is_clicked(event):
            state.current_screen = 'menu'
            return
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y -= event.y * self.scroll_speed
            self.scroll_y = max(0, min(self.scroll_y, self.max_scroll))

    def draw(self, surface, font):
        self._render_content(font)
        surface.blit(self.content_surface, (0, self.header_height - self.scroll_y))

        header_rect = pygame.Rect(0, 0, self.screen_width, self.header_height)
        pygame.draw.rect(surface, pygame.Color(constants.SCREEN['COLOR']), header_rect)

        title_surf = font.render("Users Leaderboard", True, pygame.Color('white'))
        title_rect = title_surf.get_rect(center=(self.screen_width / 2, 50))
        surface.blit(title_surf, title_rect)

        for btn in self.buttons.values():
            btn.draw(surface, font)

    def _render_content(self, font):
        self.content_surface.fill(pygame.Color(constants.SCREEN['COLOR']))
        
        if not self.users:
            no_data = font.render("No scores available", True, pygame.Color('gray'))
            self.content_surface.blit(no_data, no_data.get_rect(center=(self.screen_width / 2, 40)))
            return

        y_offset = 20
        for i, user in enumerate(self.users, 1):
            user_surf = font.render(f"{i}. {user['username']}", True, pygame.Color('white'))
            score_surf = font.render(str(user['score']), True, pygame.Color('white'))
            
            score_rect = score_surf.get_rect(topright=(self.screen_width - 200, y_offset))
            
            self.content_surface.blit(user_surf, (200, y_offset))
            self.content_surface.blit(score_surf, score_rect)
            
            y_offset += 40