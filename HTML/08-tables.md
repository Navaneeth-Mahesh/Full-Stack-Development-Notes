# HTML Tables

HTML tables are used to display data in **rows** and **columns**. They are useful for presenting structured information such as timetables, product lists, marks, and reports.

> **Note:** Tables should be used for displaying tabular data, **not** for creating page layouts.

---

# Basic Table Structure

A table is created using the `<table>` element and consists of:

- `<tr>` → Table Row
- `<th>` → Table Header Cell
- `<td>` → Table Data Cell

### Example

```html
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
    </tr>

    <tr>
        <td>Navaneeth</td>
        <td>18</td>
        <td>Hyderabad</td>
    </tr>

    <tr>
        <td>Rahul</td>
        <td>20</td>
        <td>Bengaluru</td>
    </tr>
</table>
```

---

# Table Elements

## `<table>`

Defines the entire table.

```html
<table>
    ...
</table>
```

---

## `<tr>`

Defines a table row.

```html
<tr>
    ...
</tr>
```

---

## `<th>`

Defines a table header cell.

By default:

- Text is **bold**
- Text is **center-aligned**

Example:

```html
<th>Name</th>
```

---

## `<td>`

Defines a standard table data cell.

Example:

```html
<td>Navaneeth</td>
```

---

# Adding Borders

You can add borders using CSS.

### Example

```html
<style>
table, th, td {
    border: 1px solid black;
}
</style>
```

To avoid double borders:

```html
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
```

---

# Cell Padding

Padding adds space **inside** table cells.

```html
<style>
th, td {
    padding: 10px;
}
</style>
```

---

# Cell Spacing

Spacing adds space **between** cells.

```html
<style>
table {
    border-spacing: 8px;
}
</style>
```

> **Note:** `border-spacing` works only when `border-collapse: collapse;` is **not** used.

---

# Table Caption

Use the `<caption>` element to provide a title for the table.

### Example

```html
<table>

    <caption>
        Student Details
    </caption>

    ...
</table>
```

---

# Colspan

The `colspan` attribute allows a cell to span multiple columns.

### Example

```html
<table border="1">

<tr>
    <th colspan="2">
        Student Details
    </th>
</tr>

<tr>
    <td>Name</td>
    <td>Navaneeth</td>
</tr>

</table>
```

---

# Rowspan

The `rowspan` attribute allows a cell to span multiple rows.

### Example

```html
<table border="1">

<tr>
    <td rowspan="2">Class A</td>
    <td>Rahul</td>
</tr>

<tr>
    <td>Priya</td>
</tr>

</table>
```

---

# Table Sections

HTML provides elements to organize different parts of a table.

| Element | Purpose |
|---------|---------|
| `<thead>` | Groups the table header |
| `<tbody>` | Groups the main table data |
| `<tfoot>` | Groups the table footer |

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

        <tr>
            <td>Rahul</td>
            <td>90</td>
        </tr>
    </tbody>

    <tfoot>
        <tr>
            <td>Total Students</td>
            <td>2</td>
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
    width: 60%;
    border-collapse: collapse;
}

table,
th,
td {
    border: 1px solid black;
}

th,
td {
    padding: 10px;
    text-align: left;
}

caption {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}

</style>

</head>

<body>

<table>

    <caption>Student Details</caption>

    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Course</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>Navaneeth</td>
            <td>18</td>
            <td>Computer Science</td>
        </tr>

        <tr>
            <td>Rahul</td>
            <td>20</td>
            <td>Information Technology</td>
        </tr>
    </tbody>

</table>

</body>
</html>
```

---

# Best Practices

- Use tables only for displaying tabular data.
- Use `<th>` for header cells instead of `<td>`.
- Add a `<caption>` when the table needs a title.
- Use `<thead>`, `<tbody>`, and `<tfoot>` for better organization.
- Style tables using CSS instead of HTML attributes like `border`.

---

# Summary

| Element/Attribute | Purpose |
|-------------------|---------|
| `<table>` | Creates a table |
| `<tr>` | Defines a table row |
| `<th>` | Defines a table header cell |
| `<td>` | Defines a table data cell |
| `<caption>` | Adds a title to the table |
| `colspan` | Spans a cell across multiple columns |
| `rowspan` | Spans a cell across multiple rows |
| `<thead>` | Groups table header content |
| `<tbody>` | Groups main table content |
| `<tfoot>` | Groups table footer content |
| `border-collapse` | Merges adjacent borders into one |
| `padding` | Adds space inside table cells |
| `border-spacing` | Adds space between table cells |