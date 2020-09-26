from classes.scene import Scene
from classes.text import Text
import pygame


class Home(Scene):
    def __init__(self):
        self.fontTitle = pygame.font.Font("freesansbold.ttf", 54)
        self.fontNormal = pygame.font.Font("freesansbold.ttf", 32)
        self.cWhite = (255, 255, 255)
        x, y = [50, 50]
        self.title = Text("Pokémon Game", self.fontTitle, self.cWhite, [x, y])
        y += self.title.height + 50
        self.search = Text("Look for Pokémon", self.fontNormal, self.cWhite, [x, y])
        y += self.search.height + 5
        self.team = Text("My team", self.fontNormal, self.cWhite, [x, y])
        y += self.team.height + 5
        self.exit = Text("Exit", self.fontNormal, self.cWhite, [x, y])
        super().__init__([self.title, self.search, self.team, self.exit])
