# ⚡ Flask‑WTF Validators — Quick Summary

---

## 🔹 What Are Validators?

**Validators** are rules that automatically **check user input** when a form is submitted.

They prevent:
- Empty submissions  
- Short or invalid input  
- Incorrect data formats  

### ✨ Common Built‑In Validators
| Validator | Purpose |
|------------|----------|
| **DataRequired** | Field cannot be empty |
| **Length(min, max)** | Input must be within the defined range |
| **Email** | Checks for a valid email format |
| **EqualTo(field_name)** | Ensures two fields match (e.g., password confirmation) |

---

## 🧩 Step‑by‑Step: Adding Validators in `register.html`

---

### ✅ Step 1: Install Flask‑WTF
```bash
pip install flask-wtf
```

---

### ✅ Step 2: Configure Secret Key (Required)
```python
app.config["SECRET_KEY"] = "secret123"
```

The **SECRET_KEY** is necessary for CSRF protection and form validation.

---

### ✅ Step 3: Create the Register Form

**File:** `forms.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=20)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")]
    )

    submit = SubmitField("Register")
```

✔ Fields have validation constraints for input checking.  
✔ `EqualTo("password")` ensures password confirmation matches.

---

### ✅ Step 4: Use the Form Inside Your Route

**File:** `app.py`
```python
from flask import Flask, render_template
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return "Registration Successful"

    return render_template("register.html", form=form)
```

✔ `validate_on_submit()` runs all validators automatically when the form is submitted.  
✔ If validation fails, errors are sent back to the template.

---

### ✅ Step 5: Create `register.html`

```html
<form method="POST">
    {{ form.hidden_tag() }}

    {{ form.username.label }}
    {{ form.username() }}
    {% for error in form.username.errors %}
        <p style="color:red">{{ error }}</p>
    {% endfor %}

    {{ form.email.label }}
    {{ form.email() }}
    {% for error in form.email.errors %}
        <p style="color:red">{{ error }}</p>
    {% endfor %}

    {{ form.password.label }}
    {{ form.password() }}
    {% for error in form.password.errors %}
        <p style="color:red">{{ error }}</p>
    {% endfor %}

    {{ form.confirm_password.label }}
    {{ form.confirm_password() }}
    {% for error in form.confirm_password.errors %}
        <p style="color:red">{{ error }}</p>
    {% endfor %}

    {{ form.submit() }}
</form>
```

✔ `hidden_tag()` adds a hidden CSRF protection token.  
✔ `{% for error in form.field.errors %}` displays validation errors on the page.

---

## 🧠 How Validation Works (Simplified)

```
User submits form
      ↓
validate_on_submit()
      ↓
Validators run checks
      ↓
Display error messages in register.html
```

---

## ⚠️ Common Mistakes

| Problem | Cause |
|----------|--------|
| ❌ **Form not submitting or showing errors** | Missing `SECRET_KEY` |
| ❌ **CSRF token error** | Forgot `form.hidden_tag()` |
| ❌ **No validation feedback** | Didn’t loop through `form.errors` in HTML |
| ❌ **Form not validating** | Used `GET` instead of `POST` |

---

## ✅ One‑Line Final Summary

> **Flask‑WTF validators** automatically check form inputs and show clear error messages in `register.html` whenever user data is invalid or incomplete.

---

💡 **Pro Tip:**  
Use a combination of `DataRequired`, `Length`, and `Email` for most forms — and always include `EqualTo` for password confirmation fields.


# 🧩 Form Fields & Validators (Flask‑WTF Guide)

---

## 🟢 Text & Basic Input Fields

| Field Type | Purpose |
|-------------|-----------|
| **StringField** | Single‑line text input |
| **PasswordField** | Password input (hidden characters) |
| **TextAreaField** | Multi‑line text input |

---

## 🔵 Numeric Fields

| Field Type | Purpose |
|-------------|-----------|
| **IntegerField** | Integer values only |
| **FloatField** | Floating‑point numbers |
| **DecimalField** | Precise decimal numbers (for money, etc.) |

---

## 🟣 Selection Fields

| Field Type | Purpose |
|-------------|-----------|
| **SelectField** | Dropdown (single choice) |
| **SelectMultipleField** | Dropdown (multiple selections) |
| **RadioField** | Radio button selection |

---

## 🟠 Boolean & Date/Time Fields

| Field Type | Purpose |
|-------------|-----------|
| **BooleanField** | Checkbox (True / False) |
| **DateField** | Date input (`YYYY‑MM‑DD`) |
| **DateTimeField** | Date + time input |
| **TimeField** | Time input only |

---

## 📁 File & Special Fields

| Field Type | Purpose |
|-------------|-----------|
| **FileField** | File upload field |
| **HiddenField** | Hidden form input (for IDs, tokens, etc.) |
| **SubmitField** | Standard submit button |

---

## ✅ Common Validators (Input Rules)

Validators define **rules for valid input** in Flask‑WTF or WTForms.

---

### 🟢 Required & Optional Validators

| Validator | Purpose |
|------------|----------|
| **DataRequired** | Field must not be empty (value must exist and be non‑blank) |
| **InputRequired** | Raw input required (value must be provided before filters) |
| **Optional** | Field can be empty or not provided |

---

### 🔵 Length & Format Validators

| Validator | Usage | Description |
|------------|--------|-------------|
| **Length(min, max)** | `Length(min=3, max=20)` | Restricts input length |
| **Email** | `Email()` | Must be a valid email address |
| **URL** | `URL()` | Must be a valid website URL |
| **Regexp** | `Regexp(r'^[A-Za-z0-9_]+$')` | Custom regex pattern check |

---

### 🟣 Comparison Validators

| Validator | Purpose |
|------------|----------|
| **EqualTo(field_name)** | Field must match another (e.g., confirm password) |

📘 **Example:**
```python
password = PasswordField("Password")
confirm  = PasswordField("Confirm", validators=[EqualTo("password")])
```

---

### 🔴 Value Range Validators

| Validator | Purpose |
|------------|----------|
| **NumberRange(min, max)** | Check numeric range |
| **AnyOf(values)** | Must match one of given values |
| **NoneOf(values)** | Must *not* match any given values |

---

### 🟠 File Validators (Flask‑WTF Specific)

| Validator | Purpose |
|------------|----------|
| **FileRequired** | Ensures file is uploaded |
| **FileAllowed(extensions)** | Restricts file types (e.g., images only) |

📘 **Example:**
```python
photo = FileField(
    "Profile Picture",
    validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images only!")]
)
```

---

## 🧩 Custom Validators

Create custom rules using `validate_<fieldname>()` methods inside your form class.

**Example:**
```python
class RegisterForm(FlaskForm):
    username = StringField("Username")

    def validate_username(self, username):
        if username.data.lower() == "admin":
            raise ValidationError("Username 'admin' is not allowed.")
```

✔ Custom validators provide flexibility for advanced validation logic.

---

## 🧠 Quick Memory Trick

| Concept | Description |
|----------|-------------|
| **Fields** | Define *what* user enters |
| **Validators** | Define *rules* to check the input |

---

✅ **Pro Tip:**  
Combine **fields** and **validators** to create secure, consistent forms.  
Always keep validation logic *at the form level*, not in views — helps maintain cleaner Flask code.
