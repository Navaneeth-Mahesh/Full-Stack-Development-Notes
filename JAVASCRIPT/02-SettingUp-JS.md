# Setting Up JavaScript

Before writing JavaScript programs, you need to set up a proper development environment. Fortunately, JavaScript is one of the easiest programming languages to get started with because every modern web browser already includes a JavaScript engine.

In this chapter, you'll learn how to set up JavaScript using a web browser, Visual Studio Code, and Node.js, along with different ways to run JavaScript code.

---

# Browser Environment

A **browser environment** is the environment where JavaScript runs inside a web browser.

Every modern browser has a built-in JavaScript engine that executes JavaScript code.

Popular browsers include:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox
* Safari
* Opera

The browser provides additional features such as:

* DOM (Document Object Model)
* BOM (Browser Object Model)
* Web APIs
* Local Storage
* Session Storage
* Fetch API
* Timers (`setTimeout`, `setInterval`)

These features allow JavaScript to interact with web pages.

---

## Browser Architecture

```text
Your JavaScript Code
          │
          ▼
Browser
          │
          ▼
JavaScript Engine
          │
          ▼
DOM + Web APIs
          │
          ▼
Update Webpage
```

---

## Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Example</title>
</head>
<body>

<h1>Hello JavaScript</h1>

<script>
    alert("Welcome to JavaScript!");
</script>

</body>
</html>
```

When you open this HTML file in a browser, the JavaScript code runs automatically.

---

# VS Code Setup

**Visual Studio Code (VS Code)** is one of the most popular code editors for JavaScript development.

It provides:

* Syntax highlighting
* Auto-completion (IntelliSense)
* Error detection
* Extensions
* Integrated Terminal
* Git support
* Debugging tools

---

## Step 1: Install VS Code

1. Visit the official Visual Studio Code website.
2. Download the installer for your operating system.
3. Run the installer.
4. Complete the installation.

---

## Step 2: Open VS Code

After installation:

* Open VS Code.
* Create a new folder for your project.
* Open the folder in VS Code.

Example:

```
JavaScript/
```

---

## Step 3: Create Files

Create these files:

```
JavaScript/

│── index.html
│── script.js
```

---

## Recommended Extensions

Some useful VS Code extensions for JavaScript development are:

* ESLint
* Prettier
* Live Server
* JavaScript (ES6) Code Snippets
* Error Lens
* GitLens
* Path Intellisense

---

# Node.js Installation

**Node.js** is a JavaScript runtime that allows JavaScript to run outside the browser.

Before Node.js, JavaScript could only run inside web browsers.

With Node.js, you can build:

* Servers
* APIs
* Backend applications
* Command-line tools
* Real-time applications

---

## Install Node.js

### Step 1

Go to the official Node.js website.

Download the **LTS (Long-Term Support)** version because it is the most stable version.

---

### Step 2

Run the installer.

Keep the default installation settings.

---

### Step 3

Finish the installation.

---

## Verify Installation

Open Command Prompt or Terminal.

Check the Node.js version:

```bash
node -v
```

Example:

```bash
v22.5.1
```

Check the npm version:

```bash
npm -v
```

Example:

```bash
10.8.2
```

If both commands display version numbers, Node.js is installed successfully.

---

## What is npm?

**npm (Node Package Manager)** is installed automatically with Node.js.

It is used to:

* Install packages
* Update packages
* Remove packages
* Manage project dependencies

Example:

```bash
npm install express
```

---

# Running JavaScript

JavaScript can be executed in multiple ways.

---

## Method 1: Inside the Browser

Create an HTML file.

```html
<!DOCTYPE html>
<html>
<body>

<script>
    console.log("Hello JavaScript");
</script>

</body>
</html>
```

Open the HTML file in a browser.

The JavaScript code will execute automatically.

---

## Method 2: Using Node.js

Create a file:

```
app.js
```

Example:

```javascript
console.log("Hello Node.js");
```

Run:

```bash
node app.js
```

Output:

```
Hello Node.js
```

---

## Method 3: Browser Console

Open the browser.

Press:

```
F12
```

or

```
Ctrl + Shift + I
```

Open the **Console** tab.

Type:

```javascript
console.log("Hello");
```

Press:

```
Enter
```

Output:

```
Hello
```

---

## Method 4: VS Code Terminal

Open Terminal:

```
Ctrl + `
```

Run:

```bash
node filename.js
```

Example:

```bash
node script.js
```

---

# Console

The **console** is a debugging tool used to display information while a JavaScript program is running.

It is mainly used by developers to:

* Print values
* Find errors
* Test code
* Debug applications

---

## console.log()

Prints information.

```javascript
console.log("Hello");
```

Output:

```
Hello
```

---

## console.error()

Displays an error message.

```javascript
console.error("Something went wrong");
```

---

## console.warn()

Displays a warning.

```javascript
console.warn("Warning!");
```

---

## console.table()

Displays data as a table.

```javascript
const student = {
    name: "Navaneeth",
    age: 19,
    course: "B.Tech"
};

console.table(student);
```

