from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    func,
)

from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)

def create_user(session, username, password):
    user = User(username=username, password_hash=bcrypt.hash(password))
    session.add(user)
