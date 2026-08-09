# 06 — JavaScript Constants

> A constant is a variable whose **binding cannot be reassigned** after it has been created.

In JavaScript, constants are created using:

```js
const
```

Example:

```js
const PI = 3.14159;

console.log(PI);
```

Output:

```text
3.14159
```

---

# 1. What is a Constant?

A constant is a value that you don't intend to reassign.

Example:

```js
const country = "India";

console.log(country);
```

The variable `country` is declared using `const`.

You cannot later do:

```js
country = "USA";
```

This produces an error.

---

# 2. `const` Syntax

The basic syntax is:

```js
const variableName = value;
```

Example:

```js
const age = 20;
const name = "Navaneeth";
const isStudent = true;
```

---

# 3. `const` Must Be Initialized

Unlike `let`, you cannot declare a `const` variable without giving it a value.

This is invalid:

```js
const age;
```

JavaScript throws an error.

You must do:

```js
const age = 20;
```

---

# 4. Why Does `const` Need a Value?

A `const` declaration creates a binding that cannot later be reassigned.

Therefore JavaScript needs to know what value the binding initially refers to.

Correct:

```js
const username = "Alex";
```

Incorrect:

```js
const username;
```

---

# 5. Reassigning a `const`

Consider:

```js
const age = 20;

age = 21;
```

This causes an error similar to:

```text
TypeError: Assignment to constant variable.
```

The important point is:

```text
const → cannot be reassigned
```

---

# 6. `const` vs `let`

Compare:

```js
let age = 20;

age = 21;

console.log(age);
```

Output:

```text
21
```

But:

```js
const age = 20;

age = 21;
```

causes an error.

Therefore:

```text
let  → can be reassigned
const → cannot be reassigned
```

---

# 7. `const` vs `var`

JavaScript has three main variable declaration keywords:

```text
var
let
const
```

Basic comparison:

| Feature                 | `var`         | `let` | `const` |
| ----------------------- | ------------- | ----- | ------- |
| Reassign                | Yes           | Yes   | No      |
| Redeclare in same scope | Yes           | No    | No      |
| Block scoped            | No            | Yes   | Yes     |
| Must initialize         | No            | No    | Yes     |
| Modern recommendation   | Usually avoid | Yes   | Yes     |

For modern JavaScript:

```text
Prefer const by default.
Use let when reassignment is required.
Avoid var in most modern code.
```

---

# 8. Why Prefer `const`?

Using `const` makes your intention clear.

Example:

```js
const birthYear = 2005;
```

Someone reading your code knows that you don't intend to reassign `birthYear`.

Compare:

```js
let birthYear = 2005;
```

This suggests the value might change later.

---

# 9. Constants Should Usually Be Uppercase?

You may see constants written like:

```js
const PI = 3.14159;
const MAX_USERS = 100;
const API_URL = "https://example.com";
```

This is a common naming convention for **fixed configuration values**.

But not every `const` variable needs uppercase letters.

For example:

```js
const username = "Alex";
const userAge = 20;
const profile = {};
```

These are perfectly normal.

So:

```text
const → language feature
UPPER_CASE → naming convention
```

They are not the same thing.

---

# 10. Constant Example — Pi

```js
const PI = 3.14159;

const radius = 5;

const area = PI * radius * radius;

console.log(area);
```

Output:

```text
78.53975
```

---

# 11. Constant Example — Tax Rate

```js
const TAX_RATE = 0.18;

const price = 1000;

const tax = price * TAX_RATE;

console.log(tax);
```

Output:

```text
180
```

---

# 12. Constant Example — Maximum Score

```js
const MAX_SCORE = 100;

let score = 75;

console.log(`${score}/${MAX_SCORE}`);
```

Output:

```text
75/100
```

Here:

```text
MAX_SCORE → doesn't change
score → can change
```

---

# 13. Constants and Calculations

You can use constants in expressions.

```js
const TAX_RATE = 0.18;
const price = 2000;

const tax = price * TAX_RATE;
const finalPrice = price + tax;

console.log(finalPrice);
```

