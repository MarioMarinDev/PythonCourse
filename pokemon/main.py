from scenes.home import Home
import pygame

pygame.init()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

scenes = {
    "home": Home()
}
scene_running = "home"

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scenes[scene_running].render_objects()
    pygame.display.update()


