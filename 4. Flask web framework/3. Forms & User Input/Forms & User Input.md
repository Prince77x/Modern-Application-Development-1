# 📝 Module — HTML Forms (Foundation in Flask)

---

## 🔹 1. What is an HTML Form?

An **HTML form** is used to **collect input from users**.  
The data is sent from the **browser → server (Flask)**.

### Basic Structure
```html
<form method="POST" action="/submit">
    <input type="text" name="username">
    <button type="submit">Submit</button>
</form>
```

### Important Attributes

| Attribute | Meaning |
|------------|----------|
| **method** | How data is sent (`GET` / `POST`) |
| **action** | URL where data is sent |
| **name** | Key used by Flask to access input |

⚠️ Without a `name` attribute, Flask **cannot access** the input value.

---

## 🧠 2. GET vs POST (Very Important)

### 🔹 GET Method
- Data sent through the **URL**  
- Used for **search**, **filters**, **non‑sensitive data**

**Example URL:**
```
/search?query=flask
```

**Access in Flask:**
```python
request.args.get("query")
```

---

### 🔹 POST Method
- Data sent via the **request body**  
- Used for **login**, **registration**, and **sensitive data**

**Access in Flask:**
```python
request.form.get("username")
```

---

### 🔍 Comparison Table

| Feature | GET | POST |
|----------|-----|------|
| **Data visible in URL** | ✅ | ❌ |
| **Secure** | ❌ | ✅ |
| **Used for** | Read | Write |
| **Flask access** | `request.args` | `request.form` |

---

## 🧠 3. Handling POST Requests in Flask

### 🔹 Why POST Doesn't Work Sometimes
You must:
1. ✅ Allow POST in the route definition  
2. ✅ Use correct method inside the HTML form  
3. ✅ Use correct Flask request object  

**Correct Flask Route:**
```python
from flask import Flask, request

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("username")
    return f"Hello {name}"
```

⚠️ Missing `methods=["POST"]` → ❌ **405 Method Not Allowed** error.

---

## 🧠 4. Request Object (Core Concept)

The **`request` object** stores all incoming user data.

```python
from flask import request
```

### 🔹 `request.form`
Used for **POST** data from `<form method="POST">`.

```python
name = request.form.get("name")
```

✔ Safer than using `request.form["name"]`.

---

### 🔹 `request.args`
Used for **GET** parameters (sent via URL).

**Example URL:**
```
/login?user=prince
```

**Flask Code:**
```python
user = request.args.get("user")
```

---

### 🔑 Summary

| Source | Object |
|---------|---------|
| POST form | `request.form` |
| URL query | `request.args` |
| File upload | `request.files` |

---

## 🧠 5. Single Route with GET + POST (Best Practice)

**Why?**
- Show form → with **GET**
- Submit form → via **POST**

**Flask Code:**
```python
from flask import Flask, render_template, request

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Welcome {name}"
    return render_template("login.html")
```

✔ Very common  
✔ Clean and simple  
✔ Professional practice  

---

## 🔄 6. Redirect & URL Building

### 🔹 Why Redirect?
- Prevent form re‑submission  
- Improve user experience (UX)  
- Follow web standards  

**Using `redirect()`:**
```python
from flask import redirect
return redirect("/success")
```

**Using `url_for()` (Recommended):**
```python
from flask import redirect, url_for
return redirect(url_for("success"))
```

✔ Avoids hardcoded URLs  
✔ Safe for large projects  

---

## 📦 7. File Uploads

**HTML Form:**
```html
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <button>Upload</button>
</form>
```

⚠️ `enctype="multipart/form-data"` is **mandatory** for file uploads.

**Flask Handling:**
```python
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    file.save("uploads/" + file.filename)
    return "Uploaded"
```
## 🔐 Using `multipart/form-data` + Encryption in Flask

---

## 🧠 Big Picture — What’s Happening?

When a user uploads a file:

```
Browser
   ↓ (multipart/form-data)
Flask Server
   ↓
Encrypt File
   ↓
Store Safely
```

So:

- **`multipart/form-data`** → helps send the file correctly.  
- **Encryption** → protects the file once it’s received.  

---

## 📝 Step 1: HTML Form (`multipart/form-data`)

### Why Needed?
Files are **binary data** — they can’t be sent with default form encoding.  
Hence, you must use `multipart/form-data`.

### ✅ Correct HTML Form
```html
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="document">
    <button type="submit">Upload</button>
</form>
```

### Key Rules
✔ `method="POST"`  
✔ `enctype="multipart/form-data"`  
✔ `<input type="file">` **must have a `name`**

---

## 🧠 Step 2: Flask Receives the File

