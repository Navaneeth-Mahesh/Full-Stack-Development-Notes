# 01 — JavaScript Tutorial for Beginners

> A complete beginner-friendly introduction to JavaScript, how it works, where it runs, how to write your first program, and the core concepts you need before continuing.

---

## 1. What is JavaScript?

**JavaScript (JS)** is a programming language used to make applications interactive and dynamic.

It is most commonly associated with web development, but modern JavaScript can also be used for:

* Websites
* Web applications
* Backend servers
* APIs
* Mobile applications
* Desktop applications
* Browser extensions
* Automation
* AI applications
* Full-stack applications

For example, HTML creates the structure:

```html
<h1>Hello</h1>
```

CSS controls the appearance:

```css
h1 {
  color: blue;
}
```

JavaScript controls behavior:

```js
const button = document.querySelector("button");

button.addEventListener("click", () => {
  alert("Button clicked!");
});
```

### Simple idea

Think of a website like a human:

```text
HTML       → Skeleton
CSS        → Appearance
JavaScript → Brain / Behavior
```

---

# 2. Why Learn JavaScript?

JavaScript is one of the most important languages for modern web development.

You can use JavaScript to build:

```text
Frontend
   ↓
React
Next.js
Vue
Angular

Backend
   ↓
Node.js
Express.js
NestJS

Full Stack
   ↓
React + Node.js
Next.js
```

It is also widely used with APIs, databases, authentication, real-time applications, and AI applications.

---

# 3. Where Does JavaScript Run?

JavaScript can run in different environments.

## Browser

Examples:

* Chrome
* Edge
* Firefox
* Safari

Browsers contain a JavaScript engine.

For example:

```text
Chrome
   ↓
V8 Engine
   ↓
JavaScript
```

---

## Node.js

Node.js allows JavaScript to run outside the browser.

Example:

```js
console.log("Hello from Node.js");
```

Run it using:

```bash
node app.js
```

Node.js is commonly used for:

* Backend APIs
* Servers
* CLI applications
* Automation
* File handling
* Database applications

---

# 4. JavaScript Engines

A JavaScript engine reads and executes JavaScript code.

Examples:

| Browser | JavaScript Engine |
| ------- | ----------------- |
| Chrome  | V8                |
| Edge    | V8                |
| Firefox | SpiderMonkey      |
| Safari  | JavaScriptCore    |

For example:

```js
console.log("Hello");
```

The engine processes the code and executes it.

---

# 5. How JavaScript Executes

Consider:

```js
console.log("Hello");

console.log("World");

console.log("JavaScript");
```

Normally, JavaScript executes synchronous code from top to bottom.

Output:

```text
Hello
World
JavaScript
```

Think:

```text
Line 1
   ↓
Line 2
   ↓
Line 3
   ↓
Done
```

Later, when you learn asynchronous JavaScript, you will see how timers, promises, and APIs interact with the event loop.

---

# 6. Your First JavaScript Program

The simplest JavaScript program is:

```js
console.log("Hello, World!");
```

Output:

```text
Hello, World!
```

`console.log()` prints information to the console.

---

# 7. console.log()

`console.log()` is one of the most commonly used tools while learning JavaScript.

```js
console.log("Hello");
```

You can print numbers:

```js
console.log(100);
```

Boolean values:

```js
console.log(true);
```

Multiple values:

```js
console.log("Age:", 20);
```

Expressions:

```js
console.log(10 + 20);
```

Output:

```text
30
```

---

# 8. Comments

Comments are ignored by JavaScript.

They are used to explain code.

## Single-line comment

```js
// This is a comment

console.log("Hello");
```

## Multi-line comment

```js
/*
  This is a
  multi-line comment
*/

console.log("Hello");
```

Comments are useful for:

* Explaining difficult logic
* Leaving notes
* Temporarily disabling code
* Documenting important decisions

Avoid unnecessary comments such as:

```js
// Add 1 to count
count++;
```

The code already explains itself.

---

# 9. JavaScript Statements

A statement is an instruction given to JavaScript.

Example:

```js
const name = "Alex";
```

Another:

```js
console.log(name);
```

Multiple statements:

```js
const name = "Alex";
const age = 20;

console.log(name);
console.log(age);
```

---

# 10. Semicolons

JavaScript allows semicolons to terminate statements.

