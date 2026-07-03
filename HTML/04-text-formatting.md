# HTML Text Formatting

HTML provides different tags to format text. Some tags only change the **appearance** of the text, while others also provide **meaning (semantic information)**.

Semantic tags help:

* Browsers understand your content.
* Search engines understand page structure.
* Screen readers provide a better experience for visually impaired users.

---

# Types of Text Formatting Tags

HTML formatting tags can be divided into two categories:

| Type                    | Purpose                             | Examples                               |
| ----------------------- | ----------------------------------- | -------------------------------------- |
| **Visual Formatting**   | Changes only the appearance of text | `<b>`, `<i>`, `<u>`                    |
| **Semantic Formatting** | Adds meaning along with formatting  | `<strong>`, `<em>`, `<mark>`, `<abbr>` |

> **Best Practice:** Prefer semantic tags whenever they correctly describe the meaning of the content.

---

# 1. Bold Text (`<b>`)

The `<b>` tag displays text in **bold**.

It **does not** indicate that the text is important. It only changes the appearance.

## Syntax

```html
<b>Bold Text</b>
```

## Example

```html
<p>This is <b>bold</b> text.</p>
```

### Output

This is **bold** text.

### When to Use

* Product names
* Keywords
* Labels
* Text that should simply appear bold

---

# 2. Strong Text (`<strong>`)

The `<strong>` tag indicates that the text is **important**.

Browsers usually display it in **bold**, but unlike `<b>`, it also adds semantic meaning.

## Syntax

```html
<strong>Important Text</strong>
```

## Example

```html
<p>Please read the <strong>instructions</strong> carefully.</p>
```

### Output

Please read the **instructions** carefully.

### Use When

* Warnings
* Important instructions
* Critical information

---

## `<b>` vs `<strong>`

| `<b>`               | `<strong>`           |
| ------------------- | -------------------- |
| Makes text bold     | Makes text important |
| No semantic meaning | Has semantic meaning |
| Used for appearance | Used for importance  |

---

# 3. Italic Text (`<i>`)

The `<i>` tag displays text in *italic*.

It only changes appearance.

## Syntax

```html
<i>Italic Text</i>
```

## Example

```html
<p>This is <i>italic</i> text.</p>
```

### Common Uses

* Scientific names
* Foreign words
* Book titles
* Technical terms

---

# 4. Emphasized Text (`<em>`)

The `<em>` tag indicates that text should be emphasized.

Browsers usually display it in italics.

## Syntax

```html
<em>Emphasized Text</em>
```

## Example

```html
<p>This is <em>very important</em>.</p>
```

---

## `<i>` vs `<em>`

| `<i>`             | `<em>`              |
| ----------------- | ------------------- |
| Italic styling    | Adds emphasis       |
| Visual formatting | Semantic formatting |

---

# 5. Marked Text (`<mark>`)

The `<mark>` tag highlights text.

## Syntax

```html
<mark>Highlighted Text</mark>
```

## Example

```html
<p>HTML is <mark>easy to learn</mark>.</p>
```

### Common Uses

* Search results
* Important notes
* Highlighted keywords

---

# 6. Small Text (`<small>`)

Displays text in a smaller font.

## Syntax

```html
<small>Small Text</small>
```

## Example

```html
<p>Price: ₹999 <small>(Including GST)</small></p>
```

### Common Uses

* Copyright information
* Terms and conditions
* Notes

---

# 7. Deleted Text (`<del>`)

Represents deleted or removed text.

Browsers usually display it with a line through it.

## Syntax

```html
<del>Deleted Text</del>
```

## Example

```html
<p>Price: <del>₹999</del> ₹799</p>
```

---

# 8. Inserted Text (`<ins>`)

Represents newly inserted text.

Browsers usually underline it.

## Syntax

```html
<ins>Inserted Text</ins>
```

## Example

```html
<p><ins>New Feature Added</ins></p>
```

---

# 9. Underlined Text (`<u>`)

The `<u>` tag underlines text.

Unlike `<ins>`, it does **not** mean the text was inserted.

## Syntax

```html
<u>Underlined Text</u>
```

## Example

```html
<p><u>Important Word</u></p>
```

> **Note:** Avoid underlining normal text because users often think underlined text is a hyperlink.

---

# 10. Subscript (`<sub>`)

Displays text below the normal line.

## Common Uses

* Chemical formulas
* Mathematical expressions

## Example

```html
<p>H<sub>2</sub>O</p>
```

### Output

H₂O

---

# 11. Superscript (`<sup>`)

