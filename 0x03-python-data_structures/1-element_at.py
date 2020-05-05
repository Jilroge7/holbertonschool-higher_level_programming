#!/usr/bin/python3
def element_at(my_list, idx):

    index = 0
    if idx < 0:
        return None

    for element in my_list:
        print("{:d}: idx".format(idx))
        print("{:d}: index".format(index))
        print("{:d}:element".format(element))
        if index == idx:
            print("idx equals element")
            return (element)
        index += 1
    if idx > index:
        return None
