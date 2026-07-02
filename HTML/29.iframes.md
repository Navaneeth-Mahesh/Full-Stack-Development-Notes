# HTML Iframes

An **iframe** (Inline Frame) allows you to embed another webpage or HTML document inside the current webpage.

It is commonly used to display:

- Another website
- Maps
- YouTube videos
- PDF files
- HTML pages from the same project

---

# Basic Syntax

```html
<iframe src="URL" title="Description"></iframe>
```

### Example

```html
<iframe
    src="about.html"
    title="About Page">
</iframe>
```

> **Note:** Always include the `title` attribute. It helps screen readers describe the content of the iframe, improving accessibility.

---

# The `src` Attribute

The `src` attribute specifies the webpage or document that should be displayed inside the iframe.

### Example

```html
<iframe
    src="contact.html"
    title="Contact Page">
</iframe>
```

You can also embed webpages available online.

```html
<iframe
    src="https://developer.mozilla.org"
    title="MDN Web Docs">
</iframe>
```

---

# Setting Width and Height

Use the `width` and `height` attributes to control the size of the iframe.

### Example

```html
<iframe
    src="profile.html"
    width="500"
    height="300"
    title="User Profile">
</iframe>
```

The values are measured in **pixels (px)** by default.

---

# Using CSS to Set Size

Instead of HTML attributes, you can use the `style` attribute.

### Example

```html
<iframe
    src="gallery.html"
    style="width:600px; height:350px;"
    title="Image Gallery">
</iframe>
```

---

# Removing the Border

By default, browsers display a border around an iframe.

To remove it, use the CSS `border` property.

### Example

```html
<iframe
    src="home.html"
    style="border:none;"
    title="Home Page">
</iframe>
```

---

# Customizing the Border

You can also change the border's width, style, and color.

### Example

```html
<iframe
    src="services.html"
    style="border:3px solid royalblue;"
    width="500"
    height="250"
    title="Services Page">
</iframe>
```

---

# Using an Iframe as a Link Target

An iframe can display different webpages when links are clicked.

To do this:

1. Give the iframe a `name`.
2. Set the link's `target` attribute to the same name.

### Example

```html
<iframe
    src="welcome.html"
    name="contentFrame"
    width="600"
    height="300"
    title="Content Viewer">
</iframe>

<br><br>

<a href="about.html" target="contentFrame">
    Open About Page
</a>

<br>

<a href="contact.html" target="contentFrame">
    Open Contact Page
</a>
```

When either link is clicked, the selected page opens inside the iframe instead of replacing the current webpage.

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Iframe Example</title>
</head>

<body>

    <h1>Learning HTML Iframes</h1>

    <iframe
        src="welcome.html"
        name="pageViewer"
        width="700"
        height="350"
        style="border:2px solid gray;"
        title="Page Viewer">
    </iframe>

    <br><br>

    <a href="about.html" target="pageViewer">
        About Page
    </a>

    <br>

    <a href="contact.html" target="pageViewer">
        Contact Page
    </a>

</body>

</html>
```

---

# Best Practices

- Always provide a meaningful `title` attribute.
- Set an appropriate `width` and `height` for better user experience.
- Use CSS to customize the iframe's appearance.
- Avoid embedding websites that do not allow iframes.
- Use descriptive names when assigning the `name` attribute.

---

# Summary

| Attribute | Purpose |
|-----------|---------|
| `<iframe>` | Embeds another webpage inside the current page |
| `src` | Specifies the webpage or document to display |
| `title` | Describes the iframe for accessibility |
| `width` | Sets the iframe width |
| `height` | Sets the iframe height |
| `style` | Applies CSS such as border, width, and height |
| `name` | Gives the iframe a name so links can target it |
| `target` | Opens a link inside the specified iframe |