import pygame


class Object:

    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.screen = pygame.display.get_surface()

    @property
    def rect(self):
        return self.image.get_rect()

    @property
    def width(self):
        return self.rect.size[0]

    @property
    def height(self):
        return self.rect.size[1]

    def render(self):
        self.screen.blit(self.image, self.position)
