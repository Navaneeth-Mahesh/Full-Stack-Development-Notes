# HTML Symbols & Emojis

HTML provides ways to display **special symbols** and **emojis** that cannot always be typed directly from the keyboard.

You can display them using:

- HTML Entity Names
- HTML Entity Numbers
- Unicode Characters (for emojis and symbols)

---

# Why Use HTML Entities?

Some characters have a special meaning in HTML.

For example:

- `<` is used to start an HTML tag.
- `>` is used to end an HTML tag.
- `&` is used to begin an HTML entity.

To display these characters as plain text, you must use **HTML entities**.

---

# HTML Entity Syntax

## Entity Name

```html
&entityName;
```

Example:

```html
&pound;
```

Output:

```
£
```

---

## Entity Number

```html
&#entityNumber;
```

Example:

```html
&#163;
```

Output:

```
£
```

---

# Common HTML Entities

| Character | Entity Name | Entity Number |
|-----------|-------------|---------------|
| `<` | `&lt;` | `&#60;` |
| `>` | `&gt;` | `&#62;` |
| `&` | `&amp;` | `&#38;` |
| `"` | `&quot;` | `&#34;` |
| `'` | `&apos;` | `&#39;` |
| Space (non-breaking) | `&nbsp;` | `&#160;` |
| © | `&copy;` | `&#169;` |
| ® | `&reg;` | `&#174;` |
| ™ | `&trade;` | `&#8482;` |
| € | `&euro;` | `&#8364;` |
| £ | `&pound;` | `&#163;` |
| ¥ | `&yen;` | `&#165;` |
| ₹ | `&#8377;` | `&#8377;` |

---

# Example

```html
<p>5 &lt; 10</p>

<p>10 &gt; 5</p>

<p>Tom &amp; Jerry</p>

<p>&copy; 2026 My Website</p>

<p>Price: &#8377;499</p>
```

Output

```
5 < 10

10 > 5

Tom & Jerry

© 2026 My Website

Price: ₹499
```

---

# Non-Breaking Space (`&nbsp;`)

Normally, HTML ignores multiple spaces.

Example:

```html
<p>Hello     World</p>
```

Output:

```
Hello World
```

To preserve extra spaces, use `&nbsp;`.

Example:

```html
<p>Hello&nbsp;&nbsp;&nbsp;World</p>
```

Output:

```
Hello   World
```

---

# HTML Emojis

Emojis are characters from the **Unicode** standard.

Modern browsers support most emojis without requiring images.

Example:

```html
<p>😀 😍 🚀 ❤️ 🎉</p>
```

Output:

```
😀 😍 🚀 ❤️ 🎉
```

---

# Using Unicode Numbers

You can also display emojis using their Unicode number.

Syntax:

```html
&#xHEXCODE;
```

or

```html
&#DECIMAL;
```

Example:

```html
<p>&#128512;</p>
```

Output:

```
😀
```

---

# Common Emojis

| Emoji | Unicode |
|--------|----------|
| 😀 | `&#128512;` |
| 😂 | `&#128514;` |
| 😍 | `&#128525;` |
| 😎 | `&#128526;` |
| 😢 | `&#128546;` |
| 👍 | `&#128077;` |
| ❤️ | `&#10084;&#65039;` |
| 🎉 | `&#127881;` |
| 🚀 | `&#128640;` |
| 💻 | `&#128187;` |
| 🌍 | `&#127757;` |
| 🔥 | `&#128293;` |
| ⭐ | `&#11088;` |
| 📚 | `&#128218;` |

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>HTML Symbols & Emojis</title>
</head>

<body>

    <h1>HTML Symbols & Emojis</h1>

    <h2>Special Characters</h2>

    <p>5 &lt; 10</p>

    <p>10 &gt; 5</p>

    <p>Tom &amp; Jerry</p>

    <p>&copy; 2026 My Website</p>

    <p>&reg; Registered</p>

    <p>&trade; Trademark</p>

    <p>Price: &#8377;999</p>

    <h2>Extra Spaces</h2>

    <p>Hello&nbsp;&nbsp;&nbsp;World</p>

    <h2>Emojis</h2>

    <p>😀 😍 🚀 ❤️ 🎉</p>

    <p>&#128512; &#128525; &#128640;</p>

</body>

</html>
```

---

# Best Practices

- Use HTML entities for reserved characters like `<`, `>`, and `&`.
- Use `&nbsp;` only when you need to preserve spaces.
- Prefer Unicode emojis instead of images when possible.
- Include `<meta charset="UTF-8">` to ensure symbols and emojis display correctly.
- Test emojis across different devices, as their appearance may vary.

---

# Summary

| Item | Purpose |
|------|---------|
| `&lt;` | Displays `<` |
| `&gt;` | Displays `>` |
| `&amp;` | Displays `&` |
| `&quot;` | Displays `"` |
| `&apos;` | Displays `'` |
| `&nbsp;` | Inserts a non-breaking space |
| `&copy;` | Displays © |
| `&reg;` | Displays ® |
| `&trade;` | Displays ™ |
| `&#8377;` | Displays ₹ |
| Unicode Emoji | Displays emojis using Unicode characters |