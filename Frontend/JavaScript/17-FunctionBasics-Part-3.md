# 13-Functions-Basics.md (Part 3)

---

# Callback Functions (Introduction)

## Introduction

One of JavaScript's most powerful features is that **functions can be passed as arguments to other functions**.

When a function is passed into another function and is executed later, it is called a **Callback Function**.

Simply put:

> **A callback is a function that is given to another function to be called later.**

---

## Why Do We Need Callback Functions?

Imagine you're ordering food online.

1. You place the order.
2. The restaurant prepares the food.
3. Once the food is ready, the delivery person calls you.

That phone call happens **after** the food is prepared.

The phone call is similar to a callback.

JavaScript works in the same way.

Some tasks take time to complete.

Instead of waiting, JavaScript says:

> "Continue doing other work. When I'm done, I'll call this function."

---

## Basic Example

```javascript
function greet(name) {
    console.log(`Hello ${name}`);
}

function processUser(callback) {
    callback("Navaneeth");
}

processUser(greet);
```

### Output

```
Hello Navaneeth
```

---

## Line-by-Line Explanation

```javascript
function greet(name) {
```

Creates a function named `greet`.

---

```javascript
console.log(`Hello ${name}`);
```

Prints a greeting.

---

```javascript
function processUser(callback) {
```

This function expects another function as a parameter.

---

```javascript
callback("Navaneeth");
```

Executes the function that was passed.

---

```javascript
processUser(greet);
```

Passes the `greet` function itself.

Notice:

```javascript
greet
```

NOT

```javascript
greet()
```

Adding `()` would execute it immediately.

---

# Anonymous Callback

Instead of creating a separate function:

```javascript
function greet(name){
    console.log(name);
}

processUser(greet);
```

We can write:

```javascript
processUser(function(name){

    console.log(`Hello ${name}`);

});
```

This is called an **Anonymous Callback Function**.

---

# Arrow Function Callback

Modern JavaScript usually uses arrow functions.

```javascript
processUser((name)=>{

    console.log(`Hello ${name}`);

});
```

This is the preferred style in React, Node.js, and modern JavaScript.

---

# Real-World Examples

## Button Click

```javascript
button.addEventListener("click", function(){

    console.log("Button Clicked");

});
```

The browser calls the callback whenever the button is clicked.

---

## Timer

```javascript
setTimeout(function(){

    console.log("3 Seconds Completed");

},3000);
```

JavaScript waits for 3 seconds and then calls the callback.

---

## Array Methods

```javascript
const numbers = [1,2,3,4];

numbers.forEach(function(number){

    console.log(number);

});
```

`forEach()` calls the callback once for every element.

---

# Pure Functions

## What is a Pure Function?

A Pure Function always produces the same output for the same input.

It also **does not change anything outside itself.**

---

Example

```javascript
function add(a,b){

    return a+b;

}

console.log(add(10,20));
```

Output

```
30
```

Every time

```javascript
add(10,20)
```

returns

```
30
```

Nothing else changes.

---

## Why Are Pure Functions Good?

They are

* Easy to test
* Easy to debug
* Predictable
* Reusable

Most modern JavaScript frameworks encourage pure functions.

---

# Impure Functions

Impure functions depend on outside values or modify outside values.

Example

```javascript
let count = 0;

function increment(){

    count++;

}
```

Output depends on previous executions.

First call

```
1
```

Second call

```
2
```

Third call

```
3
```

The result changes because it modifies external state.

---

# Pure vs Impure

| Pure                        | Impure               |
| --------------------------- | -------------------- |
| Same input → Same output    | Output may change    |
| Doesn't modify outside data | Changes outside data |
| Easy to test                | Harder to test       |

---

# Immediately Invoked Function Expression (IIFE)

## What is an IIFE?

Normally we write

```javascript
function greet(){

}

greet();
```

Sometimes we need a function that should execute **only once**.

Instead of

Creating →

Calling →

We can do both together.

This is called an **Immediately Invoked Function Expression**.

---

## Syntax

```javascript
(function(){

})();
```

---

## Example

```javascript
(function(){

    console.log("Application Started");

})();
```

Output

```
Application Started
```

The function executes immediately.

---

## Arrow Function IIFE

```javascript
(()=>{

    console.log("Arrow IIFE");

})();
```

---

## Why Use IIFE?

Before ES6, JavaScript had no block scope.

Developers used IIFEs to prevent variables from polluting the global scope.

Example

```javascript
(function(){

    let username = "Navaneeth";

    console.log(username);

})();
```

