#!/usr/bin/python3
"""Define a Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Attribute:
              id:
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string representation"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Adding the class method that writes the JSON string representation
        to a file
        """
        new_lt = []
        filename = ("{}.json".format(cls.__name__))
        if list_objs is None:
            new_lt = []
        else:
            with open(filename, "w", encoding="utf-8") as f:
                for items in list_objs:
                    new_lt.append(cls.to_dictionary(items))
                return f.write(cls.to_json_string(new_lt))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        new_list = []
        if json_string is None:
            new_list = []
        else:
            new_list.append(json_string)
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy
