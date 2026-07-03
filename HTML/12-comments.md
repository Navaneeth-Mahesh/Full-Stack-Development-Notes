# HTML Comments

HTML comments are used to add **notes, explanations, reminders, or labels** inside your HTML code. They are **ignored by the browser**, so they are **not displayed** on the webpage.

Comments help make your code easier to read, understand, and maintain, especially when working on large projects or with a team.

---

# Why Use Comments?

Comments are useful for:

* Explaining complex code
* Organizing different sections of a webpage
* Leaving reminders for yourself or teammates
* Temporarily disabling code for testing or debugging
* Making large HTML files easier to navigate

---

# Syntax

HTML comments begin with `<!--` and end with `-->`.

```html
<!-- This is a comment -->
```

Anything written between `<!--` and `-->` is treated as a comment and is ignored by the browser.

---

# How Comments Work

```text
HTML File
     │
     ▼
Browser reads HTML
     │
     ├── Normal HTML → Displayed
     │
     └── Comments → Ignored
```

---

# Single-Line Comment

A single-line comment is written on one line.

### Example

```html
<!-- Website Heading -->
<h1>Welcome to My Website</h1>
```

The comment is only visible in the source code.

---

# Multi-Line Comment

Comments can span multiple lines.

### Example

```html
<!--
This website was created
to practice HTML.
-->
```

Use multi-line comments when you need to write longer explanations.

---

# Commenting Out HTML Code

You can temporarily disable HTML code without deleting it.

### Example

```html
<!--
<p>This paragraph will not be displayed.</p>
-->
```

### Common Uses

* Testing different layouts
* Debugging problems
* Temporarily hiding elements
* Keeping code for future use

---

# Commenting Multiple Elements

You can comment out several HTML elements at the same time.

### Example

```html
<!--
<h1>Welcome</h1>

<p>This paragraph is hidden.</p>

<img src="logo.png" alt="Logo">
-->
```

Everything inside the comment is ignored by the browser.

---

# Organizing Your HTML with Comments

Comments are often used as section labels to make HTML easier to read.

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

<!-- Sidebar -->
<aside>
    ...
</aside>

<!-- Footer -->
<footer>
    ...
</footer>
```

This makes large HTML files much easier to navigate.

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

    <!-- Main Content -->
    <main>
        <p>Learning HTML is fun!</p>
    </main>

</body>
```

---

# Browser View vs Source Code

### HTML Code

```html
<!-- This comment is hidden -->

<h1>Hello World</h1>

<p>Welcome!</p>
```

### What the Browser Displays

```text
Hello World

Welcome!
```

The comment is completely ignored.

---

# Rules for HTML Comments

### 1. Comments are ignored by the browser

```html
<!-- This won't appear on the webpage -->
```

---

### 2. Comments are visible in the page source

Anyone can view comments by opening the page source in their browser.

**Never store:**

* Passwords
* API keys
* Secret tokens
* Personal information
* Database credentials

❌ Bad Example

```html
<!-- API Key: abc123xyz -->
```

---

### 3. Comments Cannot Be Nested

Nested comments are **invalid HTML**.

❌ Incorrect

```html
<!--
Outer Comment

<!-- Inner Comment -->

-->
```

The browser may interpret this incorrectly.

---

### 4. Comments Do Not Affect the Layout

Adding comments does not change how the webpage looks.

```html
<!-- Logo -->
<img src="logo.png" alt="Logo">

<!-- Navigation -->
<nav>...</nav>
```

---

# Common Mistakes

## Forgetting to Close a Comment

❌ Incorrect

```html
<!-- This comment never ends

<h1>Hello</h1>
```

Everything after the opening comment may be ignored by the browser.

---

## Using Too Many Comments

❌ Not Recommended

```html
<!-- Paragraph -->
<p>Hello</p>

<!-- Image -->
<img src="image.jpg">

<!-- Button -->
<button>Click</button>
```

Simple HTML usually doesn't need comments.

---

## Writing Unclear Comments

❌ Bad

```html
<!-- Stuff -->
```

✅ Better

```html
<!-- User Login Form -->
```

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
    <header>
        <h1>Learning HTML</h1>
    </header>

    <!-- Main Content -->
    <main>

        <p>This is a sample webpage.</p>

        <!--
        <p>This paragraph is temporarily hidden.</p>
        -->

    </main>

    <!-- Footer -->
    <footer>
        Copyright © 2026
    </footer>

</body>

</html>
```

---

# Best Practices

* Use comments to explain **complex** code, not obvious code.
* Divide large HTML files into logical sections.
* Keep comments short, clear, and meaningful.
* Remove outdated or unnecessary comments.
* Never include confidential information in comments.
* Use comments consistently throughout your project.

---

# Interview Questions

### 1. Are HTML comments displayed on a webpage?

No. They are ignored by the browser.

---

### 2. What is the syntax for an HTML comment?

```html
<!-- This is a comment -->
```

---

### 3. Can HTML comments be nested?

No. Nested comments are invalid.

---

### 4. Why should you avoid storing sensitive information in comments?

Because comments are hidden from the webpage but **visible in the page source**, which anyone can inspect.

---

# Summary

| Feature                 | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| Syntax                  | `<!-- Comment -->`                                                 |
| Visible on webpage?     | ❌ No                                                               |
| Visible in source code? | ✅ Yes                                                              |
| Single-line comments    | Explain one line of code                                           |
| Multi-line comments     | Explain larger sections                                            |
| Commented-out code      | Temporarily disables HTML without deleting it                      |
| Nested comments         | ❌ Not allowed                                                      |
| Best practice           | Keep comments clear, useful, and never store sensitive information |
