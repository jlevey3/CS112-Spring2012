#!/usr/bin/env python
"""lists.py

A bunch of excercises to see if you understand list comprehensions
"""
import glob

# Solve the following problems with one python statement.  It is fine 
# to break up the statement into multiple lines as long as it is only
# one actual command.
#
# This is fine:
#   print [ (x,y) 
#           for x in range(10)
#           for y in range(10) ]
#

# 1. Read a bunch of numbers from the input separated by spaces and 
#    convert them to ints
print "1.", 
nums = []
for x in raw_input("Please enter a list of numbers seperated by spaces: ").split(" "):
	nums.append(int(x))
print nums

# 2.  Read another bunch of numbers, convert them, and return the list 
#     of only the first 3
print "2.", 
nums=[]
for x in raw_input("Please enter a list of numbers seperated by spaces: ").split(" "):
	nums.append(int(x))
print nums[0:3]

# 3.  Read a bunch of words separated by commas from the command line,
#     remove any excess spaces, and print a list of their lenghts
print "3.", 
words=[]
for x in raw_input("Please enter a list of words seperated by commas: ").split(","):
	words.append(len(x))
print words
# 4.  Create a list of every multiple of 3 between 1 and 100 with their 
#     index FIX this- TRY ENUMERATE FUNCTION
#        ex:  [ [0,3], [1,6], [2,9]...]
print "4.", #[[x,y] for x in range(0,33) 
#for y in range(3,101,3)]
#if x==y.index(y)


# 5. create a list of every card in a deck of cards 
print "5.", [[x,y] for x in ["Spades","Hearts","Diamonds","Clubs"]
for y in ["2","3","4","5","6","7","8","9","JACK","QUEEN","King","ACE"]]

# 6.  Create a 5 by 5 array filled with zeros
print "6.", []

# 7.  Make a list of every perfect square between 1 and 1000
print "7.", [x**2 for x in range(1,101)]

# 8.  Make a list of every perfect square between 1 and 1000 
#     a different way
print "8.", [x*x for x in range(1,101)]

# 9.  List every python file in this directory
print "9.", glob.glob('*.py')

# 10.  Print a list of every pythagorean triple with a side less than
#      or equal to 20.  Don't include duplicates ([3,4,5] == [4,3,5])
print "10.", [[x,y,z] for x in range(1,21)
for y in range(1,21)
for z in range(1,21)
if ((x**2+y**2)==z**2) and y<=x]



# I couldn't in good concious include this, but it is fun to 
# figure out/find.

## NOT REQUIRED
# 11.  Print a list of every prime number less than 100
#print "11.", [for x in range(100)
#if x**.5 ==x%0]