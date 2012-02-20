#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

n=len(nums) 
for x in range(n): #goes through the whole array because n=len(nums)
   pos=x #sets pos to x, so cycles through and constantly reassigns pos
   for i in range(pos+1, n): #in range of next number and the len of nums
        if nums[i]<nums[pos]: #if i is less than pos, resort it
            pos=i
            
   nums[x],nums[pos]=nums[pos],nums[x] #has to be in for loop!!!

print "After sort:"
print nums
