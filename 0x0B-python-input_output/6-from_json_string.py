#!/usr/bin/python3
"""Module to return obj repr by json string"""
import json


def from_json_string(my_str):
    """func to return obj repr by json str"""
    return json.loads(my_str)
