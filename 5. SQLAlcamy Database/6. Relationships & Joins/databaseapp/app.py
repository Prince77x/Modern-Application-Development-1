from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)
sessionload = sessionmaker(bind=engine)
session = sessionload()

# now we can perform any query here 