# JavaScript Functions (Part 1)

# Introduction to Functions

Functions are one of the most important concepts in JavaScript.

If variables are used to **store data**, then **functions are used to perform tasks**.

A function is simply **a reusable block of code** that performs a specific job.

Instead of writing the same code again and again, we write it once inside a function and call it whenever we need it.

Think of a function as a **machine**.

```
Input → Function → Output
```

Example:

```
5, 10
   ↓
Add Function
   ↓
15
```

The function receives two numbers, performs addition, and returns the result.

---

# Why Do Functions Exist?

Imagine you need to display a welcome message for every user.

Without functions:

```javascript
console.log("Welcome Navaneeth!");

console.log("Welcome Rahul!");

console.log("Welcome Sai!");

console.log("Welcome Arjun!");
```

Notice something?

The same code is repeated multiple times.

Now imagine displaying this message for **10,000 users**.

That would be terrible.

Instead, we create one function.

```javascript
function welcome(name) {
    console.log(`Welcome ${name}!`);
}

welcome("Navaneeth");
welcome("Rahul");
welcome("Sai");
welcome("Arjun");
```

Now the code is:

- Cleaner
- Reusable
- Easier to maintain
- Less error-prone

This is exactly why functions exist.

---

# Problems Functions Solve

Functions solve many programming problems.

## 1. Code Reusability

Instead of writing the same code repeatedly, write it once.

Without function

```javascript
let total1 = 100 + 200;
console.log(total1);

let total2 = 500 + 300;
console.log(total2);

let total3 = 800 + 900;
console.log(total3);
```

With function

```javascript
function add(a, b) {
    return a + b;
}

console.log(add(100, 200));
console.log(add(500, 300));
console.log(add(800, 900));
```

Much cleaner.

---

## 2. Readability

Bad

```javascript
let total = (price * quantity) - discount + tax;
```

Better

```javascript
let total = calculateTotal(price, quantity, discount, tax);
```

The second example explains what the code is doing.

---

## 3. Easy Maintenance

Suppose your tax calculation changes.

Without functions

You must update hundreds of places.

With functions

Only one function needs updating.

---

## 4. Modularity

Large applications are divided into small functions.

Example:

Instagram

```
Login Function

↓

Upload Function

↓

Like Function

↓

Comment Function

↓

Logout Function
```

Every feature is built using functions.

---

# Real-World Examples

Functions are everywhere.

Amazon

```text
calculateTotal()

addToCart()

placeOrder()

applyCoupon()
```

Instagram

```text
loginUser()

uploadPost()

followUser()

likePost()
```

Netflix

```text
playMovie()

pauseMovie()

searchMovie()
```

Google Maps

```text
findRoute()

showTraffic()

calculateDistance()
```

Modern applications are simply thousands of functions working together.

---

# Function Syntax

Basic syntax

```javascript
function functionName() {

    // code

}
```

Example

```javascript
function greet() {

    console.log("Hello World");

}
```

Let's understand every part.

```javascript
function
```

This keyword tells JavaScript

"I'm creating a function."

---

```javascript
greet
```

This is the function name.

It should clearly describe what the function does.

---

```javascript
()
```

These parentheses hold parameters.

Currently they are empty.

---

```javascript
{}
```

Curly braces contain the function body.

Everything inside runs when the function is called.

---

# Function Declaration

This is the most common way to create functions.

Example

```javascript
function greet() {

    console.log("Welcome to JavaScript");

}
```

Nothing happens yet.

Why?

Because the function is only created.

It hasn't been executed.

---

# Calling (Invoking) a Function

To execute a function, call it using its name.

Example

```javascript
function greet() {

    console.log("Welcome!");

}

greet();
```

Output

```
Welcome!
```

---

# Internal Working

Consider

```javascript
function greet() {

    console.log("Hello");

}

greet();
```

Step 1

JavaScript reads

```javascript
function greet()
```

It creates a function in memory.

Nothing is printed.

---

Step 2

JavaScript reaches

```javascript
greet();
```

Now it executes the function.

---

Step 3

The code inside runs.

```javascript
console.log("Hello");
```

Output

```
Hello
```

---

# Calling Multiple Times

One function can be called many times.

```javascript
function greet() {

    console.log("Hello");

}

greet();

greet();

greet();
```

Output

```
Hello
Hello
Hello
```

Notice

We wrote the code only once.

---

# Parameters

A parameter is a variable that receives data.

Example

```javascript
function greet(name) {

    console.log(`Hello ${name}`);

}
```

Here

