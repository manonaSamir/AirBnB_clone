#!/usr/bin/python3
""" User model testing """
from models.place import Place
import unittest


class PlaceTest(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_default_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_set_values(self):
        self.place.city_id = "1"
        self.place.user_id = "2"
        self.place.name = "Cozy Cabin"
        self.place.description = "A cabin"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = [1, 2, 3]
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.user_id, "2")
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.description, "A cabin")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, [1, 2, 3])
