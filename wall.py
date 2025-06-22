import pygame

class Wall(pygame.sprite.Sprite):
    
    def __init__(self,x,y,w,h):
        super().__init__()
        self.rect = pygame.Rect(x,y,w,h)
        self.color = (255,0,0)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        