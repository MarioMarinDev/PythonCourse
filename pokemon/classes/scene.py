import pygame


class Scene():
    def __init__(self, objects):
        self.objects = objects
        self.screen = pygame.display.get_surface()

    def render_objects(self):
        for object in self.objects:
            object.render()
