# HTML Comments

HTML comments are used to add notes, explanations, or reminders within the source code. Comments are **ignored by the browser**, meaning they are not displayed on the webpage.

Comments make your code easier to read, understand, and maintain, especially when working on large projects or collaborating with others.

---

# Syntax

HTML comments start with `<!--` and end with `-->`.

```html
<!-- This is a comment -->
```

---

# Single-Line Comment

A single-line comment is written on one line.

### Example

```html
<!-- This is a heading -->
<h1>Welcome to My Website</h1>
```

---

# Multi-Line Comment

Comments can span multiple lines.

### Example

```html
<!--
This website is created
for learning HTML.
-->
```

---

# Commenting Out HTML Code

You can temporarily disable HTML code without deleting it by wrapping it inside a comment.

### Example

```html
<!--
<p>This paragraph will not be displayed.</p>
-->
```

This is useful for:

- Testing code
- Debugging
- Temporarily removing elements

---

# Commenting Multiple Elements

You can comment out multiple HTML elements at once.

### Example

```html
<!--
<h1>Welcome</h1>

<p>This paragraph is hidden.</p>

<img src="logo.png" alt="Logo">
-->
```

---

# Adding Section Labels

Comments can be used to separate different sections of your HTML document.

### Example

```html
<!-- Header -->
<header>
    ...
</header>

<!-- Navigation -->
<nav>
    ...
</nav>

<!-- Main Content -->
<main>
    ...
</main>

<!-- Footer -->
<footer>
    ...
</footer>
```

This makes large HTML files easier to navigate.

---

# Comments Inside HTML

Comments can be placed almost anywhere in an HTML document.

### Example

```html
<body>

    <!-- Website Heading -->
    <h1>My Website</h1>

    <!-- Introduction -->
    <p>Welcome to my webpage.</p>

</body>
```

---

# Rules for HTML Comments

- Comments are ignored by the browser.
- Comments are visible in the page source, so **do not store passwords, API keys, or sensitive information inside comments**.
- Comments can improve code readability and maintenance.
- Comments cannot be nested.

### Incorrect Example

```html
<!--
Outer Comment

<!-- Inner Comment -->

-->
```

Nested comments are invalid and may produce unexpected results.

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Comments</title>
</head>
<body>

    <!-- Website Header -->
    <h1>Learning HTML</h1>

    <!-- Introduction -->
    <p>This is a sample webpage.</p>

    <!--
    <p>This paragraph is hidden.</p>
    -->

    <!-- Footer -->
    <footer>
        Copyright © 2026
    </footer>

</body>
</html>
```

---

# Best Practices

- Use comments to explain complex sections of code.
- Add comments to divide large HTML documents into logical sections.
- Keep comments short, clear, and meaningful.
- Remove unnecessary comments before publishing a website.
- Never include confidential information in comments.

---

# Summary

| Syntax | Purpose |
|--------|---------|
| `<!-- Comment -->` | Adds a comment that is ignored by the browser |
| Single-line comment | Explains a single line of code |
| Multi-line comment | Explains larger sections of code |
| Commented-out code | Temporarily disables HTML code without deleting it |