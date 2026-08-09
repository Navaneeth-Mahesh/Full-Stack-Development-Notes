# 02 — JavaScript Variables

> Variables are one of the most fundamental concepts in JavaScript. They allow us to store, access, update, and organize data inside our programs.

---

# 1. What is a Variable?

A **variable** is a named reference used to store a value.

Example:

```js
const name = "Navaneeth";
```

Here:

```text
const       → keyword
name        → variable name
=           → assignment operator
"Navaneeth" → value
```

Think of a variable as a labeled box:

```text
name
┌───────────────┐
│  "Navaneeth"  │
└───────────────┘
```

You can then use the variable:

```js
console.log(name);
```

Output:

```text
Navaneeth
```

---

# 2. Why Do We Need Variables?

Without variables, we would have to repeat values everywhere.

Without variables:

```js
console.log("Navaneeth");
console.log("Navaneeth");
console.log("Navaneeth");
```

With a variable:

```js
const name = "Navaneeth";

console.log(name);
console.log(name);
console.log(name);
```

Variables make programs:

* Easier to read
* Easier to modify
* Easier to maintain
* More reusable
* More dynamic

---

# 3. Creating a Variable

JavaScript provides three keywords for declaring variables:

```js
let
const
var
```

Example:

```js
let age = 20;

const name = "Alex";

var city = "Hyderabad";
```

However, in modern JavaScript:

```text
const → default choice
let   → when reassignment is required
var   → generally avoid in modern code
```

---

# 4. Variable Declaration

Declaring a variable means creating the variable.

```js
let age;
```

Here, the variable exists but does not have an explicitly assigned value.

```js
console.log(age);
```

Output:

```text
undefined
```

---

# 5. Variable Initialization

Initialization means giving a variable its initial value.

```js
let age = 20;
```

Here:

```text
Declaration → let age
Initialization → = 20
```

You can also do them separately:

```js
let age;

age = 20;
```

---

# 6. Declaration vs Initialization vs Assignment

These concepts are related but different.

```js
let score;
```

### Declaration

The variable is created:

```text
score → undefined
```

Then:

```js
score = 100;
```

### Assignment

A value is assigned to the variable.

You can initialize directly:

```js
let score = 100;
```

This performs declaration + initialization.

---

# 7. `let`

`let` creates a block-scoped variable that can be reassigned.

Example:

```js
let age = 20;

age = 21;

console.log(age);
```

Output:

```text
21
```

You can change the value.

---

# 8. Reassigning a `let` Variable

```js
let score = 50;

console.log(score);

score = 75;

console.log(score);

score = 100;

console.log(score);
```

Output:

```text
50
75
100
```

This is useful when a value changes during program execution.

Examples:

```js
let count = 0;

count++;
```

```js
let username = "Alex";

username = "Sam";
```

---

# 9. `const`

`const` creates a variable binding that cannot be reassigned.

Example:

```js
const pi = 3.14159;
```

This is not allowed:

```js
const pi = 3.14159;

pi = 3.14;
```

You will get a `TypeError`.

---

# 10. Why Use `const`?

Most variables in a program don't need to be reassigned.

Example:

```js
const name = "Navaneeth";
const birthYear = 2005;
const country = "India";
```

These values don't need to change.

Using `const` communicates:

> "This variable should continue referring to the same value."

---

# 11. `const` Does Not Mean Immutable

This is a very important concept.

Consider:

```js
const user = {
  name: "Alex",
  age: 20
};
```

You cannot do:

```js
user = {};
```

But you can modify the object's properties:

```js
user.age = 21;
```

This works.

You can also:

```js
user.name = "Sam";
```

Why?

Because `const` prevents **reassignment of the variable binding**.

It does not automatically make the object immutable.

---

# 12. `const` with Arrays

This also applies to arrays.

```js
const fruits = ["Apple", "Banana"];
```

You cannot do:

```js
fruits = ["Mango"];
```

But you can modify the array:

```js
fruits.push("Mango");
```

Now:

