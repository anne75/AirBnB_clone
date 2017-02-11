#!/usr/bin/python3
# fix the import error
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Creates a class Review
    """
    place_id = ""
    user_id = ""
    text = ""
