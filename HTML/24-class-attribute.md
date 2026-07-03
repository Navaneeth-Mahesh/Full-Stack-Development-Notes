# HTML `class` Attribute

The `class` attribute is used to assign **one or more class names** to an HTML element.

Classes are mainly used by:

* **CSS** to apply the same styles to multiple elements.
* **JavaScript** to select and manipulate groups of elements.

> **Important:** The `class` attribute can be added to **almost any HTML element**.

---

# Why Do We Need Classes?

Imagine you have 50 buttons on a webpage.

Instead of writing CSS for each button separately, you can give them all the same class.

```text id="tvv1wv"
HTML Elements
        │
        ▼
class="button"
        │
        ▼
CSS
.button { ... }
        │
        ▼
All buttons get the same style
```

This saves time and keeps your code organized.

---

# Basic Syntax

```html
<tagname class="class-name">
    Content
</tagname>
```

Example:

```html
<p class="intro">
    Welcome to HTML.
</p>
```

Here:

* `class` → HTML attribute
* `intro` → Class name

---

# Using a Class in CSS

To style a class in CSS:

1. Start with a **dot (`.`)**.
2. Write the class name.
3. Add CSS properties inside `{}`.

## Example

### HTML

```html
<h2 class="city">London</h2>

<h2 class="city">Paris</h2>

<h2 class="city">Tokyo</h2>
```

### CSS

```css
.city {
    background-color: tomato;
    color: white;
    padding: 15px;
}
```

All three headings receive the same styling because they use the same class.

---

# How Classes Work

```text id="h7ajyu"
HTML

<h2 class="city">London</h2>
<h2 class="city">Paris</h2>
<h2 class="city">Tokyo</h2>

          │
          ▼

CSS

.city {
    color: white;
}

          │
          ▼

All elements having class="city"
receive the CSS styles.
```

---

# Applying the Same Class to Multiple Elements

One class can be shared by many elements.

## Example

### HTML

```html
<div class="city">
    <h2>London</h2>
    <p>Capital of England.</p>
</div>

<div class="city">
    <h2>Paris</h2>
    <p>Capital of France.</p>
</div>

<div class="city">
    <h2>Tokyo</h2>
    <p>Capital of Japan.</p>
</div>
```

### CSS

```css
.city {
    background-color: tomato;
    color: white;
    border: 2px solid black;
    margin: 20px;
    padding: 20px;
}
```

Each `<div>` automatically gets the same appearance.

---

# Using Classes with `<span>`

`<span>` is commonly used to style a small part of text.

Example:

```html
<p>
    Learning
    <span class="highlight">HTML</span>
    is fun.
</p>
```

```css
.highlight {
    color: red;
    font-weight: bold;
}
```

Only the word **HTML** is styled.

---

# Multiple Classes

An element can belong to **more than one class**.

Separate class names with spaces.

## Syntax

```html
class="class1 class2 class3"
```

Example:

```html
<h2 class="city main">
    London
</h2>
```

### CSS

```css
.city {
    background-color: tomato;
    color: white;
}

.main {
    text-align: center;
}
```

The element receives styles from **both** classes.

```text id="yih1ku"
city class
     +
main class
     │
     ▼
Combined styling
```

---

# Different Elements Can Share the Same Class

Classes are **not limited to one HTML tag**.

Example:

```html
<h2 class="blue-text">
    Welcome
</h2>

<p class="blue-text">
    HTML is easy to learn.
</p>

<div class="blue-text">
    Practice every day.
</div>
```

```css
.blue-text {
    color: blue;
}
```

All three elements become blue.

---

# Using Classes in JavaScript

JavaScript can select elements using their class name.

Method:

```javascript
document.getElementsByClassName("class-name")
```

Example:

```html
<h2 class="city">London</h2>

<h2 class="city">Paris</h2>

<h2 class="city">Tokyo</h2>

<button onclick="hideCities()">
    Hide Cities
</button>

<script>
function hideCities() {

    let cities = document.getElementsByClassName("city");

    for (let i = 0; i < cities.length; i++) {
        cities[i].style.display = "none";
    }

}
</script>
```

When the button is clicked, all elements with the class `city` are hidden.

