# CSS Basics

## What is CSS?

**CSS (Cascading Style Sheets)** is the language used to style and design HTML webpages.

While **HTML** defines the **structure** of a webpage, CSS controls **how it looks**, including:

* Colors
* Fonts
* Spacing
* Borders
* Backgrounds
* Layouts
* Animations
* Responsive design

Think of a webpage like building a house:

| Technology     | Role                                                        |
| -------------- | ----------------------------------------------------------- |
| **HTML**       | Builds the structure (walls, doors, windows)                |
| **CSS**        | Paints and decorates the house                              |
| **JavaScript** | Adds functionality (lights, automatic doors, smart devices) |

---

# Why Use CSS?

Without CSS, every webpage would appear as plain text with basic browser styling.

CSS allows you to:

* Change text colors
* Set fonts and font sizes
* Add background colors or images
* Control spacing using margins and padding
* Create layouts
* Add borders and shadows
* Build responsive websites
* Create transitions and animations

---

# How CSS Works

When a browser loads a webpage:

```text
Browser
    │
    ▼
Reads HTML
    │
    ▼
Loads CSS
    │
    ▼
Matches CSS selectors with HTML elements
    │
    ▼
Applies styles
    │
    ▼
Displays the final webpage
```

---

# Ways to Add CSS

There are **three** ways to add CSS to an HTML document.

---

# 1. Inline CSS

Inline CSS is written directly inside an HTML element using the `style` attribute.

## Syntax

```html
<tag style="property: value;">Content</tag>
```

## Example

```html
<h1 style="color: blue;">Hello World</h1>

<p style="color: red;">This text is red.</p>
```

### Advantages

* Quick for testing styles.
* Useful for styling a single element.

### Disadvantages

* Difficult to maintain.
* Repeats code.
* Not suitable for large projects.

---

# 2. Internal CSS

Internal CSS is written inside a `<style>` element within the `<head>` section.

## Example

```html
<!DOCTYPE html>
<html>

<head>

<style>
h1 {
    color: blue;
}

p {
    color: gray;
}
</style>

</head>

<body>

<h1>Welcome</h1>

<p>This is a paragraph.</p>

</body>
</html>
```

### Advantages

* Keeps styles in one location.
* Good for single-page websites.

### Disadvantages

* Styles cannot be shared with other pages.

---

# 3. External CSS (Recommended)

External CSS stores styles in a separate `.css` file.

## Step 1: Create a CSS File

```text
styles.css
```

## Step 2: Add CSS

```css
body {
    background-color: #f5f5f5;
}

h1 {
    color: blue;
}
```

## Step 3: Link the File

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

### Advantages

* Easy to maintain.
* Reusable across multiple pages.
* Cleaner HTML.
* Faster development for larger projects.
* Recommended for almost all websites.

---

# Comparing CSS Methods

| Method       | Where it is Written     | Best For            | Recommended  |
| ------------ | ----------------------- | ------------------- | ------------ |
| Inline CSS   | Inside the HTML element | Quick testing       | ❌ No         |
| Internal CSS | Inside `<style>`        | Small websites      | ⚠️ Sometimes |
| External CSS | Separate `.css` file    | Real-world projects | ✅ Yes        |

---

# CSS Syntax

Every CSS rule consists of:

* Selector
* Property
* Value

## Syntax

```css
selector {
    property: value;
}
```

## Example

```css
h1 {
    color: blue;
}
```

Explanation:

| Part    | Meaning  |
| ------- | -------- |
| `h1`    | Selector |
| `color` | Property |
| `blue`  | Value    |

---

# Multiple CSS Properties

You can apply multiple styles to the same selector.

```css
h1 {
    color: blue;
    font-size: 36px;
    text-align: center;
}
```

Each property must end with a semicolon (`;`).

---

# CSS Comments

Comments are ignored by the browser and are useful for explaining your code.

## Syntax

```css
/* This is a CSS comment */
```

## Example

```css
/* Main heading */
h1 {
    color: blue;
}
```

---

# Common CSS Properties

| Property           | Purpose                       |
| ------------------ | ----------------------------- |
| `color`            | Changes text color            |
| `background-color` | Sets the background color     |
| `font-size`        | Changes the text size         |
| `font-family`      | Changes the font              |
| `font-weight`      | Makes text bold or lighter    |
| `text-align`       | Aligns text                   |
| `border`           | Adds a border                 |
| `border-radius`    | Creates rounded corners       |
| `width`            | Sets width                    |
| `height`           | Sets height                   |
| `margin`           | Adds space outside an element |
| `padding`          | Adds space inside an element  |

---

# Complete Example

## HTML (`index.html`)

```html
<!DOCTYPE html>
<html>

<head>
    <title>CSS Basics</title>

    <link rel="stylesheet" href="styles.css">
</head>

<body>

<h1>Welcome to CSS</h1>

<p>This page is styled using an external CSS file.</p>

</body>

</html>
```

---

## CSS (`styles.css`)

```css
body {
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
}

h1 {
    color: blue;
    text-align: center;
}

p {
    color: #555;
    font-size: 18px;
}
```

---

# Best Practices

* Use **external CSS** for most projects.
* Keep HTML responsible for structure and CSS responsible for styling.
* Use meaningful class names.
* Avoid excessive inline styles.
* Organize related styles into sections.
* Add comments when necessary.
* Keep your CSS clean and consistent.

---

# Common Beginner Mistakes

❌ Forgetting the semicolon (`;`)

```css
h1 {
    color: blue
}
```

✅ Correct

```css
h1 {
    color: blue;
}
```

---

❌ Forgetting curly braces

```css
h1
color: blue;
```

✅ Correct

```css
h1 {
    color: blue;
}
```

---

❌ Misspelling property names

```css
colr: blue;
```

✅ Correct

```css
color: blue;
```

---

# Summary

| Method       | Description                                        | Recommended                               |
| ------------ | -------------------------------------------------- | ----------------------------------------- |
| Inline CSS   | Styles are written directly inside an HTML element | ❌ Only for quick testing or unique styles |
| Internal CSS | Styles are written inside a `<style>` tag          | ⚠️ Suitable for small projects            |
| External CSS | Styles are stored in a separate `.css` file        | ✅ Best practice for almost all websites   |

---

## Key Takeaways

* CSS is responsible for the **appearance** of a webpage.
* CSS works by applying **rules** to HTML elements.
* A CSS rule consists of a **selector**, **property**, and **value**.
* External CSS is the preferred method for most projects.
* Well-organized CSS makes websites easier to maintain and scale.
