# DOM Basics (Document Object Model)

The **DOM (Document Object Model)** is a programming interface for HTML documents. It represents the structure of a webpage as a tree of objects that can be accessed and manipulated using JavaScript.

---

# What is the DOM?

When a browser loads an HTML page, it converts the HTML into a **tree-like structure** called the DOM.

This allows JavaScript to:

- Read HTML elements
- Change content
- Modify styles
- Add or remove elements
- Respond to user actions

---

# HTML to DOM Example

### HTML Code

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Hello</h1>
    <p>Welcome to DOM</p>
</body>
</html>
```

### DOM Representation

```
Document
 └── html
     └── body
         ├── h1 → "Hello"
         └── p  → "Welcome to DOM"
```

Each HTML tag becomes a **node** in the DOM tree.

---

# Why DOM is Important

Without DOM:

- HTML is static (no interaction)

With DOM:

- Web pages become dynamic
- Content can change without reloading the page
- User interactions become possible

Example:
- Clicking a button
- Showing/hiding content
- Form validation
- Animations

---

# DOM Structure

The DOM is structured like a **family tree**:

- **Document** → root of the page
- **Element nodes** → HTML tags like `<html>`, `<body>`, `<p>`
- **Text nodes** → text inside elements
- **Attribute nodes** → properties like `id`, `class`, `src`

---

# Accessing DOM with JavaScript

You can access HTML elements using JavaScript.

## By ID

```html
<p id="demo">Hello</p>

<script>
document.getElementById("demo").innerText = "Changed Text";
</script>
```

---

## By Class Name

```html
<p class="text">Item 1</p>

<script>
document.getElementsByClassName("text")[0].innerText = "Updated";
</script>
```

---

## By Tag Name

```html
<p>Paragraph 1</p>

<script>
document.getElementsByTagName("p")[0].innerText = "Modified";
</script>
```

---

## Query Selector (Recommended)

```html
<p class="demo">Hello</p>

<script>
document.querySelector(".demo").innerText = "Hello DOM";
</script>
```

---

# Changing HTML Content

```javascript
element.innerHTML = "New Content";
element.innerText = "New Text";
```

Example:

```html
<h1 id="title">Old Title</h1>

<script>
document.getElementById("title").innerHTML = "New Title";
</script>
```

---

# Changing Styles

You can modify CSS using DOM:

```html
<p id="text">Hello</p>

<script>
document.getElementById("text").style.color = "red";
document.getElementById("text").style.fontSize = "20px";
</script>
```

---

# Creating Elements

```javascript
let para = document.createElement("p");
para.innerText = "New Paragraph";

document.body.appendChild(para);
```

---

# Removing Elements

```javascript
let element = document.getElementById("demo");
element.remove();
```

---

# Event Example (DOM Interaction)

```html
<button onclick="changeText()">Click Me</button>

<p id="text">Hello</p>

<script>
function changeText() {
    document.getElementById("text").innerText = "Button Clicked!";
}
</script>
```

---

# Common DOM Methods

| Method | Description |
|--------|-------------|
| `getElementById()` | Select element by ID |
| `getElementsByClassName()` | Select elements by class |
| `getElementsByTagName()` | Select elements by tag |
| `querySelector()` | Select first matching element |
| `querySelectorAll()` | Select all matching elements |
| `createElement()` | Create new element |
| `appendChild()` | Add element inside another |
| `remove()` | Delete an element |

---

# Summary

- DOM represents HTML as a tree structure.
- It allows JavaScript to interact with web pages.
- You can access, change, add, or remove elements.
- DOM makes websites dynamic and interactive.
```* seo-html.md
* web-apis-expanded.md
* web-components.md