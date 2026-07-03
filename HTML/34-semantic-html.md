# HTML Semantic Elements

Semantic elements are HTML tags that clearly describe **what the content means**, not just how it looks.

Instead of using generic containers like `<div>` and `<span>`, semantic HTML gives structure and meaning to a webpage.

---

# What is Semantic HTML?

Semantic HTML = HTML with meaning.

```text id="semantic-idea"
Non-semantic: <div> content </div>
Semantic:     <article> Blog Post </article>
```

* Browsers understand structure better
* Developers read code more easily
* Search engines understand content (SEO)
* Screen readers improve accessibility

---

# Why Semantic Elements Matter

* Improves SEO ranking
* Better accessibility for disabled users
* Cleaner and more readable code
* Easier maintenance
* Proper document structure

---

# Main Semantic Elements

| Element        | Purpose                          |
| -------------- | -------------------------------- |
| `<header>`     | Top section of page/section      |
| `<nav>`        | Navigation links                 |
| `<main>`       | Main content (only one per page) |
| `<section>`    | Group of related content         |
| `<article>`    | Independent content block        |
| `<aside>`      | Sidebar / related content        |
| `<footer>`     | Bottom section                   |
| `<figure>`     | Self-contained media/content     |
| `<figcaption>` | Caption for `<figure>`           |
| `<details>`    | Collapsible content              |
| `<summary>`    | Title for `<details>`            |
| `<mark>`       | Highlight text                   |
| `<time>`       | Date/time information            |

---

# 1. `<header>`

Top section of a webpage or section.

```html id="header"
<header>
    <h1>My Blog</h1>
</header>
```

---

# 2. `<nav>`

Navigation links area.

```html id="nav"
<nav>
    <a href="#">Home</a>
    <a href="#">Articles</a>
    <a href="#">Contact</a>
</nav>
```

---

# 3. `<main>`

Main content of the page.

```html id="main"
<main>
    <h2>Welcome</h2>
    <p>Main content goes here.</p>
</main>
```

### Rule:

* Only **one `<main>` per page**

---

# 4. `<section>`

Groups related content.

```html id="section"
<section>
    <h2>About</h2>
    <p>We build websites.</p>
</section>
```

---

# 5. `<article>`

Independent content block.

Used for:

* Blog posts
* News articles
* Cards

```html id="article"
<article>
    <h2>Learning HTML</h2>
    <p>HTML is the foundation of web development.</p>
</article>
```

---

# 6. `<aside>`

Side content related to main content.

Examples:

* Sidebar
* Ads
* Related links

```html id="aside"
<aside>
    <h3>Related Topics</h3>
    <ul>
        <li>CSS</li>
        <li>JavaScript</li>
    </ul>
</aside>
```

---

# 7. `<footer>`

Bottom section of the page.

```html id="footer"
<footer>
    <p>&copy; 2026 My Website</p>
</footer>
```

---

# 8. `<figure>` + `<figcaption>`

Used for images, diagrams, charts, or code blocks with captions.

```html id="figure"
<figure>
    <img src="html.png" alt="HTML Logo">
    <figcaption>HTML Logo</figcaption>
</figure>
```

---

# 9. `<details>` + `<summary>`

Creates expandable content.

```html id="details"
<details>
    <summary>What is HTML?</summary>
    <p>HTML stands for HyperText Markup Language.</p>
</details>
```

---

# 10. `<mark>` (Highlight Text)

Used to highlight important text.

```html id="mark"
<p>
    <mark>Semantic HTML improves accessibility.</mark>
</p>
```

---

# 11. `<time>` (Date & Time)

Represents dates and times in a machine-readable format.

```html id="time"
<time datetime="2026-07-03">July 3, 2026</time>
```

---

# Complete Semantic Layout Example

```html id="semantic-full"
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semantic HTML</title>
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

            <p>HTML is the foundation of web development.</p>

            <time datetime="2026-07-03">July 3, 2026</time>
        </article>

    </section>

    <aside>
        <h3>Related Topics</h3>
        <ul>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </aside>

    <figure>
        <img src="html.png" alt="HTML Logo">
        <figcaption>HTML Logo</figcaption>
    </figure>

    <details>
        <summary>What is HTML?</summary>
        <p>HTML stands for HyperText Markup Language.</p>
    </details>

    <p>
        <mark>Semantic HTML improves accessibility.</mark>
    </p>

</main>

<footer>
    <p>&copy; 2026 My Website</p>
</footer>

</body>

</html>
```

---

# Semantic vs Non-Semantic

| Semantic    | Non-Semantic      |
| ----------- | ----------------- |
| `<header>`  | `<div>`           |
| `<nav>`     | `<span>`          |
| `<main>`    | Generic container |
| `<section>` | No meaning        |
| `<article>` | No meaning        |
| `<footer>`  | No meaning        |

---

# Key Differences

### Semantic elements:

* Have meaning
* Improve SEO
* Improve accessibility

### Non-semantic elements:

* Only containers
* No meaning
* Used when no semantic tag fits

---

# Best Practices

✔ Always prefer semantic tags over `<div>`
✔ Use `<main>` only once
✔ Use `<article>` for independent content
✔ Use `<section>` for grouped content
✔ Use `<figure>` for images with captions
✔ Use `<time>` for dates
✔ Use `<mark>` only for highlighting important text

---

# Key Takeaway

Semantic HTML is about writing code that explains itself.

> Good HTML is not just what the browser displays, but what the code **means**.

---

