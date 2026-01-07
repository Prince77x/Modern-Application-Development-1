# Phase 9 — Migrations with Flask-Migrate

🎯 **Goal:** Learn how to safely change database structure using migrations

---

## Why Migrations are Necessary

### Problem Scenario

You already have this table:

```python
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
```

Later, you modify the model:

```python
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)  # NEW COLUMN
```

If you run:

```python
db.create_all()
```

❌ The new column will **not** be added.

👉 **Reason:** `create_all()` only creates tables, it does not modify existing ones.

---

## What is Flask-Migrate?

> **Flask-Migrate is a tool that tracks model changes and applies them safely to the database.**

It uses **Alembic** internally.

### Simple Flow

```text
Model Change → Migration File → Database Update
```

---

## Installation

```bash
pip install flask-migrate
```

---

## Setup Flask-Migrate

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

---

## Initialize Migrations (One Time Only)

```bash
flask db init
```

Creates:

```text
migrations/
    versions/
    env.py
    script.py.mako
```

⚠️ **Do not delete this folder**

---

## Create Migration (After Model Change)

```bash
flask db migrate -m "add age column to student"
```

✔ Detects model changes  
✔ Creates migration file

---

## Apply Migration (Upgrade Database)

```bash
flask db upgrade
```

✔ Updates the database structure

---

## Downgrade (Rollback)

```bash
flask db downgrade
```

✔ Reverts last migration

---

## Safe Model Modification Example

### Original Model

```python
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    course = db.Column(db.String(50))
```

### Modified Model

```python
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    course = db.Column(db.String(50))
    age = db.Column(db.Integer)  # NEW COLUMN
```

### Migration Commands

```bash
flask db migrate -m "added age column"
flask db upgrade
```

---

## Mini Task — Add New Column Using Migration

### Step 1: Add column to model

```python
age = db.Column(db.Integer)
```

### Step 2: Generate migration

```bash
flask db migrate -m "add age column to student"
```

### Step 3: Apply migration

```bash
flask db upgrade
```

🎉 **Result:** Column added without data loss

---

## Important Flow to Remember

```text
Change Model
    ↓
flask db migrate
    ↓
flask db upgrade
    ↓
Database Updated
```

---

## Common Mistakes to Avoid

❌ Deleting database file  
❌ Re-running `db.create_all()`  
❌ Manually editing database structure

✔ Always use **Flask-Migrate** for schema changes

---

## Interview Tip

**Q:** Why do we use Flask-Migrate?  
**A:** To safely apply database schema changes without losing existing data.

---

## One-Line Memory Trick

> **Migrations = Version control for database**

---

 