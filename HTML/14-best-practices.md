# HTML Best Practices

Writing clean and well-structured HTML makes your code easier to read, maintain, and optimize. Following best practices also improves accessibility, search engine optimization (SEO), and overall website performance.

---

# 1. Use Semantic HTML

Use semantic elements that describe the purpose of the content instead of generic `<div>` and `<span>` elements whenever possible.

### Good

```html
<header>
    <nav>...</nav>
</header>

<main>
    <article>
        <h1>Article Title</h1>
    </article>
</main>

<footer>
    Copyright © 2026
</footer>
```

### Avoid

```html
<div>
    <div>
        <div>Article Title</div>
    </div>
</div>
```

---

# 2. Use Proper Indentation

Indent nested elements consistently to improve readability.

### Good

```html
<body>
    <h1>Welcome</h1>

    <p>Hello World</p>
</body>
```

### Avoid

```html
<body>
<h1>Welcome</h1>
<p>Hello World</p>
</body>
```

---

# 3. Always Close Elements

Close all elements that require a closing tag.

### Good

```html
<p>This is a paragraph.</p>
```

### Avoid

```html
<p>This is a paragraph.
```

---

# 4. Use Lowercase Tag and Attribute Names

Although HTML is not case-sensitive, lowercase is the recommended convention.

### Good

```html
<img src="logo.png" alt="Logo">
```

### Avoid

```html
<IMG SRC="logo.png" ALT="Logo">
```

---

# 5. Always Use Quotes Around Attribute Values

Attribute values should always be enclosed in double quotes.

### Good

```html
<a href="about.html">About</a>
```

### Avoid

```html
<a href=about.html>About</a>
```

---

# 6. Add Meaningful `alt` Text to Images

Always describe the image for accessibility.

### Good

```html
<img src="team.jpg" alt="Development team meeting">
```

### Avoid

```html
<img src="team.jpg" alt="">
```

---

# 7. Use Descriptive File and Folder Names

Choose names that clearly describe the content.

### Good

```
images/
about.html
contact.html
style.css
```

### Avoid

```
img1.jpg
page1.html
abc.css
```

---

# 8. Keep CSS and JavaScript Separate

Store CSS and JavaScript in external files whenever possible.

### Good

```html
<link rel="stylesheet" href="style.css">

<script src="script.js"></script>
```

### Avoid

Using large amounts of inline CSS and JavaScript throughout the HTML document.

---

# 9. Use Comments Wisely

Use comments to explain complex sections of code.

### Example

```html
<!-- Navigation Bar -->

<nav>
    ...
</nav>
```

Avoid unnecessary comments that explain obvious code.

---

# 10. Write Accessible HTML

Accessibility helps everyone, including users who rely on assistive technologies.

Examples:

- Use descriptive link text.
- Use proper heading order (`<h1>` → `<h6>`).
- Add `alt` text to images.
- Associate labels with form inputs.
- Use semantic HTML elements.

### Good

```html
<a href="contact.html">Contact Us</a>
```

### Avoid

```html
<a href="contact.html">Click Here</a>
```

---

# 11. Optimize Images

Large images can slow down a website.

Best practices:

- Compress images before uploading.
- Use modern formats like **WebP** when possible.
- Resize images to the required dimensions.

---

# 12. Validate Your HTML

Validate your HTML to catch syntax errors and improve compatibility across browsers.

Common things to check:

- Missing closing tags
- Incorrect nesting
- Duplicate IDs
- Invalid attributes

---

# 13. Keep Your Code Organized

Group related sections together.

Example:

```html
<header>
    ...
</header>

<main>
    ...
</main>

<footer>
    ...
</footer>
```

Use blank lines between sections to improve readability.

---

# 14. Use Meaningful IDs and Classes

Choose names that describe the purpose of the element.

### Good

```html
<section id="about">

<button class="submit-btn">
```

### Avoid

```html
<section id="abc">

<button class="x1">
```

---

# 15. Keep HTML Simple

Avoid unnecessary nesting.

### Good

```html
<p>Welcome to my website.</p>
```

### Avoid

```html
<div>
    <div>
        <div>
            <p>Welcome to my website.</p>
        </div>
    </div>
</div>
```

---

# Example of Well-Structured HTML

```html
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
            <h2>About</h2>
            <p>Welcome to my website.</p>
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

# Summary

- Use semantic HTML elements whenever possible.
- Indent your code consistently.
- Close all required HTML elements.
- Write tags and attributes in lowercase.
- Always use quotes around attribute values.
- Add meaningful `alt` text to images.
- Use descriptive file, class, and ID names.
- Keep CSS and JavaScript in separate files.
- Write accessible and SEO-friendly HTML.
- Optimize images for faster loading.
- Validate your HTML regularly.
- Keep your code clean, organized, and easy to maintain.