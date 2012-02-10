#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

print "1.", 
sum=0
for num in nums:
	sum = sum + num
print ("The sum of your numbers is: %d") %(sum)


# 2. Print every even number in nums
print "2. The even numbers in your list are:",
evens=[]
for num in nums:
	if num%2 == 0:
		evens.append(num)
print evens

# 3. Does nums only contain even numbers? 
#Note: I found this a bit tricky...it seemed that if the only_even was set to False before the if statement (ie. global variable)
#that it would retain its falseness even if the statement was true because the if statement ended and it was set to a local var ...
only_even=True
print "3.",
for num in nums:
	if num%2==1:
		only_even==False
if only_even == True:
    	print "only even"
elif only_even == False:
    	print "some odd"

# 4. Generate a list every odd number less than 100. Hint: use range()
print "4.", 
for i in range(1,100,2):
	print i

# 5. [ADVANCED]  Multiply each element in nums by its index
print "5.",
for num in nums:
	num*[num:nums]
	
