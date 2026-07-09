# Meta Tags & SEO in HTML

Meta tags are special HTML elements that provide **information about a webpage**. This information is not displayed on the page but is used by browsers, search engines, and social media platforms.

They are placed inside the `<head>` section of an HTML document.

---

# Basic Meta Tags Example

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Learn HTML step by step with simple notes and examples.">
    <meta name="keywords" content="HTML, CSS, Web Development, Beginner HTML">
    <meta name="author" content="Navaneeth">

    <title>HTML Meta Tags</title>
</head>
```

---

# What is SEO?

**SEO (Search Engine Optimization)** is the process of improving a website so that it ranks higher in search engines like Google.

Meta tags play an important role in SEO because they help search engines understand your page content.

---

# Important Meta Tags

## 1. Charset Meta Tag

```html
<meta charset="UTF-8">
```

### Purpose:
Defines the character encoding of the webpage.

### Why it matters:
- Supports all languages and symbols
- Prevents text errors or broken characters

---

## 2. Viewport Meta Tag (Responsive Design)

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Purpose:
Makes your website responsive on mobile, tablet, and desktop devices.

### Without this:
- Website may look zoomed out on mobile
- Layout may break on small screens

---

## 3. Description Meta Tag

```html
<meta name="description" content="Learn HTML step by step with examples.">
```

### Purpose:
Provides a short summary of your webpage.

### SEO Impact:
- Often shown in Google search results
- Helps users understand your page before clicking

---

## 4. Keywords Meta Tag (Less Important Today)

```html
<meta name="keywords" content="HTML, CSS, JavaScript, Web Development">
```

### Purpose:
Lists keywords related to your page.

### Note:
Modern search engines like Google mostly ignore this tag, but it is still useful for learning.

---

## 5. Author Meta Tag

```html
<meta name="author" content="Navaneeth">
```

### Purpose:
Specifies the name of the page creator or author.

---

## 6. Robots Meta Tag

```html
<meta name="robots" content="index, follow">
```

### Purpose:
Controls how search engines interact with your page.

### Values:

| Value | Meaning |
|------|--------|
| `index` | Allow page to be indexed |
| `noindex` | Prevent page from appearing in search results |
| `follow` | Allow crawling of links |
| `nofollow` | Do not follow links on the page |

Example:

```html
<meta name="robots" content="noindex, nofollow">
```

---

# Open Graph Meta Tags (Social Media SEO)

Open Graph tags are used when sharing links on platforms like WhatsApp, Facebook, and LinkedIn.

```html
<meta property="og:title" content="Learn HTML Easily">
<meta property="og:description" content="Step-by-step HTML learning guide for beginners.">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com">
```

### Purpose:
Controls how your page appears when shared on social media.

---

# Twitter Meta Tags

Used for better preview on Twitter (X).

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Learn HTML Easily">
<meta name="twitter:description" content="Beginner-friendly HTML guide.">
<meta name="twitter:image" content="https://example.com/image.jpg">
```

---

# Full SEO-Friendly Head Example

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="description" content="Complete HTML tutorial for beginners.">
    <meta name="keywords" content="HTML, CSS, JavaScript, Web Development">
    <meta name="author" content="Navaneeth">
    <meta name="robots" content="index, follow">

    <meta property="og:title" content="HTML Tutorial">
    <meta property="og:description" content="Learn HTML step by step.">
    <meta property="og:image" content="https://example.com/image.jpg">
    <meta property="og:url" content="https://example.com">

    <title>HTML SEO Guide</title>
</head>
```

---

# Best Practices for SEO Meta Tags

- Always include `charset` and `viewport`
- Write clear and meaningful `title`
- Keep `description` under 150–160 characters
- Use Open Graph tags for social sharing
- Avoid keyword stuffing in `keywords`
- Keep meta tags relevant to page content

---

# Summary

- Meta tags provide information about a webpage
- They are placed inside the `<head>` section
- They help browsers, search engines, and social media platforms
- SEO meta tags improve visibility in search results
- Open Graph and Twitter tags improve link previews* forms-validation-input-types.md
* accessibility.md
* dom-basics.md
* seo-html.md
* web-apis-expanded.md
* web-components.md
