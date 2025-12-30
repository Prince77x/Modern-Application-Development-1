
# 🎯 Objectives

- Reuse and extend layouts  
- Build a base template and create child pages from it  
- Share components like headers, footers, and navbars  

---

# 📌 Core Topics

## 1️⃣ `{% block %}` and `{% endblock %}`
Used to define editable sections in a base template.
{% block content %}
{% endblock %}

text

## 2️⃣ `{% extends %}`
Used by child templates to inherit from a base layout.
{% extends "base.html" %}

text

## 3️⃣ `{% include %}`
Include reusable template parts (header, footer, navbar).
{% include "header.html" %}

text

## 4️⃣ `{% import %}`
Import macros or reusable functions.
{% import "macros.html" as tools %}
{{ tools.button("Save") }}

text

## 5️⃣ `super()`
Call parent block content inside a child block.
{% block content %}
{{ super() }}

<p>This is extra content added by the child.</p> {% endblock %} ```
🏗️ Basic Example Structure
📁 Folder Setup
text
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
🔹 base.html
text
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>

{% include "header.html" %}

{% block content %}{% endblock %}

</body>
</html>
🔹 header.html
text
<h1>Welcome to the Website!</h1>
<hr>
🔹 home.html
text
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<p>This is Home Page Content.</p>
{% endblock %}
🔹 about.html
text
{% extends "base.html" %}

{% block title %}About Us{% endblock %}

{% block content %}
{{ super() }}
<p>More info about our mission.</p>
{% endblock %}
text

***