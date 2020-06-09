#!/usr/bin/python3
"""test Square class"""

import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Square_Tests(unittest.TestCase):
    """tests Square class"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)
