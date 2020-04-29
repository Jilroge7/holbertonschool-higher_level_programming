#!/usr/bin/python3
def print_last_digit(number):

    result = number % 10
    print("{:d}".format(result), end='')
    if result < 0:
        result = result * -1
    return result
