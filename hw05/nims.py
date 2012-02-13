#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

stones = 40
maxTurn = 5
print "Welcome to Nims! Don't take the last stone from the pile or you lose!"
print "Number of stones in the pile: %d" %(stones)
print "Max number of stones per turn: %d" %(maxTurn)

while stones>0:
	p1used = int(raw_input("%d stones left. Player 1's turn [1-5]:" %(stones)))
	if p1used>maxTurn or p1used<0:
		while p1used>maxTurn or p1used<0:
			print "Invalid  number of stones. Go again."
			p1used = int(raw_input("%d stones left. Player 1's turn [1-5]:" %(stones)))
	if p1used > stones:
		while p1used>stones:
			print "There aren't that many stones left!! Go again!!"
			p1used = int(raw_input("%d stones left. Player 1's turn [1-5]:" %(stones)))
	stones-=p1used
	if stones==0:
		print "Player 1 picked the last stone. Player 2 wins!"
		break
	p2used = int(raw_input("%d stones left. Player 2's turn [1-5]:" %(stones)))
	if p2used>maxTurn or p2used<0:
		while p2used>maxTurn or p2used<0:
			print "Invalid  number of stones. Go again."
			p2used = int(raw_input("%d stones left. Player 2's turn [1-5]:" %(stones)))
	if p2used>stones:
		while p2used>stones:
			print "There aren't that many stones left!! Go again!!"
			p2used = int(raw_input("%d stones left. Player 2's turn [1-5]:" %(stones)))
	stones -= p2used
	if stones==0:
		print "Player 2 picked the last stone. Player 1 wins!!"

	