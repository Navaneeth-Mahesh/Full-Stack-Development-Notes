# JavaScript Functions — The Complete Guide

### From First Principles to Professional Mastery

> *A textbook-style reference covering every function concept in modern JavaScript — syntax, internals, scope, closures, `this`, functional programming, performance, interviews, and real projects.*

---

## Table of Contents

1. [Part 1 — Introduction](#part-1--introduction)
2. [Part 2 — Function Basics](#part-2--function-basics)
3. [Part 3 — Scope](#part-3--scope)
4. [Part 4 — Closures](#part-4--closures)
5. [Part 5 — First-Class Functions](#part-5--first-class-functions)
6. [Part 6 — Higher Order Functions](#part-6--higher-order-functions)
7. [Part 7 — The `this` Keyword](#part-7--the-this-keyword)
8. [Part 8 — call, apply, bind](#part-8--call-apply-bind)
9. [Part 9 — Function Hoisting](#part-9--function-hoisting)
10. [Part 10 — Execution Context](#part-10--execution-context)
11. [Part 11 — The Call Stack](#part-11--the-call-stack)
12. [Part 12 — Advanced Functions](#part-12--advanced-functions)
13. [Part 13 — Functional Programming](#part-13--functional-programming)
14. [Part 14 — Performance](#part-14--performance)
15. [Part 15 — Best Practices](#part-15--best-practices)
16. [Part 16 — Common Mistakes](#part-16--common-mistakes)
17. [Part 17 — Interview Questions](#part-17--interview-questions)
18. [Part 18 — Practice](#part-18--practice)
19. [Part 19 — Mini Projects](#part-19--mini-projects)
20. [Part 20 — Summary Cheat Sheet](#part-20--summary-cheat-sheet)

---

# PART 1 — INTRODUCTION

## 1.1 What Are Functions?

A **function** is a named, reusable block of code that performs a specific task. You write the logic once, give it a name, and then you can "call" (run) that logic as many times as you want, from anywhere in your program, without retyping it.

Think of a function like a **kitchen recipe**. A recipe for "boiling an egg" doesn't change every time you cook — you follow the same steps each time, and you can hand that recipe to anyone (any part of your program) who needs a boiled egg. You don't rewrite the recipe from scratch every single time you're hungry.

In JavaScript, a function is also a **value**. This is one of the most important ideas in the entire language: functions are not just "actions" — they are objects that can be stored in variables, passed around, and returned from other functions, just like a number or a string.

```
+---------------------------------------------+
|                FUNCTION                       |
|                                               |
|   Name:        greet                         |
|   Inputs:      (name)                        |
|   Logic:       return "Hello " + name        |
|   Output:      a greeting string             |
|                                               |
+---------------------------------------------+
        |                     ^
        |  call greet("Sam")  |
        v                     |
   Runs the logic  ------> Produces "Hello Sam"
```

## 1.2 Why Functions Exist

Imagine you are building a program that needs to calculate the area of a rectangle in five different places in your code.

**Without functions**, you would write this formula five separate times:

```javascript
let area1 = 10 * 20;
let area2 = 5 * 8;
let area3 = 15 * 15;
let area4 = 7 * 3;
let area5 = 100 * 2;
```

This looks harmless with a simple formula, but real-world logic is rarely this simple. Imagine the formula for calculating area had to also handle negative numbers, unit conversions, and rounding. You would need to repeat that *entire block of logic* five times. If you later find a bug, you must fix it in five places. Miss one, and you have a bug hiding in your code.

**Functions solve this by centralizing logic.** You write it once:

```javascript
function calculateArea(length, width) {
  return length * width;
}

let area1 = calculateArea(10, 20);
let area2 = calculateArea(5, 8);
let area3 = calculateArea(15, 15);
```

Now there is only **one place** where the area logic lives. Fix a bug once, and every single usage across your entire application is instantly fixed.

## 1.3 Problems Without Functions

| Problem | Description |
|---|---|
| **Code Duplication** | The same logic is copy-pasted everywhere, bloating the file. |
| **Hard to Maintain** | A single bug fix must be repeated in every duplicated block. |
| **Poor Readability** | Long files with repeated logic are hard to scan and understand. |
| **No Reusability** | Logic tied to one location cannot be reused elsewhere. |
| **Difficult Testing** | You cannot isolate and test a "block of code" the way you can test a function. |
| **No Abstraction** | The reader has to understand every low-level detail instead of a simple, named concept. |

> **Note:** Programmers describe this problem with the acronym **DRY** — "Don't Repeat Yourself." Functions are the primary tool JavaScript gives you to stay DRY.

## 1.4 Benefits of Functions

- **Reusability** — Write once, use many times.
- **Abstraction** — Hide complex logic behind a simple name (`calculateArea` hides the multiplication).
- **Maintainability** — Centralized logic means centralized fixes.
- **Readability** — `calculateArea(l, w)` reads like English; raw formulas scattered everywhere do not.
- **Testability** — Functions can be tested in isolation with known inputs and expected outputs.
- **Modularity** — Large programs can be split into small, independent, composable pieces.
- **Delegation** — Functions can be handed to other parts of the program (or other functions) to be executed later — this is the foundation of callbacks, events, and asynchronous JavaScript.

## 1.5 Real-World Examples

| Real-World Scenario | Function Example |
|---|---|
| A calculator app | `add(a, b)`, `subtract(a, b)` |
| A login system | `validateLogin(username, password)` |
| An e-commerce cart | `calculateTotal(cartItems)` |
| A weather app | `getTemperature(city)` |
| A banking app | `withdraw(amount)`, `deposit(amount)` |
| Form validation | `isValidEmail(email)` |
| Games | `movePlayer(direction)`, `checkCollision(a, b)` |

Every single button click, every form submission, and every animation you've ever seen on a website is ultimately powered by functions being called in response to events.

## 1.6 Functions in Modern JavaScript

Modern JavaScript (ES6 and beyond) gives you many *forms* of functions, each suited to different situations:

| Style | Introduced | Typical Use |
|---|---|---|
| Function Declaration | Since JS existed | General-purpose, hoisted, named functions |
| Function Expression | Since JS existed | Assigning a function to a variable |
| Arrow Function | ES6 (2015) | Short callbacks, preserving `this` |
| Generator Function | ES6 (2015) | Producing sequences of values lazily |
| Async Function | ES2017 | Working with Promises using clean syntax |
| Method (in classes/objects) | ES6 (2015) | Behavior attached to objects |

By the end of this guide, you will deeply understand every one of these forms — not just their syntax, but *why* they exist and *when* to reach for each one.

> **Tip:** Don't rush through Part 1. Every advanced JavaScript concept — closures, `this`, promises, React hooks — is built on top of a rock-solid understanding of what a function actually is. Take your time here.

---
# PART 2 — FUNCTION BASICS

## 2.1 Function Syntax

A basic JavaScript function declaration looks like this:

```javascript
function functionName(parameter1, parameter2) {
  // function body — the logic
  return result;
}
```

| Piece | Meaning |
|---|---|
| `function` | Keyword telling JS "I am defining a function" |
| `functionName` | The identifier used to call the function later |
| `(parameter1, parameter2)` | Placeholders for the values the function needs |
| `{ ... }` | The function body — the code that runs |
| `return` | Sends a value back to wherever the function was called |

## 2.2 Function Declaration

```javascript
function greet(name) {
  return "Hello, " + name + "!";
}
```

**Line-by-line:**
1. `function greet(name) {` — Declares a function named `greet` that accepts one parameter, `name`.
2. `return "Hello, " + name + "!";` — Builds a greeting string and sends it back to the caller.
3. `}` — Closes the function body.

This is called a **function declaration** (also "function statement"). It is hoisted (explained in Part 9), meaning JavaScript loads its definition into memory before any code runs, so you can call it even before its line in the file.

## 2.3 Function Invocation (Calling)

Defining a function does **nothing** by itself — it just stores the recipe. To actually run the code inside, you must **invoke** (call) it:

```javascript
function greet(name) {
  return "Hello, " + name + "!";
}

greet("Maria"); // invocation — runs the function body
console.log(greet("Maria")); // "Hello, Maria!"
```

> **Warning:** A very common beginner mistake is writing `greet;` (without parentheses) and expecting it to run. Without `()`, you are only referring to the function itself as a value — you are not calling it.

## 2.4 Parameters vs Arguments

This distinction confuses many beginners, but it is simple:

| Term | Definition | Example |
|---|---|---|
| **Parameter** | The placeholder name listed in the function definition | `function greet(name)` → `name` is a parameter |
| **Argument** | The actual value passed in when calling the function | `greet("Maria")` → `"Maria"` is an argument |

```
function greet( name )         <-- "name" is a PARAMETER (a variable placeholder)
greet( "Maria" )                <-- "Maria" is an ARGUMENT (the real value supplied)
```

> **Tip:** Parameters are like labeled empty boxes; arguments are the actual items you put inside those boxes when calling the function.

## 2.5 The Return Statement

`return` does two things:
1. It stops the function's execution immediately.
2. It sends a value back to the code that called the function.

```javascript
function add(a, b) {
  return a + b;
  console.log("This will never run"); // unreachable code
}
```

If a function has no `return` statement, it implicitly returns `undefined`.

```javascript
function sayHi() {
  console.log("Hi!");
}

let result = sayHi(); // logs "Hi!"
console.log(result);  // undefined
```

## 2.6 Returning Multiple Values

JavaScript functions can only return **one** value directly — but that value can be an array or an object, which lets you effectively return many values at once.

```javascript
function getMinMax(numbers) {
  return {
    min: Math.min(...numbers),
    max: Math.max(...numbers)
  };
}

const { min, max } = getMinMax([4, 1, 9, 2]);
console.log(min, max); // 1 9
```

```javascript
function divide(a, b) {
  return [Math.floor(a / b), a % b]; // [quotient, remainder]
}

const [quotient, remainder] = divide(17, 5);
console.log(quotient, remainder); // 3 2
```

## 2.7 Default Parameters

Introduced in ES6, default parameters let you specify a fallback value when an argument isn't provided.

```javascript
function greet(name = "Guest") {
  return "Hello, " + name;
}

greet();        // "Hello, Guest"
greet("Sara");  // "Hello, Sara"
```

**Before ES6**, developers simulated this manually:

```javascript
function greet(name) {
  name = name || "Guest"; // old-style default
  return "Hello, " + name;
}
```

> **Warning:** The old `name || "Guest"` trick fails for falsy-but-valid values like `0`, `""`, or `false`. Default parameters (`name = "Guest"`) only trigger when the argument is `undefined`, making them safer.

## 2.8 Rest Parameters (`...`)

Rest parameters collect **all remaining arguments** into a real array.

```javascript
function sum(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}

sum(1, 2, 3);       // 6
sum(1, 2, 3, 4, 5); // 15
```

Here, `...numbers` gathers every argument passed into a single array called `numbers`, no matter how many are supplied.

## 2.9 Spread vs Rest — Comparison

These use the same `...` syntax but do **opposite** jobs depending on context.

| | Rest | Spread |
|---|---|---|
| **Purpose** | Collects multiple values INTO an array | Expands an array/object OUT into individual values |
| **Location** | Used in function parameters (or destructuring) | Used in function calls, array literals, object literals |
| **Example** | `function f(...args) {}` | `f(...[1,2,3])` |

```javascript
// REST — gathering
function multiply(...nums) {
  return nums.reduce((a, b) => a * b);
}

// SPREAD — expanding
const numbers = [2, 3, 4];
console.log(multiply(...numbers)); // spreads array into arguments -> 24
```

## 2.10 Named Functions vs Anonymous Functions

A **named function** has an identifier attached to it, useful for stack traces and self-reference (e.g., recursion).

```javascript
function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n - 1); // can call itself by name
}
```

An **anonymous function** has no name. These are common when passed directly as arguments (callbacks).

```javascript
setTimeout(function () {
  console.log("Runs after 1 second");
}, 1000);
```

> **Tip:** Anonymous functions are harder to debug because stack traces show `<anonymous>` instead of a helpful name. Many style guides prefer naming even callback functions when practical.

## 2.11 Function Expressions

A **function expression** creates a function and assigns it to a variable. Unlike declarations, expressions are NOT hoisted with their definition (see Part 9).

```javascript
const greet = function (name) {
  return "Hello, " + name;
};

greet("Ken"); // "Hello, Ken"
```

A **named function expression** keeps a name for debugging/recursion purposes while still being assigned to a variable:

```javascript
const factorial = function fact(n) {
  return n <= 1 ? 1 : n * fact(n - 1);
};
```

## 2.12 Arrow Functions

Introduced in ES6, arrow functions provide a shorter syntax and, critically, do **not** have their own `this` (explained fully in Part 7).

```javascript
const add = (a, b) => {
  return a + b;
};
```

## 2.13 Arrow Function Syntax Variations

| Syntax | Example | Notes |
|---|---|---|
| Multiple params, block body | `(a, b) => { return a + b; }` | Standard form |
| Single param (no parens needed) | `x => x * 2` | Parens are optional for exactly one param |
| No params | `() => console.log("hi")` | Parens required when there are zero params |
| Implicit return | `x => x * 2` | No `return` keyword needed; expression value is returned |
| Returning an object literal | `x => ({ value: x })` | Must wrap `{}` in `()` or JS thinks it's a function body |

## 2.14 Implicit Return vs Explicit Return

```javascript
// Implicit return — one-line expression, no braces, no "return" keyword
const square = x => x * x;

// Explicit return — braces require the "return" keyword
const squareExplicit = x => {
  return x * x;
};
```

> **Warning:** `x => { x * x }` does **NOT** return anything! Once you add curly braces, JavaScript treats the arrow function as having a full block body, and you must explicitly write `return`.

## 2.15 Functions as Values

In JavaScript, a function is a value, just like a number or string. You can store it, inspect its type, and pass it around.

```javascript
function sayHi() {
  return "Hi";
}

console.log(typeof sayHi); // "function"

const stored = sayHi; // stored now points to the SAME function
console.log(stored()); // "Hi"
```

## 2.16 Functions Stored in Variables

```javascript
const operations = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b
};

console.log(operations.add(5, 3)); // 8
```

## 2.17 Passing Functions as Arguments

```javascript
function processNumbers(numbers, operation) {
  return numbers.map(operation);
}

const doubled = processNumbers([1, 2, 3], x => x * 2);
console.log(doubled); // [2, 4, 6]
```

Here, `operation` is a function passed in as an argument — a foundational idea behind **callbacks** and **higher-order functions** (Part 6).

## 2.18 Returning Functions

```javascript
function multiplierFactory(factor) {
  return function (number) {
    return number * factor;
  };
}

const double = multiplierFactory(2);
const triple = multiplierFactory(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15
```

This is the gateway to **closures** (Part 4) — the returned function "remembers" the `factor` value even after `multiplierFactory` has finished running.

## 2.19 Nested Functions

Functions can be defined inside other functions. The inner function has access to everything in the outer function's scope.

```javascript
function outer() {
  let outerVar = "I am outside";

  function inner() {
    console.log(outerVar); // inner can "see" outerVar
  }

  inner();
}

outer(); // "I am outside"
```

## 2.20 Recursive Functions

A **recursive function** is a function that calls itself to solve a smaller version of the same problem, until it reaches a **base case** that stops the recursion.

```javascript
function factorial(n) {
  if (n <= 1) return 1;       // base case
  return n * factorial(n - 1); // recursive case
}

console.log(factorial(5)); // 120
```

**Internal working:**

```
factorial(5)
= 5 * factorial(4)
       = 4 * factorial(3)
              = 3 * factorial(2)
                     = 2 * factorial(1)
                            = 1   (base case reached)
                     = 2 * 1 = 2
              = 3 * 2 = 6
       = 4 * 6 = 24
= 5 * 24 = 120
```

## 2.21 Base Case

The **base case** is the condition that stops recursion. Without one, the function calls itself forever (see next section).

```javascript
function countdown(n) {
  if (n <= 0) {          // base case
    console.log("Done!");
    return;
  }
  console.log(n);
  countdown(n - 1);       // recursive call
}
```

## 2.22 Infinite Recursion

```javascript
function brokenCountdown(n) {
  console.log(n);
  brokenCountdown(n - 1); // no base case — never stops!
}

brokenCountdown(5); // Eventually throws: "RangeError: Maximum call stack size exceeded"
```

> **Warning:** Every recursive function you write **must** have a reachable base case, or it will crash the program with a stack overflow (explained fully in Part 11).

## 2.23 Immediately Invoked Function Expressions (IIFE)

An **IIFE** is a function that runs immediately after being defined — it is never called separately, only once, right away.

```javascript
(function () {
  console.log("This runs immediately!");
})();
```

**Why IIFEs exist:** Before ES6 introduced `let`/`const` and modules, IIFEs were the primary way to create a private, isolated scope so that variables didn't leak into (and clash with) the global scope.

```javascript
const counterModule = (function () {
  let count = 0; // private, not accessible outside

  return {
    increment() { count++; return count; }
  };
})();

console.log(counterModule.increment()); // 1
console.log(counterModule.count);       // undefined — truly private
```

### Practice Questions — Part 2

1. What is the difference between a parameter and an argument?
2. Why does `x => { x * 2 }` return `undefined`?
3. What happens if a recursive function has no base case?
4. When would you use rest parameters instead of the `arguments` object?
5. Rewrite a function declaration as an arrow function expression.

### Coding Exercises — Part 2

1. Write a function `isEven(n)` that returns `true`/`false`.
2. Write a recursive function `sumRange(n)` that returns the sum of all numbers from 1 to `n`.
3. Write a function using rest parameters that returns the largest number passed to it.
4. Write an IIFE that immediately calculates and logs the area of a circle with radius 5.
5. Write a function `makeGreeter(greeting)` that returns a new function which greets a name with that greeting.

---
# PART 3 — SCOPE

## 3.1 What Is Scope?

**Scope** determines *where* in your code a variable or function name can be accessed. Think of scope as a set of nested rooms: what's inside a small room can usually see what's in the bigger room around it, but the bigger room cannot see inside the small room.

```
+-------------------------------------------+
|  GLOBAL SCOPE                              |
|   let globalVar = "I'm everywhere";        |
|                                             |
|   +-----------------------------------+    |
|   |  FUNCTION SCOPE (outer)           |    |
|   |   let outerVar = "outer only";    |    |
|   |                                    |    |
|   |   +--------------------------+     |    |
|   |   | BLOCK SCOPE (if/for)    |     |    |
|   |   |  let innerVar = "block"|     |    |
|   |   +--------------------------+     |    |
|   +-----------------------------------+    |
+-------------------------------------------+
```

## 3.2 Why Scope Exists

Without scope, every variable in a program would be visible and editable from everywhere else — a recipe for chaos. Imagine two different files both using a variable named `count`. Without scope, they would overwrite each other's data. Scope isolates variables so different parts of a program can use the same names safely without conflict, and so that internal implementation details stay hidden.

## 3.3 Global Scope

Variables declared outside of any function or block live in the **global scope** and are accessible from anywhere in the program.

```javascript
let appName = "MyApp"; // global

function showName() {
  console.log(appName); // accessible here too
}
```

> **Warning:** Overusing global variables is a major anti-pattern (see Part 15). Global variables can be accidentally overwritten by any part of a large codebase, causing hard-to-trace bugs.

## 3.4 Function Scope

Variables declared with `var` inside a function are only accessible *inside* that function.

```javascript
function demo() {
  var localVar = "only in demo";
  console.log(localVar);
}

demo();
console.log(typeof localVar); // "undefined" — not accessible outside
```

## 3.5 Block Scope

`let` and `const` (ES6) are **block-scoped** — confined to the nearest `{ }`, including `if`, `for`, and `while` blocks. `var` ignores block scope entirely.

```javascript
if (true) {
  let blockScoped = "inside if";
  var functionScoped = "ignores block";
}

console.log(functionScoped); // "ignores block" — works
console.log(blockScoped);    // ReferenceError — not defined outside the block
```

| Keyword | Scope Type | Reassignable | Hoisted (usable before declaration) |
|---|---|---|---|
| `var` | Function scope | Yes | Yes (as `undefined`) |
| `let` | Block scope | Yes | No (Temporal Dead Zone) |
| `const` | Block scope | No | No (Temporal Dead Zone) |

## 3.6 Lexical Scope

"Lexical" means "related to where things are written in the source code." JavaScript uses **lexical scoping**: a function's access to variables is determined by *where it is physically defined* in the code, not by where it is called from.

```javascript
let value = "global";

function outer() {
  let value = "outer";

  function inner() {
    console.log(value); // looks up the scope chain from WHERE inner is WRITTEN
  }

  inner();
}

outer(); // "outer"
```

Even if `inner` were called from somewhere else entirely, it would still remember the scope it was *defined* in — this is the basis of closures (Part 4).

## 3.7 Scope Chain

When JavaScript looks up a variable, it searches the current scope first, then the scope that contains it, then the one containing that, and so on — all the way up to the global scope. This chain of nested lookups is called the **scope chain**.

```javascript
let level1 = "L1";

function a() {
  let level2 = "L2";

  function b() {
    let level3 = "L3";
    console.log(level1, level2, level3); // finds all three via the scope chain
  }

  b();
}

a(); // "L1 L2 L3"
```

If a variable is not found anywhere in the chain, JavaScript throws a `ReferenceError`.

## 3.8 Variable Shadowing

**Shadowing** happens when a variable declared in an inner scope has the same name as one in an outer scope — the inner one "hides" the outer one within that scope.

```javascript
let color = "blue";

function paint() {
  let color = "red"; // shadows the outer "color"
  console.log(color); // "red"
}

paint();
console.log(color); // "blue" — outer variable is untouched
```

> **Tip:** Shadowing is not an error, but it can confuse readers. Use distinct variable names when possible to avoid ambiguity.

## 3.9 Nested Scope

Scopes can be nested arbitrarily deep — functions inside functions inside functions, each creating a new, enclosed scope layer.

## 3.10 Scope Resolution

"Scope resolution" is the process the JavaScript engine follows to decide which variable a name refers to, by walking the scope chain outward until a match is found or the global scope is exhausted.

## 3.11 Lifetime of Variables

- **Global variables** live for the entire life of the program (until the page/process ends).
- **Function-scoped variables** (`var`) live only while the function is executing, then are normally cleaned up.
- **Block-scoped variables** (`let`/`const`) live only for the duration of the block.
- **Closures** (Part 4) are the exception: a variable can outlive its normal scope if an inner function still references it after the outer function has returned.

### Practice Questions — Part 3

1. What is the difference between function scope and block scope?
2. Why does `var` "leak" out of `if` blocks but `let` does not?
3. What is the scope chain, and how does JavaScript use it to resolve a variable name?
4. Give an example of variable shadowing and explain the output.
5. Why is lexical scope determined by where code is *written*, not where it is *called*?

---
# PART 4 — CLOSURES

## 4.1 What Is a Closure?

A **closure** is formed when a function "remembers" the variables from the scope it was defined in, even after that outer scope has finished executing. In simple words: **a function bundled together with its surrounding state.**

```javascript
function makeCounter() {
  let count = 0; // this variable lives in makeCounter's scope

  return function () {
    count++;
    return count;
  };
}

const counter = makeCounter(); // makeCounter() has already finished running
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

Even though `makeCounter()` has already returned, the inner function still has access to `count`. This is a closure in action.

## 4.2 Why Closures Exist

Closures exist because of **lexical scoping** (Part 3.6) combined with the fact that functions are first-class values (Part 5) that can be returned and stored. JavaScript doesn't destroy a variable just because the function that created it has finished running — if some other function still needs that variable, the JavaScript engine keeps it alive in memory.

Closures solve a very real, very common problem: **how do you create private state without classes?** Before ES6 classes (and even alongside them today), closures are the primary way JavaScript achieves data privacy and encapsulation.

## 4.3 Internal Working

```
makeCounter() is called
   |
   v
+---------------------------------+
| Execution Context: makeCounter  |
|   count = 0                     |
|   returns an inner function --->|----+
+---------------------------------+    |
   (normally this memory would        |
    be destroyed after the function   |
    call ends)                        |
                                       v
                     The returned inner function keeps a
                     hidden reference to makeCounter's
                     scope — called its "Closure".
                     So `count` is NOT destroyed.
```

## 4.4 Lexical Environment

Every time a function runs, JavaScript creates a **Lexical Environment** — an internal record of all variables declared in that scope, plus a reference to the parent scope's Lexical Environment. A closure is simply a function paired with a reference to the Lexical Environment in which it was created.

## 4.5 Memory Behind Closures

Normally, when a function finishes executing, its local variables become eligible for **garbage collection** (memory cleanup). But if an inner function (that closes over those variables) is returned or stored somewhere still reachable, the JavaScript engine cannot safely delete those variables — so it keeps them in memory for as long as the closure exists.

## 4.6 Closure Execution

Each call to an outer function creates a **brand-new** closure with its own independent variables:

```javascript
const counterA = makeCounter();
const counterB = makeCounter();

console.log(counterA()); // 1
console.log(counterA()); // 2
console.log(counterB()); // 1 — independent from counterA
```

## 4.7 Private Variables

Closures let you simulate "private" variables that cannot be accessed or modified directly from outside:

```javascript
function createBankAccount(initialBalance) {
  let balance = initialBalance; // private — no direct outside access

  return {
    deposit(amount) {
      balance += amount;
      return balance;
    },
    withdraw(amount) {
      if (amount > balance) {
        return "Insufficient funds";
      }
      balance -= amount;
      return balance;
    },
    getBalance() {
      return balance;
    }
  };
}

const account = createBankAccount(100);
console.log(account.deposit(50));   // 150
console.log(account.withdraw(30));  // 120
console.log(account.balance);       // undefined — truly private
```

## 4.8 Data Encapsulation

**Encapsulation** means bundling data with the functions that operate on it, while hiding the internal details from the outside world. The bank account example above is a perfect case: the only way to change `balance` is through the provided methods — you cannot reach in and set it directly.

## 4.9 Counter Example (Full Breakdown)

```javascript
function createCounter(start = 0, step = 1) {
  let count = start;

  return {
    increment() { count += step; return count; },
    decrement() { count -= step; return count; },
    reset()     { count = start; return count; }
  };
}

const counter = createCounter(10, 5);
console.log(counter.increment()); // 15
console.log(counter.increment()); // 20
console.log(counter.decrement()); // 15
console.log(counter.reset());     // 10
```

## 4.10 The Module Pattern

Before ES6 modules existed, closures (often combined with IIFEs) were used to build self-contained "modules" with private internals and a public API:

```javascript
const ShoppingCart = (function () {
  let items = []; // private

  return {
    addItem(item) {
      items.push(item);
    },
    removeItem(item) {
      items = items.filter(i => i !== item);
    },
    getItems() {
      return [...items]; // return a copy, not the original reference
    }
  };
})();

ShoppingCart.addItem("Apple");
ShoppingCart.addItem("Bread");
console.log(ShoppingCart.getItems()); // ["Apple", "Bread"]
console.log(ShoppingCart.items);      // undefined — private
```

## 4.11 Event Listener Example

Closures are extremely common in DOM event handling — each handler "remembers" the variables around it when it was attached:

```javascript
function setupButton(buttonName) {
  let clickCount = 0;

  document.getElementById(buttonName).addEventListener("click", function () {
    clickCount++;
    console.log(buttonName + " clicked " + clickCount + " times");
  });
}
```

Every time the button is clicked, the handler function still has access to `clickCount` and `buttonName`, even though `setupButton` finished running long ago.

## 4.12 Timer Example

```javascript
function delayedGreeting(name) {
  setTimeout(function () {
    console.log("Hello, " + name); // closure keeps "name" alive
  }, 1000);
}

delayedGreeting("Alex"); // after 1 second: "Hello, Alex"
```

## 4.13 Practical Uses of Closures

- Data privacy / encapsulation (bank accounts, counters)
- The module pattern
- Event handlers that need contextual data
- Function factories (Part 2.18)
- Memoization / caching (Part 13)
- Currying and partial application (Part 13)
- Debounce and throttle utilities (Part 14)

## 4.14 Memory Leaks with Closures

Closures keep variables alive as long as the closure itself is reachable. If you're not careful, this can unintentionally keep large objects in memory far longer than needed.

```javascript
function attachHandler() {
  const hugeData = new Array(1000000).fill("data"); // large array

  document.getElementById("btn").addEventListener("click", function () {
    console.log("clicked"); // doesn't use hugeData...
    // ...but hugeData is still kept alive because it's in the same
    // closure scope as this handler, even though it's unused!
  });
}
```

> **Warning:** Closures can accidentally keep large objects in memory if those objects share scope with a long-lived function (like an event handler), even if the handler never actually uses them. Keep closures lean — only capture what you truly need.

## 4.15 Best Practices for Closures

- Only close over the variables you actually need.
- Avoid creating closures inside loops without understanding block scope (`let` vs `var` — see Part 9).
- Use closures deliberately for encapsulation, not by accident.
- Remove event listeners you no longer need, especially ones holding closures over large data.
- Prefer `let`/`const` in loops that create closures, since each iteration gets its own binding.

### Practice Questions — Part 4

1. In your own words, what is a closure?
2. Why doesn't `count` get destroyed after `makeCounter()` finishes running?
3. How do closures enable private variables in JavaScript?
4. What is the risk of closures and memory leaks?
5. How does the module pattern use both an IIFE and a closure together?

### Coding Exercises — Part 4

1. Build a `createCounter()` function with `increment`, `decrement`, and `reset` methods.
2. Build a `createBankAccount(balance)` function with private balance and public `deposit`/`withdraw` methods.
3. Build a `once(fn)` function that only allows `fn` to run one time, no matter how many times it's called.
4. Build a simple caching function `memoize(fn)` using a closure to store past results.
5. Write a loop using `var` that logs the wrong value due to closure behavior, then fix it using `let`.

---
# PART 5 — FIRST-CLASS FUNCTIONS

## 5.1 What Are First-Class Functions?

A programming language is said to have **first-class functions** when functions are treated like any other value — like numbers or strings. This means functions can be:

- Assigned to variables
- Stored in data structures (arrays, objects)
- Passed as arguments to other functions
- Returned as the result of another function

JavaScript treats functions as first-class citizens, which is the foundation for callbacks, array methods (`map`, `filter`, `reduce`), event handling, and the entire functional programming style available in the language.

## 5.2 Why JavaScript Functions Are First-Class

JavaScript functions are actually **objects** under the hood (of type `function`, a special callable object). Because objects can be assigned, passed, and returned freely in JavaScript, functions inherit that same flexibility automatically — no special extra rules were needed to make this possible.

## 5.3 Assigning Functions

```javascript
const sayHello = function () {
  return "Hello!";
};

console.log(sayHello()); // "Hello!"
```

## 5.4 Passing Functions (as Arguments)

```javascript
function executeTask(task) {
  console.log("Starting task...");
  task();
  console.log("Task finished.");
}

executeTask(function () {
  console.log("Doing the actual work");
});
```

## 5.5 Returning Functions

```javascript
function greetingFactory(greeting) {
  return function (name) {
    return `${greeting}, ${name}!`;
  };
}

const sayHi = greetingFactory("Hi");
console.log(sayHi("Tom")); // "Hi, Tom!"
```

## 5.6 Storing Functions

```javascript
let action = null;

if (Math.random() > 0.5) {
  action = () => console.log("Path A");
} else {
  action = () => console.log("Path B");
}

action(); // calls whichever function was stored
```

## 5.7 Functions in Arrays

```javascript
const operations = [
  x => x + 1,
  x => x * 2,
  x => x * x
];

operations.forEach(op => console.log(op(5))); // 6, 10, 25
```

## 5.8 Functions in Objects

Functions stored as object properties are called **methods**:

```javascript
const calculator = {
  add(a, b) { return a + b; },
  subtract(a, b) { return a - b; }
};

console.log(calculator.add(4, 5)); // 9
```

> **Tip:** First-class functions are *the* reason JavaScript can support callbacks, promises, array methods, and functional programming patterns. Every technique in Parts 6 and 13 relies entirely on this feature.

### Practice Questions — Part 5

1. What does it mean for functions to be "first-class citizens"?
2. Give three ways a function can be treated as a value in JavaScript.
3. Why can functions be stored inside arrays and objects?

---

# PART 6 — HIGHER ORDER FUNCTIONS

## 6.1 What Are Higher Order Functions?

A **Higher Order Function (HOF)** is a function that does at least one of the following:
- Accepts another function as an argument, **or**
- Returns a function as its result.

HOFs are only possible because JavaScript has first-class functions (Part 5).

## 6.2 Why Higher Order Functions Exist

HOFs let you **abstract behavior**, not just data. Instead of writing a separate loop for every different operation you want to perform on a list, you write one generic loop function and let the caller supply the specific behavior as a function argument.

```javascript
// Without HOFs — repeated, near-identical loops
function doubleAll(arr) {
  const result = [];
  for (let n of arr) result.push(n * 2);
  return result;
}

function squareAll(arr) {
  const result = [];
  for (let n of arr) result.push(n * n);
  return result;
}

// With a HOF — one reusable loop, behavior supplied by the caller
function transformAll(arr, transformFn) {
  const result = [];
  for (let n of arr) result.push(transformFn(n));
  return result;
}

transformAll([1, 2, 3], n => n * 2); // [2, 4, 6]
transformAll([1, 2, 3], n => n * n); // [1, 4, 9]
```

## 6.3 Functions Accepting Functions

```javascript
function repeat(times, action) {
  for (let i = 0; i < times; i++) {
    action(i);
  }
}

repeat(3, i => console.log("Iteration " + i));
```

## 6.4 Functions Returning Functions

```javascript
function greaterThan(min) {
  return function (value) {
    return value > min;
  };
}

const isAdult = greaterThan(17);
console.log(isAdult(20)); // true
console.log(isAdult(10)); // false
```

## 6.5 Callback Functions

A **callback** is a function passed into another function, to be "called back" later — often after some task completes.

```javascript
function fetchData(callback) {
  console.log("Fetching data...");
  setTimeout(() => {
    callback("Data received!");
  }, 1000);
}

fetchData(function (message) {
  console.log(message); // "Data received!" after 1 second
});
```

## 6.6 Callback Hell (Introduction)

When callbacks are nested inside other callbacks, code becomes deeply indented and hard to follow — this is nicknamed **"callback hell"**:

```javascript
getUser(1, function (user) {
  getPosts(user.id, function (posts) {
    getComments(posts[0].id, function (comments) {
      console.log(comments); // deeply nested — hard to read/maintain
    });
  });
});
```

> **Note:** This problem is one of the main reasons Promises and `async`/`await` were introduced to JavaScript (briefly covered in Part 12). Callback hell is a structural problem, not a bug — the code works, but it doesn't scale well as complexity grows.

## 6.7 Real-World Examples of HOFs

| Use Case | HOF Involved |
|---|---|
| Transforming a list of prices with tax | `array.map(addTax)` |
| Filtering active users | `array.filter(isActive)` |
| Calculating a cart total | `array.reduce(sumPrices)` |
| Sorting products by price | `array.sort(comparePrices)` |
| Handling a button click | `element.addEventListener('click', handler)` |
| Debounced search input | `debounce(searchFn, 300)` |

## 6.8 Array Higher Order Functions Introduction

JavaScript arrays come with several powerful built-in HOFs:

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.map(n => n * 2);              // [2, 4, 6, 8, 10]
numbers.filter(n => n % 2 === 0);     // [2, 4]
numbers.reduce((acc, n) => acc + n, 0); // 15
numbers.forEach(n => console.log(n)); // logs each number
numbers.find(n => n > 3);             // 4
numbers.some(n => n > 4);             // true
numbers.every(n => n > 0);            // true
```

> **Tip:** `map`, `filter`, and `reduce` are the three most important HOFs in day-to-day JavaScript. Mastering them will change how you write almost all your data-processing code.

### Practice Questions — Part 6

1. What makes a function a "higher order function"?
2. Give an example of a function that accepts a callback.
3. What is "callback hell" and why is it a problem?
4. Name three built-in array methods that are higher order functions.

### Coding Exercises — Part 6

1. Write a HOF `applyDiscount(price, discountFn)` that returns the discounted price.
2. Write your own version of `map` using a regular `for` loop (do not use the built-in `.map`).
3. Write a function `retry(fn, times)` that calls `fn` up to `times` times until it succeeds.

---
# PART 7 — THE `this` KEYWORD

## 7.1 What Is `this`?

`this` is a special keyword automatically available inside every regular function. It refers to **the object that is "executing" the current function** — but crucially, its value is determined by **how the function is called**, not where it's defined.

> **Note:** This is one of the single most misunderstood topics in JavaScript. The golden rule: **look at the call site** — the exact place and syntax used to invoke the function — to determine what `this` will be.

## 7.2 Global `this`

At the top level of a script:

```javascript
console.log(this); // In browsers: the "window" object. In Node.js modules: an empty object ({} or module.exports)
```

## 7.3 Browser vs Node.js

| Environment | Global `this` |
|---|---|
| Browser (script tag) | `window` |
| Browser (module) | `undefined` |
| Node.js (CommonJS module) | `module.exports` (an empty object by default) |
| Strict mode function (unbound) | `undefined` |

## 7.4 `this` Inside Regular Functions

```javascript
function showThis() {
  console.log(this);
}

showThis(); // In non-strict mode: the global object. In strict mode: undefined.
```

## 7.5 `this` Inside Object Methods

When a function is called *as a method* (i.e., attached to an object via dot notation), `this` refers to the object before the dot.

```javascript
const user = {
  name: "Aisha",
  greet() {
    console.log("Hello, " + this.name);
  }
};

user.greet(); // "Hello, Aisha" — this === user
```

## 7.6 `this` Inside Constructors

When a function is called with `new`, `this` refers to the brand-new object being constructed.

```javascript
function Person(name) {
  this.name = name;
}

const p1 = new Person("Leo");
console.log(p1.name); // "Leo"
```

## 7.7 `this` Inside Arrow Functions

Arrow functions do **not** have their own `this`. Instead, they inherit `this` lexically — from the surrounding (enclosing) scope where they were *written*, exactly like a normal variable.

```javascript
const user = {
  name: "Noah",
  greet: () => {
    console.log(this.name); // "this" here is NOT "user" — arrows don't bind their own this
  }
};

user.greet(); // undefined (this refers to the outer/global scope, not "user")
```

```javascript
const user = {
  name: "Noah",
  greet() {
    setTimeout(() => {
      console.log(this.name); // arrow function inherits "this" from greet() -> "user"
    }, 1000);
  }
};

user.greet(); // "Noah" after 1 second
```

> **Tip:** Arrow functions are extremely useful *inside* methods specifically because they preserve the outer `this`, fixing a very common bug (see 7.9 below).

## 7.8 `this` Inside Event Listeners

```javascript
button.addEventListener("click", function () {
  console.log(this); // "this" refers to the button element (the thing that fired the event)
});

button.addEventListener("click", () => {
  console.log(this); // arrow function — "this" is inherited from the surrounding scope, NOT the button
});
```

## 7.9 Losing `this`

A very common bug happens when you extract a method from an object and call it standalone — it "loses" its connection to the original object.

```javascript
const user = {
  name: "Priya",
  greet() {
    console.log("Hi, " + this.name);
  }
};

const greetFn = user.greet; // extracted, detached from "user"
greetFn(); // "Hi, undefined" — this is no longer "user"!
```

## 7.10 Fixing `this`

| Technique | Example |
|---|---|
| `bind()` | `const bound = user.greet.bind(user);` |
| Arrow function wrapper | `const wrapped = () => user.greet();` |
| Call directly on the object | `user.greet();` (avoid detaching in the first place) |

```javascript
const boundGreet = user.greet.bind(user);
boundGreet(); // "Hi, Priya" — this is now permanently locked to "user"
```

### Practice Questions — Part 7

1. What determines the value of `this` in a regular function?
2. Why do arrow functions not have their own `this`?
3. What happens to `this` when a method is detached from its object and called separately?
4. How does `new` affect the value of `this`?

---
# PART 8 — CALL, APPLY, BIND

## 8.1 `call()`

`call()` invokes a function immediately, letting you explicitly set what `this` should be, with arguments passed **individually**.

```javascript
function introduce(city) {
  console.log(`I'm ${this.name} from ${city}`);
}

const person = { name: "Zara" };

introduce.call(person, "Cairo"); // "I'm Zara from Cairo"
```

## 8.2 `apply()`

`apply()` works exactly like `call()`, except arguments are passed as a **single array**.

```javascript
introduce.apply(person, ["Cairo"]); // "I'm Zara from Cairo"
```

> **Tip:** A useful memory trick — "**A**pply takes an **A**rray."

## 8.3 `bind()`

`bind()` does **not** invoke the function immediately. Instead, it returns a **new function** with `this` permanently locked to whatever you specify. You can call that new function whenever you want.

```javascript
const boundIntroduce = introduce.bind(person);
boundIntroduce("Cairo"); // "I'm Zara from Cairo" — can be called anytime, "this" is locked
```

## 8.4 Differences Between call, apply, and bind

| Method | Invokes Immediately? | Argument Format | Returns |
|---|---|---|---|
| `call()` | Yes | Comma-separated list | The function's result |
| `apply()` | Yes | Array | The function's result |
| `bind()` | No | Comma-separated list | A new bound function |

## 8.5 Real-World Examples

```javascript
// Using apply() to find the max of an array (pre-spread-operator technique)
const numbers = [5, 2, 9, 1];
console.log(Math.max.apply(null, numbers)); // 9

// Modern equivalent using spread
console.log(Math.max(...numbers)); // 9
```

```javascript
// bind() used to preset arguments (partial application)
function multiply(a, b) {
  return a * b;
}

const double = multiply.bind(null, 2); // locks the first argument to 2
console.log(double(5)); // 10
```

## 8.6 Method Borrowing

You can "borrow" a method from one object and use it on another, unrelated object using `call`/`apply`.

```javascript
const person1 = { name: "Alex", greet() { console.log("Hi, I'm " + this.name); } };
const person2 = { name: "Sam" };

person1.greet.call(person2); // "Hi, I'm Sam" — borrowed person1's method
```

## 8.7 Function Borrowing (Array-like Objects)

A classic real-world use: converting `arguments` (an array-like object, not a true array) into a real array by borrowing Array's methods.

```javascript
function listArgs() {
  const argsArray = Array.prototype.slice.call(arguments);
  console.log(argsArray);
}

listArgs(1, 2, 3); // [1, 2, 3]

// Modern equivalent:
function listArgsModern(...args) {
  console.log(args);
}
```

### Practice Questions — Part 8

1. What's the key difference between `call()` and `apply()`?
2. Why does `bind()` not run the function immediately?
3. Give a real-world scenario where method borrowing is useful.

---

# PART 9 — FUNCTION HOISTING

## 9.1 Hoisting

**Hoisting** is JavaScript's behavior of moving *declarations* (not their assigned values) to the top of their scope during the memory creation phase, before any code actually executes.

## 9.2 Function Hoisting

Function **declarations** are fully hoisted — both their name and their entire body — so they can be called before their line in the source code.

```javascript
sayHi(); // "Hi!" — works, even though called before the declaration below

function sayHi() {
  console.log("Hi!");
}
```

## 9.3 Function Expression Hoisting

Function **expressions** are not fully hoisted the same way. Only the variable declaration is hoisted (as `undefined` for `var`), not the function assignment.

```javascript
sayBye(); // TypeError: sayBye is not a function (it's undefined at this point)

var sayBye = function () {
  console.log("Bye!");
};
```

## 9.4 Arrow Function Hoisting

Arrow functions assigned to `let`/`const` behave the same way — the variable exists in a "Temporal Dead Zone" until its declaration line runs.

```javascript
sayHello(); // ReferenceError: Cannot access 'sayHello' before initialization

const sayHello = () => console.log("Hello!");
```

## 9.5 Temporal Dead Zone (TDZ)

The **Temporal Dead Zone** is the period between entering a scope and the actual declaration line where a `let`/`const` variable exists but cannot yet be accessed. Accessing it during this period throws a `ReferenceError`.

```
Scope starts
   |
   |  <-- TDZ for "let x" begins here (x exists but is inaccessible)
   |
let x = 10;   <-- TDZ ends here; x becomes usable
   |
console.log(x); // 10 — safe to access now
```

## 9.6 Common Mistakes with Hoisting

- Assuming function expressions behave like function declarations regarding hoisting.
- Relying on `var` hoisting to use a variable before its declaration (leads to `undefined`, not an error, which can hide bugs).
- Forgetting that `let`/`const` are hoisted too, just left in the TDZ, unlike a popular myth that they aren't hoisted at all.

> **Tip:** A safe rule of thumb for maintainable code: **always declare functions and variables before using them**, regardless of what hoisting technically allows.

### Practice Questions — Part 9

1. Why can you call a function declaration before its line in the code, but not a function expression?
2. What is the Temporal Dead Zone, and which keywords are affected by it?
3. Is `let` hoisted? Explain your answer.

---
# PART 10 — EXECUTION CONTEXT

## 10.1 What Is an Execution Context?

An **execution context** is the environment in which JavaScript code is evaluated and run. It contains information about variables, function declarations, and the value of `this` for that particular piece of code. Every time a function is called, a brand-new execution context is created for it.

## 10.2 Global Execution Context

Created once, when your script first starts running. It sets up the global object (`window` in browsers, `global` in Node), sets `this` at the top level, and hoists global variables/functions.

## 10.3 Function Execution Context

Created every single time a function is called. Each call gets its **own** fresh context, with its own local variables, arguments, and `this` binding.

## 10.4 Memory Creation Phase (a.k.a. Creation Phase)

Before any code actually runs, JavaScript scans the current context and:
1. Sets up memory for variables (`var` → `undefined`; `let`/`const` → uninitialized/TDZ).
2. Fully hoists function declarations.
3. Determines the value of `this`.
4. Sets up the scope chain reference to the outer environment.

## 10.5 Execution Phase

After the creation phase, JavaScript runs the code line-by-line, assigning real values to variables and executing statements in order.

## 10.6 Variable Environment

The **Variable Environment** is the part of an execution context that stores variable and function declarations for that context.

## 10.7 Scope Chain (Recap in Context)

Each execution context keeps a reference to the execution context that created it, forming the scope chain used to resolve variables that aren't found locally (see Part 3.7).

## 10.8 `this` Binding (Recap in Context)

Each function execution context determines its own `this` value, following the rules explained in Part 7.

## 10.9 Internal JavaScript Engine Flow

```
1. Global Execution Context created
   |
   2. Creation Phase: hoist vars/functions, set up "this"
   |
   3. Execution Phase: run code line by line
   |
   4. Function call encountered --> NEW Execution Context pushed onto the Call Stack
         |
         5. Creation Phase for THIS function
         |
         6. Execution Phase for THIS function
         |
         7. Function returns --> Execution Context popped off the Call Stack
   |
   8. Continue Global Execution
```

### Practice Questions — Part 10

1. What is the difference between the creation phase and the execution phase?
2. What gets set up in an execution context before any code runs?
3. How many execution contexts exist while three nested function calls are in progress?

---

# PART 11 — THE CALL STACK

## 11.1 What Is the Call Stack?

The **call stack** is a data structure JavaScript uses to keep track of function calls — specifically, which function is currently running, and what should run next once it finishes. It follows a **Last In, First Out (LIFO)** principle: the most recently called function is the first one to finish and be removed.

## 11.2 Stack Memory

Every function call pushes a new execution context frame onto the stack. When the function returns, its frame is popped off, and control returns to whatever called it.

```
callStack.push(functionA_context)
callStack.push(functionB_context)  // called from inside A
callStack.push(functionC_context)  // called from inside B
   |
   v  (C finishes and returns)
callStack.pop() -> back in B
   |
   v  (B finishes and returns)
callStack.pop() -> back in A
   |
   v  (A finishes and returns)
callStack.pop() -> back to global context
```

## 11.3 Function Calls Visualized

```javascript
function a() {
  b();
  console.log("a done");
}
function b() {
  c();
  console.log("b done");
}
function c() {
  console.log("c done");
}

a();

// Call Stack over time:
// [a]
// [a, b]
// [a, b, c]
// [a, b]        <- c() finished, popped
// [a]           <- b() finished, popped
// []            <- a() finished, popped

// Console Output:
// "c done"
// "b done"
// "a done"
```

## 11.4 Nested Calls

Nested function calls simply keep pushing new frames onto the stack, one on top of the last, until the innermost call finishes first.

## 11.5 Recursion in the Call Stack

Each recursive call adds a **new** frame to the stack, even though it's the "same" function being called.

```javascript
function countdown(n) {
  if (n === 0) return;
  console.log(n);
  countdown(n - 1); // each call adds a new stack frame
}

countdown(3);
// Stack grows: [countdown(3)] -> [countdown(3), countdown(2)] -> [countdown(3), countdown(2), countdown(1)] -> [.., countdown(0)]
// Then unwinds as each call returns.
```

## 11.6 Stack Overflow

If recursion never reaches a base case, the call stack keeps growing until it exceeds the engine's maximum size, causing a crash:

```javascript
function neverStops() {
  neverStops();
}

neverStops(); // RangeError: Maximum call stack size exceeded
```

## 11.7 Debugging the Stack

Browser DevTools show a **stack trace** whenever an error is thrown — a snapshot of exactly which function called which, in order, at the moment of the crash. Reading stack traces from top to bottom shows you the most recent call first, helping you trace the bug back to its origin.

> **Tip:** Naming your functions (instead of leaving everything anonymous) makes stack traces vastly easier to read when debugging real applications.

### Practice Questions — Part 11

1. What does LIFO mean, and how does it apply to the call stack?
2. Why does deep recursion without a base case cause a crash?
3. Trace the call stack for three nested function calls, showing pushes and pops.

---
# PART 12 — ADVANCED FUNCTIONS

## 12.1 Generator Functions

A **generator function** can pause its own execution partway through and resume later, producing a sequence of values over time instead of all at once. Declared with `function*`.

```javascript
function* numberGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = numberGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: undefined, done: true }
```

## 12.2 `yield`

The `yield` keyword pauses the generator and sends a value out to whoever called `.next()`. Execution resumes right after that `yield` the next time `.next()` is called.

```javascript
function* countUpTo(max) {
  for (let i = 1; i <= max; i++) {
    yield i;
  }
}

for (const num of countUpTo(3)) {
  console.log(num); // 1, 2, 3
}
```

## 12.3 Iterators

Generators automatically implement the **iterator protocol**, meaning they can be used with `for...of` loops, spread syntax, and destructuring — anything that expects an iterable.

```javascript
console.log([...countUpTo(4)]); // [1, 2, 3, 4]
```

## 12.4 Async Functions (Introduction)

An `async` function always returns a **Promise**, and lets you use the `await` keyword inside it to pause execution until a Promise resolves — making asynchronous code read like ordinary, synchronous code.

```javascript
async function fetchUserName() {
  const response = await fetch("/api/user"); // pauses here until the fetch resolves
  const data = await response.json();
  return data.name;
}
```

> **Note:** Promises and `async`/`await` are large topics of their own, fully explored in a dedicated Async JavaScript guide. This section only introduces how they relate to function syntax.

## 12.5 Function Constructors

Every regular function you write is automatically usable as a constructor with the `new` keyword, which creates a new object and sets `this` to that object.

```javascript
function Car(brand) {
  this.brand = brand;
}

const myCar = new Car("Toyota");
console.log(myCar.brand); // "Toyota"
```

## 12.6 `new Function()`

JavaScript also allows creating a function dynamically from a string of code using the `Function` constructor directly — though this is rarely used in practice.

```javascript
const add = new Function("a", "b", "return a + b;");
console.log(add(2, 3)); // 5
```

> **Warning:** `new Function()` (like `eval()`) executes code from a string, which can introduce serious security risks if that string comes from an untrusted source. Avoid it in real applications.

## 12.7 Dynamic Functions

"Dynamic" simply means a function is generated or configured at runtime rather than written directly in the source code — for example, functions returned by factories (Part 2.18), or functions built with `bind()` to preset certain arguments.

### Practice Questions — Part 12

1. What's the difference between a regular function and a generator function?
2. What does `yield` do inside a generator?
3. Why does an `async` function always return a Promise?
4. Why is `new Function()` considered risky?

---

# PART 13 — FUNCTIONAL PROGRAMMING

## 13.1 Pure Functions

A **pure function** always returns the same output for the same input, and produces no observable side effects (it doesn't modify anything outside itself).

```javascript
function add(a, b) {
  return a + b; // pure — same inputs always give same output, nothing external is touched
}
```

## 13.2 Impure Functions

An **impure function** either depends on external state, modifies external state, or produces different results for the same inputs.

```javascript
let total = 0;

function addToTotal(n) {
  total += n; // impure — modifies a variable outside the function (a "side effect")
  return total;
}
```

| | Pure Function | Impure Function |
|---|---|---|
| Same input → same output? | Always | Not guaranteed |
| Side effects? | None | Possibly (logging, mutating external state, network calls) |
| Easy to test? | Very easy | Harder — depends on external state |
| Predictable? | Yes | No |

## 13.3 Side Effects

A **side effect** is any interaction a function has with the world *outside* its own scope: modifying a global variable, mutating an argument object, logging to the console, making a network request, or changing the DOM.

```javascript
function impureExample(arr) {
  arr.push(4); // side effect — mutates the caller's original array
  console.log("Logged!"); // side effect — interacts with the console
}
```

## 13.4 Function Composition

**Composition** means building a new function by combining two or more smaller functions, where the output of one becomes the input of the next.

```javascript
const double = x => x * 2;
const increment = x => x + 1;

const compose = (f, g) => x => f(g(x));

const doubleThenIncrement = compose(increment, double);
console.log(doubleThenIncrement(5)); // double(5)=10, then increment(10)=11
```

## 13.5 Currying

**Currying** transforms a function that takes multiple arguments into a sequence of functions that each take a single argument.

```javascript
function add(a) {
  return function (b) {
    return function (c) {
      return a + b + c;
    };
  };
}

console.log(add(1)(2)(3)); // 6
```

## 13.6 Partial Application

**Partial application** creates a new function by pre-filling some of the arguments of an existing function, leaving the rest to be supplied later.

```javascript
function multiply(a, b, c) {
  return a * b * c;
}

const double = multiply.bind(null, 2);       // "a" is pre-filled as 2
console.log(double(3, 4)); // 2 * 3 * 4 = 24
```

| | Currying | Partial Application |
|---|---|---|
| Structure | Chain of one-argument functions | One function call, some arguments pre-filled |
| Arguments per call | Always exactly one | Any number |
| Goal | Break a function into single-argument steps | Reuse a function with certain fixed inputs |

## 13.7 Memoization

**Memoization** is an optimization technique that caches a function's previous results, so repeated calls with the same input return instantly instead of recalculating.

```javascript
function memoize(fn) {
  const cache = new Map();

  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) {
      return cache.get(key); // return cached result
    }
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

function slowSquare(n) {
  for (let i = 0; i < 1e8; i++) {} // simulate slow work
  return n * n;
}

const fastSquare = memoize(slowSquare);
console.log(fastSquare(5)); // slow the first time
console.log(fastSquare(5)); // instant — served from cache
```

## 13.8 Immutability

**Immutability** means never modifying data directly — instead, you create a new copy with the changes applied. This avoids unpredictable bugs caused by shared, mutated state.

```javascript
// Mutating (avoid in functional style)
function addItemMutable(cart, item) {
  cart.push(item); // modifies the original array
  return cart;
}

// Immutable (preferred in functional style)
function addItemImmutable(cart, item) {
  return [...cart, item]; // returns a brand-new array
}

const original = ["Apple"];
const updated = addItemImmutable(original, "Bread");
console.log(original); // ["Apple"] — untouched
console.log(updated);  // ["Apple", "Bread"]
```

### Practice Questions — Part 13

1. What are the two defining traits of a pure function?
2. Give an example of a side effect that makes a function impure.
3. What is the difference between currying and partial application?
4. Why does memoization only work well for pure functions?
5. Why is immutability valued in functional programming?

### Coding Exercises — Part 13

1. Convert an impure `addToCart` function into a pure one that returns a new array.
2. Write a curried function `volume(l)(w)(h)` that returns `l * w * h`.
3. Write a `memoize` function and use it to cache Fibonacci calculations.
4. Write `compose(...fns)` that accepts any number of functions and composes them all.

---
# PART 14 — PERFORMANCE

## 14.1 Debouncing

**Debouncing** delays running a function until a certain amount of time has passed *without* it being triggered again — useful for things like search-as-you-type, where you only want to fire a request once the user stops typing.

```javascript
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);           // cancel the previous scheduled call
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}

const searchAPI = debounce(query => {
  console.log("Searching for:", query);
}, 500);

searchAPI("a");
searchAPI("ap");
searchAPI("app"); // only this call actually runs, 500ms after the last keystroke
```

**How it works internally:**

```
Keystroke -> schedule call in 500ms
Keystroke -> cancel previous timer, schedule a NEW call in 500ms
Keystroke -> cancel previous timer, schedule a NEW call in 500ms
... (user stops typing) ...
500ms pass with no new keystrokes -> the last scheduled call finally runs
```

## 14.2 Throttling

**Throttling** ensures a function runs **at most once** within a given time window, no matter how many times it's triggered — useful for scroll or resize event handlers, which can fire hundreds of times per second.

```javascript
function throttle(fn, limit) {
  let waiting = false;
  return function (...args) {
    if (!waiting) {
      fn.apply(this, args);
      waiting = true;
      setTimeout(() => { waiting = false; }, limit);
    }
  };
}

const logScroll = throttle(() => {
  console.log("Scroll position logged");
}, 1000);

window.addEventListener("scroll", logScroll); // runs at most once per second
```

| | Debounce | Throttle |
|---|---|---|
| Fires... | Only after activity stops for a set delay | At most once per fixed time interval, even during continuous activity |
| Best for | Search inputs, resize-end detection | Scroll handlers, drag events, rapid button clicks |

## 14.3 Lazy Evaluation

**Lazy evaluation** delays computing a value until it's actually needed, avoiding unnecessary work.

```javascript
function lazyValue(computeFn) {
  let cached;
  let computed = false;

  return function () {
    if (!computed) {
      cached = computeFn(); // only runs the very first time it's needed
      computed = true;
    }
    return cached;
  };
}

const getExpensiveResult = lazyValue(() => {
  console.log("Computing...");
  return 42;
});

getExpensiveResult(); // logs "Computing..." then returns 42
getExpensiveResult(); // returns 42 instantly, no recomputation
```

Generators (Part 12.1) are also a form of lazy evaluation — values are only produced one at a time, on demand.

## 14.4 Optimization Tips

- Avoid creating new functions inside frequently-run loops or render cycles when possible (define them once, outside).
- Use memoization for expensive, pure calculations that repeat with the same inputs.
- Debounce or throttle handlers tied to high-frequency events (scroll, resize, keypress).
- Avoid deep, unnecessary recursion — consider iterative solutions for very large inputs.
- Keep functions small and focused, which the JavaScript engine can optimize more effectively.

### Practice Questions — Part 14

1. What is the core difference between debouncing and throttling?
2. Give a real-world UI scenario best suited to debouncing.
3. Give a real-world UI scenario best suited to throttling.
4. How does lazy evaluation improve performance?

---

# PART 15 — BEST PRACTICES

## 15.1 Naming Conventions

- Use descriptive, verb-based names for functions: `calculateTotal`, `isValidEmail`, `fetchUserData`.
- Use `camelCase` for function names in JavaScript.
- Boolean-returning functions should read like yes/no questions: `isActive()`, `hasPermission()`, `canEdit()`.

## 15.2 Single Responsibility Principle

Each function should do **one thing**, and do it well. If you find yourself describing a function using the word "and" (e.g., "this validates the form *and* submits it *and* logs analytics"), it's likely doing too much and should be split.

```javascript
// Avoid: one function doing everything
function processOrder(order) {
  validateOrder(order);
  calculateTotal(order);
  saveToDatabase(order);
  sendConfirmationEmail(order);
}

// Prefer: one small function per responsibility, composed together
function processOrder(order) {
  if (!validateOrder(order)) return;
  const total = calculateTotal(order);
  saveToDatabase({ ...order, total });
  sendConfirmationEmail(order);
}
```

## 15.3 Small Functions

Smaller functions are easier to read, test, name accurately, and reuse elsewhere. As a rough guideline, if a function body is growing past 20-30 lines, consider whether it can be split into smaller named pieces.

## 15.4 Reusable Functions

Write functions general enough to be useful in more than one place, but not so generic that they become hard to understand. Avoid hardcoding values that should be parameters.

```javascript
// Too specific
function getDiscountedApplePrice() {
  return 100 * 0.9;
}

// Reusable
function getDiscountedPrice(price, discountRate) {
  return price * (1 - discountRate);
}
```

## 15.5 Avoid Global Variables

Global variables can be modified from anywhere, making bugs hard to trace. Prefer local variables, function parameters, module scope, or closures (Part 4) instead.

## 15.6 Prefer Pure Functions

Pure functions (Part 13.1) are easier to test, debug, and reason about because they don't depend on or modify anything outside themselves.

## 15.7 Readability

- Keep consistent indentation and spacing.
- Prefer clarity over cleverness — a slightly longer, obvious solution often beats a short, cryptic one.
- Use early returns to avoid deeply nested `if` blocks.

```javascript
// Deeply nested — harder to read
function getDiscount(user) {
  if (user) {
    if (user.isPremium) {
      return 0.2;
    } else {
      return 0.1;
    }
  } else {
    return 0;
  }
}

// Early returns — flatter and clearer
function getDiscount(user) {
  if (!user) return 0;
  if (user.isPremium) return 0.2;
  return 0.1;
}
```

## 15.8 Documentation

Use comments (or JSDoc) to explain **why**, not just **what**, especially for non-obvious logic.

```javascript
/**
 * Calculates the shipping cost based on weight and destination zone.
 * @param {number} weightKg - Package weight in kilograms.
 * @param {string} zone - Shipping zone code (e.g., "A", "B", "C").
 * @returns {number} The calculated shipping cost.
 */
function calculateShipping(weightKg, zone) {
  // Zone C has higher base rates due to remote delivery logistics
  const baseRates = { A: 5, B: 8, C: 15 };
  return baseRates[zone] + weightKg * 0.5;
}
```

### Practice Questions — Part 15

1. Why is the Single Responsibility Principle important for functions?
2. What's a practical downside of relying heavily on global variables?
3. Why might "clever" one-line code sometimes be worse than a clearer, longer version?

---
# PART 16 — COMMON MISTAKES

Below are 25 mistakes beginners commonly make with JavaScript functions, along with explanations of why they happen and how to fix them.

| # | Mistake | Why It Happens | Fix |
|---|---|---|---|
| 1 | Forgetting `()` to call a function | Confusing a function reference with an invocation | Always add `()` to actually run the function: `greet()` not `greet` |
| 2 | Confusing parameters and arguments | Not understanding the definition vs. call-site distinction | Parameters are placeholders in the definition; arguments are actual values passed in |
| 3 | Expecting `x => { x * 2 }` to return a value | Forgetting that braces require an explicit `return` | Use `x => x * 2` or `x => { return x * 2; }` |
| 4 | Writing infinite recursion | Missing or unreachable base case | Always verify the base case is guaranteed to be reached |
| 5 | Using `arguments` inside an arrow function | Arrow functions don't have their own `arguments` object | Use a regular function, or use rest parameters `(...args)` |
| 6 | Assuming function expressions hoist like declarations | Confusing the two different hoisting behaviors | Declare function expressions before using them |
| 7 | Losing `this` when passing a method as a callback | Detaching a method from its object removes its binding | Use `.bind()`, an arrow function wrapper, or call directly on the object |
| 8 | Using `this` inside an arrow function expecting it to bind to the caller | Arrow functions inherit `this` lexically, not dynamically | Use a regular function when you need dynamic `this` |
| 9 | Mutating a parameter object directly | Objects/arrays are passed by reference | Return a new copy instead of mutating the original |
| 10 | Believing `let`/`const` are not hoisted at all | Confusing "not hoisted" with "hoisted but in the Temporal Dead Zone" | Understand the TDZ — they are hoisted, just inaccessible until declared |
| 11 | Forgetting default parameters only trigger on `undefined` | Assuming any falsy value (like `0`) triggers the default | Remember only `undefined` triggers a default parameter |
| 12 | Overusing global variables inside functions | Convenience over structure | Pass values as parameters or use closures instead |
| 13 | Writing overly long functions doing many unrelated things | Not applying the Single Responsibility Principle | Break the function into smaller, focused functions |
| 14 | Not returning a value and expecting one | Forgetting the `return` keyword entirely | Double-check every code path returns what's expected |
| 15 | Creating closures inside a loop using `var` | `var` is function-scoped, so all closures share the same variable | Use `let` instead, which creates a new binding per iteration |
| 16 | Calling `bind()` and expecting immediate execution | Confusing `bind()` with `call()`/`apply()` | Remember `bind()` returns a new function; it doesn't run immediately |
| 17 | Using `apply()` with a comma-separated argument list | Confusing `apply()` (array) with `call()` (individual arguments) | Use an array with `apply()`, or switch to `call()` |
| 18 | Writing a memoized function around an impure function | Memoization assumes pure, consistent output for given inputs | Only memoize pure functions |
| 19 | Nesting many callbacks ("callback hell") | Not using Promises/async-await for asynchronous flows | Refactor with Promises or `async`/`await` |
| 20 | Forgetting `new` when calling a constructor function | Easy to forget the keyword | Use `class` syntax, or carefully remember `new`, to avoid silently broken `this` |
| 21 | Comparing functions with `==` expecting semantic equality | Functions are compared by reference, not by their code content | Understand that two functions with identical code are still different objects |
| 22 | Believing recursion is always better than loops | Overusing recursion for simple iteration | Use recursion where it improves clarity (trees, nested structures); use loops for simple counting |
| 23 | Ignoring stack overflow risk in deep recursion | Not considering call stack limits for large inputs | Consider iterative approaches or tail-call-style patterns for very large inputs |
| 24 | Shadowing an outer variable unintentionally | Reusing a common name like `data` or `value` in nested scopes | Use distinct, descriptive names, especially in nested functions |
| 25 | Not understanding those functions are objects too | Assuming functions are only "actions", not values | Remember functions can have their own properties and be passed around like any other value |

> **Tip:** Nearly all of these mistakes trace back to a shaky understanding of Parts 2, 3, 4, and 7 — basics, scope, closures, and `this`. Revisiting those sections resolves most function-related bugs you'll encounter.

---
# PART 17 — INTERVIEW QUESTIONS

Fifty commonly asked JavaScript function interview questions, with concise, accurate answers.

**1. What is a function in JavaScript?**
A reusable block of code that performs a specific task, defined once and callable multiple times.

**2. What is the difference between a function declaration and a function expression?**
A declaration (`function foo(){}`) is hoisted fully; an expression (`const foo = function(){}`) is only hoisted as a variable, not with its assigned value.

**3. What is a parameter versus an argument?**
A parameter is the placeholder name in the function definition; an argument is the actual value passed when calling the function.

**4. What does `return` do?**
It stops function execution and sends a value back to the caller. Without it, a function returns `undefined`.

**5. What are default parameters?**
Values assigned to parameters that are used only when the argument passed is `undefined`.

**6. What are rest parameters?**
A syntax (`...args`) that collects all remaining arguments into a real array.

**7. What is the difference between rest and spread?**
Rest collects multiple values into an array; spread expands an array/object into individual values.

**8. What is an anonymous function?**
A function with no name, often used as a callback or passed as an argument.

**9. What is an arrow function, and how is it different from a regular function?**
A shorter function syntax (ES6) that does not have its own `this`, `arguments`, or `super`, and cannot be used as a constructor.

**10. What is implicit return in an arrow function?**
When an arrow function has no curly braces, the expression's result is automatically returned without the `return` keyword.

**11. What is a first-class function?**
A function treated as a value — it can be assigned, passed as an argument, stored in data structures, and returned from other functions.

**12. What is a higher-order function?**
A function that accepts another function as an argument, returns a function, or both.

**13. What is a callback function?**
A function passed into another function to be executed later, often after some operation completes.

**14. What is "callback hell"?**
Deeply nested callbacks that make code hard to read and maintain, often resolved by using Promises or `async`/`await`.

**15. What is a closure?**
A function that retains access to variables from its outer (enclosing) scope, even after that outer function has finished executing.

**16. Why are closures useful?**
They enable private variables, data encapsulation, the module pattern, memoization, and function factories.

**17. Can closures cause memory leaks?**
Yes — if a closure keeps a reference to large, unused data, that data cannot be garbage collected as long as the closure is reachable.

**18. What is scope?**
The region of code where a variable or function name is accessible.

**19. What is the difference between global, function, and block scope?**
Global scope is accessible everywhere; function scope is limited to inside a function (`var`); block scope is limited to the nearest `{}` (`let`/`const`).

**20. What is lexical scope?**
A function's variable access is determined by where it is physically written in the code, not by where it's called from.

**21. What is the scope chain?**
The sequence of nested scopes JavaScript searches through, from innermost to outermost, to resolve a variable name.

**22. What is variable shadowing?**
When an inner-scope variable has the same name as an outer-scope variable, temporarily hiding the outer one within that inner scope.

**23. What is hoisting?**
JavaScript's behavior of moving variable and function declarations to the top of their scope during the creation phase, before code executes.

**24. Are function expressions hoisted the same way as function declarations?**
No — only the variable name is hoisted (as `undefined` for `var`), not the function body itself.

**25. What is the Temporal Dead Zone?**
The period between entering a scope and a `let`/`const` variable's actual declaration line, during which accessing the variable throws a `ReferenceError`.

**26. What is the `this` keyword?**
A reference to the object executing the current function, determined by how the function is called (the call site).

**27. How does `this` behave differently in arrow functions vs regular functions?**
Regular functions get their own dynamic `this` based on the call site; arrow functions inherit `this` lexically from their surrounding scope.

**28. How do you fix a function that has "lost" its `this`?**
Use `.bind()`, wrap the call in an arrow function, or call the method directly on its owning object.

**29. What does `call()` do?**
Immediately invokes a function with a specified `this` value and individually listed arguments.

**30. What does `apply()` do?**
Immediately invokes a function with a specified `this` value and arguments passed as an array.

**31. What does `bind()` do?**
Returns a new function with `this` permanently set, without invoking it immediately.

**32. What is method borrowing?**
Using `call`/`apply` to run a method that belongs to one object on a different, unrelated object.

**33. What is an IIFE, and why is it used?**
An Immediately Invoked Function Expression — a function that runs as soon as it's defined, historically used to create isolated, private scopes before ES6 modules existed.

**34. What is recursion?**
A technique where a function calls itself to solve smaller sub-problems, until it reaches a base case.

**35. What happens if a recursive function has no base case?**
It calls itself indefinitely until the call stack overflows, throwing a `RangeError`.

**36. What is the call stack?**
A Last In, First Out (LIFO) structure that tracks function calls — which function is running and what should resume once it finishes.

**37. What causes a "stack overflow"?**
Too many nested function calls (often from unterminated recursion) exceeding the engine's maximum call stack size.

**38. What is an execution context?**
The environment in which code is evaluated, including variable storage, the scope chain, and the value of `this`.

**39. What's the difference between the creation phase and execution phase of an execution context?**
The creation phase sets up hoisting, `this`, and the scope chain before running anything; the execution phase actually runs the code line by line.

**40. What is a generator function?**
A function (`function*`) that can pause and resume execution, producing a sequence of values over time using `yield`.

**41. What does the `yield` keyword do?**
It pauses a generator function and returns a value to the caller, resuming from that point on the next `.next()` call.

**42. What is a pure function?**
A function that always returns the same output for the same input and has no observable side effects.

**43. What is a side effect in the context of functions?**
Any interaction with state outside the function's own scope — such as modifying a global variable, mutating an argument, or logging output.

**44. What is function composition?**
Combining two or more functions so that the output of one becomes the input of the next, forming a new function.

**45. What is currying?**
Transforming a function that takes multiple arguments into a chain of functions that each take exactly one argument.

**46. What is partial application?**
Creating a new function by pre-filling some arguments of an existing function, leaving the rest to be supplied later.

**47. What is memoization, and when should you use it?**
An optimization technique that caches a function's results for given inputs; best used on pure, expensive-to-compute functions.

**48. What is the difference between debouncing and throttling?**
Debouncing waits for a pause in activity before running; throttling limits execution to at most once per fixed time interval.

**49. Why can't you compare two functions for logical equality with `==`?**
Functions are compared by reference (identity), not by the similarity of their code, so two functions with identical bodies are still considered different.

**50. Why should functions ideally do just "one thing" (Single Responsibility Principle)?**
Smaller, focused functions are easier to test, name accurately, reuse, and debug than large functions handling multiple unrelated responsibilities.

---
# PART 18 — PRACTICE

## 18.1 — 30 Practice Questions

1. Explain the difference between a function declaration and a function expression in your own words.
2. What will `typeof functionName` return for any function?
3. Why is it best practice to avoid modifying a parameter object directly?
4. What is the output of calling an arrow function method that uses `this.name` on an object?
5. Explain how default parameters differ from the old `||` fallback trick.
6. When would you choose rest parameters over the `arguments` object?
7. What's the difference between `null` and `undefined` as a function's return value?
8. Describe how the scope chain resolves a variable that doesn't exist locally.
9. Why does a `for` loop using `var` with a `setTimeout` callback log unexpected values?
10. How does `let` fix the classic `var`-in-a-loop closure bug?
11. What's the difference between shadowing and simply reusing a variable name in separate, unrelated scopes?
12. Why are closures described as "functions with memory"?
13. Give two real-world examples of the module pattern.
14. Why is data privacy hard to achieve without closures or classes?
15. What is the risk of forgetting to remove an event listener that closes over large data?
16. List three built-in higher-order array methods and what they do.
17. What is the fundamental cause of "callback hell"?
18. Why can arrow functions not be used as object methods that rely on dynamic `this`?
19. Explain, step by step, what happens when you call `fn.bind(obj)()`.
20. Why does method borrowing work at all in JavaScript?
21. Describe the Temporal Dead Zone using a short code example.
22. What determines whether hoisting a function will let you call it before its line of code?
23. Explain execution context creation vs execution phases using an analogy.
24. Why does deep, unbounded recursion eventually crash a program?
25. What is the purpose of `yield` in a generator function?
26. Why must an `async` function always return a Promise?
27. Give an example of an impure function and explain what makes it impure.
28. Explain the difference between currying and normal multi-argument functions.
29. When is memoization a bad idea?
30. Why is debouncing preferred over throttling for a live search box?

## 18.2 — 20 Coding Exercises

1. Write a function `isPalindrome(str)` that returns `true` if a string reads the same backward and forward.
2. Write a function `reverseString(str)` without using the built-in `.reverse()`.
3. Write a recursive function `power(base, exponent)` that computes `base^exponent`.
4. Write a function `flattenArray(arr)` that flattens a nested array one level deep.
5. Write a higher-order function `filterBy(arr, predicateFn)` that mimics `.filter()`.
6. Write a function `uniqueValues(arr)` that returns only the unique values from an array.
7. Write a closure-based `createIdGenerator()` that returns a new unique ID each time it's called (1, 2, 3, ...).
8. Write a `debounce(fn, delay)` function from scratch.
9. Write a `throttle(fn, limit)` function from scratch.
10. Write a `curry(fn)` helper that automatically curries any 3-argument function.
11. Write a `compose(...fns)` function that composes any number of unary functions.
12. Write a `pipe(...fns)` function (like compose, but left-to-right).
13. Write a `memoize(fn)` helper and apply it to a slow Fibonacci function.
14. Write a function `deepClone(obj)` for a simple nested object (no functions or circular references).
15. Write a function `groupBy(arr, keyFn)` that groups array items by a key returned from `keyFn`.
16. Write a generator function `fibonacciGenerator()` that yields an infinite Fibonacci sequence.
17. Write a function `retryAsync(fn, attempts)` that retries an async function a set number of times.
18. Write a function `chunkArray(arr, size)` that splits an array into smaller arrays of a given size.
19. Write a `pipeline` of functions to validate a form object step by step, short-circuiting on the first failure.
20. Write a `bindAll(obj, methodNames)` utility that binds several methods of an object to that object at once.

## 18.3 — 10 Debugging Questions

For each snippet, identify the bug and explain the fix.

**1.**
```javascript
function greet(name) {
  console.log("Hello " + name;
}
```
*Bug:* Missing closing parenthesis on the `console.log` call.

**2.**
```javascript
const square = x => { x * x };
console.log(square(4)); // undefined
```
*Bug:* Block body without an explicit `return`. Fix: `x => x * x` or `x => { return x * x; }`.

**3.**
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// logs 3, 3, 3 instead of 0, 1, 2
```
*Bug:* `var` is function-scoped, so all callbacks share the same `i`. Fix: use `let`.

**4.**
```javascript
const user = { name: "Kim", greet: () => console.log(this.name) };
user.greet(); // undefined
```
*Bug:* Arrow function methods don't bind `this` to the object. Fix: use a regular method shorthand `greet() {...}`.

**5.**
```javascript
function factorial(n) {
  return n * factorial(n - 1);
}
```
*Bug:* Missing base case — infinite recursion leading to a stack overflow. Fix: add `if (n <= 1) return 1;`.

**6.**
```javascript
const fn = user.greet;
fn(); // "this" is lost
```
*Bug:* Detaching a method from its object loses its `this` binding. Fix: use `.bind(user)` or call `user.greet()` directly.

**7.**
```javascript
function add(a, b = a) {
  return a + b;
}
console.log(add(5)); // works, but is this intended?
```
*Not a bug per se, but a trap:* default parameters can reference earlier parameters — confirm this is the intended behavior, since it's an uncommon but valid pattern.

**8.**
```javascript
sayHi();
const sayHi = () => console.log("hi");
```
*Bug:* `const` is in the Temporal Dead Zone until its declaration line. Fix: declare `sayHi` before calling it.

**9.**
```javascript
function makeAdder(x) {
  return y => x + y;
}
const add5 = makeAdder(5);
console.log(add5); // logs the function itself, not a number
```
*Not exactly a bug:* `add5` is a function, and needs to be called: `add5(10)` to get `15`.

**10.**
```javascript
const numbers = [1, 2, 3];
numbers.forEach(n => n * 2); // expecting doubled values, but nothing happens
```
*Bug:* `.forEach()` does not return or collect values. Fix: use `.map()` instead if you need the transformed array.

---

# PART 19 — MINI PROJECTS

Each project below is a small, complete, function-driven program demonstrating multiple concepts from this guide working together.

## 19.1 Calculator

```javascript
function calculator(a, b, operation) {
  const operations = {
    add: (x, y) => x + y,
    subtract: (x, y) => x - y,
    multiply: (x, y) => x * y,
    divide: (x, y) => (y === 0 ? "Cannot divide by zero" : x / y)
  };

  const operationFn = operations[operation];
  if (!operationFn) return "Invalid operation";

  return operationFn(a, b);
}

console.log(calculator(10, 5, "add"));      // 15
console.log(calculator(10, 5, "divide"));   // 2
console.log(calculator(10, 0, "divide"));   // "Cannot divide by zero"
```

## 19.2 Student Grade System

```javascript
function getGrade(score) {
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

function gradeStudents(students) {
  return students.map(student => ({
    ...student,
    grade: getGrade(student.score)
  }));
}

const students = [
  { name: "Ana", score: 92 },
  { name: "Ben", score: 74 }
];

console.log(gradeStudents(students));
// [{ name: "Ana", score: 92, grade: "A" }, { name: "Ben", score: 74, grade: "C" }]
```

## 19.3 Banking System (Closures + Encapsulation)

```javascript
function createAccount(owner, initialBalance = 0) {
  let balance = initialBalance;
  const history = [];

  return {
    deposit(amount) {
      if (amount <= 0) return "Invalid deposit amount";
      balance += amount;
      history.push(`Deposited ${amount}`);
      return balance;
    },
    withdraw(amount) {
      if (amount > balance) return "Insufficient funds";
      balance -= amount;
      history.push(`Withdrew ${amount}`);
      return balance;
    },
    getBalance() { return balance; },
    getHistory() { return [...history]; }
  };
}

const acc = createAccount("Riya", 500);
acc.deposit(200);
acc.withdraw(100);
console.log(acc.getBalance()); // 600
console.log(acc.getHistory()); // ["Deposited 200", "Withdrew 100"]
```

## 19.4 Shopping Cart

```javascript
function createCart() {
  let items = [];

  return {
    addItem(name, price, qty = 1) {
      items.push({ name, price, qty });
    },
    removeItem(name) {
      items = items.filter(item => item.name !== name);
    },
    getTotal() {
      return items.reduce((sum, item) => sum + item.price * item.qty, 0);
    },
    getItems() {
      return [...items];
    }
  };
}

const cart = createCart();
cart.addItem("Book", 15, 2);
cart.addItem("Pen", 2, 5);
console.log(cart.getTotal()); // 15*2 + 2*5 = 40
```

## 19.5 Employee Payroll

```javascript
function calculatePay(hoursWorked, hourlyRate) {
  const regularHours = Math.min(hoursWorked, 40);
  const overtimeHours = Math.max(hoursWorked - 40, 0);
  const regularPay = regularHours * hourlyRate;
  const overtimePay = overtimeHours * hourlyRate * 1.5;
  return regularPay + overtimePay;
}

function generatePayroll(employees) {
  return employees.map(emp => ({
    name: emp.name,
    pay: calculatePay(emp.hours, emp.rate)
  }));
}

console.log(generatePayroll([
  { name: "Sam", hours: 45, rate: 20 },
  { name: "Lee", hours: 38, rate: 25 }
]));
```

## 19.6 Todo App Functions

```javascript
function createTodoList() {
  let todos = [];
  let nextId = 1;

  return {
    add(text) {
      todos.push({ id: nextId++, text, done: false });
    },
    complete(id) {
      todos = todos.map(t => (t.id === id ? { ...t, done: true } : t));
    },
    remove(id) {
      todos = todos.filter(t => t.id !== id);
    },
    getAll() { return [...todos]; },
    getPending() { return todos.filter(t => !t.done); }
  };
}

const todoList = createTodoList();
todoList.add("Learn closures");
todoList.add("Practice recursion");
todoList.complete(1);
console.log(todoList.getPending()); // only "Practice recursion" remains
```

## 19.7 Weather Utility

```javascript
function celsiusToFahrenheit(c) {
  return (c * 9) / 5 + 32;
}

function fahrenheitToCelsius(f) {
  return ((f - 32) * 5) / 9;
}

function describeWeather(tempCelsius) {
  if (tempCelsius <= 0) return "Freezing";
  if (tempCelsius <= 15) return "Cold";
  if (tempCelsius <= 25) return "Mild";
  return "Hot";
}

console.log(celsiusToFahrenheit(30));      // 86
console.log(describeWeather(30));          // "Hot"
```

## 19.8 Login Validator

```javascript
function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isValidPassword(password) {
  return password.length >= 8;
}

function validateLogin(email, password) {
  if (!isValidEmail(email)) return "Invalid email format";
  if (!isValidPassword(password)) return "Password must be at least 8 characters";
  return "Login valid";
}

console.log(validateLogin("test@example.com", "12345678")); // "Login valid"
console.log(validateLogin("bademail", "123"));               // "Invalid email format"
```

## 19.9 Library Management

```javascript
function createLibrary() {
  let books = [];

  return {
    addBook(title, author) {
      books.push({ title, author, borrowed: false });
    },
    borrowBook(title) {
      const book = books.find(b => b.title === title && !b.borrowed);
      if (!book) return "Book not available";
      book.borrowed = true;
      return `You borrowed "${title}"`;
    },
    returnBook(title) {
      const book = books.find(b => b.title === title && b.borrowed);
      if (!book) return "This book wasn't borrowed";
      book.borrowed = false;
      return `You returned "${title}"`;
    },
    listAvailable() {
      return books.filter(b => !b.borrowed).map(b => b.title);
    }
  };
}

const library = createLibrary();
library.addBook("1984", "George Orwell");
console.log(library.borrowBook("1984"));   // "You borrowed "1984""
console.log(library.listAvailable());      // []
```

## 19.10 Quiz System

```javascript
function createQuiz(questions) {
  let score = 0;
  let currentIndex = 0;

  return {
    getCurrentQuestion() {
      return questions[currentIndex]?.question ?? "Quiz complete!";
    },
    answer(userAnswer) {
      const question = questions[currentIndex];
      if (!question) return "No more questions";

      if (userAnswer === question.correctAnswer) {
        score++;
      }
      currentIndex++;
      return `Score: ${score}/${questions.length}`;
    },
    isFinished() {
      return currentIndex >= questions.length;
    }
  };
}

const quiz = createQuiz([
  { question: "2 + 2?", correctAnswer: "4" },
  { question: "Capital of France?", correctAnswer: "Paris" }
]);

console.log(quiz.getCurrentQuestion()); // "2 + 2?"
console.log(quiz.answer("4"));          // "Score: 1/2"
console.log(quiz.answer("Paris"));      // "Score: 2/2"
```

---
# PART 20 — SUMMARY CHEAT SHEET

## 20.1 Function Syntax Forms

| Form | Syntax | Hoisted? | Has own `this`? |
|---|---|---|---|
| Function Declaration | `function foo() {}` | Fully | Yes |
| Function Expression | `const foo = function() {}` | Variable only | Yes |
| Arrow Function | `const foo = () => {}` | Variable only (TDZ) | No — inherits lexically |
| Generator Function | `function* foo() {}` | Fully | Yes |
| Async Function | `async function foo() {}` | Fully | Yes |
| Method Shorthand | `{ foo() {} }` | N/A (object property) | Yes |

## 20.2 Core Concepts At a Glance

- **Parameter** — placeholder in a function definition.
- **Argument** — actual value passed at the call site.
- **Return** — sends a value back and stops execution.
- **Default Parameter** — fallback used only when the argument is `undefined`.
- **Rest Parameter** — gathers remaining arguments into an array.
- **Spread** — expands an array/object into individual values/arguments.
- **Scope** — where a variable is accessible.
- **Lexical Scope** — access is based on where code is written, not called.
- **Scope Chain** — the nested lookup path for resolving variable names.
- **Closure** — a function plus the outer variables it remembers.
- **First-Class Function** — a function usable as a value.
- **Higher-Order Function** — accepts and/or returns functions.
- **Callback** — a function passed to run later.
- **`this`** — depends on the call site; determined dynamically (except arrow functions).
- **`call()`** — invoke now, args listed individually.
- **`apply()`** — invoke now, args as an array.
- **`bind()`** — don't invoke; return a new function with `this` locked.
- **Hoisting** — declarations moved to the top of scope during the creation phase.
- **Temporal Dead Zone** — the gap where `let`/`const` exist but can't be accessed yet.
- **Execution Context** — the environment a function runs in (memory + scope + `this`).
- **Call Stack** — LIFO structure tracking active function calls.
- **Generator** — pausable function using `yield`.
- **Pure Function** — same input → same output, no side effects.
- **Currying** — chaining single-argument functions.
- **Partial Application** — pre-filling some arguments ahead of time.
- **Memoization** — caching results of expensive pure function calls.
- **Debounce** — wait for a pause in activity before running.
- **Throttle** — run at most once per fixed interval.

## 20.3 Quick Decision Guide

```
Need a reusable named function, possibly used before it's defined?
   -> Use a Function Declaration

Need to assign a function to a variable/object property?
   -> Use a Function Expression or Arrow Function

Need to preserve the outer "this" inside a callback (e.g., inside a method)?
   -> Use an Arrow Function

Need a constructor / dynamic "this" based on caller?
   -> Use a Regular Function

Need private state that persists between calls?
   -> Use a Closure

Need to run behavior supplied by the caller?
   -> Use a Higher-Order Function (accept a callback)

Need to produce a sequence of values one at a time?
   -> Use a Generator Function

Need to avoid re-running expensive, pure calculations?
   -> Use Memoization

Need to limit how often a handler fires during rapid events?
   -> Use Debounce (wait for pause) or Throttle (fixed rate)
```

## 20.4 Final Words

Functions are the single most important building block in JavaScript. Every other concept in the language — objects, closures, asynchronous programming, classes, even modules — is built directly on top of how functions work. Master parameters, scope, closures, `this`, and the call stack deeply, and the rest of JavaScript will make dramatically more sense.

> **Keep practicing:** Revisit Parts 16, 17, and 18 periodically. Function concepts are rarely mastered by reading alone — they click into place through repeated, hands-on practice.

---

*End of Functions.md — A Complete JavaScript Functions Guide.*
