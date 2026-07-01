# Semantic HTML

Semantic HTML uses elements that clearly describe the purpose and meaning of the content they contain. Instead of using generic elements like `<div>` everywhere, semantic elements make the structure of a webpage easier to understand for developers, browsers, search engines, and assistive technologies.

---

# Why Use Semantic HTML?

Using semantic HTML provides several benefits:

- Improves code readability and maintainability.
- Helps search engines understand your webpage (SEO).
- Improves accessibility for screen readers.
- Creates a well-structured and meaningful webpage.
- Makes collaboration with other developers easier.

---

# Semantic vs Non-Semantic Elements

## Non-Semantic Elements

Non-semantic elements do not describe their content.

Examples:

```html
<div></div>
<span></span>
```

From these tags alone, it is impossible to know what kind of content they contain.

---

## Semantic Elements

Semantic elements clearly describe the type of content they contain.

Examples:

```html
<header></header>

<nav></nav>

<main></main>

<section></section>

<article></article>

<aside></aside>

<footer></footer>
```

---

# Common Semantic Elements

## `<header>`

Represents the introductory content of a webpage or a section.

It commonly contains:

- Logo
- Website title
- Navigation menu
- Search bar

### Example

```html
<header>
    <h1>My Portfolio</h1>
</header>
```

---

## `<nav>`

Represents a section containing navigation links.

### Example

```html
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
</nav>
```

---

## `<main>`

Represents the primary content of the webpage.

A webpage should contain only **one** `<main>` element.

### Example

```html
<main>
    <h2>Welcome</h2>
    <p>This is the main content.</p>
</main>
```

---

## `<section>`

Represents a thematic group of related content.

Examples:

- About section
- Services section
- Contact section

### Example

```html
<section>
    <h2>About Us</h2>
    <p>We build modern websites.</p>
</section>
```

---

## `<article>`

Represents independent, self-contained content.

Examples:

- Blog posts
- News articles
- Forum posts
- Product reviews

### Example

```html
<article>
    <h2>Learning HTML</h2>
    <p>HTML is the foundation of web development.</p>
</article>
```

---

## `<aside>`

Represents content that is related to the main content but is not essential.

Examples:

- Sidebar
- Advertisements
- Related articles
- Author information

### Example

```html
<aside>
    <h3>Related Articles</h3>
    <ul>
        <li>Introduction to CSS</li>
        <li>JavaScript Basics</li>
    </ul>
</aside>
```

---

## `<footer>`

Represents the footer of a webpage or a section.

It commonly contains:

- Copyright information
- Contact details
- Social media links
- Privacy policy
- Terms and conditions

### Example

```html
<footer>
    <p>&copy; 2026 My Website</p>
</footer>
```

---

## `<figure>` and `<figcaption>`

The `<figure>` element groups media content such as images, diagrams, or code snippets.

The `<figcaption>` element provides a caption for the content inside `<figure>`.

### Example

```html
<figure>
    <img src="mountain.jpg" alt="Mountain">
    <figcaption>Sunset over the mountains.</figcaption>
</figure>
```

---

## `<time>`

Represents a specific date or time.

### Example

```html
<p>
    Published on
    <time datetime="2026-07-01">
        July 1, 2026
    </time>
</p>
```

The `datetime` attribute provides a machine-readable date.

---

# Example Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Semantic HTML Example</title>
</head>

<body>

<header>
    <h1>My Blog</h1>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">Articles</a>
    <a href="#">Contact</a>
</nav>

<main>

    <section>

        <article>
            <h2>Learning HTML</h2>

            <p>HTML is the first language every web developer learns.</p>
        </article>

    </section>

    <aside>
        <h3>Related Posts</h3>
        <p>CSS Basics</p>
    </aside>

</main>

<footer>
    <p>&copy; 2026 My Blog</p>
</footer>

</body>
</html>
```

---

# Semantic HTML Layout

```text
+--------------------------------------------------+
|                  <header>                        |
+--------------------------------------------------+
|                    <nav>                         |
+--------------------------------------------------+
|                    <main>                        |
|  +-------------------------+  +---------------+  |
|  |      <section>          |  |    <aside>    |  |
|  |  +-------------------+  |  |               |  |
|  |  |    <article>      |  |  |               |  |
|  |  +-------------------+  |  |               |  |
|  +-------------------------+  +---------------+  |
+--------------------------------------------------+
|                  <footer>                        |
+--------------------------------------------------+
```

---

# Best Practices

- Use semantic elements whenever they accurately describe the content.
- Use only one `<main>` element per page.
- Use headings (`<h1>`–`<h6>`) to organize content logically.
- Avoid using `<div>` when a semantic element is more appropriate.
- Use `<article>` for standalone content and `<section>` for grouped related content.

---

# Summary

| Element | Purpose |
|----------|---------|
| `<header>` | Introductory content for a page or section |
| `<nav>` | Navigation links |
| `<main>` | Main content of the webpage |
| `<section>` | Groups related content |
| `<article>` | Independent, self-contained content |
| `<aside>` | Sidebar or supplementary content |
| `<footer>` | Footer information |
| `<figure>` | Groups media content |
| `<figcaption>` | Caption for a figure |
| `<time>` | Represents a date or time |
| `<div>` | Generic non-semantic container |
| `<span>` | Generic inline non-semantic container |