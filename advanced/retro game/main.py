import pygame
from PIL import Image, ImageDraw

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

studios_img = pygame.image.load('samsam studios.png')
title_img = pygame.image.load('TITLE.png')
title_screen_img = pygame.image.load('TITLE SCREEN.png')
highlight_start = pygame.image.load('highlight_start.png')
highlight_options = pygame.image.load('highlight_options.png')

pygame.display.set_caption('RETRO')
# pygame.display.set_icon(title_img)


def startup():  # 60 frames per second

    for frames in range(-225, 225, 2):  # 255 frames, 3.75 seconds

        img = Image.new(mode='RGBA',
                        size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                        color=(30, 30, 30, abs(frames)))
        img.save('fade.png')
        fade = pygame.image.load('fade.png')

        screen.blit(studios_img, (0, 0))
        screen.blit(fade, (0, 0))

        pygame.display.update()
        clock.tick(60)

def title_screen(selection):
    screen.blit(title_screen_img, (0, 0))
    screen.blit(title_img, (131, 100))
    if selection == 'start':
        screen.blit(highlight_start, (100, 276))
    if selection == 'options':
        screen.blit(highlight_options, (100, 400))


running = True
launching = True
in_title_screen = False
in_game = False
in_options = False

title_selection = 'start'
clock = pygame.time.Clock()
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if in_title_screen:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    title_selection = 'start'
                if event.key == pygame.K_DOWN:
                    title_selection = 'options'
                if event.key == pygame.K_SPACE:
                    if title_selection == 'start':
                        in_title_screen = False
                        in_game = True
                    if title_selection == 'options':
                        in_title_screen = False
                        in_options = True

    if in_title_screen:
        title_screen(title_selection)

    if in_game:
        pass

    if in_options:
        pass

    if launching:
        startup()
        launching = False
        in_title_screen = True

    pygame.display.update()
    clock.tick(60)
