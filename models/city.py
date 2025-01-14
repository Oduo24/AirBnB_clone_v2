#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    name = Column(String(128), nulable=False)
    places = relationship("Place", cascade="delete", backref="cities")
    
