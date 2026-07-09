# HTML (HyperText Markup Language)

HTML (**HyperText Markup Language**) is the standard markup language used to create and structure web pages.

It describes **what appears on a webpage** and **how the content is organized**. Every website on the internet uses HTML as its foundation.

HTML was invented by **Sir Tim Berners-Lee**, the inventor of the World Wide Web (WWW).

> **Remember:** HTML is **not a programming language**. It is a **markup language** that uses tags to describe the structure of a webpage.

---

# What Does HTML Do?

HTML tells the browser how to display different types of content, such as:

- Headings
- Paragraphs
- Images
- Links
- Lists
- Tables
- Forms
- Videos
- Audio
- Buttons
- And much more...

For example:

```html
<h1>Welcome</h1>
<p>This is my first webpage.</p>
```

The browser understands these tags and displays:

# Welcome

This is my first webpage.

---

# HTML, CSS, and JavaScript

Modern websites are built using three core technologies.

| Technology | Purpose |
|------------|---------|
| **HTML** | Provides the structure of the webpage |
| **CSS** | Styles the webpage (colors, fonts, layouts, animations) |
| **JavaScript** | Adds interactivity and functionality |

Think of it like building a house:

```text
        Website
           │
 ┌─────────┼─────────┐
 │         │         │
 ▼         ▼         ▼
HTML      CSS   JavaScript
Structure Style  Functionality
```

Another simple analogy:

```text
Human Body

Bones  → HTML
Skin   → CSS
Muscles & Brain → JavaScript
```

---

# How HTML Works

When you open an HTML file, the browser reads the code from top to bottom.

The browser then creates the webpage that you see on the screen.

```text
HTML File
    │
    ▼
Web Browser
    │
    ▼
Reads HTML Tags
    │
    ▼
Builds the Web Page
    │
    ▼
Displays the Page
```

---

# Basic HTML Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>My First Web Page</title>
</head>

<body>

    <h1>My First Heading</h1>

    <p>My first paragraph.</p>

</body>

</html>
```

Output:

```text
My First Heading

My first paragraph.
```

---

# Understanding the Code

```html
<!DOCTYPE html>
```

- Declares that the document uses **HTML5**.
- Helps the browser display the webpage correctly.

---

```html
<html>
```

- The root element.
- Everything on the webpage is written inside this tag.

---

```html
<head>
```

Contains information **about the webpage**, such as:

- Title
- Meta tags
- CSS files
- JavaScript files
- Icons

The content inside `<head>` is **not displayed** on the webpage.

---

```html
<title>
```

Sets the title shown on the browser tab.

Example:

```html
<title>My Portfolio</title>
```

Browser tab:

```text
My Portfolio
```

---

```html
<body>
```

Contains everything that is visible on the webpage, including:

- Headings
- Paragraphs
- Images
- Buttons
- Tables
- Links
- Forms

---

```html
<h1>
```

Creates the largest heading.

---

```html
<p>
```

Creates a paragraph.

---

# Where Does JavaScript Go?

JavaScript is usually added using the `<script>` tag.

It can be placed:

- Inside the `<head>`
- At the end of the `<body>` (recommended in many cases)
- In a separate `.js` file

Example:

```html
<body>

    <h1>Hello</h1>

    <script>
        console.log("Hello World");
    </script>

</body>
```

---

# How to Create an HTML File

### Step 1

Open **Visual Studio Code**.

### Step 2

Create a new file.

### Step 3

Save it with the `.html` extension.

Example:

```text
index.html
```

Other examples:

```text
about.html
contact.html
login.html
portfolio.html
```

A browser recognizes any file ending with `.html` as an HTML document.

---

# How to Run an HTML File

There are multiple ways to open an HTML file.

### Method 1 (Simplest)

Double-click the `.html` file.

The default browser will open it.

---

### Method 2 (Recommended)

Install the **Live Server** extension in VS Code.

1. Open the HTML file.
2. Right-click inside the editor.
3. Click **Open with Live Server**.

This automatically refreshes the browser whenever you save the file.

---

# File Structure Example

```text
My Website/
│
├── index.html
├── about.html
├── contact.html
├── css/
│   └── style.css
├── js/
│   └── script.js
└── images/
    └── logo.png
```

---

# Key Points to Remember

- HTML stands for **HyperText Markup Language**.
- HTML is the standard language for creating web pages.
- HTML provides the **structure** of a webpage.
- HTML uses **tags** (elements) to describe content.
- HTML is **not** a programming language.
- CSS is used for styling.
- JavaScript is used for adding interactivity.
- Every HTML file should start with `<!DOCTYPE html>`.
- HTML files are saved using the `.html` extension.
- Browsers read HTML and convert it into the webpage you see.

---

# What's Next?

After learning what HTML is, the next topic is understanding the **basic structure of an HTML document**, where you'll learn about:

- `<!DOCTYPE html>`
- `<html>`
- `<head>`
- `<body>`
- How browsers interpret an HTML page
- The purpose of each section