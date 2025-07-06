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
        pimg = pygame.transform.scale(pimg, (175//2,175//2))
        
        #enemy
        eing = pygame.image.load("Donie.png")
        eing = pygame.transform.scale(eing, (150/2.5, 150/2.5))
        
        #clock
        self.clock = pygame.time.Clock()

        #coin of a rizz
        cimg = pygame.image.load("items/coin_f0.png")
        cimg = pygame.transform.scale(cimg, (50/1.5, 50/1.5))
         
        self.player = Player(75,50, pimg)
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(Enemy(650,195, eing, 500, 675))
        self.enemy_group.add(Enemy(390,395, eing,380,670))
        self.enemy_group.add(Enemy(350,115,eing,220,375))
        
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
        
        #Score
        #font
        self.font = pygame.font.SysFont("Comic san", 30)
        
        #gameover
        self.finish = False
        self.status = ""
        
    def run(self):
        running = True
        while (running):
            delta_time = self.clock.tick(60)/ 1000
            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.bg,(0,0))
            if not self.finish:
                self.player.draw(self.screen)
                self.player.move(delta_time)
                for enemy in self.enemy_group:
                    enemy.draw(self.screen)
                    enemy.move()
                for wall in self.wall_group:
                    wall.draw(self.screen)
                for coin in self.coin_group:
                    coin.draw(self.screen)
                    if self.player.rect.colliderect(coin.rect):
                        coin.kill()
                        self.player.score += 1 
                        if self.player.score == 4:
                            self.finish = True
                            self.status = "W"
                self.wall_check()
                self.donnie_check()
                self.display_score()
            else:
                self.game_over()
            
                
            pygame.display.update() 
                
        pygame.quit()

    def display_score(self):
        text = self.font.render("SCORE: "+str(self.player.score),True,(255,255,255))
        self.screen.blit(text,(0,0))
    def wall_check(self):
        for wall in self.wall_group:
            if self.player.rect.colliderect(wall.rect):
                    self.finish =True
                    self.status = "L"
    def game_over(self):
        if self.status == "L":
            text = self.font.render("You lost LOL trash", True, (0,0,0),(0,255,255))
            self.screen.blit(text,(300,300))
        if self.status == "W":
            text = self.font.render("Yow won and go touch grass :)", True,(0,0,0), (0,255,255))
            self.screen.blit(text,(300,300))
    def donnie_check(self):
        for enemy in self.enemy_group:
            if self.player.rect.colliderect(enemy.rect):
                self.finish = True
                self.status = "L"
game = Game()
game.run()
