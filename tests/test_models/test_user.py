#!/usr/bin/python3
""" User model testing """
from models.user import User
import unittest



class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        obj = User()
        self.assertTrue(len(obj.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)