```javascript
name
```

is a parameter.

Think of it as an empty box waiting for a value.

---

# Arguments

Arguments are the actual values passed to a function.

Example

```javascript
greet("Navaneeth");
```

Here

```javascript
"Navaneeth"
```

is the argument.

---

Parameter vs Argument

```javascript
function greet(name) {

    console.log(name);

}

greet("Navaneeth");
```

```
Parameter → name

Argument → "Navaneeth"
```

Many beginners confuse these two terms.

Remember

Parameter = Variable

Argument = Actual Value

---

# Multiple Parameters

Functions can receive multiple values.

Example

```javascript
function add(a, b) {

    console.log(a + b);

}

add(10, 20);
```

Output

```
30
```

---

# Line-by-Line Explanation

```javascript
function add(a, b)
```

Create a function named add.

It expects two parameters.

---

```javascript
console.log(a + b);
```

Add the two numbers.

Print the result.

---

```javascript
add(10, 20);
```

Function is called.

```
a = 10

b = 20
```

Then

```
10 + 20
```

Output

```
30
```

---

# The Return Statement

A function can also send data back.

This is done using

```javascript
return
```

Example

```javascript
function add(a, b) {

    return a + b;

}

let result = add(10, 20);

console.log(result);
```

Output

```
30
```

---

# Why Return?

Without return

```javascript
function add(a, b) {

    console.log(a + b);

}

let result = add(10, 20);

console.log(result);
```

Output

```
30

undefined
```

Why?

Because

```
console.log()
```

prints the value.

It doesn't send it back.

---

With return

```javascript
function add(a, b) {

    return a + b;

}
```

The function gives the answer back to the caller.

Now

```javascript
let result = add(10, 20);
```

stores

```
30
```

inside

```javascript
result
```

---

# return Ends the Function

Example

```javascript
function test() {

    console.log("One");

    return;

    console.log("Two");

}

test();
```

Output

```
One
```

The second console never runs.

Because

```
return
```

immediately exits the function.

---

# Returning Strings

```javascript
function fullName(first, last) {

    return first + " " + last;

}

console.log(fullName("Navaneeth", "Mahesh"));
```

Output

```
Navaneeth Mahesh
```

---

# Returning Boolean Values

```javascript
function isAdult(age) {

    return age >= 18;

}

console.log(isAdult(20));
```

Output

```
true
```

---

# Returning Objects

```javascript
function createUser(name, age) {

    return {

        name: name,
        age: age

    };

}

console.log(createUser("Navaneeth", 19));
```

Output

```javascript
{
    name: "Navaneeth",
    age: 19
}
```

---

# Returning Arrays

```javascript
function getNumbers() {

    return [10, 20, 30];

}

console.log(getNumbers());
```

Output

```javascript
[10, 20, 30]
```

---

# Returning Multiple Values

A JavaScript function cannot directly return multiple separate values.

Wrong

```javascript
function test() {

    return 10;

    return 20;

}
```

Only the first `return` executes.

Instead, return an object or an array.

Using an object

```javascript
function calculate(a, b) {

    return {

        sum: a + b,
        difference: a - b,
        product: a * b,
        quotient: a / b

    };

}

let result = calculate(20, 10);

console.log(result.sum);
console.log(result.product);
```

Output

```
30
200
```

---

# Common Beginner Mistakes

## Forgetting to Call the Function

Wrong

```javascript
function greet() {
    console.log("Hello");
}
```

Nothing happens.

Correct

```javascript
greet();
```

---

## Confusing Parameters and Arguments

```javascript
function greet(name) {

}

greet("Navaneeth");
```

```
Parameter → name

Argument → Navaneeth
```

---

## Using console.log() Instead of return

Wrong

```javascript
function add(a, b) {

    console.log(a + b);

}
```

Correct

```javascript
function add(a, b) {

    return a + b;

}
```

---

# Practice Questions

1. What is a function?
2. Why do we use functions?
3. What is the difference between a parameter and an argument?
4. What is a function declaration?
5. What is function invocation?
6. What does the `return` keyword do?
7. What happens after a `return` statement?
8. Can a function return an object?
9. Can a function return an array?
10. Why are functions important in real-world applications?

---

# Coding Exercises

### Exercise 1

Create a function that prints your name.

---

### Exercise 2

Create a function that adds two numbers.

---

### Exercise 3

Create a function that returns the square of a number.

---

### Exercise 4

Create a function that returns whether a person is eligible to vote.

---

### Exercise 5

Create a function that accepts first name and last name and returns the full name.