"""
cake.py
=====
Write a program that asks for cake and handles a yes, no, or anything other than yes or no.  It will say different things depending on the user's answer.  Here's an example:

Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> no
No cake for you.

Do you want cake?
> blearghhh
I do not understand.
"""

usr = raw_input("Do you want cake?\n> ")

if usr.lower() in ["yes", "yea", "y", "yeah"]:
	print("Here, have some cake.")
elif usr.lower() in ["n", "nope", "no", "nay"]:
	print("No cake for you.")
else:
	print("I do not understand.")