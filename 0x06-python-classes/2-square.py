#!/usr/bin/python3
"""Module here"""


class Square:
    """Square defined class with private attribute size"""
    def __init__(self, size=0):
        self.__size = size  # size is user input or prog input
        if size is not 0:
            self._size = size

        if (str(size).isdigit()):
            try:
                if size >= 0:
                    self._size = size
            except ValueError:
                print("size must be >= 0")
            except:
                print("size must be an integer")
