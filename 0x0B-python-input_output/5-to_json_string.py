#!/usr/bin/python3
"""Module for json format func"""
import json


def to_json_string(my_obj):
    """func to return json repr of an object str"""
    return json.dumps(my_obj)
