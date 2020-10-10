from classes.scene import Scene
from classes.text import Text
from classes.button import Button
from classes.button_manager import ButtonManager
from game import colors
from game import fonts
import pygame


class Home(Scene):
    def __init__(self, controls):
        x, y = [50, 50]
        title = Text("Pokémon Game", fonts.title, colors.black, [x, y])
        y += title.height + 50
        search = Button("Look for Pokémon", fonts.normal, colors.black, [x, y], True,
                             action="scene_change", value="look")
        y += search.height + 5
        team = Button("My team", fonts.normal, colors.black, [x, y])
        y += team.height + 5
        exit = Button("Exit", fonts.normal, colors.black, [x, y], action="shutdown")
        buttons = [search, team, exit]
        button_manager = ButtonManager(buttons, controls)
        super().__init__([title, button_manager])
