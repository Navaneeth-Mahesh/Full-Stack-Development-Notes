# HTML Favicon

A **favicon** (short for **favorite icon**) is the small icon displayed in the browser tab next to a webpage's title.

It helps users quickly recognize your website when multiple tabs are open and improves your site's branding.

---

# What Does a Favicon Look Like?

When you open a website, you might see something like this:

```text
🌐 My Website
```

The **🌐** represents the favicon.

Real websites also use favicons:

```text
📺 YouTube
📘 Facebook
🐙 GitHub
🟢 Spotify
```

---

# Why Use a Favicon?

A favicon provides several benefits:

* Makes your website look more professional.
* Helps users identify your website quickly.
* Improves branding and recognition.
* Appears in:

  * Browser tabs
  * Bookmarks
  * Browser history
  * Some search results
  * Mobile home screen shortcuts (when supported)

---

# Project Structure

A favicon file should be stored inside your project.

Example:

```text
project/
│
├── index.html
├── favicon.ico
│
├── images/
│   ├── favicon.png
│   └── logo.svg
│
└── css/
    └── style.css
```

---

# How to Add a Favicon

Add a `<link>` element inside the `<head>` section of your HTML document.

## Using an ICO File

```html
<link rel="icon" href="favicon.ico">
```

---

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>My Website</title>

    <link rel="icon" href="favicon.ico">
</head>

<body>

    <h1>Welcome!</h1>

</body>

</html>
```

---

# Using a PNG Favicon

PNG is one of the most commonly used formats.

```html
<link
    rel="icon"
    type="image/png"
    href="images/favicon.png">
```

---

# Using an SVG Favicon

Modern browsers support SVG favicons.

SVG images remain sharp at every size because they are vector graphics.

```html
<link
    rel="icon"
    type="image/svg+xml"
    href="images/favicon.svg">
```

---

# Understanding the Attributes

Example:

```html
<link
    rel="icon"
    type="image/png"
    href="images/favicon.png">
```

| Attribute    | Purpose                                                 |
| ------------ | ------------------------------------------------------- |
| `<link>`     | Links an external resource to the webpage               |
| `rel="icon"` | Specifies that the linked file is the website's favicon |
| `href`       | Specifies the location (path) of the favicon            |
| `type`       | Specifies the file's MIME type (recommended)            |

---

# Different Ways to Specify the Path

## Same Folder

```text
project/
│
├── index.html
└── favicon.ico
```

```html
<link rel="icon" href="favicon.ico">
```

---

## Inside an Images Folder

```text
project/
│
├── index.html
└── images/
    └── favicon.png
```

```html
<link rel="icon" href="images/favicon.png">
```

---

## Parent Folder

```text
project/
│
├── favicon.ico
└── pages/
    └── index.html
```

```html
<link rel="icon" href="../favicon.ico">
```

---

# Common Favicon File Types

| File Type | Extension       | Description                                                   |
| --------- | --------------- | ------------------------------------------------------------- |
| ICO       | `.ico`          | Best browser compatibility                                    |
| PNG       | `.png`          | Most commonly used                                            |
| SVG       | `.svg`          | Scalable vector image with excellent quality                  |
| GIF       | `.gif`          | Supported but rarely used                                     |
| JPEG      | `.jpg`, `.jpeg` | Supported by most browsers but not commonly used for favicons |

---

# Recommended Sizes

Although browsers can resize favicons automatically, these sizes are commonly used:

| Size         | Common Use                  |
| ------------ | --------------------------- |
| 16 × 16 px   | Browser tabs                |
| 32 × 32 px   | Most websites               |
| 48 × 48 px   | Desktop shortcuts           |
| 180 × 180 px | Apple Touch Icon            |
| 192 × 192 px | Android devices             |
| 512 × 512 px | Progressive Web Apps (PWAs) |

---

# Best Practices

* Use a simple and recognizable icon.
* Keep the image square.
* Use transparent backgrounds when appropriate.
* Use PNG or SVG for modern websites.
* Name the file clearly (for example, `favicon.png` or `favicon.ico`).
* Place the favicon in the project root or an `images` folder.
* Include the favicon inside the `<head>` element.

---

# Common Beginner Mistakes

### ❌ Placing the `<link>` element inside `<body>`

Incorrect:

```html
<body>

<link rel="icon" href="favicon.ico">

</body>
```

Correct:

```html
<head>

<link rel="icon" href="favicon.ico">

</head>
```

---

### ❌ Using the Wrong File Path

Project structure:

```text
project/
│
├── index.html
└── images/
    └── favicon.png
```

Incorrect:

```html
<link rel="icon" href="favicon.png">
```

Correct:

```html
<link rel="icon" href="images/favicon.png">
```

---

### ❌ Forgetting the File Extension

Incorrect:

```html
<link rel="icon" href="favicon">
```

Correct:

```html
<link rel="icon" href="favicon.ico">
```

---

# Browser Support

Modern browsers support several favicon formats.

| Browser | ICO | PNG | GIF | JPEG | SVG |
| ------- | :-: | :-: | :-: | :--: | :-: |
| Chrome  |  ✅  |  ✅  |  ✅  |   ✅  |  ✅  |
| Edge    |  ✅  |  ✅  |  ✅  |   ✅  |  ✅  |
| Firefox |  ✅  |  ✅  |  ✅  |   ✅  |  ✅  |
| Safari  |  ✅  |  ✅  |  ✅  |   ✅  |  ✅  |
| Opera   |  ✅  |  ✅  |  ✅  |   ✅  |  ✅  |

> **Note:** While JPEG is supported by most browsers, **ICO**, **PNG**, and **SVG** are the preferred formats for favicons.

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>My Website</title>

    <link
        rel="icon"
        type="image/png"
        href="images/favicon.png">

</head>

<body>

    <h1>Welcome to My Website</h1>

    <p>
        This webpage uses a custom favicon.
    </p>

</body>

</html>
```

---

# Summary

| Element / Attribute | Purpose                                             |
| ------------------- | --------------------------------------------------- |
| `<link>`            | Links an external resource to the HTML document     |
| `rel="icon"`        | Identifies the linked file as the website's favicon |
| `href`              | Specifies the path to the favicon file              |
| `type`              | Specifies the favicon's MIME type (recommended)     |

---

# Key Points

* A **favicon** is the small icon displayed in the browser tab.
* Favicons help users quickly identify your website.
* Add the favicon using the `<link rel="icon">` element inside the `<head>` section.
* **ICO**, **PNG**, and **SVG** are the most commonly used formats.
* Use a square image (such as **32 × 32 px**) for the best results.
* Make sure the `href` path correctly points to the favicon file.
* A favicon improves the professional appearance and branding of your website.
