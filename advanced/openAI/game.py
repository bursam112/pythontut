import pygame
import random

# Set up the pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load the player and coin images
player_image = pygame.image.load("earth.png")
player_image = pygame.transform.scale(player_image, (100, 100))
coin_image = pygame.image.load("moon.png")
coin_image = pygame.transform.scale(coin_image, (100, 100))

# Set up the player and coin sprites
player = pygame.sprite.Sprite()
player.image = player_image
player.rect = player.image.get_rect()
player.rect.center = (400, 300)

coins = pygame.sprite.Group()
players = pygame.sprite.Group()
players.add(player)

# Set up the obstacles
obstacles = [
    pygame.Rect(200, 100, 50, 50),
    pygame.Rect(600, 400, 50, 50),
    pygame.Rect(100, 500, 50, 50),
]

# Set up the game variables
score = 0
game_over = False

# Set up the game loop
clock = pygame.time.Clock()
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 5
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 5
            elif event.key == pygame.K_UP:
                player.rect.y -= 5
            elif event.key == pygame.K_DOWN:
                player.rect.y += 5

    # Update the game state
    if random.random() < 0.1:
        coin = pygame.sprite.Sprite()
        coin.image = coin_image
        coin.rect = coin.image.get_rect()
        coin.rect.center = (random.randint(0, 800), random.randint(0, 600))
        coins.add(coin)
    coins.update()

    # Check for collisions
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle):
            game_over = True
    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    score += len(collected_coins)

    # Draw the game state
    screen.fill((0, 0, 0))
    players.draw(screen)
    coins.draw(screen)
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Display the game over screen
font = pygame.font.Font(None, 36)
text = font.render("Game Over! Score: {}".format(score), True, (255, 255, 255))
text_rect = text.get_rect()
