#!/usr/bin/python3
"""Module for another elaborated class Square"""


class Square:
    """class Square with private attributes size and position"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """module to get value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Module to set value of size"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif not isinstance(size, int):
                raise TypeError("size must be an integer")

    @property
    def position(self):
        """Module to get values for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Module to set values for position"""
        if isinstance(position, tuple) and position > 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method to determine area"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """Public instance method to print pattern of area square"""
        if self.__size == 0:
            print()
        else:
            if self.__position:
                for i in range(self.__position[1]):
                    print()
                for i in range(int(self.__size)):
                    for i in range(self.__position[0]):
                            print(" ", end="")
                    for i in range(int(self.__size)):
                        print("#", end="")
                    print()
