# 🎯 Module 2 — SQLAlchemy Core Basics (Engine & Connection)

---

## 📘 Objective

Learn how to:
- Install SQLAlchemy  
- Connect Python to a database  
- Understand **Engine** and **Connection**  
- Execute basic SQL safely  

⚠️ ORM is **not used yet** — this module builds the **foundation** for ORM.

---

## 1️⃣ Installing SQLAlchemy

**SQLAlchemy** is a Python library that allows Python programs to interact with databases.

### 📦 Installation Command
```bash
pip install sqlalchemy
```

### 💡 What This Does
- Makes SQLAlchemy available in Python  
- Provides key tools like `create_engine`, `Table`, `Session`  

📌 Installing SQLAlchemy does *not* connect to any database by itself.

---

## 2️⃣ Choosing the Database (SQLite)

### Why SQLite?
- No server required  
- Database stored as a single `.db` file  
- Beginner‑friendly and lightweight  
- Natively supported by SQLAlchemy  

**SQLite Database File:** `example.db`  
- Automatically created if it doesn’t exist  
- Stores all tables and data locally  

---

## 3️⃣ Engine — The Most Important Concept

### 🔍 What Is an Engine?

An **Engine** is the **main entry point** between Python and the database.  

It:
- Knows *which database* to use  
- Knows *how to connect*  
- Manages database connections  
- Sends SQL statements to the database  

📌 Without an engine, SQLAlchemy cannot work.

### Creating an Engine
```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db")
```

---

## 4️⃣ Understanding the Database URL

```text
sqlite:///example.db
```

| Part | Meaning |
|-------|---------|
| **sqlite** | Database type (dialect) |
| **:///** | Indicates a local file |
| **example.db** | Database file name |

### Variations
```text
sqlite:///example.db        # Relative path  
sqlite:////full/path/db.db  # Absolute path  
sqlite:///:memory:          # In‑memory temporary database
```

---

## 5️⃣ What Happens When Engine Is Created?

When this line runs:
```python
engine = create_engine("sqlite:///example.db")
```

SQLAlchemy does the following:
1. Reads the database type (SQLite)  
2. Prepares connection rules  
3. **Does not connect immediately**  
4. Connects only when a query is executed  

📌 This is called a **lazy connection**.

---

## 6️⃣ Connection — Executing SQL

### 🔹 What Is a Connection?
A connection is used to **execute SQL queries**.  
It comes from the engine.

```python
connection = engine.connect()
```

---

### 📋 Creating a Table
```python
connection.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")
```

---

### ➕ Inserting Data
```python
connection.execute("""
INSERT INTO users (name, email)
VALUES ('Rahul', 'rahul@gmail.com')
""")
```

---

### 🔍 Reading Data
```python
result = connection.execute("SELECT * FROM users")

for row in result:
    print(row)
```

---

### ❌ Closing the Connection
```python
connection.close()
```

📌 Always close connections to free resources and prevent locks.

---

## 7️⃣ Transactions (Commit & Rollback)

### Why Transactions?
They ensure:
- Data consistency  
- Safety on errors  

If something fails → **rollback**  
If everything works → **commit**

---

### ✅ Best Practice
Use `engine.begin()` context manager:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db")

with engine.begin() as connection:
    connection.execute("""
    INSERT INTO users (name, email)
    VALUES ('Amit', 'amit@gmail.com')
    """)
```

✔ Automatically commits on success  
✔ Automatically rolls back on error  

---

## 8️⃣ Important Clarifications

- This module uses **SQLAlchemy Core** (not ORM).  
- The goal is to understand how ORM simplifies these tasks later.  

---

## 🔁 Typical Flow in Module 2

```
Install SQLAlchemy
       ↓
Create Engine
       ↓
Get Connection
       ↓
Execute SQL
       ↓
Close Connection
```

---

## 🧠 Key Takeaways (Must Remember)

| Concept | Description |
|----------|--------------|
| **Installing SQLAlchemy** | Only installs the library — not a real connection |
| **Engine** | Core component managing database connections |
| **Connection** | Used to run SQL queries |
| **Transactions** | Protect data from partial commits |
| **SQLite** | Best database for learning and practice |

---

💡 **Pro Tip:**  
Always use context managers (`with engine.begin()`) for safe and automatic transaction handling in SQLAlchemy Core.
