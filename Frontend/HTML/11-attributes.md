# HTML Attributes

HTML **attributes** provide **additional information** about HTML elements. They modify an element's behavior, appearance, or functionality.

Attributes are always written inside the **opening tag**.

---

# Syntax

```html
<tagname attribute="value">Content</tagname>
```

### Example

```html
<a href="https://example.com">Visit Website</a>
```

### Explanation

* `<a>` → Anchor (link) element
* `href` → Attribute name
* `"https://example.com"` → Attribute value
* `Visit Website` → Visible link text

---

# How Attributes Work

```text
Opening Tag
     │
     ▼
<a href="https://example.com" target="_blank">
 │              │                     │
 │              │                     └── Opens link in a new tab
 │              └──────────────────────── Destination URL
 └────────────────────────────────────── Element
```

---

# Rules for HTML Attributes

* Attributes are written inside the **opening tag**.
* Most attributes have:

  * **Attribute name**
  * **Attribute value**
* Attribute values should be enclosed in **double quotes (`"`).**
* Some attributes are **global attributes**, meaning they can be used on almost every HTML element.
* An element can have **multiple attributes**.

### Example

```html
<img
    src="nature.jpg"
    alt="Beautiful mountain landscape"
    width="400"
    height="250">
```

In this example:

| Attribute | Purpose                                   |
| --------- | ----------------------------------------- |
| `src`     | Specifies the image location              |
| `alt`     | Alternative text if the image cannot load |
| `width`   | Sets image width                          |
| `height`  | Sets image height                         |

---

# Common HTML Attributes

## 1. `id`

The `id` attribute gives an element a **unique identifier**.

Each `id` should be used **only once** on a webpage.

### Example

```html
<h1 id="main-title">Welcome</h1>
```

### Uses

* CSS styling
* JavaScript
* Page navigation (bookmarks)

✅ Good

```html
<h1 id="header">Home</h1>
```

❌ Wrong (Duplicate IDs)

```html
<h1 id="title">Heading 1</h1>
<h2 id="title">Heading 2</h2>
```

---

## 2. `class`

The `class` attribute groups one or more elements together.

Unlike `id`, the same class can be used on **multiple elements**.

### Example

```html
<p class="highlight">
    This is highlighted text.
</p>
```

Multiple classes can be assigned.

```html
<p class="highlight large">
    Hello World
</p>
```

### Why use classes?

* Apply the same CSS style to multiple elements.
* Select multiple elements using JavaScript.

---

## Difference Between `id` and `class`

| Feature            | `id`  | `class`  |
| ------------------ | ----- | -------- |
| Must be unique?    | ✅ Yes | ❌ No     |
| Can be reused?     | ❌ No  | ✅ Yes    |
| Used in CSS        | `#id` | `.class` |
| Used in JavaScript | Yes   | Yes      |

---

## 3. `style`

The `style` attribute applies **inline CSS** directly to an element.

### Example

```html
<p style="color: blue;">
    Blue Text
</p>
```

Another example:

```html
<h2 style="color:red; text-align:center;">
    Welcome
</h2>
```

> **Note:** Inline styles are useful for quick testing, but for larger projects, use an external CSS file.

---

## 4. `title`

The `title` attribute displays a tooltip when the user hovers over an element.

### Example

```html
<p title="This is a tooltip">
    Hover over me
</p>
```

---

## 5. `href`

Used with the `<a>` element to specify the destination URL.

### Example

```html
<a href="https://example.com">
    Visit Website
</a>
```

### Types of Links

External website

```html
<a href="https://google.com">Google</a>
```

Internal page

```html
<a href="about.html">About Us</a>
```

Email

```html
<a href="mailto:hello@example.com">
    Email Us
</a>
```

Phone number

```html
<a href="tel:+911234567890">
    Call Us
</a>
```

---

## 6. `src`

The `src` attribute specifies the location of an external resource.

Commonly used with:

* Images
* Audio
* Video
* Scripts
* Iframes

### Example

```html
<img src="logo.png" alt="Company Logo">
```

---

## 7. `alt`

The `alt` attribute provides alternative text for an image.

It is displayed when:

* The image fails to load.
* A screen reader reads the webpage.
* Users have images disabled.

### Example

```html
<img
    src="cat.jpg"
    alt="White cat sitting on a sofa">
```

> **Best Practice:** Always write meaningful `alt` text.

---

## 8. `width` and `height`

Used to define an element's size.

### Example

```html
<img
    src="nature.jpg"
    alt="Nature"
    width="400"
    height="250">
```

---

## 9. `lang`

Specifies the language of the webpage.

Usually added to the `<html>` element.

### Example

```html
<html lang="en">
```

Other examples

```html
<html lang="fr">
```

```html
<html lang="hi">
```

---

## 10. `target`

Specifies where a linked document opens.

### Example

```html
<a
    href="https://example.com"
    target="_blank">
    Open Website
</a>
```

### Common Values

| Value     | Description                        |
| --------- | ---------------------------------- |
| `_self`   | Opens in the current tab (default) |
| `_blank`  | Opens in a new tab                 |
| `_parent` | Opens in the parent frame          |
| `_top`    | Opens in the full browser window   |

> **Security Tip:** When using `target="_blank"` for external links, it's recommended to also use `rel="noopener noreferrer"`.

Example:

```html
<a
    href="https://example.com"
    target="_blank"
    rel="noopener noreferrer">
    Visit Website
</a>
```

---

## 11. `disabled`

Disables form controls.

### Example

```html
<button disabled>
    Submit
</button>
```

Also works with:

```html
<input disabled>

<select disabled>

<textarea disabled></textarea>
```

---

## 12. `readonly`

Makes an input field read-only.

