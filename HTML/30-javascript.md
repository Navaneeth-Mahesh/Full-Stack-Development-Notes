# HTML JavaScript

JavaScript is a programming language that adds **interactivity and dynamic behavior** to web pages.

While **HTML** provides the structure of a webpage and **CSS** controls its appearance, **JavaScript** makes the webpage interactive by responding to user actions and updating content without reloading the page.

---

## What Can JavaScript Do?

JavaScript can:

- Change HTML content
- Change CSS styles
- Change HTML attributes
- Respond to user actions (clicks, typing, etc.)
- Validate forms
- Display the current date and time
- Create animations
- Communicate with servers without reloading the page

---

# The `<script>` Tag

The `<script>` tag is used to include JavaScript code in an HTML document.

JavaScript can be:

- Written directly inside the `<script>` tag (Internal JavaScript)
- Loaded from an external `.js` file using the `src` attribute

## Syntax

```html
<script>
    // JavaScript code goes here
</script>
```

---

# Internal JavaScript

Internal JavaScript is written inside the HTML document.

## Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>Internal JavaScript</title>
</head>

<body>

    <h2 id="demo">Hello World</h2>

    <script>
        document.getElementById("demo").innerHTML = "Hello JavaScript!";
    </script>

</body>

</html>
```

**Output:**

```
Hello JavaScript!
```

---

# External JavaScript

Instead of writing JavaScript inside the HTML file, you can place it in a separate `.js` file.

This keeps your code organized and easier to maintain.

## HTML File

```html
<script src="script.js"></script>
```

## JavaScript File (`script.js`)

```javascript
document.getElementById("demo").innerHTML = "Hello JavaScript!";
```

> **Best Practice:** Use external JavaScript files for larger projects.

---

# Understanding `document.getElementById()`

One of the most commonly used JavaScript methods is:

```javascript
document.getElementById("demo")
```

It finds an HTML element by its `id`.

Example:

```html
<p id="demo">Original Text</p>
```

```javascript
document.getElementById("demo").innerHTML = "New Text";
```

Result:

Before:

```
Original Text
```

After:

```
New Text
```

---

# Changing HTML Content

JavaScript can change the text inside an HTML element.

## Example

```html
<p id="demo">Welcome</p>

<script>
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>
```

---

# Changing CSS Styles

JavaScript can modify the style of an HTML element.

## Example

```html
<p id="demo">Hello World</p>

<script>
    document.getElementById("demo").style.fontSize = "30px";
    document.getElementById("demo").style.color = "red";
    document.getElementById("demo").style.backgroundColor = "yellow";
</script>
```

This changes:

- Font size
- Text color
- Background color

---

# Changing HTML Attributes

JavaScript can change an element's attributes.

Example: Changing an image.

## HTML

```html
<img id="image" src="bulb-off.png" alt="Bulb">
```

## JavaScript

```javascript
document.getElementById("image").src = "bulb-on.png";
```

The image changes from **bulb-off.png** to **bulb-on.png**.

---

# JavaScript with a Button

JavaScript often runs when a user interacts with the webpage.

## Example

```html
<button onclick="showMessage()">
    Click Me
</button>

<p id="demo"></p>

<script>
    function showMessage() {
        document.getElementById("demo").innerHTML = "Button Clicked!";
    }
</script>
```

When the button is clicked, the paragraph text changes.

---

# Display Current Date and Time

JavaScript can display the current date and time.

## Example

```html
<button
    onclick="document.getElementById('time').innerHTML = Date()">
    Show Date & Time
</button>

<p id="time"></p>
```

---

# The `<noscript>` Tag

The `<noscript>` tag displays alternative content if JavaScript is disabled or not supported by the browser.

## Example

```html
<script>
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
</script>

<noscript>
    Sorry, your browser does not support JavaScript or it is disabled.
</noscript>
```

---

# Where to Place JavaScript?

JavaScript can be placed in two locations.

## Inside `<head>`

```html
<head>
    <script>
        // JavaScript code
    </script>
</head>
```

## Before the Closing `</body>` Tag (Recommended)

```html
<body>

    ...

    <script src="script.js"></script>

</body>
```

> **Best Practice:** Place JavaScript just before the closing `</body>` tag. This allows the HTML to load first, improving page performance.

---

# Complete Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>HTML JavaScript Example</title>
</head>

<body>

    <h2 id="demo">Welcome to HTML</h2>

    <img
        id="image"
        src="bulb-off.png"
        alt="Bulb"
        width="150">

    <br><br>

    <button onclick="changeContent()">
        Click Me
    </button>

    <script>

        function changeContent() {

            document.getElementById("demo").innerHTML = "Hello JavaScript!";

            document.getElementById("demo").style.color = "blue";

            document.getElementById("image").src = "bulb-on.png";

        }

    </script>

    <noscript>
        JavaScript is disabled in your browser.
    </noscript>

</body>

</html>
```

---

# Summary

| Tag/Method | Purpose |
|------------|---------|
| `<script>` | Adds JavaScript to an HTML document |
| `src` | Links an external JavaScript file |
| `<noscript>` | Displays alternative content when JavaScript is disabled |
| `document.getElementById()` | Selects an element using its `id` |
| `.innerHTML` | Changes the HTML content of an element |
| `.style` | Changes CSS styles using JavaScript |
| `.src` | Changes the source of an image or other media |
| `onclick` | Executes JavaScript when an element is clicked |

---

# Best Practices

- Keep HTML, CSS, and JavaScript in separate files whenever possible.
- Place JavaScript before the closing `</body>` tag for better performance.
- Use meaningful `id` values so elements are easy to identify.
- Use external JavaScript files for larger projects.
- Avoid writing large amounts of inline JavaScript in HTML attributes.