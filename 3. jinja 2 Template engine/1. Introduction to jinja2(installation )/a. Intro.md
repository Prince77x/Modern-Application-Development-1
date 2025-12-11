 # 🧩 Jinja2 Tutorial Notes

## 1️⃣ What is Jinja2?

**Jinja2** is a templating engine for **Python**.  
It takes a **template** (usually HTML) + some **data** and produces the **final output**.

### Example
**Data:**  
```
{"name": "Prince"}
```
**Template:**  
```
Hello {{ name }}!
```
**Output:**  
```
Hello Prince!
```

### You will use Jinja2 mostly in:
- **Flask applications**
- **Django** (has its own engine but similar to Jinja2)
- **Email templating**
- **Static site generators**
- **Rendering dynamic files** (HTML, XML, text)

---

## 2️⃣ Installing Jinja2

Open terminal and run:
```
pip install Jinja2
```

To keep your environment clean:
```
python -m venv env
```

Activate virtual environment:

**Windows:**
```
env\Scripts\activate
```

**Linux/Mac:**
```
source env/bin/activate
```

Then install Jinja2:
```
pip install Jinja2
```

---

## 3️⃣ Your First Jinja2 Template (String Template)

### 👉 Example 1: Rendering a simple string template

Create a file `app.py`:

```
from jinja2 import Template

temp = Template("Hello {{ name }}!")  # Template() converts string into a jinja Object model
output = temp.render(name="Prince")  # .render() take the value of variable "name" and give the output after putting the value in template

print(output)
```

Run:
```
python app.py
```

**Output:**
```
Hello Prince!
```

---

## 4️⃣ Rendering Templates From Files

Create your project folder:

```
project/
   app.py
   templates/
       home.html
```

Inside `templates/home.html`:

```
<h1>Welcome {{ user }}!</h1>
<p>You are learning Jinja2.</p>
```

Now modify `app.py`:

```
from jinja2 import Environment, FileSystemLoader

# Connect templates folder
env = Environment(loader=FileSystemLoader('templates'))

# Load template file
template = env.get_template('home.html')

# Render template
output = template.render(user="Prince")

print(output)
```

Run again:
```
python app.py
```

You will see your **HTML** printed.

---

## 5️⃣ How Jinja2 fits into Flask (Important Preview)

You don’t need Flask yet, but this is important —  
**Flask automatically configures Jinja2** for you.

Example using Flask:

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", user="Prince")

app.run()
```

---

✅ **Summary**
- Jinja2 helps generate dynamic HTML/text using Python.  
- It’s integrated by default in Flask.  
- You can use it independently for small scripts, templated emails, or static sites.

``` 
