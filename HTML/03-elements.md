# HTML Elements

An **HTML element** is the basic building block of an HTML document. Elements define the structure and content of a webpage.

Most HTML elements consist of:

- An opening tag
- Content
- A closing tag

Example:

```html
<p>This is a paragraph.</p>
```

Here:

- `<p>` → Opening tag
- `This is a paragraph.` → Content
- `</p>` → Closing tag

---

# General Syntax

```html
<tagname>Content goes here</tagname>
```

Example:

```html
<h1>Welcome to HTML</h1>

<p>Learning HTML is fun.</p>

<button>Click Me</button>
```

---

# Nested Elements

HTML elements can contain other HTML elements. This is called **nesting**.

Example:

```html
<body>
    <h1>My Website</h1>

    <p>
        This paragraph contains
        <strong>important text</strong>.
    </p>
</body>
```

In this example:

- `<body>` contains `<h1>` and `<p>`
- `<p>` contains a `<strong>` element

Always close nested elements in the correct order.

Correct:

```html
<p>This is <strong>important</strong> text.</p>
```

Incorrect:

```html
<p>This is <strong>important</p></strong>
```

---

# Empty Elements

Some HTML elements do **not** contain any content and therefore do not require a closing tag.

These are called **empty elements**.

Examples:

```html
<br>
<hr>
<img>
<input>
<meta>
<link>
```

Example:

```html
<p>Hello<br>World</p>
```

---

# HTML Attributes

Attributes provide additional information about an element.

They are written inside the opening tag.

Syntax:

```html
<tagname attribute="value">Content</tagname>
```

Example:

```html
<a href="https://example.com">Visit Website</a>

<img src="image.jpg" alt="Nature">
```

Here:

- `href`
- `src`
- `alt`

are attributes.

---

# Common HTML Attributes

| Attribute | Description |
|-----------|-------------|
| `id` | Gives an element a unique identifier |
| `class` | Groups elements for styling or JavaScript |
| `style` | Adds inline CSS |
| `title` | Displays a tooltip when hovered |
| `href` | Specifies the destination of a link |
| `src` | Specifies the source of an image, video, or other media |
| `alt` | Alternative text for images |
| `width` | Sets the width of an element |
| `height` | Sets the height of an element |

Example:

```html
<img
    src="cat.jpg"
    alt="Cute Cat"
    width="300"
    height="200">
```

---

# Case Sensitivity

HTML tags and attributes are **not case-sensitive**.

These are equivalent:

```html
<H1>Hello</H1>

<h1>Hello</h1>
```

However, the recommended practice is to **always use lowercase** for better readability and consistency.

---

# Whitespace in HTML

The browser ignores extra spaces and line breaks in HTML.

Example:

```html
<p>
    Hello


    World
</p>
```

Output:

```
Hello World
```

If you want to preserve spaces and line breaks, use the `<pre>` element.

Example:

```html
<pre>
Hello
    World
</pre>
```

---

# HTML Element Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>HTML Elements</title>
</head>

<body>

    <h1>Welcome</h1>

    <p>This is a paragraph.</p>

    <a href="https://example.com">Visit Website</a>

    <br>

    <img src="nature.jpg" alt="Nature Image">

</body>

</html>
```

---

# Summary

- HTML elements are the building blocks of web pages.
- Most elements have an opening tag, content, and a closing tag.
- Elements can be nested inside other elements.
- Some elements, such as `<br>` and `<img>`, are empty elements.
- Attributes provide additional information about elements.
- HTML is not case-sensitive, but lowercase is the recommended convention.
- Extra spaces and line breaks are ignored by the browser unless the `<pre>` element is used.