```js
const name = "Alex";
console.log(name);
```

JavaScript also has **Automatic Semicolon Insertion (ASI)**.

This works:

```js
const name = "Alex"
console.log(name)
```

However, being consistent with semicolons or a well-defined no-semicolon style is important.

For beginners, using semicolons is perfectly fine:

```js
const age = 20;
const name = "Alex";
```

---

# 11. Case Sensitivity

JavaScript is case-sensitive.

These are different:

```js
const name = "Alex";

const Name = "Sam";

const NAME = "John";
```

They represent three different identifiers.

This:

```js
console.log(name);
```

is not the same as:

```js
console.log(Name);
```

---

# 12. Identifiers

An identifier is a name used for something in your program.

Examples:

```js
const name = "Alex";
```

Here:

```text
name → identifier
```

Another example:

```js
function calculateTotal() {}
```

Here:

```text
calculateTotal → identifier
```

Identifiers can be used for:

* Variables
* Functions
* Classes
* Parameters

---

# 13. JavaScript Naming Rules

Valid:

```js
const username = "Alex";

const userName = "Alex";

const user_name = "Alex";

const $price = 100;

const price2 = 200;
```

Invalid:

```js
const 2price = 100;
```

You cannot start an identifier with a number.

Also invalid:

```js
const user-name = "Alex";
```

The `-` is interpreted as a minus operator.

---

# 14. Reserved Keywords

JavaScript has reserved words that cannot normally be used as variable names.

Examples:

```text
let
const
var
function
class
return
if
else
for
while
switch
new
this
import
export
try
catch
throw
```

Don't do:

```js
const class = "JavaScript";
```

Use:

```js
const className = "JavaScript";
```

---

# 15. JavaScript Values

JavaScript works with values.

Examples:

```js
"Hello"
```

```js
100
```

```js
true
```

```js
null
```

```js
undefined
```

Objects:

```js
{
  name: "Alex"
}
```

Arrays:

```js
[10, 20, 30]
```

These values have different types.

---

# 16. JavaScript Data Types

JavaScript has primitive and non-primitive values.

## Primitive types

The main primitive types are:

```text
String
Number
BigInt
Boolean
Undefined
Null
Symbol
```

## Object

Objects are non-primitive/reference values.

Examples:

```js
const name = "Alex";       // String

const age = 20;            // Number

const isStudent = true;    // Boolean

const value = undefined;   // Undefined

const data = null;         // Null

const big = 123n;          // BigInt

const user = {};           // Object

const skills = [];         // Array/Object
```

You will study these types more deeply in later lessons.

---

# 17. Strings

A string represents text.

```js
const name = "Navaneeth";
```

You can use:

```js
const a = "Hello";
const b = 'Hello';
const c = `Hello`;
```

The backtick syntax is called a **template literal**.

Example:

```js
const name = "Alex";

console.log(`Hello ${name}`);
```

Output:

```text
Hello Alex
```

---

# 18. Numbers

JavaScript uses the `Number` type for most numeric values.

```js
const age = 20;
const price = 99.99;
const temperature = -5;
```

You can perform calculations:

```js
console.log(10 + 20);
```

Output:

```text
30
```

---

# 19. Boolean

A boolean has two possible values:

```js
true
false
```

Example:

```js
const isLoggedIn = true;
const isAdmin = false;
```

Booleans are extremely important for conditions.

```js
if (isLoggedIn) {
  console.log("Welcome!");
}
```

---

# 20. Undefined

`undefined` usually means a value has not been assigned.

```js
let username;

console.log(username);
```

Output:

```text
undefined
```

---

# 21. Null

`null` represents an intentional absence of a value.

```js
const selectedUser = null;
```

This means:

```text
There is currently no selected user.
```

A common distinction:

```text
undefined → value hasn't been assigned / isn't available
null      → intentionally empty
```

---

# 22. Objects

Objects store related data using key-value pairs.

```js
const user = {
  name: "Alex",
  age: 20,
  city: "Hyderabad"
};
```

Access values:

```js
console.log(user.name);
```

Output:

```text
Alex
```

Objects become extremely important when working with APIs, React, Node.js, and databases.

---

# 23. Arrays

Arrays store ordered collections.

```js
const fruits = [
  "Apple",
  "Banana",
  "Mango"
];
```

