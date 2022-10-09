"""This module defines the Database storage class"""
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine



HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')


class DBStorage:
    """Defines database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes an instance of DB storage
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                .format(HBNB_MYSQL_PWD, HBNB_MYSQL_USER, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                echo=True, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all the instances of class 'cls'. If cls is not specified
        then return all the instances of all the classes available
        """
        self.__session = Session(self.__engine)
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(Amenity).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(User).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
                obj = self.__session.query(cls)
        return {"{}.{}".format(type(elem).__name__, elem.id): elem for elem in obj}

    def new(self, obj):
        """ Adds a new object 'obj' to the current database session 
        """
        self.__session.add(obj)

    def save(self):
        """Commmits all the changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object 'obj' from the current database session
        """
        if obj:
            self.__session.delete(obj)

    reload(self):
        """Creates all the tables in the database
        """
        Base = declarative_base()
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()






        






