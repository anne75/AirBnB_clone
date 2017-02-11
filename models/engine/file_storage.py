#!/usr/bin/python3
import json
import datetime
"""
This is module file_storage.
It defines one class
"""

# json.JSONEncoder.default=lambda self, obj: (obj.isoformat() if isinstance
# (obj, datetime.datetime) else obj.__dict__)"""


class FileStorage:
    """
    Serialize and deserialize objects in models to json
    """
    def __init__(self, filename="file.json", objects={}):
        """
        Creates a FileStorage instance

        Arguments:
            filename: path to file
            objects: empty dictionary, not required
        """
        # print("INIT OBJECT", objects)
        self.__file_path = filename
        self.__objects = objects
        # print("INIT FS", self.__objects)

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key obj.id"""
        # self.__objects.update({str(obj.id): obj.to_json()})
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
        # print(self.__objects)

    def save(self):
        """serializes __objects to file __file_path in json format"""
        with open(self.__file_path, mode='w', encoding='utf-8') as fhandle:
            json.dump(self.__objects, fhandle, default=lambda obj: (
                obj.isoformat() if isinstance(
                    obj, datetime.datetime) else obj.__dict__))

    def reload(self):
        """deserializes the json file __file_path to __objects"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as fhandle:
                self.__objects = json.load(fhandle)
                # json.load(self.__objects, fhandle.__dict__)
        except FileNotFoundError:
            pass

    def mySerialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
