#!/usr/bin/env python
#Filename: prissyBotRevised.py

name = raw_input("Enter your name!") #User prompted to enter name

print "Hello there,",name

returnGreeting = raw_input() #user response 

print "That's %s, sir! I expect an apology from you." %(returnGreeting) #copies last user input and asks for apology

raw_input()

#multi line string; asks user for insult
print """Now now...why are you being such a baby?
I'm so sick of dealing with some of you kids...fuckin retards, I tell ya.
C'mon, you don't have to take that.
Give me your best insult!"""

insult = raw_input() #user input saved in var insult

print """%s?!!? You have got to be kidding me. Pitiful.
You fucking tool. Why dont you go jump off a bridge?!?""" %(insult)

raw_input()

print """You just think you're so smart. Talking like you own the motherfuckin place. 
When really you don't amount to shit."""

raw_input()

print """I can at least live up to my reputation;
I'm a smart bot. Ask me any addition problem."""

#asks user for two numbers, then finds and prints the sum
num1 = int(raw_input("Give me any number."))
num2 = int(raw_input("Any other number."))
total = int(num1+num2)
print "Psh...that's so easy. The answer to %d + %d is %d...Dumbass." %(num1,num2, total)

#asks user for two more numbers, then multiplies and finds and prints a false total and the real total
num1 = int(raw_input("I can multiply too... Give me a number."))
num2 = int(raw_input("Now another."))
total = int(num1*num1) #finds total of first number squared
trueTotal = int(num1*num2) #finds total of first * second number

#now will mess around and spit out false total
print "Idiot. Go ahead...make my data! The answer to your question is %d. How did I do?" %(total)

raw_input()

print """I got it wrong?! You must have typed it in wrong...to err is human..
and to blame it on a computer is even more so. You're pathetic. 
The real answer to your question is %d.""" %(trueTotal)

#now prompts user to do division problem. will perform regardless of answer.
decision = raw_input("Okay, would you like to do a division? (Y/N)")
if (decision == "Y") or (decision == "y"):
	num1 = int(raw_input("Great. Enter a number!")) 
	num2 = int(raw_input("enter a second number."))
	total = float(num1/num2)
	print "The answer to your question is %f." %(total)
	
elif (decision == "N") or (decision == "n"): 
	print "Well too bad...you have to do it anyway, biatch!"
	num1 = int(raw_input("Enter a number!")) 
	num2 = int(raw_input("enter a second number."))
	total = float(num1/num2)
	print "The answer to your question is %f." %(total)
	
print "Okay, I'm going to go back to sleep. Thanks for waking me. It was fun. Come back again."