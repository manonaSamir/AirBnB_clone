#!/usr/bin/python3
""" User model testing """
from models.city import City
import unittest


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def setUp(self):
        self.city = City()

    def test_default_values(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_set_values(self):
        self.city.state_id = "BurSaid"
        self.city.name = "Egypt"

        self.assertEqual(self.city.state_id, "BurSaid")
        self.assertEqual(self.city.name, "Egypt")
