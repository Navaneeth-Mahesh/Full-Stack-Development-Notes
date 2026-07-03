# HTML Block and Inline Elements

Every HTML element has a **default display behavior**. Based on how elements are displayed in a webpage, they are classified into two main types:

* **Block Elements**
* **Inline Elements**

Understanding the difference between them is essential for writing clean, well-structured HTML.

> **Note:** These are the default display behaviors. CSS can change how an element is displayed using the `display` property (for example, `display: block;` or `display: inline;`).

---

# Block vs Inline at a Glance

```text
Block Element

+--------------------------------------+
| First Block                          |
+--------------------------------------+

+--------------------------------------+
| Second Block                         |
+--------------------------------------+

Each block starts on a new line.


Inline Elements

HTML CSS JavaScript

All inline elements stay on the same line.
```

---

# Block Elements

A **block element** always starts on a **new line** and, by default, takes up the **full width available**.

Think of a block element as a large rectangular box that occupies an entire row.

## Characteristics

* Starts on a new line.
* Takes up the full available width.
* Creates vertical spacing between elements.
* Mainly used to structure a webpage.
* Can usually contain inline elements and, depending on the element, other block elements.

---

## Example

```html
<h1>Main Heading</h1>

<p>This is a paragraph.</p>

<div>This is a div.</div>
```

**Output**

```text
Main Heading

This is a paragraph.

This is a div.
```

Each element starts on a new line.

---

# Common Block Elements

| Element        | Purpose                    |
| -------------- | -------------------------- |
| `<div>`        | Generic container          |
| `<h1>`–`<h6>`  | Headings                   |
| `<p>`          | Paragraph                  |
| `<header>`     | Page or section header     |
| `<main>`       | Main content               |
| `<section>`    | Groups related content     |
| `<article>`    | Independent content        |
| `<aside>`      | Sidebar or related content |
| `<footer>`     | Page or section footer     |
| `<nav>`        | Navigation links           |
| `<form>`       | Form container             |
| `<table>`      | Table                      |
| `<ul>`         | Unordered list             |
| `<ol>`         | Ordered list               |
| `<li>`         | List item                  |
| `<blockquote>` | Long quotation             |
| `<pre>`        | Preformatted text          |
| `<hr>`         | Thematic break             |

---

# Inline Elements

An **inline element** does **not** start on a new line.

It only takes up the width needed by its content.

Inline elements are commonly used to format text or insert small pieces of content inside block elements.

## Characteristics

* Stays on the same line.
* Takes only the required width.
* Used inside block elements.
* Usually contains text or other inline elements.
* Does not create a new line.

---

## Example

```html
<p>
    Learning <strong>HTML</strong> is
    <mark>fun</mark>.
</p>
```

**Output**

```text
Learning HTML is fun.
```

Notice that all inline elements remain on the same line.

---

# Common Inline Elements

| Element    | Purpose                  |
| ---------- | ------------------------ |
| `<span>`   | Generic inline container |
| `<a>`      | Hyperlink                |
| `<img>`    | Image                    |
| `<strong>` | Important text           |
| `<b>`      | Bold text                |
| `<em>`     | Emphasized text          |
| `<i>`      | Italic text              |
| `<mark>`   | Highlighted text         |
| `<small>`  | Small text               |
| `<sub>`    | Subscript                |
| `<sup>`    | Superscript              |
| `<del>`    | Deleted text             |
| `<ins>`    | Inserted text            |
| `<abbr>`   | Abbreviation             |
| `<cite>`   | Title of a creative work |
| `<q>`      | Short quotation          |
| `<code>`   | Inline code              |
| `<br>`     | Line break               |

---

# The `<div>` Element

The `<div>` element is the most commonly used **block-level container**.

It has **no visual appearance** by default and is mainly used to group HTML elements for styling and layout.

## Example

```html
<div>

    <h2>About Me</h2>

    <p>
        I am learning HTML.
    </p>

</div>
```

**Structure**

```text
+---------------------------+
| About Me                  |
|                           |
| I am learning HTML.       |
+---------------------------+
```

---

## Common Uses of `<div>`

* Group related content
* Create page layouts
* Apply CSS styles
* Build responsive designs
* Organize sections of a webpage

---

# The `<span>` Element

The `<span>` element is the most commonly used **inline container**.

It also has **no visual appearance** by default.

Unlike `<div>`, it is used for styling or grouping **small portions of text**.

## Example

```html
<p>
    My favorite color is
    <span style="color:red;">red</span>.
</p>
```

Only the word **red** is affected.

---

## Common Uses of `<span>`

* Color specific words
* Change font styles
* Highlight text
* Apply CSS classes
* Select text with JavaScript

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

**Output**

```text
Block Elements

First Div

Second Div

---------------------

Inline Elements

HTML CSS JavaScript
```

Notice:

* Each `<div>` starts on a new line.
* Each `<span>` stays on the same line.

---

# Visual Comparison

## Block Elements

```text
+-----------------------------+
| Block Element               |
+-----------------------------+

+-----------------------------+
| Another Block Element       |
+-----------------------------+
```

---

## Inline Elements

```text
HTML CSS JavaScript
```

---

# Difference Between `<div>` and `<span>`

| `<div>`                       | `<span>`                                 |
| ----------------------------- | ---------------------------------------- |
| Block element                 | Inline element                           |
| Starts on a new line          | Stays on the same line                   |
| Takes full width              | Takes only required width                |
| Used for layouts and sections | Used for styling small text              |
| Can contain many elements     | Usually contains text or inline elements |

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Block and Inline Elements</title>
</head>

