# HTML Links

HTML links allow users to navigate between web pages, sections of the same page, files, email addresses, phone numbers, and other online resources.

Links are created using the **Anchor (`<a>`)** element.

---

# What is a Hyperlink?

A **hyperlink** (or simply a **link**) is a clickable element that takes the user to another destination.

That destination can be:
- Another webpage
- Another website
- A file (PDF, ZIP, etc.)
- An email address
- A phone number
- A section of the same page

---

# Basic Syntax

```html
<a href="URL">Link Text</a>
```

### Example

```html
<a href="https://www.google.com">Visit Google</a>
```

### Explanation

- `<a>` → Anchor element used to create a hyperlink.
- `href` → Specifies where the link should go.
- `Visit Google` → The clickable text displayed to the user.

---

# How HTML Links Work

```text
User Clicks Link
        │
        ▼
Browser Reads href
        │
        ▼
Loads the Destination
        │
        ▼
Displays the New Page or Resource
```

---

# The `href` Attribute

The `href` (**Hypertext Reference**) attribute specifies the destination of the hyperlink.

Without `href`, the anchor element is **not a functional link**.

## Link to Another Website

```html
<a href="https://www.google.com">Google</a>
```

---

## Link to Another Page in the Same Project

```html
<a href="about.html">About Us</a>
```

Project structure:

```text
project/
│
├── index.html
├── about.html
└── contact.html
```

If you're currently on `index.html`, clicking the link opens `about.html`.

---

## Link to a File

```html
<a href="notes.pdf">Download Notes</a>
```

Users can open or download the file depending on their browser settings.

---

# Absolute URL vs Relative URL

Understanding the difference between these two is very important.

## Absolute URL

An **absolute URL** contains the complete web address.

```html
<a href="https://www.google.com">
    Google
</a>
```

Example:

```
https://www.google.com
```

Use absolute URLs when linking to **other websites**.

---

## Relative URL

A **relative URL** points to a file inside your own project.

```html
<a href="about.html">
    About Us
</a>
```

Example project:

```text
website/
│
├── index.html
├── about.html
└── contact.html
```

---

### Comparison

| Absolute URL | Relative URL |
|--------------|--------------|
| Complete web address | File path inside your project |
| Used for external websites | Used for internal pages |
| Includes `https://` | Doesn't require the full address |

---

# The `target` Attribute

The `target` attribute specifies **where the linked document should open**.

| Value | Description |
|--------|-------------|
| `_self` | Opens in the current tab (default) |
| `_blank` | Opens in a new tab or window |
| `_parent` | Opens in the parent frame |
| `_top` | Opens in the full browser window |

Example:

```html
<a href="https://www.google.com" target="_blank">
    Open Google
</a>
```

---

# Why Use `rel="noopener noreferrer"`?

When opening external websites using:

```html
target="_blank"
```

it is recommended to add:

```html
rel="noopener noreferrer"
```

Example:

```html
<a
    href="https://www.google.com"
    target="_blank"
    rel="noopener noreferrer">
    Google
</a>
```

### Benefits

- Improves security
- Prevents the new page from accessing your page
- Improves privacy by hiding referral information (with `noreferrer`)

---

# The `title` Attribute

The `title` attribute displays a small tooltip when the user hovers over the link.

Example:

```html
<a
    href="https://developer.mozilla.org"
    title="Visit MDN Web Docs">
    MDN
</a>
```

Result:

```
Hover mouse
      │
      ▼
"Visit MDN Web Docs"
```

---

# Email Links

Use the **`mailto:`** scheme to open the user's default email application.

```html
<a href="mailto:john@example.com">
    Send Email
</a>
```

You can even prefill the email subject.

```html
<a href="mailto:john@example.com?subject=Hello">
    Send Email
</a>
```

---

# Telephone Links

Use the **`tel:`** scheme to call a phone number on supported devices.

```html
<a href="tel:+919876543210">
    Call Us
</a>
```

Useful for:

- Mobile websites
- Business websites
- Contact pages

---

# Download Links

You can suggest that the browser download a file using the `download` attribute.

```html
<a href="notes.pdf" download>
    Download Notes
</a>
```

You can even specify a custom filename.

```html
<a href="notes.pdf" download="HTML-Notes.pdf">
    Download Notes
</a>
```

> **Note:** The browser may ignore the `download` attribute for some external resources due to security restrictions.

---

# Image as a Link

Images can also act as hyperlinks.

```html
<a href="https://example.com">
    <img
        src="logo.png"
        alt="Website Logo"
        width="120">
</a>
```