Output:

```text
2360
```

---

# 14. `const` With Strings

```js
const firstName = "Navaneeth";
const lastName = "Gurani";

console.log(firstName + " " + lastName);
```

Output:

```text
Navaneeth Gurani
```

You cannot reassign:

```js
firstName = "Alex";
```

---

# 15. `const` With Numbers

```js
const age = 20;

console.log(age);
```

This is valid.

But:

```js
age = 21;
```

is invalid.

---

# 16. `const` With Booleans

```js
const isLoggedIn = true;

console.log(isLoggedIn);
```

You cannot do:

```js
isLoggedIn = false;
```

because that is reassignment.

---

# 17. `const` With `null`

```js
const result = null;

console.log(result);
```

This is valid.

The constant simply holds the value:

```text
null
```

---

# 18. `const` With `undefined`

You can technically write:

```js
const value = undefined;
```

This is valid because the constant is initialized.

However, if you expect the value to be assigned later, use `let` instead.

For example:

```js
let user;
```

is appropriate if the value will be assigned later.

---

# 19. `const` With Arrays

This is extremely important.

You can create an array using `const`:

```js
const fruits = ["Apple", "Banana", "Mango"];

console.log(fruits);
```

You cannot reassign the array:

```js
fruits = ["Orange"];
```

But you **can modify the contents** of the array.

```js
fruits.push("Orange");

console.log(fruits);
```

Output:

```text
["Apple", "Banana", "Mango", "Orange"]
```

---

# 20. Why Can a `const` Array Change?

Because `const` prevents **reassignment of the variable binding**.

It does not make the array itself immutable.

Think of:

```js
const fruits = [];
```

as:

```text
fruits ───────► Array
```

You cannot make `fruits` point to another array:

```js
fruits = [];
```

But you can modify the existing array:

```js
fruits.push("Apple");
```

---

# 21. Important Difference

This is invalid:

```js
const fruits = ["Apple"];

fruits = ["Banana"];
```

Because you are replacing the entire array.

But this is valid:

```js
const fruits = ["Apple"];

fruits.push("Banana");
```

Because you are modifying the existing array.

---

# 22. Array Mutation

Mutation means changing the contents of an existing object or array.

Example:

```js
const numbers = [1, 2, 3];

numbers.push(4);

console.log(numbers);
```

Output:

```text
[1, 2, 3, 4]
```

The variable still refers to the same array.

---

# 23. Other Array Mutations

These work with a `const` array:

```js
const numbers = [1, 2, 3];

numbers.push(4);
numbers.pop();
numbers.shift();
numbers.unshift(10);
numbers.splice(0, 1);
numbers.sort();
numbers.reverse();
```

All of these modify the existing array.

---

# 24. `const` With Objects

You can create objects with `const`:

```js
const user = {
  name: "Alex",
  age: 20
};

console.log(user);
```

You cannot replace the entire object:

```js
user = {
  name: "John"
};
```

But you can modify its properties:

```js
user.age = 21;
```

This is valid.

---

# 25. Object Mutation

Example:

```js
const user = {
  name: "Alex",
  age: 20
};

user.age = 21;

console.log(user);
```

Output:

```text
{
  name: "Alex",
  age: 21
}
```

The object changed, but the `user` binding was not reassigned.

---

# 26. Adding Object Properties

```js
const user = {
  name: "Alex"
};

user.age = 20;
user.city = "Hyderabad";

console.log(user);
```

Output:

```text
{
  name: "Alex",
  age: 20,
  city: "Hyderabad"
}
```

---

# 27. Removing Object Properties

```js
const user = {
  name: "Alex",
  age: 20
};

delete user.age;

console.log(user);
```

Output:

```text
{
  name: "Alex"
}
```

The object can still be mutated even though the binding is `const`.

---

# 28. The Most Important `const` Concept

Remember:

> `const` prevents reassignment, not mutation.

Example:

```js
const user = {
  name: "Alex"
};

user.name = "John";
```

Valid.

But:

```js
user = {
  name: "John"
};
```

