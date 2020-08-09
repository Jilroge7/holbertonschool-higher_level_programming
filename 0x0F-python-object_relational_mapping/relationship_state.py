#!/usr/bin/python3
""" Module for state class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import State
from relationship_city import City


Base = declarative_base()


class State(Base):
    """ State Class inherits from Base """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City")
