# HTML Character Entities

HTML character entities are special codes used to display reserved characters and symbols that cannot be typed directly in HTML or may have a special meaning.

For example, the `<` and `>` characters are used to define HTML tags. If you want to display them as plain text, you must use character entities.

---

# Why Use Character Entities?

Character entities are useful for:

- Displaying reserved HTML characters like `<`, `>`, and `&`.
- Showing symbols that are not available on the keyboard.
- Adding special characters such as currency symbols and copyright signs.
- Preventing the browser from interpreting reserved characters as HTML code.

---

# Syntax

Character entities can be written in two ways:

### Using Entity Name

```html
&entityName;
```

### Using Entity Number

```html
&#entityNumber;
```

Both produce the same output.

---

# Common HTML Character Entities

| Character | Description | Entity Name | Entity Number |
|-----------|-------------|-------------|---------------|
| Space (non-breaking) | Prevents automatic line breaks | `&nbsp;` | `&#160;` |
| `<` | Less than | `&lt;` | `&#60;` |
| `>` | Greater than | `&gt;` | `&#62;` |
| `&` | Ampersand | `&amp;` | `&#38;` |
| `"` | Double quotation mark | `&quot;` | `&#34;` |
| `'` | Single quotation mark | `&apos;` | `&#39;` |
| ¢ | Cent | `&cent;` | `&#162;` |
| £ | Pound | `&pound;` | `&#163;` |
| ¥ | Yen | `&yen;` | `&#165;` |
| € | Euro | `&euro;` | `&#8364;` |
| © | Copyright | `&copy;` | `&#169;` |
| ® | Registered Trademark | `&reg;` | `&#174;` |
| ™ | Trademark | `&trade;` | `&#8482;` |

---

# Examples

## Display Reserved Characters

```html
<p>&lt;h1&gt;Hello World&lt;/h1&gt;</p>
```

**Output:**

```text
<h1>Hello World</h1>
```

---

## Display an Ampersand

```html
<p>HTML &amp; CSS</p>
```

**Output:**

```text
HTML & CSS
```

---

## Non-Breaking Space

```html
<p>Navaneeth&nbsp;&nbsp;&nbsp;Mahesh</p>
```

Unlike normal spaces, a non-breaking space (`&nbsp;`) prevents the browser from collapsing multiple spaces into one.

---

## Currency Symbols

```html
<p>Price: &dollar;100</p>
<p>Price: &euro;80</p>
<p>Price: &pound;70</p>
<p>Price: &yen;5000</p>
```

---

## Copyright and Trademark

```html
<p>&copy; 2026 My Website</p>

<p>OpenAI&trade;</p>

<p>Microsoft&reg;</p>
```

---

# Best Practices

- Use character entities when displaying reserved HTML characters.
- Prefer entity names (such as `&copy;`) because they are easier to read.
- Use `&nbsp;` only when necessary to prevent unwanted line breaks.
- Avoid using multiple `&nbsp;` characters for layout or spacing; use CSS instead.

---

# Summary

- HTML character entities display reserved characters and special symbols.
- Entities can be written using a **name** or a **number**.
- Reserved characters like `<`, `>`, and `&` should always be written using character entities when displayed as text.
- Common entities include `&copy;`, `&reg;`, `&trade;`, `&nbsp;`, and various currency symbols.