import pygame
import random


def collision_check(obj1_x, obj1_y, obj1_img, obj2_x, obj2_y, obj2_img):
    obj1_size = obj1_img.get_rect().size
    obj2_size = obj2_img.get_rect().size
    obj1_rect = pygame.Rect(obj1_x, obj1_y, obj1_size[0], obj1_size[1])
    obj2_rect = pygame.Rect(obj2_x, obj2_y, obj2_size[0], obj2_size[1])
    return obj1_rect.colliderect(obj2_rect)


# Inicializar y configurar pygame
pygame.init()
pygame.display.set_caption("PONG!")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

# Crear ventana de juego
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Crear un jugador
playerImg = pygame.image.load("assets/player.png")
playerX = 32
playerY = 204
playerVspd = 0
playerSpd = 0.3
playerWidth, playerHeight = playerImg.get_rect().size
playerHit = False

# Crear pelota
ballImg = pygame.image.load("assets/ball.png")
ballX = 400
ballY = 300
ballSpd = 0.25
ballHspd = random.choice([ballSpd, -ballSpd])
ballVspd = random.choice([ballSpd, -ballSpd])
ballWidth, ballHeight = ballImg.get_rect().size

# Crear puntaje
score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)

# Crear fin de juego
end_text = "Fin del juego"
end_font = pygame.font.Font('freesansbold.ttf', 64)

# Lógica de juego
running = True
ended = False
while running:
    # Dibujar el fondo de pantalla
    screen.fill((0, 0, 0))
    # Checar los eventos del juego
    for event in pygame.event.get():
        # Terminar el ciclo de juego si se presiona "X"
        if event.type == pygame.QUIT:
            running = False
        # Checar si se presiona arriba o abajo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerVspd = -playerSpd
            if event.key == pygame.K_DOWN:
                playerVspd = playerSpd
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                playerVspd = 0

    # Agregar velocidad al jugador
    playerY += playerVspd

    # Solo mover jugador dentro de la ventana
    if playerY < 0:
        playerY = 0
    elif playerY + playerHeight > screenHeight:
        playerY = screenHeight - playerHeight

    # Agregar velocidad a la pelota
    ballX += ballHspd
    ballY += ballVspd

    # Cambiar la dirección de la pelota
    playerHit = collision_check(playerX, playerY, playerImg, ballX, ballY, ballImg) and not playerHit
    if ballY < 0 or ballY + ballHeight > screenHeight:
        ballVspd *= -1
        playerHit = False
    if playerHit or ballX + ballWidth > screenWidth:
        ballHspd *= -1

    # Agregar puntaje
    if playerHit:
        playerHit = True
        score += 1

    # Checar si se terminó el juego
    if ballX < 0:
        ended = True

    # Renderizar el jugador
    screen.blit(playerImg, (playerX, playerY))
    # Renderizar la pelota
    screen.blit(ballImg, (ballX, ballY))
    # Renderizar puntaje
    score_render = score_font.render("Puntaje: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (5, 5))
    # Renderizar fin de juego
    if ended:
        end_render = end_font.render(end_text, True, (255, 255, 255))
        screen.blit(end_render, (200, 270))
    # Actualizar pantalla
    pygame.display.update()
