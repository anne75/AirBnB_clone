#!/usr/bin/python3
"""
This is module base_model
This module defines one class
"""
from datetime import datetime
import uuid
import json
from models import storage


class BaseModel:
    """
    Defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Creates a BaseModel object
        Arguments:
            if any should be a dictionary containing following keys
            id: a string, unique user id
            created_at: a datetime object
            updated_at: a datetime object
        """
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime(*self.str_to_numbers(
                kwargs['created_at']))
            self.updated_at = datetime(*self.str_to_numbers(
                kwargs['updated_at']))
        elif args:
            if len(args) != 3:
                pass
            self.id = args[0]
            self.created_at = datetime(*self.str_to_numbers(args[1]))
            self.updated_at = datetime(*self.str_to_numbers(args[2]))
        else:
            setattr(self, 'id', str(uuid.uuid4()))
            setattr(self, 'created_at', datetime.now())
            storage.new(self)

    def str_to_numbers(self, s):
        """Prepares a string for datetime"""
        tmp = ''.join([o if o not in "T;:.,-_" else " " for o in s]).split()
        res = [int(i) for i in tmp]
        return res

    def __str__(self):
        """fancy printing"""
        return ("[{}] ({}) {}".format(
                            self.__class__.__name__, self.id, self.__dict__))

    def __setattr__(self, name, value):
        """
        Forbids update of instance variables

        Arguments:
        name: name
        value: value
        """
        if hasattr(self, name):
            return
        self.__dict__[name] = value

    def save(self):
        """Updates the object and saves it to file"""
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        """Prepares serialization"""
        self.__dict__.update({"__class__": self.__class__.__name__})
        return self.__dict__
