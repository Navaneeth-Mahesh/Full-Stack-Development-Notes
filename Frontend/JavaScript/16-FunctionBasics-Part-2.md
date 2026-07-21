# 16-Functions-Basics.md (Part 2)

## Topics Covered

```text
1. Default Parameters
2. Rest Parameters (...)
3. Function Expressions
4. Anonymous Functions
5. Arrow Functions
6. Functions as Values
7. Functions Stored in Variables
8. Nested Functions
```

---

## 1. Default Parameters

### Introduction

Sometimes a function expects one or more parameters.

Example:

```javascript
function greet(name) {
    console.log(`Hello ${name}`);
}

greet();
```

Output

```text
Hello undefined
```

Since we didn't provide a value, `name` becomes `undefined`.

To solve this problem, JavaScript introduced **Default Parameters**.

A default parameter provides a fallback value if no argument is passed.

---

### Syntax

```javascript
function functionName(parameter = defaultValue) {

}
```

---

### Example

```javascript
function greet(name = "Guest") {
    console.log(`Hello ${name}`);
}

greet();
greet("Navaneeth");
```

Output

```text
Hello Guest
Hello Navaneeth
```

---

### Line-by-Line Explanation

```javascript
function greet(name = "Guest") {
```

If no value is passed,

```javascript
name = "Guest"
```

Otherwise, JavaScript uses the provided value.

---

### Multiple Default Parameters

```javascript
function introduce(name = "Unknown", age = 18) {
    console.log(`Name : ${name}`);
    console.log(`Age : ${age}`);
}

introduce();
introduce("Navaneeth", 20);
```

Output

```text
Name : Unknown
Age : 18

Name : Navaneeth
Age : 20
```

---

### Real World Example

Shopping Website

```javascript
function calculatePrice(price, tax = 18) {
    return price + (price * tax / 100);
}
```

If tax isn't supplied,

Default GST = 18%.

---

## 2. Rest Parameters (...)

### Why Do We Need Rest Parameters?

Suppose we want a function that adds **any number of values**.

Without rest parameters:

```javascript
function add(a, b, c) {
    return a + b + c;
}

console.log(add(10,20,30));
```

But what if there are 10 numbers?

Or 100 numbers?

Rest Parameters solve this problem.

---

### Syntax

```javascript
function name(...parameter) {

}
```

Notice the three dots.

```text
...
```

This is called the **Rest Operator**.

---

### Example

```javascript
function add(...numbers) {

    console.log(numbers);

}

add(10,20,30,40);
```

Output

```text
[10,20,30,40]
```

JavaScript automatically stores all values inside an array.

---

### Summing Numbers

```javascript
function add(...numbers){

    let sum = 0;

    for(let number of numbers){
        sum += number;
    }

    return sum;

}

console.log(add(10,20));
console.log(add(10,20,30,40));
```

Output

```text
30
100
```

---

### Rules

Rest parameter must always be the **last parameter**.

Correct

```javascript
function demo(name,...marks){

}
```

Wrong

```javascript
function demo(...marks,name){

}
```

---

### Real World Example

Shopping Cart

```javascript
function totalPrice(...prices){

}
```

Products

```text
100
250
900
550
```

All prices arrive as an array.

---

## 3. Function Expressions

Until now we've written functions like this:

```javascript
function greet(){

}
```

This is called a **Function Declaration**.

Functions can also be stored inside variables.

This is called a **Function Expression**.

---

### Syntax

```javascript
const variable = function(){

};
```

---

### Example

```javascript
const greet = function(){

    console.log("Hello");

};

greet();
```

Output

```text
Hello
```

---

### Why Use Function Expressions?

They can be

* Stored
* Passed
* Returned
* Used as callbacks

They are widely used in React, Node.js and modern JavaScript.

---

## Function Declaration vs Function Expression

Declaration

```javascript
function add(){

}
```

Expression

```javascript
const add = function(){

};
```

---

## 4. Anonymous Functions

Anonymous means

> Without a name.

Example

```javascript
function(){

}
```

Notice

No function name exists.

Anonymous functions are commonly used inside

* Event listeners
* Timers
* Callbacks

---

Example

```javascript
const greet = function(){

    console.log("Hello");

};
```

Here,

```javascript
function(){

}
```

is anonymous.

---

## Real World Example

Button Click

```javascript
button.addEventListener("click", function(){

    console.log("Button Clicked");

});
```

The function doesn't need a name because it's used only once.

---

