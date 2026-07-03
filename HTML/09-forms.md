# HTML Forms

HTML Forms are used to **collect information from users**. The data entered in a form can be sent to a server for processing, such as creating an account, logging in, searching, submitting feedback, or placing an order.

Common examples of forms include:

- Login forms
- Registration forms
- Contact forms
- Search bars
- Feedback forms
- Online surveys

---

# How HTML Forms Work

```
User Fills Form
       │
       ▼
Browser Collects Data
       │
       ▼
<form> Sends Data
       │
       ▼
Server Receives Data
       │
       ▼
Processes Information
       │
       ▼
Returns a Response
```

---

# The `<form>` Element

The `<form>` element is the main container that holds all form controls such as text fields, buttons, checkboxes, and dropdowns.

## Syntax

```html
<form>
    <!-- Form elements go here -->
</form>
```

## Example

```html
<form>
    <label>Name:</label>
    <input type="text">
</form>
```

---

# Form Attributes

## `action`

The `action` attribute specifies **where the form data should be sent** after the user submits the form.

### Syntax

```html
<form action="/submit">
```

### Example

```html
<form action="/register">
```

If the `action` attribute is omitted, the form is submitted to the current page.

---

## `method`

The `method` attribute specifies **how the data is sent** to the server.

### Syntax

```html
<form method="GET">
```

or

```html
<form method="POST">
```

### GET vs POST

| Method | Description | Best Used For |
|----------|-------------|---------------|
| `GET` | Sends data through the URL | Search forms, filters, non-sensitive data |
| `POST` | Sends data inside the request body | Login, registration, passwords, payments |

### GET Example

```html
<form action="/search" method="GET">
```

URL after submission:

```
example.com/search?name=John
```

### POST Example

```html
<form action="/login" method="POST">
```

The submitted data is **not visible in the URL**.

---

# The `<label>` Element

The `<label>` element provides a description for an input field.

Using the `for` attribute connects the label to its corresponding input.

## Syntax

```html
<label for="username">Username</label>
<input type="text" id="username">
```

### Benefits

- Improves accessibility
- Makes forms easier to understand
- Clicking the label focuses the input field

---

# The `<input>` Element

The `<input>` element is used to create different kinds of input fields.

General syntax:

```html
<input type="...">
```

---

# Common Input Types

## 1. Text Input

Used for entering a single line of text.

```html
<input type="text">
```

Example

```html
<input
    type="text"
    placeholder="Enter your name">
```

---

## 2. Password Input

Used for entering passwords.

Characters appear as dots or asterisks.

```html
<input type="password">
```

---

## 3. Email Input

Used for entering email addresses.

The browser performs basic email validation.

```html
<input type="email">
```

Example

```html
<input
    type="email"
    placeholder="example@email.com">
```

---

## 4. Number Input

Accepts only numeric values.

```html
<input type="number">
```

Example

```html
<input
    type="number"
    min="1"
    max="100">
```

### Common Attributes

| Attribute | Purpose |
|-----------|---------|
| `min` | Minimum value |
| `max` | Maximum value |
| `step` | Increment value |

Example

```html
<input
    type="number"
    min="1"
    max="10"
    step="1">
```

---

## 5. Date Input

Displays a date picker.

```html
<input type="date">
```

---

## 6. Time Input

Allows users to select a time.

```html
<input type="time">
```

---

## 7. Datetime Input

Allows users to select both date and time.

```html
<input type="datetime-local">
```

---

## 8. Color Picker

Displays a color selection tool.

```html
<input type="color">
```

---

## 9. File Upload

Allows users to upload files.

```html
<input type="file">
```

Upload only images

```html
<input
    type="file"
    accept="image/*">
```

Allow multiple files

```html
<input
    type="file"
    multiple>
```

---

## 10. Checkbox

Checkboxes allow users to select **multiple options**.

```html
<input type="checkbox" id="html">
<label for="html">HTML</label>

<input type="checkbox" id="css">
<label for="css">CSS</label>
```

---

## 11. Radio Button

Radio buttons allow users to select **only one option**.

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

> **Important:** All radio buttons in the same group must have the same `name` attribute.

---

## 12. Range Slider

Creates a slider.

```html
<input
    type="range"
    min="0"
    max="100">
```

---

## 13. Search Input

Designed for search boxes.

```html
<input type="search">
```

---

## 14. URL Input

Accepts website URLs.

```html
<input type="url">
```

---

## 15. Telephone Input

Used for phone numbers.

```html
<input type="tel">
```

---

# Common Input Attributes

## `placeholder`

Displays temporary hint text inside an input field.

```html
<input
    type="text"
    placeholder="Enter your name">
```

---

## `value`

Sets the default value.

```html
<input
    type="text"
    value="Navaneeth">
```

---

## `required`

Makes a field mandatory.

```html
<input
    type="email"
    required>
```

---

## `readonly`

Prevents editing.

```html
<input
    type="text"
    value="HTML"
    readonly>
```

---

## `disabled`

Disables the input.

```html
<input
    type="text"
    disabled>
```

Disabled fields **are not submitted** with the form.

---

## `maxlength`

Limits the maximum number of characters.

```html
<input
    type="text"
    maxlength="20">
```

---

