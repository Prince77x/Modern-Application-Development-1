# 🧩 Jinja2 Full Course Outline (Short & Crisp)

---

## 🗂 Module 1 — Introduction to Jinja2
**Objectives:**  
Understand what Jinja2 is, install/setup, and render a first template.

**Topics:**  
- What is Jinja2 (templating engine inspired by Django).  
- Installation: `pip install Jinja2`.  
- Basic usage with `Environment`, `Template`, `FileSystemLoader`.  
- Integration with Flask/Django.

**Example:** 
```
from jinja2 import Template
t = Template("Hello {{ name }}!")
print(t.render(name="Aisha"))
```

**Exercises:**  
Render a template string and a file-based template.

---

## 💡 Module 2 — Variables, Expressions, and Syntax
**Objectives:**  
Use variables safely, control whitespace, and use filters/comments.

**Topics:**  
- `{{ }}` for expressions, `{% %}` for logic, `{# #}` for comments.  
- Attribute access, indexing, callable variables.  
- Filters: `|lower`, `|upper`, `|join`, `|default`.  
- Tests: `is defined`, `is none`, etc.  
- Whitespace control: `{{-`, `-}}`.

**Exercises:**  
Show user profile with filters and safe fallbacks.

---

## 🔁 Module 3 — Control Structures
**Objectives:**  
Iterate, conditionally render, and set variables.

**Topics:**  
- `for`, `if / elif / else`, `{% set %}`.  
- `loop` meta vars: `loop.index`, `loop.first`, `loop.last`.  
- Macro intro.

**Exercises:**  
Paginated table rendering; compute derived value with `set`.

---

## 🧱 Module 4 — Template Inheritance & Composition
**Objectives:**  
Reuse and extend layouts.

**Topics:**  
- `{% block %}` / `{% endblock %}`.  
- `{% extends %}`, `{% include %}`, `{% import %}`.  
- `super()` to call parent content.

**Exercises:**  
Base layout with header/footer + 3 child pages.

---

## ⚙️ Module 5 — Macros & Reusable Components
**Objectives:**  
Write and reuse macros across templates.

**Topics:**  
- `{% macro %}`, arguments.  
- `{% import %}` and `{% from ... import ... %}`.  
- `call` blocks.

**Exercises:**  
Macro file for form controls used in multiple templates.

---

## 🧩 Module 6 — Filters & Tests (Custom)
**Objectives:**  
Use and create filters/tests.

**Topics:**  
- Common filters: `safe`, `escape`, `sort`, `map`, `batch`.  
- Custom filters/tests via `Environment.filters/tests`.

**Example:**
```
def rev(s): return s[::-1]
env.filters["rev"] = rev
template = env.from_string("{{ 'abc' | rev }}")
```

**Exercises:**  
Rupee formatter filter & email validation test.

---

## 🔒 Module 7 — Autoescaping & Security
**Objectives:**  
Avoid XSS and template injection.

**Topics:**  
- Autoescape for HTML.  
- `|safe` for trusted HTML.  
- Escaping, sandboxing, and safe environments.

**Exercises:**  
Demonstrate XSS and fix via autoescape/sandbox.

---

## ⚡ Module 8 — Template Loading & Environment
**Objectives:**  
Configure loaders, caching, and environment options.

**Topics:**  
- `FileSystemLoader`, `PackageLoader`, `DictLoader`.  
- `ChoiceLoader`, `FileSystemBytecodeCache`.  
- Options: `autoescape`, `trim_blocks`, `cache_size`.  
- Template globals and context processors.

**Exercises:**  
Load templates via package and enable bytecode cache.

---

## 🌐 Module 9 — Internationalization (i18n)
**Objectives:**  
Add translations and localization.

**Topics:**  
- `{% trans %}` block, Flask-Babel integration.  
- `gettext` usage.

**Exercises:**  
Translate templates for English/Hindi.

---

## ⚙️ Module 10 — Extensions & Advanced Features
**Objectives:**  
Use and write extensions.

**Topics:**  
- Built-in: `with`, `do`, `loopcontrols`, `i18n`.  
- Writing custom extensions.  
- Decorators: `environmentfilter`, `contextfilter`.

**Exercises:**  
Create a `{% shout %}` tag extension that uppercases text.

---

## 🚀 Module 11 — Performance & Best Practices
**Objectives:**  
Optimize and write maintainable templates.

**Topics:**  
- Logic in Python, minimal loops in templates.  
- Template caching & organization.  
- Best practices:
  - Logic-light templates  
  - Sanitize inputs  
  - Use macros for repeated UI  
  - Use `trim_blocks` / `lstrip_blocks` for clean output

---

## 🧩 Module 12 — Integration with Flask & Others
**Objectives:**  
Use Jinja2 in Flask and similar frameworks.

**Topics:**  
- `render_template`, `app.jinja_env`.  
- Custom filters/globals via `app.template_filter`.  
- Blueprint templates and static handling.

**Exercises:**  
Build a small Flask app with layout, macros, and filters.

---

## 🧪 Module 13 — Testing & CI for Templates
**Objectives:**  
Test and validate templates automatically.

**Topics:**  
- pytest rendering tests.  
- Snapshot HTML tests.  
- Template linting and CI integration.

**Exercises:**  
Write pytest tests for templates with mock contexts.

---

## 🏁 Final Projects
Pick 1–2:
- **Portfolio Site Generator** — Static site with macros & pagination.  
- **Mini CMS (Flask + Jinja2)** — Auth + theming + WYSIWYG-safe HTML.  
- **Email Templating System** — Dynamic emails with localization.  
- **UI Component Library** — Reusable macros + documentation.

---

## 🧾 Assessment Ideas
- **Quizzes:** variables, filters, flow control.  
- **Assignments:** small template builds.  
- **Mid-Project:** Flask app with multiple templates.  
- **Final Project:** from list above.  
- **Bonus:** build a custom Jinja2 extension.
```
