import pygame
import sys
from enum import Enum, auto

# 1. Define your states using auto()
class GameState(Enum):
    START = auto()
    KITCHEN = auto()
    MALL = auto()

# 2. Main Game Class
class Game:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 900
        self.FPS = 60
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("The Perfect Day")
        self.clock = pygame.time.Clock()
        self.running = True

        original_kitchen_image = pygame.image.load("kitchen.png").convert()
        self.scaled_kitchen_image = pygame.transform.scale(original_kitchen_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        # Start the game on the Menu screen
        self.current_state = GameState.KITCHEN

    def run(self):
        while self.running:
            # Route processing based on the current Enum state
            if self.current_state == GameState.START:
                self.handle_start()
            elif self.current_state == GameState.KITCHEN:
                self.handle_kitchen()
            elif self.current_state == GameState.MALL:
                self.handle_mall()
                
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()

    # --- STATE HANDLERS ---

    def handle_start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Switch state instantly
                    self.current_state = GameState.KITCHEN 
        self.screen.fill((0, 0, 40)) 

    def handle_kitchen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Die or fail game
                    self.current_state = GameState.MALL 

        self.screen.blit(self.scaled_kitchen_image, (0, 0))
        #self.screen.fill((40, 80, 40)) # Green background for playing
        # (Update game objects and draw them here)

    def handle_mall(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Die or fail game
                        self.current_state = GameState.START 
    
            self.screen.fill((40, 80, 40)) # Green background for playing
            # (Update game objects and draw them here)

    def handle_game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart the game
                    self.current_state = GameState.START
                elif event.key == pygame.K_m:
                    # Return to main menu
                    self.current_state = GameState.START

        self.screen.fill((80, 30, 30)) # Red background for game over
        # (Draw "Game Over - Press R to Restart" text here)

if __name__ == "__main__":
    game = Game()
    game.run()
