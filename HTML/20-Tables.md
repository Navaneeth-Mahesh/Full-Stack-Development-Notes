# HTML Tables

HTML tables are used to display **tabular data** (data arranged in rows and columns).

Tables are useful when information naturally fits into a grid, such as:

* Student marks
* Employee records
* Product lists
* Timetables
* Price lists
* Monthly reports

> **Important:** Tables should be used **only for displaying data**, **not** for designing or laying out webpages. Modern webpage layouts are created using **CSS Flexbox** and **CSS Grid**.

---

# Basic Table Structure

An HTML table is created using the `<table>` element.

A table is made up of:

* **Rows** (`<tr>`)
* **Header cells** (`<th>`)
* **Data cells** (`<td>`)

## Structure Diagram

```text
<table>
│
├── <tr> (Row 1)
│     ├── <th> Header
│     └── <th> Header
│
├── <tr> (Row 2)
│     ├── <td> Data
│     └── <td> Data
│
└── <tr> (Row 3)
      ├── <td> Data
      └── <td> Data
```

---

# Table Elements

| Element   | Purpose                     |
| --------- | --------------------------- |
| `<table>` | Creates the table           |
| `<tr>`    | Creates a table row         |
| `<th>`    | Creates a table header cell |
| `<td>`    | Creates a table data cell   |

---

# Basic Example

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

**Output**

| Name      | Age |
| --------- | --- |
| Navaneeth | 19  |
| Rahul     | 20  |

---

# Understanding Each Element

## `<table>`

Creates the entire table.

```html
<table>
    ...
</table>
```

---

## `<tr>` (Table Row)

Each `<tr>` creates one horizontal row.

```html
<tr>
    ...
</tr>
```

Example:

```html
<tr>
    <td>Apple</td>
    <td>₹120</td>
</tr>
```

---

## `<th>` (Table Header)

`<th>` defines a header cell.

Browsers usually display it:

* Bold
* Center-aligned

Example:

```html
<tr>
    <th>Name</th>
    <th>Course</th>
</tr>
```

---

## `<td>` (Table Data)

`<td>` contains the actual data.

Example:

```html
<tr>
    <td>Navaneeth</td>
    <td>HTML</td>
</tr>
```

---

# Adding Borders

Tables look clearer with borders.

Use **CSS**, not the obsolete HTML `border` attribute.

## Example

```html
<table style="border-collapse: collapse;">

    <tr>
        <th style="border:1px solid black;">
            Name
        </th>

        <th style="border:1px solid black;">
            Age
        </th>
    </tr>

    <tr>
        <td style="border:1px solid black;">
            Navaneeth
        </td>

        <td style="border:1px solid black;">
            19
        </td>
    </tr>

</table>
```

---

# `border-collapse`

The `border-collapse` property controls how borders are displayed.

## Without `border-collapse`

```css
table{
    border-spacing:2px;
}
```

Every cell has its own border, creating double lines.

```
+---++---+
| A || B |
+---++---+
```

---

## With `border-collapse: collapse`

```css
table{
    border-collapse: collapse;
}
```

Adjacent borders merge into one.

```
+-------+
| A | B |
+-------+
```

This is the most commonly used style.

---

# Cell Padding

Padding adds space **inside** each table cell.

```css
th,
td{
    padding:10px;
}
```

Without padding:

```
|HTML|
```

With padding:

```
|  HTML  |
```

Padding improves readability.

---

# Border Spacing

`border-spacing` adds space **between** table cells.

```css
table{
    border-spacing:10px;
}
```

> It only works when `border-collapse` is **not** set to `collapse`.

---

# Table Caption

The `<caption>` element adds a title to the table.

It should be the **first child** inside the `<table>` element.

## Example

```html
<table>

    <caption>
        Student Report
    </caption>

    <tr>
        <th>Name</th>
        <th>Marks</th>
    </tr>

    <tr>
        <td>Navaneeth</td>
        <td>95</td>
    </tr>

</table>
```

---

# Column Span (`colspan`)

The `colspan` attribute allows one cell to span **multiple columns**.

## Syntax

```html
<td colspan="2">
```

---

## Example

```html
<table>

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

**Visual Representation**

```
+----------------------+
| Student Information  |
+-----------+----------+
| Name      | Navaneeth|
+-----------+----------+
```

---

# Row Span (`rowspan`)

The `rowspan` attribute allows one cell to span **multiple rows**.

## Syntax

```html
<td rowspan="2">
```

---

## Example

```html
<table>

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

