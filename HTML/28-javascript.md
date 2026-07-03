# HTML + JavaScript (DOM Basics for Beginners)

JavaScript is a programming language that makes web pages **interactive and dynamic**.

* **HTML** → structure of the page
* **CSS** → styling of the page
* **JavaScript** → behavior and interactivity

Without JavaScript, a webpage is mostly static. With JavaScript, it can respond to user actions, update content, and behave like an application.

---

# What JavaScript Can Do

JavaScript can control almost everything inside a webpage:

* Update text and HTML content
* Change CSS styles dynamically
* Modify attributes (images, links, inputs, etc.)
* Respond to user actions (click, input, scroll)
* Validate forms before submission
* Show real-time data (date, time, calculations)
* Create animations and effects
* Communicate with servers without reloading (AJAX/fetch concept)

---

# How JavaScript Works in HTML

JavaScript runs inside the browser and interacts with the webpage using something called the **DOM (Document Object Model)**.

```text
HTML File
   ↓
Browser reads HTML
   ↓
Creates DOM Tree
   ↓
JavaScript modifies DOM
   ↓
Page updates instantly
```

---

# The `<script>` Tag

The `<script>` tag is used to add JavaScript to an HTML page.

## Basic Syntax

```html id="script-basic"
<script>
    // JavaScript code goes here
</script>
```

---

# Ways to Add JavaScript in HTML

There are **3 main ways**:

## 1. Internal JavaScript

JavaScript written inside the HTML file.

### Example

```html id="internal-js"
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

### What happens?

* Browser finds element with id `demo`
* Replaces its content with `"Hello JavaScript!"`

---

## 2. External JavaScript (Best Practice)

JavaScript is written in a separate `.js` file.

### HTML File

```html id="external-html"
<script src="script.js"></script>
```

### JavaScript File (`script.js`)

```javascript id="external-js"
document.getElementById("demo").innerHTML = "Hello JavaScript!";
```

### Why use external JS?

* Cleaner code
* Easier to maintain
* Reusable across pages
* Better project structure

---

## 3. Inline JavaScript (Not Recommended for large projects)

```html id="inline-js"
<button onclick="alert('Hello!')">Click</button>
```

Used only for small quick actions.

---

# DOM (Document Object Model)

JavaScript cannot directly edit HTML text. It first accesses the **DOM tree**.

## Example:

```html
<p id="demo">Original Text</p>
```

```javascript
document.getElementById("demo").innerHTML = "New Text";
```

### Before:

```
Original Text
```

### After:

```
New Text
```

---

# Core JavaScript DOM Methods

## 1. `document.getElementById()`

Selects an element using its `id`.

```javascript id="getbyid"
document.getElementById("demo");
```

---

## 2. `.innerHTML`

Changes content inside an element.

```javascript id="innerhtml"
document.getElementById("demo").innerHTML = "Updated Text";
```

---

## 3. `.style`

Changes CSS styles dynamically.

```javascript id="style-change"
document.getElementById("demo").style.color = "red";
document.getElementById("demo").style.fontSize = "30px";
document.getElementById("demo").style.backgroundColor = "yellow";
```

---

## 4. `.src`

Changes image or media source.

```html id="img-src"
<img id="image" src="bulb-off.png">
```

```javascript id="change-img"
document.getElementById("image").src = "bulb-on.png";
```

---

# Event Handling (User Interaction)

JavaScript becomes powerful when it reacts to user actions.

## Example: Button Click

```html id="click-event"
<button onclick="showMessage()">Click Me</button>

<p id="demo"></p>

<script>
function showMessage() {
    document.getElementById("demo").innerHTML = "Button Clicked!";
}
</script>
```

### Concept:

* User clicks button
* Function runs
* Page updates instantly

---

# Common Events

| Event         | Meaning                  |
| ------------- | ------------------------ |
| `onclick`     | When user clicks         |
| `onchange`    | When input value changes |
| `onmouseover` | When mouse hovers        |
| `onkeydown`   | When key is pressed      |
| `onload`      | When page loads          |

---

# Display Date & Time

JavaScript has a built-in `Date()` object.

```html id="datetime"
<button onclick="document.getElementById('time').innerHTML = Date()">
    Show Date & Time
</button>

<p id="time"></p>
```

---

# The `<noscript>` Tag

Used when JavaScript is disabled.

```html id="noscript"
<noscript>
    JavaScript is not supported or is disabled in your browser.
</noscript>
```

---

# Where to Place JavaScript?

## 1. Inside `<head>` (Not recommended for beginners)

```html
<head>
<script>
    // JS code
</script>
</head>
```

## 2. Before `</body>` (Recommended)

```html
<body>

    <!-- HTML content -->

    <script src="script.js"></script>
</body>
```

### Why this is best:

* HTML loads first
* Faster page rendering
* No blocking of content

---

# Complete Example (Real Page Behavior)

```html id="full-example"
<!DOCTYPE html>
<html>

<head>
    <title>JavaScript Demo</title>
</head>

<body>

    <h2 id="title">Welcome to HTML + JavaScript</h2>

    <img id="image" src="bulb-off.png" width="120">

    <br><br>

    <button onclick="changePage()">Click Me</button>

    <script>

        function changePage() {

            // Change text
            document.getElementById("title").innerHTML = "JavaScript Activated!";

            // Change color
            document.getElementById("title").style.color = "blue";

            // Change image
            document.getElementById("image").src = "bulb-on.png";

        }

    </script>

</body>

</html>
```

---

# Key Concepts Summary

| Concept            | Meaning                       |
| ------------------ | ----------------------------- |
| `<script>`         | Adds JavaScript to HTML       |
| DOM                | Structure of webpage elements |
| `getElementById()` | Selects HTML element          |
| `.innerHTML`       | Changes text/content          |
| `.style`           | Changes CSS dynamically       |
| `.src`             | Changes image source          |
| Events             | User interactions like click  |

---

# Best Practices

* Keep JavaScript in external files
* Use meaningful `id` names
* Place scripts at the bottom of the page
* Avoid mixing too much JS inside HTML tags
* Learn DOM concepts early (very important for projects)
* Think in terms of: **User action → JS function → DOM change**

---

If you want next upgrade, I can merge all your HTML notes into a **full structured HTML course (Chapter-wise like a textbook + roadmap + exercises + mini projects)**.
