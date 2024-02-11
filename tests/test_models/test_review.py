#!/usr/bin/python3
""" Review model testing """
from models.review import Review
import unittest


class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_default_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_set_values(self):
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "good place"
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "good place")
