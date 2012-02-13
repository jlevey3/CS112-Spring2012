#!/usr/bin/env python
#edited variables for better names
#define variables
sum=0
input_list=[]
input_number=None

#while loop gets inputs and appends them to list of nums
while input_number != "":
    input_number = raw_input()
    if input_number.isdigit():
    	input_list.append(float(input_number))
#adds inputted numbers to sum
for num in input_list:
    sum+=num 
#divides sum by number of numbers in list == average of list 
print sum/len(input_list)
