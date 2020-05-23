#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """adds 2 integers

    Args:
        a(int): The first parameter
        b(int): The second parameter

    Return:
         integer: the addition of a and b
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
