#!/usr/bin/python3

""" Module for user class that contain all user in system"""
from models.base_model import BaseModel


class User (BaseModel):
    """User class contains user data"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
