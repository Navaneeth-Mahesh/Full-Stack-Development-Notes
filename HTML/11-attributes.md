# HTML Attributes

HTML attributes provide **additional information** about HTML elements. They modify the behavior or appearance of an element and are always written inside the **opening tag**.

---

# Syntax

```html
<tagname attribute="value">Content</tagname>
```

### Example

```html
<a href="https://example.com">Visit Website</a>
```

Here:

- `href` → Attribute
- `"https://example.com"` → Attribute value

---

# Rules for HTML Attributes

- Attributes are always placed inside the **opening tag**.
- Most attributes have a **name** and a **value**.
- Attribute values should be enclosed in **double quotes** (`"`).
- Some attributes are **global attributes**, meaning they can be used with almost every HTML element.
- An element can have multiple attributes.

Example:

```html
<img
    src="nature.jpg"
    alt="Nature"
    width="400"
    height="250">
```

---

# Common HTML Attributes

## `id`

The `id` attribute gives an element a **unique identifier**.

### Example

```html
<h1 id="main-title">Welcome</h1>
```

> An `id` value should be unique within a webpage.

---

## `class`

The `class` attribute groups one or more elements together. It is mainly used for CSS styling and JavaScript.

### Example

```html
<p class="highlight">
    This is highlighted text.
</p>
```

Multiple classes can be assigned:

```html
<p class="highlight large">
    Hello World
</p>
```

---

## `style`

The `style` attribute applies **inline CSS** directly to an element.

### Example

```html
<p style="color: blue;">
    Blue Text
</p>
```

---

## `title`

The `title` attribute displays a tooltip when the user hovers over an element.

### Example

```html
<p title="This is a tooltip">
    Hover over me
</p>
```

---

## `href`

Used with the `<a>` element to specify the destination URL.

### Example

```html
<a href="https://example.com">
    Visit Website
</a>
```

---

## `src`

Specifies the source of an image, video, audio, or other external resource.

### Example

```html
<img src="logo.png" alt="Company Logo">
```

---

## `alt`

Provides alternative text for an image.

### Example

```html
<img
    src="cat.jpg"
    alt="White cat sitting on a sofa">
```

---

## `width` and `height`

Set the width and height of an element.

### Example

```html
<img
    src="nature.jpg"
    alt="Nature"
    width="400"
    height="250">
```

---

## `lang`

Specifies the language of the webpage.

### Example

```html
<html lang="en">
```

---

## `target`

Specifies where a linked document should open.

### Example

```html
<a
    href="https://example.com"
    target="_blank">
    Open Website
</a>
```

Common values:

| Value | Description |
|--------|-------------|
| `_self` | Opens in the current tab (default) |
| `_blank` | Opens in a new tab |
| `_parent` | Opens in the parent frame |
| `_top` | Opens in the full browser window |

---

## `disabled`

Disables form elements such as buttons and input fields.

### Example

```html
<button disabled>
    Submit
</button>
```

---

## `readonly`

Makes an input field read-only.

### Example

```html
<input
    type="text"
    value="Hello"
    readonly>
```

---

## `placeholder`

Displays a hint inside an input field.

### Example

```html
<input
    type="text"
    placeholder="Enter your name">
```

---

## `required`

Makes a form field mandatory before submission.

### Example

```html
<input
    type="email"
    required>
```

---

# Global Attributes

Global attributes can be used on **almost every HTML element**.

Some commonly used global attributes are:

| Attribute | Purpose |
|-----------|---------|
| `id` | Unique identifier |
| `class` | Groups elements |
| `style` | Inline CSS |
| `title` | Tooltip text |
| `lang` | Language of the element |
| `hidden` | Hides an element |
| `tabindex` | Controls keyboard navigation |
| `draggable` | Makes an element draggable |

---

# Boolean Attributes

Some attributes do not require a value. Their presence alone enables the feature.

Examples:

```html
<input type="checkbox" checked>

<input type="text" readonly>

<button disabled>
    Submit
</button>

<input required>
```

Common boolean attributes:

- `checked`
- `disabled`
- `readonly`
- `required`
- `selected`
- `autofocus`
- `multiple`

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>HTML Attributes</title>
</head>

<body>

    <h1 id="heading">HTML Attributes</h1>

    <p
        class="intro"
        title="Introduction">
        Welcome to HTML.
    </p>

    <a
        href="https://example.com"
        target="_blank">
        Visit Website
    </a>

    <br><br>

    <img
        src="nature.jpg"
        alt="Nature"
        width="300">

    <br><br>

    <input
        type="text"
        placeholder="Enter your name"
        required>

    <br><br>

    <button disabled>
        Submit
    </button>

</body>

</html>
```

---

# Best Practices

- Always use **double quotes** around attribute values.
- Use meaningful `id` and `class` names.
- Always include the `alt` attribute for images.
- Avoid excessive inline styles; use external CSS whenever possible.
- Use lowercase attribute names for consistency and readability.

---

# Summary

| Attribute | Purpose |
|-----------|---------|
| `id` | Unique identifier |
| `class` | Groups elements for CSS and JavaScript |
| `style` | Applies inline CSS |
| `title` | Displays a tooltip |
| `href` | Specifies a hyperlink destination |
| `src` | Specifies the source of a resource |
| `alt` | Alternative text for images |
| `width` | Sets element width |
| `height` | Sets element height |
| `lang` | Specifies the language |
| `target` | Specifies where a link opens |
| `disabled` | Disables an element |
| `readonly` | Makes an input read-only |
| `placeholder` | Displays placeholder text |
| `required` | Makes a field mandatory |