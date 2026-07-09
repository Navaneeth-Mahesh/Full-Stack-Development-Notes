# HTML Buttons

The `<button>` element is used to create a **clickable button** on a webpage.

Buttons allow users to perform actions such as:

* Submitting a form
* Running JavaScript code
* Resetting a form
* Opening menus
* Triggering popups
* Navigating to another page (although links are usually better for navigation)

---

# Basic Syntax

```html
<button>Button Text</button>
```

## Example

```html
<button>Click Me</button>
```

**Output**

A clickable button displaying:

```text
[ Click Me ]
```

---

# How Buttons Work

```text
User Clicks Button
        │
        ▼
Browser Detects Click
        │
        ▼
Performs an Action
        │
        ├── Submit a Form
        ├── Run JavaScript
        ├── Reset a Form
        └── Open a Menu
```

---

# Button Types

The `type` attribute tells the browser what the button should do.

| Value    | Purpose                                                 |
| -------- | ------------------------------------------------------- |
| `button` | Performs a custom action (default choice outside forms) |
| `submit` | Submits a form                                          |
| `reset`  | Resets all form fields                                  |

## Syntax

```html
<button type="button">Button</button>

<button type="submit">Submit</button>

<button type="reset">Reset</button>
```

> **Important:** Inside a `<form>`, a `<button>` without a `type` attribute behaves like `type="submit"` in modern browsers. To avoid unexpected form submissions, explicitly set `type="button"` for buttons that should not submit the form.

---

# 1. Simple Button

```html
<button type="button">
    Click Me
</button>
```

This button does nothing until JavaScript is added.

---

# 2. Button with JavaScript

The `onclick` attribute executes JavaScript when the button is clicked.

## Example

```html
<button
    type="button"
    onclick="alert('Hello, World!')">
    Click Me
</button>
```

When clicked:

```text
Hello, World!
```

An alert dialog appears.

---

# 3. Button for Navigation

A button can navigate to another page using JavaScript.

## Internal Page

```html
<button
    type="button"
    onclick="location.href='about.html'">
    About Page
</button>
```

---

## External Website

```html
<button
    type="button"
    onclick="location.href='https://www.google.com'">
    Visit Google
</button>
```

> **Best Practice:** Use an `<a>` (anchor) element for navigation between pages. Use `<button>` for performing actions.

Example:

```html
<a href="about.html">
    About Us
</a>
```

---

# 4. Disabled Button

The `disabled` attribute prevents the button from being clicked.

## Example

```html
<button
    type="button"
    disabled>
    Submit
</button>
```

**Output**

The button appears disabled and cannot be clicked.

---

# 5. Tooltip

The `title` attribute displays a small tooltip when the user hovers over the button.

## Example

```html
<button
    type="button"
    title="Click to submit the form">
    Submit
</button>
```

Hovering over the button shows:

```text
Click to submit the form
```

---

# 6. Styling a Button

Buttons can be styled using CSS.

## Inline CSS Example

```html
<button
    type="button"
    style="
        background-color: royalblue;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    ">
    Styled Button
</button>
```

### CSS Properties Used

| Property           | Purpose                      |
| ------------------ | ---------------------------- |
| `background-color` | Changes button background    |
| `color`            | Changes text color           |
| `padding`          | Adds space inside the button |
| `border`           | Removes or adds a border     |
| `border-radius`    | Creates rounded corners      |
| `cursor: pointer`  | Shows a hand cursor on hover |

> In real projects, it's better to use an external CSS file instead of inline styles.

---

# 7. Button with an Image

A button can also contain images and other HTML elements.

```html
<button type="button">
    <img
        src="images/search.png"
        alt="Search"
        width="20">

    Search
</button>
```

---

# 8. Button with an Icon (Example)

```html
<button type="button">
    🔍 Search
</button>
```

Buttons can contain:

* Text
* Images
* Icons
* Multiple HTML elements

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Buttons</title>
</head>

