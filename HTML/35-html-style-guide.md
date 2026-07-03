# HTML Style Guide (Clean Beginner Notes)

A good HTML style guide helps you write **clean, readable, and maintainable code**. It also improves teamwork, SEO, accessibility, and reduces bugs.

---

# Why Style Matters

Clean HTML means:

* Easier to read
* Easier to debug
* Easier to maintain
* Better performance in teams
* Better accessibility and SEO

---

# 1. Always Start with DOCTYPE

```html id="doctype"
<!DOCTYPE html>
```

Tells the browser this is **HTML5**.

---

# 2. Basic HTML Structure

Every page must follow this structure:

```html id="structure"
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Page Title</title>
</head>

<body>

</body>

</html>
```

---

# 3. Always Add `lang`

```html id="lang"
<html lang="en">
```

### Why?

* Helps screen readers
* Improves SEO
* Helps browsers understand language

---

# 4. Essential Meta Tags

```html id="meta"
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Purpose:

| Tag      | Purpose                |
| -------- | ---------------------- |
| charset  | Supports all languages |
| viewport | Makes page responsive  |

---

# 5. Meaningful Title

```html id="title"
<title>HTML Style Guide</title>
```

Appears in:

* Browser tab
* Search results
* Bookmarks

---

# 6. Use Lowercase Tags

✔ Good:

```html id="lowercase-tags"
<p>Hello</p>
```

❌ Avoid:

```html id="uppercase-tags"
<P>Hello</P>
```

---

# 7. Lowercase Attributes

✔ Good:

```html id="attr-lower"
<a href="about.html">About</a>
```

❌ Avoid:

```html id="attr-bad"
<a HREF="about.html">About</a>
```

---

# 8. Always Quote Attributes

✔ Good:

```html id="quotes"
<img src="logo.png" alt="Logo">
```

❌ Avoid:

```html id="no-quotes"
<img src=logo.png>
```

---

# 9. Always Close Tags

✔ Good:

```html id="close-tags"
<p>Hello World</p>
```

---

# 10. Proper Indentation

```html id="indent"
<body>

    <h1>Title</h1>

    <p>Paragraph</p>

</body>
```

### Why?

* Easier to read
* Easier debugging

---

# 11. Use Blank Lines

```html id="spacing"
<header>
</header>

<main>
</main>

<footer>
</footer>
```

---

# 12. Avoid Long Lines

✔ Good:

```html id="long-lines"
<img
    src="logo.png"
    alt="Logo"
    width="200">
```

---

# 13. Always Add `alt` to Images

```html id="alt"
<img src="cat.jpg" alt="White cat sitting on chair">
```

### Why?

* Accessibility
* SEO
* Shows text if image fails

---

# 14. Define Image Size

```html id="img-size"
<img src="logo.png" alt="Logo" width="150" height="150">
```

### Why?

* Prevent layout shift
* Better performance

---

# 15. Use Meaningful File Names

✔ Good:

```
index.html
about.html
contact.html
```

❌ Avoid:

```
test1.html
abc.html
```

---

# 16. Use Lowercase File Names

✔ Good:

```
about.html
logo.png
```

❌ Avoid:

```
About.HTML
Logo.PNG
```

---

# 17. Use Comments Wisely

```html id="comment"
<!-- Navigation Menu -->
<nav></nav>
```

✔ Use comments only for important sections

---

# 18. External CSS

```html id="css"
<link rel="stylesheet" href="style.css">
```

### Benefits:

* Cleaner HTML
* Reusable styles
* Better maintenance

---

# 19. External JavaScript

```html id="js"
<script src="script.js"></script>
```

---

# 20. Use Semantic HTML

✔ Good:

```html id="semantic"
<header></header>
<nav></nav>
<main></main>
<footer></footer>
```

❌ Avoid:

```html id="non-semantic"
<div></div>
<div></div>
```

---

# 21. Descriptive Links

✔ Good:

```html id="link-good"
<a href="contact.html">Contact Us</a>
```

❌ Avoid:

```html id="link-bad"
<a href="contact.html">Click Here</a>
```

---

# 22. Organize Folder Structure

```text id="folder"
project/
│── index.html
│── about.html
│
├── css/
│   └── style.css
│
├── js/
│   └── script.js
│
└── images/
    ├── logo.png
    └── banner.jpg
```

---

# 23. Correct File Extensions

| Type  | Extension           |
| ----- | ------------------- |
| HTML  | .html               |
| CSS   | .css                |
| JS    | .js                 |
| Image | .png / .jpg / .webp |

---

# 24. Validate HTML

Before publishing:

* Check missing tags
* Check nesting
* Check attributes
* Test in browser

---

# Clean HTML Example

```html id="final-example"
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>My Website</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <header>
        <h1>My Website</h1>
    </header>

    <main>
        <section>
            <h2>Welcome</h2>

            <p>This is my first webpage.</p>

            <img src="images/logo.png" alt="Logo" width="150" height="150">
        </section>
    </main>

    <footer>
        <p>&copy; 2026 My Website</p>
    </footer>

    <script src="script.js"></script>

</body>

</html>
```

---

# Key Takeaways

* Always use proper HTML structure
* Keep code lowercase and consistent
* Use indentation and spacing
* Use semantic HTML
* Add alt text and metadata
* Separate CSS and JS into external files
* Use meaningful names everywhere
* Keep code clean and organized

---

# Final Idea

> Clean HTML is not about writing more code — it’s about writing **clear, structured, and meaningful code**.

---

If you want next step, I can:

* Combine ALL your files into a **full HTML Master Course (like a textbook)**
* Add **interview questions + quizzes + mini projects + roadmap**
