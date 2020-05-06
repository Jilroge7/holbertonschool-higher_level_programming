#!/usr/bin/python3
def no_c(my_string):

    convertList = list(my_string)

    if (len(my_string)) == 0:
        return my_string

    new_string = convertList[:]

    for elements in new_string[:]:
        if elements == 'c' or elements == 'C':
            # stuff goes here
            return new_string
