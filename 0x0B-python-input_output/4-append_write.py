#!/usr/bin/python3
"""Module for append write func"""


def append_write(filename="", text=""):
    """Func to append string to end of text file"""
    with open(filename, mode='a', encoding='UTF8') as a_file:
        a_file.write(text)
    return len(text)
