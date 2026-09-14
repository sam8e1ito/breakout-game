import pygame

BUTTON_DEFAULTS = {
    "SIZE": (260, 60),
    "COLOR": pygame.Color('gray'),
    "TEXT_COLOR": pygame.Color('black'),
    "BORDER_RADIUS": 14
}

class Button:
    def __init__(self, text, center_pos, color=BUTTON_DEFAULTS['COLOR'], size=BUTTON_DEFAULTS['SIZE']):
        self.text = text
        self.color = color
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        self.rect.center = center_pos

    def draw(self, surface, font):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=BUTTON_DEFAULTS['BORDER_RADIUS'])
        
        text_surf = font.render(self.text, True, BUTTON_DEFAULTS['TEXT_COLOR'])
        text_rect = text_surf.get_rect(center=self.rect.center)
        
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False