Users can select the text but cannot edit it.

### Example

```html
<input
    type="text"
    value="Hello"
    readonly>
```

---

## 13. `placeholder`

Displays hint text inside an input field.

### Example

```html
<input
    type="text"
    placeholder="Enter your name">
```

---

## 14. `required`

Makes a form field mandatory.

### Example

```html
<input
    type="email"
    required>
```

If left empty, the browser prevents form submission.

---

## 15. `value`

Specifies the initial value of an input.

### Example

```html
<input
    type="text"
    value="Navaneeth">
```

---

## 16. `name`

Assigns a name to form elements.

It is required when sending form data to a server.

### Example

```html
<input
    type="text"
    name="username">
```

---

## 17. `checked`

Used for checkboxes and radio buttons.

### Example

```html
<input
    type="checkbox"
    checked>
```

---

## 18. `selected`

Preselects an option inside a dropdown.

### Example

```html
<select>
    <option>Java</option>
    <option selected>HTML</option>
    <option>CSS</option>
</select>
```

---

## 19. `multiple`

Allows selecting multiple files or options.

### Example

```html
<input
    type="file"
    multiple>
```

---

## 20. `autofocus`

Automatically focuses an element when the page loads.

### Example

```html
<input
    type="text"
    autofocus>
```

---

# Global Attributes

Global attributes can be used on **almost every HTML element**.

| Attribute         | Purpose                              |
| ----------------- | ------------------------------------ |
| `id`              | Unique identifier                    |
| `class`           | Groups elements                      |
| `style`           | Inline CSS                           |
| `title`           | Tooltip                              |
| `lang`            | Language of the element              |
| `hidden`          | Hides an element                     |
| `tabindex`        | Controls keyboard navigation         |
| `draggable`       | Makes an element draggable           |
| `contenteditable` | Allows users to edit content         |
| `spellcheck`      | Enables or disables spell checking   |
| `dir`             | Sets text direction (`ltr` or `rtl`) |
| `data-*`          | Stores custom data                   |

Example:

```html
<p data-user="101">
    Welcome
</p>
```

---

# Boolean Attributes

Boolean attributes do **not require a value**.

Their presence alone enables the feature.

Example:

```html
<input type="checkbox" checked>

<input type="text" readonly>

<button disabled>
    Submit
</button>

<input required>
```

Common boolean attributes

* `checked`
* `disabled`
* `readonly`
* `required`
* `selected`
* `autofocus`
* `multiple`
* `hidden`

---

# Multiple Attributes Example

An element can have several attributes.

```html
<input
    type="email"
    id="email"
    class="input-field"
    name="email"
    placeholder="Enter your email"
    required
    autofocus>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>HTML Attributes</title>
</head>

<body>

    <h1 id="heading">HTML Attributes</h1>

    <p
        class="intro"
        title="Introduction">
        Welcome to HTML.
    </p>

    <a
        href="https://example.com"
        target="_blank"
        rel="noopener noreferrer">
        Visit Website
    </a>

    <br><br>

    <img
        src="nature.jpg"
        alt="Mountain landscape"
        width="300">

    <br><br>

    <input
        type="text"
        name="username"
        placeholder="Enter your name"
        required>

    <br><br>

    <button disabled>
        Submit
    </button>

</body>

</html>
```

---

# Best Practices

* Always use **double quotes** around attribute values.
* Use meaningful `id` and `class` names.
* Keep attribute names in **lowercase**.
* Always include the `alt` attribute for images.
* Avoid excessive inline styles; prefer external CSS.
* Use `target="_blank"` together with `rel="noopener noreferrer"` for external links.
* Choose descriptive names for `id`, `class`, and `name` attributes.

---

# Common Beginner Mistakes

❌ Missing quotes

```html
<img src=photo.jpg>
```

✅ Correct

```html
<img src="photo.jpg">
```

---

❌ Duplicate IDs

```html
<p id="box"></p>
<div id="box"></div>
```

✅ Correct

```html
<p id="box"></p>
<div id="box2"></div>
```

---

❌ Missing `alt`

```html
<img src="cat.jpg">
```

✅ Correct

```html
<img
    src="cat.jpg"
    alt="White cat sitting on a sofa">
```

---

# Summary

| Attribute     | Purpose                                  |
| ------------- | ---------------------------------------- |
| `id`          | Unique identifier                        |
| `class`       | Groups elements for CSS and JavaScript   |
| `style`       | Applies inline CSS                       |
| `title`       | Displays a tooltip                       |
| `href`        | Specifies a hyperlink destination        |
| `src`         | Specifies the source of a resource       |
| `alt`         | Alternative text for images              |
| `width`       | Sets element width                       |
| `height`      | Sets element height                      |
| `lang`        | Specifies the page language              |
| `target`      | Specifies where a link opens             |
| `name`        | Identifies form data when submitted      |
| `value`       | Sets the initial value of a form element |
| `disabled`    | Disables an element                      |
| `readonly`    | Makes an input read-only                 |
| `placeholder` | Displays hint text                       |
| `required`    | Makes a field mandatory                  |
| `checked`     | Pre-selects a checkbox or radio button   |
| `selected`    | Pre-selects a dropdown option            |
| `multiple`    | Allows multiple selections               |
| `autofocus`   | Focuses an element when the page loads   |

---

## Key Takeaways

* HTML attributes provide extra information about elements.
* Attributes are placed inside the opening tag.
* Most attributes use the format `attribute="value"`.
* Some attributes (like `disabled` and `required`) are **boolean attributes** and don't need a value.
* `id` should be **unique**, while `class` can be shared by multiple elements.
* Always write meaningful attribute values and follow HTML best practices for readable, accessible code.
