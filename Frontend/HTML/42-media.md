# HTML Media

HTML provides several elements for displaying and embedding media such as images, audio, videos, YouTube videos, and external content. These elements make web pages more interactive and engaging.

---

# HTML Image (`<img>`)

The `<img>` element is used to display an image on a webpage.

## Syntax

```html
<img src="image.jpg" alt="Description">
```

## Example

```html
<img
    src="images/html-logo.png"
    alt="HTML Logo"
    width="200"
    height="200">
```

### Common Attributes

| Attribute | Description |
|-----------|-------------|
| `src` | Path or URL of the image |
| `alt` | Alternative text if the image cannot be displayed |
| `width` | Sets the image width |
| `height` | Sets the image height |

---

# HTML Video (`<video>`)

The `<video>` element is used to embed videos in a webpage.

## Syntax

```html
<video controls>
    <source src="video.mp4" type="video/mp4">
</video>
```

## Example

```html
<video width="500" controls>
    <source src="videos/demo.mp4" type="video/mp4">

    Your browser does not support the video tag.
</video>
```

## Common Attributes

| Attribute | Description |
|-----------|-------------|
| `controls` | Displays video controls |
| `autoplay` | Plays the video automatically |
| `muted` | Starts the video without sound |
| `loop` | Repeats the video continuously |
| `width` | Sets the video width |
| `height` | Sets the video height |
| `poster` | Displays an image before the video starts |

### Example

```html
<video
    width="500"
    controls
    autoplay
    muted
    loop
    poster="images/thumbnail.jpg">

    <source src="videos/demo.mp4" type="video/mp4">
</video>
```

> **Note:** Most browsers allow autoplay only when the video is muted.

---

# HTML Audio (`<audio>`)

The `<audio>` element is used to play audio files.

## Syntax

```html
<audio controls>
    <source src="song.mp3" type="audio/mpeg">
</audio>
```

## Example

```html
<audio controls>
    <source src="audio/song.mp3" type="audio/mpeg">

    Your browser does not support the audio element.
</audio>
```

## Common Attributes

| Attribute | Description |
|-----------|-------------|
| `controls` | Shows audio controls |
| `autoplay` | Plays audio automatically |
| `muted` | Starts audio muted |
| `loop` | Repeats the audio |

---

# HTML YouTube Videos

YouTube videos are embedded using an `<iframe>`.

## Step 1

Open a YouTube video.

Click **Share → Embed**.

Copy the generated `<iframe>` code.

---

## Example

```html
<iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/dQw4w9WgXcQ"
    title="YouTube Video"
    frameborder="0"
    allowfullscreen>
</iframe>
```

### Common Attributes

| Attribute | Description |
|-----------|-------------|
| `src` | YouTube embed URL |
| `width` | Width of the video |
| `height` | Height of the video |
| `allowfullscreen` | Allows fullscreen mode |

---

# HTML `<iframe>`

The `<iframe>` element embeds another webpage inside your webpage.

## Syntax

```html
<iframe src="page.html"></iframe>
```

## Example

```html
<iframe
    src="https://example.com"
    width="600"
    height="400">
</iframe>
```

---

# HTML Plug-ins

In older versions of HTML, plug-ins were used to display PDFs, Flash content, videos, and other multimedia.

Today, plug-ins like **Adobe Flash** are obsolete, and modern HTML elements (`<video>`, `<audio>`, `<iframe>`) are used instead.

---

## `<object>` Element

The `<object>` element embeds external resources such as PDFs.

### Example

```html
<object
    data="files/html-notes.pdf"
    width="600"
    height="500">
</object>
```

---

## `<embed>` Element

The `<embed>` element embeds external content.

### Example

```html
<embed
    src="files/html-notes.pdf"
    width="600"
    height="500">
```

> **Note:** `<embed>` is still supported, but `<iframe>` is usually preferred for embedding webpages and external content.

---

# Supported Media Formats

## Image Formats

- JPG / JPEG
- PNG
- GIF
- SVG
- WebP

---

## Video Formats

- MP4 ✅ (Most Recommended)
- WebM
- OGG

---

## Audio Formats

- MP3 ✅ (Most Recommended)
- WAV
- OGG

---

# Best Practices

- Always provide the `alt` attribute for images.
- Use MP4 for videos and MP3 for audio for better browser compatibility.
- Compress media files to improve page loading speed.
- Include fallback text inside `<video>` and `<audio>` elements.
- Use `<iframe>` to embed YouTube videos instead of downloading them.
- Avoid outdated plug-ins like Adobe Flash.

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>HTML Media</title>
</head>

<body>

    <h1>HTML Media Examples</h1>

    <!-- Image -->
    <img
        src="images/html-logo.png"
        alt="HTML Logo"
        width="150">

    <hr>

    <!-- Video -->
    <video width="400" controls>
        <source src="videos/demo.mp4" type="video/mp4">

        Your browser does not support the video tag.
    </video>

    <hr>

    <!-- Audio -->
    <audio controls>
        <source src="audio/song.mp3" type="audio/mpeg">

        Your browser does not support the audio element.
    </audio>

    <hr>

    <!-- YouTube Video -->
    <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/dQw4w9WgXcQ"
        title="YouTube Video"
        frameborder="0"
        allowfullscreen>
    </iframe>

</body>

</html>
```

---

# Summary

| Element | Purpose |
|----------|---------|
| `<img>` | Displays an image |
| `<video>` | Embeds a video |
| `<audio>` | Plays audio |
| `<source>` | Specifies media files for audio or video |
| `<iframe>` | Embeds another webpage or YouTube video |
| `<object>` | Embeds external resources such as PDFs |
| `<embed>` | Embeds external content |
| `controls` | Displays media controls |
| `autoplay` | Plays media automatically |
| `muted` | Starts media without sound |
| `loop` | Repeats the media |
| `poster` | Displays a thumbnail before a video starts |