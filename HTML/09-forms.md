# HTML Forms

HTML forms are used to collect user input, such as names, email addresses, passwords, feedback, and more.

A form can contain different input elements like text fields, radio buttons, checkboxes, dropdown lists, and buttons.

---

# The `<form>` Element

The `<form>` element is the container for all form controls.

## Basic Syntax

```html
<form>
    <!-- Form elements go here -->
</form>
```

### Example

```html
<form>
    <label>Name:</label>
    <input type="text">
</form>
```

---

# The `action` Attribute

The `action` attribute specifies where the form data should be sent after submission.

### Example

```html
<form action="/submit">
    ...
</form>
```

---

# The `method` Attribute

The `method` attribute specifies how the form data is sent.

| Method | Description |
|--------|-------------|
| `GET` | Sends data through the URL. Best for search forms and non-sensitive data. |
| `POST` | Sends data in the request body. Best for passwords, login forms, and sensitive information. |

### Example

```html
<form action="/login" method="POST">
```

---

# The `<label>` Element

The `<label>` element provides a description for an input field.

Using the `for` attribute improves accessibility.

### Example

```html
<label for="username">Username</label>
<input type="text" id="username">
```

---

# The `<input>` Element

The `<input>` element is used to create different types of input fields.

## Text Input

```html
<input type="text">
```

### Example

```html
<input
    type="text"
    placeholder="Enter your name">
```

---

## Password Input

```html
<input type="password">
```

Passwords are hidden as dots or asterisks.

---

## Email Input

```html
<input type="email">
```

Browsers can validate whether the entered value looks like an email address.

---

## Number Input

```html
<input type="number">
```

Example:

```html
<input
    type="number"
    min="1"
    max="100">
```

---

## Date Input

```html
<input type="date">
```

Displays a date picker in supported browsers.

---

## Color Picker

```html
<input type="color">
```

Allows users to select a color.

---

## File Upload

```html
<input type="file">
```

Allows users to upload files.

---

## Checkbox

Checkboxes allow users to select **multiple options**.

### Example

```html
<input type="checkbox" id="html">
<label for="html">HTML</label>

<input type="checkbox" id="css">
<label for="css">CSS</label>
```

---

## Radio Button

Radio buttons allow users to select **only one option** from a group.

### Example

```html
<input
    type="radio"
    id="male"
    name="gender">

<label for="male">Male</label>

<input
    type="radio"
    id="female"
    name="gender">

<label for="female">Female</label>
```

> Radio buttons must have the same `name` attribute to behave as a group.

---

# Placeholder

The `placeholder` attribute displays temporary hint text inside an input field.

### Example

```html
<input
    type="email"
    placeholder="Enter your email">
```

---

# Required Field

The `required` attribute makes an input mandatory before submitting the form.

### Example

```html
<input
    type="text"
    required>
```

---

# Readonly Field

The `readonly` attribute prevents the user from editing the input.

### Example

```html
<input
    type="text"
    value="HTML"
    readonly>
```

---

# Disabled Field

The `disabled` attribute disables an input field.

### Example

```html
<input
    type="text"
    disabled>
```

---

# The `<textarea>` Element

Used to create a multi-line text input.

### Example

```html
<textarea
    rows="5"
    cols="30">
</textarea>
```

---

# The `<select>` Element

Creates a dropdown list.

### Example

```html
<select>

    <option>HTML</option>

    <option>CSS</option>

    <option>JavaScript</option>

</select>
```

---

# The `<button>` Element

Creates a clickable button.

### Example

```html
<button type="submit">
    Submit
</button>
```

Other button types:

| Type | Description |
|------|-------------|
| `submit` | Submits the form |
| `reset` | Resets all form fields |
| `button` | Generic button used with JavaScript |

---

# Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML Forms</title>
</head>

<body>

<form action="/submit" method="POST">

    <label for="name">Name</label>
    <input
        type="text"
        id="name"
        placeholder="Enter your name"
        required>

    <br><br>

    <label for="email">Email</label>
    <input
        type="email"
        id="email"
        required>

    <br><br>

    <label for="password">Password</label>
    <input
        type="password"
        id="password">

    <br><br>

    <label>Gender</label>

    <input
        type="radio"
        id="male"
        name="gender">

    <label for="male">Male</label>

    <input
        type="radio"
        id="female"
        name="gender">

    <label for="female">Female</label>

    <br><br>

    <label>Skills</label>

    <input
        type="checkbox"
        id="html">

    <label for="html">HTML</label>

    <input
        type="checkbox"
        id="css">

    <label for="css">CSS</label>

    <br><br>

    <label for="course">Course</label>

    <select id="course">
        <option>HTML</option>
        <option>CSS</option>
        <option>JavaScript</option>
    </select>

    <br><br>

    <label for="message">Message</label>

    <textarea
        id="message"
        rows="5"
        cols="30">
    </textarea>

    <br><br>

    <button type="submit">
        Submit
    </button>

</form>

</body>
</html>
```

---

# Summary

| Element/Attribute | Purpose |
|-------------------|---------|
| `<form>` | Creates a form |
| `action` | Specifies where form data is sent |
| `method` | Specifies how data is sent (`GET` or `POST`) |
| `<label>` | Adds a label for an input |
| `<input>` | Creates an input field |
| `type` | Defines the input type |
| `placeholder` | Displays hint text |
| `required` | Makes a field mandatory |
| `readonly` | Prevents editing |
| `disabled` | Disables an input field |
| `<textarea>` | Creates a multi-line text box |
| `<select>` | Creates a dropdown list |
| `<option>` | Defines an item in a dropdown |
| `<button>` | Creates a clickable button |