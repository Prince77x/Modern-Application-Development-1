# Template Inheritance & Composition
---
## 🎯 Objectives

- Reuse and extend layouts  
- Build a base template and create child pages from it  
- Share components like headers, footers, and navbars  
- Avoid code repetition by composing templates

---

## 📌 Core Topics

### 1️⃣ `{% block %}` and `{% endblock %}`
- Blocks are placeholders inside a base layout where child templates can insert their own content.
- Used to define editable sections in a base template.

#### Example(base.html)
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <header>My Site Header</header>

    <main>
        {% block content %}
        Default content from base template
        {% endblock %}
    </main>

    <footer>My Site Footer</footer>
</body>
</html>
```
- Here, **title** and **Content** are sections that can be replaced in child templates.
---

### 2️⃣ `{% extends "base.html" %}`
- This tells Jinja2 that a child template will use (inherit) the layout of the base.

#### Example(home.html)
```html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome to the Home Page</h1>
<p>This is child template content.</p>
{% endblock %}
```
- ✔ Only the blocks are replaced; the rest stays from the base file
---
### 3️⃣ `{% include %}` — Reusable Components
- Use include to inject small pieces like navbar, footer, or cards.
#### Example
```html
{% include "navbar.html" %}
{% include "footer.html" %}
```
- It doesn’t override structure — it just inserts the file. Useful for repeated UI components.
---

### 4️⃣ `{% import %}` — Reusing Macros (Reusable Functions)
- You can import macros like functions (e.g., for rendering a button repeatedly).

#### file: components.html
```html
{% macro button(text) %}
<button class="btn">{{ text }}</button>
{% endmacro %}
```
#### Import it where needed:
```html
{% import "components.html" as comp %}

{{ comp.button("Login") }}
{{ comp.button("Sign Up") }}
```
---
### 5️⃣ super() — Call Parent Block Content
- If you want to keep base content and add more.

#### Example
```html
{% block content %}
{{ super() }}  <!-- keeps parent text -->
<p>Extra content from child template.</p>
{% endblock %}
```


# 🎉 Final Understanding — Jinja2 Template Inheritance (Quick Reference)

| **Concept** | **Purpose** |
|-------------|--------------|
| `extends`   | Inherits layout from base template |
| `block`     | Defines replaceable/overridable sections |
| `include`   | Inserts reusable components (navbar, footer, cards, etc.) |
| `import`    | Reuse macros like functions in templates |
| `super()`   | Keep parent block content and add new content below or above it |



