#!/usr/bun/python3
def multiply_by_2(a_dictionary):

    b_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return b_dictionary
