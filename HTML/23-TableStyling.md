# HTML Table Styling

By default, HTML tables have very basic styling. CSS can be used to improve their appearance by adding borders, spacing, colors, alignment, and hover effects.

> **Note:** Table styling is done using **CSS**, not HTML.

---

# Basic Table

```html
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
    </tr>

    <tr>
        <td>Navaneeth</td>
        <td>19</td>
        <td>Hyderabad</td>
    </tr>

    <tr>
        <td>Rahul</td>
        <td>20</td>
        <td>Bengaluru</td>
    </tr>
</table>
```

Without CSS, the table appears plain.

---

# Adding Borders

Use the `border` property to add borders to the table and its cells.

```css
table,
th,
td {
    border: 1px solid black;
}
```

Output:

- Every cell has a border.
- Borders are separated by default.

---

# Border Collapse

The `border-collapse` property merges adjacent borders into a single border.

```css
table {
    border-collapse: collapse;
}
```

Without `border-collapse`:

```
| | Cell |
```

With `border-collapse`:

```
| Cell |
```

---

# Cell Padding

`padding` adds space **inside** each table cell.

```css
th,
td {
    padding: 10px;
}
```

More padding makes the table easier to read.

---

# Cell Spacing

By default, tables have spacing between cell borders.

You can control this using:

```css
table {
    border-spacing: 10px;
}
```

> `border-spacing` only works when `border-collapse` is **not** set to `collapse`.

---

# Text Alignment

### Horizontal Alignment

```css
th,
td {
    text-align: left;
}
```

Other values:

```css
text-align: center;
text-align: right;
```

---

### Vertical Alignment

```css
td {
    vertical-align: middle;
}
```

Other values:

```css
vertical-align: top;
vertical-align: bottom;
```

---

# Table Width

Set the width of the table.

```css
table {
    width: 100%;
}
```

Or use a fixed width.

```css
table {
    width: 600px;
}
```

---

# Row Height

```css
tr {
    height: 50px;
}
```

---

# Header Background Color

```css
th {
    background-color: #4CAF50;
    color: white;
}
```

---

# Alternate Row Colors (Zebra Stripes)

```css
tr:nth-child(even) {
    background-color: #f2f2f2;
}
```

This improves readability.

---

# Hover Effect

Highlight a row when the mouse moves over it.

```css
tr:hover {
    background-color: #ddd;
}
```

---

# Table Caption

A caption provides a title for the table.

### HTML

```html
<table>
    <caption>Student Details</caption>

    ...
</table>
```

### CSS

```css
caption {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}
```

---

# Complete Example

## HTML

```html
<table>

    <caption>Student Details</caption>

    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
    </tr>

    <tr>
        <td>Navaneeth</td>
        <td>19</td>
        <td>Hyderabad</td>
    </tr>

    <tr>
        <td>Rahul</td>
        <td>20</td>
        <td>Bengaluru</td>
    </tr>

    <tr>
        <td>Anjali</td>
        <td>18</td>
        <td>Chennai</td>
    </tr>

</table>
```

## CSS

```css
table {
    width: 100%;
    border-collapse: collapse;
}

caption {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}

th,
td {
    border: 1px solid black;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #4CAF50;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #ddd;
}
```

---

# Summary

| Property | Purpose |
|----------|---------|
| `border` | Adds borders to the table and cells |
| `border-collapse` | Merges adjacent borders into one |
| `border-spacing` | Adds space between table cells |
| `padding` | Adds space inside cells |
| `text-align` | Aligns text horizontally |
| `vertical-align` | Aligns text vertically |
| `width` | Sets the table width |
| `height` | Sets the row height |
| `background-color` | Changes the background color |
| `color` | Changes the text color |
| `:hover` | Adds a hover effect to rows |
| `nth-child()` | Styles alternate rows |
| `caption` | Adds a title to the table |