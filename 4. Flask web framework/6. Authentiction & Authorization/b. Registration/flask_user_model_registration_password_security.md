# Flask Authentication System — User Model, Registration & Password Security
---

## 📌 Overview
This document covers the **core foundation of authentication systems in Flask**, including:

- User Model Design (very important)
- User Registration System
- Password Security

All examples use:
- **Flask**
- **SQLAlchemy**
- **Flask-Login**
- **Flask-WTF**
- **Werkzeug Security**

---

# 🧱 PART 1 — USER MODEL DESIGN (Very Important)

## 1. User Table Design
The **User table** is the heart of authentication. It stores:

- Identity info (username, email)
- Security info (password hash)
- Status info (active, blocked)
- Role info (admin, user)
- Timestamps

### Example User Model

```python
from flask_login import UserMixin
from datetime import datetime
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="user")  # admin, user, manager

    is_active = db.Column(db.Boolean, default=True)
    is_blocked = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return f"<User {self.username}>"
```

---

## 2. UserMixin (Flask-Login)

`UserMixin` provides ready-made authentication properties:

- `is_authenticated`
- `is_active`
- `is_anonymous`
- `get_id()`

```python
from flask_login import UserMixin

class User(db.Model, UserMixin):
    ...
```

> Without `UserMixin`, Flask-Login will not work properly.

---

## 3. Username vs Email Login

Allow login via username, email, or both.

```python
user = User.query.filter(
    (User.username == login_input) | (User.email == login_input)
).first()
```

---

## 4. Unique Constraints

```python
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
```

### Why?
- Prevent duplicate accounts
- Avoid login confusion
- Improve security

> Always enforce uniqueness at **database level**, even if you validate in forms.

---

## 5. User Status (active, blocked, suspended)

```python
is_active = db.Column(db.Boolean, default=True)
is_blocked = db.Column(db.Boolean, default=False)
```

### Usage

```python
if user.is_blocked:
    flash("Your account is blocked", "danger")
```

---

## 6. Roles Field (admin, user, manager)

```python
role = db.Column(db.String(20), default="user")
```

```python
if current_user.role == "admin":
    # allow admin access
```

---

## 7. Timestamps (created_at, last_login)

```python
created_at = db.Column(db.DateTime, default=datetime.utcnow)
last_login = db.Column(db.DateTime)
```

```python
user.last_login = datetime.utcnow()
db.session.commit()
```

---

# 🧩 PART 2 — MODULE 3: USER REGISTRATION SYSTEM

## 1. Signup Route Design

```python
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        ...
    return render_template("register.html", form=form)
```

---

## 2. Form Handling (POST/GET) — Flask-WTF

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
```

---

## 3. Input Validation

```python
validators=[DataRequired(), Email(), Length(min=6)]
```

> First layer of defense against invalid data.

---

## 4. Email/Username Uniqueness Check

```python
existing_user = User.query.filter_by(email=form.email.data).first()
if existing_user:
    flash("Email already registered", "danger")
    return redirect(url_for("register"))
```

---

## 5. Password Confirmation & Strength

```python
confirm_password = PasswordField("Confirm", validators=[EqualTo("password")])
```

---

## 6. Save User to Database

```python
from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash(form.password.data)

user = User(
    username=form.username.data,
    email=form.email.data,
    password_hash=hashed_password
)

db.session.add(user)
db.session.commit()
```

---

## 7. Flash Messages & Redirect

```python
flash("Account created successfully!", "success")
return redirect(url_for("login"))
```

---

# 🧩 PART 3 — MODULE 4: PASSWORD SECURITY

## 1. Why Plain-Text Passwords Are Dangerous

```text
password = "mypassword123"
```

❌ Easily readable if DB is hacked
❌ Security violation
❌ Breaks user trust

---

## 2. Password Hashing & Salting

- **Hashing** → converts password to fixed-length random string
- **Salting** → adds randomness to prevent rainbow-table attacks

Werkzeug handles both automatically.

---

## 3. generate_password_hash()

```python
from werkzeug.security import generate_password_hash

hashed = generate_password_hash("mypassword123")
```

Stored value:

```text
pbkdf2:sha256:260000$...
```

---

## 4. check_password_hash()

```python
from werkzeug.security import check_password_hash

check_password_hash(user.password_hash, entered_password)
```

Returns:
- `True` → correct password
- `False` → wrong password

---

## 5. Login Example (Full Flow)

```python
from datetime import datetime
from flask_login import login_user
from werkzeug.security import check_password_hash

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            user.last_login = datetime.utcnow()
            db.session.commit()
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html", form=form)
```

---

## 6. Password Policy Enforcement

```python
from wtforms.validators import Regexp

validators=[
    DataRequired(),
    Length(min=8),
    Regexp(r'^(?=.*[A-Z])(?=.*\\d).+$', message="Must contain 1 capital & 1 number")
]
```

---

# 🔥 Big Picture Flow

```text
User enters password
        ↓
generate_password_hash()
        ↓
Store hash in DB
        ↓
On login:
check_password_hash()
        ↓
Allow or deny access
```

---

# 🎯 Final Mental Model

| Concept | Purpose |
|--------|--------|
| User Model | Represents identity |
| UserMixin | Flask-Login compatibility |
| Unique Fields | Prevent duplicates |
| Roles | Authorization |
| Status Fields | Access control |
| Hashing | Security |
| Flask-WTF | Validation |
| Flash Messages | UX feedback |

---
