#!/usr/bin/python3
"""encoding of python object to json"""
import json


def to_json_string(my_obj):
    """json representation of an object"""

    return json.dumps(my_obj)
