# Semantic HTML

Semantic HTML uses elements that clearly describe the purpose and meaning of the content they contain. Instead of using generic elements like `<div>`, semantic elements tell browsers, developers, search engines, and assistive technologies what each part of the webpage represents.

Think of semantic elements as **meaningful labels** for different sections of your webpage.

---

# Why Use Semantic HTML?

Using semantic HTML has many advantages:

* Makes code easier to read and maintain.
* Improves Search Engine Optimization (SEO).
* Makes websites more accessible for screen readers.
* Creates a well-structured webpage.
* Makes collaboration easier when working with other developers.
* Helps browsers better understand the page structure.

---

# Semantic vs Non-Semantic Elements

## Non-Semantic Elements

Non-semantic elements do **not** describe the content inside them.

Examples:

```html
<div></div>

<span></span>
```

Looking at these tags alone, you cannot determine what kind of content they contain.

They are mainly used for:

* Styling with CSS
* Manipulating elements with JavaScript
* Grouping content when no semantic element is appropriate

---

## Semantic Elements

Semantic elements clearly describe the purpose of the content they contain.

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

Just by reading these tags, you can understand the structure of the webpage.

---

# Semantic HTML Page Structure

A typical webpage is organized like this:

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

# Common Semantic Elements

## `<header>`

Represents the introductory content of a webpage or a section.

It commonly contains:

* Website logo
* Website title
* Navigation menu
* Search bar
* Introduction

### Example

```html
<header>
    <h1>My Portfolio</h1>
</header>
```

---

## `<nav>`

Represents a section that contains navigation links.

Usually placed near the top of the page.

### Example

```html
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/projects">Projects</a>
    <a href="/contact">Contact</a>
</nav>
```

---

## `<main>`

Represents the **main content** of the webpage.

Everything unique to the page should be inside `<main>`.

### Rules

* Only **one** `<main>` element should exist on a webpage.
* It should **not** be placed inside `<header>`, `<footer>`, `<nav>`, or `<aside>`.

### Example

```html
<main>
    <h2>Welcome</h2>
    <p>This is the primary content of the webpage.</p>
</main>
```

---

## `<section>`

Represents a group of related content.

Each section should usually have a heading.

Examples:

* About section
* Services section
* Contact section
* FAQ section

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

The content should make sense even if viewed separately.

Common examples:

* Blog posts
* News articles
* Forum posts
* User comments
* Product reviews

### Example

```html
<article>
    <h2>Learning HTML</h2>

    <p>HTML is the foundation of web development.</p>
</article>
```

---

## Difference Between `<section>` and `<article>`

Many beginners confuse these two elements.

| `<section>`                     | `<article>`                            |
| ------------------------------- | -------------------------------------- |
| Groups related content          | Contains independent content           |
| Depends on the surrounding page | Can stand alone                        |
| Organizes a webpage             | Represents a complete piece of content |

### Example

```html
<section>
    <h2>Latest Articles</h2>

    <article>
        <h3>Learning HTML</h3>
        <p>...</p>
    </article>

    <article>
        <h3>Learning CSS</h3>
        <p>...</p>
    </article>
</section>
```

Here:

* `<section>` groups related articles.
* Each `<article>` is an independent piece of content.

---

## `<aside>`

Represents content related to the main content but not essential.

Common examples:

* Sidebar
* Advertisements
* Related posts
* Author information
* Quick links

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

Commonly contains:

* Copyright
* Contact information
* Social media links
* Privacy Policy
* Terms & Conditions

### Example

```html
<footer>
    <p>&copy; 2026 My Website</p>
</footer>
```

---

## `<figure>` and `<figcaption>`

### `<figure>`

Groups media content such as:

* Images
* Diagrams
* Charts
* Code snippets

### `<figcaption>`

Provides a caption describing the content inside `<figure>`.

### Example

```html
<figure>
    <img src="mountain.jpg" alt="Mountain">

    <figcaption>
        Sunset over the mountains.
    </figcaption>
</figure>
```

---

## `<time>`

Represents a specific date or time.

The `datetime` attribute provides a machine-readable value for browsers and search engines.

### Example

```html
<p>
    Published on

    <time datetime="2026-07-01">
        July 1, 2026
    </time>
</p>
```

---

# Complete Example

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

                <p>
                    HTML is the first language every web developer learns.
                </p>

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

# When Should You Use `<div>`?

Use `<div>` **only when no semantic element fits the purpose.**

### Good Example

```html
<header>
    <h1>My Website</h1>
</header>
```

### Less Meaningful Example

```html
<div>
    <h1>My Website</h1>
</div>
```

The `<header>` version clearly tells everyone that this is the page header.

---

# Common Mistakes

### ❌ Using `<div>` for everything

```html
<div class="header"></div>
<div class="menu"></div>
<div class="content"></div>
<div class="footer"></div>
```

### ✅ Better

```html
<header></header>

<nav></nav>

<main></main>

<footer></footer>
```

---

### ❌ Multiple `<main>` elements

```html
<main>...</main>

<main>...</main>
```

### ✅ Correct

```html
<main>
    ...
</main>
```

Only one `<main>` should exist on a page.

---

### ❌ Using `<article>` for everything

Not every piece of content is an article.

If content is simply grouped together, use `<section>` instead.

---

# Best Practices

* Use semantic elements whenever they accurately describe the content.
* Keep headings (`<h1>`–`<h6>`) in a logical order.
* Use only one `<main>` element per page.
* Use `<article>` for standalone content.
* Use `<section>` to group related content.
* Use `<div>` only when no semantic element is suitable.
* Always provide meaningful `alt` text for images inside `<figure>`.
* Write clean, readable HTML with proper indentation.

---

# Quick Revision Table

| Element        | Purpose                  | Common Use                  |
| -------------- | ------------------------ | --------------------------- |
| `<header>`     | Introductory content     | Logo, title, navigation     |
| `<nav>`        | Navigation links         | Menus                       |
| `<main>`       | Main page content        | Primary webpage content     |
| `<section>`    | Groups related content   | About, Services, Contact    |
| `<article>`    | Independent content      | Blog posts, news, reviews   |
| `<aside>`      | Supplementary content    | Sidebar, related links, ads |
| `<footer>`     | Footer content           | Copyright, contact details  |
| `<figure>`     | Groups media             | Images, charts, diagrams    |
| `<figcaption>` | Caption for a figure     | Image description           |
| `<time>`       | Represents date or time  | Publish dates, events       |
| `<div>`        | Generic block container  | Layout and styling          |
| `<span>`       | Generic inline container | Styling inline text         |

---

# Key Points to Remember

* Semantic HTML gives **meaning** to your webpage.
* It improves **SEO**, **accessibility**, and **code readability**.
* Prefer semantic elements over generic `<div>` containers whenever possible.
* Use only one `<main>` element per page.
* Remember the rule:

  * **`<section>` = groups related content**
  * **`<article>` = independent content that can stand alone**
