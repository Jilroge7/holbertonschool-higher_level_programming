#!/usr/bin/python3
"""Module of real definition of a rectangle"""


class Rectangle:
    """class Rectangle defined with priv inst attrib width and height"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method to get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """method to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """method to get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
