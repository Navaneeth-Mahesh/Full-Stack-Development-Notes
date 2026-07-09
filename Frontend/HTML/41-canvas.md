# HTML Canvas

The `<canvas>` element is used to draw graphics directly on a webpage using **JavaScript**.

Unlike an image, a canvas is blank by default. JavaScript is required to draw shapes, text, lines, animations, and games on it.

> **Note:** The `<canvas>` element only provides a drawing area. All drawing is done using JavaScript.

---

# Basic Syntax

```html
<canvas id="myCanvas" width="500" height="300"></canvas>
```

### Example

```html
<canvas
    id="myCanvas"
    width="400"
    height="200">
</canvas>
```

---

# Canvas Attributes

| Attribute | Description |
|-----------|-------------|
| `id` | Unique identifier used to access the canvas in JavaScript |
| `width` | Width of the canvas (in pixels) |
| `height` | Height of the canvas (in pixels) |

---

# Adding a Border

A canvas is invisible by default. Adding a border helps you see its boundaries.

```html
<canvas
    id="myCanvas"
    width="400"
    height="200"
    style="border:1px solid black;">
</canvas>
```

---

# Accessing the Canvas

Use JavaScript to access the canvas element.

```html
<canvas
    id="myCanvas"
    width="400"
    height="200"
    style="border:1px solid black;">
</canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
</script>
```

### Explanation

- `getElementById()` selects the canvas.
- `getContext("2d")` creates a 2D drawing context.
- `ctx` is used to draw on the canvas.

---

# Draw a Line

```html
<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

ctx.moveTo(20, 20);
ctx.lineTo(200, 100);
ctx.stroke();
</script>
```

---

# Draw a Rectangle

### Filled Rectangle

```javascript
ctx.fillStyle = "blue";
ctx.fillRect(20, 20, 150, 80);
```

### Outlined Rectangle

```javascript
ctx.strokeStyle = "red";
ctx.strokeRect(20, 120, 150, 80);
```

---

# Draw a Circle

```javascript
ctx.beginPath();

ctx.arc(150, 100, 50, 0, 2 * Math.PI);

ctx.stroke();
```

### Parameters

```text
arc(x, y, radius, startAngle, endAngle)
```

---

# Draw Text

### Filled Text

```javascript
ctx.font = "30px Arial";

ctx.fillText("Hello Canvas", 20, 60);
```

### Outlined Text

```javascript
ctx.font = "30px Arial";

ctx.strokeText("Hello Canvas", 20, 120);
```

---

# Draw an Image

```html
<img
    id="logo"
    src="images/logo.png"
    style="display:none;">

<canvas
    id="myCanvas"
    width="400"
    height="300">
</canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

const image = document.getElementById("logo");

image.onload = function () {
    ctx.drawImage(image, 20, 20);
};
</script>
```

---

# Common Canvas Methods

| Method | Purpose |
|---------|---------|
| `getContext("2d")` | Creates a 2D drawing context |
| `moveTo()` | Moves the drawing cursor |
| `lineTo()` | Draws a line |
| `stroke()` | Draws the outline |
| `beginPath()` | Starts a new drawing path |
| `arc()` | Draws circles and arcs |
| `fillRect()` | Draws a filled rectangle |
| `strokeRect()` | Draws a rectangle outline |
| `clearRect()` | Clears a portion of the canvas |
| `fillText()` | Draws filled text |
| `strokeText()` | Draws outlined text |
| `drawImage()` | Draws an image |

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>Canvas Example</title>
</head>

<body>

<canvas
    id="myCanvas"
    width="500"
    height="300"
    style="border:1px solid black;">
</canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Filled Rectangle
ctx.fillStyle = "skyblue";
ctx.fillRect(20, 20, 120, 70);

// Line
ctx.moveTo(180, 20);
ctx.lineTo(320, 100);
ctx.stroke();

// Circle
ctx.beginPath();
ctx.arc(400, 80, 40, 0, 2 * Math.PI);
ctx.stroke();

// Text
ctx.font = "24px Arial";
ctx.fillStyle = "black";
ctx.fillText("Hello Canvas!", 20, 170);

</script>

</body>
</html>
```

---

# Canvas vs SVG

| Canvas | SVG |
|---------|-----|
| Pixel-based | Vector-based |
| Best for games and animations | Best for icons, logos, and diagrams |
| Faster for drawing many objects | Better for scalable graphics |
| Graphics cannot be individually edited after drawing | Each shape remains a separate element |

---

# Common Uses of Canvas

- Drawing shapes
- Charts and graphs
- Image editing
- Animations
- 2D games
- Digital signatures
- Interactive drawings
- Data visualization

---

# Summary

- `<canvas>` provides a drawable area for graphics.
- JavaScript is required to draw on a canvas.
- Use `getContext("2d")` to create a 2D drawing context.
- Canvas can draw lines, rectangles, circles, text, and images.
- It is commonly used for games, animations, charts, and interactive graphics.