#!/usr/bin/python3
"""Module for class Square 2.0"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square inherits Rectangle class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """builting to print str repr of instance"""
        result = "[Square] {:d}/{:d}".format(int(self.__size), (
                 int(self.__size)))
        return result