---

## console.clear()

Clears the console.

```javascript
console.clear();
```

---

## console.time()

Measures execution time.

```javascript
console.time("Timer");

for (let i = 0; i < 1000000; i++) {}

console.timeEnd("Timer");
```

Example Output:

```
Timer: 2.4ms
```

---

# Developer Tools

Every modern browser provides **Developer Tools (DevTools)**.

These tools help developers inspect, debug, and optimize websites.

---

## Open Developer Tools

### Chrome / Edge

```
F12
```

or

```
Ctrl + Shift + I
```

---

### Firefox

```
F12
```

---

## Important Tabs

### Elements

Inspect and edit HTML and CSS.

---

### Console

Run JavaScript code and view logs or errors.

---

### Sources

View JavaScript files.

Set breakpoints for debugging.

---

### Network

Monitor:

* API requests
* Images
* CSS files
* JavaScript files
* Response times

---

### Application

View:

* Cookies
* Local Storage
* Session Storage
* IndexedDB

---

### Performance

Analyze webpage speed and performance.

---

# Script Tag

The `<script>` tag is used to include JavaScript in an HTML document.

---

## Syntax

```html
<script>
    JavaScript Code
</script>
```

---

## Example

```html
<!DOCTYPE html>
<html>
<body>

<h1>Hello</h1>

<script>
    alert("Welcome!");
</script>

</body>
</html>
```

---

## Where to Place the `<script>` Tag?

### Inside `<head>`

```html
<head>
    <script>
        console.log("Head");
    </script>
</head>
```

The script runs while the page is loading. If it tries to access HTML elements that haven't loaded yet, it may cause errors.

---

### Before `</body>` (Recommended)

```html
<body>

<h1>Hello</h1>

<script>
    console.log("Body");
</script>

</body>
```

This is recommended because the HTML content loads first, then the JavaScript executes.

---

## Using `defer`

```html
<head>
    <script src="script.js" defer></script>
</head>
```

The browser downloads the script while parsing HTML but waits to execute it until the HTML document has been fully parsed. This is the recommended approach for most external scripts.

---

## Using `async`

```html
<head>
    <script src="script.js" async></script>
</head>
```

The browser downloads the script in parallel and executes it as soon as it finishes downloading. This is useful for independent scripts but not for scripts that depend on the HTML or on other scripts.

---

## Difference Between `defer` and `async`

| Feature                    | `defer`              | `async`                               |
| -------------------------- | -------------------- | ------------------------------------- |
| Downloads in parallel      | Yes                  | Yes                                   |
| Waits until HTML is parsed | Yes                  | No                                    |
| Maintains script order     | Yes                  | No                                    |
| Best for                   | Most website scripts | Independent scripts (e.g., analytics) |

---

# External JavaScript Files

Instead of writing JavaScript directly inside HTML, you can store it in a separate `.js` file.

Example:

```
project/

│── index.html
│── script.js
```

---

## script.js

```javascript
console.log("Hello JavaScript");
```

---

## index.html

```html
<!DOCTYPE html>
<html>
<body>

<script src="script.js"></script>

</body>
</html>
```

The browser loads and executes the JavaScript file.

---

## Advantages of External Files

* Better code organization
* Easier maintenance
* Reusable across multiple pages
* Improved readability
* Browser caching improves performance

---

# Strict Mode

**Strict Mode** is a special mode in JavaScript that enforces stricter parsing and error handling. It helps you write cleaner, safer, and more reliable code by preventing common mistakes.

Strict Mode is enabled by adding the following statement at the beginning of a script or function:

```javascript
"use strict";
```

---

## Example Without Strict Mode

```javascript
name = "Navaneeth";

console.log(name);
```

This works because JavaScript automatically creates a global variable, even though it wasn't declared.

---

## Example With Strict Mode

```javascript
"use strict";

name = "Navaneeth";

console.log(name);
```

Output:

```
ReferenceError: name is not defined
```

Strict Mode prevents the accidental creation of global variables.

---

## Strict Mode Example

```javascript
"use strict";

let age = 19;

console.log(age);
```

Output:

```
19
```

---

## Benefits of Strict Mode

* Prevents accidental global variables
* Catches common coding mistakes
* Makes debugging easier
* Encourages better coding practices
* Improves code reliability
* Helps write code that is easier to maintain

---

## When to Use Strict Mode

* For modern JavaScript projects, always use Strict Mode unless your build tools already enable it automatically (for example, ES Modules are always in strict mode).
* Place `"use strict";` at the top of your script or function if you're writing traditional JavaScript files.

---

# Summary

After completing this chapter, you should understand:

* What a browser environment is and how JavaScript runs inside it.
* How to install and configure Visual Studio Code.
* How to install Node.js and verify the installation.
* Different ways to run JavaScript using the browser, Node.js, and VS Code.
* How to use the console for debugging.
* How to use browser Developer Tools effectively.
* How to include JavaScript using the `<script>` tag.
* How to organize code with external JavaScript files.
* Why Strict Mode is important and how it helps write safer JavaScript code.
