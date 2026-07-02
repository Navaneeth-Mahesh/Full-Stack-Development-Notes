# HTML Quotations

HTML provides special elements to display quotations, citations, abbreviations, and contact information in a meaningful way.

These elements do not just change appearance—they also add **semantic meaning** to the content.

---

# 1. Blockquote (`<blockquote>`)

The `<blockquote>` element is used for **long quotations** taken from another source.

### Syntax

```html
<blockquote cite="URL">
    Quoted text goes here.
</blockquote>
```

### Example

```html
<blockquote cite="https://www.w3schools.com">
    HTML is the standard markup language for creating web pages.
</blockquote>
```

### Output

A separate indented block of quoted text.

> Use `<blockquote>` when the quote is longer and needs its own section.

---

# 2. Inline Quote (`<q>`)

The `<q>` element is used for **short quotations** inside a sentence.

Browsers automatically add quotation marks.

### Syntax

```html
<q>Short quote</q>
```

### Example

```html
<p>
    W3Schools says, <q>Learning HTML is easy.</q>
</p>
```

---

# 3. Abbreviation (`<abbr>`)

The `<abbr>` element defines abbreviations or acronyms.

The full form is shown when you hover over the text.

### Syntax

```html
<abbr title="Full Form">Abbreviation</abbr>
```

### Example

```html
<p>
    <abbr title="HyperText Markup Language">HTML</abbr>
    is used to create webpages.
</p>
```

---

# 4. Address (`<address>`)

The `<address>` element is used to display **contact information**.

It can include name, email, location, or phone number.

### Syntax

```html
<address>
    Contact details here
</address>
```

### Example

```html
<address>
    Navaneeth<br>
    Andhra Pradesh, India<br>
    Email: nav@example.com
</address>
```

> Browsers usually display it in italic style by default.

---

# 5. Citation (`<cite>`)

The `<cite>` element is used to define the **title of a creative work** such as:

- Books
- Movies
- Songs
- Paintings
- Websites

### Syntax

```html
<cite>Work Title</cite>
```

### Example

```html
<p>
    My favorite book is <cite>Atomic Habits</cite>.
</p>
```

---

# 6. Bidirectional Override (`<bdo>`)

The `<bdo>` element overrides the text direction.

It is used to display text from:

- Left to Right (LTR)
- Right to Left (RTL)

### Syntax

```html
<bdo dir="rtl">Text</bdo>
```

### Example

```html
<p>
    <bdo dir="rtl">Hello World</bdo>
</p>
```

### Output

The text appears reversed.

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>HTML Quotations</title>
</head>

<body>

    <h1>HTML Quotations Examples</h1>

    <!-- Blockquote -->
    <blockquote cite="https://www.w3schools.com">
        HTML is the standard markup language for creating web pages.
    </blockquote>

    <!-- Inline Quote -->
    <p>
        W3Schools says, <q>Learning HTML is easy.</q>
    </p>

    <!-- Abbreviation -->
    <p>
        <abbr title="HyperText Markup Language">HTML</abbr>
        is the foundation of the web.
    </p>

    <!-- Address -->
    <address>
        Navaneeth<br>
        Andhra Pradesh, India<br>
        Email: nav@example.com
    </address>

    <!-- Citation -->
    <p>
        My favorite book is <cite>Atomic Habits</cite>.
    </p>

    <!-- Bidirectional Override -->
    <p>
        <bdo dir="rtl">Hello World</bdo>
    </p>

</body>
</html>
```

---

# Summary

| Tag | Purpose |
|-----|--------|
| `<blockquote>` | Displays long quoted content |
| `<q>` | Displays short inline quotation |
| `<abbr>` | Defines abbreviations with full form tooltip |
| `<address>` | Shows contact information |
| `<cite>` | Represents title of creative work |
| `<bdo>` | Overrides text direction |
```