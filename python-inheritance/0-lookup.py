#!/usr/bin/python3
"""
Module that defines the lookup function which returns the list of
available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods we want to inspect.

    Returns:
        A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
