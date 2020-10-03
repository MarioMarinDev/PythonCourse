import pygame


class Scene():
    def __init__(self, objects):
        self.objects = objects
        self.screen = pygame.display.get_surface()
        self.action_data = None

    def render_objects(self):
        for object in self.objects:
            object.render()

    def control_objects(self):
        for object in self.objects:
            control_attr = getattr(object, "control", None)
            if callable(control_attr):
                data = control_attr()
                if type(data) == dict:
                    self.action_data = data
