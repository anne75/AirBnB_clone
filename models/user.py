#!/usr/bin/python3
# fix the import error
from models.base_model import BaseModel


class User(BaseModel):
    """
    Creates a class for users
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
