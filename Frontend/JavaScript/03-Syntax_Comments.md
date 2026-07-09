# JavaScript Syntax

JavaScript syntax is the set of rules that defines how JavaScript programs are written and interpreted. Just as every spoken language has grammar rules, JavaScript has syntax rules that determine how code should be written.

Understanding JavaScript syntax is essential because even a small syntax mistake can cause your program to produce errors or fail to run.

---

# What is JavaScript Syntax?

**Syntax** refers to the rules for writing valid JavaScript code.

JavaScript syntax defines:

* How variables are declared
* How functions are written
* How statements are structured
* How operators are used
* How blocks of code are organized

A program that follows JavaScript syntax rules is called **syntactically correct**.

---

## Example

```javascript
let name = "Navaneeth";
console.log(name);
```

This code follows JavaScript syntax correctly.

---

## Incorrect Example

```javascript
let = "Navaneeth";
```

Output:

```text
SyntaxError: Unexpected token '='
```

This code is invalid because `let` is a keyword and cannot be used as a variable name.

---

# Statements

A **statement** is a complete instruction that tells JavaScript to perform an action.

A JavaScript program is made up of one or more statements.

---

## Example

```javascript
let name = "Navaneeth";
let age = 19;

console.log(name);
console.log(age);
```

Each line above is a separate statement.

---

## Types of Statements

### Variable Declaration

```javascript
let city = "Hyderabad";
```

---

### Assignment Statement

```javascript
city = "Bangalore";
```

---

### Function Call Statement

```javascript
console.log("Hello World");
```

---

### Conditional Statement

```javascript
if (age >= 18) {
    console.log("Eligible");
}
```

---

### Loop Statement

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

---

# Expressions

An **expression** is a piece of code that produces or evaluates to a value.

Unlike statements, expressions always return a result.

---

## Example 1

```javascript
10 + 20
```

Result:

```text
30
```

---

## Example 2

```javascript
5 * 8
```

Result:

```text
40
```

---

## Example 3

```javascript
let result = 10 + 5;
```

The expression is:

```javascript
10 + 5
```

Its value is:

```text
15
```

---

## Types of Expressions

### Arithmetic Expression

```javascript
10 + 5
```

---

### String Expression

```javascript
"Hello" + " World"
```

Output:

```text
Hello World
```

---

### Comparison Expression

```javascript
20 > 10
```

Output:

```text
true
```

---

### Logical Expression

```javascript
true && false
```

Output:

```text
false
```

---

### Function Expression

```javascript
const greet = function () {
    console.log("Hello");
};
```

---

## Statement vs Expression

| Statement                     | Expression                  |
| ----------------------------- | --------------------------- |
| Performs an action            | Produces a value            |
| May not return a value        | Always evaluates to a value |
| Example: `if`, `for`, `while` | Example: `10 + 5`, `"Hi"`   |

---

# Semicolons

A **semicolon (`;`)** marks the end of a JavaScript statement.

Although JavaScript can automatically insert semicolons in many cases, it is considered a good practice to write them explicitly for better readability and to avoid unexpected behavior.

---

## Example

```javascript
let name = "Navaneeth";
let age = 19;

console.log(name);
console.log(age);
```

---

## Automatic Semicolon Insertion (ASI)

JavaScript has a feature called **Automatic Semicolon Insertion (ASI)**, which inserts semicolons automatically when possible.

Example:

```javascript
let x = 10
let y = 20

console.log(x + y)
```

This code works because JavaScript inserts semicolons automatically.

---

## A Problem with ASI

```javascript
function getNumber() {
    return
    100;
}

console.log(getNumber());
```

Output:

```text
undefined
```

JavaScript inserts a semicolon after `return`, making the code behave like this:

```javascript
return;
100;
```

Correct version:

```javascript
function getNumber() {
    return 100;
}
```

---

## Best Practice

Always write semicolons consistently, especially in beginner projects and team environments.

---

# Comments

Comments are notes written inside the code that JavaScript ignores during execution.

They help explain code, improve readability, and make maintenance easier.

---

## Single-Line Comment

Use `//`.

```javascript
// This is a comment

let age = 19;
```

---

## Multi-Line Comment

Use `/* ... */`.

```javascript
/*
This is a
multi-line comment.
*/

console.log("Hello");
```

---

## Why Use Comments?

* Explain complex logic
* Improve readability
* Temporarily disable code
* Leave notes for other developers

---

## Example

```javascript
// Store the user's name
let username = "Navaneeth";

// Display the username
console.log(username);
```

---

# Code Formatting

**Code formatting** means organizing your code so it is clean, readable, and easy to maintain.

Good formatting does not change how the program works, but it makes the code easier for humans to understand.

---

## Good Formatting

```javascript
function greet(name) {
    console.log("Hello " + name);
}

greet("Navaneeth");
```

---

## Poor Formatting

```javascript
function greet(name){console.log("Hello "+name);}greet("Navaneeth");
```

Both examples produce the same output, but the first is much easier to read.

---

## Formatting Best Practices

* Use consistent indentation (2 or 4 spaces).
* Add spaces around operators.
* Write one statement per line.
* Use meaningful variable names.
* Keep related code together.
* Leave blank lines between logical sections of code.

---

## Example

```javascript
let firstName = "Navaneeth";
let lastName = "Kumar";

let fullName = firstName + " " + lastName;

console.log(fullName);
```

---

# Identifiers

