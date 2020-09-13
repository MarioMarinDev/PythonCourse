import pygame
import random


# Checar si dos objectos colisionan
def collision_check(obj1_x, obj1_y, obj1_img, obj2_x, obj2_y, obj2_img):
    obj1_size = obj1_img.get_rect().size
    obj2_size = obj2_img.get_rect().size
    obj1_rect = pygame.Rect(obj1_x, obj1_y, obj1_size[0], obj1_size[1])
    obj2_rect = pygame.Rect(obj2_x, obj2_y, obj2_size[0], obj2_size[1])
    return obj1_rect.colliderect(obj2_rect)


# Inicializar
pygame.init()
pygame.display.set_caption("PONG!")
iconImg = pygame.image.load("assets/icon.png")
pygame.display.set_icon(iconImg)

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Colores (Red, Green, Blue)
cWhite = (255, 255, 255)
cBlack = (0, 0, 0)

# Crear jugador
playerImg = pygame.image.load("assets/player.png")
playerWidth, playerHeight = playerImg.get_rect().size
playerX = 50
playerY = (screenHeight / 2) - (playerHeight / 2)
playerSpd = 0.3
playerVspd = 0
playerJustHit = False

# Crear la pelota
ballImg = pygame.image.load("assets/ball.png")
oBallX = 384
oBallY = 284
ballX = oBallX
ballY = oBallY
ballSpd = 0.3
ballHspd = random.choice([ballSpd, -ballSpd])
ballVspd = random.choice([ballSpd, -ballSpd])
ballWidth, ballHeight = ballImg.get_rect().size

# Crear puntaje
score = 0
scoreFont = pygame.font.Font("freesansbold.ttf", 32)

# Crear fin de juego
ended = False
endText = "Game Over"
endFont = pygame.font.Font("freesansbold.ttf", 64)

# Crear sonido del golpe
hitSound = pygame.mixer.Sound("assets/hit.wav")

running = True
while running:
    # Dibujar el fondo de pantalla
    screen.fill(cBlack)
    # Checar los eventos del juego
    for event in pygame.event.get():
        # Si el jugador presionó "X"
        if event.type == pygame.QUIT:
            running = False
        # Si se presiona arriba o abajo o enter
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerVspd = -playerSpd
            if event.key == pygame.K_DOWN:
                playerVspd = playerSpd
            if event.key in [pygame.K_SPACE, pygame.K_RETURN] and ended:
                ended = False
                score = 0
                ballX = oBallX
                ballY = oBallY
                ballHspd = random.choice([ballSpd, -ballSpd])
                ballVspd = random.choice([ballSpd, -ballSpd])
        # Si se deja de presionar arriba o abajo
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                playerVspd = 0

    # Aplicar velocidad al jugador
    playerY += playerVspd

    # Aplicar velocidad a la pelota
    if not ended:
        ballX += ballHspd
        ballY += ballVspd

    # Limitar movimiento del jugador
    if playerY < 0:
        playerY = 0
    elif playerY > screenHeight - playerHeight:
        playerY = screenHeight - playerHeight

    # Rebotar la pelota
    hit = False
    if ballX + ballWidth > screenWidth:
        hit = True
        playerJustHit = False
        ballHspd *= -1
    if ballY < 0 or ballY + ballHeight > screenHeight:
        hit = True
        ballVspd *= -1
    if collision_check(playerX, playerY, playerImg, ballX, ballY, ballImg) and not playerJustHit:
        hit = True
        playerJustHit = True
        score += 1
        ballHspd *= -1

    # Reproducir sonido de golpe
    if hit:
        hitSound.play()

    # Checar si se acabó el juego
    if ballX + ballWidth < 0:
        ended = True

    # Renderizar jugador
    screen.blit(playerImg, (playerX, playerY))
    # Renderizar pelota
    screen.blit(ballImg, (ballX, ballY))
    # Renderizar el puntaje
    scoreRender = scoreFont.render("Score: " + str(score), True, cWhite)
    screen.blit(scoreRender, (5, 5))
    # Renderizar el fin de juego
    if ended:
        endRender = endFont.render(endText, True, cWhite)
        endWidth, endHeight = endRender.get_rect().size
        endX = (screenWidth / 2) - (endWidth / 2)
        endY = (screenHeight / 2) - (endHeight / 2)
        screen.blit(endRender, (endX, endY))
        restartRender = scoreFont.render("Press Enter to Restart", True, cWhite)
        restartWidth, restartHeight = restartRender.get_rect().size
        restartX = (screenWidth / 2) - (restartWidth / 2)
        restartY = endY + endHeight
        screen.blit(restartRender, (restartX, restartY))
    pygame.display.update()
