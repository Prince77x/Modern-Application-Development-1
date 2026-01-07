from sqlalchemy.orm import DeclarativeBase ,relationship
from sqlalchemy import Column, ForeignKey, String, Integer

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100))
    posts = relationship("Post", back_populates="user") 

    # relationship("Post") here post is a class name 2nd model 
    # and in backpopulate "user" is the attribute name of relationship in 2nd model 

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id")) # foreignKey is alway assigned in child model 
    user = relationship("User",back_populates="posts")
    comments = relationship("Comment" , back_populates="post")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key= True)
    post_id = Column(Integer,ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")