Invalid.

---

# 29. Primitive vs Reference Values

This becomes easier when you understand JavaScript values conceptually as:

```text
Primitive values
Reference/object values
```

Primitive examples:

```text
string
number
boolean
bigint
symbol
undefined
null
```

Objects include:

```text
object
array
function
```

For primitive values:

```js
const age = 20;

age = 21;
```

is reassignment and therefore invalid.

For objects:

```js
const user = {
  age: 20
};

user.age = 21;
```

this mutates the existing object and is allowed.

---

# 30. `const` Does Not Mean Immutable

This is a very important distinction.

Incorrect understanding:

```text
const = completely immutable
```

Correct understanding:

```text
const = cannot reassign the binding
```

For example:

```js
const user = {
  name: "Alex"
};

user.name = "John";
```

The property changes.

---

# 31. Making Objects Immutable

If you want to prevent direct modification of an object's properties, you can use:

```js
Object.freeze()
```

Example:

```js
const user = Object.freeze({
  name: "Alex",
  age: 20
});
```

Attempting:

```js
user.age = 21;
```

will not successfully change the frozen object's property.

In strict mode, attempting to modify a frozen property can throw an error.

---

# 32. `Object.freeze()` Is Shallow

Consider:

```js
const user = Object.freeze({
  name: "Alex",
  address: {
    city: "Hyderabad"
  }
});
```

The top-level object is frozen.

But:

```js
user.address.city = "Chennai";
```

can still modify the nested object.

Why?

Because:

```text
Object.freeze()
```

is shallow.

Deep immutability requires additional techniques.

---

# 33. `const` and Functions

Functions can be stored in constants:

```js
const greet = function () {
  console.log("Hello");
};

greet();
```

You cannot reassign:

```js
greet = function () {
  console.log("Hi");
};
```

---

# 34. `const` With Arrow Functions

Modern JavaScript commonly uses:

```js
const greet = () => {
  console.log("Hello");
};

greet();
```

This is very common in:

* React
* Node.js
* Express
* Modern JavaScript
* TypeScript

---

# 35. `const` With Classes

You can also store a class declaration in a `const` variable when using a class expression:

```js
const Person = class {
  constructor(name) {
    this.name = name;
  }
};

const person = new Person("Alex");

console.log(person.name);
```

---

# 36. `const` and Block Scope

`const` is **block scoped**.

A block is commonly represented by:

```js
{
  // block
}
```

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

causes an error because `message` only exists inside the block.

---

# 37. `const` Inside `if`

```js
if (true) {
  const message = "Logged in";

  console.log(message);
}
```

Works.

But:

```js
if (true) {
  const message = "Logged in";
}

console.log(message);
```

does not work.

---

# 38. `const` Inside Loops

You can use `const` inside loops.

Example:

```js
for (const fruit of ["Apple", "Banana", "Mango"]) {
  console.log(fruit);
}
```

Output:

```text
Apple
Banana
Mango
```

Each iteration gets its own loop variable binding.

---

# 39. `const` in `for...of`

This is very common:

```js
const fruits = ["Apple", "Banana", "Mango"];

for (const fruit of fruits) {
  console.log(fruit);
}
```

You don't need to reassign `fruit`.

Each iteration assigns the current iteration value to the loop variable.

---

# 40. `const` in `for...in`

```js
const user = {
  name: "Alex",
  age: 20
};

for (const key in user) {
  console.log(key);
}
```

Output:

```text
name
age
```

---

# 41. Why Not Use `let` Everywhere?

You technically can use `let` for many situations.

But if a variable should not be reassigned:

```js
const name = "Alex";
```

communicates more information than:

```js
let name = "Alex";
```

Using `const` helps make your code easier to reason about.

---

# 42. When Should You Use `const`?

Use `const` when:

```text
The binding should not be reassigned.
```

Examples:

```js
const username = "Alex";
const birthYear = 2005;
const API_URL = "https://example.com";
const user = {};
const fruits = [];
```

---

# 43. When Should You Use `let`?

