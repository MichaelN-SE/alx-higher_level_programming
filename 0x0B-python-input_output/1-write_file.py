#!/usr/bin/python3
""""Open file and write into it and if not present creates it"""


def write_file(filename="", text=""):
    """we use with to open file write and close it"""
    with open(filename,  'w' , encoding='utf-8') as f:
        f.write(text)
        return len(text)
