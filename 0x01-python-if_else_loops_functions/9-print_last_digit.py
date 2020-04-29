#!/usr/bin/python3
def print_last_digit(number):

    result = number % 10
    if result < 0:
        result *= -1
    return result
