#!/usr/bin/env python0
# Filename: fraction.py

print("Hello, ready for some fractions?")
num = int(raw_input("First, enter a number to be used for your numerator."))
den = int(raw_input("Great! Now, enter a second number for your denomenator."))
print """Okay. Let me think about this....
So you want me to reduce %d/%d...
That wont be too difficult...""" %(num,den)

reduced = num/den
r = num%den

print "Okay. Your number is now %d with a remainder of %d."%(reduced,r)