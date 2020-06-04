#!/usr/bin/python3
"""Module for class Student 2.0"""


class Student():
    """class Student defines student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Pub Method to retrieve dict repr of instance"""
        if type(attrs) == list:
            if all(isinstance(value, str) for value in attrs):
                new_dict = {}
                for value in attrs:
                    if value in list(self.__dict__.keys()):
                        new_dict[value] = self.__dict__[value]
            return new_dict
        else:
            return self.__dict__