Flask automatically understands `multipart/form-data`.

**Python code:**
```python
file = request.files.get("document")
```

📌 File is available in → `request.files`  
❌ Not available in → `request.form`

---

## 🔐 Step 3: Encrypt the File (Practical)

### 1️⃣ Install Encryption Library
```bash
pip install cryptography
```

### 2️⃣ Load Encryption Key
```python
from cryptography.fernet import Fernet

with open("secret.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)
```

*(Generate a key once using `Fernet.generate_key()` and save it to `secret.key` for reuse.)*

### 3️⃣ Encrypt Uploaded File
```python
data = file.read()
encrypted_data = fernet.encrypt(data)
```

✔ File data is now **unreadable**.  
✔ Safe for secure storage.

---

## 💾 Step 4: Save the Encrypted File

```python
with open("uploads/secure_file.enc", "wb") as f:
    f.write(encrypted_data)
```

📌 The original, unencrypted file is **never saved**.

---

## 🔓 Step 5: Decrypt When Needed

```python
with open("uploads/secure_file.enc", "rb") as f:
    encrypted_data = f.read()

original_data = fernet.decrypt(encrypted_data)
```

✔ Retrieves the **original file content** safely.

---

## 🧩 Complete Flask Route Example

```python
from flask import Flask, request, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

# Load encryption key
with open("secret.key", "rb") as f:
    key = f.read()
fernet = Fernet(key)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("document")
        if not file:
            return "No file uploaded"

        data = file.read()
        encrypted = fernet.encrypt(data)

        with open("uploads/" + file.filename + ".enc", "wb") as f:
            f.write(encrypted)

        return "✅ File uploaded & encrypted successfully!"

    return render_template("upload.html")
```

---

## ⚠️ Common Mistakes (Very Important)

| Mistake | Result |
|----------|--------|
| Missing `enctype` | File not received |
| Using `GET` method | Upload fails |
| Using `request.form` instead of `request.files` | File missing |
| Hard‑coding key | Security risk |
| Storing file without encryption | Sensitive data exposure |

---

## 🧠 Easy Memory Trick

| Concept | Meaning |
|----------|----------|
| **`multipart/form-data`** | SEND the file |
| **Encryption** | PROTECT the file |

---

## ✅ Final Summary

| Concept | Explanation |
|----------|--------------|
| `multipart/form-data` | Required to upload files in forms |
| `request.files` | Flask object that stores uploaded files |
| **Encryption** | Applied after receiving file, before saving |
| **Fernet** | Symmetric encryption module from `cryptography` |
| **Key storage** | Keep your secret key private and secure |

---

💡 **Best Practice Tip:**  
- Generate and save your Fernet key once (`secret.key`).  
- Never hardcode it in your app.  
- Always encrypt before storing — build secure apps from day one.


---

## ✅ 8. Form Validation (Manual)

### Why Validate?
- Never trust client input  
- Prevent empty or invalid data  

**Example:**
```python
name = request.form.get("name")

if not name:
    return "Name is required"
```

✔ Always validate  
✔ Enhances security & data correctness  

---

## 🧩 9. Flask-WTF (Introduction)

### Why Flask-WTF?
- Built‑in validation  
- CSRF protection  
- Cleaner, class-based forms  

**Install:**
```bash
pip install flask-wtf
```

**Basic Form Class:**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Login")
```

✔ Industry standard  
✔ Secure and scalable  

---

## ⚠️ Common Errors & Solutions

| Problem | Reason |
|----------|---------|
| POST not working | Missing `methods=["POST"]` |
| Empty value | Missing `name` attribute |
| `KeyError` | Use `.get()` instead of `["key"]` |
| File not uploading | Missing `enctype="multipart/form-data"` |

---

## 🧪 Practice (Highly Recommended)

1️⃣ Create a **Login Form** (GET + POST)  
2️⃣ Validate empty input fields  
3️⃣ Redirect after successful submission  
4️⃣ Add Profile Picture Upload (using `request.files`)  
5️⃣ Use `url_for()` everywhere to manage links  

---

## ✅ Final Summary

| Concept | Explanation |
|----------|--------------|
| **Forms** | Collect user input |
| **GET** | `request.args` (visible in URL) |
| **POST** | `request.form` (hidden in body) |
| **Redirects** | Used after POST to prevent duplicates |
| **Validation** | Must check user input |
| **Flask‑WTF** | Simplifies and secures forms |

---

💡 **Key Takeaway:**  
HTML forms + Flask make interactive web apps possible.  
Always **validate inputs**, **redirect after POST**, and **use `url_for()`** for maintainable, professional code.
