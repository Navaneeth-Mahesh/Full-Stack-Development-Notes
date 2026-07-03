# HTML Computer Code Elements

HTML provides several elements to display programming code, keyboard input, computer output, variables, and preformatted text. These elements improve readability and give semantic meaning to technical content.

---

# `<code>` Element

The `<code>` element is used to display programming code.

By default, browsers display the text in a **monospace font**.

## Syntax

```html
<code>Your code here</code>
```

## Example

```html
<p>
    Use the
    <code>print()</code>
    function to display output in Python.
</p>
```

**Output:**

Use the `print()` function to display output in Python.

---

# `<kbd>` Element

The `<kbd>` element represents keyboard input.

It is commonly used in documentation to show which keys the user should press.

## Syntax

```html
<kbd>Ctrl</kbd>
```

## Example

```html
<p>
    Press
    <kbd>Ctrl</kbd> +
    <kbd>C</kbd>
    to copy text.
</p>
```

**Output:**

Press **Ctrl + C** to copy text.

---

# `<samp>` Element

The `<samp>` element represents output produced by a computer program.

## Syntax

```html
<samp>Output</samp>
```

## Example

```html
<p>
    Program Output:
    <samp>Hello, World!</samp>
</p>
```

---

# `<var>` Element

The `<var>` element represents a variable in mathematics or programming.

Browsers usually display it in italics.

## Syntax

```html
<var>variable</var>
```

## Example

```html
<p>
    The value of
    <var>x</var>
    is 10.
</p>
```

Another example:

```html
<p>
    Area = <var>length</var> × <var>width</var>
</p>
```

---

# `<pre>` Element

The `<pre>` element displays preformatted text.

It preserves:

- Spaces
- Tabs
- Line breaks

Exactly as they are written in the HTML file.

## Syntax

```html
<pre>
Text goes here
</pre>
```

## Example

```html
<pre>
Name   : Navaneeth
Course : HTML
Editor : VS Code
</pre>
```

---

# Combining Code Elements

These elements are often used together.

### Example

```html
<p>
    Save the file as
    <code>index.html</code>.
</p>

<p>
    Press
    <kbd>Ctrl</kbd> +
    <kbd>S</kbd>
    to save the file.
</p>

<p>
    Output:
    <samp>File saved successfully.</samp>
</p>

<p>
    Let
    <var>x</var>
    be the user's age.
</p>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Computer Code Elements</title>
</head>

<body>

    <h1>HTML Computer Code Elements</h1>

    <p>
        HTML code example:
        <code>&lt;h1&gt;Hello World&lt;/h1&gt;</code>
    </p>

    <p>
        Press
        <kbd>Ctrl</kbd> +
        <kbd>C</kbd>
        to copy.
    </p>

    <p>
        Output:
        <samp>Hello, World!</samp>
    </p>

    <p>
        The variable
        <var>age</var>
        stores the user's age.
    </p>

    <pre>
Name   : Navaneeth
Course : HTML
Editor : VS Code
    </pre>

</body>

</html>
```

---

# Summary

| Element | Purpose |
|---------|---------|
| `<code>` | Displays programming code |
| `<kbd>` | Represents keyboard input |
| `<samp>` | Represents computer or program output |
| `<var>` | Represents a variable in programming or mathematics |
| `<pre>` | Displays preformatted text while preserving spaces and line breaks |