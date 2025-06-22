import pygame
from player import *
from enemy import *
from wall import *
class Game():
    
    def __init__(self):
        pygame.init()
        #screen
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Donie escape game")
        
        #bg
        self.bg = pygame.image.load("Background.png")
        self.bg = pygame.transform.scale(self.bg,((800,600)))
        
        #player
        pimg = pygame.image.load("Emu.png")
        pimg = pygame.transform.scale(pimg, (175//1.5,175//1.5))
        
        #enemy
        eing = pygame.image.load("Donie.png")
        eing = pygame.transform.scale(eing, (180/1.5, 180/1.5))
        
        #clock
        self.clock = pygame.time.Clock()
        
        self.player = Player(0,0, pimg)
        self.enemy = Enemy(500,100, eing)
        
        #wall
        self.wall_group = pygame.sprite.Group()
        self.wall_group.add(Wall(30,40, 60,300))
        self.wall_group.add(Wall(150, 200, 50,250))
        self.wall_group.add(Wall(500,300, 35, 70))
        self.wall_group.add(Wall(400,400,10,150))
    def run(self):
        running = True
        while (running):
            delta_time = self.clock.tick(60)/ 1000
            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.bg,(0,0))
            self.player.draw(self.screen)
            self.player.move(delta_time)
            self.enemy.draw(self.screen)
            for wall in self.wall_group:
                wall.draw(self.screen)
            pygame.display.update()         
        pygame.quit()

    
game = Game()
game.run()
