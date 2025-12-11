# 🧪 Jinja2 Practice Tasks (Must Do)

## ✅ Task 1 — If Condition

### Objective
Print:
- **"Adult"** if `age ≥ 18`
- **"Minor"** otherwise

### Example
**Python:**
```
age = 20
```

**Template:**
```
{% if age >= 18%}
Adult
{% else %}
Minor
{% endif %}
```

**Output:**
```
Adult
```

---

## ✅ Task 2 — For Loop

### Objective
Loop over a list of 5 friends and print numbered names using `loop.index`.

### Example
**Python:**
```
friends = ["Prince", "Rahul", "Amit", "Neha", "Sneha"]
```

**Template:**
```
{% for f in friends %}
{{ loop.index }}. {{ f }}
{% endfor %}
```

**Output:**
```
1. Prince
2. Rahul
3. Amit
4. Neha
5. Sneha
```

---

## ✅ Task 3 — Dictionary Loop

### Objective
Given:
```
profile = {"name": "Prince", "club": "Aryavarta Sangam", "region": "Mithila"}
```
Print:
```
key → value
```

### Template:
```
{% for key, value in profile.items() %}
{{ key }} → {{ value }}
{% endfor %}
```

**Output:**
```
name → Prince  
club → Aryavarta Sangam  
region → Mithila
```

---

## ✅ Task 4 — Include Templates

### Objective
Create reusable parts with **includes**.

**Files:**
```
header.html
footer.html
main.html
```

### Content
**header.html**
```
<header>
    <h1>Welcome to My Website</h1>
</header>
```

**footer.html**
```
<footer>
    <p>© 2025 My Website</p>
</footer>
```

**main.html**
```
{% include "header.html" %}
<main>
    <h2>Main Page</h2>
    <p>This is the main content area.</p>
</main>
{% include "footer.html" %}
```

---

## ✅ Task 5 — Bonus (Macro)

### Objective
Create a macro for reusable greetings.

```
{% macro greet(user) %}
Hello {{ user }}! Welcome to Jinja2.
{% endmacro %}

{{ greet("Prince") }}
```

**Output:**
```
Hello Prince! Welcome to Jinja2.
```

---

✅ **Tip:**  
These tasks help solidify your understanding of control structures, includes, and macros — all essential for mastering **Flask templating** and creating dynamic web pages.
```

Would you like me to add this **Practice Tasks section** at the end of your existing `jinja2_complete_notes.md` when I combine all the files?
