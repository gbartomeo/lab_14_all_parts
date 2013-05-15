"""
go_for_gold.py
=====
Translate an athlete's finishing placement (1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal.  Do this by asking for user input.  For example:

What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!

"""

usr = raw_input("What number should I translate into a medal?\n> ")

if usr == "1":
	print("gold")
elif usr == "2":
	print("silver")
elif usr == "3":
	print("bronze")
else:
	print("No medal for you!")