# HTML Comments

HTML comments are used to add notes inside your code. These comments are ignored by the browser, meaning they will not appear on the webpage.

They are mainly used to:
- Explain code
- Organize sections
- Help developers understand the structure
- Temporarily disable code

---

# Syntax of HTML Comments

```html
<!-- This is a comment -->
```

Anything written inside `<!-- -->` is treated as a comment.

---

# Basic Example

```html
<p>This is visible text.</p>

<!-- This is a comment and will not be shown in the browser -->

<p>This is another visible text.</p>
```

---

# Using Comments for Organization

Comments help divide your code into sections.

### Example

```html
<!-- Header Section -->
<header>
    <h1>My Website</h1>
</header>

<!-- Main Content Section -->
<main>
    <p>Welcome to my website.</p>
</main>

<!-- Footer Section -->
<footer>
    <p>Copyright © 2026</p>
</footer>
```

---

# Commenting Out Code

You can disable code temporarily by wrapping it inside comments.

### Example

```html
<!--
<p>This paragraph is disabled and will not show on the page.</p>
-->
```

---

# Single-Line Comment

HTML does not have a separate syntax for single-line comments. You simply write:

```html
<!-- This is a single-line comment -->
```

---

# Multi-Line Comment

You can write comments across multiple lines.

### Example

```html
<!--
This is a multi-line comment.
It can span multiple lines.
Used for longer explanations.
-->
```

---

# Important Rules

- Comments cannot be nested inside other comments.
- Avoid putting sensitive information inside comments.
- Comments do not affect how the webpage is displayed.
- Use comments to make code easier to read, not clutter it.

---

# Good Practice Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>Comments Example</title>
</head>

<body>

    <!-- Main Heading -->
    <h1>Welcome</h1>

    <!-- Intro Paragraph -->
    <p>This is a simple HTML page.</p>

    <!-- Button Section -->
    <button>Click Me</button>

</body>
</html>
```

---

# Summary

- HTML comments are written using `<!-- -->`
- They are not displayed in the browser
- Used for explanations, organization, and debugging
- Can be single-line or multi-line
- Cannot be nested inside each other