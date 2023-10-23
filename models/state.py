#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import shlex
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            mdls = models.storage.all()
            first_list = []
            final_list = []
            for key in mdls:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    first_list.append(mdls[key])
            for elem in first_list:
                if (elem.state_id == self.id):
                    final_list.append(elem)
            return final_list
