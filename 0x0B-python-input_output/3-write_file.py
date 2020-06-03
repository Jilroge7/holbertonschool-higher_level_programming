#!/usr/bin/python3
"""Module to write to a file"""


def write_file(filename="", text=""):
    """Func to write text to a file"""
    with open('my_first_file.txt', mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
    return len(text)
