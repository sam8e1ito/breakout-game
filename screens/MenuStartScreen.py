import pygame
from classes import Button
from utils import generate_guest
from data import constants
from store import db_utils

class MenuStart:
    def __init__(self, screen_size, users):
        self.screen_width, self.screen_height = screen_size
        self.users = users
        
        self.static_buttons = {
            "back": Button("Back", (100, 50), size=(100, 50)),
            "newUser": Button('New User', (self.screen_width - 170, 50), color=pygame.Color(127, 235, 113), size=(170, 50))
        }
        
        self.choose_buttons = []
        self.delete_buttons = []
        
        self.scroll_y = 0
        self.scroll_speed = 25
        self.header_height = 80
        self.row_height = 50
        
        self._update_scroll_bounds()
        self._init_user_buttons()

    def refresh_users(self, users):
        self.users = users
        self._update_scroll_bounds()
        self._init_user_buttons()

    def _update_scroll_bounds(self):
        self.content_height = max(1, len(self.users) * self.row_height + 40)
        self.max_scroll = max(0, self.content_height - (self.screen_height - self.header_height))
        self.content_surface = pygame.Surface((self.screen_width, self.content_height))
        self.scroll_y = max(0, min(self.scroll_y, self.max_scroll))

    def _init_user_buttons(self):
        self.choose_buttons.clear()
        self.delete_buttons.clear()

        y_offset = 20
        for user in self.users:
            btn_x = self.screen_width - 280
            btn_y = y_offset + 15
            
            choose_btn = Button('Choose', (btn_x, btn_y), size=(120, 30))
            choose_btn.user = user

            delete_btn = Button('Delete', (btn_x + 135, btn_y), size=(120, 30), color=pygame.Color(237, 97, 78))
            delete_btn.user = user

            self.choose_buttons.append(choose_btn)
            self.delete_buttons.append(delete_btn)
            
            y_offset += self.row_height

    def handle_event(self, event, state):
        if self.static_buttons["back"].is_clicked(event):
            state.current_screen = 'menu'
            return
            
        if self.static_buttons['newUser'].is_clicked(event):
            generate_guest()
            state.currentScore = 0
            state.current_screen = 'game'
            return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[1] < self.header_height:
                return

            adjusted_pos = (event.pos[0], event.pos[1] - self.header_height + self.scroll_y)
            
            scrolled_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {
                'pos': adjusted_pos,
                'button': 1
            })
            
            for btn in self.choose_buttons:
                if btn.is_clicked(scrolled_event):
                    chosen_user = btn.user
                    state.user = chosen_user
                    state.currentScore = 0
                    state.current_screen = 'game'
                    return

            for btn in self.delete_buttons:
                if btn.is_clicked(scrolled_event):
                    chosen_user = btn.user
                    db_utils.delete_user(chosen_user)
                    
                    self.users.remove(chosen_user)

                    self._update_scroll_bounds()
                    self._init_user_buttons()
                    return

        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y -= event.y * self.scroll_speed
            self.scroll_y = max(0, min(self.scroll_y, self.max_scroll))

    def _render_content(self, font):
        self.content_surface.fill(pygame.Color(constants.SCREEN['COLOR']))
        
        y_offset = 20
        for i, user in enumerate(self.users):
            user_text = f"{i + 1}. {user['username']}"
            user_surf = font.render(user_text, True, pygame.Color('white'))
            self.content_surface.blit(user_surf, (200, y_offset))
            
            self.choose_buttons[i].draw(self.content_surface, font)
            self.delete_buttons[i].draw(self.content_surface, font)
            
            y_offset += self.row_height

    def draw(self, surface, font):
        self._render_content(font)
        
        surface.blit(self.content_surface, (0, self.header_height - self.scroll_y))

        header_rect = pygame.Rect(0, 0, self.screen_width, self.header_height)
        pygame.draw.rect(surface, pygame.Color(constants.SCREEN['COLOR']), header_rect)

        title_surf = font.render("Users", True, pygame.Color('white'))
        title_rect = title_surf.get_rect(center=(self.screen_width / 2, 50))
        surface.blit(title_surf, title_rect)

        for btn in self.static_buttons.values():
            btn.draw(surface, font)