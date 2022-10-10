#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Describes the amenities present"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
