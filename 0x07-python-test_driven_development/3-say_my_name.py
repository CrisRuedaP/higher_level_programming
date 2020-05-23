#!/usr/bin/python3
"""function that prints strings."""


def say_my_name(first_name, last_name=""):
    """Prints My_name

    Args:
        first_name(str): The first parameter
        last_name(str): The second parameter (not necessary)

    Return:
         string: prints My_name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
