from classes.player import Player
from classes.ball import Ball
from classes.score import Score
import pygame

# Colores (Red, Green, Blue)
cWhite = (255, 255, 255)
cBlack = (0, 0, 0)

# Inicializar juego
pygame.init()
pygame.display.set_caption("PONG!")
iconImage = pygame.image.load("assets/icon.png")
pygame.display.set_icon(iconImage)

# Configurar ventana de juego
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Crear jugadores
players = [
    Player([50, 50], (pygame.K_w, pygame.K_s)),
    Player([718, 50])
]

# Crear puntaje para jugadores
score = Score(players)

# Crear pelota
ball = Ball()

# Sonido de puntaje
scoreSound = pygame.mixer.Sound("assets/score.wav")

# Juego
running = True
while running:
    # Renderizar fondo de pantalla
    screen.fill(cBlack)
    # Checar las acciones de los jugadores
    for event in pygame.event.get():
        # Checar si se cerró el juego
        if event.type == pygame.QUIT:
            running = False
        # Checar si se mueve algún jugador
        if event.type == pygame.KEYDOWN:
            # Emezar a mover pelota
            if event.key == pygame.K_SPACE:
                ball.run = True
            for player in players:
                if event.key == player.key_up:
                    player.move_up()
                if event.key == player.key_down:
                    player.move_down()
        # Checar si se detiene algún jugador
        if event.type == pygame.KEYUP:
            for player in players:
                if event.key in [player.key_up, player.key_down]:
                    player.stop()

    # Agregar puntos y crear nuevas pelota
    ballX = ball.position[0]
    newBall = False
    if ballX < -ball.width:
        newBall = True
        players[1].score += 1
    elif ballX > screenWidth:
        newBall = True
        players[0].score += 1
    if newBall:
        del ball
        ball = Ball()
        scoreSound.play()

    for player in players:
        ball.collision_check(player)
        player.update()
        player.render()
    ball.update()
    score.render()
    ball.render()
    pygame.display.update()
