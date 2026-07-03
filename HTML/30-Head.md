# HTML `<head>` Element (Organized Notes)

The `<head>` element is a container for **metadata** (information about the webpage).
This data is **not visible** on the page but is important for the browser, SEO, and performance.

---

# What is `<head>`?

* Placed inside `<html>` and before `<body>`
* Contains settings and information about the page
* Not shown directly on the webpage

## Structure

```html id="head-structure"
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Metadata goes here -->
</head>

<body>
    <!-- Visible content goes here -->
</body>

</html>
```

---

# How Browser Uses `<head>`

```text id="head-flow"
HTML File
   │
   ▼
<head> reads metadata
   │
   ├── Title → Browser Tab
   ├── Meta → SEO + Settings
   ├── Link → CSS / Icons
   ├── Script → JavaScript
   ▼
Body renders visible content
```

---

# Main Purpose of `<head>`

* Define page title
* Add SEO information
* Link CSS files
* Add JavaScript
* Configure mobile responsiveness
* Improve performance and sharing

---

# Important Elements Inside `<head>`

## 1. `<title>` (Page Title)

Defines the text shown in the browser tab.

### Syntax

```html id="title-syntax"
<title>My Portfolio</title>
```

### Example

```html id="title-example"
<head>
    <title>HTML Tutorial</title>
</head>
```

### Where it appears:

* Browser tab
* Bookmarks
* Search results

---

## 2. `<meta>` (Metadata)

Provides extra information about the page.

---

### (a) Character Encoding

```html id="charset"
<meta charset="UTF-8">
```

* Supports all languages and symbols
* Must be included in every page

---

### (b) Viewport (MOST IMPORTANT)

```html id="viewport"
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Why it is needed:

Without it:

* Mobile pages look zoomed out
* Text becomes too small

With it:

* Page becomes responsive
* Fits screen properly

---

### (c) Page Description (SEO)

```html id="description"
<meta name="description" content="Learn HTML from basics to advanced.">
```

* Shown in search results
* Helps SEO ranking

---

### (d) Keywords (Old SEO use)

```html id="keywords"
<meta name="keywords" content="HTML, CSS, JavaScript">
```

* Rarely used by modern search engines

---

### (e) Author

```html id="author"
<meta name="author" content="Navaneeth">
```

---

### (f) Auto Refresh

```html id="refresh"
<meta http-equiv="refresh" content="30">
```

* Refreshes page every 30 seconds

---

# 3. `<link>` (External Resources)

Used to connect external files like CSS or icons.

---

## CSS File Linking

```html id="css-link"
<link rel="stylesheet" href="style.css">
```

### Meaning:

| Attribute | Purpose              |
| --------- | -------------------- |
| `rel`     | Type of relationship |
| `href`    | File path            |

---

## Other Common `<link>` Uses

### Favicon (Website Icon)

```html id="favicon"
<link rel="icon" href="favicon.ico">
```

---

### Preloading (Performance)

```html id="preload"
<link rel="preload" href="style.css" as="style">
```

---

### DNS Prefetch (Faster loading external sites)

```html id="dns"
<link rel="dns-prefetch" href="https://example.com">
```

---

# 4. `<style>` (Internal CSS)

Used to write CSS inside HTML file.

```html id="internal-css"
<style>
    body {
        background-color: lightblue;
    }

    h1 {
        color: red;
    }
</style>
```

---

## When to use:

* Small projects
* Single-page designs

## Not recommended for:

* Large projects (use external CSS instead)

---

# 5. `<script>` (JavaScript)

Adds interactivity to the webpage.

---

## Basic Example

```html id="script-basic"
<script>
function greet() {
    alert("Hello!");
}
</script>
```

---

## Example with Button

```html id="script-example"
<p id="demo">Welcome</p>

<button onclick="greet()">Click Me</button>

<script>
function greet() {
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
}
</script>
```

---

## Best Practice (IMPORTANT)

### Use `defer` for better performance:

```html id="defer"
<script src="app.js" defer></script>
```

### Why?

* Loads HTML first
* Then runs JavaScript
* Faster page rendering

---

## async vs defer (Simple)

| Attribute | Behavior                         |
| --------- | -------------------------------- |
| `async`   | Runs immediately when downloaded |
| `defer`   | Runs after HTML is fully loaded  |

---

# 6. `<base>` (Default URL)

Sets default path for all relative links.

---

## Syntax

```html id="base"
<base href="https://example.com/" target="_blank">
```

---

## Example

```html id="base-example"
<head>
    <base href="https://www.example.com/" target="_blank">
</head>

<body>
    <a href="about.html">About</a>
</body>
```

### Result:

```
https://www.example.com/about.html
```

---

# Order of `<head>` Elements (Best Practice)

Recommended structure:

```html id="head-order"
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Page Title</title>

    <link rel="stylesheet" href="style.css">

    <script defer src="app.js"></script>
</head>
```

---

# Complete Example (Clean & Modern)

```html id="full-example"
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="description" content="HTML Head Element Tutorial">

    <meta name="author" content="Navaneeth">

    <title>HTML Head Guide</title>

    <link rel="stylesheet" href="style.css">

    <link rel="icon" href="favicon.ico">

    <script defer>
        function welcome() {
            alert("Welcome to HTML Learning!");
        }
    </script>
</head>

<body>

    <h1>HTML Head Section</h1>

    <button onclick="welcome()">Click Me</button>

</body>

</html>
```

---

# Common Mistakes

❌ Putting visible content inside `<head>`

```html
<head>
    <h1>Hello</h1>
</head>
```

✔ Only metadata belongs in `<head>`

---

❌ Missing viewport tag

✔ Always include:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

❌ Using too much internal CSS

✔ Prefer external CSS for real projects

---

# Key Takeaways

* `<head>` contains **non-visible metadata**
* It controls title, SEO, CSS, JS, and settings
* `<title>` defines browser tab name
* `<meta>` controls page behavior and SEO
* `<link>` connects external files
* `<style>` adds internal CSS
* `<script>` adds JavaScript
* `<base>` defines default URL for links
* Proper `<head>` improves performance and SEO

---

If you send the next file, I can also start merging everything into a **full HTML master notes document (like a mini course)**.
