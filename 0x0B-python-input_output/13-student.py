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
        if type(attrs) == list:
            if all(isinstance(value, attrs) for value in attrs):
                new_dict = {}
                for value in attrs:
                    if value in list(self.__dict__.key()):
                        new_dict[value] = self.__dict__[value]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Pub Method to replace all attrib of Student"""
        if "first_name" in (json.keys()):
            self.first_name = json.get("first_name")
        if "last_name" in (json.keys()):
            self.last_name = json.get("last_name")
        if "age" in (json.keys()):
            self.age = json.get("age")
