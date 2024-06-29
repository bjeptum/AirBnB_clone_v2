#!/usr/bin/python3
""""
DBStorage Module
New storage engine
"""


import os
from os import getenv
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Class Definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage class"""
        # Environment variables
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        # Create engine and connect to db
        self.__engine = create_engine(f'mysql+mysqldb://{user}:'
                                      f'{password}@{host}/{database}',
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        # Drop all tables if env is test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create a scoped session factory
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))
