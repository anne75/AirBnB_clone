#!/usr/bin/python3
# fix the import error
from models.base_model import BaseModel


class City(BaseModel):
    """
    Creates a class City
    """
    state_id = ""
    name = ""