> Don't worry if you don't understand JavaScript yet. Just remember that classes help JavaScript find groups of elements.

---

# Naming Rules for Classes

Class names:

* Are **case-sensitive**.
* Should describe the purpose of the element.
* Cannot contain spaces (spaces separate multiple classes).
* Should be meaningful.

## Good Examples

```html
class="card"

class="navbar"

class="product"

class="btn-primary"

class="footer"

class="user-profile"
```

## Avoid

```html
class="abc"

class="x"

class="test1"

class="xyz123"
```

Meaningful names make your code easier to understand.

---

# Best Practices

### ✔ Use lowercase letters

```html
class="header"
```

Instead of:

```html
class="Header"
```

---

### ✔ Use hyphens for multiple words

```html
class="main-content"

class="login-form"

class="product-card"
```

Instead of:

```html
class="mainContent"

class="main_content"
```

Both work, but hyphen-separated names are commonly used in CSS.

---

### ✔ Reuse classes

Instead of:

```css
.button1 { }

.button2 { }

.button3 { }
```

Use:

```css
.button { }
```

and apply it wherever needed.

---

# `class` vs `id`

| `class`                               | `id`                                              |
| ------------------------------------- | ------------------------------------------------- |
| Can be used on multiple elements      | Must be unique on the page                        |
| Used for groups of elements           | Used for one specific element                     |
| CSS uses `.`                          | CSS uses `#`                                      |
| JavaScript can select many elements   | JavaScript usually selects one element            |
| One element can have multiple classes | An element should have only one unique `id` value |

Example:

```html
<h2 class="city">
    London
</h2>

<h1 id="main-heading">
    Welcome
</h1>
```

---

# `class` vs `id` Visualization

```text id="rlsbnd"
Classes

.city
 │
 ├── London
 ├── Paris
 └── Tokyo


ID

#main-heading
 │
 └── Welcome
```

One class can be shared by many elements.

An `id` should identify only one element.

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>Class Attribute</title>

    <style>

        .card {
            border: 1px solid black;
            padding: 15px;
            margin: 10px;
        }

        .highlight {
            color: red;
            font-weight: bold;
        }

    </style>

</head>

<body>

    <div class="card">

        <h2>HTML</h2>

        <p>
            HTML is the
            <span class="highlight">foundation</span>
            of web development.
        </p>

    </div>

    <div class="card">

        <h2>CSS</h2>

        <p>
            CSS styles webpages beautifully.
        </p>

    </div>

</body>

</html>
```

---

# Common Beginner Mistakes

### ❌ Forgetting the dot in CSS

Wrong:

```css
city {
    color: blue;
}
```

Correct:

```css
.city {
    color: blue;
}
```

---

### ❌ Using spaces inside one class name

Wrong:

```html
class="main content"
```

This creates **two classes**:

* `main`
* `content`

If you want one class name, use:

```html
class="main-content"
```

---

### ❌ Giving every element a different class

Wrong:

```html
class="button1"

class="button2"

class="button3"
```

Better:

```html
class="button"
```

Reuse classes whenever possible.

---

### ❌ Using meaningless names

```html
class="abc"

class="x"

class="test"
```

Use descriptive names instead.

```html
class="login-form"

class="sidebar"

class="product-card"
```

---

# Summary

| Feature                         | Description                            |
| ------------------------------- | -------------------------------------- |
| Attribute                       | `class`                                |
| Purpose                         | Groups elements for CSS and JavaScript |
| CSS Selector                    | `.className`                           |
| JavaScript Method               | `getElementsByClassName()`             |
| Multiple Elements               | ✅ Yes                                  |
| Multiple Classes on One Element | ✅ Yes                                  |

---

# Key Points

* The `class` attribute assigns one or more class names to an HTML element.
* Classes are mainly used for **CSS styling** and **JavaScript selection**.
* A class can be applied to **multiple elements**.
* One element can have **multiple classes**, separated by spaces.
* Class names are **case-sensitive** and should be descriptive.
* In CSS, classes are selected using a **dot (`.`)**.
* In JavaScript, classes can be accessed using `document.getElementsByClassName()`.
* Reusing meaningful class names makes your code cleaner, easier to maintain, and more consistent.
