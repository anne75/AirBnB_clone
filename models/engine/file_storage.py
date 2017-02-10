#!/usr/bin/python3
import json
import datetime

"""json.JSONEncoder.default=lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else obj.__dict__)"""
class FileStorage:
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """self.__objects.update({str(obj.id): obj.to_json()})"""
        self.__objects[obj.id] = obj

    def save(self):
       with open(self.__file_path, mode='w', encoding='utf-8') as fhandle:
            json.dump(self.__objects, fhandle, default=lambda obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else obj.__dict__))

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as fhandle:
                self.__objects = json.load(fhandle)
        except FileNotFoundError:
            pass
    def mySerialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
