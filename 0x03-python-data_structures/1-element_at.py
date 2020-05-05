#!/usr/bin/python3
def element_at(my_list, idx):

    if idx < 0:
        return None

    for index in my_list:
        if index == idx:
            return (my_list[index])
    if idx > index:
        return None
