#!/usr/bin/python3
"""Module for rectangle class"""


class Rectangle:
    """class rectangle with priv inst attrib width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """Method to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif isinstance(value, int):
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
            raise TypeError("width must be an integer")
        elif isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """Pub Method to determine area of rect"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """Pub method to determine perimeter of rect"""
        if int(self__width) == 0 or int(self.__height) == 0:
            return 0
        else:
            return (int(self.__width) * 2) + (int(self.__height) * 2)

    def __str__(self):
        """Builtin to print representation of string instance"""
        picture = ""
        for i in range(int(self.__height)):
            for i in range(int(self.__width)):
                if int(self.__height) == 0 or int(self.__width) == 0:
                    return picture
                picture += int(self.print_symbol)
            picture += '\n'
        return picture

    def __repr__(self):
        """Builtin to return representation of string instance"""
        return "Rectangle({}, {})".format(eval(repr(self.__width)), (
               eval(repr(self.__height))))

    def __del__(self):
        """Builtin to ensure proper deletion of an instance"""
        self.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static metho to return bigger instance"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if isinstance((rect_1, rect_2), Rectangle):
            if self.area(rect_1) == self.area(rect_2):
                return self.rect_1
            elif self.area(rect_1) < self.area(rect_2):
                return self.rect_2
            else:
                return self.rect_1
