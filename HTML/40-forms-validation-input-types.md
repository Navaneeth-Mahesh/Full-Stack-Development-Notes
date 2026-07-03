# HTML Forms, Input Types & Validation

HTML **forms** are used to collect user input. This input can then be sent to a server for processing.

Forms are essential for:
- Login pages
- Registration pages
- Contact forms
- Surveys
- Search boxes

---

# Basic Form Structure

```html
<form action="/submit" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">

    <input type="submit" value="Submit">
</form>
```

---

# `<form>` Element

The `<form>` tag is used to create an HTML form.

### Common Attributes:

| Attribute | Description |
|----------|-------------|
| `action` | URL where form data is sent |
| `method` | HTTP method (GET or POST) |
| `target` | Where to display response |
| `autocomplete` | Enables/disables autofill |

Example:

```html
<form action="/submit" method="POST">
```

---

# Input Element

The `<input>` tag is used to accept user data.

Syntax:

```html
<input type="text">
```

---

# Common Input Types

## Text Inputs

```html
<input type="text">
<input type="password">
<input type="email">
<input type="search">
```

---

## Number & Date Inputs

```html
<input type="number">
<input type="date">
<input type="time">
<input type="datetime-local">
```

---

## Selection Inputs

```html
<input type="radio">
<input type="checkbox">
```

Example:

```html
<input type="radio" name="gender" value="male"> Male
<input type="radio" name="gender" value="female"> Female
```

---

## File & Media Inputs

```html
<input type="file">
<input type="image">
```

---

## Button Inputs

```html
<input type="submit">
<input type="reset">
<input type="button" value="Click Me">
```

---

# Label Element

The `<label>` tag improves accessibility and usability.

Example:

```html
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

Clicking the label focuses the input field.

---

# Placeholder Attribute

Shows hint text inside input fields.

```html
<input type="text" placeholder="Enter your name">
```

---

# Required Attribute

Makes a field mandatory.

```html
<input type="text" required>
```

---

# Pattern Validation

Used for custom input rules using regex.

Example:

```html
<input type="text" pattern="[A-Za-z]{3,}">
```

Only allows at least 3 letters.

---

# Min and Max

Used for number and date inputs.

```html
<input type="number" min="1" max="10">
```

---

# Maxlength

Limits number of characters.

```html
<input type="text" maxlength="10">
```

---

# Disabled & Readonly

```html
<input type="text" value="Disabled" disabled>

<input type="text" value="Readonly" readonly>
```

- `disabled` → cannot be edited or submitted
- `readonly` → cannot be edited but is submitted

---

# Select Dropdown

```html
<select name="country">
    <option value="india">India</option>
    <option value="usa">USA</option>
    <option value="uk">UK</option>
</select>
```

---

# Textarea

Used for multi-line input.

```html
<textarea rows="4" cols="50" placeholder="Enter message"></textarea>
```

---

# Fieldset & Legend

Used to group related form elements.

```html
<fieldset>
    <legend>Personal Info</legend>

    <input type="text" placeholder="Name">
    <input type="email" placeholder="Email">

</fieldset>
```

---

# Form Validation

HTML provides built-in validation features:

## Required Field

```html
<input type="text" required>
```

## Email Validation

```html
<input type="email">
```

## Number Range

```html
<input type="number" min="10" max="100">
```

## Pattern Matching

```html
<input type="text" pattern="[0-9]{10}">
```

---

# Complete Form Example

```html
<form action="/submit" method="POST">

    <fieldset>
        <legend>Registration Form</legend>

        <label>Name:</label>
        <input type="text" required>

        <br><br>

        <label>Email:</label>
        <input type="email" required>

        <br><br>

        <label>Password:</label>
        <input type="password" required minlength="6">

        <br><br>

        <label>Age:</label>
        <input type="number" min="18" max="60">

        <br><br>

        <label>Gender:</label>
        <input type="radio" name="gender"> Male
        <input type="radio" name="gender"> Female

        <br><br>

        <label>Country:</label>
        <select>
            <option>India</option>
            <option>USA</option>
        </select>

        <br><br>

        <textarea placeholder="Your message"></textarea>

        <br><br>

        <input type="submit">
        <input type="reset">

    </fieldset>

</form>
```

---

# Summary

- HTML forms collect user input.
- `<input>` supports many types like text, email, number, checkbox, etc.
- Validation helps ensure correct data entry.
- Attributes like `required`, `pattern`, `min`, `max`, and `maxlength` control input rules.
- `<select>` and `<textarea>` provide advanced input options.
- `<label>` improves accessibility and usability.