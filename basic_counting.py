"""
basic_counting.py
=====
* count from 2 through 8 by 2's
* print every number out
* count odd numbers except 13 (go up to 99)
	* print all of the odd numbers from 1-99
	* skips 13

"""

for each in range (2,9):
	if each%2 == 0:
		print(each)

for each in range(100):
	if each%2 == 1 and each != 13:
		print(each)