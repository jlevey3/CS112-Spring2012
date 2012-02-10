#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()

print "1. First, let's see how long many elements are stored in our list: ", len(nums)

# 2.  Append 3 and 5 to nums

print "2. Let's append a 3 & and 5 to the our list: ",
nums.append(3), nums.append(5),
print nums
# 3.  Remove the last element from nums

print "3. Here, we will remove the 5: ", 
nums.remove(5)
print nums
# 4.  Set the 3rd element to 7

print "4. Now let's set the third element to 7: ", 
del nums[2]
nums[2:2]=[7]
print nums


# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one

print "5. Now let's add another list to this one: "
num2 = input_nums()
nums+=num2
print nums

# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values
print "6. Here, we will make a copy of this new list and delete the 2nd-4th values: "
nums_copy = nums[:]
del nums_copy[1:4]
print nums_copy

# 7-9. [ADVANCED] Print the following:
nums=nums_copy
print "7. Now lets print the first three elements of our newly revised list", nums[0:3]    # first 3 elements
print "8. The last element in the list is", nums[-1]    # last element
print "9. The list beginning with the second element is:", nums[1:]    # a list of the second element
