# HTML `<div>` Element

The `<div>` (Division) element is a **block-level container** used to group other HTML elements together.

It does not have any visual appearance by default. Instead, it helps organize content and makes it easier to apply CSS styles or JavaScript.

> **Note:** The `<div>` element has no predefined meaning. It is simply a container for other HTML elements.

---

# Basic Syntax

```html
<div>
    Content goes here...
</div>
```

---

# Basic Example

```html
<div>
    <h2>London</h2>

    <p>London is the capital city of England.</p>

    <p>London has over 9 million inhabitants.</p>
</div>
```

### Output

```
London

London is the capital city of England.

London has over 9 million inhabitants.
```

---

# Why Use `<div>`?

The `<div>` element is commonly used to:

- Group related HTML elements
- Apply the same CSS styles to multiple elements
- Create page layouts
- Organize sections of a webpage
- Target groups of elements using JavaScript

---

# Multiple `<div>` Elements

A webpage can contain any number of `<div>` elements.

### Example

```html
<div>
    <h2>London</h2>

    <p>London is the capital city of England.</p>

    <p>London has over 9 million inhabitants.</p>
</div>

<div>
    <h2>Oslo</h2>

    <p>Oslo is the capital city of Norway.</p>

    <p>Oslo has over 700,000 inhabitants.</p>
</div>

<div>
    <h2>Rome</h2>

    <p>Rome is the capital city of Italy.</p>

    <p>Rome has over 4 million inhabitants.</p>
</div>
```

### Output

```
London
London is the capital city of England.
London has over 9 million inhabitants.

Oslo
Oslo is the capital city of Norway.
Oslo has over 700,000 inhabitants.

Rome
Rome is the capital city of Italy.
Rome has over 4 million inhabitants.
```

Notice that each `<div>` starts on a **new line** because it is a **block-level element**.

---

# `<div>` is a Block-Level Element

A block-level element always starts on a new line and takes up the full available width.

Example:

```html
<div>First Div</div>

<div>Second Div</div>

<div>Third Div</div>
```

Output:

```
First Div

Second Div

Third Div
```

---

# Aligning `<div>` Elements Side by Side

By default, `<div>` elements appear one below another.

Using CSS, we can display them side by side.

There are several methods:

- Float
- Inline-block
- Flexbox
- Grid

---

# Method 1: Using Float

The `float` property was originally created for positioning images, but it was commonly used to create layouts before Flexbox and Grid.

### Example

```html
<style>
.mycontainer {
    width: 100%;
    overflow: auto;
}

.mycontainer div {
    width: 33%;
    float: left;
}
</style>

<div class="mycontainer">

    <div>
        <h2>London</h2>
        <p>London is the capital city of England.</p>
    </div>

    <div>
        <h2>Oslo</h2>
        <p>Oslo is the capital city of Norway.</p>
    </div>

    <div>
        <h2>Rome</h2>
        <p>Rome is the capital city of Italy.</p>
    </div>

</div>
```

> **Note:** Today, `float` is rarely used for layouts. Flexbox and Grid are the preferred methods.

---

# Method 2: Using `display: inline-block`

Changing the display property from `block` to `inline-block` allows multiple `<div>` elements to appear on the same line.

### Example

```html
<style>
div {
    width: 30%;
    display: inline-block;
}
</style>

<div>
    <h2>London</h2>
</div>

<div>
    <h2>Oslo</h2>
</div>

<div>
    <h2>Rome</h2>
</div>
```

This method is simple but has limitations when creating complex layouts.

---

# Method 3: Using Flexbox (Recommended)

Flexbox is the most common method for arranging elements in a row or column.

### Example

```html
<style>
.mycontainer {
    display: flex;
}

.mycontainer > div {
    width: 33%;
}
</style>

<div class="mycontainer">

    <div>
        <h2>London</h2>
    </div>

    <div>
        <h2>Oslo</h2>
    </div>

    <div>
        <h2>Rome</h2>
    </div>

</div>
```

### Advantages of Flexbox

- Easy to create responsive layouts
- Less code than float
- Automatically aligns elements
- Most commonly used in modern websites

---

# Method 4: Using CSS Grid

CSS Grid is another modern layout system.

Unlike Flexbox, Grid can organize content into both **rows** and **columns**.

### Example

```html
<style>
.grid-container {
    display: grid;
    grid-template-columns: 33% 33% 33%;
}
</style>

<div class="grid-container">

    <div>
        <h2>London</h2>
    </div>

    <div>
        <h2>Oslo</h2>
    </div>

    <div>
        <h2>Rome</h2>
    </div>

</div>
```

### Advantages of Grid

- Excellent for complex layouts
- Supports rows and columns
- Easy to build responsive webpages

---

# Comparison of Layout Methods

| Method | Recommended? | Best For |
|---------|--------------|----------|
| Float | ❌ No | Older websites |
| Inline-block | ⚠️ Sometimes | Simple layouts |
| Flexbox | ✅ Yes | One-dimensional layouts (row or column) |
| Grid | ✅ Yes | Two-dimensional layouts (rows and columns) |

---

# Real-World Example

```html
<div class="card">

    <h2>HTML Course</h2>

    <p>Learn HTML from beginner to advanced.</p>

    <button>Enroll Now</button>

</div>
```

The `<div>` groups the heading, paragraph, and button into a single **card**.

---

# Best Practices

- Use `<div>` only when no semantic HTML element fits the purpose.
- Prefer semantic elements like `<header>`, `<main>`, `<section>`, `<article>`, `<nav>`, and `<footer>` whenever appropriate.
- Give `<div>` elements meaningful `class` or `id` names.
- Use Flexbox or Grid instead of Float for modern layouts.
- Avoid unnecessary nesting of multiple `<div>` elements.

---

# Summary

| Tag | Description |
|------|-------------|
| `<div>` | Defines a block-level container used to group HTML elements together |

### Key Points

- `<div>` is a block-level element.
- It is mainly used to group HTML elements.
- It has no default styling or semantic meaning.
- Multiple `<div>` elements can be used on the same page.
- CSS can display `<div>` elements side by side.
- Modern websites commonly use **Flexbox** and **Grid** for layouts.