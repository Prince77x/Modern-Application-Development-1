from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class user(Base):
    __tablename__ = "USER"
    