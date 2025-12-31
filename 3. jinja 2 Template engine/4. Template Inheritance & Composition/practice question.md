# 📝 Practice Questions — Jinja2 Template Inheritance

---

## 🧩 Level 1 — Basics

### 🧱 Task 1: Create `base.html`
- Add the following blocks:
  - `{% block title %}` → for page titles  
  - `{% block content %}` → for main content  
- Include a **static header** and **footer**.

### 🧩 Task 2: Create `home.html`
- Extend from `base.html` using:
  ```
  {% extends "base.html" %}
  ```
- Override **only** the `content` block.

### 🧩 Task 3: Create `about.html`
- Extend `base.html`
- Override **both** `title` and `content` blocks.

---

## 🧩 Level 2 — Reusability & Components

### 🧱 Task 4: Include Navbar
- Create `navbar.html`
- Use:
  ```
  {% include "navbar.html" %}
  ```
  to insert the navbar inside `base.html`.

### 🧱 Task 5: Component Macros
- Create `components.html` with a macro:
  ```
  {% macro card(title, description) %}
  <div class="card">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
  </div>
  {% endmacro %}
  ```

- Import this macro in `home.html`:
  ```
  {% import "components.html" as comp %}
  ```

- Display 3 cards:
  ```
  {{ comp.card("Python", "Powerful language") }}
  {{ comp.card("Flask", "Micro web framework") }}
  {{ comp.card("Jinja2", "Template engine for Flask") }}
  ```

### 🧱 Task 6: Add Footer
- Create a `footer.html` file.
- Include it in **every page** using:
  ```
  {% include "footer.html" %}
  ```

---

## 🧩 Level 3 — Advanced (Composition + super())

### 🧱 Task 7: Using `super()`
- In `base.html`, within `{% block content %}`, add:
  ```
  <p>Parent Content: This comes from base.</p>
  ```

- In `contact.html`, override the block but keep parent content:
  ```
  {% extends "base.html" %}
  {% block content %}
      {{ super() }}
      <p>Child Additional Content</p>
  {% endblock %}
  ```

### 🧱 Task 8: Services Page
- Create `services.html` that:
  - Extends `base.html`  
  - Uses both `{% include %}` and `{% import %}`  
  - Displays a **dynamic list of services** using macros.

---

## ⭐ Challenge Task — Project‑Style Setup

### 📂 Project Structure
```
templates/
├── base.html
├── navbar.html
├── footer.html
├── components.html
├── home.html
├── about.html
├── contact.html
```

### 🧱 Requirements
- **Base Template**
  - 3 Blocks → `title`, `content`, and `scripts`
- **Includes**
  - `navbar.html` and `footer.html` included using `{% include %}`
- **Macros**
  - Buttons/cards rendered via `{% import "components.html" as comp %}`
- **super()**
  - At least one page (`contact.html`) should use `{{ super() }}` in its overridden block.

---

