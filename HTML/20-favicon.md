# HTML Favicon

A **favicon** (short for **favorite icon**) is the small icon displayed in the browser tab next to the webpage title. It helps users easily identify your website among multiple open tabs.

---

# Example

When you open a website in your browser, you may see a small icon like this:

```
🌐 My Website
```

The 🌐 icon is the **favicon**.

---

# How to Add a Favicon

Place your favicon image inside your project folder.

Example project structure:

```text
project/
│
├── index.html
├── favicon.ico
└── images/
```

Then add the following `<link>` element inside the `<head>` section of your HTML document.

```html
<head>
    <title>My Website</title>

    <link rel="icon" href="favicon.ico">
</head>
```

---

# Using a PNG Image

You can also use a PNG image as a favicon.

```html
<link
    rel="icon"
    type="image/png"
    href="images/favicon.png">
```

---

# Using an SVG Image

Modern browsers also support SVG favicons.

```html
<link
    rel="icon"
    type="image/svg+xml"
    href="favicon.svg">
```

---

# Common Favicon File Types

| File Type | Extension | Recommended |
|-----------|-----------|-------------|
| ICO | `.ico` | Best browser compatibility |
| PNG | `.png` | Most commonly used |
| SVG | `.svg` | Best for scalable vector icons |
| GIF | `.gif` | Supported but rarely used |

---

# Where to Place the Favicon

The `<link rel="icon">` element should always be placed inside the `<head>` section.

Example:

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

# Best Practices

- Use a simple and recognizable icon.
- Keep the favicon square (for example, **32 × 32 px** or **48 × 48 px**).
- Use PNG or SVG for modern websites.
- Give the file a meaningful name such as `favicon.png` or `favicon.ico`.
- Place the favicon in the project root or an `images` folder.

---

# Summary

| Element/Attribute | Purpose |
|-------------------|---------|
| `<link>` | Links an external resource to the HTML document |
| `rel="icon"` | Specifies that the linked file is the website's favicon |
| `href` | Specifies the path to the favicon file |
| `type` | Specifies the MIME type of the favicon (optional but recommended) |

Favicon File Format Support
The following table shows the file format support for a favicon image:

Browser	ICO	PNG	GIF	JPEG	SVG
Edge	Yes	Yes	Yes	Yes	Yes
Chrome	Yes	Yes	Yes	Yes	Yes
Firefox	Yes	Yes	Yes	Yes	Yes
Opera	Yes	Yes	Yes	Yes	Yes
Safari	Yes	Yes	Yes	Yes	Yes