<body>

    <h1>HTML Button Examples</h1>

    <!-- Simple Button -->
    <button type="button">
        Click Me
    </button>

    <br><br>

    <!-- Disabled Button -->
    <button
        type="button"
        disabled>
        Disabled Button
    </button>

    <br><br>

    <!-- Tooltip -->
    <button
        type="button"
        title="Click to continue">
        Hover Over Me
    </button>

    <br><br>

    <!-- JavaScript -->
    <button
        type="button"
        onclick="alert('Welcome to HTML!')">
        Show Alert
    </button>

    <br><br>

    <!-- Navigation -->
    <button
        type="button"
        onclick="location.href='about.html'">
        About Page
    </button>

    <br><br>

    <!-- Styled Button -->
    <button
        type="button"
        style="
            background-color: royalblue;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        ">
        Styled Button
    </button>

</body>

</html>
```

---

# Common Button Attributes

| Attribute  | Purpose                              |
| ---------- | ------------------------------------ |
| `type`     | Specifies the button type            |
| `onclick`  | Executes JavaScript when clicked     |
| `disabled` | Disables the button                  |
| `title`    | Displays a tooltip                   |
| `style`    | Applies inline CSS                   |
| `id`       | Gives the button a unique identifier |
| `class`    | Applies CSS classes                  |

---

# `<button>` vs `<input type="button">`

Both create clickable buttons, but `<button>` is more flexible.

| `<button>`                          | `<input type="button">` |
| ----------------------------------- | ----------------------- |
| Can contain text, images, and icons | Displays only text      |
| More flexible                       | Less flexible           |
| Preferred in modern HTML            | Used less often         |

Example:

```html
<button type="button">
    Save
</button>

<input
    type="button"
    value="Save">
```

---

# Common Beginner Mistakes

### ❌ Using a button for navigation

```html
<button onclick="location.href='about.html'">
    About
</button>
```

✔ Better

```html
<a href="about.html">
    About
</a>
```

---

### ❌ Forgetting the `type` attribute inside a form

```html
<form>

    <button>
        Cancel
    </button>

</form>
```

The button may submit the form unexpectedly.

✔ Better

```html
<button type="button">
    Cancel
</button>
```

---

### ❌ Using generic button text

```html
<button>
    Click Here
</button>
```

✔ Better

```html
<button>
    Download File
</button>
```

Users should understand exactly what the button does.

---

### ❌ Using inline CSS everywhere

```html
<button style="background:red;">
    Save
</button>
```

For larger projects, use external CSS files instead.

---

# Best Practices

* Use meaningful button text such as **Submit**, **Save**, **Download**, or **Login**.
* Use `<button>` for **actions**.
* Use `<a>` for **navigation**.
* Always specify the `type` attribute, especially inside forms.
* Disable buttons when an action is unavailable.
* Use CSS to style buttons instead of relying on browser defaults.
* Keep button labels short, clear, and action-oriented.

---

# Summary

| Tag / Attribute | Purpose                                |
| --------------- | -------------------------------------- |
| `<button>`      | Creates a clickable button             |
| `type`          | Defines the button's behavior          |
| `onclick`       | Runs JavaScript when clicked           |
| `disabled`      | Prevents the button from being clicked |
| `title`         | Displays a tooltip                     |
| `style`         | Applies inline CSS styling             |
| `id`            | Gives the button a unique identifier   |
| `class`         | Applies CSS classes                    |

---

# Key Points

* The `<button>` element creates clickable buttons for user interaction.
* Use `type="button"` for general-purpose buttons, `type="submit"` to submit forms, and `type="reset"` to reset forms.
* The `onclick` attribute allows buttons to execute JavaScript.
* Use the `disabled` attribute to make a button inactive.
* Use the `title` attribute to provide additional information on hover.
* A `<button>` can contain text, images, icons, and other HTML elements.
* Prefer `<button>` over `<input type="button">` because it is more flexible.
* Use `<button>` for actions and `<a>` for navigation to create semantic and accessible HTML.
