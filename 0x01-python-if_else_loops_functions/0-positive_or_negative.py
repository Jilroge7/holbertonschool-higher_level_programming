#!/usr/bin/python3
import random
number = random.randint(-10, 10)
positive = " is positive"
zero = " is zero"
negative = " is negative"

if number > 0:
    print("{:d}{}".format(number, positive))

elif number < 0:
    print("{:d}{}".format(number, negative))
else:
    print("{:d}{}".format(number, zero))
