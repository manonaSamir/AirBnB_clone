#!/usr/bin/python3
""" User model testing """
from models.place import Place
import unittest


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""
    
    def setUp(self):
         self.amenity = Amenity()

    def test_default_value(self):
         self.assertEqual(self.amenity.name, "")

    def test_set_value(self):
         self.amenity.name = "Wifi"
         self.assertEqual(self.amenity.name, "Wifi")
         