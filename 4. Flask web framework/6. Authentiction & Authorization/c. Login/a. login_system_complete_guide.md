# 🧩 MODULE 5 — LOGIN SYSTEM (Complete Guide)

A complete, real‑world implementation guide for building a **secure login system** using **Flask, Flask‑Login, SQLAlchemy, and Flask‑WTF**.

---

## 🧠 Big Picture First (Understand This)

Every professional login system follows this exact flow:

```text
User submits form
        ↓
Validate form
        ↓
Get user from DB
        ↓
Check password hash
        ↓
Check blocked / locked
        ↓
login_user()
        ↓
Redirect
```

👉 **If you understand this flow, everything becomes easy.**

---

## 🧱 STEP 1 — Update User Model (Important)

Add these fields to your `User` model:

```python
login_attempts = db.Column(db.Integer, default=0)
is_locked = db.Column(db.Boolean, default=False)
```

### Full Model Snippet

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="user")
    is_active = db.Column(db.Boolean, default=True)
    login_attempts = db.Column(db.Integer, default=0)
    is_locked = db.Column(db.Boolean, default=False)
```

### 👉 Why?

| Field | Purpose |
|------|---------|
| `login_attempts` | Counts wrong password tries |
| `is_locked` | Blocks brute force attacks |

---

## 🧩 STEP 2 — Login Form (Flask‑WTF)

### `forms.py`

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
```

👉 This form handles validation and user input safely.

---

## 🧩 STEP 3 — Setup Flask‑Login

### `app.py`

```python
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
```

### User Loader (Mandatory)

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

👉 Flask‑Login uses this to load user from session.

---

## 🧩 STEP 4 — Login Route (Full Logic)

### `app.py`

```python
from werkzeug.security import check_password_hash
from flask_login import login_user

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # 1️⃣ If user not found
        if not user:
            flash("Invalid email or password", "danger")
            return redirect(url_for("login"))

        # 2️⃣ If account is locked
        if user.is_locked:
            flash("Account locked due to multiple failed attempts", "danger")
            return redirect(url_for("login"))

        # 3️⃣ Check password
        if check_password_hash(user.password_hash, form.password.data):

            # Reset attempts
            user.login_attempts = 0
            user.is_locked = False

            login_user(user, remember=form.remember.data)
            db.session.commit()

            flash("Login successful", "success")
            return redirect(url_for("dashboard"))

        else:
            # Wrong password
            user.login_attempts += 1

            if user.login_attempts >= 3:
                user.is_locked = True
                flash("Account locked after 3 failed attempts", "danger")
            else:
                flash("Invalid email or password", "danger")

            db.session.commit()
            return redirect(url_for("login"))

    return render_template("login.html", form=form)
```

---

## 🧠 Breakdown of Each Security Layer

### 1️⃣ Credential Verification

```python
check_password_hash(user.password_hash, form.password.data)
```

👉 Compares:
- stored hashed password
- entered plain password

Returns `True` or `False`.

---

### 2️⃣ Incorrect Login Handling

```python
if not user:
    flash("Invalid email or password", "danger")
```

❌ We **never say**: “Email not found”

👉 Why?
To prevent **user enumeration attacks**.

---

### 3️⃣ Flash Messages

```python
flash("Invalid email or password", "danger")
flash("Login successful", "success")
```

Used for:
- UX feedback
- clarity
- professional behavior

---

### 4️⃣ Login Attempt Tracking

```python
user.login_attempts += 1
```

Each wrong attempt → counter increases.

---

### 5️⃣ Account Lockout Logic

```python
if user.login_attempts >= 3:
    user.is_locked = True
```

Prevents:
- brute force attacks
- bots
- password guessing

---

### 6️⃣ Remember‑Me Checkbox

```python
login_user(user, remember=form.remember.data)
```

| If checked | User stays logged in after browser close |
| If not | User logs out when browser closes |

---

## 🧪 Real Example

| Attempt | Password | Result |
|--------|----------|--------|
| 1 | wrong | attempts = 1 |
| 2 | wrong | attempts = 2 |
| 3 | wrong | attempts = 3 → LOCKED |
| 4 | correct | ❌ still blocked |

👉 This is **real production security logic**.

---

## 🧠 Interview‑Level Understanding

### Why do we reset attempts on success?

```python
user.login_attempts = 0
```

Because:
- user proved identity
- no longer suspicious
- system trusts user again

---

## ✅ Final Summary

You now understand:
- **Real login flow**
- **Security layers**
- **Professional patterns**
- **How real companies implement login systems**

