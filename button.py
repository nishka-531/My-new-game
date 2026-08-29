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
