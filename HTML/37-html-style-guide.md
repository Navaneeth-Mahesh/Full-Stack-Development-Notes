# HTML Style Guide

Writing clean and consistent HTML makes your code easier to read, understand, debug, and maintain. Following a style guide also improves teamwork, accessibility, SEO, and browser compatibility.

---

# 1. Always Declare the Document Type

Every HTML document should begin with the HTML5 document declaration.

### Good

```html
<!DOCTYPE html>
```

This tells the browser that the document is written in HTML5.

---

# 2. Always Include the Basic HTML Structure

Every HTML page should contain the following elements:

- `<!DOCTYPE html>`
- `<html>`
- `<head>`
- `<body>`

### Good

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>My Website</title>
</head>

<body>

</body>

</html>
```

---

# 3. Specify the Language

Always include the `lang` attribute inside the `<html>` tag.

### Good

```html
<html lang="en">
```

Benefits:

- Improves accessibility.
- Helps search engines understand the page language.
- Assists browsers and screen readers.

---

# 4. Add Essential Meta Tags

Every webpage should include these meta tags.

```html
<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">
```

### Why?

- `charset="UTF-8"` supports most languages and symbols.
- `viewport` makes the webpage responsive on all devices.

---

# 5. Always Include a Meaningful Title

Every webpage should have a descriptive title.

### Good

```html
<title>HTML Style Guide</title>
```

The title appears:

- Browser tab
- Bookmarks
- Search engine results

---

# 6. Use Lowercase Tag Names

HTML is not case-sensitive, but lowercase is the standard convention.

### Good

```html
<body>

<p>Hello World</p>

</body>
```

### Avoid

```html
<BODY>

<P>Hello World</P>

</BODY>
```

---

# 7. Use Lowercase Attribute Names

Write attribute names in lowercase.

### Good

```html
<a href="about.html">
```

### Avoid

```html
<a HREF="about.html">
```

---

# 8. Always Quote Attribute Values

Always surround attribute values with double quotes.

### Good

```html
<img src="logo.png" alt="Logo">
```

### Avoid

```html
<img src=logo.png>
```

---

# 9. Close HTML Elements

Although some HTML elements don't require closing tags, it is good practice to close every element that can be closed.

### Good

```html
<p>This is a paragraph.</p>
```

### Avoid

```html
<p>This is a paragraph.
```

---

# 10. Use Proper Indentation

Indent nested elements consistently.

### Good

```html
<body>

    <h1>Welcome</h1>

    <p>Hello World</p>

</body>
```

Good indentation makes code easier to read.

---

# 11. Use Blank Lines Between Sections

Separate different sections of your HTML using blank lines.

### Good

```html
<header>
</header>

<main>
</main>

<footer>
</footer>
```

This improves readability.

---

# 12. Avoid Very Long Lines

Break long lines into multiple lines.

### Good

```html
<img
    src="logo.png"
    alt="Company Logo"
    width="200">
```

Instead of:

```html
<img src="logo.png" alt="Company Logo" width="200">
```

Breaking long lines makes code easier to read.

---

# 13. Always Add the `alt` Attribute to Images

Every image should include meaningful alternative text.

### Good

```html
<img
    src="cat.jpg"
    alt="White cat sitting on a chair">
```

Benefits:

- Accessibility
- SEO
- Displays text if the image fails to load

---

# 14. Specify Image Width and Height

Whenever possible, define image dimensions.

### Good

```html
<img
    src="logo.png"
    alt="Logo"
    width="150"
    height="150">
```

This helps browsers reserve space before the image loads.

---

# 15. Use Meaningful File Names

Choose descriptive names.

### Good

```
index.html
about.html
contact.html
style.css
script.js
logo.png
```

### Avoid

```
abc.html
test1.css
img1.png
```

---

# 16. Use Lowercase File Names

Always use lowercase file names.

### Good

```
about.html

contact.html

profile.jpg
```

### Avoid

```
About.HTML

Profile.JPG
```

Some web servers treat uppercase and lowercase file names differently.

---

# 17. Use Comments to Explain Code

Write comments for important sections.

### Example

```html
<!-- Navigation Bar -->

<nav>

</nav>
```

Avoid unnecessary comments that explain obvious code.

---

# 18. Keep CSS in External Files

Instead of inline styles, place CSS in a separate file.

### Good

```html
<link
    rel="stylesheet"
    href="style.css">
```

Benefits:

- Easier maintenance
- Cleaner HTML
- Reusable styles

---

# 19. Keep JavaScript in External Files

Load JavaScript from a separate file.

### Good

```html
<script src="script.js"></script>
```

Benefits:

- Cleaner HTML
- Better organization
- Easier debugging

---

# 20. Use Semantic HTML

Prefer semantic elements instead of generic `<div>` elements.

### Good

```html
<header>

<nav>

<main>

<section>

<article>

<footer>
```

Semantic HTML improves:

- Accessibility
- SEO
- Code readability

---

# 21. Write Descriptive Link Text

Avoid generic text like "Click Here."

### Good

```html
<a href="contact.html">
    Contact Us
</a>
```

### Avoid

```html
<a href="contact.html">
    Click Here
</a>
```

---

# 22. Keep Folder Structure Organized

Example project structure:

```
project/

│── index.html

│── about.html

│── css/
│     └── style.css

│── js/
│     └── script.js

│── images/
│     ├── logo.png
│     └── banner.jpg
```

A good folder structure makes projects easier to manage.

---

# 23. Use the Correct File Extensions

Use standard file extensions.

| File Type | Extension |
|-----------|-----------|
| HTML | `.html` |
| CSS | `.css` |
| JavaScript | `.js` |
| Image | `.png`, `.jpg`, `.svg`, `.webp` |

---

# 24. Validate Your HTML

Before publishing your website:

- Check for missing tags.
- Check for invalid nesting.
- Verify attributes.
- Ensure proper indentation.
- Test in multiple browsers.

---

# Example of Clean HTML

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

    <title>My Website</title>

    <link
        rel="stylesheet"
        href="style.css">
</head>

<body>

    <header>
        <h1>My Website</h1>
    </header>

    <main>
        <section>
            <h2>Welcome</h2>

            <p>This is my first webpage.</p>

            <img
                src="images/logo.png"
                alt="Website Logo"
                width="150"
                height="150">
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

- Always declare `<!DOCTYPE html>`.
- Include `<html>`, `<head>`, and `<body>`.
- Specify the `lang` attribute.
- Add `charset` and `viewport` meta tags.
- Use lowercase tags, attributes, and file names.
- Always quote attribute values.
- Close HTML elements properly.
- Indent code consistently.
- Use blank lines to separate sections.
- Add meaningful `title` and `alt` attributes.
- Specify image dimensions.
- Organize CSS and JavaScript into external files.
- Use semantic HTML elements.
- Write descriptive file names and link text.
- Keep your project folder organized.
- Validate your HTML before deployment.