An **identifier** is the name given to variables, functions, classes, objects, and other programming elements.

---

## Examples

```javascript
let age = 19;

function greet() {}

const studentName = "Navaneeth";
```

Identifiers here are:

* `age`
* `greet`
* `studentName`

---

## Rules for Identifiers

### 1. Can contain

* Letters (`A-Z`, `a-z`)
* Digits (`0-9`)
* Underscore (`_`)
* Dollar sign (`$`)

Example:

```javascript
let userName;
let user_name;
let $price;
```

---

### 2. Cannot start with a number

Incorrect:

```javascript
let 1age = 19;
```

Correct:

```javascript
let age1 = 19;
```

---

### 3. Cannot contain spaces

Incorrect:

```javascript
let first name = "John";
```

Correct:

```javascript
let firstName = "John";
```

---

### 4. Cannot use JavaScript keywords

Incorrect:

```javascript
let class = "B.Tech";
```

Correct:

```javascript
let course = "B.Tech";
```

---

### 5. JavaScript is Case-Sensitive

```javascript
let name = "Navaneeth";
let Name = "Rahul";
```

These are two different identifiers.

---

# Keywords

**Keywords** are reserved words in JavaScript that have predefined meanings.

They cannot be used as identifiers.

---

## Examples of JavaScript Keywords

| Keyword      | Purpose                             |
| ------------ | ----------------------------------- |
| `let`        | Declare a block-scoped variable     |
| `const`      | Declare a constant variable         |
| `var`        | Declare a function-scoped variable  |
| `if`         | Conditional statement               |
| `else`       | Alternative condition               |
| `switch`     | Multiple conditions                 |
| `case`       | A branch inside `switch`            |
| `default`    | Default branch in `switch`          |
| `for`        | Loop                                |
| `while`      | Loop                                |
| `do`         | Do-while loop                       |
| `break`      | Exit a loop or switch               |
| `continue`   | Skip to the next loop iteration     |
| `function`   | Declare a function                  |
| `return`     | Return a value from a function      |
| `class`      | Define a class                      |
| `extends`    | Inherit from another class          |
| `new`        | Create an object                    |
| `this`       | Reference the current object        |
| `super`      | Access the parent class             |
| `try`        | Start exception handling            |
| `catch`      | Handle exceptions                   |
| `finally`    | Always executes after `try`/`catch` |
| `throw`      | Throw an exception                  |
| `import`     | Import modules                      |
| `export`     | Export modules                      |
| `await`      | Wait for a promise                  |
| `async`      | Declare an asynchronous function    |
| `typeof`     | Get the data type of a value        |
| `delete`     | Remove an object property           |
| `instanceof` | Check an object's prototype         |

---

## Invalid Example

```javascript
let return = 10;
```

Output:

```text
SyntaxError
```

---

# Naming Conventions

A **naming convention** is a set of recommended practices for naming identifiers.

Following naming conventions makes code easier to read and maintain.

---

## 1. Use Meaningful Names

Bad:

```javascript
let x = "Navaneeth";
```

Good:

```javascript
let studentName = "Navaneeth";
```

---

## 2. Use camelCase (Recommended)

JavaScript commonly uses **camelCase** for variables and functions.

```javascript
let firstName;
let studentAge;
let totalMarks;

function calculateTotal() {}
```

---

## 3. Use PascalCase for Classes

```javascript
class StudentProfile {}

class BankAccount {}
```

---

## 4. Use UPPER_SNAKE_CASE for Constants

```javascript
const MAX_USERS = 100;
const PI = 3.14159;
```

---

## 5. Use Verb Names for Functions

Functions usually perform actions, so use verbs.

```javascript
function calculateTotal() {}

function sendEmail() {}

function getUser() {}

function printReport() {}
```

---

## 6. Use Boolean Prefixes

Boolean variables often start with words like `is`, `has`, `can`, or `should`.

```javascript
let isLoggedIn = true;
let hasPermission = false;
let canEdit = true;
let shouldSave = false;
```

---

## 7. Avoid Abbreviations

Bad:

```javascript
let stdNm;
```

Good:

```javascript
let studentName;
```

---

## 8. Be Consistent

Choose a naming style and use it consistently throughout your project.

---

# Common Beginner Mistakes

```javascript
// Starts with a number ❌
let 2name = "John";

// Contains spaces ❌
let first name = "John";

// Uses a keyword ❌
let class = "B.Tech";

// Good examples ✅
let firstName = "John";
const MAX_SIZE = 100;
class StudentProfile {}
```

---

# Summary

In this chapter, you learned the fundamental syntax rules of JavaScript, including:

* **Statements** – Instructions that perform actions.
* **Expressions** – Pieces of code that evaluate to a value.
* **Semicolons** – Used to mark the end of statements and avoid issues with Automatic Semicolon Insertion (ASI).
* **Comments** – Notes that improve code readability and are ignored during execution.
* **Code Formatting** – Best practices for writing clean and maintainable code.
* **Identifiers** – Valid names for variables, functions, classes, and other program elements.
* **Keywords** – Reserved words with predefined meanings that cannot be used as identifiers.
* **Naming Conventions** – Recommended naming styles such as `camelCase`, `PascalCase`, and `UPPER_SNAKE_CASE` to write professional, readable JavaScript code.

Mastering these syntax rules will make your code easier to read, debug, and maintain, forming a strong foundation for learning more advanced JavaScript concepts.