```js
console.log(fruits);
```

Output:

```text
["Apple", "Banana", "Mango"]
```

Again:

```text
const → cannot reassign the variable
```

not:

```text
const → everything inside the value is immutable
```

---

# 13. `var`

`var` is the older way of declaring variables.

Example:

```js
var name = "Alex";
```

It can be reassigned:

```js
var age = 20;

age = 21;
```

It can also be redeclared:

```js
var name = "Alex";

var name = "Sam";
```

This is one reason modern JavaScript developers generally prefer `let` and `const`.

---

# 14. `let` vs `const` vs `var`

| Feature                 | `let` | `const` | `var`         |
| ----------------------- | ----- | ------- | ------------- |
| Reassign                | Yes   | No      | Yes           |
| Redeclare in same scope | No    | No      | Yes           |
| Block scoped            | Yes   | Yes     | No            |
| Function scoped         | Yes   | Yes     | Yes           |
| Modern recommendation   | Yes   | Yes     | Usually avoid |

Example:

```js
let age = 20;
age = 21;
```

Allowed.

```js
const age = 20;
age = 21;
```

Not allowed.

```js
var age = 20;
var age = 21;
```

Allowed, but generally not recommended.

---

# 15. Best Practice

Use:

```js
const
```

by default.

If you later discover that the variable must change:

```js
let
```

Example:

```js
const name = "Alex";

let score = 0;

score = 10;
```

Avoid:

```js
var
```

unless you specifically need to understand or work with legacy JavaScript code.

---

# 16. Variable Naming Rules

JavaScript variable names must follow certain rules.

Valid:

```js
const name = "Alex";
const age = 20;
const userName = "Alex";
const user_name = "Alex";
const $price = 100;
const price2 = 200;
```

Invalid:

```js
const 2name = "Alex";
```

You cannot start a variable name with a number.

Invalid:

```js
const user-name = "Alex";
```

The `-` is interpreted as subtraction.

---

# 17. Case Sensitivity

JavaScript is case-sensitive.

These are different variables:

```js
const name = "Alex";
const Name = "Sam";
const NAME = "John";
```

So:

```js
console.log(name);
```

is different from:

```js
console.log(Name);
```

---

# 18. Naming Conventions

JavaScript commonly uses **camelCase**.

Good:

```js
const firstName = "Alex";
const lastName = "Smith";
const userAge = 20;
const totalPrice = 500;
const isLoggedIn = true;
```

Avoid unnecessarily unclear names:

```js
const x = 20;
const y = 30;
const z = 50;
```

Unless you're writing mathematical logic where such names are meaningful.

---

# 19. Descriptive Variable Names

Bad:

```js
const x = 50000;
```

Better:

```js
const salary = 50000;
```

Bad:

```js
const a = 20;
```

Better:

```js
const studentAge = 20;
```

Good variable names reduce the amount of explanation your code needs.

---

# 20. Boolean Naming Convention

Boolean variables often start with words such as:

```text
is
has
can
should
will
```

Examples:

```js
const isLoggedIn = true;

const isAdmin = false;

const hasPermission = true;

const canEdit = false;

const shouldUpdate = true;
```

This makes conditions easier to understand:

```js
if (isLoggedIn) {
  console.log("Welcome!");
}
```

---

# 21. Constants Naming Convention

For true application-wide constants, uppercase names are sometimes used.

```js
const MAX_USERS = 100;
const API_TIMEOUT = 5000;
const TAX_RATE = 0.18;
```

However, don't feel that every `const` variable must be uppercase.

This is perfectly normal:

```js
const userName = "Alex";
```

Uppercase is mainly useful when communicating that a value represents a fixed configuration or mathematical constant.

---

# 22. Reserved Words

