import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x ,y,image,gyatt, butt):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.Ohio = False
        self.gyatt = gyatt
        self.butt = butt
        self.offset_w = 20*1.5
        self.offset_x = 10*1.5
        self.rect.w -= self.offset_w
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x-self.offset_x,self.rect.y))
        # pygame.draw.rect(screen, (255,0,0), (self.rect.x, self.rect.y, self.rect.w, self.rect.h), 1)
    def move(self):
        
        
        if self.rect.x >= self.gyatt  and not self.Ohio:
            self.rect.x -= 3
        else:
            self.Ohio = True
        
        if self.Ohio and self.rect.x <= self.butt:
            self.rect.x +=3
        else:
            self.Ohio = False
        