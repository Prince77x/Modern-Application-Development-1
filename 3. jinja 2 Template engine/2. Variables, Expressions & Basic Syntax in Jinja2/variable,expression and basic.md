f# 🧩 Jinja2 Variables, Expressions, and Filters

## 1️⃣ Variables in Jinja2

You print variables using:
```
{{ variable }}
```

### Example (Python side)
```
name = "Prince"
age = 20
```

**Template:** 
```
My name is {{ name }} and I am {{ age }} years old.
```

**Output:**
```
My name is Prince and I am 20 years old.
```

### Variables can be:
- ✔ Strings  
- ✔ Numbers  
- ✔ Lists  
- ✔ Dictionaries  
- ✔ Objects  
- ✔ Functions (callable)

---

## 2️⃣ Expressions in Jinja2

Inside `{{ ... }}` you can use:

### ✔ Math expressions
```
{{ 10 + 5 }}
{{ price * quantity }}
```

### ✔ Comparison
```
{{ age > 18 }}
{{ marks == 100 }}
```

### ✔ String operations
```
{{ name.upper() }}
{{ "Hi " + user }}
```

---

## 3️⃣ Dot Notation (Super Important)

Jinja2 uses **dot notation**:
```
{{ user.name }}
{{ student.age }}
{{ product.price }}
```

It can access:
- Dictionary keys  
- Object attributes  
- List indices (with `[]`)

### Example dictionary
```
user = {"name": "Prince", "city": "Bihar"}
```

**Template:**
```
Hello {{ user.name }} from {{ user.city }}!
```

**Output:**
```
Hello Prince from Bihar!
```

---

## 4️⃣ Filters in Jinja2 

Filters modify variables.

**Syntax:**
``` 
{{ variable | filter }}
```

### Examples:
```
{{ name | upper }}
{{ city | lower }}
{{ book | title }}
{{ students | length }}
{{ username | default("Guest") }}
```

---

## 5️⃣ Comments in Jinja2

### Single-line comment
```
{# This is a comment #}
```

Comments are **completely removed** when rendering.

---

## 6️⃣ Whitespace Control (Advanced but useful)

Use:
```
{{- variable -}}
```

The minus `-` removes surrounding spaces.

**Example:**
```
{{- name -}}
```

---

## 7️⃣ Printing Multiple Variables

```
Name: {{ name }}, Age: {{ age }}, Email: {{ email }}
```

Jinja2 handles spacing automatically and prints cleanly.

---

## 8️⃣ Accessing List Values

**Python:**
```
fruits = ["apple", "banana", "mango"]
```

**Template:**
```
{{ fruits }}
{{ fruits }}
```

**Output:**
```
apple
banana
```

---

## 9️⃣ Accessing Dictionary Values

**Python:**
```
student = {"name": "Prince", "marks": 95}
```

**Template:**
```
{{ student.name }}
{{ student["marks"] }}
```

Both work!

---

## 🔟 Calling Functions in Template

**Python:**
```
def greet(name):
    return f"Hello {name}"
```

**Template:**
```
{{ greet("Prince") }}
```

**Output:**
```
Hello Prince
```

---

## 🎯 Summary Table

| Feature            | Syntax              | Example              | Output / Meaning       |
|--------------------|--------------------|----------------------|------------------------|
| Variable           | `{{ variable }}`   | `{{ name }}`         | Value of variable      |
| Expression         | `{{ 10 + 20 }}`    | `30`                 | Arithmetic result      |
| Filter             | `{{ name | upper }}` | `"PRINCE"`          | Applies transformation |
| Comment            | `{# comment #}`    | —                    | Not rendered           |
| List access        | `{{ list[0] }}`    | —                    | First element          |
| Dictionary access  | `{{ dict.key }}`   | —                    | Value from dictionary  |
| Function call      | `{{ func() }}`     | —                    | Function output        |

---

✅ **Quick Recap**
- Use `{{ ... }}` to print or compute values.  
- Use filters (`|`) to transform data.  
- Use `{# ... #}` for comments.  
- Access list, dict, and object data easily with dot notation.
```

 