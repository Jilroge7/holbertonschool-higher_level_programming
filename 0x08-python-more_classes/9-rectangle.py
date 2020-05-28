#!/usr/bin/python3
"""Module to set new instance of rect as square"""


class Rectangle:
    """class Rectangle of priv ins attrib width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        """Method to get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """Pub Inst Method to determine area of rect"""
        return int(self.width) * int(self.height)

    def perimeter(self):
        """Pub Inst Method to determine perimeter of rect"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (int(self.width) * 2) + (int(self.height) * 2)

    def __str__(self):
        """Builtin to print representation of string instance"""
        picture = ""
        for i in range(self.height):
            for i in range(self.width):
                if self.height == 0 or self.width == 0:
                    return picture
                picture += str(self.print_symbol)
            picture += '\n'
        return picture[:-1]

    def __repr__(self):
        """Builtin to return representation of string instance"""
        return "Rectangle({}, {})".format(eval(repr(self.width)), (
            eval(repr(self.height))))

    def __del__(self):
        """Builtin to return a printed message when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to determine which inst is bigger or equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_1.area()) == (rect_2.area()):
                return rect_1
            elif (rect_1.area()) > (rect_2.area()):
                return rect_1
            elif (rect_2.area()) > (rect_2.area()):
                return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new rectangle"""
        return cls(size, size)
