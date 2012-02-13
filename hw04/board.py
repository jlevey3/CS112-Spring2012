#!/usr/bin/env python
#Filename: board.py
#THIS IS INCOMPLETE
b = "-"
w = "#"
height=int(raw_input("Please enter your checkerboard height: "))
width=int(raw_input("Please enter your checkerboard width (please user an even #): "))
heights=0
widths=0

while heights!=height:
		print (b+w)*(width/2)
		heights+=1
		if widths!=width:
			print (w+b)*(width/2)
			widths+=1