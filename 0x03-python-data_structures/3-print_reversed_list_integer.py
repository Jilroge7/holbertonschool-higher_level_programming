#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    for index in my_list:
        print(my_list[-1])
        my_list[-1] -= 1
