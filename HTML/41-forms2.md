# HTML Input Types and Attributes

HTML forms collect information from users. The `<input>` element is the most commonly used form element, and its behavior changes depending on the `type` attribute.

---

# Input Types

The `type` attribute tells the browser what kind of input field to display.

## Text

Used to enter a single line of text.

```html
<input type="text">
```

Example:

```html
<input type="text" placeholder="Enter your name">
```

---

## Password

Hides the entered characters.

```html
<input type="password">
```

---

## Email

Accepts email addresses and performs basic validation.

```html
<input type="email">
```

---

## Number

Accepts only numeric values.

```html
<input type="number">
```

---

## Tel

Used for entering phone numbers.

```html
<input type="tel">
```

---

## URL

Accepts website addresses.

```html
<input type="url">
```

---

## Search

Used for search boxes.

```html
<input type="search">
```

---

## Date

Lets the user choose a date.

```html
<input type="date">
```

---

## Time

Allows the user to select a time.

```html
<input type="time">
```

---

## Month

Allows selecting a month and year.

```html
<input type="month">
```

---

## Week

Allows selecting a week.

```html
<input type="week">
```

---

## Date & Time

Lets the user choose both date and time.

```html
<input type="datetime-local">
```

---

## Color

Displays a color picker.

```html
<input type="color">
```

---

## Range

Creates a slider.

```html
<input type="range">
```

---

## Checkbox

Allows selecting multiple options.

```html
<input type="checkbox">
```

Example

```html
<input type="checkbox"> HTML

<input type="checkbox"> CSS

<input type="checkbox"> JavaScript
```

---

## Radio

Allows selecting only one option from a group.

```html
<input type="radio">
```

Example

```html
<input type="radio" name="gender"> Male

<input type="radio" name="gender"> Female
```

> Radio buttons must share the same `name` value.

---

## File

Allows users to upload files.

```html
<input type="file">
```

---

## Hidden

Stores data that users cannot see.

```html
<input type="hidden" value="12345">
```

---

## Button

Creates a clickable button.

```html
<input type="button" value="Click Me">
```

---

## Submit

Submits the form.

```html
<input type="submit">
```

---

## Reset

Resets all form fields.

```html
<input type="reset">
```

---

## Image

Uses an image as the submit button.

```html
<input
    type="image"
    src="submit.png"
    alt="Submit">
```

---

# Common Input Attributes

Attributes provide extra functionality to input fields.

---

## value

Sets the default value.

```html
<input type="text" value="Navaneeth">
```

---

## placeholder

Displays a hint inside the input.

```html
<input
    type="text"
    placeholder="Enter your name">
```

---

## required

Makes the field mandatory.

```html
<input
    type="email"
    required>
```

---

## readonly

Allows users to view the value but prevents editing.

```html
<input
    type="text"
    value="Admin"
    readonly>
```

---

## disabled

Disables the input completely.

```html
<input
    type="text"
    disabled>
```

> Disabled fields are not submitted with the form.

---

## maxlength

Limits the number of characters.

```html
<input
    type="text"
    maxlength="20">
```

---

## minlength

Specifies the minimum number of characters.

```html
<input
    type="password"
    minlength="8">
```

---

## size

Changes the visible width of the input.

```html
<input
    type="text"
    size="40">
```

---

## min

Sets the minimum allowed value.

```html
<input
    type="number"
    min="1">
```

---

## max

Sets the maximum allowed value.

```html
<input
    type="number"
    max="100">
```

---

## step

Controls the increment between values.

```html
<input
    type="number"
    step="5">
```

---

## pattern

Uses a regular expression to validate input.

```html
<input
    type="text"
    pattern="[A-Za-z]{3}">
```

---

## multiple

Allows selecting multiple files or email addresses.

```html
<input
    type="file"
    multiple>
```

---

## autofocus

Automatically focuses the input when the page loads.

```html
<input
    type="text"
    autofocus>
```

---

## autocomplete

Enables or disables browser suggestions.

```html
<input
    type="email"
    autocomplete="off">
```

---

## list

Connects an input to a `<datalist>`.

```html
<input list="languages">

<datalist id="languages">
    <option value="HTML">
    <option value="CSS">
    <option value="JavaScript">
</datalist>
```

---

## width & height

Used only with `type="image"`.

```html
<input
    type="image"
    src="submit.png"
    width="80"
    height="40">
```

---

# Complete Example

```html
<form>

    <label>Name</label>
    <input
        type="text"
        placeholder="Enter your name"
        required>

    <br><br>

    <label>Email</label>
    <input
        type="email"
        required>

    <br><br>

    <label>Password</label>
    <input
        type="password"
        minlength="8">

    <br><br>

    <label>Age</label>
    <input
        type="number"
        min="18"
        max="60">

    <br><br>

    <label>Resume</label>
    <input
        type="file">

    <br><br>

    <input type="submit">

    <input type="reset">

</form>
```

---

# Summary

## Common Input Types

| Type | Purpose |
|------|----------|
| `text` | Single-line text |
| `password` | Hidden text |
| `email` | Email address |
| `number` | Numeric input |
| `tel` | Phone number |
| `url` | Website URL |
| `search` | Search box |
| `date` | Date picker |
| `time` | Time picker |
| `datetime-local` | Date and time |
| `month` | Month selector |
| `week` | Week selector |
| `color` | Color picker |
| `range` | Slider |
| `checkbox` | Multiple choices |
| `radio` | Single choice |
| `file` | File upload |
| `hidden` | Hidden value |
| `button` | Button |
| `submit` | Submit form |
| `reset` | Reset form |
| `image` | Image submit button |

## Common Attributes

| Attribute | Purpose |
|-----------|----------|
| `value` | Default value |
| `placeholder` | Hint text |
| `required` | Mandatory field |
| `readonly` | Cannot be edited |
| `disabled` | Completely disabled |
| `maxlength` | Maximum characters |
| `minlength` | Minimum characters |
| `size` | Visible width |
| `min` | Minimum value |
| `max` | Maximum value |
| `step` | Value interval |
| `pattern` | Validation rule |
| `multiple` | Multiple values/files |
| `autofocus` | Focus on page load |
| `autocomplete` | Browser suggestions |
| `list` | Uses a datalist |
| `width` | Image width |
| `height` | Image height |