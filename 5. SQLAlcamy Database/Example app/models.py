import email
from app import db

class Teacher(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subject_expert = db.Column(db.string(100),nullable = False)



class Student(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subject_learning = db.Column(db.string(100),nullable = False)
    
