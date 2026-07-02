# HTML Block and Inline Elements

Every HTML element has a default display behavior. Based on this behavior, HTML elements are divided into two types:

- **Block Elements**
- **Inline Elements**

Understanding the difference between them is important for creating well-structured web pages.

---

# Block Elements

A **block element** always starts on a new line and takes up the full width available by default.

Characteristics:

- Starts on a new line.
- Occupies the full available width.
- Can contain both block and inline elements (depending on the element).
- Commonly used to structure a webpage.

### Example

```html
<h1>Main Heading</h1>

<p>This is a paragraph.</p>

<div>This is a div.</div>
```

**Output:**

```
Main Heading

This is a paragraph.

This is a div.
```

Notice that each element appears on a new line.

---

# Common Block Elements

| Element | Purpose |
|----------|---------|
| `<div>` | Generic container |
| `<h1>` to `<h6>` | Headings |
| `<p>` | Paragraph |
| `<header>` | Page or section header |
| `<main>` | Main content |
| `<section>` | Section of content |
| `<article>` | Independent content |
| `<aside>` | Sidebar content |
| `<footer>` | Page or section footer |
| `<nav>` | Navigation links |
| `<form>` | Form container |
| `<table>` | Table |
| `<ul>` | Unordered list |
| `<ol>` | Ordered list |
| `<li>` | List item |
| `<blockquote>` | Long quotation |
| `<pre>` | Preformatted text |
| `<hr>` | Horizontal line |

---

# Inline Elements

An **inline element** does **not** start on a new line. It only takes up as much width as necessary.

Characteristics:

- Does not start on a new line.
- Takes only the required width.
- Usually used inside block elements.
- Cannot normally contain block elements.

### Example

```html
<p>
    Learning <strong>HTML</strong> is
    <mark>fun</mark>.
</p>
```

**Output:**

```
Learning HTML is fun.
```

All the inline elements remain on the same line.

---

# Common Inline Elements

| Element | Purpose |
|----------|---------|
| `<span>` | Generic inline container |
| `<a>` | Hyperlink |
| `<img>` | Image |
| `<strong>` | Important text |
| `<b>` | Bold text |
| `<em>` | Emphasized text |
| `<i>` | Italic text |
| `<mark>` | Highlighted text |
| `<small>` | Small text |
| `<sub>` | Subscript |
| `<sup>` | Superscript |
| `<del>` | Deleted text |
| `<ins>` | Inserted text |
| `<abbr>` | Abbreviation |
| `<cite>` | Citation |
| `<q>` | Short quotation |
| `<br>` | Line break |

---

# The `<div>` Element

The `<div>` element is a **block-level** container used to group other HTML elements.

It has no visual appearance by default and is commonly used for layout and styling with CSS.

### Example

```html
<div>
    <h2>About Me</h2>
    <p>I am learning HTML.</p>
</div>
```

---

# The `<span>` Element

The `<span>` element is an **inline** container used to group or style a small portion of text.

It also has no visual appearance by default.

### Example

```html
<p>
    My favorite color is
    <span style="color:red;">red</span>.
</p>
```

---

# Block vs Inline Example

```html
<h2>Block Elements</h2>

<div>First Div</div>

<div>Second Div</div>

<hr>

<h2>Inline Elements</h2>

<span>HTML</span>
<span>CSS</span>
<span>JavaScript</span>
```

**Output:**

```
Block Elements

First Div

Second Div

-------------------

Inline Elements

HTML CSS JavaScript
```

Notice that:

- Each `<div>` starts on a new line.
- Each `<span>` stays on the same line.

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Block and Inline Elements</title>
</head>

<body>

    <h1>Block and Inline Elements</h1>

    <!-- Block Elements -->
    <h2>Block Elements</h2>

    <div>This is the first div.</div>

    <div>This is the second div.</div>

    <p>This is a paragraph.</p>

    <hr>

    <!-- Inline Elements -->
    <h2>Inline Elements</h2>

    <p>
        Learning
        <strong>HTML</strong>,
        <mark>CSS</mark>,
        and
        <span style="color:blue;">JavaScript</span>
        is fun.
    </p>

    <a href="#">Click Here</a>

    <img
        src="images/html.png"
        alt="HTML Logo"
        width="60">

