#!/usr/bin/env python
#Note: I worked hours and hours on this and gave it my best. I'm close
import pygame
from pygame.locals import *
from random import randrange

#settings
FPS = 30

#colors
C_HIDDEN = 80,80,80
C_BORDER = 0,0,0
C_ACTIVE = 255,255,255
C_CLEARED = 180,180,180
C_BOMB = 129,21,55
C_FLAG = 50,32,111

def clearSquare(world,x,y):
    world[x][y]["cleared"] = True
    return world[x][y]["bomb"]
	
def flagSquare(world,x,y):
	world[x][y]["flagged"] = not world[x][y]["flagged"]

def bomb_at(world, x, y):
    width = len(world)
    height = len(world[0])

    # if out of bounds
    if x<0 or x>=width or y<0 or y>=height:
        return False
    else:
        return world[x][y]["bomb"]

def countTouching(world,x,y):
    # check each neigbor for bomb_at
        # add 1 if bomb
    cell = world[x][y]
    if bomb_at(world,x-1,y-1):
        cell["count"] +=1
    if bomb_at(world,x+1,y+1):
        cell["count"] += 1
    if bomb_at(world,x-1,y+1):
        cell["count"] += 1
    if bomb_at(world,x+1,y-1):
        cell["count"] += 1
    if bomb_at(world,x,y+1):
        cell["count"] += 1
    if bomb_at(world,x+1,y):
        cell["count"] += 1
    if bomb_at(world,x-1,y):
        cell["count"] += 1
    if bomb_at(world,x,y-1):
        cell["count"] += 1
    

#Game
def game(tile,width,height,numBombs):
    #init - window size = width*tile
    screen = pygame.display.set_mode((width*tile, height*tile))
    font = pygame.font.Font(None, tile)
    numFlag = numBombs
    #this will store all of the game data...now every tile will have its own dict that will store its information
    world = []
    for x in range(width):
        row = []
        for y in range(height):
            cell = {}
            cell["bomb"]=False #make sure that not every cell has a bomb
            #make tiles- top left 
            cell["rect"] = pygame.Rect(x*tile, y*tile, tile, tile)
            cell["count"] = 0
            cell["cleared"]=False
            row.append(cell)
        world.append(row)
        if cell["count"]==1:
            print "1"

    #place bombs and make sure that there are no other bombs there
    c = 0 #bombs=10 (see where you call game function- 4th num)

    while c<numBombs:
        #pick random location
        x = randrange(width)
        y = randrange(height)
        if not world[x][y]["bomb"]:
            world[x][y]["bomb"] = True
            c += 1
	
	
    #loop through each cell and count touching
    for y in range(height):
        for x in range(width):
            countTouching(world,x,y)
            print world[x][y]["count"], 
        print ""


    #loop
    clock = pygame.time.Clock()
    done = False

    #flags
    lmbClicked = False
    rmbClicked = False
    actionClearSquare = False
    actionFlagSquare = False
    gameOver = False

    while not done:
        #input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True

        #click mouse
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                lmbClicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                lmbClicked = False
                actionClearSquare = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                rmbClicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                rmbClicked = False
                actionFlagSquare = True
        #update
        if actionClearSquare:
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
      	if not world[x][y]["flagged"]:
            gameOver = clearSquare(world,x,y)
            actionClearSquare = False
			
       	if actionFlagSquare:
         	x,y = pygame.mouse.get_pos()
	       	x /= tile
	       	y /= tile
	       	if numFlag > 0 and not world[x][y]["flagged"]:
		       	world[x][y]["flagged"]=True
		       	numFlag-=1
                elif world[x][y]["flagged"]:
                    world[x][y]["flagged"]=False
                    numFlag+=1
			
                actionFlagSquare = False
			
		if gameOver:
			for x in range(width):
				for y in range(height):
					worldpx[x][y]["cleared"] = True
			
        
        
        
        #display
        screen.fill(C_BORDER) #fill wth border color
        for x in range(width):
            for y in range(height):

                #get rect for cell
                rect = world[x][y]["rect"]

                #color for cell
                if world[x][y]["cleared"]:
                    bg_color = C_CLEARED
                elif lmbClicked and rect.collidepoint(pygame.mouse.get_pos()):
                    bg_color = C_ACTIVE
                elif rmbClicked and rect.collidepoint(pygame.mouse.get_pos()):
                    bg_color = C_FLAG
                else:
                    bg_color = C_HIDDEN

                #draw background, inflate so can nsee squares
                screen.fill(bg_color, rect.inflate(-2,-2))
                
                #draw cleared graphics
                if world[x][y]["cleared"]:
                    if world[x][y]["bomb"]:
                        pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-2,-2))
                    elif world[x][y]["count"]:
                        n = world[x][y]["count"]
                        color = [(23,22,11),(77,23,112),(255,3,14),(4,150,200),(222,11,112),(237,85,30),(66,66,233),(38,75,89)]
                        text = font.render(str(n), True, color[n-1])
                        loc = text.get_rect()
                        loc.center = rect.center
                        screen.blit(text,loc)
        #refresh
        pygame.display.flip()
        clock.tick(FPS)


#application
def main():
    pygame.init()
    game(50,10,10,10)


main()
print "ByeBye"
