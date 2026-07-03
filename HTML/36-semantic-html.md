# HTML Semantic Elements

Semantic elements clearly describe the purpose of their content to both browsers and developers.

Unlike generic elements such as `<div>` and `<span>`, semantic elements provide meaningful structure to a webpage, making the code easier to read, maintain, and more accessible.

### Benefits of Semantic HTML

- Improves code readability.
- Helps search engines understand webpage content (SEO).
- Improves accessibility for screen readers.
- Makes websites easier to maintain.
- Creates a well-structured webpage.

---

# Common Semantic Elements

| Element | Description |
|---------|-------------|
| `<header>` | Defines the header of a webpage or section. |
| `<nav>` | Contains navigation links. |
| `<main>` | Represents the main content of the webpage. |
| `<section>` | Defines a thematic section of content. |
| `<article>` | Represents independent, self-contained content such as a blog post or news article. |
| `<aside>` | Contains content related to the main content, such as a sidebar. |
| `<footer>` | Defines the footer of a webpage or section. |
| `<figure>` | Represents self-contained content such as an image, diagram, chart, or code snippet. |
| `<figcaption>` | Provides a caption for a `<figure>` element. |
| `<details>` | Creates a section that users can expand or collapse. |
| `<summary>` | Defines the visible heading for a `<details>` element. |
| `<mark>` | Highlights or marks important text. |
| `<time>` | Represents a specific date, time, or duration. |

---

# Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Semantic HTML</title>
</head>

<body>

    <header>
        <h1>My Blog</h1>
    </header>

    <nav>
        <a href="#">Home</a> |
        <a href="#">Articles</a> |
        <a href="#">Contact</a>
    </nav>

    <main>

        <section>

            <article>
                <h2>Learning HTML</h2>

                <p>
                    HTML is the foundation of web development.
                </p>

                <time datetime="2026-07-03">
                    July 3, 2026
                </time>

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
            <img src="images/html.png" alt="HTML Logo">

            <figcaption>
                HTML Logo
            </figcaption>
        </figure>

        <details>

            <summary>What is HTML?</summary>

            <p>
                HTML stands for HyperText Markup Language.
            </p>

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

# Semantic vs Non-Semantic Elements

| Semantic Elements | Non-Semantic Elements |
|-------------------|-----------------------|
| `<header>` | `<div>` |
| `<nav>` | `<span>` |
| `<main>` | |
| `<section>` | |
| `<article>` | |
| `<aside>` | |
| `<footer>` | |

Semantic elements describe **what the content is**, while non-semantic elements only act as generic containers.

---

# Summary

- Semantic elements provide meaning to webpage content.
- They improve readability, accessibility, and SEO.
- Use semantic elements whenever possible instead of generic `<div>` elements.
- Semantic HTML makes your code easier to understand and maintain.