<body>

    <h1>Block and Inline Elements</h1>

    <h2>Block Elements</h2>

    <div>This is the first div.</div>

    <div>This is the second div.</div>

    <p>This is a paragraph.</p>

    <hr>

    <h2>Inline Elements</h2>

    <p>
        Learning
        <strong>HTML</strong>,
        <mark>CSS</mark>,
        and
        <span style="color: blue;">JavaScript</span>
        is fun.
    </p>

    <p>
        Visit
        <a href="#">our website</a>
        for more information.
    </p>

</body>

</html>
```

---

# Complete List of Common Block Elements

| Element        | Purpose                                   |
| -------------- | ----------------------------------------- |
| `<address>`    | Contact information                       |
| `<article>`    | Independent content                       |
| `<aside>`      | Sidebar or related content                |
| `<blockquote>` | Long quotation                            |
| `<canvas>`     | Drawing graphics with JavaScript          |
| `<dd>`         | Description in a description list         |
| `<div>`        | Generic block container                   |
| `<dl>`         | Description list                          |
| `<dt>`         | Description term                          |
| `<fieldset>`   | Groups related form controls              |
| `<figcaption>` | Caption for a figure                      |
| `<figure>`     | Self-contained content                    |
| `<footer>`     | Footer section                            |
| `<form>`       | User input form                           |
| `<h1>`–`<h6>`  | Headings                                  |
| `<header>`     | Header section                            |
| `<hr>`         | Thematic break                            |
| `<li>`         | List item                                 |
| `<main>`       | Main content                              |
| `<nav>`        | Navigation links                          |
| `<noscript>`   | Content shown when JavaScript is disabled |
| `<ol>`         | Ordered list                              |
| `<p>`          | Paragraph                                 |
| `<pre>`        | Preformatted text                         |
| `<section>`    | Section of content                        |
| `<table>`      | Table                                     |
| `<tfoot>`      | Table footer                              |
| `<ul>`         | Unordered list                            |
| `<video>`      | Video player                              |

---

# Complete List of Common Inline Elements

| Element      | Purpose                      |
| ------------ | ---------------------------- |
| `<a>`        | Hyperlink                    |
| `<abbr>`     | Abbreviation                 |
| `<b>`        | Bold text                    |
| `<bdo>`      | Overrides text direction     |
| `<br>`       | Line break                   |
| `<button>`   | Clickable button             |
| `<cite>`     | Title of a creative work     |
| `<code>`     | Inline code                  |
| `<dfn>`      | Defines a term               |
| `<em>`       | Emphasized text              |
| `<i>`        | Italic text                  |
| `<img>`      | Displays an image            |
| `<input>`    | Input field                  |
| `<kbd>`      | Keyboard input               |
| `<label>`    | Label for a form control     |
| `<map>`      | Image map                    |
| `<object>`   | Embeds external content      |
| `<output>`   | Displays calculation results |
| `<q>`        | Short quotation              |
| `<samp>`     | Sample program output        |
| `<script>`   | JavaScript code              |
| `<select>`   | Drop-down list               |
| `<small>`    | Smaller text                 |
| `<span>`     | Generic inline container     |
| `<strong>`   | Important text               |
| `<sub>`      | Subscript                    |
| `<sup>`      | Superscript                  |
| `<textarea>` | Multi-line text input        |
| `<time>`     | Date or time                 |
| `<var>`      | Variable name                |

> **Deprecated Elements:** `<acronym>`, `<big>`, and `<tt>` are deprecated and should not be used in modern HTML. Use semantic alternatives such as `<abbr>` and CSS for styling.

---

# Common Beginner Mistakes

### ❌ Using `<span>` to create page sections

```html
<span>
    <h1>About</h1>
</span>
```

✔ Use a block element like `<div>` or `<section>`.

```html
<div>
    <h1>About</h1>
</div>
```

---

### ❌ Using `<div>` to style a single word

```html
<div style="color:red;">
    HTML
</div>
```

✔ Use `<span>`.

```html
<span style="color:red;">
    HTML
</span>
```

---

### ❌ Assuming every element is either block or inline forever

An element's default behavior can be changed with CSS.

```css
div {
    display: inline;
}

span {
    display: block;
}
```

However, it is generally best to keep the default behavior unless you have a specific design requirement.

---

# Summary

| Block Elements                                              | Inline Elements                                |
| ----------------------------------------------------------- | ---------------------------------------------- |
| Start on a new line                                         | Stay on the same line                          |
| Take up the full available width                            | Take only the required width                   |
| Used for page structure and layout                          | Used for formatting text and small content     |
| Can usually contain inline elements and some block elements | Usually contain text or other inline elements  |
| Examples: `<div>`, `<p>`, `<section>`, `<article>`          | Examples: `<span>`, `<a>`, `<strong>`, `<img>` |

---

# Key Points

* HTML elements are classified into **block** and **inline** elements based on their default display behavior.
* **Block elements** start on a new line and usually occupy the full available width.
* **Inline elements** stay on the same line and occupy only the space they need.
* `<div>` is the most commonly used **block-level container**.
* `<span>` is the most commonly used **inline container**.
* CSS can change an element's display behavior using the `display` property.
* Choosing the correct element improves **readability**, **accessibility**, **maintainability**, and **semantic HTML**.