</body>

</html>
```

---

# Summary

| Block Elements | Inline Elements |
|----------------|-----------------|
| Start on a new line | Stay on the same line |
| Take up the full available width | Take only the required width |
| Used for page structure and layout | Used for formatting or small pieces of content |
| Examples: `<div>`, `<p>`, `<h1>`, `<section>` | Examples: `<span>`, `<a>`, `<strong>`, `<img>` |

---

# Key Points

- **Block elements** start on a new line and take up the full available width.
- **Inline elements** stay on the same line and only take up the space they need.
- `<div>` is the most commonly used **block-level container**.
- `<span>` is the most commonly used **inline container**.
- Choosing the correct type of element helps create clean, semantic, and maintainable HTML.

Here are the block-level elements in HTML:
| Element        | Purpose                                           |
| -------------- | ------------------------------------------------- |
| `<address>`    | Contact information for the author or owner       |
| `<article>`    | Independent, self-contained content               |
| `<aside>`      | Sidebar or related content                        |
| `<blockquote>` | Long quotation from another source                |
| `<canvas>`     | Drawing graphics using JavaScript                 |
| `<dd>`         | Description/details in a description list         |
| `<div>`        | Generic block-level container                     |
| `<dl>`         | Description list                                  |
| `<dt>`         | Term in a description list                        |
| `<fieldset>`   | Groups related form elements                      |
| `<figcaption>` | Caption for a `<figure>` element                  |
| `<figure>`     | Self-contained content such as images or diagrams |
| `<footer>`     | Footer for a page or section                      |
| `<form>`       | Form for collecting user input                    |
| `<h1>`–`<h6>`  | Headings (largest to smallest)                    |
| `<header>`     | Header for a page or section                      |
| `<hr>`         | Horizontal thematic break                         |
| `<li>`         | List item inside `<ul>` or `<ol>`                 |
| `<main>`       | Main content of the document                      |
| `<nav>`        | Navigation links                                  |
| `<noscript>`   | Content shown when JavaScript is disabled         |
| `<ol>`         | Ordered (numbered) list                           |
| `<p>`          | Paragraph                                         |
| `<pre>`        | Preformatted text                                 |
| `<section>`    | Thematic section of content                       |
| `<table>`      | Table                                             |
| `<tfoot>`      | Footer section of a table                         |
| `<ul>`         | Unordered (bulleted) list                         |
| `<video>`      | Embeds a video                                    |


Here are the inline elements in HTML:

| Element      | Purpose                        |
| ------------ | ------------------------------ |
| `<a>`        | Hyperlink                      |
| `<abbr>`     | Abbreviation or acronym        |
| `<acronym>`  | Acronym (**Deprecated**)       |
| `<b>`        | Bold text                      |
| `<bdo>`      | Overrides text direction       |
| `<big>`      | Larger text (**Deprecated**)   |
| `<br>`       | Line break                     |
| `<button>`   | Clickable button               |
| `<cite>`     | Title of a creative work       |
| `<code>`     | Inline code snippet            |
| `<dfn>`      | Defines a term                 |
| `<em>`       | Emphasized text                |
| `<i>`        | Italic text                    |
| `<img>`      | Displays an image              |
| `<input>`    | User input field               |
| `<kbd>`      | Keyboard input                 |
| `<label>`    | Label for a form control       |
| `<map>`      | Image map                      |
| `<object>`   | Embeds external resources      |
| `<output>`   | Result of a calculation        |
| `<q>`        | Short quotation                |
| `<samp>`     | Sample program output          |
| `<script>`   | JavaScript code                |
| `<select>`   | Drop-down list                 |
| `<small>`    | Smaller text                   |
| `<span>`     | Generic inline container       |
| `<strong>`   | Important text                 |
| `<sub>`      | Subscript text                 |
| `<sup>`      | Superscript text               |
| `<textarea>` | Multi-line text input          |
| `<time>`     | Represents a date or time      |
| `<tt>`       | Teletype text (**Deprecated**) |
| `<var>`      | Variable name                  |
