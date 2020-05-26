#!/usr/bin/python3
"""prevents the user from dynamically
creating new instance attributes"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
           firs_name
    """

    __slots__ = ["first_name"]
