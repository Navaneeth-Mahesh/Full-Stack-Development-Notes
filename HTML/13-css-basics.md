# CSS Basics

CSS (**Cascading Style Sheets**) is used to style and format HTML documents. While HTML provides the **structure** of a webpage, CSS controls its **appearance**, such as colors, fonts, spacing, layouts, and animations.

> **Think of it this way:**
>
> - **HTML** → Structure
> - **CSS** → Styling
> - **JavaScript** → Interactivity

---

# Why Use CSS?

Without CSS, every webpage would look like plain text with basic formatting.

CSS allows you to:

- Change text colors
- Set fonts and font sizes
- Add backgrounds
- Control spacing (margin and padding)
- Create layouts
- Add borders and shadows
- Make websites responsive
- Create animations and transitions

---

# Ways to Add CSS

There are **three** ways to add CSS to an HTML document.

## 1. Inline CSS

Inline CSS is written directly inside an HTML element using the `style` attribute.

### Syntax

```html
<h1 style="color: blue;">Hello World</h1>
```

### Example

```html
<p style="color: red;">This text is red.</p>
```

### Advantages

- Quick for testing small styles.
- Useful for applying a unique style to a single element.

### Disadvantages

- Difficult to maintain.
- Repeats styles across multiple elements.
- Not recommended for large projects.

---

## 2. Internal CSS

Internal CSS is written inside a `<style>` element within the `<head>` section of the HTML document.

### Example

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

- Keeps styles in one place.
- Suitable for single-page websites or small projects.

### Disadvantages

- Styles cannot be shared across multiple HTML files.

---

## 3. External CSS

External CSS stores all styles in a separate `.css` file.

### Step 1: Create a CSS File

```text
styles.css
```

### Step 2: Write CSS

```css
body {
    background-color: #f5f5f5;
}

h1 {
    color: blue;
}
```

### Step 3: Link the CSS File

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

### Advantages

- Easy to maintain.
- Styles can be reused across multiple pages.
- Improves code organization.
- Recommended for most websites.

---

# CSS Syntax

A CSS rule consists of:

- Selector
- Property
- Value

### Syntax

```css
selector {
    property: value;
}
```

### Example

```css
h1 {
    color: blue;
}
```

Here:

- `h1` → Selector
- `color` → Property
- `blue` → Value

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

# Common CSS Properties

| Property | Purpose |
|----------|---------|
| `color` | Changes text color |
| `background-color` | Sets the background color |
| `font-size` | Sets the font size |
| `font-family` | Changes the font |
| `text-align` | Aligns text |
| `border` | Adds a border |
| `width` | Sets the width |
| `height` | Sets the height |
| `margin` | Adds space outside an element |
| `padding` | Adds space inside an element |

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

- Use **external CSS** for most projects.
- Keep HTML focused on structure and CSS focused on styling.
- Use meaningful class names instead of inline styles.
- Organize CSS into logical sections.
- Add comments for complex styles.

---

# Summary

| Method | Description | Recommended |
|---------|-------------|-------------|
| Inline CSS | Styles are added directly to HTML elements | ❌ Only for small changes |
| Internal CSS | Styles are written inside a `<style>` tag | ⚠️ Good for small projects |
| External CSS | Styles are stored in a separate `.css` file | ✅ Best practice for most websites |