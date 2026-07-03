# HTML Layout

A webpage is divided into multiple sections like header, navigation, content area, sidebar, and footer.

HTML5 provides **semantic elements** that clearly describe these sections, making the code easier to read, maintain, and understand.

---

# HTML vs CSS Role

* **HTML → Structure (layout skeleton)**
* **CSS → Design + positioning (visual layout)**

```text id="html-css-role"
HTML = skeleton of the page
CSS  = styling + layout design
```

---

# Typical Webpage Layout

```text id="layout-diagram"
+--------------------------------------+
|              HEADER                  |
+--------------------------------------+
| NAVIGATION                          |
+--------------------------------------+
| MAIN CONTENT        |  SIDEBAR      |
| (Articles/Sections) |  (Aside)      |
+--------------------------------------+
|              FOOTER                  |
+--------------------------------------+
```

---

# HTML5 Semantic Layout Elements

| Element     | Purpose                          |
| ----------- | -------------------------------- |
| `<header>`  | Top section of page or section   |
| `<nav>`     | Navigation links                 |
| `<main>`    | Main content (only one per page) |
| `<section>` | Group of related content         |
| `<article>` | Independent content (blog/news)  |
| `<aside>`   | Sidebar or related content       |
| `<footer>`  | Bottom section                   |
| `<details>` | Collapsible content              |
| `<summary>` | Visible title for `<details>`    |

---

# 1. `<header>`

Used for introductory content like logo, title, or heading.

```html id="header"
<header>
    <h1>My Website</h1>
    <p>Welcome to my site</p>
</header>
```

---

# 2. `<nav>`

Contains navigation links.

```html id="nav"
<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Services</a>
</nav>
```

---

# 3. `<main>`

Represents the main content of the page.

```html id="main"
<main>
    <h2>Welcome</h2>
    <p>Main content goes here.</p>
</main>
```

### Important Rule:

* Only **one `<main>` per page**

---

# 4. `<section>`

Used to group related content.

```html id="section"
<section>
    <h2>About Us</h2>
    <p>We build websites.</p>
</section>
```

---

# 5. `<article>`

Independent content block.

Examples:

* Blog post
* News article
* Product card

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
        <li>HTML Basics</li>
        <li>CSS Basics</li>
    </ul>
</aside>
```

---

# 7. `<footer>`

Bottom section of a webpage.

```html id="footer"
<footer>
    <p>&copy; 2026 My Website</p>
</footer>
```

---

# 8. `<details>` + `<summary>`

Used for expandable/collapsible content.

```html id="details"
<details>
    <summary>What is HTML?</summary>
    <p>HTML stands for HyperText Markup Language.</p>
</details>
```

### Behavior:

```text id="details-behavior"
▶ Click Summary
   ↓
Show hidden content
```

---

# Complete Example (Modern Layout)

```html id="full-layout"
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            <p>HTML is used to structure webpages.</p>
        </section>

        <article>
            <h2>Latest Post</h2>
            <p>Semantic HTML improves accessibility and SEO.</p>
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

# Layout Methods (CSS Side of Layout)

HTML only creates structure. CSS handles layout positioning.

---

## 1. CSS Frameworks

Examples:

* Bootstrap
* Tailwind CSS
* Bulma

### Pros:

* Fast development
* Responsive by default
* Prebuilt components

---

## 2. Float (Old Method)

```css id="float"
.sidebar {
    float: left;
}
```

### Problems:

* Hard to control
* Old approach
* Not recommended today

---

## 3. Flexbox (Modern 1D Layout)

Used for rows OR columns.

```css id="flexbox"
.container {
    display: flex;
}
```

### Best for:

* Navigation bars
* Cards
* Aligning items

---

## 4. CSS Grid (Modern 2D Layout)

Used for rows AND columns.

```css id="grid"
.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
}
```

### Best for:

* Full page layouts
* Dashboards
* Complex UI

---

# Flexbox vs Grid

| Feature    | Flexbox                | Grid                    |
| ---------- | ---------------------- | ----------------------- |
| Direction  | 1D (row OR column)     | 2D (row AND column)     |
| Best Use   | Navbar, buttons, cards | Page layout, dashboards |
| Complexity | Easy                   | Advanced but powerful   |

---

# Modern Recommendation

* Use **Flexbox → small layouts**
* Use **Grid → full page layouts**
* Avoid **float → outdated**

---

# Best Practices

✔ Use semantic tags instead of many `<div>`
✔ Use only one `<main>`
✔ Keep layout clean and readable
✔ Use Flexbox/Grid for positioning
✔ Separate structure (HTML) and design (CSS)
✔ Use semantic tags for SEO and accessibility

---

# Key Takeaways

* HTML defines structure, not design
* Semantic tags improve readability and SEO
* `<main>` should appear only once
* `<section>` groups related content
* `<article>` is independent content
* `<aside>` is side content
* Flexbox = 1D layout
* Grid = 2D layout
* Modern websites rely on Flexbox + Grid

---

If you send the next file, I can start merging everything into a **single “HTML Master Notes” document (like a full beginner course in one file)**.
