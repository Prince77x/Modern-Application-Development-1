# 🧠 What is a Session in SQLAlchemy?

---

## 📘 Definition

A **Session** represents a **workspace** for talking to the database:
- You **attach objects** to it  
- It **tracks** new/changed/deleted rows  
- You decide when to **commit** or **rollback**  

**Technically:** A Session is a high-level wrapper around a database connection and transaction, created from `sessionmaker(bind=engine)`. [web:1]

📌 **Rule:** Create **one Session per unit of work** (CLI command, HTTP request), use it, then close it.

---

## 🛠 Creating and Using a Session

### Typical Pattern (ORM Style)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Create engine
engine = create_engine("sqlite:///example.db", echo=True)

# 2. Create session factory
SessionLocal = sessionmaker(bind=engine)

# 3. Create actual session
session = SessionLocal()
```

### Context Manager (Recommended for Bigger Apps)
```python
with Session(engine) as session:
    # Your CRUD operations here
    pass  # Auto-commits or auto-rollbacks
```

---

## 🧩 CRUD Operations with Session

**Assume this simple `User` model:**
```python
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

Base = DeclarativeBase()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```

---

### ➕ **Create (Add)**
```python
user = User(name="Rahul", email="rahul@example.com")
session.add(user)           # Add to session (not saved yet)
# session.add_all([user1, user2])  # Multiple objects
session.commit()            # Saves to database
```

**Before `commit()`:** User exists only in memory.  
**After `commit()`:** Row appears in `users` table.

---

### 🔍 **Read (Query)**
```python
# All users
users = session.query(User).all()

# Filter by exact match
rahul = session.query(User).filter_by(name="Rahul").first()

# Results are User objects — access like Python attributes
print(rahul.email, rahul.id)
```

---

### 🔄 **Update**
```python
# Load, modify, commit
user = session.query(User).filter_by(id=1).first()
user.email = "new_email@example.com"
session.commit()  # Generates UPDATE SQL automatically
```

**How it works:** Session detects "dirty" objects and generates the right `UPDATE` statement.

---

### 🗑️ **Delete**
```python
user = session.query(User).filter_by(id=1).first()
session.delete(user)
session.commit()  # Row removed from database
```

**Note:** Python object still exists, but has no database backing after delete.

---

## ✅ Commit vs Rollback

### 🔒 **Commit**
```python
session.commit()
```
- Ends current transaction  
- **Permanently saves** all pending changes  
- SQLAlchemy flushes `INSERT/UPDATE/DELETE`, then database `COMMIT`

### ↩️ **Rollback**
```python
session.rollback()
```
- **Undoes** all uncommitted changes  
- Used when errors occur (validation, exceptions)

---

### 🛡️ **Safe Pattern (Always Use This)**
```python
session = SessionLocal()
try:
    # Your CRUD operations
    session.commit()
except Exception:
    session.rollback()
    raise  # Re-raise the exception
finally:
    session.close()
```

---

## 🛠 Mini Project: CLI User Management

**Complete system combining all CRUD operations:**

### 1️⃣ **Add User**
```python
name = input("Name: ")
email = input("Email: ")
user = User(name=name, email=email)
session.add(user)
session.commit()
print("User added!")
```

### 2️⃣ **View Users**
```python
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
```

### 3️⃣ **Delete User**
```python
user_id = int(input("User ID to delete: "))
user = session.query(User).get(user_id)
if user:
    session.delete(user)
    session.commit()
    print("User deleted!")
else:
    print("User not found")
```

---

## 🧠 Key Takeaways

| Concept | Purpose |
|---------|---------|
| **Session** | Workspace for database operations |
| **session.add()** | Stages object for INSERT |
| **session.query()** | Fetches objects from DB |
| **session.commit()** | Saves all changes permanently |
| **session.rollback()** | Undoes all changes |
| **One Session per request** | Clean separation of work units |

---

💡 **Pro Tip:**  
Always use the **try/except/finally** pattern with sessions — it prevents database corruption and connection leaks in production apps.