## `minlength`

Specifies the minimum number of characters.

```html
<input
    type="password"
    minlength="8">
```

---

## `autocomplete`

Controls browser auto-fill.

```html
<input
    type="email"
    autocomplete="on">
```

or

```html
<input
    type="email"
    autocomplete="off">
```

---

## `autofocus`

Automatically focuses the input when the page loads.

```html
<input
    type="text"
    autofocus>
```

---

## `name`

The `name` attribute identifies the input when data is sent to the server.

```html
<input
    type="text"
    name="username">
```

> Without a `name` attribute, most form fields are **not included** in the submitted data.

---

# The `<textarea>` Element

Creates a multi-line text input.

```html
<textarea
    rows="5"
    cols="30">
</textarea>
```

Example

```html
<textarea
    rows="6"
    cols="40"
    placeholder="Write your message...">
</textarea>
```

---

# The `<select>` Element

Creates a dropdown list.

```html
<select>
    <option>HTML</option>
    <option>CSS</option>
    <option>JavaScript</option>
</select>
```

---

# The `<option>` Element

Represents an item inside a dropdown.

```html
<option>HTML</option>
```

Default selected option

```html
<option selected>HTML</option>
```

---

# The `<optgroup>` Element

Groups related options.

```html
<select>

    <optgroup label="Frontend">
        <option>HTML</option>
        <option>CSS</option>
    </optgroup>

    <optgroup label="Backend">
        <option>Node.js</option>
        <option>Java</option>
    </optgroup>

</select>
```

---

# The `<button>` Element

Creates a clickable button.

```html
<button type="submit">
    Submit
</button>
```

## Button Types

| Type | Purpose |
|------|---------|
| `submit` | Submits the form |
| `reset` | Clears all form fields |
| `button` | General-purpose button (usually with JavaScript) |

---

# Useful Form Attributes

| Attribute | Description |
|-----------|-------------|
| `action` | Where the data is sent |
| `method` | GET or POST |
| `name` | Name of the field |
| `id` | Unique identifier |
| `placeholder` | Hint text |
| `value` | Default value |
| `required` | Mandatory field |
| `readonly` | Read-only |
| `disabled` | Disabled field |
| `maxlength` | Maximum characters |
| `minlength` | Minimum characters |
| `autocomplete` | Enables or disables autofill |
| `autofocus` | Focuses input automatically |

---

# Complete Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>Student Registration Form</title>
</head>

<body>

<form action="/register" method="POST">

    <label for="name">Full Name</label><br>
    <input
        type="text"
        id="name"
        name="name"
        placeholder="Enter your name"
        required>

    <br><br>

    <label for="email">Email</label><br>
    <input
        type="email"
        id="email"
        name="email"
        required>

    <br><br>

    <label for="password">Password</label><br>
    <input
        type="password"
        id="password"
        name="password"
        minlength="8"
        required>

    <br><br>

    <label>Gender</label><br>

    <input
        type="radio"
        id="male"
        name="gender"
        value="Male">

    <label for="male">Male</label>

    <input
        type="radio"
        id="female"
        name="gender"
        value="Female">

    <label for="female">Female</label>

    <br><br>

    <label>Skills</label><br>

    <input
        type="checkbox"
        id="html"
        name="skills"
        value="HTML">

    <label for="html">HTML</label>

    <input
        type="checkbox"
        id="css"
        name="skills"
        value="CSS">

    <label for="css">CSS</label>

    <br><br>

    <label for="course">Course</label><br>

    <select
        id="course"
        name="course">

        <option>HTML</option>
        <option>CSS</option>
        <option>JavaScript</option>

    </select>

    <br><br>

    <label for="message">Message</label><br>

    <textarea
        id="message"
        name="message"
        rows="5"
        cols="30"
        placeholder="Write your message...">
    </textarea>

    <br><br>

    <button type="submit">
        Register
    </button>

    <button type="reset">
        Reset
    </button>

</form>

</body>
</html>
```

---

# Best Practices

- Always use `<label>` with form fields.
- Use meaningful `name` attributes.
- Use `required` for mandatory inputs.
- Use `POST` when sending sensitive information.
- Group related radio buttons using the same `name`.
- Use placeholders only as hints—not as replacements for labels.
- Choose the correct input type (`email`, `number`, `date`, etc.) for better user experience and built-in validation.

---

# Summary

| Element/Attribute | Purpose |
|-------------------|---------|
| `<form>` | Creates a form |
| `action` | Specifies where form data is sent |
| `method` | Defines how data is sent |
| `<label>` | Describes an input field |
| `<input>` | Creates an input field |
| `type` | Specifies the input type |
| `name` | Identifies the field when submitted |
| `id` | Unique identifier for an element |
| `placeholder` | Displays hint text |
| `value` | Sets the default value |
| `required` | Makes a field mandatory |
| `readonly` | Prevents editing |
| `disabled` | Disables the field |
| `maxlength` | Limits the number of characters |
| `minlength` | Sets the minimum number of characters |
| `<textarea>` | Creates a multi-line text box |
| `<select>` | Creates a dropdown menu |
| `<option>` | Defines a dropdown item |
| `<optgroup>` | Groups related dropdown options |
| `<button>` | Creates a clickable button |