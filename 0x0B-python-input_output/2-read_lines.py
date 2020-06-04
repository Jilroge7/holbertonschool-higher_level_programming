#!/usr/bin/python3
"""Module for read n lines func"""


def read_lines(filename="", nb_lines=0):
    """Func to read n of lines in a txt file"""
    with open(filename, encoding='UTF8') as a_file:
        lineNum = 0

        for line in a_file:
            lineNum += 1
            if nb_lines <= 0 or nb_lines >= lineNum:
                print(line, end="")

            elif lineNum < nb_lines:
                print(a_file.readline(), end="")

            if lineNum == nb_lines:
                break
