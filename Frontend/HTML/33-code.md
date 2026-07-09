# HTML Computer Code Elements (Clean Beginner Notes)

HTML provides special elements to display **code, keyboard input, output, variables, and formatted text** in a meaningful way.

These elements are useful for:

* Programming tutorials
* Documentation pages
* Technical blogs
* Developer notes

---

# Why These Elements Matter

Instead of using plain text, these tags:

* Improve readability
* Preserve meaning (semantic HTML)
* Display content in a developer-friendly way
* Use monospace font by default (like code editors)

---

# 1. `<code>` (Programming Code)

Used to display **code snippets**.

```html id="code"
<code>print()</code>
```

### Example

```html id="code-example"
<p>
    Use the <code>print()</code> function in Python.
</p>
```

### Output:

Use the `print()` function in Python.

---

# 2. `<kbd>` (Keyboard Input)

Represents keys pressed on a keyboard.

```html id="kbd"
<kbd>Ctrl</kbd>
```

---

## Example

```html id="kbd-example"
<p>
    Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.
</p>
```

### Output:

Press **Ctrl + C** to copy.

---

# 3. `<samp>` (Program Output)

Represents **output from a program or system**.

```html id="samp"
<samp>Hello</samp>
```

---

## Example

```html id="samp-example"
<p>
    Output: <samp>Hello, World!</samp>
</p>
```

---

# 4. `<var>` (Variables)

Represents variables in programming or math.

Usually displayed in italics.

```html id="var"
<var>x</var>
```

---

## Example

```html id="var-example"
<p>
    Let <var>x</var> be the age of the user.
</p>
```

---

## Mathematical Example

```html id="math-var"
<p>
    Area = <var>length</var> × <var>width</var>
</p>
```

---

# 5. `<pre>` (Preformatted Text)

Preserves:

* Spaces
* Line breaks
* Tabs

Exactly as written in HTML.

---

## Example

```html id="pre"
<pre>
Name   : Navaneeth
Course : HTML
Level  : Beginner
</pre>
```

---

## Why `<pre>` is useful

Normal HTML ignores extra spaces:

```text id="normal-html"
HTML ignores spacing
```

But `<pre>` preserves formatting exactly.

---

# Combining All Code Elements

These tags are often used together in documentation.

---

## Example

```html id="combined"
<p>
    Save file as <code>index.html</code>.
</p>

<p>
    Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save.
</p>

<p>
    Output: <samp>File saved successfully</samp>
</p>

<p>
    Variable <var>x</var> stores a number.
</p>
```

---

# Complete Example Page

```html id="full-example"
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Computer Code Elements</title>
</head>

<body>

    <h1>HTML Computer Code Elements</h1>

    <p>
        Example code: <code>&lt;h1&gt;Hello World&lt;/h1&gt;</code>
    </p>

    <p>
        Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.
    </p>

    <p>
        Output: <samp>Hello, World!</samp>
    </p>

    <p>
        Variable: <var>age</var>
    </p>

    <pre>
Name   : Navaneeth
Course : HTML
Tool   : VS Code
    </pre>

</body>

</html>
```

---

# Summary Table

| Element  | Purpose                      |
| -------- | ---------------------------- |
| `<code>` | Displays programming code    |
| `<kbd>`  | Shows keyboard input         |
| `<samp>` | Shows program output         |
| `<var>`  | Represents variables         |
| `<pre>`  | Preserves formatting exactly |

---

# Key Takeaway

These elements don’t just change appearance—they give **meaning to technical content**, making HTML more readable and professional for developers.

---

If you send the next file, I can start combining everything into a **single structured HTML course (Chapter-wise notes like a textbook)**.
