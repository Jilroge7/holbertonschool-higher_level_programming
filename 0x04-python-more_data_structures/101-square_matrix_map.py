#!/usr/bin/python3
def square_matrix_map(matrix=[]):

    i = 0
    j = 1

    newList = [list(map(lambda j: j ** 2, i)) for i in matrix]
    return newList
