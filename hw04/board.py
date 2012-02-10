#!/usr/bin/env python
#Filename: board.py
#THIS IS INCOMPLETE
b = "-"
w = "#"
height=int(raw_input("Please enter your checkerboard height: "))
width=int(raw_input("Please enter your checkerboard width: "))
heights=0
widths=0

while widths!=width:
	print (b+w)*(width/2)
	print (b+w)*(height)
	widths+=1
	heights+=1
#if heights<height:
#	print (b+w)*(height/2)
#	heights+=1