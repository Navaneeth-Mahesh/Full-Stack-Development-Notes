# HTML `<head>` Element

The `<head>` element contains **metadata** (information about the webpage) that is **not displayed** in the browser window.

It is placed between the `<html>` and `<body>` elements.

```html
<!DOCTYPE html>
<html>

<head>
    <!-- Metadata goes here -->
</head>

<body>
    <!-- Visible content goes here -->
</body>

</html>
```

> **Note:** Everything inside the `<head>` helps the browser, search engines, and other services understand the webpage.

---

# Common Elements Inside `<head>`

The `<head>` section commonly contains:

- `<title>`
- `<meta>`
- `<link>`
- `<style>`
- `<script>`
- `<base>`

---

# 1. `<title>` Element

The `<title>` element defines the title of the webpage.

The title appears:

- In the browser tab
- In bookmarks
- In search engine results

## Syntax

```html
<title>My Portfolio</title>
```

## Example

```html
<head>
    <title>HTML Tutorial</title>
</head>
```

---

# 2. `<style>` Element

The `<style>` element is used to write **Internal CSS**.

It allows you to style a single HTML page without creating a separate CSS file.

## Syntax

```html
<style>
    selector {
        property: value;
    }
</style>
```

## Example

```html
<head>
    <style>
        body {
            background-color: powderblue;
        }

        h1 {
            color: red;
        }

        p {
            color: blue;
        }
    </style>
</head>
```

### Output

- Background becomes powder blue.
- Heading becomes red.
- Paragraph becomes blue.

> **Note:** Internal CSS only affects the current HTML page.

---

# 3. `<link>` Element

The `<link>` element connects the HTML document to an external resource.

It is most commonly used to link an external CSS file.

## Syntax

```html
<link rel="stylesheet" href="style.css">
```

## Example

```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

### Attributes

| Attribute | Description |
|-----------|-------------|
| `rel` | Specifies the relationship between the document and the linked file. |
| `href` | Specifies the path to the external file. |

> **Best Practice:** Use external CSS (`<link>`) for projects with multiple pages because it keeps your HTML clean and allows the same stylesheet to be reused.

---

# 4. `<meta>` Element

The `<meta>` element provides **metadata** about the webpage.

Metadata is not displayed on the webpage but is used by:

- Browsers
- Search engines
- Social media platforms
- Other web services

---

## Character Encoding

Defines the character encoding used by the webpage.

```html
<meta charset="UTF-8">
```

`UTF-8` supports almost all languages and special characters.

---

## Page Description

Provides a short description of the webpage.

```html
<meta
    name="description"
    content="Learn HTML from beginner to advanced.">
```

Search engines may display this description in search results.

---

## Keywords

Specifies keywords related to the webpage.

```html
<meta
    name="keywords"
    content="HTML, CSS, JavaScript">
```

> **Note:** Modern search engines place little or no importance on the `keywords` meta tag for ranking.

---

## Author

Specifies the author of the webpage.

```html
<meta
    name="author"
    content="Navaneeth">
```

---

## Auto Refresh

Refreshes the webpage automatically after a specified number of seconds.

```html
<meta
    http-equiv="refresh"
    content="30">
```

This refreshes the page every **30 seconds**.

---

# Viewport Meta Tag

One of the most important meta tags for modern websites.

```html
<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0">
```

## Why is it Important?

Different devices have different screen sizes.

Without this tag:

- Mobile websites may appear zoomed out.
- Text can become difficult to read.
- Layouts may not fit the screen properly.

With this tag:

- The webpage adapts to the device width.
- Mobile users get a better viewing experience.
- Responsive layouts work correctly.

### Explanation

```text
width=device-width
```

Makes the webpage width match the device's screen width.

```text
initial-scale=1.0
```

Sets the initial zoom level to 100%.

> **Best Practice:** Include the viewport meta tag in every modern webpage.

---

# 5. `<script>` Element

The `<script>` element is used to add **JavaScript** to an HTML page.

JavaScript makes webpages interactive.

## Example

```html
<script>
function greet() {
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
}
</script>
```

### Example with HTML

```html
<p id="demo">Welcome</p>

<button onclick="greet()">
    Click Me
</button>

<script>
function greet() {
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
}
</script>
```

> JavaScript is usually placed just before the closing `</body>` tag for better page loading performance, though it can also be included in the `<head>`.

---

# 6. `<base>` Element

The `<base>` element specifies a default URL and/or default target for all relative URLs in the document.

There can only be **one** `<base>` element in an HTML document.

## Syntax

```html
<base
    href="https://example.com/"
    target="_blank">
```

## Example

```html
<head>

    <base
        href="https://www.example.com/"
        target="_blank">

</head>

<body>

    <a href="about.html">
        About
    </a>

</body>
```

The browser treats the link as:

```
https://www.example.com/about.html
```

It also opens the link in a new tab because of:

```html
target="_blank"
```

### Attributes

| Attribute | Description |
|-----------|-------------|
| `href` | Sets the base URL for all relative links |
| `target` | Sets the default target for all links |

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

    <meta
        name="description"
        content="HTML Head Elements Tutorial">

    <meta
        name="author"
        content="Navaneeth">

    <title>HTML Head Example</title>

    <link
        rel="stylesheet"
        href="style.css">

    <style>
        h1 {
            color: blue;
        }
    </style>

    <script>
        function welcome() {
            alert("Welcome to HTML!");
        }
    </script>

</head>

<body>

    <h1>HTML Head Elements</h1>

    <button onclick="welcome()">
        Click Me
    </button>

</body>

</html>
```

---

# Summary

| Element | Purpose |
|---------|---------|
| `<head>` | Contains metadata about the webpage |
| `<title>` | Sets the browser tab title |
| `<style>` | Adds internal CSS |
| `<link>` | Links external resources such as CSS files |
| `<meta charset="UTF-8">` | Sets the character encoding |
| `<meta name="description">` | Describes the webpage |
| `<meta name="keywords">` | Specifies webpage keywords |
| `<meta name="author">` | Specifies the webpage author |
| `<meta http-equiv="refresh">` | Refreshes the webpage automatically |
| `<meta name="viewport">` | Makes webpages responsive on different devices |
| `<script>` | Adds JavaScript to the webpage |
| `<base>` | Sets the default URL or target for relative links |