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
