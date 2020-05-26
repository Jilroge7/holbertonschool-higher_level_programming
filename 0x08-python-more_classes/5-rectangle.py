#!/usr/bin/python3
"""Module for evolved rectangle now including delmsg"""


class Rectangle:
    """class Rectangle with priv inst attrib width and height"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Method to get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """Method to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """Pub Inst Method to determine area of rect"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """Pub Inst Method to determine perimeter of rect"""
        if int(self.__width) == 0 or int(self.__height) == 0:
            return 0
        else:
            return (int(self.__width) * 2) + (int(self.__height) * 2)

    def __str__(self):
        """Builtin to return printed representation of string instance"""
        picture = ""
        for i in range(int(self.__height)):
            for i in range(int(self.__width)):
                if int(self.__height) == 0 or int(self.__width) == 0:
                    return picture
                picture += "#"
            picture += '\n'
        return picture[:-1]

    def __repr__(self):
        """Builtin to return string representation of string instance"""
        return "Rectangle({}, {})".format(eval(repr(self.__width)), (
               eval(repr(self.__height))))

    def __del__(self):
        """Builtin to ensure proper deletion of instance"""
        print("Bye rectangle...")
