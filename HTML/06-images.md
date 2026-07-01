# HTML Images

Images make webpages more attractive and help communicate information visually. In HTML, images are added using the `<img>` element.

The `<img>` element is an **empty element**, which means it does not have a closing tag.

---

# Basic Syntax

```html
<img src="image.jpg" alt="Description">
```

### Example

```html
<img src="nature.jpg" alt="Beautiful Nature">
```

---

# The `src` Attribute

The `src` (source) attribute specifies the path or URL of the image.

### Image in the Same Folder

```html
<img src="logo.png" alt="Logo">
```

### Image Inside a Folder

```html
<img src="images/logo.png" alt="Logo">
```

### Image from Another Website

```html
<img
    src="https://example.com/image.jpg"
    alt="Sample Image">
```

> **Note:** Hotlinking images from other websites is generally discouraged because the image owner may remove or change the file. Whenever possible, use images stored in your own project.

---

# The `alt` Attribute

The `alt` (alternative text) attribute describes the image.

It is displayed when:

- The image cannot be loaded.
- A screen reader is used by visually impaired users.
- Search engines analyze the webpage.

### Example

```html
<img
    src="cat.jpg"
    alt="A cute white cat sitting on a chair">
```

> **Best Practice:** Always provide meaningful alternative text for better accessibility.

---

# Setting Image Width and Height

You can specify the image dimensions using the `width` and `height` attributes.

### Example

```html
<img
    src="nature.jpg"
    alt="Nature"
    width="400"
    height="250">
```

> The values are measured in **pixels (px)** by default.

---

# Using CSS for Image Size

Instead of HTML attributes, you can also use CSS.

### Example

```html
<img
    src="nature.jpg"
    alt="Nature"
    style="width:400px; height:250px;">
```

---

# Image as a Link

Wrap the image inside an anchor (`<a>`) element to make it clickable.

### Example

```html
<a href="https://example.com">
    <img
        src="logo.png"
        alt="Website Logo"
        width="120">
</a>
```

---

# Animated Images (GIF)

GIF images can also be displayed using the `<img>` element.

### Example

```html
<img
    src="loading.gif"
    alt="Loading Animation">
```

---

# Image Paths

## Relative Path

Points to an image within your project.

```html
<img src="images/photo.jpg" alt="Photo">
```

## Absolute Path

Points to an image using a complete URL.

```html
<img
    src="https://example.com/photo.jpg"
    alt="Photo">
```

---

# Common Image Formats

| Format | Description |
|---------|-------------|
| `.jpg` / `.jpeg` | Best for photographs |
| `.png` | Supports transparent backgrounds |
| `.gif` | Supports simple animations |
| `.svg` | Scalable vector graphics without quality loss |
| `.webp` | Modern format with high quality and smaller file sizes |

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Images</title>
</head>
<body>

    <h1>HTML Image Examples</h1>

    <img
        src="nature.jpg"
        alt="Beautiful Nature"
        width="400">

    <br><br>

    <img
        src="images/logo.png"
        alt="Company Logo"
        width="150">

    <br><br>

    <a href="https://example.com">
        <img
            src="logo.png"
            alt="Clickable Logo"
            width="120">
    </a>

</body>
</html>
```

---

# Best Practices

- Always include the `alt` attribute.
- Use descriptive file names (e.g., `mountain-sunset.jpg` instead of `image1.jpg`).
- Optimize images to reduce file size and improve page loading speed.
- Use relative paths for images stored within your project.
- Specify image dimensions to reduce layout shifts while the page loads.

---

# Summary

| Attribute | Purpose |
|-----------|---------|
| `<img>` | Displays an image |
| `src` | Specifies the image path or URL |
| `alt` | Provides alternative text for accessibility |
| `width` | Sets the image width |
| `height` | Sets the image height |
| `style` | Applies CSS styling to the image |
| `<a>` + `<img>` | Makes an image clickable |