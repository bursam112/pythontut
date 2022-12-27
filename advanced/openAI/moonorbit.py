import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600
window_size = (window_width, window_height)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Moon Orbit Simulation')

# Load the images for the earth and moon
earth_image = pygame.image.load('earth.png')
earth_image = pygame.transform.scale(earth_image, (370, 370))
moon_image = pygame.image.load('moon.png')
moon_image = pygame.transform.scale(moon_image, (100, 100))
# Set the initial position of the moon
moon_x = 300
moon_y = 300

# Set the radius of the orbit
orbit_radius = 200

# Set the initial angle of the moon
angle = 0

# Set the angular velocity of the moon (in radians per frame)
angular_velocity = 0.01

# Set the frame rate
frame_rate = 60

# Set the running flag
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Calculate the x and y position of the moon based on the angle
    moon_x = orbit_radius * math.cos(angle)
    moon_y = orbit_radius * math.sin(angle)

    # Draw the earth
    screen.blit(earth_image,
                (window_width / 2 - earth_image.get_width() / 2, window_height / 2 - earth_image.get_height() / 2))

    # Draw the moon
    screen.blit(moon_image,
                (window_width / 2 - moon_image.get_width() / 2 + moon_x,
                 window_height / 2 - moon_image.get_height() / 2 + moon_y))

    # Update the angle
    angle += angular_velocity

    # Update the display
    pygame.display.flip()

    # Delay to maintain the frame rate
    pygame.time.delay(1000 // frame_rate)

# Quit Pygame
pygame.quit()
