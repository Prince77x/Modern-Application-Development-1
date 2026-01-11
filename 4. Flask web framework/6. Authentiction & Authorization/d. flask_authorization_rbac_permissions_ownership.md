# 🔐 Flask Authorization – RBAC, Permission-Based & Ownership-Based (Complete Guide)

This document explains **Role-Based Access Control (RBAC)**, **Permission-Based Authorization**, and **Ownership-Based Authorization** in a clear, practical, and EPMS-focused way.

---

## 📌 Big Picture

Modern secure systems use **4 layers**:

1. **Authentication** – Who are you?
2. **Role-Based Access** – What is your position?
3. **Permission-Based Access** – What actions can you do?
4. **Ownership-Based Access** – Is this resource yours?

All four together = **real production security**.

---

# 🧩 PART 1 – Role-Based Access Control (RBAC)

## 1️⃣ What is RBAC?

> **Role-Based Access Control means access to features is decided based on the role of the user.**

You don’t check *who* the person is, you check *what role* they have.

### Real-Life Example

| Person | Role | What they can do |
|--------|------|------------------|
| HR Head | Admin | Everything |
| Team Lead | Manager | Manage team |
| Developer | Employee | Work on tasks |

You don’t ask: *Is this Rahul?*
You ask: *Is this an Admin, Manager, or Employee?*

That is RBAC.

---

## 2️⃣ Why Do We Need RBAC?

Because in real applications:
- Not everyone should see everything
- Not everyone should modify everything
- It gives **security + organization + clarity**

### EPMS Example

| Role | Access |
|------|--------|
| Admin | Create/delete employees, full control |
| Manager | Assign projects, view team |
| Employee | View own tasks, update profile |

Without RBAC → **Chaos ❌**
With RBAC → **Structured system ✅**

---

## 3️⃣ How RBAC Works Internally

Flow:

```
User logs in
    ↓
User role loaded into current_user
    ↓
current_user.role
    ↓
Role check in route
    ↓
Allow or Block
```

This is **server-side security** (real security).

---

## 4️⃣ Storing Role in Database

```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="user")
```

Example values:
- admin
- manager
- user

---

## 5️⃣ Role Check Inside Routes (Basic)

```python
@app.route("/admin")
@login_required
def admin_panel():
    if current_user.role != "admin":
        abort(403)
    return "Welcome Admin"
```

---

## 6️⃣ Professional Way – Custom Role Decorator

```python
from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(role_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if current_user.role != role_name:
                abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Usage

```python
@app.route("/manager")
@role_required("manager")
def manager_dashboard():
    return "Welcome Manager"
```

---

## 7️⃣ Role-Based Dashboard

```python
@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "admin":
        return render_template("admin_dashboard.html")
    elif current_user.role == "manager":
        return render_template("manager_dashboard.html")
    else:
        return render_template("user_dashboard.html")
```

---

## 8️⃣ EPMS Role Mapping

| Feature | Role |
|--------|------|
| Create employee | Admin |
| Delete employee | Admin |
| Assign project | Manager |
| View team | Manager |
| View own tasks | Employee |
| Edit own profile | Employee |

---

## 9️⃣ Common RBAC Mistakes

- ❌ Checking role only in frontend
- ❌ Hardcoding admin email
- ❌ Using `if user == "admin"`
- ❌ Not protecting routes

> **Frontend hides, Backend protects**

---

# 🧩 PART 2 – Permission-Based Authorization

## 1️⃣ Why Role Is Not Enough

Two users:
- Rahul → Manager
- Amit → Manager

Same role, but:
- Rahul can delete employee
- Amit cannot

👉 Same role, different power.

---

## 2️⃣ Definition

> **Permission-based authorization controls specific actions, not just positions.**

Role = position
Permission = power

---

## 3️⃣ EPMS Permission Mapping

| Action | Permission |
|--------|------------|
| Create employee | create_employee |
| Delete employee | delete_employee |
| Assign project | assign_project |
| Edit project | edit_project |
| View salary | view_salary |

---

## 4️⃣ Database Design

### Permission Table

```python
class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
```

### Role Table

```python
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
```

### Role–Permission Mapping

```python
role_permissions = db.Table(
    'role_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'))
)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    permissions = db.relationship('Permission', secondary=role_permissions, backref='roles')
```

---

## 5️⃣ Permission Check Logic

```python
if "create_employee" in [p.name for p in current_user.role.permissions]:
    allow