Use `let` when the value needs to be reassigned.

Example:

```js
let score = 0;

score += 10;
score += 20;

console.log(score);
```

Output:

```text
30
```

Here `let` is appropriate because `score` changes.

---

# 44. When Should You Use `var`?

In modern JavaScript, generally avoid `var` unless you are dealing with legacy code or specifically need its older semantics.

Prefer:

```js
const
```

or:

```js
let
```

---

# 45. `const` Naming Rules

JavaScript variable naming rules apply to `const`.

Valid:

```js
const name = "Alex";
const userName = "Alex";
const _name = "Alex";
const $price = 100;
const age2 = 20;
```

Invalid:

```js
const 2age = 20;
```

Invalid:

```js
const user-name = "Alex";
```

Invalid:

```js
const class = "JavaScript";
```

because `class` is a reserved keyword.

---

# 46. Naming Convention

For normal variables:

```js
const firstName = "Alex";
const userAge = 20;
const isLoggedIn = true;
```

Use camelCase.

For fixed configuration values:

```js
const API_URL = "...";
const MAX_RETRIES = 3;
const TAX_RATE = 0.18;
```

UPPER_CASE is a common convention.

---

# 47. Constants With User Input

A common mistake is:

```js
const age = prompt("Enter age:");

age = Number(age);
```

This is invalid because `age` is a constant.

Instead:

```js
const input = prompt("Enter age:");
const age = Number(input);
```

Or:

```js
const age = Number(prompt("Enter age:"));
```

---

# 48. Constant With Calculation

```js
const radius = 10;
const PI = Math.PI;

const area = PI * radius ** 2;

console.log(area);
```

`radius` and `PI` are not reassigned.

`area` is also a constant because the calculated result itself isn't reassigned.

---

# 49. `const` With Counters

A counter normally changes.

Therefore this is wrong:

```js
const count = 0;

count++;
```

You need:

```js
let count = 0;

count++;
```

Because:

```text
count → changes
```

---

# 50. `const` With a Fixed Counter Limit

You can combine `const` and `let`:

```js
const MAX_COUNT = 10;

let count = 0;

while (count < MAX_COUNT) {
  console.log(count);
  count++;
}
```

Here:

```text
MAX_COUNT → constant
count → changing variable
```

This is an excellent real-world pattern.

---

# 51. Constant Configuration

A program might have:

```js
const API_URL = "https://api.example.com";
const MAX_RETRIES = 3;
const REQUEST_TIMEOUT = 5000;
```

These values represent configuration that your code should not reassign during execution.

---

# 52. Constant in a Game

```js
const MAX_HEALTH = 100;

let health = MAX_HEALTH;

health -= 20;

console.log(health);
```

Output:

```text
80
```

Here:

```text
MAX_HEALTH → fixed
health → changes
```

---

# 53. Constant in a Shopping Cart

```js
const TAX_RATE = 0.18;

let cartTotal = 1000;

const tax = cartTotal * TAX_RATE;

console.log(tax);
```

---

# 54. Constant in a Game

```js
const MAX_SCORE = 1000;

let score = 0;

score += 100;
score += 200;

console.log(`${score}/${MAX_SCORE}`);
```

Output:

```text
300/1000
```

---

# 55. Constants and `Math`

JavaScript provides built-in mathematical constants.

For example:

```js
console.log(Math.PI);
```

Output:

```text
3.141592653589793
```

You can store it:

```js
const PI = Math.PI;
```

Other examples:

```js
Math.E
Math.LN2
Math.LN10
Math.LOG2E
Math.LOG10E
Math.SQRT1_2
Math.SQRT2
```

---

# 56. `const` With Objects — Reference Example

Consider:

```js
const person = {
  name: "Alex"
};
```

Think of it conceptually as:

```text
person ───────► object
```

This is allowed:

```js
person.name = "John";
```

because the object itself is being modified.

This is not:

```js
person = {};
```

because the binding would point to a different object.

---

# 57. `const` With Arrays — Reference Example

```js
const numbers = [1, 2, 3];
```

