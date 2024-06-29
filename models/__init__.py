#!/usr/bin/python3
"""This module instantiates an object of
Storage: FileStorage and DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