Some words are reserved by JavaScript.

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
try
catch
throw
import
export
```

You should not use them as variable names.

Invalid:

```js
const class = "JavaScript";
```

Valid:

```js
const className = "JavaScript";
```

---

# 23. Variables Can Store Different Types

JavaScript variables can hold many types of values.

String:

```js
const name = "Alex";
```

Number:

```js
const age = 20;
```

Boolean:

```js
const isStudent = true;
```

Array:

```js
const skills = ["JavaScript", "React"];
```

Object:

```js
const user = {
  name: "Alex",
  age: 20
};
```

Function:

```js
const greet = function () {
  console.log("Hello");
};
```

---

# 24. Variables Can Change Types

Because JavaScript is dynamically typed:

```js
let value = 100;
```

Then:

```js
value = "Hello";
```

Then:

```js
value = true;
```

This is valid JavaScript.

However, changing the type of a variable repeatedly can make code harder to understand.

Prefer meaningful and consistent variables:

```js
let score = 0;

score = 100;
score = 200;
```

instead of:

```js
let data = 100;

data = "Hello";

data = true;
```

---

# 25. Variable Scope

Scope determines where a variable can be accessed.

Example:

```js
{
  const message = "Hello";

  console.log(message);
}
```

This works.

But:

```js
{
  const message = "Hello";
}

console.log(message);
```

causes:

```text
ReferenceError
```

because `message` only exists inside the block.

---

# 26. Block Scope

`let` and `const` are block-scoped.

A block is usually represented by `{}`.

Example:

```js
if (true) {
  const message = "Inside block";

  console.log(message);
}
```

This works.

Outside:

```js
if (true) {
  const message = "Inside block";
}

console.log(message);
```

The variable is not accessible.

---

# 27. `var` and Block Scope

`var` behaves differently.

```js
if (true) {
  var message = "Hello";
}

console.log(message);
```

This can work because `var` is not block-scoped.

This behavior can create unexpected bugs.

That is another reason modern JavaScript prefers:

```js
let
const
```

---

# 28. Function Scope

Variables declared inside a function are generally accessible only inside that function.

```js
function greet() {
  const message = "Hello";

  console.log(message);
}

greet();
```

But:

```js
function greet() {
  const message = "Hello";
}

console.log(message);
```

causes an error.

---

# 29. Global Variables

A variable declared in the top-level scope may be accessible throughout the relevant program/module scope.

Example:

```js
const appName = "My App";

function showAppName() {
  console.log(appName);
}

showAppName();
```

Output:

```text
My App
```

However, avoid creating unnecessary global state.

Global variables can make programs harder to:

* Debug
* Test
* Maintain
* Understand

Prefer local variables when possible.

---

# 30. Lexical Scope

JavaScript uses **lexical scoping**.

This means the accessibility of variables is determined by where code is written.

Example:

```js
const name = "Alex";

function greet() {
  console.log(name);
}

greet();
```

The function can access `name` because it was defined in an outer scope.

---

# 31. Nested Scope

Scopes can exist inside other scopes.

```js
const country = "India";

function outer() {
  const city = "Hyderabad";

  function inner() {
    const name = "Alex";

    console.log(country);
    console.log(city);
    console.log(name);
  }

  inner();
}

outer();
```

The inner function can access variables from its outer scopes.

This concept eventually leads to **closures**.

---

# 32. Shadowing

A variable inside a nested scope can have the same name as one outside.

Example:

```js
const name = "Alex";

function greet() {
  const name = "Sam";

  console.log(name);
}

greet();
```

Output:

```text
Sam
```

The inner `name` shadows the outer `name`.

Outside:

```js
console.log(name);
```

Output:

```text
Alex
```

---

# 33. Temporal Dead Zone

`let` and `const` are hoisted but cannot be accessed before their declaration is initialized.

Example:

```js
console.log(age);

let age = 20;
```

This produces:

```text
ReferenceError
```

This period between entering the scope and the declaration being initialized is called the **Temporal Dead Zone (TDZ)**.

---

# 34. `var` Hoisting

`var` behaves differently.

```js
console.log(age);

