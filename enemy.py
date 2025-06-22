import pygame
class Enemy():
    def __init__(self, x ,y,image):
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))