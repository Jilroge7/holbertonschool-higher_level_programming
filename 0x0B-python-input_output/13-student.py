#!/usr/bin/python3
"""Module for class Student 3.0"""


class Student():
    """class Student defines student here"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Pub Method to retrieve dict repr of instance"""
        if all(isinstance(value, attrs) for value in attrs):
            return self.__dict__
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Pub Method to replace all attrib of Student"""
