# HTML Structure

Every HTML document follows a standard structure. This structure tells the browser how the webpage is organized and what content should be displayed.

---

# Basic HTML Structure

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>

<body>
    <h1>Welcome</h1>
    <p>This is a basic HTML page.</p>
</body>

</html>
```

---

# How the Browser Reads an HTML Page

```text
HTML File
    │
    ▼
Browser Reads HTML
    │
    ▼
Builds the Document Structure (DOM)
    │
    ▼
Loads CSS (if any)
    │
    ▼
Executes JavaScript (if any)
    │
    ▼
Displays the Web Page
```

---

# HTML Document Structure

```text
<!DOCTYPE html>
│
└── <html>
    │
    ├── <head>
    │   ├── <meta>
    │   ├── <title>
    │   ├── <link>
    │   ├── <style>
    │   └── <script>
    │
    └── <body>
        ├── Headings
        ├── Paragraphs
        ├── Images
        ├── Links
        ├── Forms
        ├── Tables
        └── Other Visible Content
```

---

# Structure Explanation

## `<!DOCTYPE html>`

Declares that the document is an **HTML5** document.

It should **always be the very first line** of every HTML file.

### Why is it Important?

Without it, the browser may switch to **Quirks Mode**, causing some HTML and CSS features to behave differently.

Example:

```html
<!DOCTYPE html>
```

---

## `<html>`

The `<html>` element is the **root element** of every HTML document.

Everything on the webpage must be placed inside this tag.

Example:

```html
<html lang="en">
```

---

## The `lang` Attribute

The `lang` attribute specifies the primary language of the webpage.

Example:

```html
<html lang="en">
```

### Why use `lang`?

- Helps screen readers pronounce words correctly.
- Improves accessibility.
- Helps search engines understand the page language.
- Assists browsers with translation.

### Common Values

| Value | Language |
|---------|----------|
| `en` | English |
| `en-US` | English (United States) |
| `en-GB` | English (United Kingdom) |
| `fr` | French |
| `de` | German |
| `es` | Spanish |
| `hi` | Hindi |
| `ja` | Japanese |
| `zh` | Chinese |

---

# `<head>`

The `<head>` element contains **information about the webpage**, not the visible content.

The browser uses this information to correctly display and manage the webpage.

Common elements inside `<head>` include:

- `<title>`
- `<meta>`
- `<link>`
- `<style>`
- `<script>`
- `<base>`

Example:

```html
<head>
    <title>My Website</title>
</head>
```

---

# Common Tags Inside `<head>`

| Tag | Purpose |
|------|---------|
| `<title>` | Browser tab title |
| `<meta>` | Metadata about the page |
| `<link>` | Connects external CSS files, icons, fonts, etc. |
| `<style>` | Internal CSS |
| `<script>` | JavaScript |
| `<base>` | Sets the default URL for relative links |

---

# `<meta>`

The `<meta>` tag provides **metadata** (information about the webpage).

Metadata is **not visible** on the webpage but is used by browsers, search engines, and other web services.

---

## Character Encoding

```html
<meta charset="UTF-8">
```

### Purpose

Specifies that the webpage uses **UTF-8** character encoding.

UTF-8 supports almost every language and many special symbols.

Examples:

- English
- తెలుగు
- हिन्दी
- 日本語
- العربية
- €
- ©
- ✓
- ❤️

Without UTF-8, some characters may appear incorrectly.

---

## Viewport Meta Tag

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Purpose

Makes the webpage responsive on different devices.

Without it, mobile browsers may display the desktop version, making text and buttons appear very small.

### Breakdown

| Property | Meaning |
|-----------|---------|
| `width=device-width` | Sets the page width to match the device's screen width |
| `initial-scale=1.0` | Sets the initial zoom level to 100% |

---

## Other Useful Meta Tags

### Page Description

```html
<meta name="description" content="Learn HTML with beginner-friendly notes.">
```

Used by search engines to display a description in search results.

---

### Author

```html
<meta name="author" content="Navaneeth">
```

Specifies the author of the webpage.

---

### Keywords (Mostly Obsolete)

```html
<meta name="keywords" content="HTML, CSS, JavaScript">
```

Older search engines used this for indexing. Modern search engines largely ignore it.

---

# `<title>`

The `<title>` tag defines the title of the webpage.

Example:

```html
<title>My Portfolio</title>
```

The title appears in:

- Browser tabs
- Browser history
- Bookmarks
- Search engine results

Example:

```text
Chrome Tab

My Portfolio
```

---

# `<body>`

The `<body>` element contains **everything visible** on the webpage.

Examples include:

- Headings
- Paragraphs
- Images
- Videos
- Links
- Buttons
- Forms
- Tables
- Lists
- Navigation bars

Example:

```html
<body>
    <h1>Hello World</h1>
    <p>Welcome to HTML.</p>
</body>
```

---

# HTML Comments

Comments are ignored by the browser.

They are used to explain code or temporarily disable parts of HTML.

Syntax:

```html
<!-- This is a comment -->
```

Example:

```html
<!-- Header Section -->
<header>
    ...
</header>
```

You can also comment out code:

```html
<!--
<p>This paragraph won't appear.</p>
-->
```

---

# Putting Everything Together

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <meta
        name="description"
        content="Learning HTML Structure"
    >

    <title>HTML Structure</title>

</head>

<body>

    <h1>Welcome to HTML</h1>

    <p>This is my first webpage.</p>

</body>

</html>
```

---

# Best Practices

- Always start with `<!DOCTYPE html>`.
- Always include the `lang` attribute.
- Use `UTF-8` encoding.
- Include the viewport meta tag for responsive webpages.
- Write a meaningful page title.
- Keep metadata inside `<head>`.
- Place visible content inside `<body>`.
- Use comments only where they improve readability.

---

# Common Beginner Mistakes

❌ Forgetting `<!DOCTYPE html>`

```html
<html>
```

✔ Correct

```html
<!DOCTYPE html>
<html>
```

---

❌ Writing visible content inside `<head>`

```html
<head>
    <h1>Hello</h1>
</head>
```

✔ Correct

```html
<body>
    <h1>Hello</h1>
</body>
```

---

❌ Forgetting the viewport meta tag

```html
<head>
</head>
```

✔ Correct

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

---

# Summary

| Element | Purpose |
|----------|---------|
| `<!DOCTYPE html>` | Declares the document as HTML5 |
| `<html>` | Root element of the HTML document |
| `lang` | Specifies the language of the webpage |
| `<head>` | Contains metadata and page information |
| `<meta>` | Provides metadata such as encoding, viewport, and page description |
| `<title>` | Sets the browser tab title |
| `<body>` | Contains all visible webpage content |
| `<!-- -->` | Adds comments ignored by the browser |

---

# Quick Revision

- HTML documents follow a fixed structure.
- `<!DOCTYPE html>` tells the browser to use HTML5.
- `<html>` is the root element.
- `<head>` stores page information.
- `<body>` contains everything visible.
- `<meta charset="UTF-8">` supports most languages and symbols.
- `<meta name="viewport">` makes webpages responsive.
- `<title>` sets the browser tab title.
- Comments help explain code without affecting the webpage.