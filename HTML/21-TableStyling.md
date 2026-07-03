# HTML Table Styling (Using CSS)

By default, HTML tables have a simple appearance. **CSS (Cascading Style Sheets)** is used to improve their look by adding borders, spacing, colors, alignment, hover effects, and more.

> **Important:** HTML creates the table structure, while **CSS controls its appearance**.

---

# How HTML and CSS Work Together

```text
HTML
│
├── Creates the table structure
│
└── CSS
     ├── Adds borders
     ├── Changes colors
     ├── Controls spacing
     ├── Aligns text
     └── Adds hover effects
```

---

# Basic HTML Table

Before applying any styles, create a table using HTML.

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

Without CSS, most browsers display a plain table with little or no styling.

---

# 1. Adding Borders

Use the `border` property to display borders around the table and its cells.

## Syntax

```css
table,
th,
td {
    border: 1px solid black;
}
```

### Explanation

* `1px` → Border thickness
* `solid` → Border style
* `black` → Border color

**Result**

```
+----------+-----+-----------+
| Name     | Age | City      |
+----------+-----+-----------+
| Navaneeth| 19  | Hyderabad |
+----------+-----+-----------+
```

---

# 2. Border Collapse

By default, adjacent table borders are separated.

The `border-collapse` property merges them into a single border.

## Syntax

```css
table {
    border-collapse: collapse;
}
```

### Without `border-collapse`

```text
+----++----+
| A  || B  |
+----++----+
```

### With `border-collapse`

```text
+---------+
| A | B   |
+---------+
```

> `border-collapse: collapse;` is commonly used in modern websites because it creates cleaner tables.

---

# 3. Cell Padding

Padding adds space **inside** each table cell.

## Syntax

```css
th,
td {
    padding: 10px;
}
```

### Without Padding

```
|Name|
```

### With Padding

```
|  Name  |
```

Padding makes tables much easier to read.

---

# 4. Border Spacing

`border-spacing` adds space **between table cells**.

## Syntax

```css
table {
    border-spacing: 10px;
}
```

### Important

`border-spacing` works **only when**:

```css
border-collapse: separate;
```

or when `border-collapse` is not specified.

If you use:

```css
border-collapse: collapse;
```

then `border-spacing` has **no effect**.

---

# 5. Table Width

The `width` property controls the width of the table.

## Full Width

```css
table {
    width: 100%;
}
```

The table fills its parent container.

---

## Fixed Width

```css
table {
    width: 600px;
}
```

The table always remains 600 pixels wide.

---

# 6. Row Height

The `height` property changes the height of table rows.

```css
tr {
    height: 50px;
}
```

Larger row heights make tables easier to read.

---

# 7. Text Alignment

## Horizontal Alignment

Use `text-align` to align text horizontally.

### Left (Default for most table cells)

```css
th,
td {
    text-align: left;
}
```

### Center

```css
text-align: center;
```

### Right

```css
text-align: right;
```

---

## Vertical Alignment

Use `vertical-align` to align text vertically.

```css
td {
    vertical-align: middle;
}
```

Possible values:

```css
vertical-align: top;
vertical-align: middle;
vertical-align: bottom;
```

---

# 8. Header Styling

Headers are usually highlighted to distinguish them from data cells.

```css
th {
    background-color: #4CAF50;
    color: white;
}
```

### Explanation

* `background-color` changes the background.
* `color` changes the text color.

---

# 9. Zebra Stripes

Alternating row colors improve readability.

```css
tr:nth-child(even) {
    background-color: #f2f2f2;
}
```

### How It Works

```
Row 1 → White
Row 2 → Gray
Row 3 → White
Row 4 → Gray
```

`nth-child()` is a CSS pseudo-class that selects elements based on their position.

---

# 10. Hover Effect

Highlight a row when the mouse pointer moves over it.

```css
tr:hover {
    background-color: #ddd;
}
```

This makes large tables easier to navigate.

---

# 11. Table Caption

A `<caption>` provides a title for the table.

## HTML

```html
<table>

    <caption>Student Details</caption>

    ...
</table>
```

The caption appears above the table by default.

---

## Styling the Caption

```css
caption {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}
```

---

# 12. Complete Example

## HTML

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Table</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

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

</body>

</html>
```

---

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

# Common Beginner Mistakes

### ❌ Forgetting `border-collapse`

```css
table {
    border: 1px solid black;
}
```

This creates double borders.

✔ Better

```css
table {
    border-collapse: collapse;
}
```

---

### ❌ Using `border-spacing` with `border-collapse`

```css
table {
    border-collapse: collapse;
    border-spacing: 10px;
}
```

`border-spacing` will not work.

---

### ❌ No Padding

```css
td {
    border: 1px solid black;
}
```

The content looks cramped.

✔ Better

```css
td {
    border: 1px solid black;
    padding: 10px;
}
```

---

### ❌ Centering Everything Without Need

```css
th,
td {
    text-align: center;
}
```

Choose alignment based on the type of data.

For example:

* Names → Left
* Numbers → Center or Right
* Prices → Right

---

# Commonly Used Table CSS Properties

| Property           | Purpose                             |
| ------------------ | ----------------------------------- |
| `border`           | Adds borders to the table and cells |
| `border-collapse`  | Merges adjacent borders into one    |
| `border-spacing`   | Adds space between table cells      |
| `padding`          | Adds space inside cells             |
| `width`            | Sets the width of the table         |
| `height`           | Sets the row height                 |
| `text-align`       | Aligns text horizontally            |
| `vertical-align`   | Aligns text vertically              |
| `background-color` | Changes the background color        |
| `color`            | Changes the text color              |
| `font-size`        | Changes the text size               |
| `font-weight`      | Makes text bold or normal           |
| `:hover`           | Adds a hover effect                 |
| `nth-child()`      | Styles rows based on their position |
| `caption`          | Styles the table title              |

---

# Key Points

* HTML creates the **structure** of a table, while CSS controls its **appearance**.
* Use `border-collapse: collapse;` to create clean, single borders.
* Use `padding` to add space inside cells and improve readability.
* Use `width` to control the table's size.
* Use `text-align` and `vertical-align` to position content inside cells.
* Apply `background-color` to style table headers.
* Use `tr:nth-child(even)` to create zebra-striped rows.
* Use `tr:hover` to highlight rows when the mouse pointer moves over them.
* Use `<caption>` to provide a meaningful title for the table.
* A well-styled table is easier to read, looks more professional, and improves the overall user experience.
