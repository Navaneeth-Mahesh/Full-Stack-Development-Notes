# HTML Buttons

The `<button>` element is used to create a **clickable button** on a webpage. Buttons can perform actions such as submitting forms, navigating to another page, or executing JavaScript code.

---

# Basic Syntax

```html
<button>Button Text</button>
```

### Example

```html
<button>Click Me</button>
```

Output:

A button displaying the text **Click Me**.

---

# Button with JavaScript

The `onclick` attribute allows you to execute JavaScript when the button is clicked.

### Example

```html
<button onclick="alert('Hello, World!')">
    Click Me
</button>
```

When the button is clicked, an alert box appears with the message:

```
Hello, World!
```

---

# Button to Navigate to Another Page

You can use JavaScript to redirect the user to another webpage.

### Example

```html
<button onclick="document.location='about.html'">
    Go to About Page
</button>
```

You can also navigate to an external website.

```html
<button onclick="document.location='https://www.google.com'">
    Visit Google
</button>
```

> **Note:** For simple navigation, using an `<a>` (anchor) element styled as a button is generally preferred over using JavaScript.

---

# Disable a Button

Use the `disabled` attribute to prevent the button from being clicked.

### Example

```html
<button disabled>
    Submit
</button>
```

---

# Add a Tooltip

Use the `title` attribute to display a tooltip when the user hovers over the button.

### Example

```html
<button title="Click to submit the form">
    Submit
</button>
```

---

# Button with Inline CSS

The `style` attribute can be used to change the appearance of a button.

### Example

```html
<button
    style="
        background-color: royalblue;
        color: white;
        padding: 10px 20px;
    ">
    Styled Button
</button>
```

---

# Complete Example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>HTML Buttons</title>
</head>

<body>

    <h1>HTML Button Examples</h1>

    <!-- Simple Button -->
    <button>Click Me</button>

    <br><br>

    <!-- Disabled Button -->
    <button disabled>
        Disabled Button
    </button>

    <br><br>

    <!-- Tooltip -->
    <button title="Click to continue">
        Hover Over Me
    </button>

    <br><br>

    <!-- JavaScript Button -->
    <button onclick="alert('Welcome to HTML!')">
        Show Alert
    </button>

    <br><br>

    <!-- Navigation Button -->
    <button onclick="document.location='https://www.google.com'">
        Visit Google
    </button>

</body>

</html>
```

---

# Best Practices

- Use meaningful button text such as **Submit**, **Save**, or **Download** instead of generic labels like **Click Here**.
- Use the `<button>` element for actions.
- Use the `<a>` element for navigation between pages.
- Disable buttons when an action is not available.
- Add a `title` attribute only when it provides useful additional information.

---

# Summary

| Tag / Attribute | Purpose |
|-----------------|---------|
| `<button>` | Creates a clickable button |
| `onclick` | Executes JavaScript when clicked |
| `disabled` | Disables the button |
| `title` | Displays a tooltip on hover |
| `style` | Applies inline CSS styling |