#!/usr/bin/python3
"""Module for read n lines func"""


def read_lines(filename="", nb_lines=0):
    """Func to read n of lines in a txt file"""
    with open(filename, encoding='UTF8') as a_file:
        lineNum = 0

        for line in a_file:
            if lineNum < nb_lines:
                print(line, end="")

            elif nb_lines <= 0 or nb_lines >= len(line):
                print(line, end="")
            lineNum += 1
