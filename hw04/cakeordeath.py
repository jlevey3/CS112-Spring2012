#!/usr/bin/env python
#Filename: cakeordeath.py
slices = 3
running = True
while running:
	response = raw_input("Cake or death? ")
	if response == "Cake":
		print "Here is a slice of cake!"
		slices-=1
		if slices==0:
			print "I am oh so sorry, you have eaten all of the cake."
	elif response == "cake":
			print "Here is a slice of cake!"
			slices-=1
			if slices==0:
				print "I am oh so sorry, you have eaten all of the cake."
	elif response == "Death":
		print "You will have all of your skin sliced open so that your insides fall out before being beheaded."
		running=False 
	elif response == "death":
		print "You will be hung and shot at."
		running=False
print "Loop over!!"
		