# HTML Attributes

HTML attributes provide **extra information** about HTML elements. They are always written inside the **opening tag**.

Attributes help define how an element behaves or how it is displayed.

---

# Basic Syntax

```html
<tagname attribute="value">Content</tagname>
```

### Example

```html
<a href="https://www.google.com">Google</a>
```

Here:
- `a` is the tag
- `href` is the attribute
- `"https://www.google.com"` is the value

---

# Common Rules for Attributes

- Attributes are always written in the **opening tag**
- Most attributes come in **name = "value"** format
- Always use quotes around values (recommended best practice)
- One element can have multiple attributes

### Example

```html
<img src="image.jpg" alt="Nature Image" width="300">
```

---

# Global Attributes

Global attributes can be used on **almost all HTML elements**.

---

## 1. `id` Attribute

Gives a **unique identity** to an element.

### Example

```html
<h1 id="main-title">Welcome</h1>
```

- Each `id` must be unique in a page

---

## 2. `class` Attribute

Used to group multiple elements together.

### Example

```html
<p class="text">Paragraph 1</p>
<p class="text">Paragraph 2</p>
```

---

## 3. `style` Attribute

Used to apply inline CSS styling.

### Example

```html
<p style="color:red;">This is red text</p>
```

---

## 4. `title` Attribute

Shows extra information when hovering over an element.

### Example

```html
<p title="This is a tooltip">Hover over me</p>
```

---

# Link Attributes (`<a>`)

## `href` Attribute

Defines the link destination.

```html
<a href="https://example.com">Visit Site</a>
```

## `target` Attribute

Controls where the link opens.

```html
<a href="https://example.com" target="_blank">Open in new tab</a>
```

| Value | Meaning |
|------|--------|
| `_self` | Opens in same tab |
| `_blank` | Opens in new tab |
| `_parent` | Opens in parent frame |
| `_top` | Opens in full window |

---

# Image Attributes (`<img>`)

## `src` Attribute

Specifies image path.

```html
<img src="cat.jpg">
```

## `alt` Attribute

Alternative text if image fails to load.

```html
<img src="cat.jpg" alt="Cute Cat">
```

## `width` and `height`

Controls image size.

```html
<img src="cat.jpg" width="200" height="200">
```

---

# Input Attributes (Forms Basics)

## `type`

Defines input type.

```html
<input type="text">
<input type="password">
<input type="email">
```

## `placeholder`

Shows hint text.

```html
<input type="text" placeholder="Enter your name">
```

## `value`

Sets default value.

```html
<input type="text" value="Navaneeth">
```

---

# Disabled and Readonly

## `disabled`

Makes an element unclickable.

```html
<button disabled>Click Me</button>
```

## `readonly`

User cannot edit input.

```html
<input type="text" value="Hello" readonly>
```

---

# Boolean Attributes

Some attributes do not need a value.

### Example

```html
<input type="checkbox" checked>
```

- `checked`
- `disabled`
- `readonly`

---

# Multiple Attributes Example

```html
<a
    href="https://google.com"
    target="_blank"
    title="Go to Google"
    class="link">
    Open Google
</a>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>HTML Attributes</title>
</head>

<body>

    <h1 id="main-title" class="title">
        HTML Attributes
    </h1>

    <p class="text" title="This is a paragraph">
        This is an example of attributes.
    </p>

    <a href="https://www.google.com" target="_blank">
        Visit Google
    </a>

    <br><br>

    <img
        src="images/html.png"
        alt="HTML Logo"
        width="200">

    <br><br>

    <input type="text" placeholder="Enter your name">

    <br><br>

    <button disabled>
        Disabled Button
    </button>

</body>

</html>
```

---

# Summary

- Attributes give extra information about HTML elements
- They are written inside opening tags
- Format: `name="value"`
- Global attributes work on most elements (`id`, `class`, `style`, `title`)
- Some attributes are specific to elements (`href`, `src`, `alt`)
- Some attributes are boolean (no value needed)
- One element can have multiple attributes
```