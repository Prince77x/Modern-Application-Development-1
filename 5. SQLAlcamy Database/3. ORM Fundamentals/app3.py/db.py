from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column ,String , Integer, VARCHAR

class Base(DeclarativeBase):
    pass

class user(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key = True)
    name = Column(String)
    email = Column(String)


class student(Base):
    __tablename__ = "Students"
    id = Column(Integer,primary_key= True)
    name = Column(String)
    roll_no = Column(Integer)
