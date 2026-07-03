# HTML Character Entities (Clean Beginner Notes)

HTML character entities are special codes used to display **reserved characters and symbols** that HTML normally cannot show directly.

---

# Why Character Entities Are Needed

Some characters have special meaning in HTML:

* `<` and `>` → used for tags
* `&` → used for entities

So if you want to display them as text, you must use entities.

---

# What Are Character Entities?

Character entities let you show:

* Reserved HTML symbols
* Special characters
* Currency symbols
* Copyright and trademark symbols
* Extra spacing (non-breaking space)

---

# Syntax

## 1. Entity Name (Recommended)

```html id="entity-name"
&entityName;
```

## 2. Entity Number

```html id="entity-number"
&#entityNumber;
```

Both produce the same result.

---

# Common HTML Character Entities

| Character | Meaning            | Entity Name | Entity Number |
| --------- | ------------------ | ----------- | ------------- |
| space     | non-breaking space | `&nbsp;`    | `&#160;`      |
| `<`       | less than          | `&lt;`      | `&#60;`       |
| `>`       | greater than       | `&gt;`      | `&#62;`       |
| `&`       | ampersand          | `&amp;`     | `&#38;`       |
| `"`       | double quote       | `&quot;`    | `&#34;`       |
| `'`       | single quote       | `&apos;`    | `&#39;`       |
| ©         | copyright          | `&copy;`    | `&#169;`      |
| ®         | registered         | `&reg;`     | `&#174;`      |
| ™         | trademark          | `&trade;`   | `&#8482;`     |
| €         | euro               | `&euro;`    | `&#8364;`     |
| £         | pound              | `&pound;`   | `&#163;`      |
| ¥         | yen                | `&yen;`     | `&#165;`      |
| ¢         | cent               | `&cent;`    | `&#162;`      |

---

# 1. Display HTML Tags as Text

If you write:

```html id="bad"
<h1>Hello</h1>
```

Browser will treat it as a real heading.

---

## Correct way:

```html id="good"
<p>&lt;h1&gt;Hello&lt;/h1&gt;</p>
```

### Output:

```text id="output-tag"
<h1>Hello</h1>
```

---

# 2. Display Ampersand (&)

```html id="amp"
<p>HTML &amp; CSS</p>
```

### Output:

HTML & CSS

---

# 3. Non-Breaking Space (`&nbsp;`)

Used to prevent line breaks or collapse of spaces.

```html id="nbsp"
<p>Navaneeth&nbsp;&nbsp;&nbsp;Mahesh</p>
```

### Difference:

| Normal space                | Non-breaking space |
| --------------------------- | ------------------ |
| Collapses into single space | Keeps spacing      |
| Can break line              | Prevents break     |

---

# 4. Currency Symbols

```html id="currency"
<p>Price: &dollar;100</p>
<p>Price: &euro;80</p>
<p>Price: &pound;70</p>
<p>Price: &yen;5000</p>
```

---

# 5. Copyright and Trademark

```html id="legal"
<p>&copy; 2026 My Website</p>
<p>OpenAI&trade;</p>
<p>Microsoft&reg;</p>
```

---

# Real Use Cases

* Writing code examples
* Documentation websites
* Blogs about programming
* UI text formatting
* Preventing HTML parsing errors

---

# Best Practices

✔ Use entity names instead of numbers (easier to read)
✔ Use `&lt;` and `&gt;` when showing HTML code
✔ Use `&nbsp;` only when necessary
❌ Don’t use `&nbsp;` for layout (use CSS instead)
✔ Always escape `&`, `<`, `>` in text

---

# Common Mistake

❌ Wrong:

```html
<p>5 < 10</p>
```

✔ Correct:

```html
<p>5 &lt; 10</p>
```

---

# Summary

* Character entities display reserved symbols safely
* They prevent HTML from misinterpreting special characters
* Two types: entity name (`&copy;`) and number (`&#169;`)
* Most important entities: `&lt;`, `&gt;`, `&amp;`, `&nbsp;`
* Always use them when showing HTML code or special symbols

---

# Final Idea

> Character entities are the “escape system” of HTML — they let you safely display characters that normally have special meaning.

---