Workflow:

```text
User Clicks Image
        │
        ▼
Browser Opens Link
```

---

# Linking to a Section on the Same Page

This is also called an **anchor link** or **page bookmark**.

## Step 1

Give an element an `id`.

```html
<h2 id="contact">Contact</h2>
```

---

## Step 2

Create a link pointing to that `id`.

```html
<a href="#contact">
    Go to Contact Section
</a>
```

Workflow:

```text
Click Link
      │
      ▼
Find Matching id
      │
      ▼
Scroll to That Section
```

---

# Linking to Another Page's Section

You can jump directly to a section on another page.

```html
<a href="about.html#team">
    Meet Our Team
</a>
```

And on `about.html`:

```html
<h2 id="team">Our Team</h2>
```

---

# Button as a Link

You might see this:

```html
<button onclick="document.location='about.html'">
    About Page
</button>
```

Although it works, it is **not recommended** for normal navigation.

Instead, use an anchor element and style it like a button using CSS.

```html
<a href="about.html">
    About Page
</a>
```

This is:
- Better for accessibility
- Better for search engines
- Standard HTML practice

---

# Opening Different Types of Resources

HTML links can open many kinds of resources.

| Resource | Example |
|----------|---------|
| Website | `https://example.com` |
| HTML Page | `about.html` |
| PDF | `guide.pdf` |
| Image | `photo.jpg` |
| Email | `mailto:user@example.com` |
| Phone | `tel:+919876543210` |

---

# Complete Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>HTML Links</title>
</head>

<body>

    <h1>HTML Links Example</h1>

    <!-- External Website -->
    <a href="https://www.google.com">
        Google
    </a>

    <br><br>

    <!-- Internal Page -->
    <a href="about.html">
        About Us
    </a>

    <br><br>

    <!-- Open in New Tab -->
    <a
        href="https://developer.mozilla.org"
        target="_blank"
        rel="noopener noreferrer">
        Open MDN
    </a>

    <br><br>

    <!-- Email -->
    <a href="mailto:info@example.com">
        Send Email
    </a>

    <br><br>

    <!-- Telephone -->
    <a href="tel:+919876543210">
        Call Us
    </a>

    <br><br>

    <!-- Download -->
    <a href="notes.pdf" download>
        Download Notes
    </a>

    <br><br>

    <!-- Jump to Section -->
    <a href="#bottom">
        Go to Bottom
    </a>

    <br><br><br><br><br><br><br><br>

    <h2 id="bottom">Bottom of the Page</h2>

</body>

</html>
```

---

# Best Practices

- Use meaningful link text.

✅ Good

```html
<a href="guide.html">HTML Beginner Guide</a>
```

❌ Bad

```html
<a href="guide.html">Click Here</a>
```

---

- Use relative URLs for pages within your project.

- Use absolute URLs for external websites.

- Always include `alt` text for linked images.

- Use `target="_blank"` only when necessary.

- Add `rel="noopener noreferrer"` when using `_blank` for external websites.

- Keep link text short and descriptive.

---

# Common Mistakes

❌ Missing `href`

```html
<a>Google</a>
```

✅ Correct

```html
<a href="https://www.google.com">
    Google
</a>
```

---

❌ Incorrect internal file path

```html
<a href="About.HTML">
```

File names are often case-sensitive on web servers.

---

❌ Using JavaScript for simple navigation

```html
<button onclick="location='home.html'">
```

Prefer:

```html
<a href="home.html">
    Home
</a>
```

---

# Summary

| Element / Attribute | Purpose |
|---------------------|---------|
| `<a>` | Creates a hyperlink |
| `href` | Specifies the destination |
| `target` | Specifies where the link opens |
| `_self` | Current tab (default) |
| `_blank` | New tab/window |
| `title` | Displays a tooltip |
| `mailto:` | Opens the default email application |
| `tel:` | Opens the phone dialer |
| `download` | Downloads a file |
| `#id` | Links to a section on the same page |
| `<img>` inside `<a>` | Creates a clickable image |

---

# Key Points to Remember

- Every hyperlink is created using the `<a>` element.
- The `href` attribute is required to specify the destination.
- Use **relative URLs** for pages within your project.
- Use **absolute URLs** for external websites.
- Use `target="_blank"` to open a link in a new tab.
- Add `rel="noopener noreferrer"` when opening external links in a new tab.
- The `download` attribute allows users to download files.
- Use `mailto:` for email links and `tel:` for phone links.
- Use `#id` to navigate to a specific section on the same page.