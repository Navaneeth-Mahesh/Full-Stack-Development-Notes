# SVG in HTML

SVG stands for **Scalable Vector Graphics**. It is an XML-based image format used to create graphics such as icons, logos, charts, shapes, and illustrations directly in HTML.

Unlike normal images (`.jpg`, `.png`), SVG graphics **do not lose quality when resized**.

---

# Why Use SVG?

Advantages of SVG:

- Scales without losing quality
- Small file size for simple graphics
- Can be styled using CSS
- Can be animated using CSS or JavaScript
- Editable with a text editor
- Perfect for logos, icons, and illustrations

---

# SVG vs PNG vs JPG

| Feature | SVG | PNG | JPG |
|----------|-----|-----|-----|
| Scalable | ✅ Yes | ❌ No | ❌ No |
| Best For | Icons, Logos | Graphics | Photos |
| Editable | ✅ Yes | ❌ No | ❌ No |
| Transparent Background | ✅ Yes | ✅ Yes | ❌ No |
| File Size | Usually Small | Medium | Small |

---

# SVG Syntax

SVG is created using the `<svg>` element.

```html
<svg width="200" height="200">

</svg>
```

Example:

```html
<svg width="200" height="200">
    <circle
        cx="100"
        cy="100"
        r="80"
        fill="blue">
    </circle>
</svg>
```

---

# Important SVG Attributes

| Attribute | Description |
|-----------|-------------|
| `width` | Width of the SVG |
| `height` | Height of the SVG |
| `fill` | Fill color |
| `stroke` | Border color |
| `stroke-width` | Border thickness |
| `cx` | X-coordinate of a circle's center |
| `cy` | Y-coordinate of a circle's center |
| `r` | Radius of a circle |
| `x` | X position |
| `y` | Y position |

---

# Rectangle

The `<rect>` element draws a rectangle.

```html
<svg width="300" height="200">
    <rect
        x="20"
        y="20"
        width="150"
        height="100"
        fill="skyblue"
        stroke="black"
        stroke-width="3">
    </rect>
</svg>
```

---

# Circle

The `<circle>` element draws a circle.

```html
<svg width="200" height="200">
    <circle
        cx="100"
        cy="100"
        r="60"
        fill="red">
    </circle>
</svg>
```

---

# Ellipse

The `<ellipse>` element draws an ellipse.

```html
<svg width="300" height="200">
    <ellipse
        cx="150"
        cy="100"
        rx="100"
        ry="50"
        fill="orange">
    </ellipse>
</svg>
```

---

# Line

The `<line>` element draws a straight line.

```html
<svg width="300" height="100">
    <line
        x1="20"
        y1="50"
        x2="280"
        y2="50"
        stroke="blue"
        stroke-width="5">
    </line>
</svg>
```

---

# Polygon

The `<polygon>` element draws a closed shape using multiple points.

```html
<svg width="250" height="250">
    <polygon
        points="125,20 230,220 20,220"
        fill="green">
    </polygon>
</svg>
```

---

# Polyline

The `<polyline>` element draws connected lines without closing the shape.

```html
<svg width="300" height="150">
    <polyline
        points="20,100 70,20 120,100 170,20 220,100"
        fill="none"
        stroke="purple"
        stroke-width="4">
    </polyline>
</svg>
```

---

# Text

Text can also be displayed inside SVG.

```html
<svg width="300" height="100">
    <text
        x="40"
        y="60"
        font-size="30"
        fill="blue">
        Hello SVG
    </text>
</svg>
```

---

# SVG as an Image

SVG files can be used with the `<img>` element.

```html
<img
    src="images/logo.svg"
    alt="Company Logo"
    width="200">
```

---

# SVG with CSS

SVG elements can be styled using CSS.

```html
<svg width="200" height="200">
    <circle
        cx="100"
        cy="100"
        r="70"
        style="fill:tomato; stroke:black; stroke-width:4;">
    </circle>
</svg>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>SVG Example</title>
</head>
<body>

    <h1>Basic SVG Shapes</h1>

    <svg width="500" height="300">

        <rect
            x="20"
            y="20"
            width="100"
            height="80"
            fill="skyblue" />

        <circle
            cx="220"
            cy="60"
            r="40"
            fill="red" />

        <ellipse
            cx="370"
            cy="60"
            rx="60"
            ry="40"
            fill="orange" />

        <line
            x1="20"
            y1="170"
            x2="200"
            y2="170"
            stroke="green"
            stroke-width="5" />

        <polygon
            points="300,130 360,220 240,220"
            fill="purple" />

        <text
            x="20"
            y="280"
            font-size="28"
            fill="blue">
            Hello SVG
        </text>

    </svg>

</body>
</html>
```

---

# When Should You Use SVG?

Use SVG for:

- Website logos
- Icons
- Buttons
- Graphs and charts
- Illustrations
- Simple animations
- Diagrams

Avoid SVG for:

- Photographs
- Complex, high-resolution images
- Large image galleries

---

# Summary

| Element | Purpose |
|---------|---------|
| `<svg>` | Creates an SVG drawing area |
| `<rect>` | Draws a rectangle |
| `<circle>` | Draws a circle |
| `<ellipse>` | Draws an ellipse |
| `<line>` | Draws a straight line |
| `<polygon>` | Draws a closed shape |
| `<polyline>` | Draws connected lines |
| `<text>` | Displays text inside SVG |
| `fill` | Sets the fill color |
| `stroke` | Sets the border color |
| `stroke-width` | Sets the border thickness |
| `width` / `height` | Sets the SVG size |