Access an element:

```js
console.log(fruits[0]);
```

Output:

```text
Apple
```

Array indexes start from `0`.

```text
Index       Value

0           Apple
1           Banana
2           Mango
```

---

# 24. typeof Operator

`typeof` tells you the type of a value.

```js
console.log(typeof "Hello");
```

Output:

```text
string
```

Examples:

```js
console.log(typeof 100);
// number

console.log(typeof true);
// boolean

console.log(typeof undefined);
// undefined

console.log(typeof {});
// object

console.log(typeof []);
// object
```

Important JavaScript quirk:

```js
typeof null
```

returns:

```text
"object"
```

This is a historical JavaScript behavior.

---

# 25. Expressions

An expression produces a value.

Example:

```js
10 + 20
```

produces:

```text
30
```

Another:

```js
age >= 18
```

produces:

```text
true
```

Another:

```js
"Hello " + "World"
```

produces:

```text
Hello World
```

---

# 26. Operators

Operators perform operations.

Examples:

```js
+
-
*
/
%
```

Comparison:

```js
>
<
>=
<=
===
!==
```

Logical:

```js
&&
||
!
```

Assignment:

```js
=
+=
-=
*=
/=
```

You will study these in detail in later lessons.

---

# 27. Basic Example

Let's combine several concepts.

```js
const name = "Navaneeth";
const age = 20;
const isStudent = true;

console.log("Name:", name);
console.log("Age:", age);
console.log("Student:", isStudent);
```

Output:

```text
Name: Navaneeth
Age: 20
Student: true
```

---

# 28. Template Literals

Template literals use backticks:

```js
const name = "Alex";
const age = 20;

console.log(`My name is ${name} and I am ${age} years old.`);
```

Output:

```text
My name is Alex and I am 20 years old.
```

You can also perform expressions:

```js
const a = 10;
const b = 20;

console.log(`Total: ${a + b}`);
```

Output:

```text
Total: 30
```

Template literals are heavily used in modern JavaScript.

---

# 29. Basic Input and Output

Output:

```js
console.log("Hello");
```

Browser input:

```js
const name = prompt("Enter your name:");

console.log(`Hello ${name}`);
```

Example:

```text
Enter your name: Navaneeth

Hello Navaneeth
```

`prompt()` returns text, so numeric input usually needs conversion:

```js
const age = Number(prompt("Enter your age:"));

console.log(age + 1);
```

---

# 30. A Complete Beginner Program

```js
const name = prompt("Enter your name:");
const age = Number(prompt("Enter your age:"));

console.log("========== PROFILE ==========");

console.log(`Name: ${name}`);
console.log(`Age: ${age}`);

if (age >= 18) {
  console.log("Status: Adult");
} else {
  console.log("Status: Minor");
}
```

This small program already combines:

* Variables
* Strings
* Numbers
* Input
* Type conversion
* Template literals
* Conditions
* Output

---

# 31. JavaScript in HTML

You can connect JavaScript to HTML.

## HTML

```html
<!DOCTYPE html>
<html>
<head>
  <title>JavaScript</title>
</head>

<body>

  <h1>Hello JavaScript</h1>

  <script>
    console.log("JavaScript is running!");
  </script>

</body>
</html>
```

The `<script>` element allows JavaScript code to run in the browser.

---

# 32. External JavaScript File

Instead of putting JavaScript directly inside HTML, you can create:

```text
index.html
script.js
```

HTML:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My App</title>
</head>

<body>

  <h1>Hello</h1>

  <script src="script.js"></script>

</body>
</html>
```

JavaScript:

```js
console.log("External JavaScript file!");
```

This is generally better for larger applications because it separates structure from behavior.

---

# 33. `defer`

When loading external JavaScript in the `<head>`, you can use `defer`.

```html
<script src="script.js" defer></script>
```

Example:

```html
<head>
  <script src="script.js" defer></script>
</head>
```

`defer` tells the browser to download the script while parsing HTML and execute it after the document has been parsed.

This is commonly useful for DOM-based scripts.

---

# 34. Browser Console

You can experiment with JavaScript directly in your browser.

In Chrome:

```text
Right Click
     ↓
Inspect
     ↓
