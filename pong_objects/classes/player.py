import pygame


class Player:
    """
    Pong main player class
    """
    def __init__(self, position, move_controls=(pygame.K_UP, pygame.K_DOWN)):
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.size
        self.position = position
        self.speed = 0.3
        self.vSpeed = 0
        self.key_up, self.key_down = move_controls
        self.screen = pygame.display.get_surface()
        self.score = 0

    def move_up(self):
        self.vSpeed = -self.speed

    def move_down(self):
        self.vSpeed = self.speed

    def stop(self):
        self.vSpeed = 0

    def update(self):
        y = self.position[1]
        y_max = self.screen.get_height() - self.height
        y += self.vSpeed
        if y < 0:
            y = 0
        elif y > y_max:
            y = y_max
        self.position[1] = y

    def render(self):
        self.screen.blit(self.image, self.position)
