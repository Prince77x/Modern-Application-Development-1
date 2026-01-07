# 📘 SQLAlchemy Relationships — Complete Notable Notes
---
## 1️⃣ What is a Relationship?
- Relationship = logical connection between two tables

##### In real life:
- One User → many Posts
- One Post → many Comments
- One Student → many Courses
##### In DB:
- Relationship is created using Foreign Key
##### In ORM:
- Relationship is handled using relationship()
---

## 2️⃣ Foreign Key (FK) — The Foundation
Definition:
- Foreign Key is a column that references Primary Key of another table
##### Example:
```
user_id = Column(Integer, ForeignKey("users.id"))
```
##### Meaning:
- user_id stores the id of a user from users table.

## 3️⃣ Golden Rule of Foreign Key
- 🔥 Foreign Key ALWAYS goes in the CHILD table (the MANY side)
RelationshipFK goes in
User → Posts
Posts
Order → Items
Items
Teacher → Subjects
Subjects
4️⃣ Types of Relationships
1. One-to-One (1:1)
One record in A → One record in B
Example:
User → Profile
2. One-to-Many (1:M)
One record in A → Many records in B
Example:
User → Posts
Teacher → Students
3. Many-to-Many (M:M)
Many records in A ↔ Many records in B
Example:
Student ↔ Courses
User ↔ Groups
5️⃣ relationship() — The ORM Connector
Definition:
relationship() connects Python objects, not database columns
Important:
❗ It does NOT create any column in DB
Without relationship():
post.user_id   # works
post.user      # ❌ does not work

With relationship():
post.user      # ✅ gives User object
user.posts     # ✅ gives list of Post objects

6️⃣ back_populates — The Two-Way Link
Definition:
back_populates connects two relationship() definitions
It tells SQLAlchemy:
“These two sides belong to the same relationship.”
Example:
class User(Base):
    posts = relationship("Post", back_populates="user")

class Post(Base):
    user = relationship("User", back_populates="posts")

Meaning:
SideMeans
User.posts
user has many posts
Post.user
post belongs to user
7️⃣ Visual Representation
User ───────< Post
  posts         user

posts ↔ user connected via back_populates
8️⃣ One-to-Many — Full Pattern
Parent: User
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    posts = relationship("Post", back_populates="user")

Child: Post
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")

9️⃣ One-to-One Pattern
Same as one-to-many but with unique=True and uselist=False
class User(Base):
    profile = relationship("Profile", back_populates="user", uselist=False)

class Profile(Base):
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="profile")

10️⃣ Many-to-Many Pattern
Step 1: Association Table
student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id")),
    Column("course_id", ForeignKey("courses.id"))
)

Step 2: Student
class Student(Base):
    courses = relationship("Course", secondary=student_course, back_populates="students")

Step 3: Course
class Course(Base):
    students = relationship("Student", secondary=student_course, back_populates="courses")

11️⃣ Parent vs Child (VERY IMPORTANT)
RuleMeaning
Parent
The “one” side
Child
The “many” side
FK goes in
Child
relationship
On both sides
12️⃣ Join — Combining Tables
Definition:
Join = combine rows from two tables
Inner Join:
session.query(Post).join(User).all()

Join with filter:
session.query(Post).join(User).filter(User.name == "Prince").all()

Outer Join:
session.query(Post).outerjoin(User).all()

13️⃣ Lazy vs Eager Loading
Lazy (Default)
user = session.query(User).first()
user.posts   # loads later

📌 Two queries
Eager
from sqlalchemy.orm import joinedload
user = session.query(User).options(joinedload(User.posts)).first()

📌 One query
14️⃣ backref (Shortcut)
Instead of:
posts = relationship("Post", back_populates="user")
user = relationship("User", back_populates="posts")

You can do:
posts = relationship("Post", backref="user")

⚠️ But:
Use back_populates for clarity (best for beginners)
15️⃣ The 6-Step Relationship Checklist (Memorize)
Before writing relationship, ask:
Is it 1-1, 1-M, or M-M?
Who is parent?
Who is child?
Is FK in child?
Is relationship() on both sides?
Is back_populates used?
If yes → perfect design ✅
16️⃣ Common Mistakes (Avoid These)
MistakeWhy wrong
FK in parent
wrong logic
relationship only one side
incomplete
wrong table name in FK
runtime error
many-to-many without association table
invalid
17️⃣ Real World Example — Blog System
User ───────< Post ───────< Comment

User
class User(Base):
    posts = relationship("Post", back_populates="user")

Post
class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")

    comments = relationship("Comment", back_populates="post")

Comment
class Comment(Base):
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")

18️⃣ One Line to Remember Forever
ForeignKey connects tables.
relationship connects objects.
back_populates connects both sides.
19️⃣ Final Mental Model
DATABASE LAYER  →  ForeignKey
ORM LAYER       →  relationship()
TWO-WAY LINK    →  back_populates