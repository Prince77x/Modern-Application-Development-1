# 🎨 Jinja2 Template Engine (Flask)

---

## 🔹 What is Jinja2?

**Jinja2** is the **template engine** used by Flask.

It allows you to:
- Write **HTML + Python‑like logic**
- Pass **data from Flask to HTML**
- Reuse layouts (**DRY principle**)

👉 **Flask + Jinja2 = Dynamic Web Pages**

---

## 🔹 Rendering HTML (`render_template`)

### Purpose
Sends an **HTML file** from Flask to the browser.

### Flask Code
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
```

📌 Flask **automatically looks** inside the `templates/` folder to find HTML files.

---

## 🔹 Template Folder Structure

```
project/
│── app.py
│── templates/
│   ├── index.html
│   ├── base.html
│   └── header.html
│── static/
│   ├── css/
│   └── js/
```

- `templates/` → All HTML files  
- `static/` → CSS, JS, and images  

---

## 🔹 Template Variables (`{{ }}`)

Used to **display dynamic values** in HTML.

**Flask:**
```python
@app.route("/")
def home():
    name = "Prince"
    return render_template("index.html", name=name)
```

**HTML:**
```html
<h1>Hello {{ name }}</h1>
```

✔ `{{ }}` → Outputs data  
❌ Cannot write logic inside `{{ }}`

---

## 🔹 Filters (Modify Data)

Filters **change how data is displayed**.

### Syntax
```jinja2
{{ variable | filter }}
```

### Common Filters

| Filter | Purpose |
|--------|----------|
| `upper` | Uppercase text |
| `lower` | Lowercase text |
| `title` | Capitalize each word |
| `length` | Count items |
| `safe` | Render HTML safely |

### Example
```html
<p>{{ name | upper }}</p>
<p>Total: {{ items | length }}</p>
```

---

## 🔹 Control Statements (`{% %}`)

Used for **logic**, not direct output.

---

## 🧪 Practice Concepts

### 🔹 if / else Statement
```jinja2
{% if age >= 18%}
    <p>Adult</p>
{% else %}
    <p>Minor</p>
{% endif %}
```

✔ Used for conditions  
✔ Syntax similar to Python  

---

### 🔹 for Loop
```jinja2
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

---

### 🔹 Loop Index — `loop` Object

| Attribute | Meaning |
|------------|----------|
| `loop.index` | Index starting at 1 |
| `loop.index0` | Index starting at 0 |
| `loop.first` | True for first iteration |
| `loop.last` | True for last iteration |

**Example:**
```jinja2
{% for item in items %}
    {{ loop.index }} - {{ item }}
{% endfor %}
```

---

### 🔹 Working with Lists

**Flask:**
```python
@app.route("/")
def home():
    subjects = ["Math", "Physics", "CS"]
    return render_template("index.html", subjects=subjects)
```

**HTML:**
```jinja2
{% for sub in subjects %}
    <p>{{ sub }}</p>
{% endfor %}
```

---

### 🔹 Working with Dictionaries

**Flask:**
```python
@app.route("/profile")
def profile():
    user = {"name": "Prince", "age": 20}
    return render_template("profile.html", user=user)
```

**HTML:**
```jinja2
<p>Name: {{ user.name }}</p>
<p>Age: {{ user.age }}</p>
```

---

### 🔹 Include Templates

Used to **reuse small components** like headers, navbars, or footers.

**Example:**
```jinja2
{% include "header.html" %}
```

✔ Common includes:
- Navbar  
- Footer  
- Sidebar  

---

## 🔹 Blocks & Template Inheritance

**Base Template (`base.html`):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**Child Template (`index.html`):**
```jinja2
{% extends "base.html" %}

{% block title %}
Home
{% endblock %}

{% block content %}
<h1>Welcome</h1>
{% endblock %}
```

✔ Avoids repetition  
✔ Creates professional, structured templates  

---

## ⚠️ Common Mistakes

❌ Using `{{ }}` for logic  
❌ Writing raw Python code inside templates  
❌ Forgetting `{% endfor %}` or `{% endif %}`  
❌ Placing HTML files **outside** `templates/`  

---

## 🎯 Practice Tasks (Must Do)

1️⃣ Pass a list of subjects and display them in HTML  
2️⃣ Show **“Pass / Fail”** using an `if` condition  
3️⃣ Display a list with its **loop index**  
4️⃣ Create a `base.html` and extend it in a child page  
5️⃣ Include a `footer.html` template at the end  

---

## ✅ Summary

| Concept | Meaning |
|----------|----------|
| Jinja2 | Flask’s template engine for dynamic HTML |
| `{{ }}` | Used for output |
| `{% %}` | Used for logic |
| Filters | Modify data before rendering |
| Loops & Conditions | Control display dynamically |
| Inheritance | Keeps templates clean and reusable |

---

💡 **In short:**  
Jinja2 turns plain HTML into **powerful, data‑driven templates**—making Flask web pages dynamic, efficient, and modular.