var age = 20;
```

The result is:

```text
undefined
```

Conceptually, JavaScript treats the declaration as being available earlier, although the assignment happens later.

This behavior can be confusing, so prefer `let` and `const`.

---

# 35. Hoisting

Hoisting describes how JavaScript processes declarations before executing code.

Function declarations:

```js
greet();

function greet() {
  console.log("Hello");
}
```

This works because function declarations are hoisted.

With `let`/`const`:

```js
console.log(name);

const name = "Alex";
```

You get a `ReferenceError`.

Understanding hoisting is important for debugging and understanding JavaScript execution.

---

# 36. Assignment Operator

The basic assignment operator is:

```js
=
```

Example:

```js
let score = 10;
```

It means:

```text
Take the value 10
and assign it to score.
```

It does NOT mean mathematical equality.

---

# 37. Reassignment

```js
let score = 10;

score = 20;

console.log(score);
```

Output:

```text
20
```

The old value is replaced.

---

# 38. Compound Assignment

JavaScript provides shorthand assignment operators.

Instead of:

```js
score = score + 10;
```

you can write:

```js
score += 10;
```

Similarly:

```js
score -= 5;
score *= 2;
score /= 2;
score %= 3;
```

Example:

```js
let score = 100;

score += 20;

console.log(score);
```

Output:

```text
120
```

---

# 39. Increment and Decrement

Increment:

```js
let count = 0;

count++;
```

Now:

```text
count = 1
```

Decrement:

```js
count--;
```

Now:

```text
count = 0
```

These are commonly used with loops and counters.

---

# 40. Multiple Variables

You can declare multiple variables.

```js
const firstName = "Alex";
const lastName = "Smith";
const age = 20;
```

Avoid writing unnecessarily compressed code:

```js
const firstName = "Alex", lastName = "Smith", age = 20;
```

The first style is usually easier to read.

---

# 41. Constants and Configuration

Consider an application:

```js
const MAX_LOGIN_ATTEMPTS = 5;
const API_TIMEOUT = 5000;
const TAX_RATE = 0.18;
```

These values can be used throughout the relevant module.

```js
if (attempts >= MAX_LOGIN_ATTEMPTS) {
  console.log("Account locked");
}
```

This is better than scattering magic numbers throughout your code.

Bad:

```js
if (attempts >= 5) {
  ...
}
```

Better:

```js
if (attempts >= MAX_LOGIN_ATTEMPTS) {
  ...
}
```

---

# 42. Magic Numbers

A **magic number** is a number used directly in code without explaining its meaning.

Example:

```js
const total = price * 1.18;
```

What is `1.18`?

Better:

```js
const TAX_RATE = 0.18;

const total = price * (1 + TAX_RATE);
```

Now the meaning is clear.

---

# 43. Variable Destructuring Preview

JavaScript allows values to be extracted into variables.

Object:

```js
const user = {
  name: "Alex",
  age: 20
};

const { name, age } = user;
```

Now:

```js
console.log(name);
console.log(age);
```

Array:

```js
const colors = ["red", "green", "blue"];

const [first, second] = colors;
```

You will study destructuring in detail later.

---

# 44. Variable Default Values

You can provide defaults using destructuring:

```js
const user = {
  name: "Alex"
};

const {
  name,
  age = 18
} = user;

console.log(age);
```

Output:

```text
18
```

This becomes especially useful when processing API responses.

---

# 45. Variables and User Input

Example:

```js
const name = prompt("Enter your name:");

console.log(`Hello ${name}`);
```

The variable stores whatever the user enters.

For numbers:

```js
const age = Number(prompt("Enter your age:"));

console.log(age);
```

Always remember that browser `prompt()` returns a string or `null`.

---

# 46. Real-World Example — Shopping Cart

```js
const productName = "Laptop";
const price = 70000;
let quantity = 1;

quantity = 2;

const total = price * quantity;

