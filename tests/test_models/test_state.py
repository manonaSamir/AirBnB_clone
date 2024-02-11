#!/usr/bin/python3
""" User model testing """
from models.state import State
import unittest


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""
    def setUp(self):
        self.state = State()

    def test_default_value(self):
        self.assertEqual(self.state.name, "")

    def test_set_value(self):
        self.state.name = "Egypt"
        self.assertEqual(self.state.name, "Egypt")
