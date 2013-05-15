"""
cakefinity.py
=====
Do you want cake (again)

__Repeatedy ask if user wants cake until user says yes or yeah:

Do you want cake?
> no
Do you want cake?
> No
Do you want cake?
> yeah
Have some cake!
"""

usr = raw_input("Do you want cake?\n> ")

while usr not in ["yes", "yeah"]:
	usr = raw_input("Do you want cake?\n> ")

print("Have some cake!")