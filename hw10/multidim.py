#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.
"""


# 1.  find_coins
#       find every coin (the number 1) in a givven room
#          room: a NxN grid which contains coins

#          returns: a list of the location of coind
#
#       Example:
#       0 0 0 1 0 0
#       0 0 1 0 0 0
#       0 0 0 0 1 0
#       0 0 0 0 0 0
# 
#       >>> find_coins(room)
#       [ [3, 0], [2, 1], [4, 2] ]
#      
def find_coins(room):
    "returns a list of every coin in the room"
    locs = []
    for i,row in enumerate(room):
        for j,cell in enumerate(row):
            if cell == 1:
                locs.append((j,i))
    return locs

# 2. distance_from_player
#      calculate the distance from the player for each 
#      square in a room.  Returns a new grid of given
#      width and height where each square is the distance
#      from the player
import math
def distance_from_player(player_x, player_y, width, height):
    "calculates the distance of each square from the player"
	room = []
	for i in range(height):
		row = []
		for h in range(width):
			row.append(0)
		room.append(row)
	room[player_x][player_y] = 0
	
	a = 0
	for x in room:
		b = 0
		for y in x:
			dist = 0
			dist = math.sqrt((a-player_x)**2 + (b-player_y)**2)
			room[a][b]=dist
			b += 1
		a+=1
	return room 
