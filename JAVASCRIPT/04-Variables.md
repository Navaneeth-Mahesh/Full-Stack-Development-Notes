# Variables in JavaScript

Variables are one of the most fundamental concepts in programming. A variable acts as a **named container** that stores data in memory. Instead of using values directly throughout your program, you store them in variables and use their names whenever needed.

Think of a variable as a labeled box:

```text
Variable Name
     │
     ▼
┌───────────────┐
│   "Navaneeth" │
└───────────────┘
```

Whenever you need the value, you simply use the variable's name.

---

# What is a Variable?

A **variable** is a named memory location used to store data that can be accessed and manipulated throughout a program.

Variables can store different types of values, such as:

* Numbers
* Strings
* Booleans
* Arrays
* Objects
* Functions
* Null
* Undefined

---

## Example

```javascript
let name = "Navaneeth";
let age = 19;
let isStudent = true;

console.log(name);
console.log(age);
console.log(isStudent);
```

Output

```text
Navaneeth
19
true
```

---

# Why Do We Need Variables?

Without variables, we would have to write the same values repeatedly.

### Without Variables

```javascript
console.log("Navaneeth");
console.log("Navaneeth");
console.log("Navaneeth");
```

---

### With Variables

```javascript
let name = "Navaneeth";

console.log(name);
console.log(name);
console.log(name);
```

If the value changes, you only need to update it once.

---

# var

`var` is the original way of declaring variables in JavaScript.

It was introduced in the first version of JavaScript (1995).

Today, `var` is rarely used in modern JavaScript because it has several confusing behaviors.

---

## Syntax

```javascript
var variableName = value;
```

---

## Example

```javascript
var name = "Navaneeth";

console.log(name);
```

Output

```text
Navaneeth
```

---

## Reassigning a var Variable

```javascript
var city = "Hyderabad";

city = "Bangalore";

console.log(city);
```

Output

```text
Bangalore
```

---

## Redeclaring a var Variable

```javascript
var age = 18;

var age = 19;

console.log(age);
```

Output

```text
19
```

`var` allows both **reassignment** and **redeclaration**.

---

## Problems with var

```javascript
var language = "JavaScript";

if (true) {
    var language = "Python";
}

console.log(language);
```

Output

```text
Python
```

The value changed outside the block because `var` is **function-scoped**, not block-scoped.

---

## When to Use var

In modern JavaScript, avoid using `var` unless you're maintaining older codebases.

---

# let

`let` was introduced in **ES6 (ECMAScript 2015)**.

It is the recommended way to declare variables whose values may change.

---

## Syntax

```javascript
let variableName = value;
```

---

## Example

```javascript
let name = "Navaneeth";

console.log(name);
```

---

## Reassigning

```javascript
let age = 19;

age = 20;

console.log(age);
```

Output

```text
20
```

---

## Redeclaring

```javascript
let age = 19;

let age = 20;
```

Output

```text
SyntaxError
```

A `let` variable **cannot** be redeclared in the same scope.

---

## Block Scope

```javascript
let city = "Hyderabad";

if (true) {
    let city = "Delhi";
    console.log(city);
}

console.log(city);
```

Output

```text
Delhi
Hyderabad
```

Each block has its own `city` variable.

---

# const

`const` was also introduced in **ES6**.

It is used to declare variables whose **binding should not change** after initialization.

---

## Syntax

```javascript
const variableName = value;
```

---

## Example

```javascript
const country = "India";

console.log(country);
```

---

## Reassignment

```javascript
const country = "India";

country = "USA";
```

Output

```text
TypeError: Assignment to constant variable.
```

---

## Declaration Without Initialization

```javascript
const PI;
```

Output

```text
SyntaxError: Missing initializer in const declaration
```

`const` must always be initialized when declared.

---

## Objects with const

Many beginners think `const` makes an object completely immutable.

That's not true.

```javascript
const student = {
    name: "Navaneeth"
};

student.name = "Rahul";

console.log(student);
```

Output

```javascript
{
    name: "Rahul"
}
```

You **can modify the contents** of an object or array declared with `const`, but you **cannot reassign** the variable itself.

---

## Reassignment Example

```javascript
const student = {
    name: "Navaneeth"
};

student = {};
```

Output

```text
TypeError
```

---

# var vs let vs const

| Feature                     | var               | let      | const    |
| --------------------------- | ----------------- | -------- | -------- |
| Scope                       | Function          | Block    | Block    |
| Redeclaration               | Yes               | No       | No       |
| Reassignment                | Yes               | Yes      | No       |
| Hoisted                     | Yes               | Yes      | Yes      |
| Initialized During Hoisting | Yes (`undefined`) | No (TDZ) | No (TDZ) |
| Modern Usage                | Rare              | Yes      | Yes      |

---

## Which One Should You Use?

* Use **`const`** by default.
* Use **`let`** when the variable's value needs to change.
* Avoid **`var`** in modern JavaScript.

---

# Variable Declaration

Variable declaration means **creating a variable**.

---

## Syntax

```javascript
let name;
```

Here:

* `let` → keyword
* `name` → variable name

At this point, the variable exists but has no assigned value.

---

## Example

```javascript
let age;

console.log(age);
```

Output

```text
undefined
```

