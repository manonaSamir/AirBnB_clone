#!/usr/bin/python3
""" User model testing """
from models.user import User
import unittest



class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def setUp(self):
        self.user = User()

    def test_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_set_values(self):
        self.user.email = "example@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "example@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        
