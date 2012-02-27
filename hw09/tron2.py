#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""
import pygame, sys, time
from pygame.locals import *
from pygame import draw
from random import randrange



#Create variables
red_x, red_y = 10,250 #red position
blue_x, blue_y = 590,250 #blue position
red_dx, red_dy = 0,0 #direction; begins at 0
blue_dx, blue_dy = 0,0
p1 = []
p2 = []
trail = []
BLUE = (0,255,255)
RED = (168,0,0)
pygame.display.set_caption("TRON")

def drawPlayer(surf, pos, color=(255,255,255), square=10):
    x,y = pos
    draw.rect(surf, color, (x,y,square,square))

def movePlayer(x, y, dx, dy, up, down, left, right, bounds):
    x += dx
    y += dy

#move up
    if event.type == KEYDOWN and event.key == up and dy != 10:
        dx = 0
        dy = -10

#down
    if event.type == KEYDOWN and event.key == down and dy != -10:
        dx = 0
        dy = 10

#left
    if event.type == KEYDOWN and event.key == left and dx != 10:
        dx = -10
        dy = 0

#right    
    if event.type == KEYDOWN and event.key == right and dx != -10:
        dx = 10
        dy = 0   
#sets boundaries-- if player hits bounds on any direction GAME OVER
    if y < bounds.top and y > bounds.bottom:
        dx, dy = 0,0
        pygame.quit()
        sys.exit()
    if x <bounds.left and x > bounds.right:
        dx,dy = 0,0
        pygame.quit()
        sys.exit()
    return x,y,dx,dy

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        
        screen.fill((0,0,0))

    #begin game
    if event.type == KEYDOWN and event.key == K_SPACE and blue_x == 590 and blue_y == 250 and red_x == 10 and red_y == 250:
        blue_dx, blue_dy = -10, 0
        red_dx, red_dy = 10, 0

    #drawing red lines
    red_x, red_y, red_dx, red_dy = movePlayer(red_x, red_y, red_dx, red_dy, K_w, K_s, K_a, K_d, screen_bounds)
    p1.append([red_x, red_y])
    for i in range(len(p1)):
        drawPlayer(screen, p1[i], RED)

    #red crashes
    for t in trail: 
        if(red_x,red_y) == t:
            red_dx, red_dy = 0, 0
            blue_dx, blue_dy = 0,0
    trail.append((red_x, red_y))
        
    #drawing blue
    blue_x, blue_y, blue_dx, blue_dy = movePlayer(blue_x, blue_y, blue_dx, blue_dy, K_UP, K_DOWN, K_LEFT, K_RIGHT, screen_bounds)
    p2.append([blue_x,blue_y])
    for v in range (len(p2)):
        drawPlayer(screen, p2[v], BLUE)
            
    #blue crashes
    for t in trail:
        if(blue_x,blue_y) == t:
            blue_dx, blue_dy = 0,0
            red_dx, red_dy = 0,0       
    trail.append((blue_x,blue_y))

    pygame.display.flip()
    clock.tick(30)
