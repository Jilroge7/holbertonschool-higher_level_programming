#!/usr/bin/python3
""" Function to find peak of unsorted integers in an array """


def find_peak(list_of_integers):
    """ Function find_peak """
    i = 0

    if list_of_integers is None:
        return None

    if len(list_of_integers) % 3 == 0:
        """ If length is odd only one peak """
        for index in range(len(list_of_integers)):
            """ Traverse through list """
            if index[i] > index[i + 1]:
                """ compare left and right values """
                peak = index[i]
                """ if true store larger value in peak """
            else:
                """ store right value in peak """
                peak = index[i + 1]
            i += 1
        return peak

    elif len(list_of_integers) % 2 == 0:
        """ If length is even there are two peaks """
        for index in range(len(list_of_integers)):
            if index[i] > index[i + 1]:
                peak = index[i]
            else:
                peak = index[i + 1]
            i += 1
        return peak
