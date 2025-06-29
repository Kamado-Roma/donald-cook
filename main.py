import pygame
from player import *
from enemy import *
from wall import *
from coin import *
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
        eing = pygame.transform.scale(eing, (150/1.5, 150/1.5))
        
        #clock
        self.clock = pygame.time.Clock()

        #coin of a rizz
        cimg = pygame.image.load("items/coin_f0.png")
        cimg = pygame.transform.scale(cimg, (50/1.5, 50/1.5))
         
        self.player = Player(75,50, pimg)
        self.enemy1 = Enemy(650,175, eing)
        self.enemy2 = Enemy(390,375, eing)
        self.enemy3 = Enemy(350,90,eing)
        
        #wall
        self.wall_group = pygame.sprite.Group()
        self.wall_group.add(Wall(0,0, 50,590))
        self.wall_group.add(Wall(175, 0, 50,450))
        self.wall_group.add(Wall(500,300, 350, 30))
        self.wall_group.add(Wall(325,400,50,200))
        self.wall_group.add(Wall(0,590,900,10))
        self.wall_group.add(Wall(0,0,900,10))
        self.wall_group.add(Wall(750,0, 50,590))
        self.wall_group.add(Wall(450,0, 50,175))
        self.wall_group.add(Wall(175,190, 180,50))
        self.wall_group.add(Wall(550,500, 50,100))

        #coin
        self.coin_group = pygame.sprite.Group()
        self.coin_group.add(Coin(675, 50,cimg))
        self.coin_group.add(Coin(675, 550,cimg))
        self.coin_group.add(Coin(375, 45,cimg))
        self.coin_group.add(Coin(100, 525,cimg))
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
            self.enemy1.draw(self.screen)
            self.enemy1.move()
            self.enemy2.draw(self.screen)
            self.enemy3.draw(self.screen)
            for wall in self.wall_group:
                wall.draw(self.screen)
            for coin in self.coin_group:
                coin.draw(self.screen)
            pygame.display.update()         
        pygame.quit()

    
game = Game()
game.run()
