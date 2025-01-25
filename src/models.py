import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    planet_id= Column(Integer, ForeignKey('planet.id'))
    character_id= Column(Integer, ForeignKey('character.id'))
    user= relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planets= Column(Integer, ForeignKey('planet.id'))
    planet= relationship(Favorite)

class Charachter(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    charachters= Column(Integer, ForeignKey('character.id'))
    character= relationship(Favorite)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