Console
```

Then:

```js
console.log("Hello JavaScript");
```

Try:

```js
10 + 20
```

You should get:

```text
30
```

Try:

```js
typeof "Hello"
```

Result:

```text
"string"
```

The console is one of the best places to experiment while learning.

---

# 35. JavaScript Errors

JavaScript can produce errors.

Example:

```js
console.log(username);
```

If `username` does not exist, you may get:

```text
ReferenceError
```

Another example:

```js
const age = 20;

age = 30;
```

This produces an error because a `const` variable cannot be reassigned.

Errors are normal during programming.

The important skill is learning how to:

1. Read the error.
2. Find the file and line.
3. Understand what caused it.
4. Fix the underlying problem.

---

# 36. Debugging with console.log()

Suppose:

```js
const price = 100;
const quantity = 3;

const total = price * quantity;
```

You can inspect values:

```js
console.log("price:", price);
console.log("quantity:", quantity);
console.log("total:", total);
```

Output:

```text
price: 100
quantity: 3
total: 300
```

This is a basic but powerful debugging technique.

---

# 37. Strict Mode

JavaScript supports strict mode.

```js
"use strict";
```

Example:

```js
"use strict";

x = 10;
```

This causes an error because `x` was not declared.

In modern JavaScript modules, strict mode is automatically enabled, so you usually do not need to manually write `"use strict"` in module-based code.

---

# 38. JavaScript is Dynamically Typed

You do not normally declare a variable's type explicitly.

```js
let value = 10;
```

Later:

```js
value = "Hello";
```

The variable can now reference a string.

Another example:

```js
let data = true;

data = 100;

data = "JavaScript";
```

This flexibility is called **dynamic typing**.

However, TypeScript can add static type checking on top of JavaScript.

---

# 39. Primitive vs Reference Values

This is an important foundation.

Primitive example:

```js
let a = 10;
let b = a;

b = 20;

console.log(a);
console.log(b);
```

Output:

```text
10
20
```

Objects behave differently:

```js
const user1 = {
  name: "Alex"
};

const user2 = user1;

user2.name = "Sam";

console.log(user1.name);
```

Output:

```text
Sam
```

Why?

Because both variables refer to the same object.

Conceptually:

```text
user1 ─────┐
           ↓
        Object
        name: Sam
           ↑
user2 ─────┘
```

This concept becomes extremely important when working with React state, APIs, and application data.

---

# 40. JavaScript is Prototype-Based

JavaScript objects use prototypes for inheritance.

Example:

```js
const user = {
  name: "Alex"
};

console.log(user.toString());
```

You didn't define `toString()` yourself.

It is available through the object's prototype chain.

Later, when learning:

```js
class
extends
super
prototype
```

you will understand this system more deeply.

---

# 41. JavaScript is Multi-Paradigm

JavaScript supports multiple programming styles.

## Procedural

```js
const a = 10;
const b = 20;

const result = a + b;

console.log(result);
```

## Functional

```js
const numbers = [1, 2, 3];

const doubled = numbers.map(n => n * 2);
```

## Object-Oriented

```js
class User {
  constructor(name) {
    this.name = name;
  }
}
```

Modern JavaScript applications often combine these approaches.

---

# 42. JavaScript Functions

Functions allow you to reuse code.

```js
function greet() {
  console.log("Hello!");
}

greet();
```

With parameters:

```js
function greet(name) {
  console.log(`Hello ${name}`);
}

greet("Alex");
greet("Sam");
```

Output:

```text
Hello Alex
Hello Sam
```

Functions become one of the most important concepts in JavaScript.

---

# 43. A Practical Example — Shopping Cart

```js
const productName = "Laptop";
const price = 70000;
const quantity = 2;

const total = price * quantity;

console.log("Product:", productName);
console.log("Price:", price);
console.log("Quantity:", quantity);
console.log("Total:", total);
```

Output:

```text
Product: Laptop
Price: 70000
Quantity: 2
Total: 140000
```

This introduces concepts you will use in real applications.

---

# 44. A Practical Example — Student Profile

```js
const name = "Navaneeth";
const age = 20;
const course = "Computer Science";
const isStudent = true;

console.log("========== STUDENT ==========");

console.log(`Name: ${name}`);
console.log(`Age: ${age}`);
console.log(`Course: ${course}`);
console.log(`Student: ${isStudent}`);
```

---

# 45. A Practical Example — Login Check

```js
const username = "admin";
const password = "1234";

