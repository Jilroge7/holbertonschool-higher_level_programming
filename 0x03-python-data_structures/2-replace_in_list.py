#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    index = 0
    if idx < 0:
        return (my_list)

    for elem in my_list:
        if index == idx:
            my_list[index] = element
            return (my_list)
        index += 1
    if idx > index:
        return (my_list)
