import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('peoples.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

class People(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)
    height = Column(String(20))
    mass = Column(String(20))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(Date)
    gender = Column(String(10))
    name = Column(String(100))
    planet_id = Column(String(100), ForeignKey('planets.id'))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    name = Column(String)
    url = Column(String)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e