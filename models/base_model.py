#!/usr/bin/python3
import datetime
import uuid
import json
import models

class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        if isinstance(args, dict):
            self.__dict__ = args
        else:
            models.storage.new(self)

    def __str__(self):
        """UPDATE CLASS PART"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def __setattr__(self, name, value):
        """
        Forbids update of instance variables
        """
        if name in self.__dict__:
            pass


    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_json(self):
        self.__dict__.update({"__class__": "BaseModel"})
        return self.__dict__