Conceptually:

```text
numbers ───────► [1, 2, 3]
```

This is allowed:

```js
numbers.push(4);
```

But:

```js
numbers = [5, 6, 7];
```

is not allowed.

---

# 58. Reassignment vs Mutation

This distinction is extremely important.

### Reassignment

Changing what the variable refers to:

```js
const user = {};

user = {};
```

Not allowed.

### Mutation

Changing the existing object:

```js
const user = {};

user.name = "Alex";
```

Allowed.

---

# 59. Another Mutation Example

```js
const settings = {
  theme: "dark",
  language: "English"
};

settings.theme = "light";

console.log(settings);
```

Output:

```text
{
  theme: "light",
  language: "English"
}
```

---

# 60. Nested Object Mutation

```js
const user = {
  name: "Alex",
  address: {
    city: "Hyderabad"
  }
};

user.address.city = "Chennai";

console.log(user.address.city);
```

Output:

```text
Chennai
```

The nested object was mutated.

---

# 61. Reassigning a Nested Property

This is allowed:

```js
const user = {
  address: {
    city: "Hyderabad"
  }
};

user.address = {
  city: "Chennai"
};
```

Why?

Because you are changing a property of the object, not reassigning the `user` variable itself.

---

# 62. Destructuring With `const`

You can use `const` with destructuring.

Array:

```js
const numbers = [10, 20, 30];

const [a, b, c] = numbers;

console.log(a);
console.log(b);
console.log(c);
```

Output:

```text
10
20
30
```

---

# 63. Object Destructuring With `const`

```js
const user = {
  name: "Alex",
  age: 20
};

const { name, age } = user;

console.log(name);
console.log(age);
```

Output:

```text
Alex
20
```

---

# 64. Constants With Default Values

You can use default values during destructuring:

```js
const user = {
  name: "Alex"
};

const { name, age = 18 } = user;

console.log(name);
console.log(age);
```

Output:

```text
Alex
18
```

---

# 65. `const` and Temporal Dead Zone

`const` variables are block scoped and are subject to the **Temporal Dead Zone (TDZ)**.

Example:

```js
console.log(age);

const age = 20;
```

This produces a `ReferenceError`.

You must access the variable only after its declaration has been evaluated.

Correct:

```js
const age = 20;

console.log(age);
```

---

# 66. Temporal Dead Zone Concept

Conceptually:

```text
Block starts
     ↓
TDZ
     ↓
const declaration evaluated
     ↓
Variable can be accessed
```

This is one reason `const` and `let` behave differently from older `var` declarations.

---

# 67. `const` and Hoisting

`const` declarations are technically hoisted in the JavaScript execution model, but they cannot be accessed before initialization because of the Temporal Dead Zone.

This:

```js
console.log(name);

const name = "Alex";
```

does **not** behave like:

```js
console.log(name);

var name = "Alex";
```

The `const` example throws a `ReferenceError`.

---

# 68. Nested Blocks

```js
const name = "Alex";

{
  const name = "John";

  console.log(name);
}

console.log(name);
```

Output:

```text
John
Alex
```

Each block has its own `name` binding.

---

# 69. Shadowing

A variable in an inner scope can have the same name as one in an outer scope.

Example:

```js
const name = "Alex";

{
  const name = "John";

  console.log(name);
}

console.log(name);
```

Output:

```text
John
Alex
```

This is called **shadowing**.

---

# 70. `const` Inside Functions

```js
function greet() {
  const message = "Hello";

  console.log(message);
}

greet();
```

`message` exists only inside the function.

---

# 71. Function Scope vs Block Scope

`const` is block scoped.

Example:

```js
function test() {
  if (true) {
    const message = "Hello";

    console.log(message);
  }

  // message is not accessible here
}
```

The variable only exists inside the block where it was declared.

---

# 72. Constant References

You can have:

```js
const user1 = user2;
```

if `user2` exists.

For objects:

```js
const user1 = {
  name: "Alex"
};

const user2 = user1;

user2.name = "John";

console.log(user1.name);
```

