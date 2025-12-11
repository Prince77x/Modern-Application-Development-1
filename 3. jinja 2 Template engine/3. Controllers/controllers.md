# 🧩 Jinja2 Control Structures and Template Inheritance

## 1️⃣ If / Else Conditions

### Syntax
```
{% if condition %}
    ...
{% elif condition %}
    ...
{% else %}
    ...
{% endif %}
```

### Example
**Python:**
```
age = 20
```

**Template:**
```
{% if age >= 18%}
    You are an adult.
{% else %}
    You are a minor.
{% endif %}
```

**Output:**
```
You are an adult.
```

---

## 2️⃣ For Loops

### Basic Loop
```
{% for item in list %}
    {{ item }}
{% endfor %}
```

### Example
**Python:**
```
fruits = ["apple", "banana", "mango"]
```

**Template:**
```
{% for f in fruits %}
- {{ f }}
{% endfor %}
```

**Output:**
```
- apple
- banana
- mango
```

---

## 3️⃣ Loop Variables (Super Useful)

Inside a loop, Jinja2 provides **special loop variables**:

| Variable      | Meaning               |
|----------------|------------------------|
| `loop.index`   | 1-based index          |
| `loop.index0`  | 0-based index          |
| `loop.first`   | True for first item    |
| `loop.last`    | True for last item     |
| `loop.length`  | Total number of items  |

### Example
```
{% for student in students %}
{{ loop.index }}. {{ student }}
{% endfor %}
```

**Output:**
```
1. Prince
2. Rahul
3. Arjun
```

---

## 4️⃣ Loop Over Dictionary

**Python:**
```
student = {"name": "Prince", "age": 20, "city": "Bihar"}
```

**Template:**
```
{% for key, value in student.items() %}
{{ key }} → {{ value }}
{% endfor %}
```

---

## 5️⃣ Using if inside for loop

```
{% for mark in marks %}
    {% if mark >= 35%}
        Pass: {{ mark }}
    {% else %}
        Fail: {{ mark }}
    {% endif %}
{% endfor %}
```

---

## 6️⃣ Range Loop (like Python)

```
{% for i in range(1, 6) %}
    Number: {{ i }}
{% endfor %}
```

---

## 7️⃣ Filter Items Inside Loop

```
{% for f in fruits if f != "banana" %}
    {{ f }}
{% endfor %}
```

**Output:**
```
apple
mango
```

---

## 8️⃣ Set Variable in Template

You can create or update variables using:
```
{% set total = price * quantity %}
Total Amount: {{ total }}
```

---

## 9️⃣ Macros (Functions in Templates)

Macros allow creating **reusable blocks** of code.

```
{% macro greet(name) %}
    Hello {{ name }}!
{% endmacro %}

{{ greet("Prince") }}
```

---

## 🔟 Include Other Templates

You can include another template file:

```
{% include "header.html" %}
<h1>Home Page</h1>
{% include "footer.html" %}
```

---

## 1️⃣1️⃣ Extends + Blocks (Template Inheritance)

Used in **Flask web development** for layout reuse.

**base.html**
```
<html>
<body>
{% block content %}{% endblock %}
</body>
</html>
```

**home.html**
```
{% extends "base.html" %}

{% block content %}
<h1>Welcome Prince</h1>
{% endblock %}
```

---

## 💡 Module 3 Summary Table

| Feature | Syntax | Purpose |
|-----------|----------|-----------|
| If | `{% if %}` | Conditional rendering |
| For | `{% for %}` | Looping over data |
| Loop vars | `loop.index`, `loop.first`, etc. | Access loop metadata |
| Set | `{% set x = ... %}` | Create or override variables |
| Include | `{% include %}` | Import a template |
| Extends | `{% extends %}` | Template inheritance |
| Macros | `{% macro %}` | Create reusable template functions |

---

✅ **Quick Recap**
- Use `{% if %}` and `{% for %}` for logic and iteration.  
- Leverage `loop` variables for indexing and control.  
- Use `{% set %}` for temporary variables.  
- Use `{% include %}` and `{% extends %}` to build reusable templates.  
- Macros help write DRY (Don’t Repeat Yourself) template code.
```

