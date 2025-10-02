# 🌐 Introduction to HTML  

**HTML (HyperText Markup Language)** is the **standard language** used to create and structure content on the web.  
- It tells the browser **what to display** (text, images, videos, links, forms, etc.).  
- HTML uses **tags** (like `<h1>`, `<p>`, `<img>`) to mark parts of content.  
- Tags usually come in **pairs**: an opening tag `<p>` and a closing tag `</p>`.  
- Case-insensitive

---

## 🔹 Key Features
1. **Structure** → Organizes content (headings, paragraphs, lists).  
2. **Links** → Connects web pages (via `<a>`).  
3. **Media** → Adds images, videos, and audio.  
4. **Forms** → Collects user input.  
5. **Semantics** → Uses meaningful tags (`<header>`, `<footer>`, `<article>`) for clarity.  

---
## Timelines
- SGML based
    - 1989- HTML original
    - 1995 - HTML 2
    - 1997 - HTML 3,4
- XML based
    - XHTML - 1997 -mid 2010s

- HTML5
    - First release 2008
    - W3c recomandation 2014


## 🔹 Example HTML Code
html
<!DOCTYPE html>
<html>
<head>
  <title>My First Page</title>
</head>
<body>
  <h1>Hello World!</h1>
  <p>This is my first web page.</p>
</body>
</html>


# 🌐 Document Object Model (DOM) in HTML  

**Definition:**  
The **Document Object Model (DOM)** is a **programmatic representation of an HTML document**. It allows **scripts (like JavaScript) to access, modify, and interact** with the content, structure, and style of a webpage.  

In short:  
- The DOM turns the HTML page into a **tree-like structure** of objects (nodes).  
- Each HTML element becomes a **node** in the tree.  
- JavaScript can use the DOM to dynamically **change content, styles, and structure** of the page.  

---

## 🔹 Key Concepts

1. **Nodes**  
   - Everything in the DOM is a node.  
   - Types of nodes:  
     - **Element nodes** → `<p>`, `<div>`, `<h1>`  
     - **Text nodes** → Text inside elements  
     - **Attribute nodes** → Attributes like `id`, `class`, `src`  

2. **Tree Structure**  
   - The HTML document is represented as a **tree of nodes**.  
   - Example:  

Document
└── html
    ├── head
    │   └── title
    └── body
        ├── h1
        └── p



3. **DOM Manipulation**  
   - Using JavaScript, you can:  
     - Change content → `element.textContent = "Hello"`  
     - Change styles → `element.style.color = "red"`  
     - Add/remove elements → `document.createElement()`, `appendChild()`, `removeChild()`  

4. **Event Handling**  
   - DOM allows you to respond to user actions:  
     - Click → `onclick`  
     - Hover → `onmouseover`  
     - Input → `onchange`  

---

## 🔹 Example

```html
<p id="demo">Hello World!</p>
<button onclick="changeText()">Click Me</button>

<script>
function changeText() {
  document.getElementById("demo").textContent = "Hello DOM!";
}
</script>