Output:

```text
John
```

Why?

Both variables refer to the same object.

Conceptually:

```text
user1 ───┐
         ├──► object
user2 ───┘
```

---

# 73. Copying an Object

If you want a separate shallow copy:

```js
const user1 = {
  name: "Alex"
};

const user2 = {
  ...user1
};

user2.name = "John";

console.log(user1.name);
console.log(user2.name);
```

Output:

```text
Alex
John
```

This is an example of using the spread operator to create a shallow copy.

---

# 74. Copying an Array

```js
const numbers1 = [1, 2, 3];

const numbers2 = [...numbers1];

numbers2.push(4);

console.log(numbers1);
console.log(numbers2);
```

Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

---

# 75. Common Mistake — Reassigning `const`

Wrong:

```js
const username = "Alex";

username = "John";
```

Correct if the value needs to change:

```js
let username = "Alex";

username = "John";
```

---

# 76. Common Mistake — Declaring Without Initialization

Wrong:

```js
const age;
```

Correct:

```js
const age = 20;
```

If you need to assign later:

```js
let age;

age = 20;
```

---

# 77. Common Mistake — Thinking Objects Are Immutable

Wrong assumption:

```text
const object cannot change
```

Correct:

```js
const user = {
  name: "Alex"
};

user.name = "John";
```

This works.

`const` prevents reassignment of `user`, not mutation of the object.

---

# 78. Common Mistake — Using `const` for Counters

Wrong:

```js
const count = 0;

count++;
```

Correct:

```js
let count = 0;

count++;
```

---

# 79. Common Mistake — Using `let` for Everything

This works:

```js
let API_URL = "https://example.com";
```

But if the URL should never be reassigned, better:

```js
const API_URL = "https://example.com";
```

This communicates intent.

---

# 80. Best Practice — Default to `const`

A common modern JavaScript style is:

```text
1. Start with const.
2. If you discover that reassignment is required, use let.
3. Avoid var in new code.
```

Example:

```js
const name = "Alex";
const age = 20;

let score = 0;

score += 10;
```

---

# 81. Real-World Example — User Profile

```js
const user = {
  name: "Navaneeth",
  age: 20,
  city: "Hyderabad"
};

console.log(user.name);
console.log(user.age);
console.log(user.city);
```

You can modify the profile:

```js
user.age = 21;
```

But you cannot replace:

```js
user = {};
```

---

# 82. Real-World Example — Configuration

```js
const CONFIG = {
  API_URL: "https://api.example.com",
  TIMEOUT: 5000,
  MAX_RETRIES: 3
};

console.log(CONFIG.API_URL);
```

If your application needs the configuration to be immutable, consider freezing it:

```js
const CONFIG = Object.freeze({
  API_URL: "https://api.example.com",
  TIMEOUT: 5000,
  MAX_RETRIES: 3
});
```

Remember that `Object.freeze()` is shallow.

---

# 83. Real-World Example — Game

```js
const MAX_HEALTH = 100;
const DAMAGE = 20;

let playerHealth = MAX_HEALTH;

playerHealth -= DAMAGE;

console.log(`Player health: ${playerHealth}`);
```

Output:

```text
Player health: 80
```

---

# 84. Real-World Example — Shopping

```js
const TAX_RATE = 0.18;

let cartTotal = 2000;

const tax = cartTotal * TAX_RATE;
const finalPrice = cartTotal + tax;

console.log(`Tax: ₹${tax}`);
console.log(`Final price: ₹${finalPrice}`);
```

---

# 85. Real-World Example — Counter

```js
const MAX_COUNT = 5;

let count = 0;

while (count < MAX_COUNT) {
  console.log(count);

  count++;
}
```

Here:

```text
MAX_COUNT → const
count → let
```

This is the correct use of both keywords.

---

# 86. Real-World Example — API

```js
const API_URL = "https://api.example.com/users";

fetch(API_URL)
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
```

`API_URL` is not reassigned, so `const` is appropriate.

---

# 87. Real-World Example — React

In React, you'll frequently see:

