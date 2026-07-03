# HTML Tables

HTML tables are used to display **structured data** in **rows** and **columns**. They are useful for presenting information that naturally fits into a grid, such as:

* Student marks
* Timetables
* Product lists
* Employee records
* Financial reports

> **Important:** Use tables only for displaying **tabular data**. Do **not** use tables to design or position webpage layouts. Modern layouts should be created using **CSS Flexbox** or **CSS Grid**.

---

# Basic Table Structure

A table is created using the `<table>` element and contains rows and cells.

## Table Elements

| Element   | Purpose                     |
| --------- | --------------------------- |
| `<table>` | Creates the table           |
| `<tr>`    | Creates a table row         |
| `<th>`    | Creates a table header cell |
| `<td>`    | Creates a table data cell   |

### Visual Structure

```text
<table>
│
├── <tr> (Header Row)
│      ├── <th>
│      ├── <th>
│      └── <th>
│
├── <tr> (Data Row)
│      ├── <td>
│      ├── <td>
│      └── <td>
│
└── <tr> (Another Data Row)
       ├── <td>
       ├── <td>
       └── <td>
```

---

# Basic Example

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

### Output

| Name      | Age | City      |
| --------- | --- | --------- |
| Navaneeth | 18  | Hyderabad |
| Rahul     | 20  | Bengaluru |

---

# Understanding Each Element

## `<table>`

The `<table>` element is the **container** for the entire table.

```html
<table>
    ...
</table>
```

Everything related to the table must be placed inside this element.

---

## `<tr>` — Table Row

The `<tr>` element creates a **horizontal row**.

```html
<tr>
    ...
</tr>
```

A table can have as many rows as needed.

---

## `<th>` — Table Header Cell

The `<th>` element defines a **header cell**.

```html
<th>Name</th>
```

By default:

* Text is **bold**
* Text is **center-aligned**
* Screen readers recognize it as a **header**, improving accessibility.

Example:

| Name   | Age    |
| ------ | ------ |
| Header | Header |

---

## `<td>` — Table Data Cell

The `<td>` element defines a **regular data cell**.

```html
<td>Navaneeth</td>
```

Example:

| Name      |
| --------- |
| Navaneeth |

---

# Adding Table Borders

Tables have **no visible borders** by default.

Use CSS to add them.

```html
<style>

table,
th,
td {
    border: 1px solid black;
}

</style>
```

### Output

Every cell will have a visible border.

---

# `border-collapse`

Without `border-collapse`, adjacent borders appear as **double borders**.

```html
table {
    border-collapse: collapse;
}
```

### Without `border-collapse`

```text
+----++----+
| A || B |
+----++----+
```

### With `border-collapse`

```text
+---------+
| A | B |
+---------+
```

> `border-collapse: collapse;` is commonly used in modern web development.

---

# Cell Padding

Padding adds space **inside** a table cell.

```html
th,
td {
    padding: 10px;
}
```

### Without Padding

```text
|A|
```

### With Padding

```text
|   A   |
```

---

# Cell Spacing

`border-spacing` adds space **between** cells.

```html
table {
    border-spacing: 8px;
}
```

> **Note:** `border-spacing` only works when `border-collapse: collapse;` is **not** used.

---

# Aligning Cell Content

Use the `text-align` property to align text.

```css
td {
    text-align: left;
}
```

Possible values:

```css
left
center
right
justify
```

Example:

```css
th {
    text-align: center;
}
```

---

# Table Width

You can control the table width using CSS.

```css
table {
    width: 100%;
}
```

Common values:

```css
width: 50%;
width: 80%;
width: 100%;
width: 600px;
```

---

# Table Caption

The `<caption>` element adds a title to the table.

```html
<table>

    <caption>
        Student Details
    </caption>

</table>
```

Output:

```text
Student Details

+----------------+
| Name | Age |
+----------------+
```

Only one `<caption>` should be used per table.

---

# `colspan`

The `colspan` attribute allows a cell to span **multiple columns**.

```html
<table>

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

### Visual Representation

```text
+----------------------+
| Student Details      |
+-----------+----------+
| Name      | Navaneeth|
+-----------+----------+
```

---

# `rowspan`

The `rowspan` attribute allows a cell to span **multiple rows**.

```html
<table>

<tr>
    <td rowspan="2">Class A</td>
    <td>Rahul</td>
</tr>

<tr>
    <td>Priya</td>
</tr>

</table>
```

### Visual Representation

```text
+---------+---------+
| Class A | Rahul   |
|         +---------+
|         | Priya   |
+---------+---------+
```

---

# Table Sections

Large tables should be divided into sections.

| Element   | Purpose        |
| --------- | -------------- |
| `<thead>` | Header section |
| `<tbody>` | Main data      |
| `<tfoot>` | Footer section |

### Structure

```text
<table>
│
├── <thead>
├── <tbody>
└── <tfoot>
```

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

# Accessibility Best Practices

For better accessibility:

* Use `<th>` instead of `<td>` for headers.
* Add a `<caption>` to describe the table.
* Organize large tables with `<thead>`, `<tbody>`, and `<tfoot>`.
* Avoid empty rows and columns.
* Use CSS for styling instead of deprecated HTML attributes like `border="1"`.

---

# Common Mistakes

❌ Using tables to create page layouts.

❌ Using `<td>` instead of `<th>` for column headings.

❌ Forgetting `border-collapse: collapse;`.

❌ Using deprecated HTML attributes (`border`, `cellpadding`, `cellspacing`) instead of CSS.

---

# Best Practices

* Use tables only for tabular data.
* Keep tables simple and readable.
* Use semantic elements like `<caption>`, `<thead>`, `<tbody>`, and `<tfoot>`.
* Style tables using CSS.
* Make tables responsive if they contain many columns.

---

# Summary

| Element / Property | Purpose                            |
| ------------------ | ---------------------------------- |
| `<table>`          | Creates a table                    |
| `<tr>`             | Creates a table row                |
| `<th>`             | Creates a header cell              |
| `<td>`             | Creates a data cell                |
| `<caption>`        | Adds a table title                 |
| `<thead>`          | Groups header rows                 |
| `<tbody>`          | Groups main table data             |
| `<tfoot>`          | Groups footer rows                 |
| `colspan`          | Makes a cell span multiple columns |
| `rowspan`          | Makes a cell span multiple rows    |
| `border-collapse`  | Merges adjacent borders into one   |
| `padding`          | Adds space inside cells            |
| `border-spacing`   | Adds space between cells           |
| `text-align`       | Aligns text inside cells           |
| `width`            | Sets the table width               |

> **Key Takeaway:** HTML tables are designed to display structured data. Combine semantic HTML (`<thead>`, `<tbody>`, `<tfoot>`, `<caption>`) with CSS styling to create clean, accessible, and maintainable tables.
