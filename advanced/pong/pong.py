import pygame

# Required, init == initialize
pygame.init()

# Screen Resolution and Creation
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pong!")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)

# Player + Opponent
playerImg = pygame.image.load('pong_player.png')  # 6x32 pixels

playerX = 20  # distance from left side of screen
playerY = 270  # 600 / 2 = 300, 300 - 60/2 = 270
playerY_change = 0

opponentX = 774  # 800 - 20 - 6 = 774
opponentY = 270  # same as playerY
opponentY_change = 0

# Ball
ballImg = pygame.image.load('ball.png')

ballX = 395
ballX_change = 1.5
ballY = 301
ballY_change = 3

# Scoreboard
player_score_counter = 0
opponent_score_counter = 0

pygame.font.get_fonts()
score_font = pygame.font.Font(None, 100)


def player(x, y):
    screen.blit(playerImg, (x, y))


def opponent(x, y):
    screen.blit(playerImg, (x, y))


def ball(x, y):
    screen.blit(ballImg, (x, y))


def score():
    player_score = score_font.render(str(player_score_counter), False, (255, 255, 255))
    opponent_score = score_font.render(str(opponent_score_counter), False, (255, 255, 255))
    screen.blit(player_score, (150, 50))
    screen.blit(opponent_score, (600, 50))


# Game Loop
running = True
start = False
clock = pygame.time.Clock()

while running:

    # R, G, B
    screen.fill((0, 0, 0))
    for i in range(0, 600, 25):
        pygame.draw.line(screen, (255, 255, 255), (399, i), (399, i + 10), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                playerY_change = -3
            if event.key == pygame.K_s:
                playerY_change = 3

            if event.key == pygame.K_UP:
                opponentY_change = -3
            if event.key == pygame.K_DOWN:
                opponentY_change = 3

            if event.key == pygame.K_SPACE:
                start = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                opponentY_change = 0

    if playerY <= 0:
        playerY = 0
    elif playerY >= 540:
        playerY = 540

    if opponentY <= 0:
        opponentY = 0
    elif opponentY >= 540:
        opponentY = 540

    if ballY <= 0:
        ballY = 0
        ballY_change = -ballY_change
    elif ballY >= 590:
        ballY = 590
        ballY_change = -ballY_change

    # Paddle Collision
    if ballX == playerX + 6 and playerY - 5 <= ballY + 5 <= playerY + 65:
        ballX_change = -ballX_change

    if ballX + 10 == opponentX and opponentY - 5 <= ballY + 5 <= opponentY + 65:
        ballX_change = -ballX_change

    # Scoring
    if ballX < playerX - 30 or ballX > 800:
        start = False
        if ballX < playerX - 30:
            opponent_score_counter += 1
        elif ballX > 800:
            player_score_counter += 1
        ballX = 395
        ballY = 301

    playerY += playerY_change
    opponentY += opponentY_change

    if start:
        ballX -= ballX_change
        ballY += ballY_change

    ball(ballX, ballY)
    player(playerX, playerY)
    opponent(opponentX, opponentY)
    score()

    # Screen Update
    pygame.display.update()
    # 144 fps
    clock.tick(144)

pygame.quit()

# SCOREBOARD ✔
# REPLAY-ABILITY ✔
# INCONSISTENCIES IN BALL MOVEMENT
# MODES: TWO-PLAYER, PLAYER vs. AI, ENDLESS(pass to yourself + high score)
# SOUNDS
