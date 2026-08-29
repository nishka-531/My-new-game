import pygame

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, text_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        
        # Initialize default font
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        # Get mouse position to handle hover behavior
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        # Draw button background
        pygame.draw.rect(surface, current_color, self.rect)
        
        # Render and center text inside the button
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        # Check if a mouse click event happened inside the button bounds
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class ImageButton: 
    def __init__(self, x, y, width, height, imagePath):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        image = pygame.image.load(imagePath).convert_alpha() 
        self.image = pygame.transform.scale(image, (width, height)) 
        # Rectangle used for positioning and detecting clicks 
        self.image_rect = self.image.get_rect(topleft=(x, y)) 
        self.wasClicked = False 
    def draw(self, surface): 
        surface.blit(self.image, self.image_rect) 
    def is_clicked(self, event): 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if self.image_rect.collidepoint(event.pos): 
                return True 
            return False 
    def toggleClicked(self): 
        self.wasClicked = not self.wasClicked
    def getWasClicked(self):
        return self.wasClicked


