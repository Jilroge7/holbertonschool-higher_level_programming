#!/usr/bin/python3
"""Base class 1.0"""
import json


class Base():
    """class Base of all classes in project 0x0c"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to convert to json str repr"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """return list repr of json str"""
        if json_string is not None:
            return json.loads(json_string)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """cls method to save json str to file"""
        with open('{}.json.'.format(cls), mode='w', encoding='UTF8') as a_file:
            if list_objs:
                json_list = Base.to_json_string([list_objs])
            else:
                json_list = []
            a_file.write(json.dumps(json_list))
