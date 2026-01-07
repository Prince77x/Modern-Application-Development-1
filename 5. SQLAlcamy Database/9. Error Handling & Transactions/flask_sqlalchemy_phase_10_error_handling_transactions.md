# Phase 10 — Error Handling & Transactions (Flask + SQLAlchemy)
🎯 **Goal:** Make your application handle database errors gracefully without crashing.

---

## What You Will Learn

- Try/Except for DB errors  
- Rollbacks on failure  
- Handle integrity errors  
- Safe transaction commits  
- Build crash-proof applications

---

## 1️⃣ Why Error Handling is Necessary

Without error handling:

```python
db.session.add(user)
db.session.commit()
```

If:
- email is duplicate
- constraint fails
- database is locked

❌ App will crash  
❌ User sees 500 error

👉 **Never trust user input. Always protect DB operations.**

---

## 2️⃣ Try / Except for DB Errors

Basic pattern:

```python
try:
    db.session.add(user)
    db.session.commit()
except:
    db.session.rollback()
    return "Error occurred"
```

**Meaning:**
- `try` → attempt DB operation  
- `except` → handle error  
- `rollback()` → undo changes

---

## 3️⃣ Rollback on Failure (Critical Concept)

```python
db.session.rollback()
```

- Resets dirty session
- Keeps database consistent

---

## 4️⃣ Handling Integrity Errors (Duplicate / Null)

Common issue: **Duplicate email**

```python
from sqlalchemy.exc import IntegrityError
```

```python
try:
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
except IntegrityError:
    db.session.rollback()
    return "Email already exists"
```

---

## 5️⃣ Safe Transaction Commit (Professional Pattern)

```python
from sqlalchemy.exc import SQLAlchemyError

try:
    db.session.add(student)
    db.session.commit()
except SQLAlchemyError as e:
    db.session.rollback()
    print(e)
    return "Database error"
```

---

## 6️⃣ Full Example – Safe User Registration

```python
from sqlalchemy.exc import IntegrityError

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]

    try:
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return "User registered successfully"

    except IntegrityError:
        db.session.rollback()
        return "Email already exists"

    except Exception:
        db.session.rollback()
        return "Something went wrong"
```

---

## 7️⃣ What is a Transaction?

> **A transaction is a group of database operations treated as a single unit.**

Either:
- All succeed ✅  
- All fail ❌

---

## 8️⃣ Transaction Example

```python
try:
    db.session.add(user)
    db.session.add(profile)
    db.session.commit()
except:
    db.session.rollback()
```

👉 If profile fails → user is also not saved

---

## 9️⃣ Real Life Example — Bank Transfer

```text
Debit A
Credit B
Commit
```

If credit fails → debit must rollback

---

## 🔟 Important Rules (Memorize)

| Rule | Meaning |
|------|--------|
Always use try/except | Prevent crashes |
Always rollback on error | Reset session |
Never ignore exceptions | Debug safety |
Show user-friendly message | Better UX |
Log actual error | Debugging |

---

## 🔥 One-Line Memory Trick

> **Commit = Save, Rollback = Undo**

---

## Mini Practice Task

Create a safe delete route:

- If user exists → delete
- If not → show "User not found"
- If DB error → rollback + message

---
 