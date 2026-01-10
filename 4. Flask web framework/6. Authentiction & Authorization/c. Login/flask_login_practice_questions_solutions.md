# Flask Login System – Practice Questions & Complete Solutions
---

## 🟢 Level 1 – Conceptual Questions

### **1. What is the difference between Authentication and Authorization?**

- **Authentication** → *Who are you?* (Login process)
- **Authorization** → *What are you allowed to do?* (Permissions)

**Example:**
- Logging into admin panel → Authentication
- Deleting a user → Authorization

---

### **2. Why can’t we rely only on cookies for login without sessions?**

Because cookies are:
- Stored on client side
- Can be modified or deleted
- Not fully secure

Sessions are:
- Server controlled
- Secure
- Trustworthy

👉 Cookies store data, sessions store **identity**.

---

### **3. What problem does session solve in HTTP?**

HTTP is **stateless**.

Without session:
- Server forgets user after each request

Session:
- Maintains user identity across requests

👉 Session gives **memory to HTTP**.

---

### **4. What is stored inside Flask session by default?**

Flask session stores **small key–value data**.

Example:
```python
session["user_id"] = 5
```

Stored inside a **signed secure cookie**.

---

### **5. Why should passwords never be stored in plain text?**

Because:
- Databases can be leaked
- Hackers get full access
- Users reuse passwords

Always use:
```python
generate_password_hash()
check_password_hash()
```

👉 Plain text password = **security disaster**.

---

## 🟡 Level 2 – Code Understanding

### **6. What does `session["user_id"] = user.id` do?**

It:
- Logs in the user
- Stores identity in session
- Enables user tracking

👉 This is the **actual login action**.

---

### **7. What happens if `secret_key` is not set?**

Flask will:
- Not allow sessions
- Throw runtime error

Because session signing requires `secret_key`.

---

### **8. Explain:**
```python
if "user_id" in session:
    return redirect(url_for("dashboard"))
```

It means:
- If user is logged in → go to dashboard
- Else → stay on login

👉 Authentication check.

---

### **9. Why do we write `session.clear()` before login?**

To:
- Destroy old session
- Prevent **session fixation attacks**

Security rule:
> Always clear session before login.

---

### **10. What is the role of `session.permanent = True`?**

It:
- Enables session expiration
- Uses `permanent_session_lifetime`

Without it:
- Session ends when browser closes

---

## 🟠 Level 3 – Practical Scenarios

### **11. User logs in, closes browser, opens again – logged in or not?**

| Setting | Result |
|--------|--------|
| `session.permanent = False` | ❌ Logged out |
| `session.permanent = True` | ✅ Still logged in |

---

### **12. What happens if two users share same browser & session not cleared?**

- Second user gets first user’s account
- Major security risk

👉 Always clear session on logout.

---

### **13. Why is auto logout important in banking apps?**

Because:
- Sensitive financial data
- Public/shared computers
- High security risk

👉 Auto logout is **mandatory**.

---

### **14. What security risk occurs if HttpOnly is disabled?**

JavaScript can access cookies:
```javascript
document.cookie
```

Hacker can steal session → account takeover.

---

### **15. Why is session fixation dangerous?**

Because:
- Attacker sets session ID
- User logs in
- Attacker hijacks session

👉 Without `session.clear()` → account compromise.

---

## 🔵 Level 4 – Implementation Tasks (Solved)

### **16. Login Route**
```python
@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(email=request.form["email"]).first()

    if user and check_password_hash(user.password_hash, request.form["password"]):
        session.clear()
        session["user_id"] = user.id
        session.permanent = True
        return redirect(url_for("dashboard"))

    flash("Invalid credentials")
    return redirect(url_for("login"))
```

---

### **17. Logout Route**
```python
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
```
---

### **18. Protect Profile Route**
```python
@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return "Profile Page"
```

---

### **19. Auto Logout After 5 Minutes**
```python
@app.before_request
def auto_logout():
    now = datetime.utcnow()
    last = session.get("last_activity")

    if last and now - last > timedelta(minutes=5):
        session.clear()
        return redirect(url_for("login"))

    session["last_activity"] = now
```

---

### **20. Session Fixation Protection**
```python
session.clear()
session["user_id"] = user.id
```

---

## 🔴 Level 5 – Real World / Interview Questions

### **21. Why is Flask-Login preferred in large apps?**

Because it:
- Handles sessions
- Manages cookies
- Protects routes
- Handles remember-me
- Reduces bugs

👉 Industry standard.

---

### **22. How to handle “Remember Me” securely?**

- Long-lived token
- Server validation
- Never store password in cookie ❌

---

### **23. What should be stored in session: user id or full object?**

Always:
```python
session["user_id"] = user.id
```

Never:
```python
session["user"] = user
```

Because:
- Session size limit
- Serialization issues
- Security

---

### **24. How to prevent session hijacking?**

- HTTPS
- HttpOnly
- Secure cookies
- Session regeneration
- Short expiry

---

### **25. If user changes password, what should happen to existing sessions?**

All sessions must be destroyed:
```python
session.clear()
```

Because:
- Old sessions may be compromised

---

## ⭐ Bonus – Question 26

### **26. Online Exam Portal – Secure Design**

#### Session Handling
- `session["user_id"]`
- `session["exam_id"]`

#### Timeout
- Auto logout after **2–5 minutes inactivity**

#### Security Steps
- Disable multiple logins
- IP binding
- Device fingerprinting
- No back button
- Force logout on tab close
- Strict session expiration

👉 Enterprise-level security design.
---