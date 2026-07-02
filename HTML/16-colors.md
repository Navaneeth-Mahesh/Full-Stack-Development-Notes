# HTML Colors

Colors in HTML are used to style text, backgrounds, borders, and other elements. You can apply colors using **color names, HEX values, RGB, RGBA, HSL, and HSLA**.

---

# 1. Color Names

HTML supports around **140 standard color names**.

### Syntax

```html
<p style="color:red;">This is red text</p>
```

### Example

```html
<h2 style="color:Tomato;">Tomato Color</h2>
<h2 style="color:DodgerBlue;">Dodger Blue</h2>
<h2 style="color:MediumSeaGreen;">Medium Sea Green</h2>
```

---

# 2. Background Colors

You can change the background color of any element.

### Syntax

```html
<h2 style="background-color:yellow;">Hello</h2>
```

### Example

```html
<h1 style="background-color:lightblue;">
    Welcome to HTML Colors
</h1>
```

---

# 3. Border Colors

You can also apply color to borders.

### Syntax

```html
<p style="border:2px solid red;">Border Text</p>
```

### Example

```html
<p style="border:2px solid green;">
    This is a green border
</p>
```

---

# 4. HEX Colors

HEX colors are written using a `#` followed by 6 characters.

### Format

```
#RRGGBB
```

### Example

```html
<h2 style="color:#ff0000;">Red Text</h2>
<h2 style="color:#00ff00;">Green Text</h2>
<h2 style="color:#0000ff;">Blue Text</h2>
```

---

# 5. Short HEX Colors

If values are repeating, you can shorten HEX codes.

### Example

```html
#ff0000 → #f00
#00ff00 → #0f0
#0000ff → #00f
```

```html
<p style="color:#f00;">Short Red HEX</p>
```

---

# 6. RGB Colors

RGB stands for:

- Red
- Green
- Blue

Each value ranges from **0 to 255**.

### Syntax

```html
rgb(red, green, blue)
```

### Example

```html
<p style="color:rgb(255, 0, 0);">Red Text</p>
<p style="color:rgb(0, 255, 0);">Green Text</p>
<p style="color:rgb(0, 0, 255);">Blue Text</p>
```

---

# 7. RGBA Colors (with Transparency)

RGBA adds an **alpha value (opacity)** from 0 to 1.

### Syntax

```html
rgba(red, green, blue, alpha)
```

### Example

```html
<p style="color:rgba(255, 0, 0, 0.5);">
    Semi Transparent Red
</p>
```

---

# 8. HSL Colors

HSL stands for:

- Hue (0–360)
- Saturation (0–100%)
- Lightness (0–100%)

### Syntax

```html
hsl(hue, saturation, lightness)
```

### Example

```html
<p style="color:hsl(0, 100%, 50%);">Red</p>
<p style="color:hsl(120, 100%, 50%);">Green</p>
<p style="color:hsl(240, 100%, 50%);">Blue</p>
```

---

# 9. HSLA Colors (with Transparency)

HSLA adds an **alpha value (opacity)**.

### Syntax

```html
hsla(hue, saturation, lightness, alpha)
```

### Example

```html
<p style="color:hsla(0, 100%, 50%, 0.5);">
    Transparent Red
</p>
```

---

# 10. Color in Different Elements

## Text Color

```html
<p style="color:red;">Red Text</p>
```

---

## Background Color

```html
<div style="background-color:yellow;">
    Yellow Background
</div>
```

---

## Border Color

```html
<div style="border:2px solid blue;">
    Blue Border
</div>
```

---

# 11. Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Colors</title>
</head>
<body>

    <h1 style="color:white; background-color:black;">
        HTML Colors Demo
    </h1>

    <p style="color:red;">Red Text</p>
    <p style="color:rgb(0, 128, 0);">Green RGB Text</p>
    <p style="color:#0000ff;">Blue HEX Text</p>

    <h2 style="background-color:lightgray;">
        Background Example
    </h2>

    <p style="border:2px solid tomato;">
        Border Color Example
    </p>

</body>
</html>
```

---

# Summary

| Type | Example |
|------|--------|
| Color Name | `red`, `blue`, `tomato` |
| HEX | `#ff0000` |
| Short HEX | `#f00` |
| RGB | `rgb(255,0,0)` |
| RGBA | `rgba(255,0,0,0.5)` |
| HSL | `hsl(0,100%,50%)` |
| HSLA | `hsla(0,100%,50%,0.5)` |

---

# Key Points

- Colors can be applied to text, background, and borders.
- HEX is the most commonly used format in real projects.
- RGBA and HSLA allow transparency control.
- Color names are easy but limited.
- Use consistent color formats in your projects.