console.log(`Product: ${productName}`);
console.log(`Price: ₹${price}`);
console.log(`Quantity: ${quantity}`);
console.log(`Total: ₹${total}`);
```

Output:

```text
Product: Laptop
Price: ₹70000
Quantity: 2
Total: ₹140000
```

Notice:

```text
productName → const
price       → const
quantity    → let
total       → const
```

Why?

Because only `quantity` changes.

---

# 47. Real-World Example — User Profile

```js
const firstName = "Navaneeth";
const lastName = "Gurani";
const age = 20;
const country = "India";
const isStudent = true;

console.log(`
Name: ${firstName} ${lastName}
Age: ${age}
Country: ${country}
Student: ${isStudent}
`);
```

---

# 48. Real-World Example — Score

```js
let score = 0;

score += 10;
score += 20;
score += 30;

console.log(score);
```

Output:

```text
60
```

This is a perfect example of why `let` is useful.

---

# 49. Real-World Example — Bank Balance

```js
let balance = 10000;

balance += 5000;

balance -= 2000;

console.log(`Current balance: ₹${balance}`);
```

Output:

```text
Current balance: ₹13000
```

In a real banking application, financial operations require much stronger validation, server-side authorization, transaction handling, and precise monetary representation.

---

# 50. Real-World Example — Temperature

```js
const celsius = 30;

const fahrenheit = (celsius * 9) / 5 + 32;

console.log(`Temperature: ${fahrenheit}°F`);
```

Because `celsius` does not change:

```js
const celsius = 30;
```

is appropriate.

---

# 51. Real-World Example — Login State

```js
let isLoggedIn = false;

console.log(isLoggedIn);

isLoggedIn = true;

console.log(isLoggedIn);
```

Output:

```text
false
true
```

This demonstrates why boolean state often uses `let`.

---

# 52. Real-World Example — Shopping Cart Count

```js
let cartItems = 0;

cartItems++;

cartItems++;

cartItems++;

console.log(`Items in cart: ${cartItems}`);
```

Output:

```text
Items in cart: 3
```

---

# 53. Variable References

A variable doesn't always literally contain an object.

For example:

```js
const user = {
  name: "Alex"
};
```

The variable `user` refers to an object.

Conceptually:

```text
user
 │
 ▼
┌───────────────┐
│ name: "Alex"  │
└───────────────┘
```

This becomes very important when learning:

* Objects
* Arrays
* Functions
* React state
* Memory
* References
* Shallow copies
* Deep copies

---

# 54. Reassignment vs Mutation

This distinction is extremely important.

## Reassignment

Changing what a variable refers to:

```js
let user = {
  name: "Alex"
};

user = {
  name: "Sam"
};
```

The variable now refers to a different object.

---

## Mutation

Changing the existing object:

```js
const user = {
  name: "Alex"
};

user.name = "Sam";
```

The same object was modified.

Remember:

```text
Reassignment → change the variable's reference
Mutation     → change the existing object's contents
```

---

# 55. `const` Example

```js
const user = {
  name: "Alex"
};

user.name = "Sam";
```

Allowed.

But:

```js
user = {
  name: "John"
};
```

Not allowed.

Visual:

```text
const user
    │
    ▼
Object A
name: Alex
```

You can modify:

```text
Object A
name: Sam
```

But you cannot make `user` point to another object.

---

# 56. `let` Example

```js
let user = {
  name: "Alex"
};

user = {
  name: "Sam"
};
```

Allowed.

Now:

```text
user
 │
 ▼
Object B
name: Sam
```

---

# 57. Variable Lifetime

A variable exists within its scope.

Example:

```js
function test() {
  const message = "Hello";

  console.log(message);
}

