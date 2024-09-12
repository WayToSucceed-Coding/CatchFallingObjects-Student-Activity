import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player (basket) settings
basket_width = 50
basket_height = 10
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 30
basket_speed = 5

# Falling objects
falling_objects = {}#Correction 1
object_width, object_height = 20, 20
fall_speed = 3

# Game variables
score = 0
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Add new falling object randomly
    if random.randint(1, 30) == 1:
        falling_objects.Append([random.randint(0, WIDTH - object_width), 0])#Correction 3
        

    # Move falling objects
    for obj in falling_objects:
        obj[1] += fall_speed
        pygame.draw.rect(screen, RED, (obj[0], obj[1], object_width, object_height))

        # Check if object is caught by the basket
        if basket_y <= obj[1] + object_height <= basket_y + basket_height and \
           basket_x <= obj[0] <= basket_x + basket_width:
            falling_objects.remove(obj)
            score += 1

        # Remove objects that fall below the screen
        if obj[1] > HEIGHT:
            falling_objects.(obj)#correction 2

    # Draw the basket
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
