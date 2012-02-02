#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""
name = raw_input("Enter your name!")
print "Hello there,",name
returnGreeting = raw_input()
print "That's",returnGreeting,", sir! I expect an apology from you."
raw_input()
print """Now now...why are you being such a baby?
I'm so sick of dealing with some of you kids...fuckin retards, I tell ya.
C'mon, you don't have to take that.
Give me your best insult!"""
insult = raw_input()
print insult,"""?!!? You have got to be kidding me. Pitiful.
You fucking tool. Why dont you go jump off a bridge?!?"""
raw_input()
print """You just think you're so smart. Talking like you own the motherfuckin place. 
When really you don't amount to shit."""
raw_input()
print """I can at least live up to my reputation.
I'm a smart bot. Ask me any addition problem."""
num1 = int(raw_input("Give me any number."))
num2 = int(raw_input("Any other number."))
print "Psh...that's so easy. The answer to", num1,"+", num2, "is",num1+num2,"...Dumbass."
num1 = int(raw_input("I can multiply too... Give me a number."))
num2 = int(raw_input("Now another."))
print "Idiot. Go ahead...make my data! The answer to your question is",num1*num1,". How did I do?"
raw_input()
print """I got it wrong?! You must have typed it in wrong...to err is human..and to blame 
it on a computer is even more so. You're pathetic. 
The real answer to your question is""",num1*num2,"."
decision = raw_input("Okay, would you like to do a division? (Y/N)")
if decision == "Y":
	num1 = int(raw_input("Great. Enter a number!")) 
	num2 = int(raw_input("enter a second number."))
	print "The answer to your question is ",num1/num2,"."
elif decision == "N": 
	print "Well too bad...you have to do it anyway, biatch!"
	num1 = int(raw_input("Great. Enter a number!")) 
	num2 = int(raw_input("enter a second number."))
	print "The answer to your question is ",num1/num2,"."
elif decision == "y":
	num1 = int(raw_input("Great. Enter a number!")) 
	num2 = int(raw_input("enter a second number."))
	print "The answer to your question is ",num1/num2,"."
elif decision =="n":
	print "Well too bad...you have to do it anyway, biatch!"
	num1 = int(raw_input("Great. Enter a number!")) 
	num2 = int(raw_input("enter a second number."))
	print "The answer to your question is ",num1/num2,"."
print "Okay, I'm going to go back to sleep. Thanks for waking me. It was fun. Come back again."
# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