test();
```

The local variable belongs to the function's execution context.

After the function finishes, the variable is no longer directly accessible from outside.

Closures can allow some variables to remain reachable after the outer function returns.

---

# 58. Best Practice — Declare Close to Use

Prefer:

```js
function calculateTotal(price, quantity) {
  const total = price * quantity;

  return total;
}
```

Instead of declaring many unrelated variables far away from where they are used.

Keeping variables close to their purpose improves readability.

---

# 59. Best Practice — Minimize Mutability

Prefer:

```js
const name = "Alex";
const age = 20;
```

over unnecessary:

```js
let name = "Alex";
let age = 20;
```

If a value never changes, `const` communicates that clearly.

---

# 60. Best Practice — Avoid Global Variables

Avoid:

```js
let currentUser;
let cart;
let settings;
let appState;
```

all living globally.

Prefer organizing application state into appropriate modules, objects, functions, or framework-managed state.

For example:

```js
const appState = {
  currentUser: null,
  cart: [],
  settings: {}
};
```

For larger applications, you would usually use more structured architecture rather than one giant global object.

---

# 61. Best Practice — Use Meaningful Names

Bad:

```js
const x = 500;
```

Good:

```js
const productPrice = 500;
```

Bad:

```js
let a = false;
```

Good:

```js
let isLoggedIn = false;
```

Bad:

```js
const d = 30;
```

Good:

```js
const daysInMonth = 30;
```

---

# 62. Best Practice — Don't Over-Abbreviate

Avoid:

```js
const usrNm = "Alex";
const phNo = "1234567890";
```

Prefer:

```js
const username = "Alex";
const phoneNumber = "1234567890";
```

Readable code is more valuable than saving a few characters.

---

# 63. Best Practice — Don't Create Unnecessary Variables

This:

```js
const result = 10 + 20;

console.log(result);
```

is fine if `result` is meaningful or reused.

But:

```js
const temporaryResult = 10 + 20;
console.log(temporaryResult);
```

may be unnecessary if the variable adds no clarity.

Sometimes this is perfectly fine:

```js
console.log(10 + 20);
```

Use variables when they improve readability, reuse, or debugging.

---

# 64. Common Mistakes

## Mistake 1

```js
const age = 20;

age = 21;
```

Problem:

`const` cannot be reassigned.

Use:

```js
let age = 20;

age = 21;
```

---

## Mistake 2

```js
let userName = "Alex";

let userName = "Sam";
```

Problem:

`let` cannot be redeclared in the same scope.

Use:

```js
let userName = "Alex";

userName = "Sam";
```

---

## Mistake 3

```js
console.log(name);

const name = "Alex";
```

Problem:

The variable is in the Temporal Dead Zone until initialization.

Correct:

```js
const name = "Alex";

console.log(name);
```

---

## Mistake 4

```js
const 123name = "Alex";
```

Invalid identifier.

Correct:

```js
const name123 = "Alex";
```

---

## Mistake 5

```js
const user-name = "Alex";
```

Invalid because `-` is an operator.

Correct:

```js
const userName = "Alex";
```

---

# 65. Practice Challenge 1 — Student Information

Create variables for:

```text
Name
Age
College
Branch
Year
```

Use `const`.

Then print:

```text
Name: ...
Age: ...
College: ...
Branch: ...
Year: ...
```

---

# 66. Practice Challenge 2 — Score Tracker

Start:

```js
let score = 0;
```

Then:

```text
Add 10
Add 20
Subtract 5
Add 50
```

Print the final score.

Expected:

```text
75
```

---

# 67. Practice Challenge 3 — Shopping Cart

Create:

```js
const productName = "Phone";
const price = 30000;
let quantity = 2;
```

Calculate:

```text
Total price
```

Then change quantity to `3`.

Calculate the new total.

---

# 68. Practice Challenge 4 — User Login

Create:

```js
let isLoggedIn = false;
```

Change it to:

```js
true
```

Print:

```text
User logged in: true
```

---

# 69. Practice Challenge 5 — Profile Generator

Create:

```js
const name = "Navaneeth";
const age = 20;
const city = "Rajahmundry";
const country = "India";
const profession = "Student";
const dreamJob = "Software Engineer";
```

Print:

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

---

# 70. Interview Questions

## Q1. What is a variable?

A variable is a named binding/reference used to access a value in a program.

---

## Q2. Difference between `let` and `const`?

`let` allows reassignment.

```js
let age = 20;
age = 21;
```

`const` does not allow reassignment.

```js
const age = 20;
// age = 21; // Error
```

Both are block-scoped.

---

## Q3. Difference between `var` and `let`?

Important differences:

```text
var → function scoped
let → block scoped
```

`var` can also be redeclared in the same scope, while `let` cannot.

---

## Q4. Should I use `var`?

For modern JavaScript development, normally use:

```text
const
let
```

instead of `var`.

---

## Q5. Can a `const` object be modified?

Yes.

```js
const user = {
  name: "Alex"
};

