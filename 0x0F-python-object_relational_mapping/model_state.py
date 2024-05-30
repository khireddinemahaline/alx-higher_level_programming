#!/usr/bin/python3
""" Start link class to table in database """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,  primary_key=True)
    name = Column(String(200), nullable=True)