**Visual Representation**

```
+---------+------------+
| Name    | Navaneeth  |
|         +------------+
|         | Rahul      |
+---------+------------+
```

---

# Table Sections

Large tables can be divided into three semantic sections.

```
<table>
│
├── <thead>
├── <tbody>
└── <tfoot>
```

---

## `<thead>`

Contains header rows.

```html
<thead>

<tr>
    <th>Name</th>
    <th>Marks</th>
</tr>

</thead>
```

---

## `<tbody>`

Contains the main table data.

```html
<tbody>

<tr>
    <td>Navaneeth</td>
    <td>95</td>
</tr>

</tbody>
```

---

## `<tfoot>`

Contains summary information like totals or averages.

```html
<tfoot>

<tr>
    <td>Total</td>
    <td>95</td>
</tr>

</tfoot>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>HTML Tables</title>

    <style>

        table{
            width:60%;
            border-collapse:collapse;
        }

        th,
        td{
            border:1px solid black;
            padding:10px;
            text-align:left;
        }

        caption{
            font-size:20px;
            font-weight:bold;
            margin-bottom:10px;
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

# Accessibility in Tables

For better accessibility, use the `scope` attribute with `<th>`.

```html
<th scope="col">Name</th>

<th scope="col">Age</th>
```

For row headers:

```html
<th scope="row">Student 1</th>
```

This helps screen readers understand the relationship between headers and data.

---

# Common Beginner Mistakes

### ❌ Using tables for webpage layout

```html
<table>
    <tr>
        <td>Sidebar</td>
        <td>Main Content</td>
    </tr>
</table>
```

✔ Use **CSS Flexbox** or **CSS Grid** for layouts.

---

### ❌ Using the obsolete `border` attribute

```html
<table border="1">
```

✔ Use CSS instead.

```css
table{
    border-collapse:collapse;
}

th,
td{
    border:1px solid black;
}
```

---

### ❌ Forgetting `<th>` for headings

```html
<tr>
    <td>Name</td>
    <td>Age</td>
</tr>
```

✔ Better:

```html
<tr>
    <th>Name</th>
    <th>Age</th>
</tr>
```

---

### ❌ Overusing `rowspan` and `colspan`

Using too many merged cells can make tables difficult to read and maintain.

---

# Best Practices

* Use tables only for **tabular data**.
* Use `<th>` for headings and `<td>` for data.
* Add a `<caption>` to describe the table.
* Organize large tables using `<thead>`, `<tbody>`, and `<tfoot>`.
* Use CSS instead of obsolete HTML attributes.
* Use `border-collapse: collapse` for cleaner borders.
* Add padding to improve readability.
* Use `scope` attributes on header cells for better accessibility.
* Use `rowspan` and `colspan` only when necessary.

---

# Summary

| Element / Attribute | Purpose                                  |
| ------------------- | ---------------------------------------- |
| `<table>`           | Creates a table                          |
| `<tr>`              | Creates a table row                      |
| `<th>`              | Creates a header cell                    |
| `<td>`              | Creates a data cell                      |
| `<caption>`         | Adds a title to the table                |
| `<thead>`           | Groups header rows                       |
| `<tbody>`           | Groups main table data                   |
| `<tfoot>`           | Groups footer or summary rows            |
| `colspan`           | Spans a cell across multiple columns     |
| `rowspan`           | Spans a cell across multiple rows        |
| `border-collapse`   | Merges adjacent borders                  |
| `padding`           | Adds space inside cells                  |
| `border-spacing`    | Adds space between cells                 |
| `scope`             | Improves accessibility for table headers |

---

# Key Points

* HTML tables organize **tabular data** into rows and columns.
* `<table>` is the container, `<tr>` creates rows, `<th>` creates header cells, and `<td>` creates data cells.
* Use **CSS** to style tables instead of obsolete HTML attributes like `border`.
* Use `<caption>` to give your table a meaningful title.
* Divide large tables into `<thead>`, `<tbody>`, and `<tfoot>` for better structure.
* `colspan` merges columns, while `rowspan` merges rows.
* Add `scope` attributes to header cells to improve accessibility.
* Avoid using tables for webpage layouts; use **CSS Flexbox** or **CSS Grid** instead.
