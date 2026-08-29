import pygame
import sys
import button

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Kitchen Task")

original_image = pygame.image.load("kitchen.png").convert()
scaled_image = pygame.transform.scale(original_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

start_button = button.Button("Start Cooking!", 900, 600, 200, 60, (0, 150, 0), (0, 200, 0), (255, 255, 255))

running = True
while running:
    # Handle events (like clicking the 'X' to close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if start_button.is_clicked(event):
                print("Button Clicked! Start the game logic here.")

    screen.blit(scaled_image, (0, 0))
    start_button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
