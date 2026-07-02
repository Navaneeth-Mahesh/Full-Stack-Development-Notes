# Headings and Paragraphs in HTML

Headings and paragraphs are the most basic building blocks of any webpage. They are used to structure and display text content in a clear and readable way.

---

# Headings in HTML

HTML provides six levels of headings from `<h1>` to `<h6>`.

## Syntax

```html
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<h3>Section Heading</h3>
<h4>Smaller Heading</h4>
<h5>Very Small Heading</h5>
<h6>Smallest Heading</h6>
```

---

## Heading Levels Explained

| Tag | Size | Use |
|------|------|-----|
| `<h1>` | Largest | Main title of the page |
| `<h2>` | Large | Major section heading |
| `<h3>` | Medium | Sub-section heading |
| `<h4>` | Small | Smaller section |
| `<h5>` | Very small | Minor heading |
| `<h6>` | Smallest | Least important heading |

---

## Example

```html
<h1>Welcome to My Website</h1>
<h2>About Me</h2>
<h3>Skills</h3>
<h4>Frontend Development</h4>
<h5>HTML Basics</h5>
<h6>Notes Section</h6>
```

---

## Important Rules for Headings

- `<h1>` should be used only once per page (recommended for SEO and structure)
- Headings should be used in proper order (don’t skip levels randomly)
- Use headings for structure, not for styling

### Good Example

```html
<h1>Blog Title</h1>
<h2>Introduction</h2>
<h2>Content</h2>
<h3>Details</h3>
```

### Bad Example

```html
<h4>Main Title</h4>
<h1>Sub Title</h1>
```

---

# Paragraphs in HTML

The `<p>` tag is used to define paragraphs of text.

---

## Syntax

```html
<p>This is a paragraph.</p>
```

---

## Example

```html
<p>
    HTML is used to create web pages.
</p>

<p>
    It defines the structure of a webpage using elements.
</p>
```

---

## Features of Paragraphs

- Automatically adds space before and after text
- Helps organize content into readable blocks
- Supports inline elements like `<b>`, `<i>`, `<a>`, etc.

---

## Paragraph with Formatting

```html
<p>
    This is <b>bold</b>, this is <i>italic</i>, and this is a <a href="#">link</a>.
</p>
```

---

# Line Break Inside Paragraphs

HTML ignores extra spaces and line breaks inside `<p>`.

To force a line break, use `<br>`.

## Example

```html
<p>
    Hello<br>
    Welcome to HTML<br>
    Enjoy learning
</p>
```

---

# Horizontal Line

The `<hr>` tag is used to separate content visually.

## Example

```html
<h1>Section 1</h1>
<p>This is content.</p>

<hr>

<h1>Section 2</h1>
<p>This is new content.</p>
```

---

# Difference Between Headings and Paragraphs

| Feature | Headings (`h1`–`h6`) | Paragraph (`p`) |
|----------|---------------------|-----------------|
| Purpose | Titles and structure | Normal text content |
| Importance | High | Normal |
| Size | Large to small | Regular text |
| Usage | Organize content | Write content |

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Headings and Paragraphs</title>
</head>

<body>

    <h1>My Website</h1>

    <h2>About This Page</h2>
    <p>
        This webpage is created to learn HTML headings and paragraphs.
    </p>

    <h2>Content Section</h2>
    <p>
        HTML uses tags to structure content on a webpage.
        It is the foundation of web development.
    </p>

    <h3>Important Note</h3>
    <p>
        Always use headings in proper order and keep paragraphs simple and readable.
    </p>

</body>

</html>
```

---

# Summary

- Headings are used for titles and structure (`h1` to `h6`)
- `<h1>` is the most important, `<h6>` is the least
- Paragraphs are used for normal text content
- `<p>` automatically adds spacing around text
- `<br>` is used for line breaks
- `<hr>` is used to separate sections visually
- Proper use of headings improves readability and SEO