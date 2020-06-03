#!/usr/bin/python3
"""Module for file read function"""


def read_file(filename=""):
    """Function to read a file to standard output"""
    with open('my_file_0.txt', encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
