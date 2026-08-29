import pygame
import sys
import button
from enum import Enum, auto

class GameState(Enum):
    START = auto()
    KITCHEN = auto()
    COOKING = auto()
    MALL = auto()
    DOG = auto()
    END = auto()

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

        #original_start_image = pygame.image.load("start.png").convert()
        #self.scaled_start_image = pygame.transform.scale(original_start_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_kitchen_image = pygame.image.load("kitchen.png").convert()
        self.scaled_kitchen_image = pygame.transform.scale(original_kitchen_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_cooking_image = pygame.image.load("cooking.png").convert()
        self.scaled_cooking_image = pygame.transform.scale(original_cooking_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_mall_image = pygame.image.load("mall.png").convert()
        self.scaled_mall_image = pygame.transform.scale(original_mall_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        #original_dog_image = pygame.image.load("dog.png").convert()
        #self.scaled_dog_image = pygame.transform.scale(original_dog_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.next_button = button.Button("Next Module", 900, 600, 200, 60, (0, 150, 0), (0, 200, 0), (255, 255, 255))

        # Start the game on the Menu screen
        self.current_state = GameState.START

    def run(self):
        while self.running:
            # Route processing based on the current Enum state
            if self.current_state == GameState.START:
                self.handle_start()
            elif self.current_state == GameState.KITCHEN:
                self.handle_kitchen()
            elif self.current_state == GameState.COOKING:
                self.handle_cooking()
            elif self.current_state == GameState.MALL:
                self.handle_mall()
            elif self.current_state == GameState.DOG:
                self.handle_dog()
                
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()

    # --- STATE HANDLER METHODS---

    def handle_start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.KITCHEN
        self.screen.fill((0, 0, 40)) 
        self.next_button.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

        self.BUTTON_SIZE = 100

        x_pos = (self.SCREEN_WIDTH // 2) - (self.BUTTON_SIZE // 2)
        y_pos = (self.SCREEN_HEIGHT // 2) - (self.BUTTON_SIZE // 2)

        self.next_button = button.Button("START GAME", x_pos, y_pos, 200, 60, (0, 150, 0), (0, 200, 0), (255, 255, 255))


    def handle_kitchen(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.COOKING 
        self.screen.blit(self.scaled_kitchen_image, (0, 0))
        self.next_button.draw(self.screen)

    def handle_cooking(self):
        flourButton = button.ImageButton(200, 200, 200, 200, "flour.png")
        sugarButton = button.ImageButton(200, 200, 200, 200, "sugar.png")
        vanillaButton = button.ImageButton(200, 200, 200, 200, "vanilla.png")
        bakingPowderButton = button.ImageButton(200, 200, 200, 200, "bakingPowder.png")
        butterButton = button.ImageButton(800, 200, 200, 200, "butter.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.MALL

            if butterButton.is_clicked(event):
                print("butterButton button Clicked")
                butterButton.toggleClicked()
            elif flourButton.is_clicked(event):
                print("flour button clicked")
                flourButton.toggleClicked()
            elif sugarButton.is_clicked(event):
                print("sugar button clicked")
                sugarButton.toggleClicked()
            elif vanillaButton.is_clicked(event):
                print("vanillaButton clicked")
                vanillaButton.toggleClicked()
            elif bakingPowderButton.is_clicked(event):
                print("bakingPowderButton clicked")
                bakingPowderButton.toggleClicked()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("other button")
                flourButton.toggleClicked()
                sugarButton.toggleClicked()
                vanillaButton.toggleClicked()
                bakingPowderButton.toggleClicked()
                butterButton.toggleClicked()

            if(flourButton.getWasClicked() and 
               sugarButton.getWasClicked() and 
               vanillaButton.getWasClicked() and 
               bakingPowderButton.getWasClicked() and 
               butterButton.getWasClicked()):
                self.next_button.draw(self.screen)
            else: 
                flourButton.draw(self.screen)
                sugarButton.draw(self.screen)
                vanillaButton.draw(self.screen)
                bakingPowderButton.draw(self.screen)
                butterButton.draw(self.screen)

        self.screen.blit(self.scaled_cooking_image, (0, 0))

    def handle_mall(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.DOG 
        self.screen.fill((40, 80, 40))
        self.next_button.draw(self.screen)

    def handle_dog(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.START 
        self.screen.fill((40, 80, 40))
        self.next_button.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()
