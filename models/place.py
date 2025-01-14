#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, relationship
from sqlalchemy import Column, String, Integer, Float, Table


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True )
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete-orphan", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, backref="place_amenities")
    amenity_ids = []
        
