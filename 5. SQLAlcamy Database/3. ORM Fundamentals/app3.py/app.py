from sqlalchemy import create_engine
from db import Base

engine = create_engine('sqlite:///example.db')

Base.metadata.create_all(engine) # this will create all the tables in database that we have defined in db.py block 