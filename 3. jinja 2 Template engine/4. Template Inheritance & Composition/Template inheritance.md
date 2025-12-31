# Template Inheritance & Composition
---
## 🎯 Objectives

- Reuse and extend layouts  
- Build a base template and create child pages from it  
- Share components like headers, footers, and navbars  

---

## 📌 Core Topics

### 1️⃣ `{% block %}` and `{% endblock %}`
Used to define editable sections in a base template.

```jinja2 
{% block content %}
{% endblock %}
```
---
### 2️⃣ `{% extends %}`
Used by child templates to inherit from a base layout.
```jinja2
{% extends "base.html" %}
```
---
### 3️⃣ `{% include %}`
Include reusable template parts (header, footer, navbar).
```jinja2
{% include "header.html" %}
```
---
### 4️⃣ `{% import %}`
Import macros or reusable functions.
```jinja2
{% import "macros.html" as tools %}
{{ tools.button("Save") }}
```
---
## 5️⃣ `super()`
Call parent block content inside a child block.
```jinja2
{% block content %}
{{ super() }}

<p>This is extra content added by the child.</p> {% endblock %}
```
---

🏗️ Basic Example Structure
📁 Folder Setup
```arduino
project/
│
├─ templates/
│   ├─ base.html
│   ├─ home.html
│   ├─ about.html
│   ├─ contact.html
│   └─ header.html
│
└─ app.py
```

#### 🔹 base.html
```html
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>

{% include "header.html" %}

{% block content %}{% endblock %}

</body>
</html>
```
#### 🔹 header.html
```html
<h1>Welcome to the Website!</h1>
<hr>
```
#### 🔹 home.html
```html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<p>This is Home Page Content.</p>
{% endblock %}
```
#### 🔹 about.html
```html
{% extends "base.html" %}

{% block title %}About Us{% endblock %}

{% block content %}
{{ super() }}
<p>More info about our mission.</p>
{% endblock %}
```
