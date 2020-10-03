from scenes.home import Home
from scenes.look import Look
from classes.input import Input
from classes.scene_manager import SceneManager
import pygame

pygame.init()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

input_control = Input()

scenes = {
    "home": Home(input_control),
    "look": Look()
}
scene_manager = SceneManager(scenes, "home")

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                input_control.move_down = True
            if event.key == pygame.K_UP:
                input_control.move_up = True
            if event.key == pygame.K_RIGHT:
                input_control.move_right = True
            if event.key == pygame.K_LEFT:
                input_control.move_left = True
            if event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                input_control.accept = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                input_control.move_down = False
            if event.key == pygame.K_UP:
                input_control.move_up = False
            if event.key == pygame.K_RIGHT:
                input_control.move_right = False
            if event.key == pygame.K_LEFT:
                input_control.move_left = False
            if event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                input_control.accept = False
    scene_manager.control()
    pygame.display.update()