const enteredUsername = "admin";
const enteredPassword = "1234";

if (
  enteredUsername === username &&
  enteredPassword === password
) {
  console.log("Login successful");
} else {
  console.log("Invalid credentials");
}
```

This introduces:

* Variables
* Strings
* Conditions
* Comparison
* Logical operators

> This is only a learning example. Real authentication should never store passwords like this in frontend JavaScript.

---

# 46. A Practical Example — Age Calculator

```js
const birthYear = 2005;
const currentYear = 2026;

const age = currentYear - birthYear;

console.log(`You are approximately ${age} years old.`);
```

Output:

```text
You are approximately 21 years old.
```

For real applications, use actual dates rather than simply subtracting years when exact age matters.

---

# 47. A Practical Example — Simple Bill Calculator

```js
const itemPrice = 500;
const quantity = 3;
const taxRate = 0.18;

const subtotal = itemPrice * quantity;
const tax = subtotal * taxRate;
const total = subtotal + tax;

console.log(`Subtotal: ₹${subtotal}`);
console.log(`Tax: ₹${tax}`);
console.log(`Total: ₹${total}`);
```

Output:

```text
Subtotal: ₹1500
Tax: ₹270
Total: ₹1770
```

This is a good beginner exercise because it resembles real application logic.

---

# 48. Important JavaScript Concepts to Remember

At this stage, understand these ideas:

```text
JavaScript
    ↓
Programming Language
    ↓
Runs in browsers + Node.js
    ↓
Works with values
    ↓
Values have types
    ↓
Variables store references to values
    ↓
Operators manipulate values
    ↓
Conditions control decisions
    ↓
Loops repeat work
    ↓
Functions organize reusable logic
    ↓
Objects organize related data
    ↓
DOM allows browser JavaScript to interact with HTML
    ↓
Async JavaScript handles delayed operations
    ↓
Fetch communicates with APIs
```

---

# 49. Beginner Mistakes to Avoid

## Mistake 1 — Using `var` everywhere

Avoid:

```js
var name = "Alex";
```

Prefer:

```js
const name = "Alex";
```

or:

```js
let name = "Alex";
```

---

## Mistake 2 — Using `==` without understanding coercion

Instead of:

```js
if (age == 18)
```

prefer:

```js
if (age === 18)
```

---

## Mistake 3 — Forgetting that user input is usually text

```js
const age = prompt("Age:");

console.log(age + 1);
```

If the user enters `20`, the result may be:

```text
201
```

because `"20"` is a string.

Convert it:

```js
const age = Number(prompt("Age:"));

console.log(age + 1);
```

Result:

```text
21
```

---

## Mistake 4 — Confusing `=` and `===`

Assignment:

```js
age = 20;
```

Comparison:

```js
age === 20;
```

---

## Mistake 5 — Trying to memorize everything

Do not try to memorize every JavaScript method.

Instead:

```text
Understand the concept
        ↓
Write code
        ↓
Make mistakes
        ↓
Debug
        ↓
Practice
        ↓
Build projects
```

Programming skill comes from applying concepts.

---

# 50. Recommended Beginner Workflow

When learning a new JavaScript concept:

### Step 1 — Understand

Read what the concept means.

### Step 2 — Type the example

Do not just copy-paste.

Type it yourself.

### Step 3 — Predict

Before running:

```js
console.log(10 + 20);
```

ask yourself:

```text
What will happen?
```

### Step 4 — Run

Execute the program.

### Step 5 — Modify

Change:

```js
10 + 20
```

to:

```js
50 + 70
```

### Step 6 — Break it

Intentionally make an error.

### Step 7 — Fix it

Read the error and understand why it happened.

### Step 8 — Build something

Turn the concept into a small project.

---

# 51. Mini Challenges

## Challenge 1 — Personal Information

Create variables for:

```text
Name
Age
City
Country
Profession
```

Print them using a template literal.

Expected style:

```text
My name is Alex.
I am 20 years old.
I live in Hyderabad, India.
I am a student.
```

---

## Challenge 2 — Rectangle

Create:

```js
const length = 10;
const width = 5;
```

Calculate:

```text
Area
Perimeter
```

Formula:

```text
Area = length × width

