import pygame
import math
from shadow import new_img_gradient

pygame.init()

screen = pygame.display.set_mode((1540, 804))
pygame.display.set_caption("The Earth and the Moon")

earth_img = pygame.image.load('earth_picture.png')
earth_img_scaled = pygame.transform.scale(earth_img, (256, 256))

new_img_gradient(earth_img_scaled.get_size(), 'earth_shadow')
earth_shadow = pygame.image.load('earth_shadow.png')
earth_shadow_scaled = pygame.transform.scale(earth_shadow, earth_img_scaled.get_size())

moon_img = pygame.image.load('moon 2.png')
moon_img_scaled = pygame.transform.scale(moon_img, (64, 64))

new_img_gradient(moon_img_scaled.get_size(), 'moon_shadow')
moon_shadow = pygame.image.load('moon_shadow.png')
moon_shadow_scaled = pygame.transform.scale(moon_shadow, moon_img_scaled.get_size())

bg_img = pygame.image.load('starry sky 2.jpg')

pygame.display.set_icon(earth_img_scaled)


def display_bg():
    screen.blit(bg_img, (0, 0))

def earth(degrees):
    screen.blit(earth_img_scaled, (642, 274))
    rotation(earth_shadow_scaled, degrees, (642, 274))

def moon(degrees, shadow_degrees):
    apoapsis = 6
    periapsis = 1
    # moon_img_scaled = pygame.transform.scale(moon_img_scaled, )
    # moon_shadow_scaled = pygame.transform.scale(moon_shadow_scaled, )
    rotation(moon_img_scaled, shadow_degrees, earth_orbit(apoapsis, periapsis, degrees))
    rotation(moon_shadow_scaled, shadow_degrees, earth_orbit(apoapsis, periapsis, degrees))

def rotation(image, degrees, top_left):
    rotated_image = pygame.transform.rotate(image, degrees*(-50))
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    screen.blit(rotated_image, new_rect)

def earth_orbit(apoapsis, periapsis, degrees):
    earth_center_x = 770
    earth_center_y = 402

    orbit_coordinates = (apoapsis*to_degrees(math.cos(degrees)) + earth_center_x,
                         periapsis*to_degrees(math.sin(degrees)) + earth_center_y)
    return orbit_coordinates

def to_degrees(value):
    return value * 180 / math.pi


def find_center(image, top_left):
    new_rect = image.get_rect(center=image.get_rect(topleft=top_left).center)
    return new_rect


clock = pygame.time.Clock()
running = True
counter = 0
shadow_counter = 0
behind = False

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if counter > 6.3:
        counter = 0

    display_bg()

    if counter <= 3.15:
        earth(shadow_counter)
        moon(counter, shadow_counter)
    else:
        moon(counter, shadow_counter)
        earth(shadow_counter)

    counter += 0.005
    shadow_counter += 0.005
    pygame.display.update()
    clock.tick(144)

print('Simulation closed.')
