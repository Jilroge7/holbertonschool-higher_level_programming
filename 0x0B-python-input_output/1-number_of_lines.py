#!/usr/bin/python3
"""Module for number of lines func"""


def number_of_lines(filename=""):
    """Func to return number of lines in a txt file"""
    with open('my_file_0.txt', encoding='utf-8') as a_file:

        lineNum = 0

        for eachLine in a_file:
            lineNum += 1
        return lineNum
