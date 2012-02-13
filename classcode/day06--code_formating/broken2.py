#!/usr/bin/env python
from random import randint
#variables
s=1
numInput=int(raw_input())
numList=[]
#prints as many random numbers as was specified in numInput
for _ in range(numInput):
    numList.append(randint(0,20))
print numList

while s:
    s=0
    for num in range(1,numInput): 
        if numList[num-1]>numList[num]:
            t1=numList[num-1]
            t2=numList[num]
            numList[num-1]=t2
            numList[num]=t1
            s=1

print numList