## 5. Arrow Functions

Arrow Functions were introduced in ES6.

They provide a shorter syntax.

---

### Normal Function

```javascript
function greet(name){

    return `Hello ${name}`;

}
```

---

### Arrow Function

```javascript
const greet = (name) => {

    return `Hello ${name}`;

};
```

Both do the same thing.

---

### If Only One Parameter

Parentheses are optional.

```javascript
const greet = name => {

    return `Hello ${name}`;

};
```

---

### If Only One Statement

```javascript
const greet = name => `Hello ${name}`;
```

JavaScript automatically returns the value.

---

### Multiple Parameters

```javascript
const add = (a,b) => {

    return a+b;

};
```

---

### No Parameters

```javascript
const hello = () => {

    console.log("Hello");

};
```

---

### Arrow Function vs Normal Function

| Normal Function         | Arrow Function                |
| ----------------------- | ----------------------------- |
| Uses `function` keyword | Uses `=>`                     |
| Has its own `this`      | Doesn't create its own `this` |
| Longer syntax           | Short syntax                  |

(We'll study `this` later.)

---

### Real World Example

Filtering products

```javascript
const expensive = products.filter(product => product.price > 1000);
```

React

```javascript
const Home = () => {

};
```

Arrow functions are everywhere in modern JavaScript.

---

## 6. Functions as Values

One of JavaScript's biggest features:

Functions are **First-Class Citizens**.

That means functions behave like any other value.

Just like

```javascript
let age = 20;
```

We can also do

```javascript
let greet = function(){

};
```

Functions can be

* Stored
* Assigned
* Passed
* Returned

---

Example

```javascript
const hello = function(){

    console.log("Hello");

};

hello();
```

---

## 7. Functions Stored in Variables

Functions can be assigned to variables.

```javascript
const add = function(a,b){

    return a+b;

};

console.log(add(10,20));
```

Output

```text
30
```

---

Functions can even be copied.

```javascript
const greet = function(){

    console.log("Hello");

};

const welcome = greet;

welcome();
```

Output

```text
Hello
```

Both variables point to the same function.

---

## 8. Nested Functions

A function inside another function is called a **Nested Function**.

Example

```javascript
function outer(){

    console.log("Outer Function");

    function inner(){

        console.log("Inner Function");

    }

    inner();

}

outer();
```

Output

```text
Outer Function
Inner Function
```

---

### Why Use Nested Functions?

They help

* Organize code
* Hide helper functions
* Prepare for Closures

---

### Real World Example

User Registration

```javascript
function registerUser(name){

    function validate(){

        return name.length >= 3;

    }

    if(validate()){

        console.log("Registration Successful");

    }

}

registerUser("Navaneeth");
```

The `validate()` function is only needed inside `registerUser()`, so it is kept private.

---

# Common Beginner Mistakes

### Forgetting to Return

Wrong

```javascript
function add(a,b){

    a+b;

}

console.log(add(10,20));
```

Output

```text
undefined
```

Correct

```javascript
function add(a,b){

    return a+b;

}
```

---

### Calling Before Assignment

Wrong

```javascript
greet();

const greet = function(){

};
```

Function expressions are **not hoisted** like function declarations.

---

### Confusing Rest and Spread

Rest

```javascript
function add(...numbers){

}
```

Spread

```javascript
add(...array);
```

They look the same but serve different purposes.

---

# Practice Questions

1. What are default parameters?
2. Why do we use rest parameters?
3. What is the difference between function declaration and function expression?
4. What is an anonymous function?
5. What are arrow functions?
6. What are the advantages of arrow functions?
7. Why are functions called first-class citizens?
8. What is a nested function?

---

# Coding Exercises

### Exercise 1

Create a function that greets the user using a default name.

---

### Exercise 2

Create a function that accepts unlimited numbers and returns their sum.

---

### Exercise 3

Convert a normal function into an arrow function.

---

### Exercise 4

Store a function inside a variable and call it.

---

### Exercise 5

Create a nested function that validates a username before printing "Welcome".

---

# Mini Project

## Student Report Generator

Create a program that:

* Uses **default parameters** for missing marks.
* Uses a **rest parameter** to accept multiple subject marks.
* Uses a **function expression** to calculate the average.
* Uses an **arrow function** to determine the grade.
* Uses a **nested function** to validate marks before calculating the result.

This project combines every concept learned in this chapter and prepares you for advanced topics like **Scope**, **Closures**, and **Higher-Order Functions**.
