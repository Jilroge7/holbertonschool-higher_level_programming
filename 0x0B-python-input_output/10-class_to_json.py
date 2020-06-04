#!/usr/bin/python3
"""Module for class to json func"""
import json


def class_to_json(obj):
    """Func to return dict description for json object"""
    return obj.__dict__
