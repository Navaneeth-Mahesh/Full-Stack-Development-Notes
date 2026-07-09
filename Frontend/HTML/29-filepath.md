# HTML File Paths (Beginner Notes)

A **file path** tells the browser where to find a file used in a webpage. These files can be images, CSS, JavaScript, videos, audio, or even other HTML pages.

Whenever you link or embed a file in HTML, you must specify its correct path so the browser can locate it.

---

# Why File Paths Matter

File paths are used whenever your webpage needs external resources like:

* Images
* CSS stylesheets
* JavaScript files
* Videos and audio
* Other HTML pages

Example:

```html
<img src="images/logo.png" alt="Logo">
```

Here, `images/logo.png` is the file path that tells the browser:

> “Go inside the images folder and get logo.png”

---

# Types of File Paths

HTML supports two main types of file paths:

1. Relative File Path
2. Absolute File Path

---

# Relative File Path

A **relative file path** is based on the location of your current HTML file.

It is the most commonly used approach in real projects because it keeps everything portable.

---

## Example Project Structure

```text id="proj1"
project/
│
├── index.html
├── about.html
├── images/
│   ├── logo.png
│   └── banner.jpg
├── css/
│   └── style.css
└── js/
    └── script.js
```

---

## 1. File in the Same Folder

If both files are in the same folder:

```html
<a href="about.html">About</a>
```

```text id="same1"
index.html → about.html
```

---

## 2. File Inside a Folder

If the file is inside a folder:

```html
<img src="images/logo.png" alt="Logo">
```

```text id="folder1"
index.html → images/logo.png
```

Meaning:

* Go into `images/`
* Then open `logo.png`

---

## 3. File Inside Nested Folders

```html
<img src="assets/images/logo.png" alt="Logo">
```

```text id="nested1"
index.html → assets → images → logo.png
```

---

## 4. File in Parent Folder (`..`)

`..` means move **one folder up**

```html
<img src="../logo.png" alt="Logo">
```

Folder structure:

```text id="parent1"
project/
│
├── logo.png
└── pages/
    └── about.html
```

Explanation:

* `about.html` is inside `pages/`
* `../` moves you back to `project/`
* Then it finds `logo.png`

---

## 5. Moving Up Multiple Levels

Each `../` moves up one folder.

```html
<img src="../../images/logo.png" alt="Logo">
```

```text id="multiup1"
project/
│
├── images/
│   └── logo.png
└── pages/
    └── blog/
        └── article.html
```

Steps:

* `../` → blog → pages
* `../` → pages → project
* then go to `images/logo.png`

---

# Absolute File Path

An **absolute path** gives the full location of a file, usually starting from a domain or full URL.

```html
<img src="https://example.com/images/logo.png" alt="Logo">
```

This tells the browser:

> “Go to this website and fetch the file directly.”

---

## Where Absolute Paths Are Used

* Images from websites (CDNs)
* External libraries (CSS/JS)
* APIs or hosted assets

---

# Linking CSS Files

```html
<link rel="stylesheet" href="css/style.css">
```

```text id="css1"
index.html → css/style.css
```

---

# Linking JavaScript Files

```html
<script src="js/script.js"></script>
```

```text id="js1"
index.html → js/script.js
```

---

# Linking Another HTML Page

```html
<a href="contact.html">Contact Us</a>
```

Used for navigation between pages inside your project.

---

# Using Images

```html
<img src="images/profile.jpg" alt="Profile Picture">
```

Always include:

* `src` → file path
* `alt` → fallback text (important for accessibility)

---

# Relative vs Absolute Paths

| Feature           | Relative Path             | Absolute Path          |
| ----------------- | ------------------------- | ---------------------- |
| Based on          | Current file location     | Full URL or full path  |
| Portability       | High (moves with project) | Low (can break easily) |
| Usage             | Local project files       | External resources     |
| Internet required | No                        | Usually yes            |

---

# Best Practices

* Keep files organized in folders:

  * `images/`
  * `css/`
  * `js/`
* Always prefer **relative paths** for project files
* Avoid spaces in filenames (`my image.png` ❌ → `my-image.png` ✔)
* Use lowercase file names for consistency
* Structure projects clearly for scalability

---

# Recommended Project Structure

```text id="structure1"
my-website/
│
├── index.html
├── about.html
├── contact.html
│
├── images/
│   ├── logo.png
│   ├── banner.jpg
│   └── profile.png
│
├── css/
│   └── style.css
│
├── js/
│   └── script.js
│
└── assets/
    ├── videos/
    └── audio/
```

---

# Quick Summary

| Path                     | Meaning                 |
| ------------------------ | ----------------------- |
| `about.html`             | Same folder             |
| `images/logo.png`        | Inside folder           |
| `assets/images/logo.png` | Nested folders          |
| `../logo.png`            | Parent folder           |
| `../../images/logo.png`  | Move up multiple levels |
| `https://...`            | External resource       |

---

If you send the next `.md` file, I’ll keep building this into a complete structured HTML notes system (like a mini textbook).
