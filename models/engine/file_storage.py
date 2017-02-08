#!/usr/bin/python3
import json


class FileStorage:
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.update(obj.id: None)

    def save(self):
       with open('basic.json', mode='w', encoding='utf-8') as fhandle:
            json.dump(self.__objects, fhandle)

    def reload(self):
        with open('basic.json', mode='r', encoding='utf-8') as fhandle:
            json.loads(self.__objects, fhandle)

    
        
