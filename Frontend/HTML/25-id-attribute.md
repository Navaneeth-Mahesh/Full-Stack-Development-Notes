# HTML `id` Attribute

The `id` attribute is used to assign a **unique identifier** to an HTML element.

Each `id` value **must be unique** within a webpage. This means **no two elements should have the same `id`**.

The `id` attribute is commonly used for:

* Identifying a specific HTML element
* Applying CSS styles
* Accessing elements with JavaScript
* Creating page bookmarks (jump links)
* Improving accessibility by linking elements together (for example, `<label>` with form inputs)

---

# Syntax

```html
<tag id="unique-name">
    Content
</tag>
```

## Example

```html
<h1 id="main-heading">
    Welcome to HTML
</h1>
```

### Explanation

* `id` → Attribute name
* `main-heading` → Unique identifier

The browser can now uniquely identify this `<h1>` element.

---

# How an `id` Works

```text id="8y4sl0"
HTML Element
      │
      ▼
id="main-heading"
      │
      ├── CSS → #main-heading
      │
      ├── JavaScript → getElementById()
      │
      └── HTML Links → href="#main-heading"
```

One `id` can be used by **CSS**, **JavaScript**, and **HTML links**.

---

# Rules for the `id` Attribute

When creating an `id`, follow these rules:

* Every `id` must be unique within the page.
* One element can have only one `id`.
* Do not use spaces.
* Use meaningful names.
* `id` values are **case-sensitive**.
* An `id` should not begin with a number (recommended for compatibility with CSS and JavaScript selectors).

---

## Good Examples

```html
<h1 id="main-title">

<section id="about-us">

<div id="contact">

<footer id="page-footer">
```

---

## Avoid

```html
<h1 id="1">

<div id="my section">

<p id="abc123xyz">

<section id="Header">
```

Better:

```html
<section id="page-header">
```

---

# Naming Convention

The most common naming style is:

* Lowercase letters
* Hyphens (`-`)
* Meaningful names

Example:

```html
<section id="about-us">

<div id="student-profile">

<footer id="page-footer">
```

Avoid underscores or random names unless your project requires them.

---

# Using `id` with CSS

The `id` attribute allows CSS to style **one specific element**.

CSS uses the **`#` selector** for IDs.

## HTML

```html
<h1 id="title">
    Welcome
</h1>
```

## CSS

```css
#title {
    color: blue;
    text-align: center;
}
```

### Result

Only the element with `id="title"` is affected.

---

# Using `id` with JavaScript

JavaScript can find an element using its `id`.

The most common method is:

```javascript
document.getElementById("id-name");
```

---

## Example

### HTML

```html
<p id="message">
    Hello World
</p>
```

### JavaScript

```javascript
document.getElementById("message").innerHTML = "Welcome!";
```

### Before

```text id="d7rmlh"
Hello World
```

### After

```text id="vx9j62"
Welcome!
```

---

# Using `id` for Page Bookmarks

An `id` can create links that jump to a specific section of the same page.

This is called a **bookmark** or **fragment identifier**.

---

## Step 1: Add an `id`

```html
<h2 id="contact">
    Contact Us
</h2>
```

---

## Step 2: Create a Link

```html
<a href="#contact">
    Go to Contact Section
</a>
```

When the user clicks the link, the browser automatically scrolls to the element with `id="contact"`.

---

## How It Works

```text id="8vbo52"
<a href="#contact">
        │
        ▼
Looks for

id="contact"

        │
        ▼
Browser scrolls to that element
```

---

# Bookmark Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Bookmarks</title>
</head>

<body>

    <a href="#about">
        Go to About Section
    </a>

    <br><br><br><br><br><br><br><br><br><br>

    <h2 id="about">
        About Us
    </h2>

    <p>
        This is the About section.
    </p>

</body>

</html>
```

---

# Difference Between `id` and `class`

Both `id` and `class` identify HTML elements, but they are used differently.

| `id`                                        | `class`                                                                     |
| ------------------------------------------- | --------------------------------------------------------------------------- |
| Must be unique                              | Can be shared by many elements                                              |
| Used for one specific element               | Used for groups of similar elements                                         |
| CSS selector uses `#`                       | CSS selector uses `.`                                                       |
| JavaScript commonly uses `getElementById()` | JavaScript commonly uses `getElementsByClassName()` or `querySelectorAll()` |
| One element should have only one `id`       | One element can have multiple classes                                       |

