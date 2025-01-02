import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Mario character properties
mario_width, mario_height = 70, 70
mario_x, mario_y = 100, HEIGHT - mario_height - 107
mario_speed = 5
jump_height = 15
is_jumping = False
velocity_y = 0

# Load Mario image
mario_image = pygame.image.load('mario_image.png')
mario_image = pygame.transform.scale(mario_image, (mario_width, mario_height))

# Load obstacle image
obstacle_image_path = 'cactus.jpeg'
obstacle_image = pygame.image.load(obstacle_image_path)
obstacle_image = pygame.transform.scale(obstacle_image, (60,60))

# Load background image
background_image_path = 'background2.gif'  # Replace with the actual path
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Gravity
gravity = 0.8

# Obstacle properties
obstacle_width, obstacle_height = 30, 115
obstacle_x = WIDTH
obstacle_y = HEIGHT - 50 - obstacle_height
obstacle_speed = 5

# Remove ground height, merge with background

def draw_mario(x, y):
    screen.blit(mario_image, (x, y))

def draw_obstacle(x, y):
    screen.blit(obstacle_image, (x, y))

def show_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, BLACK)
    restart_text = pygame.font.Font(None, 36).render("Press R to Restart", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))
    pygame.display.flip()

def reset_game():
    global mario_x, mario_y, is_jumping, velocity_y, obstacle_x
    mario_x = 100
    mario_y = HEIGHT - mario_height - 107
    is_jumping = False
    velocity_y = 0
    obstacle_x = WIDTH

def main():
    global mario_x, mario_y, is_jumping, velocity_y, obstacle_x

    running = True
    game_over = False

    while running:
        screen.blit(background_image, (0, 0))  # Draw the background image

        if game_over:
            show_game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    game_over = False
                    reset_game()
        else:
            draw_mario(mario_x, mario_y)
            draw_obstacle(obstacle_x, HEIGHT - 50 - obstacle_height)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Key controls
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                mario_x -= mario_speed
            if keys[pygame.K_RIGHT]:
                mario_x += mario_speed
            if keys[pygame.K_SPACE] and not is_jumping:
                is_jumping = True
                velocity_y = -jump_height

            # Apply gravity and jumping
            if is_jumping:
                mario_y += velocity_y
                velocity_y += gravity
                if mario_y >= HEIGHT - mario_height - 100:
                    mario_y = HEIGHT - mario_height - 107
                    is_jumping = False

            # Prevent Mario from going out of bounds
            mario_x = max(0, min(WIDTH - mario_width, mario_x))

            # Move obstacle
            obstacle_x -= obstacle_speed
            if obstacle_x < -obstacle_width:
                obstacle_x = WIDTH

            # Check collision
            if (mario_x < obstacle_x + obstacle_width and
                mario_x + mario_width > obstacle_x and
                mario_y < obstacle_y + obstacle_height and
                mario_y + mario_height > obstacle_y):
                game_over = True

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