else:
    block
```

---

## 6️⃣ Permission Decorator

```python
from functools import wraps
from flask import abort
from flask_login import current_user

def permission_required(permission_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if not any(p.name == permission_name for p in current_user.role.permissions):
                abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Usage

```python
@app.route("/create-employee")
@permission_required("create_employee")
def create_employee():
    return "Employee Created"
```

---

## 7️⃣ Role vs Permission

| Role | Permission |
|------|------------|
| Big category | Specific action |
| Who you are | What you can do |
| Admin, Manager | create, delete, edit |

---

# 🧩 PART 3 – Ownership-Based Authorization

## 1️⃣ Definition

> **Ownership-based authorization ensures a user can only access or modify resources that belong to them.**

---

## 2️⃣ Real-Life Example

Instagram:
- You can edit **your profile**
- You cannot edit **someone else’s profile**

---

## 3️⃣ EPMS Ownership Mapping

| Resource | Owner |
|---------|------|
| Employee profile | The employee |
| Project | Assigned manager |
| Task | Assigned employee |

---

## 4️⃣ Why Role + Permission is Not Enough

Two users:
- Aman → Employee
- Rohan → Employee

Same role.

Without ownership check:
👉 Aman could edit Rohan’s profile 😱

So we need:

> **Role + Permission + Ownership**

---

## 5️⃣ Database Example

```python
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    projects = db.relationship('Project', backref='manager')
```

---

## 6️⃣ Ownership Check Logic

```python
if project.manager_id != current_user.id:
    abort(403)
```

---

## 7️⃣ Edit Project Example

```python
@app.route("/project/<int:id>/edit")
def edit_project(id):
    project = Project.query.get_or_404(id)

    if project.manager_id != current_user.id:
        abort(403)

    return render_template("edit_project.html", project=project)
```

---

## 8️⃣ Ownership + Permission (Best Practice)

```python
@app.route("/project/<int:id>/delete")
@permission_required("delete_project")
def delete_project(id):
    project = Project.query.get_or_404(id)

    if project.manager_id != current_user.id:
        abort(403)

    db.session.delete(project)
    db.session.commit()
    return "Deleted"
```

---

## 9️⃣ Ownership Decorator

```python
from functools import wraps
from flask import abort
from flask_login import current_user

def owner_required(model):
    def decorator(func):
        @wraps(func)
        def wrapper(id, *args, **kwargs):
            obj = model.query.get_or_404(id)
            if obj.user_id != current_user.id:
                abort(403)
            return func(id, *args, **kwargs)
        return wrapper
    return decorator
```

### Usage

```python
@app.route("/profile/<int:id>/edit")
@owner_required(User)
def edit_profile(id):
    return "Profile edit page"
```

---

## 10️⃣ EPMS Practical Scenarios

- **Employee profile** → `profile.user_id == current_user.id`
- **Task update** → `task.assigned_to_id == current_user.id`
- **Project update** → `project.manager_id == current_user.id`

---

## 11️⃣ Security Layers (Final Model)

```
Authentication  → Are you logged in?
Role            → Who are you?
Permission      → What can you do?
Ownership       → Is it yours?
```

All 4 together = **Real security**

---

## 12️⃣ Common Mistakes

- ❌ Only checking role
- ❌ Only checking permission
- ❌ Forgetting ownership
- ❌ Trusting frontend
- ❌ Using user_id from form

> Always use: `current_user.id`

---

## 13️⃣ Final Mental Model

```
User wants resource
        ↓
Check login
        ↓
Check role
        ↓
Check permission
        ↓
Check ownership
        ↓
Allow or Block
```

---

## 🚀 Why This Makes You Advanced

Most beginners stop at:
- Login
- Role

You now understand:
- Permission
- Ownership

👉 This is **industry-level backend design**.

---

## ✅ Conclusion

You now have a complete understanding of:
- RBAC
- Permission-based authorization
- Ownership-based authorization

This architecture is exactly what is used in:
- Company ERP systems
- Employee management portals
- Government dashboards
- Admin panels

---

**End of Document**

