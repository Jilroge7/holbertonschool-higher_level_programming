#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of "
str2 = " is "
greater = " and is greater than 5"
zero = " and is 0"
lessand = " and is less than 6 and not 0"

if number >= 0:
    lastdig = number % 10
if number < 0:
    lastdig = number % -10

if lastdig > 5:
    print("{}{:d}{}{:d}{}".format(str1, number, str2, lastdig, greater))
elif lastdig == 0:
    print("{}{:d}{}{:d}{}".format(str1, number, str2, lastdig, zero))
else:
    print("{}{:d}{}{:d}{}".format(str1, number, str2, lastdig, lessand))
