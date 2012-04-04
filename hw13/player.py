"""
player.py
Player class for shmup"""
import pygame
from pygame import Surface
from pygame.sprite import Sprite, Group

class Player(Sprite):
    color = 255,25,69
    size = 20,20

    def __init__(self, loc, bounds):
        Sprite.__init__(self) #makes player a sprite object

        self.image = Surface(self.size)
        self.rect = self.image.get_rect() 

        self.rect.center = loc
        self.bounds = bounds

        self.image.fill(self.color)
        self.bullets = Group()

    def update(self):
        self.rect.center = pygame.mouse.get_pos() #player moves/stays with mouse
        self.rect.clamp_ip(self.bounds) #cant leave screen bounds

    def shoot(self):
        if not self.alive():
            return #stop doing anything in this function
        bullet = Bullet(self.bounds)
        bullet.rect.midbottom = self.rect.midtop 
        self.bullets.add(bullet)


class Bullet(Sprite):
    size = 5,10
    color = 0, 255, 0
    speed = 10

    def __init__(self,bounds):
        Sprite.__init__(self)

        self.image = Surface(self.size)
        self.rect = self.image.get_rect()

        self.bounds = bounds
        self.image.fill(self.color)

    def update(self): #causes bullets to move
        self.rect.y -= self.speed 

        if self.rect.top < self.bounds.top: #if bullet top is above top of screen, then kill them - see they disappear as they reach the top edge
            self.kill()
