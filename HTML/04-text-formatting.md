# HTML Text Formatting

HTML provides several tags to format text, making it more meaningful and visually appealing. Some tags only change the appearance, while others also add semantic meaning, which helps browsers, search engines, and assistive technologies understand the content.

---

# Bold Text

The `<b>` tag displays text in **bold** without adding any special meaning.

### Syntax

```html
<b>Bold Text</b>
```

### Example

```html
<p>This is <b>bold</b> text.</p>
```

**Output:**

This is **bold** text.

---

# Strong Text

The `<strong>` tag indicates that the text is **important**. Browsers usually display it in bold.

### Syntax

```html
<strong>Important Text</strong>
```

### Example

```html
<p>Please read the <strong>instructions</strong> carefully.</p>
```

**Output:**

Please read the **instructions** carefully.

> **Difference:** Use `<strong>` for important content and `<b>` when you only want bold styling.

---

# Italic Text

The `<i>` tag displays text in *italic* without adding emphasis.

### Syntax

```html
<i>Italic Text</i>
```

### Example

```html
<p>This is <i>italic</i> text.</p>
```

---

# Emphasized Text

The `<em>` tag indicates emphasized text. Browsers usually display it in italics.

### Syntax

```html
<em>Emphasized Text</em>
```

### Example

```html
<p>This is <em>very important</em>.</p>
```

> **Difference:** Use `<em>` when the text needs emphasis and `<i>` when you only want italic styling.

---

# Marked Text

The `<mark>` tag highlights text.

### Syntax

```html
<mark>Highlighted Text</mark>
```

### Example

```html
<p>HTML is <mark>easy to learn</mark>.</p>
```

---

# Small Text

The `<small>` tag displays smaller-sized text.

### Syntax

```html
<small>Small Text</small>
```

### Example

```html
<p>Price: ₹999 <small>Including GST</small></p>
```

---

# Deleted Text

The `<del>` tag represents deleted or removed text.

### Syntax

```html
<del>Deleted Text</del>
```

### Example

```html
<p>Price: <del>₹999</del> ₹799</p>
```

---

# Inserted Text

The `<ins>` tag represents newly inserted text. Browsers usually underline it.

### Syntax

```html
<ins>Inserted Text</ins>
```

### Example

```html
<p><ins>New Feature Added</ins></p>
```

---

# Subscript Text

The `<sub>` tag displays text below the normal line.

Common uses:

- Chemical formulas
- Mathematical expressions

### Example

```html
<p>H<sub>2</sub>O</p>
```

**Output:**

H₂O

---

# Superscript Text

The `<sup>` tag displays text above the normal line.

Common uses:

- Exponents
- Footnotes

### Example

```html
<p>2<sup>3</sup> = 8</p>
```

**Output:**

2³ = 8

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>Text Formatting</title>
</head>
<body>

    <p><b>Bold Text</b></p>

    <p><strong>Important Text</strong></p>

    <p><i>Italic Text</i></p>

    <p><em>Emphasized Text</em></p>

    <p><mark>Highlighted Text</mark></p>

    <p><small>Small Text</small></p>

    <p><del>Old Price: ₹999</del></p>

    <p><ins>New Price: ₹799</ins></p>

    <p>H<sub>2</sub>O</p>

    <p>2<sup>5</sup> = 32</p>

</body>
</html>
```

---

# Summary

| Tag | Purpose |
|------|---------|
| `<b>` | Displays bold text without semantic meaning |
| `<strong>` | Marks important text (usually bold) |
| `<i>` | Displays italic text without semantic meaning |
| `<em>` | Marks emphasized text (usually italic) |
| `<mark>` | Highlights text |
| `<small>` | Displays smaller text |
| `<del>` | Represents deleted text |
| `<ins>` | Represents inserted text (usually underlined) |
| `<sub>` | Displays subscript text |
| `<sup>` | Displays superscript text |