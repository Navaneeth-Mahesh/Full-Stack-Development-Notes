# HTML Images

Images make web pages more attractive and help explain information visually. In HTML, images are added using the **`<img>`** element.

The `<img>` element is an **empty (self-closing) element**, meaning it **does not have a closing tag** because it doesn't contain any content.

---

# Basic Syntax

```html
<img src="image.jpg" alt="Description">
```

### Example

```html
<img src="nature.jpg" alt="Beautiful nature landscape">
```

### How it Works

```
<img
 ├── src → Location of the image
 └── alt → Text shown if the image cannot load
```

---

# The `src` Attribute

The **`src` (source)** attribute tells the browser where the image is located.

### 1. Image in the Same Folder

Project Structure

```
project/
│
├── index.html
└── logo.png
```

```html
<img src="logo.png" alt="Company Logo">
```

---

### 2. Image Inside a Folder

Project Structure

```
project/
│
├── index.html
└── images/
    └── logo.png
```

```html
<img src="images/logo.png" alt="Company Logo">
```

---

### 3. Image from Another Website

```html
<img
    src="https://example.com/image.jpg"
    alt="Sample Image">
```

> **Note:** Avoid hotlinking images from other websites. If the owner removes or changes the image, it will no longer appear on your website. Store important images in your own project whenever possible.

---

# The `alt` Attribute

The **`alt` (alternative text)** attribute describes the image.

It is used when:

* The image cannot be loaded.
* A screen reader reads the page for visually impaired users.
* Search engines analyze your webpage.

### Example

```html
<img
    src="cat.jpg"
    alt="A white cat sitting on a wooden chair">
```

### Good vs Bad `alt` Text

❌ Poor

```html
alt="image"
```

❌ Poor

```html
alt="photo"
```

✅ Better

```html
alt="Golden Retriever puppy playing with a ball"
```

> **Best Practice:** Write meaningful descriptions instead of generic words like "image" or "photo".

---

# Setting Image Size

You can control an image's size using the **`width`** and **`height`** attributes.

```html
<img
    src="nature.jpg"
    alt="Nature"
    width="400"
    height="250">
```

### Output

```
Width  → 400 pixels
Height → 250 pixels
```

The values are measured in **pixels (px)** by default.

---

# Setting Image Size Using CSS

Instead of HTML attributes, you can use CSS.

```html
<img
    src="nature.jpg"
    alt="Nature"
    style="width:400px; height:250px;">
```

### Which Should You Use?

| HTML Attributes                         | CSS                          |
| --------------------------------------- | ---------------------------- |
| Defines the image's actual display size | Better for styling           |
| Helps reduce layout shifts              | More flexible                |
| Good for basic HTML                     | Best for responsive websites |

---

# Making an Image Clickable

Wrap the `<img>` element inside an `<a>` element.

```html
<a href="https://example.com">

    <img
        src="logo.png"
        alt="Website Logo"
        width="120">

</a>
```

When users click the image, they are taken to the specified webpage.

---

# Animated Images (GIF)

GIF files work exactly like normal images.

```html
<img
    src="loading.gif"
    alt="Loading Animation">
```

Common uses:

* Loading animations
* Small illustrations
* Short looping animations

---

# Background Images

Background images are usually added using **CSS**, not the `<img>` element.

### Background for the Entire Page

```html
<body style="background-image: url('background.jpg');">

    <h1>Welcome</h1>

</body>
```

---

### Background for a Single Element

```html
<div
    style="
        background-image: url('background.jpg');
        width:300px;
        height:200px;">

    Content Here

</div>
```

> **Remember**
>
> * `<img>` displays an image as page content.
> * `background-image` places an image behind content.

---

# Image Paths

## Relative Path

A relative path points to a file inside your project.

```
project/
│
├── index.html
└── images/
    └── photo.jpg
```

```html
<img src="images/photo.jpg" alt="Photo">
```

---

## Absolute Path

An absolute path uses the complete URL.

```html
<img
    src="https://example.com/photo.jpg"
    alt="Photo">
```

---

# Lazy Loading (HTML5)

Modern browsers can delay loading images until they are about to appear on the screen.

```html
<img
    src="nature.jpg"
    alt="Nature"
    loading="lazy">
```

### Benefits

* Faster page loading
* Saves internet bandwidth
* Improves website performance

---

# Responsive Images Using `srcset`

Different devices have different screen sizes.

Instead of loading one large image for every device, you can let the browser choose the best image.

```html
<img
    src="small.jpg"
    srcset="
        small.jpg 500w,
        medium.jpg 1000w,
        large.jpg 1500w"
    alt="Nature">
```

The browser automatically selects the most suitable image.

---

# The `<picture>` Element

The `<picture>` element provides multiple versions of the same image.

