#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = 0

print "1.",
num = int(raw_input("Please enter a number.")) 
while num%3!=0:
	num = int(raw_input("Please enter a number.")) 
print num

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

print "2. Countdown from", num
while num>0:
	num-=3
	print num


# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.

num = int(raw_input("3. Countdown from: "))
print num
if num%3==0:
	while num>0:
		num-=3
		print num
elif num%2==0:
	while num>0:
		num-=2
		print num
else:
	while num>0:
		num-=1
		print num

