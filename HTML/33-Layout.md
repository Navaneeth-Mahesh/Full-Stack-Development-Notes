# HTML Layout

A webpage is usually divided into different sections such as a header, navigation bar, main content, sidebar, and footer. HTML5 provides **semantic layout elements** that make web pages easier to read, maintain, and understand.

> **Note:** HTML defines the structure of the layout, while CSS is used to control the appearance and positioning of these elements.

---

# Typical Webpage Layout

A basic webpage is commonly organized like this:

```text
+--------------------------------------+
|               Header                 |
+--------------------------------------+
| Navigation Menu                      |
+--------------------------------------+
|          Main Content                |
|  +-------------+  +---------------+  |
|  |   Section   |  |     Aside     |  |
|  +-------------+  +---------------+  |
+--------------------------------------+
|               Footer                 |
+--------------------------------------+
```

---

# HTML5 Layout Elements

HTML5 introduced semantic elements that clearly describe different parts of a webpage.

| Element | Description |
|---------|-------------|
| `<header>` | Defines the header of a webpage or section |
| `<nav>` | Contains navigation links |
| `<main>` | Represents the main content of the webpage |
| `<section>` | Represents a section of related content |
| `<article>` | Represents independent content such as a blog post or news article |
| `<aside>` | Contains content related to the main content, such as a sidebar |
| `<footer>` | Defines the footer of a webpage or section |
| `<details>` | Creates expandable and collapsible content |
| `<summary>` | Defines the visible heading for a `<details>` element |

---

# `<header>`

The `<header>` element represents introductory content for a webpage or a section.

Example:

```html
<header>
    <h1>My Website</h1>
    <p>Welcome to my website</p>
</header>
```

---

# `<nav>`

The `<nav>` element contains navigation links.

Example:

```html
<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Services</a>
    <a href="#">Contact</a>
</nav>
```

---

# `<main>`

The `<main>` element contains the primary content of the webpage.

Example:

```html
<main>
    <h2>Welcome</h2>

    <p>This is the main content of the webpage.</p>
</main>
```

> A webpage should contain only **one** `<main>` element.

---

# `<section>`

The `<section>` element groups related content together.

Example:

```html
<section>
    <h2>About Us</h2>

    <p>We build modern websites.</p>
</section>
```

---

# `<article>`

The `<article>` element represents independent, self-contained content.

Examples include:

- Blog posts
- News articles
- Product cards
- Forum posts

Example:

```html
<article>
    <h2>Learning HTML</h2>

    <p>HTML is the foundation of web development.</p>
</article>
```

---

# `<aside>`

The `<aside>` element contains content related to the main content.

Examples:

- Sidebar
- Advertisements
- Related links
- Author information

Example:

```html
<aside>
    <h3>Related Articles</h3>

    <ul>
        <li>Introduction to HTML</li>
        <li>Learning CSS</li>
    </ul>
</aside>
```

---

# `<footer>`

The `<footer>` element represents the bottom section of a webpage.

Example:

```html
<footer>
    <p>&copy; 2026 My Website</p>
</footer>
```

---

# `<details>` and `<summary>`

These elements create expandable and collapsible content.

Example:

```html
<details>

    <summary>What is HTML?</summary>

    <p>
        HTML stands for HyperText Markup Language.
    </p>

</details>
```

Output:

```
▶ What is HTML?
```

When clicked, the hidden content becomes visible.

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>HTML Layout</title>
</head>

<body>

    <header>
        <h1>My Website</h1>
    </header>

    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>

    <main>

        <section>

            <h2>About HTML</h2>

            <p>HTML is used to create webpages.</p>

        </section>

        <article>

            <h2>Latest Article</h2>

            <p>Semantic HTML improves accessibility.</p>

        </article>

        <aside>

            <h3>Related Links</h3>

            <ul>
                <li>HTML Basics</li>
                <li>CSS Basics</li>
            </ul>

        </aside>

    </main>

    <footer>

        <p>&copy; 2026 My Website</p>

    </footer>

</body>

</html>
```

---

# HTML Layout Techniques

HTML provides the structure of a webpage, while CSS is used to arrange the layout.

There are several techniques for creating webpage layouts.

## 1. CSS Frameworks

CSS frameworks provide pre-built components and layouts, allowing you to build websites quickly.

Popular frameworks include:

- Bootstrap
- Tailwind CSS
- Bulma
- Foundation

**Advantages**

- Faster development
- Responsive design
- Ready-made components

---

## 2. CSS Float

The `float` property was traditionally used to create multi-column layouts.

Example:

```css
.sidebar {
    float: left;
}

.content {
    float: right;
}
```

**Advantages**

- Easy to learn
- Supported by all browsers

**Disadvantages**

- Difficult to manage
- Not recommended for modern layouts

---

## 3. CSS Flexbox

Flexbox is designed for creating one-dimensional layouts (row or column).

Example:

```css
.container {
    display: flex;
}
```

**Advantages**

- Easy alignment
- Responsive
- Great for navigation bars and cards

---

## 4. CSS Grid

CSS Grid is designed for two-dimensional layouts (rows and columns).

Example:

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
}
```

**Advantages**

- Powerful layout system
- Ideal for complete webpage layouts
- Highly responsive

---

# Which Layout Technique Should You Use?

| Technique | Recommended |
|-----------|-------------|
| CSS Framework | Large projects and rapid development |
| CSS Float | Older websites (rarely used today) |
| CSS Flexbox | Navigation bars, cards, small layouts |
| CSS Grid | Complete webpage layouts and dashboards |

> **Modern Recommendation:** Use **Flexbox** for one-dimensional layouts and **CSS Grid** for complex two-dimensional layouts. Avoid using floats for new projects.

---

# Best Practices

- Use semantic HTML elements instead of multiple `<div>` elements.
- Keep only one `<main>` element per page.
- Use `<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, and `<footer>` appropriately.
- Use CSS Flexbox or CSS Grid for modern layouts.
- Keep the HTML structure clean and organized.

---

# Summary

| Element | Purpose |
|---------|---------|
| `<header>` | Header section |
| `<nav>` | Navigation links |
| `<main>` | Main webpage content |
| `<section>` | Groups related content |
| `<article>` | Independent content |
| `<aside>` | Sidebar or related content |
| `<footer>` | Footer section |
| `<details>` | Expandable content |
| `<summary>` | Heading for `<details>` |
| Flexbox | One-dimensional layouts |
| CSS Grid | Two-dimensional layouts |
| Float | Older layout technique |
| CSS Framework | Fast website development |