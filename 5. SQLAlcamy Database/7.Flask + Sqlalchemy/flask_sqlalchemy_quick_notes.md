# Flask + SQLAlchemy — Quick Notable Notes

A concise revision sheet for **Flask + SQLAlchemy integration**. Suitable for GitHub notes and quick recall.

---

## 1️⃣ Flask-SQLAlchemy Setup

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)
```

**Notable Points:**
- Connects Flask with SQLAlchemy
- `sqlite:///app.db` → creates local database file
- `db` becomes your main ORM object

---

## 2️⃣ `db.Model` (Base Class)

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
```

**Notable Points:**
- Every model must inherit from `db.Model`
- Each class = one table
- Each attribute = one column

---

## 3️⃣ Table Name (`__tablename__`)

```python
class User(db.Model):
    __tablename__ = "users"
```

**Notable Points:**
- Controls actual table name in DB
- Used in ForeignKey
- Best practice to always define it

---

## 4️⃣ Database Creation

```python
with app.app_context():
    db.create_all()
```

**Notable Points:**
- Creates tables in database
- Must be inside `app_context()`
- Reads model structure and generates tables

---

## 5️⃣ Using Models Inside Routes ⭐ (Core Concept)

```python
@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template("users.html", users=all_users)
```

**Notable Points:**
- Route = handles request
- Model = talks to database
- `User.query` = ORM query system
- This is real backend development

---

## 6️⃣ CREATE (Insert Data)

```python
user = User(name="Prince", email="p@gmail.com")
db.session.add(user)
db.session.commit()
```

**Notable Points:**
- `add()` → stage data
- `commit()` → save permanently
- Without commit, data is not stored

---

## 7️⃣ READ (Fetch Data)

```python
User.query.all()
User.query.get(1)
User.query.filter_by(name="Prince").first()
```

**Notable Points:**
- `.all()` → multiple rows
- `.get(id)` → by primary key
- `.first()` → first matching row

---

## 8️⃣ UPDATE

```python
user = User.query.get(1)
user.name = "Prince Rawat"
db.session.commit()
```

**Notable Points:**
- Fetch → modify → commit
- No separate update command
- ORM tracks changes automatically

---

## 9️⃣ DELETE

```python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```

**Notable Points:**
- `delete()` removes object
- `commit()` confirms deletion

---

## 🔟 `db.session` (Very Important)

**Meaning:**
> Temporary memory where changes are stored before saving to DB

**Flow:**
```text
Model Object → db.session → commit() → Database
```

---

## 1️⃣1️⃣ Relationships

```python
class Post(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
```

**Notable Points:**
- Connects two tables
- `users.id` → table name, not class name
- Used in One-to-Many, Many-to-Many

---

## 1️⃣2️⃣ ForeignKey

```python
db.ForeignKey("users.id")
```

**Notable Points:**
- Creates link between tables
- Enforces data integrity
- Always uses **table name**

---

## 1️⃣3️⃣ Templates + Data

```python
return render_template("users.html", users=users)
```

**Notable Points:**
- Sends DB data to HTML
- Jinja2 displays it
- Bridge between backend and frontend

---

## 1️⃣4️⃣ Mini Project Flow (Important)

```text
Form → Route → Model → Database → Route → Template → User
```

This is **full-stack flow**.

---

## 🔥 Ultra-Short Summary (Interview Ready)

- `db.Model` → base class for tables
- `__tablename__` → table name
- `db.session` → save changes
- `commit()` → final save
- `User.query` → fetch data
- Routes use models → real backend logic
- Models represent tables
- Templates show data

---