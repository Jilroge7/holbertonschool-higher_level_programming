#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module for class Rectangle"""


class Rectangle(BaseGeometry):
    """class Rectangle inherits BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)

    def area(self):
        """Pub Inst Method to determine area"""
        return int(self.width) * int(self.height)