---

# Variable Initialization

Initialization means **assigning a value** to a variable.

---

## Example

```javascript
let age = 19;
```

Here:

* Variable Declaration → `let age`
* Variable Initialization → `= 19`

---

## Separate Declaration and Initialization

```javascript
let city;

city = "Hyderabad";

console.log(city);
```

Output

```text
Hyderabad
```

---

## Multiple Variables

```javascript
let firstName = "Navaneeth";
let lastName = "Kumar";
let age = 19;
```

---

# Variable Naming Rules

Variable names must follow specific rules.

---

## 1. Can Contain

* Letters
* Numbers
* Underscore (`_`)
* Dollar sign (`$`)

```javascript
let username;
let user1;
let _price;
let $total;
```

---

## 2. Cannot Start with a Number

Incorrect

```javascript
let 1name = "John";
```

Correct

```javascript
let name1 = "John";
```

---

## 3. No Spaces

Incorrect

```javascript
let first name = "John";
```

Correct

```javascript
let firstName = "John";
```

---

## 4. Cannot Use Keywords

Incorrect

```javascript
let return = 5;
```

Correct

```javascript
let result = 5;
```

---

## 5. Case Sensitive

```javascript
let name = "John";
let Name = "David";
```

These are two different variables.

---

## Good Variable Names

```javascript
let studentName;
let totalMarks;
let userAge;
let isLoggedIn;
```

---

## Bad Variable Names

```javascript
let x;
let y;
let abc;
let data1;
```

Choose meaningful names that describe the stored value.

---

# Variable Scope

**Scope** determines where a variable can be accessed.

JavaScript has three main types of scope.

---

# Global Scope

A variable declared outside all functions and blocks has **global scope**.

```javascript
let country = "India";

function showCountry() {
    console.log(country);
}

showCountry();

console.log(country);
```

Output

```text
India
India
```

The variable is accessible everywhere in the program.

---

# Function Scope

Variables declared with `var` inside a function are accessible only within that function.

```javascript
function display() {
    var message = "Hello";
    console.log(message);
}

display();

console.log(message);
```

Output

```text
ReferenceError: message is not defined
```

---

# Block Scope

Variables declared with `let` and `const` inside a block are only available within that block.

```javascript
if (true) {
    let age = 19;
    console.log(age);
}

console.log(age);
```

Output

```text
ReferenceError
```

---

## Scope Comparison

```javascript
var x = 1;
let y = 2;
const z = 3;

if (true) {
    var x = 10;
    let y = 20;
    const z = 30;

    console.log(x, y, z);
}

console.log(x, y, z);
```

Output

```text
10 20 30
10 2 3
```

Notice that:

* `var` changes the original variable.
* `let` creates a new block-scoped variable.
* `const` also creates a new block-scoped variable.

---

# Hoisting

**Hoisting** is JavaScript's behavior of moving declarations to the top of their scope before code execution.

Only the **declarations** are hoisted—not the initializations.

---

## Hoisting with var

```javascript
console.log(age);

var age = 19;
```

JavaScript internally treats it like this:

```javascript
var age;

console.log(age);

age = 19;
```

Output

```text
undefined
```

---

## Hoisting with let

```javascript
console.log(age);

let age = 19;
```

Output

```text
ReferenceError:
Cannot access 'age' before initialization
```

Although `let` is hoisted, it remains in the **Temporal Dead Zone (TDZ)** until its declaration is executed.

---

## Hoisting with const

```javascript
console.log(PI);

const PI = 3.14;
```

Output

```text
ReferenceError:
Cannot access 'PI' before initialization
```

Like `let`, `const` is hoisted but stays in the **Temporal Dead Zone** until initialized.

---

# Temporal Dead Zone (TDZ)

The **Temporal Dead Zone (TDZ)** is the period between entering a scope and executing the declaration of a `let` or `const` variable.

During this time, accessing the variable results in a `ReferenceError`.

```javascript
{
    // TDZ starts

    console.log(name); // ReferenceError

    let name = "Navaneeth";

    console.log(name);

    // TDZ ends
}
```

Output

```text
ReferenceError
Navaneeth
```

---

# Best Practices

* Use **`const`** by default.
* Use **`let`** only when reassignment is required.
* Avoid using **`var`** in new projects.
* Always initialize variables before using them.
* Use meaningful variable names.
* Declare variables as close as possible to where they are used.
* Prefer block scope (`let` and `const`) over function scope (`var`).

---

# Summary

In this chapter, you learned:

* **Variables** are named containers used to store data.
* **`var`** is function-scoped, allows redeclaration, and is mainly used in legacy code.
* **`let`** is block-scoped, allows reassignment, but does not allow redeclaration.
* **`const`** is block-scoped, must be initialized during declaration, and cannot be reassigned.
* **Variable declaration** creates a variable, while **initialization** assigns it a value.
* **Variable naming rules** ensure valid and meaningful variable names.
* **Variable scope** determines where a variable can be accessed (global, function, and block scope).
* **Hoisting** moves declarations before execution, while `let` and `const` remain in the **Temporal Dead Zone (TDZ)** until their declarations are reached.

Understanding variables thoroughly is essential because they are used in almost every JavaScript program, from simple scripts to large-scale web applications.
