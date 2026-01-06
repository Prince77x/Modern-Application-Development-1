from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base,student

engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)  # Create tables if they don't exist
sessionLocal = sessionmaker(bind=engine)
session = sessionLocal()

# Update a student's name
prince = session.query(student).filter_by(name="Prince").first()
if prince:
    prince.name = "Prince Rawat"
    session.commit()
    print("Student updated successfully")

# Query and print all students
students = session.query(student).all()
for stu in students:
    print(f"ID: {stu.id}, Name: {stu.name}, Roll No: {stu.roll_no}")
