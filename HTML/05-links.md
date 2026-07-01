# HTML Links

HTML links allow users to navigate from one webpage to another, another section of the same page, an email address, or other resources.

Links are created using the `<a>` (anchor) tag.

---

# Basic Syntax

```html
<a href="URL">Link Text</a>
```

### Example

```html
<a href="https://www.google.com">Visit Google</a>
```

Here:

- `<a>` → Anchor tag
- `href` → Specifies the destination URL
- `Visit Google` → Clickable link text

---

# The `href` Attribute

The `href` (Hypertext Reference) attribute specifies the destination of the link.

### External Website

```html
<a href="https://www.google.com">Google</a>
```

### Another Page in the Same Project

```html
<a href="about.html">About Us</a>
```

### Open a PDF

```html
<a href="notes.pdf">Download Notes</a>
```

---

# The `target` Attribute

The `target` attribute specifies where the linked document should open.

| Value | Description |
|--------|-------------|
| `_self` | Opens the link in the current tab (Default) |
| `_blank` | Opens the link in a new tab or window |
| `_parent` | Opens the link in the parent frame |
| `_top` | Opens the link in the full browser window |

### Example

```html
<a href="https://www.google.com" target="_blank">
    Open Google
</a>
```

> **Tip:** When using `target="_blank"` for external websites, it's a good practice to also include `rel="noopener noreferrer"` for better security.

Example:

```html
<a href="https://www.google.com"
   target="_blank"
   rel="noopener noreferrer">
    Open Google
</a>
```

---

# The `title` Attribute

The `title` attribute displays additional information as a tooltip when the user hovers over the link.

### Example

```html
<a
    href="https://developer.mozilla.org"
    title="Visit MDN Web Docs">
    MDN
</a>
```

---

# Email Links

Use the `mailto:` scheme to open the user's default email application.

### Syntax

```html
<a href="mailto:someone@example.com">
    Send Email
</a>
```

### Example

```html
<a href="mailto:john@example.com">
    Contact John
</a>
```

---

# Telephone Links

Use the `tel:` scheme to call a phone number on supported devices.

### Example

```html
<a href="tel:+919876543210">
    Call Us
</a>
```

---

# Image as a Link

An image can be wrapped inside an anchor tag to make it clickable.

### Example

```html
<a href="https://example.com">
    <img
        src="logo.png"
        alt="Website Logo"
        width="120">
</a>
```

---

# Button as a Link

A button can be used to navigate to another page using JavaScript.

### Example

```html
<button onclick="document.location='about.html'">
    Go to About Page
</button>
```

> **Note:** For simple navigation, using an `<a>` element styled as a button is generally preferred over JavaScript.

---

# Linking to a Section on the Same Page

You can create links that jump to a specific section using the `id` attribute.

### Step 1: Add an `id`

```html
<h2 id="contact">Contact</h2>
```

### Step 2: Create the Link

```html
<a href="#contact">Go to Contact Section</a>
```

---

# Absolute vs Relative URLs

## Absolute URL

An absolute URL contains the complete web address.

```html
<a href="https://www.google.com">
    Google
</a>
```

## Relative URL

A relative URL points to a file within the same project.

```html
<a href="about.html">
    About Us
</a>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Links</title>
</head>
<body>

    <h1>Examples of HTML Links</h1>

    <a href="https://www.google.com">
        Google
    </a>

    <br><br>

    <a href="about.html">
        About Page
    </a>

    <br><br>

    <a
        href="https://developer.mozilla.org"
        target="_blank"
        rel="noopener noreferrer">
        Open MDN in New Tab
    </a>

    <br><br>

    <a href="mailto:info@example.com">
        Send Email
    </a>

    <br><br>

    <a href="#bottom">
        Jump to Bottom
    </a>

    <br><br><br><br><br>

    <h2 id="bottom">Bottom of Page</h2>

</body>
</html>
```

---

# Summary

| Attribute/Tag | Purpose |
|---------------|---------|
| `<a>` | Creates a hyperlink |
| `href` | Specifies the destination URL |
| `target` | Specifies where the link opens |
| `_self` | Opens in the current tab (default) |
| `_blank` | Opens in a new tab or window |
| `title` | Displays a tooltip on hover |
| `mailto:` | Opens the default email application |
| `tel:` | Opens the phone dialer on supported devices |
| `#id` | Links to a specific section on the same page |
| `<img>` inside `<a>` | Makes an image clickable |