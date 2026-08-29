import pygame
import sys
import button
from enum import Enum, auto

class GameState(Enum):
    START = auto()
    KITCHEN = auto()
    COOKING = auto()
    MALL = auto()
    SHOPPING = auto()
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

        original_start_image = pygame.image.load("start.png").convert()
        self.scaled_start_image = pygame.transform.scale(original_start_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_kitchen_image = pygame.image.load("kitchen.png").convert()
        self.scaled_kitchen_image = pygame.transform.scale(original_kitchen_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_cooking_image = pygame.image.load("cooking.png").convert()
        self.scaled_cooking_image = pygame.transform.scale(original_cooking_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_mall_image = pygame.image.load("mall.png").convert()
        self.scaled_mall_image = pygame.transform.scale(original_mall_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_shopping_image = pygame.image.load("shopping.png").convert()
        self.scaled_shopping_image = pygame.transform.scale(original_shopping_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        original_dog_image = pygame.image.load("dog.png").convert()
        self.scaled_dog_image = pygame.transform.scale(original_dog_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.next_button = button.Button("Next Module", 900, 600, 200, 60, (0, 150, 0), (0, 200, 0), (255, 255, 255))
        x_pos = (self.SCREEN_WIDTH // 2) - (100 // 2)
        y_pos = (self.SCREEN_HEIGHT // 2) - (100 // 2)
        self.start_button = button.Button("START GAME", x_pos, y_pos, 200, 60, (0, 150, 0), (0, 200, 0), (255, 255, 255))

        self.dog_pos = [150, 800]
        self.dog_speed = 5
        self.dogRightReq = False
        self.dogLeftReq = False

        original_dog_sprite = pygame.image.load("dogSprite.png").convert_alpha()
        self.dog_sprite = pygame.transform.scale(original_dog_sprite, (100, 100))
        self.dog_rect = self.dog_sprite.get_rect(topleft=(150, 100))

        # Cooking buttons 
        self.flourButton = button.ImageButton(100, 175, 200, 200, "flour.png")
        self.sugarButton = button.ImageButton(100, 400, 200, 200, "sugar.png")
        self.vanillaButton = button.ImageButton(1000, 200, 200, 200, "vanilla.png")
        self.bakingPowderButton = button.ImageButton(1000, 400, 200, 200, "bakingPowder.png")
        self.butterButton = button.ImageButton(500, 500, 200, 200, "butter.png")

        # Start the game on the Menu screen
        self.current_state = GameState.START

    async def run(self):
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
            elif self.current_state == GameState.SHOPPING:
                self.handle_shopping()
            elif self.current_state == GameState.DOG:
                self.handle_dog()
                
            pygame.display.flip()
            self.clock.tick(60)
            await asyncio.sleep(0)

        pygame.quit()
        sys.exit()

    # --- STATE HANDLER METHODS---

    def handle_start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.start_button.is_clicked(event):
                self.current_state = GameState.KITCHEN
        self.screen.fill((0, 0, 40)) 
        self.screen.blit(self.scaled_start_image, (0, 0))
        self.start_button.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

    def handle_kitchen(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.COOKING 
        self.screen.blit(self.scaled_kitchen_image, (0, 0))
        self.next_button.draw(self.screen)

    def handle_cooking(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.MALL

            if self.butterButton.is_clicked(event):
                print("butterButton button Clicked")
                self.butterButton.toggleClicked()
            elif self.flourButton.is_clicked(event):
                print("flour button clicked")
                self.flourButton.toggleClicked()
            elif self.sugarButton.is_clicked(event):
                print("sugar button clicked")
                self.sugarButton.toggleClicked()
            elif self.vanillaButton.is_clicked(event):
                print("vanillaButton clicked")
                self.vanillaButton.toggleClicked()
            elif self.bakingPowderButton.is_clicked(event):
                print("bakingPowderButton clicked")
                self.bakingPowderButton.toggleClicked()

        self.screen.blit(self.scaled_cooking_image, (0, 0))
        if(self.flourButton.getWasClicked() and 
            self.sugarButton.getWasClicked() and 
            self.vanillaButton.getWasClicked() and 
            self.bakingPowderButton.getWasClicked() and 
            self.butterButton.getWasClicked()):
            pygame.draw.circle(self.screen, (237, 197, 123), [500, 350], 40)
            self.next_button.draw(self.screen)
        else: 
            self.flourButton.draw(self.screen)
            self.sugarButton.draw(self.screen)
            self.vanillaButton.draw(self.screen)
            self.bakingPowderButton.draw(self.screen)
            self.butterButton.draw(self.screen)

    def handle_mall(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.next_button.is_clicked(event):
                self.current_state = GameState.SHOPPING 
        self.screen.fill((40, 80, 40))
        self.next_button.draw(self.screen)

        self.screen.blit(self.scaled_mall_image, (0, 0))

        self.next_button.draw(self.screen)

    def handle_shopping(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if self.next_button.is_clicked(event):
                    self.current_state = GameState.DOG 
            
            self.screen.blit(self.scaled_shopping_image, (0, 0))
            self.next_button.draw(self.screen)

    def handle_dog(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.next_button.is_clicked(event):
                self.current_state = GameState.START

        # Move dog
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dog_pos[0] -= self.dog_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dog_pos[0] += self.dog_speed

        # Keep dog on screen
        self.dog_pos[0] = max(
            0,
            min(self.dog_pos[0], self.SCREEN_WIDTH - 100)
        )

        # Check if dog reached both sides
        if self.dog_pos[0] >= self.SCREEN_WIDTH - 100:
            self.dogRightReq = True

        if self.dog_pos[0] <= 0:
            self.dogLeftReq = True

        # Draw background
        self.screen.blit(self.scaled_dog_image, (0, 0))

        # Draw moving dog
        self.screen.blit(self.dog_sprite, self.dog_pos)

        # Show next button after visiting both sides
        if self.dogRightReq and self.dogLeftReq:
            self.next_button.draw(self.screen)

if __name__ == "__main__":
    import asyncio

    game = Game()
    asyncio.run(game.run())
