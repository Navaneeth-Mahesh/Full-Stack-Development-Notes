# HTML Forms

HTML forms are used to collect user input, such as names, email addresses, passwords, feedback, and more. The collected data is usually sent to a server for processing.

Examples of forms include:

- Login Form
- Registration Form
- Contact Form
- Feedback Form
- Survey Form

---

# The `<form>` Element

The `<form>` element is the container for all form controls.

### Syntax

```html
<form>
    Form elements go here
</form>
```

Example:

```html
<form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
</form>
```

---

# Basic Form Example

```html
<form>

    <label for="fname">First Name:</label>
    <input type="text" id="fname" name="fname">

    <br><br>

    <label for="lname">Last Name:</label>
    <input type="text" id="lname" name="lname">

</form>
```

Output:

```
First Name: [________]

Last Name : [________]
```

---

# The `<input>` Element

The `<input>` element is the most commonly used form element.

It is used to create different types of input fields depending on the `type` attribute.

### Syntax

```html
<input type="text">
```

---

# Common Input Types

| Input Type | Description |
|------------|-------------|
| `text` | Single-line text input |
| `password` | Password field |
| `email` | Email input |
| `number` | Number input |
| `radio` | Select one option |
| `checkbox` | Select multiple options |
| `submit` | Submit the form |
| `reset` | Reset all fields |
| `button` | Normal button |
| `date` | Date picker |
| `color` | Color picker |
| `file` | Upload a file |

---

# Text Input

Used to enter a single line of text.

```html
<label for="username">Username:</label>

<input
    type="text"
    id="username"
    name="username">
```

---

# Password Input

Characters entered are hidden.

```html
<label for="password">Password:</label>

<input
    type="password"
    id="password"
    name="password">
```

---

# Email Input

Accepts email addresses.

```html
<label for="email">Email:</label>

<input
    type="email"
    id="email"
    name="email">
```

---

# Number Input

Allows only numbers.

```html
<input
    type="number"
    name="age">
```

---

# The `<label>` Element

The `<label>` element provides a descriptive label for an input field.

### Syntax

```html
<label for="email">
    Email
</label>
```

The `for` attribute should match the `id` of the corresponding input.

Example:

```html
<label for="email">Email</label>

<input
    type="email"
    id="email">
```

### Benefits

- Improves accessibility.
- Makes forms easier to understand.
- Clicking the label focuses the input.

---

# Radio Buttons

Radio buttons allow users to select **only one** option.

Example:

```html
<p>Select your favorite language:</p>

<input
    type="radio"
    id="html"
    name="language"
    value="HTML">

<label for="html">HTML</label>

<br>

<input
    type="radio"
    id="css"
    name="language"
    value="CSS">

<label for="css">CSS</label>

<br>

<input
    type="radio"
    id="js"
    name="language"
    value="JavaScript">

<label for="js">JavaScript</label>
```

> **Note:** Radio buttons belong to the same group when they share the same `name` attribute.

---

# Checkboxes

Checkboxes allow users to select **zero, one, or multiple** options.

Example:

```html
<input
    type="checkbox"
    id="bike"
    name="vehicle"
    value="Bike">

<label for="bike">Bike</label>

<br>

<input
    type="checkbox"
    id="car"
    name="vehicle"
    value="Car">

<label for="car">Car</label>

<br>

<input
    type="checkbox"
    id="boat"
    name="vehicle"
    value="Boat">

<label for="boat">Boat</label>
```

---

# Submit Button

The submit button sends the form data to the server.

Example:

```html
<form action="/submit">

    <label for="name">Name:</label>

    <input
        type="text"
        id="name"
        name="name">

    <br><br>

    <input
        type="submit"
        value="Submit">

</form>
```

---

# Reset Button

Resets all form fields.

```html
<input type="reset">
```

---

# Button

Creates a normal clickable button.

```html
<button>
    Click Me
</button>
```

---

# Important Input Attributes

## `id`

Provides a unique identifier.

```html
<input id="email">
```

---

## `name`

Specifies the field name sent to the server.

```html
<input
    name="username">
```

> Without the `name` attribute, the input value is **not submitted**.

---

## `value`

Sets the default value.

```html
<input
    type="text"
    value="Navaneeth">
```

---

## `placeholder`

Displays hint text inside the input.

```html
<input
    type="text"
    placeholder="Enter your name">
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
    value="India"
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

---

# Important `<form>` Attributes

## `action`

Specifies where form data is sent.

```html
<form action="/register">
```

---

## `method`

Specifies how data is sent.

```html
<form method="GET">
```

or

```html
<form method="POST">
```

### GET

- Data appears in the URL.
- Used for searching.

### POST

- Data is hidden.
- Used for login, registration, payments, etc.

---

## `autocomplete`

Turns browser suggestions on or off.

```html
<form autocomplete="on">
```

---

## `target`

Specifies where to display the response.

```html
<form target="_blank">
```

---

# Complete Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>HTML Forms</title>
</head>

<body>

<h2>Student Registration Form</h2>

<form action="/submit" method="POST">

    <label for="name">Full Name:</label><br>
    <input
        type="text"
        id="name"
        name="name"
        placeholder="Enter your name"
        required>

    <br><br>

    <label for="email">Email:</label><br>
    <input
        type="email"
        id="email"
        name="email"
        required>

    <br><br>

    <label for="password">Password:</label><br>
    <input
        type="password"
        id="password"
        name="password">

    <br><br>

    <p>Gender</p>

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

    <p>Skills</p>

    <input
        type="checkbox"
        id="html"
        name="skill"
        value="HTML">

    <label for="html">HTML</label>

    <input
        type="checkbox"
        id="css"
        name="skill"
        value="CSS">

    <label for="css">CSS</label>

    <input
        type="checkbox"
        id="js"
        name="skill"
        value="JavaScript">

    <label for="js">JavaScript</label>

    <br><br>

    <input
        type="submit"
        value="Register">

    <input
        type="reset"
        value="Reset">

</form>

</body>
</html>
```

---

# Summary

| Element/Attribute | Purpose |
|-------------------|---------|
| `<form>` | Creates a form |
| `<input>` | Creates an input field |
| `<label>` | Adds a label for an input |
| `type` | Specifies the input type |
| `id` | Unique identifier |
| `name` | Sends data to the server |
| `value` | Default value |
| `placeholder` | Displays hint text |
| `required` | Makes a field mandatory |
| `readonly` | Makes a field read-only |
| `disabled` | Disables an input |
| `action` | Specifies where form data is sent |
| `method` | Specifies GET or POST request |
| `autocomplete` | Enables or disables browser suggestions |
| `target` | Specifies where to display the response |