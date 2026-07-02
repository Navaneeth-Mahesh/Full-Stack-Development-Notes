# The `class` Attribute

The `class` attribute is used to assign one or more class names to an HTML element.

Classes are mainly used for:

- Applying the same CSS styles to multiple elements.
- Selecting and manipulating elements using JavaScript.

> **Note:** The `class` attribute can be used on **any HTML element**.

---

# Syntax

```html
<tagname class="class-name">
    Content
</tagname>
```

### Example

```html
<p class="intro">
    Welcome to HTML.
</p>
```

Here:

- `class` → Attribute
- `intro` → Class name

---

# Using a Class with CSS

To create a class in CSS:

1. Start with a **period (`.`)**.
2. Write the class name.
3. Add CSS properties inside `{ }`.

### Example

```html
<!DOCTYPE html>
<html>

<head>

<style>

.city {
    background-color: tomato;
    color: white;
    padding: 15px;
}

</style>

</head>

<body>

<h2 class="city">London</h2>

<h2 class="city">Paris</h2>

<h2 class="city">Tokyo</h2>

</body>
</html>
```

### Output

All three headings will have:

- Tomato background
- White text
- 15px padding

This is because they all use the same class (`city`).

---

# Applying the Same Class to Multiple Elements

A single class can be shared by multiple HTML elements.

### Example

```html
<!DOCTYPE html>
<html>

<head>

<style>

.city {
    background-color: tomato;
    color: white;
    border: 2px solid black;
    margin: 20px;
    padding: 20px;
}

</style>

</head>

<body>

<div class="city">
    <h2>London</h2>
    <p>London is the capital of England.</p>
</div>

<div class="city">
    <h2>Paris</h2>
    <p>Paris is the capital of France.</p>
</div>

<div class="city">
    <h2>Tokyo</h2>
    <p>Tokyo is the capital of Japan.</p>
</div>

</body>

</html>
```

All three `<div>` elements receive the same styling because they use the same class name.

---

# Using Classes with `<span>`

The `<span>` element is commonly used to style a specific part of a sentence.

### Example

```html
<!DOCTYPE html>
<html>

<head>

<style>

.note {
    color: red;
    font-size: 120%;
}

</style>

</head>

<body>

<h1>
    My <span class="note">Important</span> Heading
</h1>

<p>
    This is some <span class="note">important</span> text.
</p>

</body>

</html>
```

Only the word **Important** and **important** will be styled.

---

# Multiple Classes

An HTML element can have **more than one class**.

Separate multiple class names with a space.

### Syntax

```html
class="class1 class2"
```

### Example

```html
<!DOCTYPE html>
<html>

<head>

<style>

.city {
    background-color: tomato;
    color: white;
}

.main {
    text-align: center;
}

</style>

</head>

<body>

<h2 class="city main">London</h2>

<h2 class="city">Paris</h2>

<h2 class="city">Tokyo</h2>

</body>

</html>
```

The first heading belongs to **both** classes:

- `city`
- `main`

So it receives styles from both classes.

---

# Different Elements Can Share the Same Class

A class is **not limited to one HTML tag**.

Different elements can use the same class.

### Example

```html
<!DOCTYPE html>
<html>

<head>

<style>

.city {
    color: blue;
}

</style>

</head>

<body>

<h2 class="city">Paris</h2>

<p class="city">
    Paris is the capital of France.
</p>

</body>

</html>
```

Both the `<h2>` and `<p>` elements share the same styling.

---

# Using Classes with JavaScript

JavaScript can select elements using their class name.

The method used is:

```javascript
document.getElementsByClassName("class-name")
```

### Example

```html
<!DOCTYPE html>
<html>

<body>

<h2 class="city">London</h2>

<h2 class="city">Paris</h2>

<h2 class="city">Tokyo</h2>

<button onclick="hideCities()">
    Hide Cities
</button>

<script>

function hideCities() {

    var cities = document.getElementsByClassName("city");

    for (var i = 0; i < cities.length; i++) {
        cities[i].style.display = "none";
    }

}

</script>

</body>

</html>
```

When the button is clicked, all elements with the class **city** will disappear.

> **Don't worry if you don't understand the JavaScript yet.** You'll learn it later. Just remember that JavaScript can use class names to access HTML elements.

---

# Rules for Class Names

- Class names are **case-sensitive**.
- A class name should describe the purpose of the element.
- Multiple elements can use the same class.
- One element can have multiple classes.

### Good Examples

```html
class="card"

class="navbar"

class="btn-primary"

class="product"
```

### Avoid

```html
class="abc"

class="x1"

class="test123"
```

Choose meaningful names that describe the content or purpose.

---

# `class` vs `id`

| `class` | `id` |
|----------|------|
| Can be used on multiple elements | Must be unique on the page |
| Used for groups of elements | Used for one specific element |
| Written as `.className` in CSS | Written as `#idName` in CSS |
| Can assign multiple classes | Only one unique `id` per element |

Example:

```html
<h2 class="city">London</h2>

<h2 id="main-heading">
    Welcome
</h2>
```

---

# Summary

- The `class` attribute assigns one or more class names to an HTML element.
- Classes are mainly used by CSS and JavaScript.
- A class can be applied to any HTML element.
- Multiple elements can share the same class.
- One element can have multiple classes by separating class names with spaces.
- Class names are case-sensitive.
- JavaScript can access elements using `getElementsByClassName()`.
- Use meaningful class names to make your code easier to understand and maintain.