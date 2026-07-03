# HTML Iframes

An **iframe** (**Inline Frame**) is an HTML element used to **embed another webpage or document inside the current webpage**.

Think of an iframe as a **window inside a webpage** that displays another HTML page, website, video, map, or PDF.

---

# How an Iframe Works

```text
Current Webpage
┌─────────────────────────────────────────────┐
│ My Website                                  │
│                                             │
│  ┌──────────────────────────────────────┐   │
│  │                                      │   │
│  │      Another Webpage (iframe)        │   │
│  │                                      │   │
│  └──────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

The outer webpage remains the same, while the iframe displays another page inside it.

---

# Common Uses of Iframes

Iframes are commonly used to embed:

* Another HTML page
* Google Maps
* YouTube videos
* PDF documents
* Interactive forms
* Dashboards
* External websites (if allowed)

---

# Basic Syntax

```html
<iframe src="URL" title="Description"></iframe>
```

## Example

```html
<iframe
    src="about.html"
    title="About Page">
</iframe>
```

---

# The `src` Attribute

The `src` attribute specifies **which webpage or document should be displayed** inside the iframe.

## Example (Local File)

```html
<iframe
    src="contact.html"
    title="Contact Page">
</iframe>
```

---

## Example (External Website)

```html
<iframe
    src="https://developer.mozilla.org"
    title="MDN Web Docs">
</iframe>
```

> **Note:** Many websites prevent themselves from being displayed inside an iframe for security reasons. If that happens, the webpage will not load inside the iframe.

---

# The `title` Attribute

The `title` attribute describes the iframe.

It helps:

* Screen readers
* Accessibility tools
* Search engines better understand the iframe's purpose

Example:

```html
<iframe
    src="about.html"
    title="About Our Company">
</iframe>
```

Always provide a meaningful title.

---

# Setting Width and Height

Use the `width` and `height` attributes to control the iframe's size.

```html
<iframe
    src="profile.html"
    width="500"
    height="300"
    title="User Profile">
</iframe>
```

Output:

```text
Width  → 500 pixels
Height → 300 pixels
```

If no unit is specified, HTML treats the values as **pixels (px)**.

---

# Using CSS for Size

Instead of HTML attributes, you can use CSS.

```html
<iframe
    src="gallery.html"
    style="width:600px; height:350px;"
    title="Gallery">
</iframe>
```

Using CSS is generally preferred because it keeps styling separate from HTML.

---

# Removing the Border

Browsers usually display a border around an iframe.

Default:

```text
+-----------------------+
|                       |
|     Webpage           |
|                       |
+-----------------------+
```

Remove it using CSS:

```html
<iframe
    src="home.html"
    style="border:none;"
    title="Home Page">
</iframe>
```

---

# Customizing the Border

You can change:

* Width
* Style
* Color

Example:

```html
<iframe
    src="services.html"
    style="border:3px solid royalblue;"
    width="500"
    height="250"
    title="Services">
</iframe>
```

Other border styles include:

```css
border:2px dashed black;
border:4px dotted red;
border:5px double green;
```

---

# Opening Links Inside an Iframe

Instead of opening a new webpage, links can load inside an iframe.

This requires:

1. Giving the iframe a `name`
2. Using the same value in the link's `target`

## Example

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
    About
</a>

<br>

<a href="contact.html" target="contentFrame">
    Contact
</a>
```

### How It Works

```text
Click Link
     │
     ▼
target="contentFrame"
     │
     ▼
iframe name="contentFrame"
     │
     ▼
New page loads inside the iframe
```

The browser does **not** replace the current webpage.

Only the iframe content changes.

---

# Embedding a YouTube Video

Many websites provide embed links.

Example:

```html
<iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/VIDEO_ID"
    title="YouTube Video">
</iframe>
```

Replace `VIDEO_ID` with the video's ID.

---

# Embedding Google Maps

Google Maps also provides embed code.

Example:

```html
<iframe
    src="https://www.google.com/maps/embed?..."
    width="600"
    height="450"
    style="border:0;"
    title="Google Map">
</iframe>
```

---

# Loading PDF Files

An iframe can display PDF documents.

```html
<iframe
    src="notes.pdf"
    width="700"
    height="500"
    title="HTML Notes">
</iframe>
```

---

# Security Considerations

Not every website allows embedding.

Many websites send security headers like:

* `X-Frame-Options`
* `Content-Security-Policy`

These prevent other websites from displaying their pages inside iframes to protect against attacks such as **clickjacking**.

If a website blocks embedding, you'll usually see a message instead of the webpage.

---

# Common Attributes

| Attribute        | Description                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| `src`            | URL or file to display                                                           |
| `title`          | Description for accessibility                                                    |
| `width`          | Width of the iframe                                                              |
| `height`         | Height of the iframe                                                             |
| `name`           | Gives the iframe a name                                                          |
| `style`          | Applies CSS styling                                                              |
| `loading="lazy"` | Delays loading until the iframe is near the viewport, improving page performance |

Example:

```html
<iframe
    src="about.html"
    loading="lazy"
    title="About Page">
</iframe>
```

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
        loading="lazy"
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

* Always provide a meaningful `title` attribute.
* Set an appropriate `width` and `height`.
* Prefer CSS for styling instead of inline HTML attributes.
* Use `loading="lazy"` for better performance when appropriate.
* Give descriptive names when using the `name` attribute.
* Only embed websites that allow iframe embedding.
* Avoid embedding untrusted websites.

---

# Common Beginner Mistakes

### ❌ Forgetting the `title`

```html
<iframe src="about.html"></iframe>
```

✔ Correct

```html
<iframe
    src="about.html"
    title="About Page">
</iframe>
```

---

### ❌ Using the wrong `target`

```html
<a href="about.html" target="frame1">
```

```html
<iframe name="viewer">
```

The names do not match, so the link will not open inside the iframe.

✔ Correct

```html
<a href="about.html" target="viewer">
```

```html
<iframe name="viewer">
```

---

### ❌ Trying to embed blocked websites

Some websites intentionally prevent embedding. If an iframe stays blank or shows an error, the website likely does not permit being displayed inside an iframe.

---

# Interview Questions

### 1. What is an iframe?

An iframe is an HTML element that embeds another webpage or document inside the current webpage.

---

### 2. Which attribute specifies the webpage to display?

The `src` attribute.

---

### 3. Why is the `title` attribute important?

It improves accessibility by helping screen readers describe the iframe's content.

---

### 4. Can every website be embedded in an iframe?

No. Many websites block iframe embedding using security headers such as `X-Frame-Options` or `Content-Security-Policy`.

---

### 5. How do links open inside an iframe?

Assign the iframe a `name` and set the link's `target` attribute to the same value.

---

# Key Points

* `<iframe>` embeds another webpage or document inside the current page.
* The `src` attribute specifies what content to display.
* The `title` attribute is important for accessibility.
* `width` and `height` control the iframe's size.
* CSS can be used to style the iframe, including its border.
* The `name` and `target` attributes allow links to open inside the iframe.
* Iframes are commonly used for videos, maps, PDFs, and embedded webpages.
* Not all websites allow themselves to be displayed in an iframe due to security restrictions.