---

## Example

```html
<h1 id="main-title">
    Welcome
</h1>

<p class="text">
    Paragraph One
</p>

<p class="text">
    Paragraph Two
</p>
```

Here:

* `main-title` identifies one heading.
* `text` groups multiple paragraphs.

---

# Visual Comparison

```text id="jlwmel"
ID

main-title
     │
     ▼
<h1>


CLASS

text
 │
 ├── <p>
 ├── <p>
 └── <p>
```

One `id` → One element

One `class` → Many elements

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>HTML ID Attribute</title>

    <style>

        #heading {
            color: blue;
        }

        #box {
            border: 2px solid black;
            padding: 10px;
        }

    </style>

</head>

<body>

    <a href="#contact">
        Jump to Contact
    </a>

    <h1 id="heading">
        Welcome to HTML
    </h1>

    <div id="box">
        This is a styled box.
    </div>

    <br><br><br><br><br><br><br>

    <h2 id="contact">
        Contact Section
    </h2>

    <p>
        You have successfully jumped to this section using the
        <code>id</code> attribute.
    </p>

</body>

</html>
```

---

# Example: Difference Between `id` and `class`

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <style>

        /* Styles one element */
        #myHeader {
            background-color: lightblue;
            color: black;
            padding: 20px;
            text-align: center;
        }

        /* Styles multiple elements */
        .city {
            background-color: tomato;
            color: white;
            padding: 10px;
        }

    </style>

</head>

<body>

    <h1 id="myHeader">
        My Cities
    </h1>

    <h2 class="city">London</h2>
    <p>London is the capital of England.</p>

    <h2 class="city">Paris</h2>
    <p>Paris is the capital of France.</p>

    <h2 class="city">Tokyo</h2>
    <p>Tokyo is the capital of Japan.</p>

</body>

</html>
```

Here:

* `#myHeader` styles **one** heading.
* `.city` styles **all three** city headings.

---

# Common Beginner Mistakes

### ❌ Using the same `id` multiple times

```html
<div id="box"></div>

<div id="box"></div>
```

IDs must be unique.

✔ Correct

```html
<div id="box1"></div>

<div id="box2"></div>
```

or

```html
<div class="box"></div>

<div class="box"></div>
```

---

### ❌ Using spaces

```html
<div id="my box">
```

✔ Better

```html
<div id="my-box">
```

---

### ❌ Using meaningless names

```html
<div id="abc123">
```

✔ Better

```html
<div id="user-profile">
```

---

### ❌ Using `id` when a `class` is more appropriate

If several elements need the same styling:

```html
<p id="text">One</p>

<p id="text">Two</p>
```

Use a class instead.

```html
<p class="text">One</p>

<p class="text">Two</p>
```

---

# Best Practices

* Give every `id` a meaningful name.
* Keep `id` values unique.
* Use lowercase letters and hyphens (`-`).
* Avoid spaces and special characters.
* Use `id` for unique elements.
* Use `class` for reusable styles.
* Keep names short but descriptive.

---

# Summary

| Feature        | `id`                            |
| -------------- | ------------------------------- |
| Purpose        | Identifies one specific element |
| Must be Unique | Yes                             |
| CSS Selector   | `#id-name`                      |
| JavaScript     | `document.getElementById()`     |
| HTML Bookmark  | `href="#id-name"`               |
| Reusable       | No                              |

---

# Key Points

* The `id` attribute gives an HTML element a **unique identifier**.
* Each `id` value should appear **only once** on a webpage.
* CSS selects IDs using the `#` symbol.
* JavaScript commonly accesses IDs with `document.getElementById()`.
* IDs can be used to create **page bookmarks** using `href="#id-name"`.
* Use `id` for **unique elements** and `class` for **groups of similar elements**.
* Follow a consistent naming convention using **lowercase letters** and **hyphens** for clean, maintainable HTML.
