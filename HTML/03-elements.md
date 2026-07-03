# HTML Elements

HTML elements are the **building blocks of every webpage**. They tell the browser **what to display** and **how the content should be structured**.

Everything you see on a webpage—headings, paragraphs, images, buttons, links, forms—is created using HTML elements.

---

# Anatomy of an HTML Element

Most HTML elements have **three parts**:

1. **Opening Tag**
2. **Content**
3. **Closing Tag**

### Syntax

```html
<tagname>Content goes here</tagname>
```

### Example

```html
<p>This is a paragraph.</p>
```

### Breakdown

| Part | Description |
|------|-------------|
| `<p>` | Opening tag |
| `This is a paragraph.` | Content |
| `</p>` | Closing tag |

### Visual Representation

```text
<p> This is a paragraph. </p>
 │           │            │
 │           │            └── Closing Tag
 │           └────────────── Content
 └────────────────────────── Opening Tag
```

---

# Common HTML Elements

| Element | Purpose |
|----------|---------|
| `<h1>` to `<h6>` | Headings |
| `<p>` | Paragraph |
| `<a>` | Hyperlink |
| `<img>` | Image |
| `<button>` | Button |
| `<div>` | Generic container |
| `<span>` | Inline container |
| `<ul>` | Unordered list |
| `<ol>` | Ordered list |
| `<li>` | List item |

Example:

```html
<h1>Welcome to HTML</h1>

<p>Learning HTML is fun.</p>

<button>Click Me</button>
```

---

# Nested Elements

An HTML element can contain **other HTML elements**. This is called **nesting**.

### Example

```html
<body>

    <h1>My Website</h1>

    <p>
        This paragraph contains
        <strong>important text</strong>.
    </p>

</body>
```

### Structure

```text
<body>
│
├── <h1>
│
└── <p>
      │
      └── <strong>
```

In this example:

- `<body>` contains both `<h1>` and `<p>`.
- `<p>` contains a `<strong>` element.
- `<strong>` makes the enclosed text bold and indicates that it is important.

---

# Closing Nested Elements Correctly

Always close elements in the **reverse order** in which they were opened.

### Correct

```html
<p>This is <strong>important</strong> text.</p>
```

### Incorrect

```html
<p>This is <strong>important</p></strong>
```

Incorrect nesting may lead to unexpected webpage layouts.

---

# Empty (Void) Elements

Some HTML elements **do not have content**, so they **do not require a closing tag**.

These are called **empty elements** (also known as **void elements**).

### Common Empty Elements

| Element | Purpose |
|----------|---------|
| `<br>` | Line break |
| `<hr>` | Horizontal line |
| `<img>` | Displays an image |
| `<input>` | Input field |
| `<meta>` | Metadata |
| `<link>` | Links external resources (like CSS) |

### Example

```html
<p>Hello<br>World</p>
```

Output:

```text
Hello
World
```

---

# HTML Attributes

Attributes provide **additional information** about an HTML element.

They are written **inside the opening tag**.

### Syntax

```html
<tagname attribute="value">Content</tagname>
```

### Example

```html
<a href="https://example.com">Visit Website</a>

<img src="image.jpg" alt="Nature">
```

Here:

- `href`
- `src`
- `alt`

are **attributes**.

---

# How Attributes Work

```text
<img src="cat.jpg" alt="Cute Cat">

 │      │             │
 │      │             └── alt attribute
 │      └──────────────── src attribute
 └─────────────────────── img element
```

---

# Common HTML Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `id` | Gives an element a unique identifier | `id="header"` |
| `class` | Groups elements for styling or JavaScript | `class="card"` |
| `style` | Adds inline CSS | `style="color:red;"` |
| `title` | Shows a tooltip on hover | `title="Click here"` |
| `href` | Specifies the destination of a link | `href="about.html"` |
| `src` | Specifies the source of an image, video, etc. | `src="photo.jpg"` |
| `alt` | Alternative text if an image cannot load | `alt="Mountain"` |
| `width` | Sets width | `width="300"` |
| `height` | Sets height | `height="200"` |
| `target` | Specifies where to open a linked document | `target="_blank"` |

### Example

```html
<img
    src="cat.jpg"
    alt="Cute Cat"
    width="300"
    height="200">
```

---

# Multiple Attributes

An element can have **multiple attributes**.

Example:

```html
<a
    href="https://example.com"
    target="_blank"
    title="Visit Example">
    Visit Website
</a>
```

---

# HTML is Not Case-Sensitive

HTML tags and attribute names are **not case-sensitive**.

These are treated the same:

```html
<H1>Hello</H1>

<h1>Hello</h1>
```

However, the recommended practice is to **always use lowercase**.

### Recommended

```html
<h1>Hello</h1>
```

---

# Whitespace in HTML

Browsers ignore:

- Extra spaces
- Multiple blank lines
- Additional tabs

### Example

```html
<p>
    Hello


    World
</p>
```

Output:

```text
Hello World
```

---

# Preserving Whitespace with `<pre>`

The `<pre>` element preserves:

- Spaces
- Tabs
- Line breaks

exactly as written.

### Example

```html
<pre>
Hello
    World
</pre>
```

Output:

```text
Hello
    World
```

---

# Complete Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>HTML Elements</title>
</head>

<body>

    <h1>Welcome</h1>

    <p>This is a paragraph.</p>

    <a href="https://example.com">
        Visit Website
    </a>

    <br>

    <img
        src="nature.jpg"
        alt="Nature Image"
        width="300">

</body>

</html>
```

---

# Best Practices

- Use lowercase for all HTML tags and attributes.
- Always close elements that require a closing tag.
- Nest elements correctly.
- Write meaningful `alt` text for images.
- Use double quotes (`" "`) around attribute values.
- Keep your code properly indented for better readability.

Example:

```html
<div class="card">
    <h2>Product</h2>
    <p>Price: ₹500</p>
</div>
```

---

# Common Beginner Mistakes

### Forgetting the Closing Tag

❌ Incorrect

```html
<p>Hello
```

✅ Correct

```html
<p>Hello</p>
```

---

### Incorrect Nesting

❌ Incorrect

```html
<p><strong>Hello</p></strong>
```

✅ Correct

```html
<p><strong>Hello</strong></p>
```

---

### Forgetting Quotes Around Attribute Values

❌ Incorrect

```html
<img src=cat.jpg>
```

✅ Correct

```html
<img src="cat.jpg">
```

---

### Using Uppercase Tags

Allowed:

```html
<H1>Hello</H1>
```

Recommended:

```html
<h1>Hello</h1>
```

---

# Quick Revision

- HTML elements are the building blocks of webpages.
- Most elements have an opening tag, content, and a closing tag.
- Elements can be nested inside other elements.
- Some elements, like `<br>` and `<img>`, are empty (void) elements and do not require closing tags.
- Attributes provide additional information about elements.
- Multiple attributes can be added to a single element.
- HTML is not case-sensitive, but lowercase is the recommended convention.
- Browsers ignore extra spaces and blank lines.
- Use the `<pre>` element to preserve whitespace exactly as written.
- Always write clean, properly indented HTML for better readability and maintenance.