# HTML Structure

Every HTML document follows a standard structure. This structure helps the browser understand how to display the webpage.

## Basic HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>

<body>
    <h1>Welcome</h1>
    <p>This is a basic HTML page.</p>
</body>
</html>
```

---

# Structure Explanation

## `<!DOCTYPE html>`

Declares that the document is an **HTML5** document. It must always be the first line of an HTML file.

---

## `<html>`

The root element of an HTML document. Every other HTML element is placed inside this tag.

Example:

```html
<html lang="en">
```

### `lang` Attribute

The `lang` attribute specifies the language of the webpage.

Example:

```html
<html lang="en">
```

Common values:

| Value | Language |
|--------|----------|
| `en` | English |
| `en-US` | English (United States) |
| `en-GB` | English (United Kingdom) |
| `fr` | French |
| `de` | German |
| `es` | Spanish |
| `hi` | Hindi |

---

## `<head>`

The `<head>` element contains information **about the webpage** that is not displayed on the page itself.

Common elements inside `<head>` include:

- `<title>`
- `<meta>`
- `<link>`
- `<style>`
- `<script>`

Example:

```html
<head>
    <title>My Website</title>
</head>
```

---

## `<meta>`

The `<meta>` tag provides metadata about the webpage.

### Character Encoding

```html
<meta charset="UTF-8">
```

Specifies that the webpage uses **UTF-8** character encoding, allowing it to display most languages and symbols correctly.

### Responsive Viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Ensures that the webpage scales properly on different screen sizes, especially mobile devices.

---

## `<title>`

Defines the title of the webpage.

The title appears:

- In the browser tab
- In bookmarks
- In search engine results

Example:

```html
<title>My Portfolio</title>
```

---

## `<body>`

The `<body>` element contains everything that is visible on the webpage.

Examples include:

- Headings
- Paragraphs
- Images
- Buttons
- Links
- Lists
- Tables
- Forms

Example:

```html
<body>
    <h1>Hello World</h1>
    <p>Welcome to HTML.</p>
</body>
```

---

## HTML Comments

Comments are ignored by the browser and are used to explain code.

Syntax:

```html
<!-- This is a comment -->
```

Example:

```html
<!-- Header Section -->
<header>
    ...
</header>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Structure</title>
</head>

<body>

    <h1>Welcome to HTML</h1>

    <p>This is a paragraph.</p>

</body>

</html>
```

---

# Summary

| Element | Purpose |
|----------|---------|
| `<!DOCTYPE html>` | Declares the document as HTML5 |
| `<html>` | Root element of the HTML document |
| `lang` | Specifies the language of the webpage |
| `<head>` | Contains metadata and page information |
| `<meta>` | Provides metadata such as encoding and viewport |
| `<title>` | Sets the browser tab title |
| `<body>` | Contains all visible webpage content |
| `<!-- -->` | Adds comments that are ignored by the browser |