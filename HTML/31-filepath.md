# HTML File Paths

A **file path** tells the browser where to find a file, such as an image, CSS file, JavaScript file, video, or another HTML page.

Whenever you use files in HTML, you specify their location using a file path.

---

# Why Are File Paths Important?

File paths help the browser locate resources used in your webpage, such as:

- Images
- CSS files
- JavaScript files
- Videos
- Audio files
- Other HTML pages

Example:

```html
<img src="images/logo.png" alt="Logo">
```

Here, `images/logo.png` is the file path.

---

# Types of File Paths

There are two main types of file paths:

1. Relative File Path
2. Absolute File Path

---

# Relative File Path

A **relative file path** points to a file based on the location of the current HTML file.

It is the most commonly used type of file path in web development.

## Example Folder Structure

```text
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

## File in the Same Folder

If the file is in the same folder as the HTML file:

```html
<a href="about.html">About</a>
```

```
project/
│
├── index.html
└── about.html
```

---

## File Inside a Folder

If the file is inside another folder:

```html
<img src="images/logo.png" alt="Logo">
```

```
project/
│
├── index.html
└── images/
    └── logo.png
```

---

## File Inside a Nested Folder

```html
<img src="assets/images/logo.png" alt="Logo">
```

```
project/
│
├── index.html
└── assets/
    └── images/
        └── logo.png
```

---

## File in the Parent Folder

Use `..` to move up one folder.

Example:

```html
<img src="../logo.png" alt="Logo">
```

Folder structure:

```text
project/
│
├── logo.png
└── pages/
    └── about.html
```

Since `about.html` is inside the `pages` folder, `../` moves one level up to the `project` folder.

---

## Moving Up Multiple Folders

Each `../` moves up one directory.

Example:

```html
<img src="../../images/logo.png" alt="Logo">
```

Folder structure:

```text
project/
│
├── images/
│   └── logo.png
└── pages/
    └── blog/
        └── article.html
```

Explanation:

- First `../` → moves from `blog` to `pages`
- Second `../` → moves from `pages` to `project`
- Then enters the `images` folder

---

# Absolute File Path

An **absolute file path** specifies the complete location of a file.

Example:

```html
<img
    src="https://example.com/images/logo.png"
    alt="Logo">
```

Absolute paths are commonly used for:

- Images hosted online
- External CSS libraries
- External JavaScript libraries

---

# Linking CSS Files

```html
<link rel="stylesheet" href="css/style.css">
```

Folder structure:

```text
project/
│
├── index.html
└── css/
    └── style.css
```

---

# Linking JavaScript Files

```html
<script src="js/script.js"></script>
```

Folder structure:

```text
project/
│
├── index.html
└── js/
    └── script.js
```

---

# Linking Another HTML Page

```html
<a href="contact.html">
    Contact Us
</a>
```

---

# Using Images

```html
<img
    src="images/profile.jpg"
    alt="Profile Picture">
```

---

# Relative vs Absolute File Paths

| Relative Path | Absolute Path |
|---------------|---------------|
| Based on the current file's location | Uses the complete URL or file location |
| Easier to move an entire project | May break if the external resource changes |
| Commonly used in projects | Commonly used for external resources |
| Works offline | Usually requires an internet connection for online resources |

---

# Best Practices

- Organize files into folders such as `images`, `css`, and `js`.
- Use **relative paths** for files within your project.
- Use meaningful file and folder names.
- Avoid spaces in file names. Use hyphens (`-`) or underscores (`_`) instead.
- Keep your project structure organized as it grows.

---

# Example Project Structure

```text
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

# Summary

| File Path | Description |
|-----------|-------------|
| `about.html` | File in the same folder |
| `images/logo.png` | File inside a folder |
| `assets/images/logo.png` | File inside nested folders |
| `../logo.png` | File in the parent folder |
| `../../images/logo.png` | Move up multiple folders |
| `https://example.com/image.jpg` | Absolute path (external resource) |