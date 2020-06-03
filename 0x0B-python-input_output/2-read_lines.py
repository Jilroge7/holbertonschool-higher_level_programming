#!/usr/bin/python3
"""Module for read n lines func"""


def read_lines(filename="", nb_lines=0):
    """Func to read n of lines in a txt file"""
    with open('my_file_0.txt', encoding='utf-8') as a_file:
        lineNum = 0

        for line in a_file:
            if lineNum < nb_lines:
                print(line, end="")

            elif nb_lines == 0:
                print(line, end="")
            lineNum += 1
