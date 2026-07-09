# HTML Accessibility

**Accessibility** in HTML means designing web pages so that everyone can use them, including people with disabilities (visual, hearing, motor, or cognitive impairments).

Accessible HTML ensures that websites work well with:

- Screen readers
- Keyboard navigation
- Voice control systems
- Assistive technologies

The goal is to make web content **usable, understandable, and reachable for all users**.

---

# Why Accessibility Matters

Accessible websites:

- Improve user experience for everyone
- Help users with disabilities access content
- Improve SEO (search engine optimization)
- Make websites more professional and standards-compliant
- Are required by modern web standards (like WCAG guidelines)

---

# Semantic HTML (Most Important Rule)

Use **semantic elements** instead of non-semantic ones.

### Example of good structure:

```html
<header>
    <h1>My Website</h1>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
</nav>

<main>
    <article>
        <h2>Blog Post</h2>
        <p>This is content.</p>
    </article>
</main>

<footer>
    <p>© 2026 My Website</p>
</footer>
```

### Why semantic HTML matters:

- Helps screen readers understand structure
- Improves SEO ranking
- Makes code easier to read and maintain

---

# Alternative Text for Images (`alt`)

Always provide meaningful `alt` text for images.

```html
<img src="dog.jpg" alt="Golden retriever playing in the park">
```

### Good alt text:
- Describes the image clearly
- Explains purpose if image is functional

### Bad alt text:
- `alt="image"`
- `alt="photo123"`

---

# Headings Structure

Use headings in correct order.

### Correct:

```html
<h1>Main Title</h1>
<h2>Section Title</h2>
<h3>Subsection</h3>
```

### Incorrect:

```html
<h3>Main Title</h3>
<h1>Section Title</h1>
```

Screen readers rely on heading structure to navigate content.

---

# Keyboard Navigation

All interactive elements should be usable with a keyboard:

- `<a>`
- `<button>`
- `<input>`
- `<select>`

Example:

```html
<button>Submit</button>
```

Avoid using non-interactive elements like `<div>` for buttons.

---

# Labels for Form Inputs

Always connect `<label>` with form controls.

```html
<label for="name">Name:</label>
<input type="text" id="name">
```

### Why it matters:

- Screen readers announce labels properly
- Clicking label focuses input

---

# ARIA (Accessible Rich Internet Applications)

ARIA attributes help improve accessibility when HTML alone is not enough.

Example:

```html
<button aria-label="Close menu">X</button>
```

Common ARIA attributes:

| Attribute | Purpose |
|------------|--------|
| `aria-label` | Provides label for screen readers |
| `aria-hidden` | Hides elements from assistive tech |
| `role` | Defines element purpose |
| `aria-live` | Announces dynamic content updates |

---

# Color Contrast

Ensure text is readable:

- Dark text on light background
- Light text on dark background

Avoid low contrast combinations like:

- Light gray text on white background
- Yellow text on white background

---

# Links Should Be Descriptive

Avoid vague links like:

```html
<a href="page.html">Click here</a>
```

Better:

```html
<a href="page.html">Read HTML basics guide</a>
```

---

# Form Accessibility Example

```html
<form>
    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email">

    <button type="submit">Submit</button>
</form>
```

---

# Common Accessibility Mistakes

- Missing `alt` attributes on images
- Using only `<div>` instead of semantic tags
- Poor heading structure
- Unlabeled form inputs
- Low color contrast
- Non-keyboard-friendly UI

---

# Summary

- Accessibility makes websites usable for everyone
- Use semantic HTML elements properly
- Always add `alt` text for images
- Maintain proper heading structure
- Ensure keyboard navigation support
- Use labels for form inputs
- Apply ARIA only when necessary
- Keep good color contrast for readability