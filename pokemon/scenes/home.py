from classes.scene import Scene
from classes.text import Text
from classes.button import Button
from classes.button_manager import ButtonManager
import pygame


class Home(Scene):
    def __init__(self, controls):
        self.fontTitle = pygame.font.Font("freesansbold.ttf", 54)
        self.fontNormal = pygame.font.Font("freesansbold.ttf", 32)
        self.cWhite = (255, 255, 255)
        x, y = [50, 50]
        self.title = Text("Pokémon Game", self.fontTitle, self.cWhite, [x, y])
        y += self.title.height + 50
        self.search = Button("Look for Pokémon", self.fontNormal, self.cWhite, [x, y], True,
                             action="scene_change", value="look")
        y += self.search.height + 5
        self.team = Button("My team", self.fontNormal, self.cWhite, [x, y])
        y += self.team.height + 5
        self.exit = Button("Exit", self.fontNormal, self.cWhite, [x, y])
        buttons = [self.search, self.team, self.exit]
        self.button_manager = ButtonManager(buttons, controls)
        super().__init__([self.title, self.button_manager])
