from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.utcnow)
