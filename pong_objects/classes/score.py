import pygame


class Score:
    """
        Shows the score of current players in screen
    """
    def __init__(self, players):
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.players = players
        self.oPosition = [5, 5]
        self.position = self.oPosition
        self.screen = pygame.display.get_surface()

    def render(self):
        x, y = self.position
        for i, player in enumerate(self.players):
            render = self.font.render("P" + str(i+1) + ": " + str(player.score), True, (255, 255, 255))
            self.screen.blit(render, (x, y))
            width = render.get_rect().size[0]
            x += width + 50
