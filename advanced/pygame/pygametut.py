import pygame
import random

# Required, init == initialize
pygame.init()

# Screen Resolution and Creation
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("DVD Screen Saver Simulator")
blue_icon = pygame.image.load('DVD icon/DVD_logo_blue.png')
red_icon = pygame.image.load('DVD icon/DVD_logo_red.png')
green_icon = pygame.image.load('DVD icon/DVD_logo_green.png')
yellow_icon = pygame.image.load('DVD icon/DVD_logo_yellow.png')
purple_icon = pygame.image.load('DVD icon/DVD_logo_purple.png')

pygame.display.set_icon(blue_icon)

# Images (assign all images to a variable. if not, could cause complications)
you_win = pygame.image.load('you_win.png')
blue = pygame.image.load('DVD icon/DVD_logo_blue.png')
red = pygame.image.load('DVD icon/DVD_logo_red.png')
green = pygame.image.load('DVD icon/DVD_logo_green.png')
yellow = pygame.image.load('DVD icon/DVD_logo_yellow.png')
purple = pygame.image.load('DVD icon/DVD_logo_purple.png')

# Player
playerImg = pygame.image.load('DVD icon/DVD_logo_blue.png')  # 6x32 pixels

playerX = random.randrange(0, 600, 100)
playerY = random.randrange(0, 400, 100)


def player(x, y):
    screen.blit(playerImg, (x, y))


def dvd_switch_logo():
    value = random.randint(0, 3)
    this_list = [blue, red, green, yellow, purple]

    if playerImg == blue:
        this_list.pop(0)
    elif playerImg == red:
        this_list.pop(1)
    elif playerImg == green:
        this_list.pop(2)
    elif playerImg == yellow:
        this_list.pop(3)
    elif playerImg == purple:
        this_list.pop(4)

    return this_list[value]


def dvd_switch_icon():
    return playerImg


speedX = 1
speedY = 1
win = False

# Game Loop
running = True
clock = pygame.time.Clock()
while running:

    # R, G, B
    screen.fill((10, 10, 10))

    # DVD movement player
    if 0 <= playerX <= 672:
        playerX += speedX
    else:
        speedX = -speedX
        playerImg = dvd_switch_logo()
        pygame.display.set_icon(dvd_switch_icon())
        if playerX < 0:
            playerX = 0
        elif playerX > 672:
            playerX = 672

    if 0 <= playerY <= 536:
        playerY += speedY
    else:
        speedY = -speedY
        playerImg = dvd_switch_logo()
        pygame.display.set_icon(dvd_switch_icon())
        if playerY < 0:
            playerY = 0
        elif playerY > 536:
            playerY = 536

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if speedX < 0:
                    speedX -= 0.5
                elif speedX > 0:
                    speedX += 0.5
                if speedY > 0:
                    speedY += 0.5
                elif speedY < 0:
                    speedY -= 0.5
                if speedX == 0 and speedY == 0:
                    speedX = 0.5
                    speedY = 0.5
            if event.key == pygame.K_DOWN:
                if speedX < 0:
                    speedX += 0.5
                elif speedX > 0:
                    speedX -= 0.5
                if speedY > 0:
                    speedY -= 0.5
                elif speedY < 0:
                    speedY += 0.5

    player(playerX, playerY)

    if playerX == 0 and playerY == 0 or playerX == 0 and playerY == 536 or playerX == 672 and playerY == 0 or playerX == 672 and playerY == 536:
        win = True

    if win:
        screen.blit(you_win, (0, 0))

    # Screen Update
    pygame.display.update()
    # 144 fps
    clock.tick(144)

# UP_ARROW speed goes up, DOWN_ARROW speed goes down *check*
