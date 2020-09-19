import pygame
import random


class Ball:
    """
    Ball that bounce around
    """
    def __init__(self):
        self.image = pygame.image.load("assets/ball.png")
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.size
        self.screen = pygame.display.get_surface()
        self.position = [
            (self.screen.get_width() / 2) - (self.width / 2),
            (self.screen.get_height() / 2) - (self.height / 2)
        ]
        self.speed = 0.3
        self.vSpeed = random.choice([self.speed, -self.speed])
        self.hSpeed = random.choice([self.speed, -self.speed])
        self.lastHit = None
        self.run = False
        self.sound = pygame.mixer.Sound("assets/hit.wav")

    def update(self):
        if not self.run:
            return
        x, y = self.position
        x += self.hSpeed
        y += self.vSpeed
        # Collide with ceilings
        if y < 0 or y > self.screen.get_height() - self.height:
            self.vSpeed = -self.vSpeed
        self.position = [x, y]

    def render(self):
        self.screen.blit(self.image, self.position)

    def collision_check(self, player):
        x, y = self.position
        ball_rect = pygame.Rect(x, y, self.width, self.height)
        x, y = player.position
        player_rect = pygame.Rect(x, y, player.width, player.height)
        if ball_rect.colliderect(player_rect) and self.lastHit != player:
            self.lastHit = player
            self.hSpeed = -self.hSpeed
            self.sound.play()
