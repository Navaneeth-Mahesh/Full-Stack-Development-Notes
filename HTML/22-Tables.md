# HTML Tables

HTML tables are used to organize and display data in **rows** and **columns**.

Examples of table data include:

- Student marks
- Employee records
- Product lists
- Timetables
- Price lists

---

# Basic Table Structure

A table is created using the `<table>` element.

Inside a table:

- `<tr>` defines a **table row**.
- `<th>` defines a **table header**.
- `<td>` defines a **table data (cell)**.

### Example

```html
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>

    <tr>
        <td>Navaneeth</td>
        <td>19</td>
    </tr>

    <tr>
        <td>Rahul</td>
        <td>20</td>
    </tr>
</table>
```

---

# Table Elements

| Element | Purpose |
|----------|---------|
| `<table>` | Creates a table |
| `<tr>` | Creates a table row |
| `<th>` | Creates a table header cell |
| `<td>` | Creates a table data cell |

---

# Adding Borders

You can add borders using CSS.

### Example

```html
<table style="border-collapse: collapse;">

    <tr>
        <th style="border:1px solid black;">Name</th>
        <th style="border:1px solid black;">Age</th>
    </tr>

    <tr>
        <td style="border:1px solid black;">Navaneeth</td>
        <td style="border:1px solid black;">19</td>
    </tr>

</table>
```

> **Note:** The `border` HTML attribute is obsolete. Use CSS instead.

---

# Table Headers

Header cells are created using the `<th>` element.

Browsers display them in **bold** and **center-aligned** by default.

### Example

```html
<table>

    <tr>
        <th>Name</th>
        <th>Course</th>
        <th>Marks</th>
    </tr>

    <tr>
        <td>Navaneeth</td>
        <td>HTML</td>
        <td>95</td>
    </tr>

</table>
```

---

# Table Caption

Use the `<caption>` element to add a title to the table.

### Example

```html
<table>

    <caption>
        Student Details
    </caption>

    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>

    <tr>
        <td>Navaneeth</td>
        <td>19</td>
    </tr>

</table>
```

---

# Cell Padding

Padding creates space between the cell content and its border.

### Example

```html
<table style="border-collapse: collapse;">

    <tr>
        <th style="border:1px solid black; padding:10px;">
            Name
        </th>

        <th style="border:1px solid black; padding:10px;">
            Age
        </th>
    </tr>

</table>
```

---

# Cell Spacing

`border-spacing` creates space **between** table cells.

### Example

```html
<table
    style="
        border-spacing:10px;
        border:1px solid black;
    ">

    ...
</table>
```

> `border-spacing` works only when `border-collapse` is not set to `collapse`.

---

# `colspan` Attribute

The `colspan` attribute allows one cell to span multiple columns.

### Example

```html
<table border="1">

    <tr>
        <th colspan="2">
            Student Information
        </th>
    </tr>

    <tr>
        <td>Name</td>
        <td>Navaneeth</td>
    </tr>

</table>
```

---

# `rowspan` Attribute

The `rowspan` attribute allows one cell to span multiple rows.

### Example

```html
<table border="1">

    <tr>
        <th rowspan="2">
            Name
        </th>

        <td>Navaneeth</td>
    </tr>

    <tr>
        <td>Rahul</td>
    </tr>

</table>
```

---

# Table Sections

Large tables can be divided into three sections:

- `<thead>` → Header
- `<tbody>` → Body
- `<tfoot>` → Footer

### Example

```html
<table>

    <thead>
        <tr>
            <th>Name</th>
            <th>Marks</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>Navaneeth</td>
            <td>95</td>
        </tr>
    </tbody>

    <tfoot>
        <tr>
            <td>Total</td>
            <td>95</td>
        </tr>
    </tfoot>

</table>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Tables</title>

    <style>
        table {
            border-collapse: collapse;
            width: 60%;
        }

        th,
        td {
            border: 1px solid black;
            padding: 10px;
            text-align: left;
        }

        caption {
            font-size: 20px;
            margin-bottom: 10px;
            font-weight: bold;
        }
    </style>
</head>

<body>

    <table>

        <caption>
            Student Report
        </caption>

        <thead>
            <tr>
                <th>Name</th>
                <th>Course</th>
                <th>Marks</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>Navaneeth</td>
                <td>HTML</td>
                <td>95</td>
            </tr>

            <tr>
                <td>Rahul</td>
                <td>CSS</td>
                <td>90</td>
            </tr>
        </tbody>

        <tfoot>
            <tr>
                <td colspan="2">
                    Average Marks
                </td>

                <td>
                    92.5
                </td>
            </tr>
        </tfoot>

    </table>

</body>
</html>
```

---

# Best Practices

- Use `<th>` for headings instead of `<td>`.
- Use `<caption>` to describe the table.
- Use CSS instead of the old `border` attribute.
- Use `<thead>`, `<tbody>`, and `<tfoot>` for better organization.
- Keep tables for displaying tabular data, **not** for webpage layout.
- Use `colspan` and `rowspan` only when necessary.

---

# Summary

| Element/Attribute | Purpose |
|-------------------|---------|
| `<table>` | Creates a table |
| `<tr>` | Creates a table row |
| `<th>` | Creates a header cell |
| `<td>` | Creates a data cell |
| `<caption>` | Adds a title to the table |
| `<thead>` | Groups the table header |
| `<tbody>` | Groups the table body |
| `<tfoot>` | Groups the table footer |
| `colspan` | Spans a cell across multiple columns |
| `rowspan` | Spans a cell across multiple rows |
| `border-collapse` | Merges adjacent borders |
| `padding` | Adds space inside table cells |
| `border-spacing` | Adds space between table cells |