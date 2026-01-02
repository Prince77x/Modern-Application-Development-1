# 📘 Jinja2 Macros — Complete Guide with Examples

---

## 📌 1. Defining a Macro

### 🧩 Code
```jinja2
{% macro input_field(label, name, type="text", placeholder="") %}
<label>{{ label }}</label>
<input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
<br>
{% endmacro %}
```

### 🧠 Line‑by‑Line Explanation

| Line | Explanation |
|------|--------------|
| `{% macro input_field(label, name, type="text", placeholder="") %}` | Defines a macro (like a function). Takes 4 parameters, `type` and `placeholder` have default values. |
| `<label>{{ label }}</label>` | Displays the label text passed to the macro. `{{ }}` prints values to HTML. |
| `<input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">` | Creates an input field with dynamic type, name, and placeholder. |
| `<br>` | Adds a line break after the field. |
| `{% endmacro %}` | Ends the macro definition. |

🔑 **Macro = Function for HTML (Reusable UI block)**

---

## 📌 2. Importing the Macro File

### 🧩 Code
```jinja2
{% import "forms.html" as form %}
```

### 🧠 Explanation
- `import "forms.html"` → Loads the macro file.  
- `as form` → Creates a namespace so macros can be accessed like `form.macroName`.  
- Prevents naming conflicts across multiple macro files.

✔ After importing:
```jinja2
{{ form.input_field("Email", "email") }}
```

---

## 📌 3. Using the Macro in a Template

### 🧩 Code
```jinja2
<form>
    {{ form.input_field("Email", "email", "email", "Enter your email here") }}
    {{ form.input_field("Password", "password", "password", "Enter password") }}
</form>
```

### 🧠 Explanation

| Line | What It Does |
|------|---------------|
| `<form>` | Starts an HTML form. |
| `{{ form.input_field(...) }}` | Calls the macro and injects dynamically generated HTML. |
| `"Email"` | Becomes `<label>Email</label>`. |
| `"email"` | Becomes `name="email"` (backend receives this field). |
| `"email"` | Sets `type="email"` (HTML5 validation). |
| `"Enter your email here"` | Sets placeholder text in the input field. |
| `</form>` | Ends the form. |

🎯 **Everything inside `{{ }}` becomes visible HTML output.**

---

## 📌 4. Importing Only Specific Macros

### 🧩 Code
```jinja2
{% from "forms.html" import input_field %}
```

### 🧠 Explanation
- Imports **only one macro** from the file.  
- Call directly **without a prefix**:
  ```jinja2
  {{ input_field("Username", "username") }}
  ```
✔ Best when working with a macro file containing many reusable components.

---

## 📌 5. `call` Blocks (Advanced Feature)

### 🧩 Macro Definition
```jinja2
{% macro panel(title) %}
<div class="panel">
    <h2>{{ title }}</h2>
    {% call() %}{% endcall %}
</div>
{% endmacro %}
```

### 🧠 Line‑by‑Line Meaning

| Syntax | Meaning |
|---------|----------|
| `{% macro panel(title) %}` | Defines a macro with a `title` parameter. |
| `<div class="panel">` | Creates a container for dynamic content. |
| `<h2>{{ title }}</h2>` | Displays the title. |
| `{% call() %}{% endcall %}` | Placeholder for nested HTML content provided by the caller. |
| `{% endmacro %}` | Ends the macro definition. |

### 🧩 Calling It
```jinja2
{% call panel("User Profile") %}
    <p>Name: John</p>
    <p>Email: john@example.com</p>
{% endcall %}
```

### 🧠 Explanation
- `{% call panel("User Profile") %}` → Starts macro execution with a title.  
- The HTML inside (`<p>...</p>`) → Injected into the macro’s call block.  
- `{% endcall %}` → Ends and passes the inner content back to the macro body.

---

## 🧠 Why Are Macros Important?

| Without Macros | With Macros |
|------------------|-------------|
| Repeated HTML everywhere | Write once, reuse anywhere |
| Hard to maintain | Update one place → changes everywhere |
| Messy templates | Organized and professional structure |

---

## 🎯 Final Understanding Summary

| Concept | Explanation |
|----------|--------------|
| `macro` | Defines a reusable HTML component |
| **Parameters** | Allow passing dynamic values to the macro |
| `import` | Loads the entire macro file with a namespace |
| `from ... import ...` | Imports specific macros only |
| `call` | Allows inserting nested HTML inside a macro |

---
