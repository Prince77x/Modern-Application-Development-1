# 🔍 Querying Like a Pro — Advanced SQLAlchemy Queries

---

## 1️⃣ `filter()` vs `filter_by()` (Very Important Difference)

### 🔹 **`filter_by()`** → Simple, keyword style
```python
users = session.query(User).filter_by(name="Prince").all()
```

**Use when:**
- Only **exact equality** conditions  
- Simple, straightforward queries  

### 🔹 **`filter()`** → Powerful, expression style
```python
users = session.query(User).filter(User.name == "Prince").all()
```

**Use when:**
- Multiple conditions  
- `<`, `>`, `!=`, `LIKE`, etc.  

### 🧠 **Rule of Thumb**
| Method | When to Use |
|--------|-------------|
| `filter_by()` | Easy but **limited** |
| `filter()` | **Powerful** and flexible |

---

## 2️⃣ Query Conditions (`==`, `>`, `<`, `!=`, `>=`, `<=`)

**Assume this `User` model:**
```python
class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
```

### Examples
```python
# Equal
User.age == 20

# Greater than
User.age > 18

# Less than
User.age < 30

# Not equal
User.name != "Aman"

# Combined
users = session.query(User).filter(User.age > 18).all()
```

---

## 3️⃣ `and_` and `or_` (Multiple Conditions)

**Import first:**
```python
from sqlalchemy import and_, or_
```

### AND Condition
```python
users = session.query(User).filter(
    and_(User.age > 18, User.city == "Delhi")
).all()
```
**Means:** `age > 18 AND city = Delhi`

### OR Condition
```python
users = session.query(User).filter(
    or_(User.age < 18, User.city == "Patna")
).all()
```
**Means:** `age < 18 OR city = Patna`

### ✅ **Cleaner Way (Commas = AND)**
```python
users = session.query(User).filter(
    User.age > 18,
    User.city == "Delhi"
).all()
```

---

## 4️⃣ Searching (`LIKE` / `contains`)

```python
# Contains (LIKE %pri%)
users = session.query(User).filter(User.name.contains("pri")).all()

# Starts with
users = session.query(User).filter(User.name.startswith("P")).all()

# Ends with
users = session.query(User).filter(User.email.endswith("@gmail.com")).all()

# LIKE pattern
users = session.query(User).filter(User.name.like("%an%")).all()
```

---

## 5️⃣ Sorting (`ORDER BY`)

```python
# Ascending (A-Z, 1-9)
users = session.query(User).order_by(User.name).all()

# Descending (Z-A, 9-1)
from sqlalchemy import desc
users = session.query(User).order_by(desc(User.age)).all()
```

---

## 6️⃣ Pagination (`LIMIT` & `OFFSET`)

```python
# First 5 users
users = session.query(User).limit(5).all()

# Skip first 5, get next 5 (page 2)
users = session.query(User).offset(5).limit(5).all()
```

**Real-life pagination:**
- Page 1 → `offset(0).limit(10)`  
- Page 2 → `offset(10).limit(10)`  
- Page 3 → `offset(20).limit(10)`

---

## 7️⃣ Searching by Multiple Fields (Real-World)

```python
search = "prince"

users = session.query(User).filter(
    or_(
        User.name.contains(search),
        User.email.contains(search)
    )
).all()
```

---

## 8️⃣ Mini Task — Multi-Field Search Function

```python
def search_users(keyword):
    users = session.query(User).filter(
        or_(
            User.name.contains(keyword),
            User.email.contains(keyword),
            User.age == keyword  # If keyword is a number
        )
    ).all()

    for user in users:
        print(f"{user.id}: {user.name} ({user.email}) - Age: {user.age}")

# Usage
search_users("prince")
```

📌 **This is real-world search logic** used in web apps.

---

## 9️⃣ **Very Important: Query is LAZY**

```python
q = session.query(User)              # No DB call
q = q.filter(User.age > 18)          # Still no DB call  
users = q.all()                      # NOW database is hit
```

📌 **Query executes ONLY when:**
- `.all()`, `.first()`, `.one()`  
- You iterate over results  
- You access results in a list comprehension  

---

## 🔁 **10️⃣ Mental Model (Must Remember)**

```
session.query(User)
       ↓
    .filter()
       ↓
   .order_by()
       ↓
     .limit()
       ↓
      .all()  ← Database hit here!
```

---

## 🧠 **Super Important Rules**

| Rule | Explanation |
|------|-------------|
| **`filter()`** > `filter_by()` | More powerful for complex queries |
| **`and_`, `or_`** | For complex conditions |
| **`contains()`, `like()`** | For search functionality |
| **Always paginate** | Large datasets |
| **`.all()`, `.first()`** | Triggers database execution |

---

💡 **Pro Tip:**  
Chain methods like `filter().order_by().limit()` — they don't hit the database until `.all()` or iteration.
