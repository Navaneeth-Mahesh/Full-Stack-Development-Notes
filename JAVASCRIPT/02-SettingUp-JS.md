# Setting Up JavaScript

Before writing JavaScript code, you need a few basic tools.

Don't worry—setting up JavaScript is simple.

---

# What You Need

You only need:

- A web browser (Google Chrome is recommended)
- A code editor (Visual Studio Code is recommended)

---

# Install Visual Studio Code

Visual Studio Code (VS Code) is a free code editor used by millions of developers.

### Download

https://code.visualstudio.com/

After installing, open VS Code.

---

# Install Google Chrome

Most developers use Google Chrome because it has excellent developer tools.

### Download

https://www.google.com/chrome/

---

# Create Your Project Folder

Create a new folder anywhere on your computer.

Example:

```
JavaScript/
```

Inside it, create these files:

```
JavaScript/
│── index.html
│── script.js
```

---

# Connect JavaScript to HTML

Open **index.html** and write:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First JavaScript</title>
</head>
<body>

    <h1>Hello JavaScript!</h1>

    <script src="script.js"></script>

</body>
</html>
```

The `<script>` tag connects your JavaScript file to the HTML page.

---

# Write Your First JavaScript Code

Open **script.js** and write:

```javascript
console.log("Hello, JavaScript!");
```

---

# Run Your Code

1. Open **index.html** in your browser.
2. Right-click anywhere on the page.
3. Select **Inspect**.
4. Open the **Console** tab.

You should see:

```
Hello, JavaScript!
```

---

# Another Way to Write JavaScript

Instead of using a separate file, JavaScript can also be written directly inside the HTML file.

Example:

```html
<script>
    console.log("Hello!");
</script>
```

This is called **Internal JavaScript**.

However, for real projects, it's better to use a separate `.js` file.

---

# JavaScript in an External File (Recommended)

Example:

```html
<script src="script.js"></script>
```

This is called **External JavaScript**.

Benefits:
- Keeps your code organized
- Easier to maintain
- Can be reused across multiple pages

---

# Where Should the `<script>` Tag Go?

The recommended place is just before the closing `</body>` tag.

Example:

```html
<body>

    <h1>Welcome</h1>

    <script src="script.js"></script>

</body>
```

This ensures the HTML loads before the JavaScript runs.

---

# Using Live Server (Recommended)

Instead of opening the HTML file manually every time, you can use the **Live Server** extension in VS Code.

### Steps

1. Open VS Code.
2. Go to the **Extensions** tab.
3. Search for **Live Server**.
4. Install it.
5. Right-click **index.html**.
6. Click **Open with Live Server**.

Now your page will open in the browser, and it will automatically refresh whenever you save changes.

---

# Folder Structure

```
JavaScript/
│── index.html
│── script.js
```

As you learn more, your project may grow like this:

```
JavaScript/
│── index.html
│── script.js
│── style.css
│── images/
│── assets/
```

---

# Common Mistakes

Forgetting to link the JavaScript file.

```html
<script src="script.js"></script>
```

---

Misspelling the file name.

Example:

```html
<script src="scripts.js"></script>
```

If your file is named `script.js`, this will not work.

---

Placing the `<script>` tag in the wrong location without understanding when it runs.

For beginners, place it just before `</body>`.

---

# Summary

To start coding with JavaScript:

1. Install VS Code.
2. Install Google Chrome.
3. Create an `index.html` file.
4. Create a `script.js` file.
5. Link the JavaScript file using the `<script>` tag.
6. Write your code in `script.js`.
7. Open the browser and check the Console to see the output.

---

## Key Points

- JavaScript code is usually written in a `.js` file.
- Use the `<script src="script.js"></script>` tag to connect it to HTML.
- `console.log()` displays output in the browser's Console.
- The best place for the `<script>` tag is just before the closing `</body>` tag.
- Use the Live Server extension to make development easier.