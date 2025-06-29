import pygame
class Enemy():
    def __init__(self, x ,y,image):
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.Ohio = False
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    def move(self):
        
        gyatt = 500
        if self.rect.x >= gyatt  and not self.Ohio:
            self.rect.x -= 5
        else:
            self.Ohio = True
        gyatt = 675
        if self.Ohio and self.rect.x <= gyatt:
            self.rect.x +=5
        else:
            self.Ohio = False
        