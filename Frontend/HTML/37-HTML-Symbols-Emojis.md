# HTML Symbols & Emojis (Clean Beginner Notes)

HTML allows you to display **special symbols and emojis** using:

* HTML Entities
* Unicode characters
* Entity numbers (decimal/hex)

---

# Why Symbols & Emojis Need Special Handling

Some characters already have meaning in HTML:

* `<` → starts a tag
* `>` → ends a tag
* `&` → starts an entity

So they must be escaped using entities.

---

# 1. HTML Entity Syntax

## (a) Entity Name

```html id="entity-name"
&entityName;
```

Example:

```html id="pound-name"
&pound;
```

Output:
£

---

## (b) Entity Number

```html id="entity-number"
&#entityNumber;
```

Example:

```html id="pound-number"
&#163;
```

Output:
£

---

# 2. Common HTML Entities

| Character | Meaning            | Entity    |
| --------- | ------------------ | --------- |
| `<`       | Less than          | `&lt;`    |
| `>`       | Greater than       | `&gt;`    |
| `&`       | Ampersand          | `&amp;`   |
| `"`       | Double quote       | `&quot;`  |
| `'`       | Single quote       | `&apos;`  |
| space     | Non-breaking space | `&nbsp;`  |
| ©         | Copyright          | `&copy;`  |
| ®         | Registered         | `&reg;`   |
| ™         | Trademark          | `&trade;` |
| €         | Euro               | `&euro;`  |
| £         | Pound              | `&pound;` |
| ¥         | Yen                | `&yen;`   |
| ₹         | Rupee              | `&#8377;` |

---

# 3. Example (Special Characters)

```html id="symbols-example"
<p>5 &lt; 10</p>
<p>10 &gt; 5</p>
<p>Tom &amp; Jerry</p>
<p>&copy; 2026 My Website</p>
<p>Price: &#8377;499</p>
```

### Output:

5 < 10
10 > 5
Tom & Jerry
© 2026 My Website
Price: ₹499

---

# 4. Non-Breaking Space (`&nbsp;`)

HTML normally collapses multiple spaces into one.

```html id="normal-space"
<p>Hello     World</p>
```

Output:
Hello World

---

## Using `&nbsp;`

```html id="nbsp-example"
<p>Hello&nbsp;&nbsp;&nbsp;World</p>
```

Output:
Hello   World

### Use case:

* Prevent line breaks
* Add controlled spacing

---

# 5. HTML Emojis (Unicode)

Modern browsers support emojis using Unicode.

```html id="emoji-basic"
<p>😀 😍 🚀 ❤️ 🎉</p>
```

---

# 6. Emojis Using Unicode Numbers

## Decimal format

```html id="emoji-decimal"
<p>&#128512;</p>
```

Output:
😀

---

## Hex format

```html id="emoji-hex"
<p>&#x1F600;</p>
```

Output:
😀

---

# 7. Common Emojis

| Emoji | Code               |
| ----- | ------------------ |
| 😀    | `&#128512;`        |
| 😂    | `&#128514;`        |
| 😍    | `&#128525;`        |
| 😎    | `&#128526;`        |
| 😢    | `&#128546;`        |
| 👍    | `&#128077;`        |
| ❤️    | `&#10084;&#65039;` |
| 🎉    | `&#127881;`        |
| 🚀    | `&#128640;`        |
| 💻    | `&#128187;`        |
| 🌍    | `&#127757;`        |
| 🔥    | `&#128293;`        |
| ⭐     | `&#11088;`         |
| 📚    | `&#128218;`        |

---

# 8. Complete Example

```html id="full-example"
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Symbols & Emojis</title>
</head>

<body>

<h1>HTML Symbols & Emojis</h1>

<h2>Special Characters</h2>

<p>5 &lt; 10</p>
<p>10 &gt; 5</p>
<p>Tom &amp; Jerry</p>
<p>&copy; 2026 My Website</p>
<p>Price: &#8377;999</p>

<h2>Spaces</h2>
<p>Hello&nbsp;&nbsp;&nbsp;World</p>

<h2>Emojis</h2>
<p>😀 😍 🚀 ❤️ 🎉</p>
<p>&#128512; &#128525; &#128640;</p>

</body>

</html>
```

---

# 9. Best Practices

✔ Use `&lt;`, `&gt;`, `&amp;` for code display
✔ Use Unicode emojis instead of images
✔ Always include UTF-8:

```html
<meta charset="UTF-8">
```

✔ Use `&nbsp;` only when necessary
❌ Don’t use it for layout spacing

---

# 10. Key Takeaway

> Symbols and emojis in HTML are handled using entities and Unicode so the browser knows exactly how to display them safely.

---

If you want next step, I can combine ALL your notes into a **single structured “HTML Master Course” with chapters + revision sheets + interview questions + mini projects**.
