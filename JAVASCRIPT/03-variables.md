# Variables in JavaScript

# What is a Variable?

A **variable** is a container that stores data.

Think of a variable as a **box** with a name. You can store information inside the box and use it later.

Example:

```
Name Box → Navaneeth
Age Box → 19
```

In JavaScript:

```javascript
let name = "Navaneeth";
let age = 19;
```

---

# Why Do We Need Variables?

Variables help us store information that can be used or changed later.

Examples:
- User name
- Age
- Score
- Price
- Email
- Marks

Without variables, you would have to write the same value again and again.

---

# Creating a Variable

There are **three ways** to create variables in JavaScript:

```javascript
let name = "John";
const country = "India";
var age = 20;
```

Each keyword works differently.

---

# 1. let

`let` is used for values that **can change** later.

Example:

```javascript
let city = "Hyderabad";

city = "Visakhapatnam";

console.log(city);
```

Output:

```
Visakhapatnam
```

Since the value changed, `let` is the correct choice.

---

# 2. const

`const` is used for values that **should never change**.

Example:

```javascript
const pi = 3.14159;

console.log(pi);
```

Output:

```
3.14159
```

Trying to change it will cause an error.

Example:

```javascript
const pi = 3.14159;

pi = 3.14; // Error
```

---

# 3. var

`var` is the old way of declaring variables.

Example:

```javascript
var language = "JavaScript";

console.log(language);
```

Although `var` still works, modern JavaScript mostly uses **let** and **const**.

---

# Which One Should You Use?

| Keyword   | Can Change?   | Recommended? |
|---------- |-------------  |--------------|
| `let`     |  Yes          |  Yes         |
| `const`   | No            |  Yes         |
| `var`     |  Yes          |  Mostly No   |

**Rule:**
- Use `const` by default.
- Use `let` if the value needs to change.
- Avoid `var` in modern JavaScript.

---

# Variable Naming Rules

 Variable names can:

- Start with a letter
- Start with `_`
- Start with `$`
- Contain numbers (after the first character)

Examples:

```javascript
let name;
let age18;
let _price;
let $salary;
```

---

# Invalid Variable Names

These are **not allowed**:

```javascript
let 123name;
let first-name;
let let;
```

Why?

- Cannot start with a number.
- Hyphen (`-`) is treated as the subtraction operator.
- Reserved keywords cannot be used as variable names.

---

# JavaScript is Case-Sensitive

These are different variables:

```javascript
let name = "John";
let Name = "David";
let NAME = "Alex";
```

All three variables are different.

---

# Good Variable Names

Choose names that clearly describe the data.

Good:

```javascript
let firstName;
let totalPrice;
let studentAge;
let isLoggedIn;
```

Bad:

```javascript
let x;
let abc;
let temp123;
```

Meaningful names make your code easier to read.

---

# Multiple Variables

You can declare multiple variables.

```javascript
let firstName = "John";
let lastName = "Doe";
let age = 20;
```

Or in one line:

```javascript
let firstName = "John",
    lastName = "Doe",
    age = 20;
```

---

# Changing Variable Values

Variables created with `let` can be updated.

```javascript
let score = 50;

score = 80;

console.log(score);
```

Output:

```
80
```

---

# Using Variables

Variables can be printed using `console.log()`.

```javascript
let name = "Navaneeth";

console.log(name);
```

Output:

```
Navaneeth
```

You can also print multiple values.

```javascript
let name = "Navaneeth";
let age = 18;

console.log(name, age);
```

Output:

```
Navaneeth 18
```

---

# Real-Life Example

```javascript
const website = "Google";
let visitors = 100;

visitors = 120;

console.log(website);
console.log(visitors);
```

Output:

```
Google
120
```

The website name never changes, so we use `const`.

The number of visitors changes, so we use `let`.

---

# Common Mistakes

### Forgetting Quotes for Strings

***** Wrong *****

```javascript
let name = Navaneeth;
```

***** Correct *****

```javascript
let name = "Navaneeth";
```

---

### Reassigning a `const`

***** Wrong *****

```javascript
const age = 18;

age = 19;
```

This causes an error.

---

### Using Meaningless Names

Wrong

```javascript
let a = 100;
```

Correct

```javascript
let totalMarks = 100;
```

---

# Best Practices

- Use `const` whenever possible.
- Use `let` only when the value needs to change.
- Avoid using `var` in modern JavaScript.
- Give variables meaningful names.
- Use camelCase for variable names.

Example:

```javascript
let firstName = "John";
let totalMarks = 450;
let isStudent = true;
```

---

# Summary

Variables are used to store data in JavaScript. The three keywords used to declare variables are `let`, `const`, and `var`. In modern JavaScript, `const` and `let` are preferred, while `var` is rarely used.

---

## Key Points

- Variables store data.
- `let` allows the value to change.
- `const` creates a constant value.
- `var` is the older way of declaring variables.
- JavaScript is case-sensitive.
- Use meaningful variable names.
- Prefer `const` first, then `let` if needed.