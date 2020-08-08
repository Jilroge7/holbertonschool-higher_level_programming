#!/usr/bin/python3
""" Module for state class """
from sqlalchemy import create_engine, Metadata, Table
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

Class State(Base):
    """ State Class inherits from Base """
    __tablename__ ='states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