Outside

```javascript
console.log(username);
```

Output

```
ReferenceError
```

The variable stays private.

---

# Recursion (Introduction)

## What is Recursion?

Recursion means

> **A function calling itself.**

---

## Why Use Recursion?

Some problems naturally repeat themselves.

Examples

* Folder traversal
* Tree structures
* File systems
* Menus
* Mathematical calculations

---

## Example

```javascript
function countdown(number){

    if(number===0){

        return;

    }

    console.log(number);

    countdown(number-1);

}

countdown(5);
```

Output

```
5
4
3
2
1
```

---

## How It Works

```
countdown(5)

↓

countdown(4)

↓

countdown(3)

↓

countdown(2)

↓

countdown(1)

↓

countdown(0)

↓

Stop
```

---

# Base Case

Every recursive function **must have a stopping condition**.

Without it,

the function keeps calling itself forever.

Example

```javascript
function test(){

    test();

}

test();
```

Output

```
Maximum Call Stack Size Exceeded
```

---

# Common Beginner Mistakes

## Forgetting Return

Wrong

```javascript
function square(number){

    number*number;

}

console.log(square(5));
```

Output

```
undefined
```

Correct

```javascript
function square(number){

    return number*number;

}
```

---

## Calling Instead of Passing

Wrong

```javascript
processUser(greet());
```

Correct

```javascript
processUser(greet);
```

---

## Forgetting Base Case

Wrong

```javascript
function demo(){

    demo();

}
```

Infinite recursion.

---

## Using Arrow Functions Everywhere

Arrow functions are excellent,

but not every function should be an arrow function.

Normal functions are still preferred in some situations (especially when working with `this`, constructors, and object methods).

---

# Best Practices

* Use meaningful function names.
* Keep functions small.
* Make each function perform one task.
* Use `return` instead of relying on global variables.
* Prefer arrow functions for short callbacks.
* Prefer pure functions whenever possible.
* Avoid deeply nested functions unless necessary.
* Write reusable functions.

---

# Real-World Uses

Functions are used everywhere in JavaScript applications.

Examples include:

* Form validation
* Login systems
* API requests
* Button click events
* Shopping cart calculations
* Authentication
* Image processing
* Payment gateways
* React components
* Node.js servers

Functions are one of the core building blocks of modern JavaScript development.

---

# Practice Questions

1. What is a callback function?
2. Why do we pass functions as arguments?
3. What is the difference between a callback and a normal function?
4. What is a pure function?
5. What is an impure function?
6. What is an IIFE?
7. Why were IIFEs commonly used before ES6?
8. What is recursion?
9. Why is a base case necessary?
10. What happens if a recursive function has no stopping condition?

---

# Coding Exercises

## Exercise 1

Create a callback function that prints a welcome message.

---

## Exercise 2

Create a pure function that calculates the area of a rectangle.

---

## Exercise 3

Create an impure function that increments a global counter.

---

## Exercise 4

Write an IIFE that prints:

```
JavaScript Course Started
```

---

## Exercise 5

Create a recursive function that prints numbers from **10 to 1**.

---

## Exercise 6

Write a recursive function to calculate the factorial of a number.

Example:

```
5! = 120
```

---

# Mini Project — Student Result Management System

Build a console-based program that demonstrates all the function concepts you've learned.

### Requirements

* Create separate functions for:

  * Input validation
  * Calculating total marks
  * Calculating average
  * Determining grade
  * Displaying the final report

* Use a **callback function** to display the result after calculations are complete.

* Use a **pure function** for calculating the total and average.

* Use an **IIFE** to display a startup message like `"Student Result System Started"`.

* Use a **recursive function** to display subject names or count down before showing the result.

---

# Chapter Summary

After completing **Functions (Part 1, Part 2, and Part 3)**, you should be able to:

* Create and invoke functions.
* Work with parameters, arguments, and return values.
* Use default and rest parameters.
* Understand function declarations, expressions, anonymous functions, and arrow functions.
* Store and pass functions as values.
* Write nested functions.
* Use callback functions.
* Understand pure vs. impure functions.
* Use IIFEs for one-time execution.
* Write basic recursive functions.
* Apply functions to solve real-world programming problems.

**Next Chapter:** **14-Functions-Advanced.md**, where you'll dive into **Scope, Lexical Scope, Closures, First-Class Functions, Higher-Order Functions, `this`, `call()`, `apply()`, `bind()`, Hoisting, Execution Context, Call Stack, Generator Functions, and more.**
