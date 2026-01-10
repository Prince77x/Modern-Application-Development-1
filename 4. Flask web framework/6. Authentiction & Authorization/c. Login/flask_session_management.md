# Session Management in Flask (Complete Guide)

## Overview
In this module, we will cover:

- What is a session
- How Flask session works
- Secure cookies
- HttpOnly cookies
- Session expiration
- Auto-logout on inactivity
- Session fixation protection

---

## 1️⃣ What is a Session? (Very Important)

### Simple Definition
A **session** is a way to remember a user across multiple requests.

### Why Needed?
- HTTP is **stateless**
- Server forgets everything after each request
- Session helps the server remember who you are

### Real-Life Example

> You log into a website →
> You open another page →
> You are still logged in.

👉 That is **session in action**.

Without session:
- You would need to login on every page ❌

---

## 2️⃣ How Flask Session Works

Flask uses **secure cookies** to store session data.

```python
from flask import session

session["user_id"] = user.id
```

Flask stores this inside a **signed cookie** in the browser.

### On Next Request

```python
user_id = session.get("user_id")
```

👉 Flask automatically:
- Reads cookie
- Verifies signature
- Gives you session data

### Real Application Usage

```python
@app.route("/login", methods=["POST"])
def login():
    session["user_id"] = user.id
    return redirect(url_for("dashboard"))
```

```python
@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        return "Welcome user"
    return redirect(url_for("login"))
```

👉 This is **manual session handling**.

> Flask-Login does this internally for you.

---

## 3️⃣ Secure Cookies (Very Important for Security)

Flask session cookies are:
- **Signed**
- **Tamper-proof**
- **Cannot be modified by user**

Controlled by:

```python
app.secret_key = "supersecretkey"
```

### Why Important?

If attacker changes cookie →
Flask detects →
Session becomes invalid.

👉 This prevents:
- Session hijacking
- Identity forging

---

## 4️⃣ HttpOnly Cookies

### What is HttpOnly?
It means:
- JavaScript cannot access the cookie

So this is safe from:
- XSS attacks
- Client-side stealing

### In Flask

```python
app.config["SESSION_COOKIE_HTTPONLY"] = True
```

(Default is already `True`)

### Real-Life Impact

If hacker injects JS:

```javascript
document.cookie
```

👉 It **cannot read session cookie**.

That is huge security protection.

---

## 5️⃣ Session Expiration

### Why Needed?
To:
- Auto logout inactive users
- Reduce risk if someone forgets to logout

### Flask Setting

```python
from datetime import timedelta

app.permanent_session_lifetime = timedelta(minutes=30)
```

Then:

```python
session.permanent = True
```

### Real Application Example

```python
@app.route("/login", methods=["POST"])
def login():
    session.permanent = True
    session["user_id"] = user.id
```

Now:
- After 30 minutes of inactivity
- User is auto logged out

👉 This is standard in **banking apps**.

---

## 6️⃣ Auto-Logout on Inactivity (Real Security Feature)

### Simple Approach

```python
@app.before_request
def check_activity():
    session.permanent = True
    session.modified = True
```

### Manual & Controlled Approach

```python
from datetime import datetime, timedelta

@app.before_request
def auto_logout():
    now = datetime.utcnow()
    last = session.get("last_activity")

    if last:
        if now - last > timedelta(minutes=10):
            session.clear()
            flash("Session expired. Please login again.")
            return redirect(url_for("login"))

    session["last_activity"] = now
```

### Real-Life Scenario

User logs in →
Leaves laptop open →
After 10 minutes →
Session expires → auto logout.

👉 Used in:
- Banking
- Admin panels
- Government portals

---

## 7️⃣ Session Fixation Protection (Advanced Security)

### What is Session Fixation?

**Attack scenario:**
- Attacker sets session id
- User logs in
- Attacker uses same session → gains access

### Protection in Flask

On login, clear and regenerate session:

```python
session.clear()
login_user(user)
```

### Real Application Example

```python
@app.route("/login", methods=["POST"])
def login():
    session.clear()   # 🔐 important
    login_user(user)
    return redirect(url_for("dashboard"))
```

👉 This ensures:
- Old session destroyed
- New secure session created

---

## 🧠 Very Important Understanding

Flask-Login internally:
- Uses Flask session
- Stores `user_id`
- Manages expiration
- Handles remember-me cookies

### Comparison

| You Do (Manual) | Flask-Login Does |
|----------------|------------------|
| `session["user_id"]` | `login_user(user)` |
| `session.clear()` | `logout_user()` |
| Session check | `login_required` |

👉 Flask-Login is a **layer on top of session**.

---

## 🔁 Real Application Flow (Session Perspective)

```
User logs in
   ↓
Session created
   ↓
Cookie stored in browser
   ↓
User makes request
   ↓
Flask reads cookie
   ↓
User identified
```

---