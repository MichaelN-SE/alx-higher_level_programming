#!/usr/bin/python3
"""Add new attribute to object"""


def add_attribute(obj, name, value):
    """add new attribute to object"""

    if hasattr(obj, "__dict__"):

        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
