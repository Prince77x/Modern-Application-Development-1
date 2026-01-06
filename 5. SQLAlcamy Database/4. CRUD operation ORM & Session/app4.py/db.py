from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): # this is the base class. of all the class
    pass


class student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,unique=True)
    name = Column(String(100))
    roll_no = Column(Integer)