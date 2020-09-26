import pygame


class Text:
    def __init__(self, text, font, color, position):
        self.text = text
        self.font = font
        self.color = color
        self.position = position
        self.screen = pygame.display.get_surface()

    @property
    def text_render(self):
        return self.font.render(self.text, True, self.color)

    @property
    def rect(self):
        return self.text_render.get_rect()

    @property
    def width(self):
        return self.rect.size[0]

    @property
    def height(self):
        return self.rect.size[1]

    def render(self):
        self.screen.blit(self.text_render, self.position)
