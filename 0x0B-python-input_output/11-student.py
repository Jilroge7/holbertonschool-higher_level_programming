#!/usr/bin/python3
"""Module for class Student"""


class Student():
    """class Student with three attrib"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Pub method to retrieve dict repr of student"""
        return self.__dict__
