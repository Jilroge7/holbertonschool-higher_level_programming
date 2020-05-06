#!/usr/bin/python3
def max_integer(my_list=[]):

    maxNumber = my_list[0]

    if len(my_list) == 0:
        return None

    for elements in my_list:
        if elements > maxNumber:
            maxNumber = elements

    return maxNumber