user.name = "Sam";
```

This works.

But reassignment does not:

```js
user = {};
```

---

## Q6. What is scope?

Scope determines where a variable can be accessed.

---

## Q7. What is block scope?

Variables declared with `let` and `const` are accessible only within the block where they are declared.

---

## Q8. What is hoisting?

Hoisting refers to JavaScript's processing of declarations before execution of code. The behavior differs between `var`, `let`, `const`, and function declarations.

---

## Q9. What is the Temporal Dead Zone?

The TDZ is the period from entering a scope until a `let` or `const` declaration is initialized, during which accessing the variable causes a `ReferenceError`.

---

## Q10. What is reassignment?

Changing the value/reference associated with a variable.

```js
let age = 20;

age = 21;
```

---

# 71. Quick Comparison

```text
                  let          const          var
-------------------------------------------------------
Reassign          Yes           No            Yes
Redeclare         No            No            Yes
Block scoped      Yes           Yes           No
Function scoped   Yes           Yes           Yes
Modern usage      Yes           Yes           Avoid
```

---

# 72. The Golden Rule

When declaring a variable, ask:

### Does this variable need to be reassigned?

If **NO**:

```js
const
```

If **YES**:

```js
let
```

Avoid:

```js
var
```

unless working with legacy code or studying its behavior.

---

# 73. Final Mental Model

Think about variables like this:

```text
                    VARIABLE
                       │
          ┌────────────┴────────────┐
          │                         │
        let                       const
          │                         │
   Can reassign              Cannot reassign
          │                         │
          └────────────┬────────────┘
                       │
                     VALUE
                       │
          ┌────────────┼─────────────┐
          │            │             │
        String       Number       Boolean
          │
          ├── Object
          │
          ├── Array
          │
          └── Function
```

And remember:

```text
Declaration
    ↓
Create the variable

Initialization
    ↓
Give it its first value

Assignment
    ↓
Give/update its value

Scope
    ↓
Where can it be accessed?

const
    ↓
Cannot reassign

let
    ↓
Can reassign

var
    ↓
Legacy behavior; generally avoid
```

---

# 74. Final Checklist

Before moving to Topic 03, you should be able to explain and use:

* [ ] What a variable is
* [ ] Declaration
* [ ] Initialization
* [ ] Assignment
* [ ] Reassignment
* [ ] `let`
* [ ] `const`
* [ ] `var`
* [ ] `let` vs `const`
* [ ] `let` vs `var`
* [ ] Block scope
* [ ] Function scope
* [ ] Global scope
* [ ] Lexical scope
* [ ] Shadowing
* [ ] Hoisting
* [ ] Temporal Dead Zone
* [ ] Naming rules
* [ ] camelCase
* [ ] Boolean naming
* [ ] Constants
* [ ] Compound assignment
* [ ] Increment/decrement
* [ ] Primitive vs reference values
* [ ] Reassignment vs mutation
* [ ] `const` with objects
* [ ] `const` with arrays
* [ ] Descriptive variable names
* [ ] Avoiding global variables
* [ ] Avoiding unnecessary mutation

---

# 75. What Comes Next?

Now that you understand variables, the next topic is:

# 03 — Arithmetic Operators

You will learn how JavaScript performs calculations using:

```text
+
-
*
/
%
**
++
--
+=
-=
*=
/=
%=
```

You will also learn:

* Operator precedence
* Parentheses
* Increment/decrement
* Pre-increment vs post-increment
* Floating-point behavior
* Practical calculation programs
* Common arithmetic mistakes
* Real-world examples
