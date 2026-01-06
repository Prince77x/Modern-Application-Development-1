# 🧠 ORM Fundamentals

---

## 🔑 Core Idea

> **ORM = Python classes pretending to be database tables.**  
> If you understand this line, everything else makes sense.

---

## 1️⃣ The Big Picture (Before Coding)

### Traditional SQL Thinking
- Table exists first  
- You write SQL queries to interact with it

### ORM Thinking
- Class exists first  
- ORM creates and manages the table for you  

📌 You no longer think in SQL — you think in **objects**.

---

## 2️⃣ Declarative Base (Why It Exists)

**Question:** Why can’t we just write a normal Python class?

```python
class User:
    pass
```

❌ Because SQLAlchemy needs:
- **Metadata** (table information)  
- **Column information**  
- **Mapping rules**  

### ✅ Solution → Declarative Base

The **Declarative Base** tells SQLAlchemy:  
> “This class represents a database table.”

**SQLAlchemy 2.x syntax:**
```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

📌 `Base` = Parent of all models (tables).

---

## 3️⃣ Class → Table Mapping (MOST IMPORTANT)

This is **not a regular Python class**:

```python
class User(Base):
    __tablename__ = "users"
```

| Python Code | Meaning |
|--------------|----------|
| `User` | Defines a table blueprint |
| `__tablename__` | Actual table name in DB |
| Inherits `Base` | Enables ORM mapping |

---

## 4️⃣ Columns (Attributes ≠ Normal Variables)

```python
id = Column(Integer, primary_key=True)
```

This is **not** a normal assignment like `id = 5`.  
Instead, it means:  
> “Create a column named **id** of type Integer.”

### How ORM Sees This
```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
```

➡ Internally, SQLAlchemy automatically generates:
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR
);
```

📌 You never write this SQL yourself — ORM does it for you.

---

## 5️⃣ Why Primary Key Is Mandatory

**ORM Rule:** Every table must have a **primary key**.

### Why?
- ORM tracks rows using the primary key  
- Updates and deletes depend on it  

❌ Without a primary key → ORM cannot manage rows properly.

---

## 6️⃣ Engine + Base.metadata (Create Tables)

### Engine → Knows *where* the database is:
```python
engine = create_engine("sqlite:///example.db")
```

### Create All Tables From Models:
```python
Base.metadata.create_all(engine)
```

📌 This does three things:
1. Reads your model classes  
2. Generates SQL for each table  
3. Executes it safely in the database  

---

## 7️⃣ Full Flow (Visual)

```
Python Class
    ↓
Declarative Base
    ↓
Metadata (Mapping)
    ↓
SQL Generated Automatically
    ↓
Database Table Created
```

---

## 8️⃣ Creating Objects (Preview of Next Phase)

```python
user = User(name="Prince", email="p@gmail.com")
```

📌 This is *just a Python object* — it’s not saved to the database until you use a **Session**.

(Session and Persistence are covered in the next module.)

---
# 🧠 Very Important Mapping (ORM ↔ SQL)

## SQLAlchemy Types vs SQL Types

| SQLAlchemy Type | SQL Type  |
|-----------------|-----------|
| `Integer`       | `INT`     |
| `String`        | `VARCHAR` |
| `Text`          | `TEXT`    |
| `Float`         | `FLOAT`   |
| `Numeric`       | `DECIMAL` |
| `Boolean`       | `BOOLEAN` |
| `Date`          | `DATE`    |
| `DateTime`      | `DATETIME`|
| `LargeBinary`   | `BLOB`    |
---

## 🧪 Practice Questions (Very Important)

---

### 🟢 Level 1 — Understanding

1️⃣ Why must ORM models inherit from `Base`?  
2️⃣ What does `__tablename__` do?  
3️⃣ Why is a primary key required?

---

### 🟡 Level 2 — Code Reading

```python
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
```

**Questions:**
- How many columns will the table have?  
- What is the table name?  
- Which column uniquely identifies a row?  

---

### 🟠 Level 3 — Write Your Own Models

**A) Student Table**
- id (primary key)  
- name  
- roll_number  

**B) Course Table**
- id (primary key)  
- title  
- duration  

---

### 🔴 Level 4 — Thinking Question

Why do you think ORM prefers this style:
```python
class User(Base):
```
instead of:
```python
User = Table(...)
```

*(Hint: Cleaner OOP syntax, easier maintenance)*

---

## 🧠 Golden Rule (Remember Forever)

> **ORM = Table is a Class 🟰 Row is an Object**

---

💡 **Summary:**  
ORM maps Python classes to database tables, makes columns into attributes, and saves objects as rows — offering a simple, Pythonic way to work with databases without ever writing SQL directly.
