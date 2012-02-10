#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

print "1.", 
if n%2 == 0:
	print "Your number is even."
else:
	print "Your number is odd."

# 2. If n is odd, double it
print "2.", 
if n%2==1:
	n+=n
	print "Your number doubled is %d." %(n)


# 3. If n is evenly divisible by 3, add four
print "3.",
if n%3==0:
	n+=4
	print "Your number is evenly divisible by 3. Your new number + 4 is %d." %(n)
else:
	print "Your number is not divisible by three."

# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

print "4.", 
if grade >= 90:
	print "Your grade receives an A"
elif grade >= 80:
	print "Your grade receives a B"
elif grade >= 70:
	print "Your grade receives a C"
elif grade >= 60:
	print "Your grade receives a D"
elif grade <= 60: 
	print "Sorry...No eval."
