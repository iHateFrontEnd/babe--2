import pygame
import sys

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

# Mario character properties
mario_width, mario_height = 50, 50
mario_x, mario_y = 100, HEIGHT - mario_height - 50
mario_speed = 5
jump_height = 15
is_jumping = False
velocity_y = 0

# Load Mario image
mario_image = pygame.image.load('/mnt/data/2d_only_body_mario_for_a_game.jpeg')
mario_image = pygame.transform.scale(mario_image, (mario_width, mario_height))

# Gravity
gravity = 0.8

# Ground properties
ground_height = 50

def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - ground_height, WIDTH, ground_height))

def draw_mario(x, y):
    screen.blit(mario_image, (x, y))

def main():
    global mario_x, mario_y, is_jumping, velocity_y

    running = True
    while running:
        screen.fill(BLUE)  # Clear the screen with a sky-blue background
        draw_ground()
        draw_mario(mario_x, mario_y)

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
            if mario_y >= HEIGHT - mario_height - ground_height:
                mario_y = HEIGHT - mario_height - ground_height
                is_jumping = False

        # Prevent Mario from going out of bounds
        mario_x = max(0, min(WIDTH - mario_width, mario_x))

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