Displays text above the normal line.

## Common Uses

* Exponents
* Footnotes

## Example

```html
<p>2<sup>5</sup> = 32</p>
```

### Output

2⁵ = 32

---

# 12. Code (`<code>`)

Displays inline code.

## Syntax

```html
<code>console.log("Hello");</code>
```

## Example

```html
<p>Use <code>console.log()</code> to print output.</p>
```

---

# 13. Preformatted Text (`<pre>`)

Preserves spaces and line breaks exactly as written.

## Example

```html
<pre>
Name : Navaneeth
Age  : 18
City : Guntur
</pre>
```

---

# 14. Keyboard Input (`<kbd>`)

Represents keyboard shortcuts.

## Example

```html
<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.</p>
```

---

# 15. Sample Output (`<samp>`)

Represents output from a computer program.

## Example

```html
<samp>File Saved Successfully</samp>
```

---

# 16. Variable (`<var>`)

Represents a variable in mathematics or programming.

## Example

```html
<p><var>x</var> = 10</p>
```

---

# 17. Abbreviation (`<abbr>`)

Represents an abbreviation or acronym.

## Syntax

```html
<abbr title="HyperText Markup Language">HTML</abbr>
```

Hovering over the abbreviation displays the full form.

---

# 18. Citation (`<cite>`)

Represents the title of a creative work.

## Example

```html
<p><cite>Harry Potter</cite></p>
```

---

# 19. Short Quotation (`<q>`)

Represents a short quotation.

Browsers automatically add quotation marks.

## Example

```html
<p><q>Practice makes perfect.</q></p>
```

---

# 20. Block Quote (`<blockquote>`)

Represents a long quotation from another source.

## Example

```html
<blockquote>
The best way to predict the future is to create it.
</blockquote>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Text Formatting</title>
</head>
<body>

    <p><b>Bold Text</b></p>

    <p><strong>Important Text</strong></p>

    <p><i>Italic Text</i></p>

    <p><em>Emphasized Text</em></p>

    <p><mark>Highlighted Text</mark></p>

    <p><small>Small Text</small></p>

    <p><u>Underlined Text</u></p>

    <p><del>Old Price: ₹999</del></p>

    <p><ins>New Price: ₹799</ins></p>

    <p>Water: H<sub>2</sub>O</p>

    <p>2<sup>5</sup> = 32</p>

    <p>Use <code>console.log()</code> to print output.</p>

    <pre>
HTML
CSS
JavaScript
    </pre>

    <p>Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save.</p>

    <p><abbr title="HyperText Markup Language">HTML</abbr></p>

    <blockquote>
        Learning HTML is the first step toward becoming a web developer.
    </blockquote>

</body>
</html>
```

---

# Best Practices

* Use `<strong>` instead of `<b>` when the text is important.
* Use `<em>` instead of `<i>` when the text needs emphasis.
* Use `<mark>` only to highlight important content.
* Use `<code>` for inline code snippets.
* Use `<pre>` when spacing and line breaks must be preserved.
* Avoid using `<u>` for regular text because users may mistake it for a hyperlink.
* Choose semantic tags whenever possible because they improve accessibility and SEO.

---

# Summary

| Tag            | Purpose                                       |
| -------------- | --------------------------------------------- |
| `<b>`          | Displays bold text without semantic meaning   |
| `<strong>`     | Marks important text (usually bold)           |
| `<i>`          | Displays italic text without semantic meaning |
| `<em>`         | Marks emphasized text (usually italic)        |
| `<mark>`       | Highlights text                               |
| `<small>`      | Displays smaller text                         |
| `<u>`          | Underlines text                               |
| `<del>`        | Represents deleted text                       |
| `<ins>`        | Represents inserted text (usually underlined) |
| `<sub>`        | Displays subscript text                       |
| `<sup>`        | Displays superscript text                     |
| `<code>`       | Displays inline code                          |
| `<pre>`        | Preserves whitespace and line breaks          |
| `<kbd>`        | Represents keyboard input                     |
| `<samp>`       | Represents program output                     |
| `<var>`        | Represents a variable                         |
| `<abbr>`       | Defines an abbreviation                       |
| `<cite>`       | Represents the title of a creative work       |
| `<q>`          | Displays a short quotation                    |
| `<blockquote>` | Displays a long quotation                     |

> **Remember:** Semantic tags (such as `<strong>`, `<em>`, `<abbr>`, and `<blockquote>`) not only format text but also describe its meaning, making web pages more accessible and easier for search engines to understand.