Perimeter = 2 × (length + width)
```

---

## Challenge 3 — Shopping

Create:

```text
Product
Price
Quantity
```

Calculate the total.

---

## Challenge 4 — Temperature

Create a Celsius temperature:

```js
const celsius = 30;
```

Convert it to Fahrenheit.

Formula:

```text
F = (C × 9/5) + 32
```

---

## Challenge 5 — Age

Create:

```js
const birthYear = 2005;
const currentYear = 2026;
```

Calculate the approximate age.

---

# 52. Beginner Project

## Personal Profile Generator

Create a program that asks the user:

```text
Name
Age
City
Country
Profession
Dream Job
```

Then display:

```text
================================
          MY PROFILE
================================

Name       : Navaneeth
Age        : 20
City       : Rajahmundry
Country    : India
Profession : Student
Dream Job  : Software Engineer

================================
```

Example:

```js
const name = prompt("Enter your name:");
const age = Number(prompt("Enter your age:"));
const city = prompt("Enter your city:");
const country = prompt("Enter your country:");
const profession = prompt("Enter your profession:");
const dreamJob = prompt("Enter your dream job:");

console.log("================================");
console.log("           MY PROFILE");
console.log("================================");

console.log(`Name       : ${name}`);
console.log(`Age        : ${age}`);
console.log(`City       : ${city}`);
console.log(`Country    : ${country}`);
console.log(`Profession : ${profession}`);
console.log(`Dream Job  : ${dreamJob}`);

console.log("================================");
```

---

# 53. What You Should Understand Before Topic 02

Before moving to **Variables**, make sure you understand:

* What JavaScript is
* Where JavaScript runs
* Browser vs Node.js
* JavaScript engines
* `console.log()`
* Comments
* Statements
* Semicolons
* Case sensitivity
* Identifiers
* JavaScript values
* Basic data types
* Strings
* Numbers
* Booleans
* `undefined`
* `null`
* Objects
* Arrays
* `typeof`
* Expressions
* Operators
* Template literals
* User input
* Basic errors
* Basic debugging
* Dynamic typing
* Primitive vs reference values
* Functions at a basic level
* How JavaScript connects to HTML

---

# 54. Quick Revision

```js
// Output
console.log("Hello");

// String
const name = "Alex";

// Number
const age = 20;

// Boolean
const isStudent = true;

// Object
const user = {
  name: "Alex",
  age: 20
};

// Array
const skills = [
  "JavaScript",
  "React",
  "Node.js"
];

// Expression
const total = 10 + 20;

// Template literal
console.log(`Hello ${name}`);

// Condition
if (age >= 18) {
  console.log("Adult");
}

// Function
function greet(name) {
  console.log(`Hello ${name}`);
}

greet("Alex");
```

---

# 55. Final Mental Model

Remember JavaScript like this:

```text
                  JAVASCRIPT
                       │
          ┌────────────┴────────────┐
          │                         │
        Values                   Behavior
          │                         │
    ┌─────┼─────┐             ┌─────┼─────┐
    │     │     │             │     │     │
 String Number Boolean      Functions Conditions Loops
    │     │     │
    └─────┼─────┘
          │
       Objects
          │
       Arrays
          │
          ▼
      Application
          │
    ┌─────┼──────────┐
    │     │          │
   DOM   APIs      Async
    │     │          │
    └─────┼──────────┘
          │
          ▼
      Real Apps
          │
     ┌────┼────┐
     │    │    │
   React Node APIs
```

The most important thing is not memorizing syntax. **Understand what the code is doing, predict the result, run it, modify it, break it, and fix it.**

---

# Practice Checklist

Before moving to Topic 02, you should be able to write these without looking at the notes:

* [ ] `console.log()`
* [ ] Comments
* [ ] Strings
* [ ] Numbers
* [ ] Booleans
* [ ] Objects
* [ ] Arrays
* [ ] `typeof`
* [ ] Basic arithmetic
* [ ] Template literals
* [ ] `if / else`
* [ ] Basic functions
* [ ] User input
* [ ] Type conversion
* [ ] Basic debugging
* [ ] A small profile program

Once these feel comfortable, move to:

# 02 — Variables

where you will learn `let`, `const`, `var`, scope, reassignment, declaration, initialization, naming conventions, and best practices in much greater depth.
