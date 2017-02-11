#!/usr/bin/python3
# fix the import error
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Creates a class Place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenities = ""
