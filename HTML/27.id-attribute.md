# HTML `id` Attribute

The `id` attribute is used to give an HTML element a **unique identifier**.

An `id` value must be **unique**, which means it can be used only once on a webpage.

The `id` attribute is commonly used for:

- Identifying a specific HTML element
- Applying CSS styles
- Accessing elements with JavaScript
- Creating bookmarks (jump links) within a webpage

---

# Syntax

```html
<tag id="unique-name">Content</tag>
```

### Example

```html
<h1 id="main-heading">Welcome to HTML</h1>
```

In this example:

- `id` is the attribute.
- `main-heading` is the unique identifier.

---

# Rules for the `id` Attribute

When creating an `id`, follow these rules:

- Each `id` must be unique within the page.
- An element can have only one `id`.
- Avoid spaces in an `id` value.
- Use meaningful names that describe the element.
- IDs are **case-sensitive** (`Header` and `header` are different).

### Good Examples

```html
<h1 id="main-title">

<div id="about">

<section id="contact">
```

### Avoid

```html
<h1 id="1">

<div id="my section">

<p id="abc123xyz">
```

> **Tip:** Use lowercase letters and hyphens (`-`) for better readability.

Example:

```html
<section id="about-us">
```

---

# Using `id` with CSS

The `id` attribute can be used to apply styles to a specific element.

In CSS, an `id` selector begins with the `#` symbol.

### HTML

```html
<h1 id="title">Welcome</h1>
```

### CSS

```css
#title {
    color: blue;
    text-align: center;
}
```

---

# Using `id` with JavaScript

JavaScript can access an element by its `id`.

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

The text changes from:

```
Hello World
```

to:

```
Welcome!
```

---

# Using `id` for Page Bookmarks

One of the most useful features of the `id` attribute is creating links that jump to a specific section of the same webpage.

## Step 1: Add an `id`

```html
<h2 id="contact">Contact Us</h2>
```

## Step 2: Create a Link

```html
<a href="#contact">
    Go to Contact Section
</a>
```

When the user clicks the link, the browser scrolls directly to the element with the matching `id`.

---

# Bookmark Example

```html
<!DOCTYPE html>
<html>
<head>
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

| `id` | `class` |
|------|---------|
| Must be unique | Can be used on multiple elements |
| One element should have one unique `id` | Many elements can share the same class |
| Used for unique sections | Used for grouping similar elements |
| CSS selector uses `#` | CSS selector uses `.` |
| JavaScript uses `getElementById()` | JavaScript can use `getElementsByClassName()` or `querySelectorAll()` |

### Example

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

---

# Best Practices

- Use unique and descriptive `id` values.
- Use lowercase letters and hyphens (`-`) instead of spaces.
- Don't use the same `id` on multiple elements.
- Use `id` for unique elements and `class` for reusable styles.
- Keep `id` names short and meaningful.

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
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
        You have successfully jumped to this section using the <code>id</code> attribute.
    </p>

</body>
</html>
```

---

Difference Between Class and ID
A class name can be used by multiple HTML elements, while an id name must only be used by one HTML element within the page: 

<!DOCTYPE html>
<html>
    <head>
        <style>
            /* Style the element with the id "myHeader" */
            #myHeader {
            background-color: lightblue;
            color: black;
            padding: 40px;
            text-align: center;
            }

            /* Style all elements with the class name "city" */
            .city {
            background-color: tomato;
            color: white;
            padding: 10px;
            } 
        </style>
    </head>
<body>
    <h2>Difference Between Class and ID</h2>
    <p>A class name can be used by multiple HTML elements, while an id name must only be used by one HTML element within the page:</p>

    <!-- An element with a unique id -->
    <h1 id="myHeader">My Cities</h1>

    <!-- Multiple elements with same class -->
    <h2 class="city">London</h2>
    <p>London is the capital of England.</p>

    <h2 class="city">Paris</h2>
    <p>Paris is the capital of France.</p>

    <h2 class="city">Tokyo</h2>
    <p>Tokyo is the capital of Japan.</p>
</body>
</html>



# Summary

- The `id` attribute uniquely identifies an HTML element.
- Every `id` value must be unique within a webpage.
- CSS selects an `id` using the `#` symbol.
- JavaScript can access an element using `getElementById()`.
- The `id` attribute is commonly used for styling, JavaScript, and page bookmarks.
- Use descriptive, lowercase, and hyphen-separated names for better readability.

