from classes.scene import Scene
from classes.text import Text
import pygame


class Look(Scene):
    def __init__(self):
        font_title = pygame.font.Font("freesansbold.ttf", 54)
        c_white = (255, 255, 255)
        x, y = [50, 50]
        title = Text("Look for Pokémon", font_title, c_white, [x, y])
        super().__init__([title])