```js
const [count, setCount] = useState(0);
```

Why is `count` a `const`?

Because React gives you a value for the current render.

You don't do:

```js
count = count + 1;
```

Instead, you use:

```js
setCount(count + 1);
```

This concept becomes extremely important when you learn React.

---

# 88. Real-World Example — Node.js

In Node.js, you will frequently use:

```js
const express = require("express");
```

or with ES modules:

```js
import express from "express";
```

You will commonly use `const` for modules and dependencies that aren't reassigned.

Example:

```js
const app = express();

const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

# 89. `const` in Modern JavaScript

You will see `const` everywhere in:

```text
Frontend
React
Node.js
Express
Next.js
TypeScript
Backend APIs
AI applications
```

Example:

```js
const user = getUser();
const response = await fetch(url);
const data = await response.json();
const result = processData(data);
```

This is why understanding `const` properly is important before moving into advanced JavaScript frameworks.

---

# 90. Interview Question — Is `const` Immutable?

Question:

> Does `const` make an object immutable?

Answer:

**No.**

`const` prevents reassignment of the binding.

Example:

```js
const user = {
  name: "Alex"
};

user.name = "John";
```

This is allowed.

But:

```js
user = {};
```

is not allowed.

---

# 91. Interview Question — Can a `const` Array Change?

Yes.

```js
const numbers = [1, 2, 3];

numbers.push(4);

console.log(numbers);
```

Output:

```text
[1, 2, 3, 4]
```

But:

```js
numbers = [5, 6];
```

is not allowed.

---

# 92. Interview Question — Can `const` Be Declared Without a Value?

No.

This is invalid:

```js
const x;
```

You must initialize it:

```js
const x = 10;
```

---

# 93. Interview Question — Is `const` Block Scoped?

Yes.

```js
{
  const x = 10;
}

console.log(x);
```

This causes a `ReferenceError`.

---

# 94. Interview Question — Can You Redeclare a `const`?

Not in the same scope.

This is invalid:

```js
const age = 20;

const age = 30;
```

Similarly:

```js
let age = 20;

const age = 30;
```

is invalid in the same scope.

But separate nested scopes can have separate bindings:

```js
const age = 20;

{
  const age = 30;

  console.log(age);
}
```

Output:

```text
30
```

---

# 95. `const` Cheat Sheet

```text
const
│
├── Cannot be reassigned
│
├── Must be initialized
│
├── Block scoped
│
├── Cannot be redeclared in same scope
│
├── Objects can be mutated
│
├── Arrays can be mutated
│
└── Does NOT mean deep immutability
```

---

# 96. `const` vs `let` Cheat Sheet

```text
                const              let
                 │                  │
        Cannot reassign       Can reassign
                 │                  │
        Must initialize       Initialization optional
                 │                  │
            Block scoped         Block scoped
                 │                  │
        Cannot redeclare       Cannot redeclare
          same scope             same scope
```

Example:

```js
const name = "Alex";

let score = 0;

score = 100;
```

---

# 97. `const` vs `let` Example

```js
const MAX_SCORE = 100;

let score = 0;

score += 20;
score += 30;

console.log(`${score}/${MAX_SCORE}`);
```

Output:

```text
50/100
```

This demonstrates a very common pattern:

```text
constant limit + changing state
```

---

# 98. Best Practices

### Use `const` by default

```js
const name = "Alex";
```

### Use `let` when reassignment is necessary

```js
let score = 0;
score++;
```

### Avoid `var` in modern code

```js
var name = "Alex";
```

Prefer:

```js
const name = "Alex";
```

### Use meaningful names

Good:

```js
const MAX_RETRIES = 3;
const TAX_RATE = 0.18;
const API_URL = "...";
```

Bad:

```js
const x = 3;
const a = 0.18;
const y = "...";
```

when the purpose isn't obvious.

---

# 99. Practice Questions

## Question 1

What happens?

```js
const age = 20;

