#!/usr/bin/python3
import datetime
import uuid
import json


class BaseModel:

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """UPDATE CLASS PART"""
        return ("[{}] ({}) {}".format(self.__class__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_json(self):
        self.__dict__.update({"__class__": "BaseModel"})
        return self.__dict__
