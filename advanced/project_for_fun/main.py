import pygame
import math

# Required, init == initialize
pygame.init()

# Screen Resolution and Creation
screen = pygame.display.set_mode((1540, 804))
pygame.display.set_caption("Graphing Calculator")
graph = pygame.image.load('graph.png')

points = []
lines = []  # This was so clever


def display_equation(x_forward, x_backward, y_forward, y_backward, last_position_forward, last_position_backwards):
    if x <= 770:
        points.append((screen, (255, 0, 0), (x_forward, y_forward), 3))
        points.append((screen, (255, 0, 0), (x_backward, y_backward), 3))
        # surface, color, center, radius

        lines.append(last_position_forward)
        lines.append(last_position_backwards)
        # surface, color, start_pos, end_pos, width

    for circles in range(0, len(points)):
        pygame.draw.circle(surface=points[circles][0],
                           color=points[circles][1],
                           center=points[circles][2],
                           radius=points[circles][3])

        pygame.draw.line(surface=points[circles][0],
                         color=points[circles][1],
                         start_pos=lines[circles],
                         end_pos=points[circles][2],
                         width=points[circles][3])


# Game Loop
running = True
x = 0
clock = pygame.time.Clock()
temp_coordinate_f = (770, 402)
temp_coordinate_b = (770, 402)
# Zoom (%)
zoom_X = 100
zoom_Y = 100

while running:

    # R, G, B
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                zoom_Y += 10
            if event.key == pygame.K_DOWN:
                if zoom_Y > 10:
                    zoom_Y -= 10
            if event.key == pygame.K_RIGHT:
                zoom_X += 10
            if event.key == pygame.K_LEFT:
                if zoom_X > 10:
                    zoom_X -= 10

    # To draw lines between
    if x > 0:
        temp_coordinate_f = (x1+770, -y1+402)
        temp_coordinate_b = (x2+770, -y2+402)

    # X values
    x1 = x * zoom_X
    x2 = -x * zoom_X
    # Y values (equation)
    y1 = math.sin(x1) * zoom_Y
    y2 = math.sin(x2) * zoom_Y

    # Screen Update
    screen.blit(graph, (0, 0))
    display_equation(x1+770, x2+770, -y1+402, -y2+402, temp_coordinate_f, temp_coordinate_b)
    x += 1
    pygame.display.update()
    # 144 fps
    clock.tick(60)

# ZOOM FEATURE THAT CHANGES WHOLE GRAPH
