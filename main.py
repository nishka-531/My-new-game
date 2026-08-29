import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Game Constants & Setup
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
FPS = 60

# Colors (RGB)
BG_COLOR = (150, 234, 255)      # light blue
PLAYER_COLOR = (255, 255, 255) # Mint white

# Create the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Masterpiece")

# Game Clock to control frame rate
clock = pygame.time.Clock()

# Example state variables
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_speed = 5

# 3. Main Game Loop
running = True
while running:
    # --- EVENT HANDLING (Inputs) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- GAME LOGIC (Updates) ---
    # Handle continuous keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos[1] += player_speed

    # --- DRAWING / RENDERING ---
    # Wipe the screen clean from the last frame
    screen.fill(BG_COLOR)

    # Draw the player (a simple circle)
    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, 20)

    # Flip the display buffer to show changes on screen
    pygame.display.flip()

    # --- FRAME RATE CONTROL ---
    clock.tick(FPS)

# 4. Clean Shutdown
pygame.quit()
sys.exit()
