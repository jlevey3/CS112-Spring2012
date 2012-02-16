#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""
#gives stones value of 40 and max stones per turn to 5. 
stones = 40
maxTurn = 5

#then we will state how many stones there are as well as the max per turn
print "Welcome to Nims! Don't take the last stone from the pile or you lose!"
print "Number of stones in the pile: %d" %(stones)
print "Max number of stones per turn: %d" %(maxTurn)

#while loop that runs until the end--until stones are zero
while stones>0:
	#prompts player 1 to take up to 5 stones
	p1used = int(raw_input("%d stones left. Player 1's turn [1-5]:" %(stones)))
	
	#if player 1 picks more than 5, or less than 0, it is invalid, and they have to go again (while loop until correct)
	if p1used>maxTurn or p1used<0:
		while p1used>maxTurn or p1used<0:
			print "Invalid  number of stones. Go again."
			p1used = int(raw_input("%d stones left. Player 1's turn [1-5]:" %(stones)))
	
	#if player 1 tries to pick more stones than there currently are, prompted to go again until correct
	if p1used > stones:
		while p1used>stones:
			print "There aren't that many stones left!! Go again!!"
			p1used = int(raw_input("%d stones left. Player 1's turn [1-5]:" %(stones)))
	
	#subtracts player 1's stones from the number of total stones		
	stones-=p1used
	
	#if stones are now equal to 0, player 1 has picked the last stone, and they lose
	if stones==0:
		print "Player 1 picked the last stone. Player 2 wins!"
		break #loop ends
		
	#prompts player 2 to choose stones -- same format as above	
	p2used = int(raw_input("%d stones left. Player 2's turn [1-5]:" %(stones)))
	
	#if p2 picks more stones than allowed or less than 0, INVALID and must go again
	if p2used>maxTurn or p2used<0:
		while p2used>maxTurn or p2used<0:
			print "Invalid  number of stones. Go again."
			p2used = int(raw_input("%d stones left. Player 2's turn [1-5]:" %(stones)))
			
	#if p2 picks more stones than there are, they must choose a valid number		
	if p2used>stones:
		#while loop runs until valid number is chosen
		while p2used>stones:
			print "There aren't that many stones left!! Go again!!"
			p2used = int(raw_input("%d stones left. Player 2's turn [1-5]:" %(stones)))
	
	#p2 chosen stones subtracted from total		
	stones -= p2used
	
	#if stones now equal 0, p2 loses. while loop ends (because stones are not > 0) 
	if stones==0:
		print "Player 2 picked the last stone. Player 1 wins!!"

