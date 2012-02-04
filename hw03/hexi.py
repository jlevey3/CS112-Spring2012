#!/usr/bin/env python

name = raw_input("Hello. What is your name? ")
s = " "

print """Okay, %s, We are going to make a hexidecimal conversion table
                       Out of your input
----------------------------------------------------------""" %(name)

num1 = int(raw_input("Enter your first number (less than 256)."))
num2 = int(raw_input("Enter a number (less than 256)."))
num3 = int(raw_input("Enter a number (less than 256)."))
num4 = int(raw_input("Enter a number (less than 256)."))
num5 = int(raw_input("Enter a number (less than 256)."))
hnum1 = hex(num1)
hnum2 = hex(num2)
hnum3 = hex(num3)
hnum4 = hex(num4)
hnum5 = hex(num5)
bnum1 = bin(num1)
bnum2 = bin(num2)
bnum3 = bin(num3)
bnum4 = bin(num4)
bnum5 = bin(num5)

print "INT",s*3,"|",s*3,"HEX",s*3,"|",s*3,"BIN"
print "-------------------------------------------"
print num1,s*8,hnum1,s*8,bnum1
print num2,s*8,hnum2,s*8,bnum2
print num3,s*8,hnum3,s*8,bnum3
print num4,s*8,hnum4,s*8,bnum4
print num4,s*8,hnum4,s*8,bnum5
