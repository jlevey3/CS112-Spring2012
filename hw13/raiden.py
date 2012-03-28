#!/usr/bin/env python
#unfinished at this point!!!

import pygame, math, random
from pygame.locals import *


MAX_X = 780
MAX_XSHIP = 760
MAX_Y = 580
MIN_X = 0
MIN_Y = 0

NUM_ENEMY = 40

class StatusDisplay(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 0
        self.score = 0
        self.wave = 1
        self.font = pygame.font.SysFont("arial", 22)
        self.text = "SHIELD HITS: %d  MISSILE HITS: %d WAVE NUMBER: %d" %(self.lives, self.score, self.wave)
        self.image = self.font.render(self.text, 1, (0,0,255))
        self.rect = self.image.get_rect()

    def update(self,lives,score,waves):
        if lives > 0:
            self.lives += 1
        elif score > 0:
            self.score += 1
        elif wave > 0:
            self.wave += 1
        self.text = "SHIELD HITS: %d MISSILE HITS: %d WAVE NUMBER: %d" % (self.lives, self.score, self.wave)
        self.image = self.font.render(self.text, 1, (0,0,255))
        self.rect = self.image.get_rect()

class Enemy(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagearray=[]
        self.images = pygame.image.load('light .bmp').convert()
        self.images.set_colorkey((255,0,255))
        for i in range(0,120,24):
            self.imagearray.append(self.images.subsurface((i,0,24,24)
        self.image = self.imagearray[0]
        self.rect = self.imagearray[0].get_rect()
        self.rect.topleft = [random.randrange(0,780),random.randrange(0,200)]
        self.direction = [random.randrange(1,5),random.randrange(1,5)]
        self.movement_ticks = 0                                            
        self.animationcounter = random.randrange(0,4)
        self.animation_ticks = 0
    def update(self,timer):
        if self.movement_ticks < timer:
            self.movement_ticks = timer
            if self.rect.left < MIN_X or self.rect.left > MAX_X:
                self.direction[0] = -self.direction[0]
            if self.rect.top < MIN_Y or self.rect.top > MAX_Y:
                self.direction[1] = -self.direction[1]
  
            self.rect.left = self.rect.left + self.direction[0]
            self.rect.top = self.rect.top + self.direction[1]
                 
            self.movement_ticks += 20
               
            self.image = self.imagearray[self.animationcounter]
            if self.animation_ticks < timer:
                self.animation_ticks = timer
                self.animationcounter -= 1
                if self.animationcounter < 0:
                    self.animationcounter = 4
                self.animation_ticks += 150
class Player(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.bmp').convert()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [350,580]
    
    def update(self, direction):
        if direction == 0 and self.rect.left > MIN_X:
            self.rect.left -=4
        elif direction == 1 and self.rect.left < MAX_XSHIP:
            self.rect.left +=4
    
class Shoot(Sprite):
    def __init__(self,initialpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('missile .bmp').convert()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = initialpos
    def update(self):
        if self.rect.top > MIN_Y:
            self.rect.top -= 4
        else: 
            self.kill()

class Explosion(Sprite):
    def __init__(self, initialpos):
        pygame.sprite.Sprite.__init__(self)                          
        self.imagearray=[]
        self.images = pygame.image.load('explos.bmp').convert()
        self.images.set_colorkey((255,0,255))
        for i in range(0,240,60):
            self.imagearray.append(self.images.subsurface((i,0,60,60)))
        self.image = self.imagearray[0]
        self.rect = self.imagearray[0].get_rect()
        self.animation_ticks = 0
        self.animationcounter = 0
        self.rect.topleft = initialpos

    def update(self,timer):
        if self.animation_ticks < timer:
            self.animation_ticks = timer
            self.image = self.imagearray[self.animationcounter]
            self.animationcounter+=1                        
            if self.animationcounter > 3: 
                self.kill()
            self.animation_ticks+=50
#main game loop
def main():
    GAMEOVER = FALSE
    missile_missed = 0
    missile_hits = 0
    missileticks = 0
    SCREENSIZE = [800,600]
    pygame.init()
   
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREENSIZE)
    
    enemies = pygame.sprite.RenderUpdates()

    i = NUM_ENEMY
    while i > 0:
        enemies.add(Enemy())
        i -= 1
   
    statusdisplay = pygame.sprite.RenderUpdates()
    statusdisplay.add(StatusDisplay())
   
    player = pygame.sprite.RenderUpdates()
    player.add(Player())
   
    missiles = pygame.sprite.RenderUpdates()
    explosions = pygame.sprite.RenderUpdates()
    background = pygame.image.load('background.bmp').convert()
    screen.blit(background,(0,0))

    pygame.display.update()
    
    while not GAMEOVER:
        time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                GAMEOVER = True
##left and right steer the ship, space fires missile
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            GAMEOVER = True
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            direction = 1
        elif event.type == KEYDOWN and event.key == K_LEFT:
            direction = 0
        else direction = 3
        if event.type == KEYDOWN and event.key == SPACE:
            fired = 1
        else: fired = 0
       
        if fired == 1 and time > missileticks:
            missileticks = time + 300
            a,b,c,d = rectlistplayer[0]
            missiles.add(Shoot((a+18,b)))
                             
                                 
        player.clear(screen,background)
        enemies.clear(screen,background)
        missiles.clear(screen,background)
        explosions.clear(screen,background) 
        statusdisplay.clear(screen,background)
        player.update(direction)                      
        missiles.update()
        enemies.update(time)
        explosions.update(time)
       
        for i in pygame.sprite.groupcollide(enemies, missiles, True, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a-20, b-20)))
            statusdisplay.update(0,1,0)
        for i in pygame.sprite.groupcollide(player, enemies, False, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a-20,b-20)))
            statusdisplay.update(1,0,0)
        
        rectlistplayer = player.draw(screen)
        rectlistmissiles = missiles.draw(screen)
        rectlistenemies = enemies.draw(screen)
        
        if len(rectlistenemies) == 0:
            i = NUM_ENEMY
            while i > 0:
                aliens.add(Enemy())
                i -=1
            statusdisplay.update(0,0,1)

        rectlistexplosions = explosions.draw(screen)
        rectliststatusdisplay = statusdisplay.draw(screen)
        pygame.display.update(rectlistplayer)
        pygame.display.update(rectlistmissiles)
        pygame.display.update(rectlistenemies)
        pygame.display.update(rectlistexplosions)
        pygame.display.update(rectliststatusdisplay)
 
        clock.tick(60)
if __name__ == '__main__': main()

                                

                     
            
        
                                                         
                                                        
