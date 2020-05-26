#!/usr/bin/python3
"""Module for str and repr"""


class Rectangle:
    """class rectangle defined with private inst attrib width and height"""
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
        elif isinstance(value, int):
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
        elif isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """publ ins method to determine area of rect"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """publ inst method to determine perimeter of rect"""
        if int(self.__width) == 0 or int(self.__height) == 0:
            return 0
        else:
            return (int(self.__width) * 2) + (int(self.__height) * 2)

    def __str__(self):
        """built in to return printed representation of string instance"""
        picture = ""
        for i in range(int(self.__height)):
            for i in range(int(self.__width)):
                if int(self.__height) == 0 or int(self.__width) == 0:
                    return picture
                picture += "#"
            picture += '\n'
        return picture[:-1]
