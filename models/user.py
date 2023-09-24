#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    first_name = Column(String(128))
    last_name = Column(String(128))
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