The browser automatically chooses the best image based on screen size or supported image format.

```html
<picture>

    <source
        media="(min-width:900px)"
        srcset="large.jpg">

    <source
        media="(min-width:600px)"
        srcset="medium.jpg">

    <img
        src="small.jpg"
        alt="Nature">

</picture>
```

### Why Use `<picture>`?

* Responsive images
* Better performance
* Different images for different screen sizes
* Modern image formats (WebP, AVIF)

---

# The `<figure>` and `<figcaption>` Elements

Use these when an image needs a caption.

```html
<figure>

    <img
        src="mountain.jpg"
        alt="Mountain">

    <figcaption>
        Sunrise over the mountains.
    </figcaption>

</figure>
```

### Why Use Them?

* Better document structure
* Improved accessibility
* Easier styling with CSS

---

# HTML Image Maps

An image map lets different parts of an image act as different links.

## Step 1

```html
<img
    src="computer.jpg"
    alt="Computer"
    usemap="#workmap">
```

## Step 2

```html
<map name="workmap">

    <area
        shape="rect"
        coords="34,44,270,350"
        href="computer.html"
        alt="Computer">

    <area
        shape="circle"
        coords="337,300,44"
        href="phone.html"
        alt="Phone">

</map>
```

### Common Shapes

| Shape     | Description  |
| --------- | ------------ |
| `rect`    | Rectangle    |
| `circle`  | Circle       |
| `poly`    | Polygon      |
| `default` | Entire image |

---

# Common Image Formats

| Format           | Best Used For                                  |
| ---------------- | ---------------------------------------------- |
| `.jpg` / `.jpeg` | Photographs                                    |
| `.png`           | Images with transparency                       |
| `.gif`           | Simple animations                              |
| `.svg`           | Logos, icons, illustrations                    |
| `.webp`          | Modern compressed images                       |
| `.avif`          | High-quality images with excellent compression |

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

    <!-- Normal Image -->
    <img
        src="nature.jpg"
        alt="Beautiful Nature"
        width="400">

    <br><br>

    <!-- Clickable Image -->
    <a href="https://example.com">

        <img
            src="logo.png"
            alt="Website Logo"
            width="120">

    </a>

    <br><br>

    <!-- Responsive Image -->
    <picture>

        <source
            media="(min-width:800px)"
            srcset="large.jpg">

        <img
            src="small.jpg"
            alt="Responsive Image">

    </picture>

</body>

</html>
```

---

# Best Practices

* Always include the `alt` attribute.
* Use meaningful image names like `mountain-sunset.jpg` instead of `image1.jpg`.
* Compress large images before uploading.
* Prefer **WebP** or **AVIF** for better performance.
* Specify `width` and `height` to reduce layout shifts.
* Use `loading="lazy"` for images below the visible area.
* Use `<picture>` or `srcset` for responsive websites.
* Use CSS for background images.
* Use `<figure>` and `<figcaption>` when an image requires a caption.

---

# Common Beginner Mistakes

❌ Missing `alt`

```html
<img src="cat.jpg">
```

✅ Correct

```html
<img
    src="cat.jpg"
    alt="White cat sitting on a chair">
```

---

❌ Wrong File Path

```html
<img src="photo.jpg">
```

(File is actually inside the `images` folder.)

✅ Correct

```html
<img src="images/photo.jpg">
```

---

❌ Extremely Large Image

Uploading a 10 MB image will make your website slow.

✅ Compress the image before using it.

---

# Summary

| Element / Attribute | Purpose                                   |
| ------------------- | ----------------------------------------- |
| `<img>`             | Displays an image                         |
| `src`               | Specifies the image path or URL           |
| `alt`               | Provides alternative text                 |
| `width`             | Sets the image width                      |
| `height`            | Sets the image height                     |
| `loading="lazy"`    | Loads images only when needed             |
| `srcset`            | Provides multiple image sizes             |
| `<picture>`         | Displays responsive images                |
| `<source>`          | Specifies alternative image sources       |
| `<figure>`          | Groups an image with its caption          |
| `<figcaption>`      | Adds a caption to an image                |
| `<a>` + `<img>`     | Makes an image clickable                  |
| `background-image`  | Adds a background image using CSS         |
| `<map>`             | Defines an image map                      |
| `<area>`            | Defines clickable regions inside an image |
| `usemap`            | Connects an image to an image map         |

---

## Interview Questions

1. What is the purpose of the `alt` attribute?
2. What is the difference between relative and absolute image paths?
3. When should you use `<picture>` instead of `<img>`?
4. What is `loading="lazy"` and why is it useful?
5. What is the difference between `src` and `srcset`?
6. When would you use `<figure>` and `<figcaption>`?
7. Which image format is best for photographs? Logos? Transparent images?
8. What is an image map, and how does `usemap` work?
