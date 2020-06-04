#!/usr/bin/python3
"""Module for load from json"""
import json


def load_from_json_file(filename):
    """Func to create obj from a json file"""
    with open(filename) as a_file:
        filename = json.load(a_file)
    return filename
