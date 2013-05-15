"""
for.py
=====
* count to 100 starting from 1
	* print out every number
* count to 100 by twos from 0
	* print out every number
* count backwards starting from 100 down to and including 0
	* print out every number
* print out the sum the first 1-100 numbers (which, of course, [doesn't need a loop](http://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/))
* roll a die 1000 times; count how many times a one is rolled!
* fizz buzz: http://c2.com/cgi/wiki?FizzBuzzTest
"""

import random

t=0

for each in range(1,101):
	print(each)
for each in range(0,101,2):
	print(each)
for each in range(100,0,-1):
	print(each)
print((100*(100+1))/2)
for each in range(1000):
	d = random.randint(1,6)
	if d == 1:
		t+=1
print(t)

for each in range(1,101):
	if each%15 == 0:
		print("FizzBuzz")
	elif each%5 == 0:
		print("Buzz")
	elif each%3 ==0:
		print("Fizz")
	else:
		print(each)