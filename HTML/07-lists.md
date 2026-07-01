# HTML Lists

HTML lists are used to group related items together. They make content more organized and easier to read.

There are **three types of lists** in HTML:

1. Ordered List (`<ol>`)
2. Unordered List (`<ul>`)
3. Description List (`<dl>`)

---

# Ordered List (`<ol>`)

An **ordered list** displays items in a numbered or lettered sequence. Use it when the order of items matters.

### Syntax

```html
<ol>
    <li>First Item</li>
    <li>Second Item</li>
    <li>Third Item</li>
</ol>
```

### Example

```html
<ol>
    <li>Wake up</li>
    <li>Brush your teeth</li>
    <li>Go to college</li>
</ol>
```

**Output:**

1. Wake up
2. Brush your teeth
3. Go to college

---

# Ordered List Types

The `type` attribute changes the numbering style.

| Value | Output |
|--------|--------|
| `1` | 1, 2, 3 (Default) |
| `A` | A, B, C |
| `a` | a, b, c |
| `I` | I, II, III |
| `i` | i, ii, iii |

### Example

```html
<ol type="A">
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
```

---

# The `start` Attribute

The `start` attribute specifies the starting number of an ordered list.

### Example

```html
<ol start="5">
    <li>Chapter Five</li>
    <li>Chapter Six</li>
    <li>Chapter Seven</li>
</ol>
```

Output:

5. Chapter Five
6. Chapter Six
7. Chapter Seven

---

# Unordered List (`<ul>`)

An **unordered list** displays items using bullet points.

### Syntax

```html
<ul>
    <li>Item One</li>
    <li>Item Two</li>
    <li>Item Three</li>
</ul>
```

### Example

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

---

# Bullet Styles

The `list-style-type` CSS property changes the bullet style.

| Value | Appearance |
|--------|------------|
| `disc` | ● (Default) |
| `circle` | ○ |
| `square` | ■ |
| `none` | No bullets |

### Example

```html
<ul style="list-style-type: square;">
    <li>Apple</li>
    <li>Mango</li>
    <li>Orange</li>
</ul>
```

---

# Description List (`<dl>`)

A **description list** is used to display terms and their descriptions.

It uses three tags:

- `<dl>` → Description List
- `<dt>` → Description Term
- `<dd>` → Description Details

### Syntax

```html
<dl>
    <dt>HTML</dt>
    <dd>Used to structure web pages.</dd>

    <dt>CSS</dt>
    <dd>Used to style web pages.</dd>
</dl>
```

---

# Nested Lists

A list can contain another list inside one of its items.

### Example

```html
<ul>
    <li>
        Frontend
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </li>

    <li>Backend</li>
</ul>
```

Nested lists are useful for creating menus, categories, and hierarchical content.

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Lists</title>
</head>
<body>

    <h2>Ordered List</h2>

    <ol type="A">
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ol>

    <h2>Unordered List</h2>

    <ul style="list-style-type: square;">
        <li>Apple</li>
        <li>Banana</li>
        <li>Mango</li>
    </ul>

    <h2>Description List</h2>

    <dl>
        <dt>HTML</dt>
        <dd>Creates the structure of a webpage.</dd>

        <dt>CSS</dt>
        <dd>Styles the webpage.</dd>

        <dt>JavaScript</dt>
        <dd>Adds interactivity to the webpage.</dd>
    </dl>

</body>
</html>
```

---

# Best Practices

- Use ordered lists when the sequence of items is important.
- Use unordered lists for collections where order does not matter.
- Use description lists for definitions, glossaries, FAQs, and key-value information.
- Keep list items concise and meaningful.
- Use nested lists only when needed to maintain readability.

---

# Summary

| Tag/Attribute | Purpose |
|---------------|---------|
| `<ol>` | Creates an ordered (numbered) list |
| `<ul>` | Creates an unordered (bulleted) list |
| `<li>` | Defines a list item |
| `<dl>` | Creates a description list |
| `<dt>` | Defines a term in a description list |
| `<dd>` | Provides the description of a term |
| `type` | Changes the numbering style of an ordered list |
| `start` | Sets the starting number of an ordered list |
| `list-style-type` | Changes the bullet style of an unordered list |