age = 21;
```

Answer:

```text
TypeError
```

because `const` cannot be reassigned.

---

## Question 2

Is this valid?

```js
const age;
```

Answer:

```text
No.
```

A `const` declaration must be initialized.

---

## Question 3

Is this valid?

```js
const numbers = [1, 2, 3];

numbers.push(4);
```

Answer:

```text
Yes.
```

The array is mutated; the variable is not reassigned.

---

## Question 4

Is this valid?

```js
const numbers = [1, 2, 3];

numbers = [4, 5, 6];
```

Answer:

```text
No.
```

The binding is being reassigned.

---

## Question 5

Is this valid?

```js
const user = {
  name: "Alex"
};

user.name = "John";
```

Answer:

```text
Yes.
```

The object is being mutated.

---

# 100. Practice Challenge — Student

Create a program with:

```js
const MAX_MARKS = 100;

let marks = 0;
```

Ask the user for marks and display:

```text
Marks: 85/100
```

Make sure you convert the input to a number.

---

# 101. Practice Challenge — Game Health

Create:

```js
const MAX_HEALTH = 100;
const DAMAGE = 25;

let health = MAX_HEALTH;
```

Subtract damage three times.

Expected result:

```text
Health: 25
```

---

# 102. Practice Challenge — Shopping Cart

Create constants for:

```text
TAX_RATE
```

Use `let` for:

```text
cartTotal
```

Calculate:

```text
Subtotal
Tax
Final price
```

---

# 103. Practice Challenge — User Profile

Create a `const` object:

```js
const user = {
  name: "Alex",
  age: 20,
  city: "Hyderabad"
};
```

Then:

1. Print the user.
2. Change the age.
3. Add an email.
4. Delete the city.
5. Try replacing the entire object and observe the error.

---

# 104. Practice Challenge — Counter

Create:

```js
const MAX_COUNT = 10;
let count = 0;
```

Use a loop to print:

```text
0
1
2
3
4
5
6
7
8
9
```

Notice why:

```text
MAX_COUNT → const
count → let
```

---

# 105. Final Mental Model

Think of `const` like this:

```text
const user = object;

        user
          │
          ▼
      ┌─────────┐
      │ Object  │
      └─────────┘
```

You cannot make `user` point somewhere else:

```js
user = anotherObject;
```

But you can change the existing object:

```js
user.name = "John";
```

Therefore:

```text
const
   ↓
No reassignment

NOT

const
   ↓
Nothing can ever change
```

---

# 106. Final Checklist

Before moving to the next topic, make sure you understand:

* [ ] What `const` is
* [ ] How to declare a constant
* [ ] Why `const` must be initialized
* [ ] Reassignment
* [ ] Redeclaration
* [ ] `const` vs `let`
* [ ] `const` vs `var`
* [ ] Block scope
* [ ] Temporal Dead Zone
* [ ] Hoisting behavior
* [ ] `const` with strings
* [ ] `const` with numbers
* [ ] `const` with booleans
* [ ] `const` with arrays
* [ ] `const` with objects
* [ ] Mutation vs reassignment
* [ ] Object references
* [ ] Array references
* [ ] `Object.freeze()`
* [ ] Shallow immutability
* [ ] `const` with functions
* [ ] `const` with arrow functions
* [ ] `const` with loops
* [ ] `const` with destructuring
* [ ] Naming conventions
* [ ] Constants in real-world programs
* [ ] When to use `const`
* [ ] When to use `let`

---

# 107. One-Line Summary

> **`const` creates a block-scoped binding that cannot be reassigned after initialization, but if it refers to an object or array, the object's or array's contents can still be mutated.**

---

# 108. Key Rule to Remember

```js
const x = 10;

// ❌ Reassignment
x = 20;
```

But:

```js
const user = {
  name: "Alex"
};

// ✅ Mutation
user.name = "John";
```

And:

```js
const numbers = [1, 2, 3];

// ✅ Mutation
numbers.push(4);
```

The golden rule is:

```text
const → cannot reassign
const → can mutate objects/arrays
```

This distinction becomes extremely important when you move into **objects, arrays, functions, React, Node.js, and TypeScript**.
