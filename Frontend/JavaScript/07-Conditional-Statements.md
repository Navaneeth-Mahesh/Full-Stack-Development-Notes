# Conditional Statements in JavaScript

## Introduction

Programs are not just a sequence of instructions—they also need to **make decisions**.

Imagine a website:

* If the user enters the correct password → Log them in.
* If the password is incorrect → Show an error message.
* If the user is under 18 → Restrict access.
* If the shopping cart is empty → Display "Your cart is empty."

All of these decisions are made using **conditional statements**.

A conditional statement allows JavaScript to execute different blocks of code based on whether a condition is **true** or **false**.

---

# Real-Life Example

Imagine you're entering a movie theater.

Rules:

* If your age is **18 or above**, you can watch the movie.
* Otherwise, you cannot enter.

In JavaScript:

```javascript
let age = 20;

if (age >= 18) {
    console.log("Entry Allowed");
}
```

The program checks the condition.

* If it is **true**, the code inside the `if` block runs.
* If it is **false**, JavaScript skips that block.

---

# Comparison Operators

Conditions usually use comparison operators.

| Operator | Meaning                     | Example               |
| -------- | --------------------------- | --------------------- |
| `==`     | Equal (value only)          | `5 == "5"` → `true`   |
| `===`    | Strict Equal (value + type) | `5 === "5"` → `false` |
| `!=`     | Not Equal                   | `5 != 4`              |
| `!==`    | Strict Not Equal            | `5 !== "5"`           |
| `>`      | Greater Than                | `10 > 5`              |
| `<`      | Less Than                   | `5 < 10`              |
| `>=`     | Greater Than or Equal       | `18 >= 18`            |
| `<=`     | Less Than or Equal          | `10 <= 20`            |

**Professional Tip**

Always prefer `===` and `!==` because they compare both **value** and **data type**, making your code safer and more predictable.

---

# The `if` Statement

## Syntax

```javascript
if (condition) {
    // Code runs if condition is true
}
```

---

## Example 1

```javascript
let age = 20;

if (age >= 18) {
    console.log("You are eligible to vote.");
}
```

### Step-by-Step

```javascript
let age = 20;
```

Creates a variable named `age` and stores the value `20`.

```javascript
if (age >= 18)
```

Checks:

```
20 >= 18
```

Result:

```
true
```

Since the condition is true, JavaScript enters the block.

```javascript
console.log("You are eligible to vote.");
```

Output:

```
You are eligible to vote.
```

---

## Example 2

```javascript
let marks = 85;

if (marks >= 35) {
    console.log("Pass");
}
```

Output:

```
Pass
```

---

# The `if...else` Statement

Sometimes we want one block to execute when the condition is true and another block when it is false.

## Syntax

```javascript
if (condition) {

} else {

}
```

---

## Example

```javascript
let age = 16;

if (age >= 18) {
    console.log("Eligible");
} else {
    console.log("Not Eligible");
}
```

### How it Works

Condition:

```
16 >= 18
```

Result:

```
false
```

So JavaScript skips the `if` block and executes the `else` block.

Output:

```
Not Eligible
```

---

# Flow Diagram

```
Condition
     |
     |
  True? ---- No -----> else block
     |
    Yes
     |
  if block
```

---

# Example: Even or Odd

```javascript
let number = 12;

if (number % 2 === 0) {
    console.log("Even Number");
} else {
    console.log("Odd Number");
}
```

Explanation:

```
12 % 2 = 0
```

Since the remainder is `0`, the number is even.

---

# The `if...else if...else` Statement

Sometimes there are multiple conditions.

Example:

Marks can be:

* A Grade
* B Grade
* C Grade
* Fail

One `if...else` is not enough.

---

## Syntax

```javascript
if (condition1) {

} else if (condition2) {

} else if (condition3) {

} else {

}
```

JavaScript checks each condition **from top to bottom**.

The first true condition is executed.

The remaining conditions are skipped.

---

## Example

```javascript
let marks = 82;

if (marks >= 90) {
    console.log("Grade A+");
}
else if (marks >= 75) {
    console.log("Grade A");
}
else if (marks >= 60) {
    console.log("Grade B");
}
else if (marks >= 35) {
    console.log("Grade C");
}
else {
    console.log("Fail");
}
```

Output:

```
Grade A
```

---

# Example: Temperature

```javascript
let temperature = 38;

if (temperature >= 40) {
    console.log("Very Hot");
}
else if (temperature >= 30) {
    console.log("Hot");
}
else if (temperature >= 20) {
    console.log("Pleasant");
}
else {
    console.log("Cold");
}
```

Output

```
Hot
```

---

# Nested `if`

An `if` statement can exist inside another `if`.

Example:

Only adults can vote.

Among adults:

* Indian citizens can vote.
* Others cannot.

```javascript
let age = 22;
let citizen = true;

if (age >= 18) {

    if (citizen) {
        console.log("Eligible to Vote");
    } else {
        console.log("Only Citizens Can Vote");
    }

} else {
    console.log("Under Age");
}
```

---

# Logical Operators

Sometimes one condition is not enough.

## AND (`&&`)

Both conditions must be true.

```javascript
let age = 22;
let hasID = true;

if (age >= 18 && hasID) {
    console.log("Entry Allowed");
}
```

---

## OR (`||`)

At least one condition must be true.

```javascript
let isAdmin = false;
let isManager = true;

if (isAdmin || isManager) {
    console.log("Access Granted");
}
```

---

## NOT (`!`)

Reverses the boolean value.

```javascript
let isLoggedIn = false;

if (!isLoggedIn) {
    console.log("Please Login");
}
```

---

# Truthy and Falsy Values

JavaScript doesn't always require `true` or `false`.

Some values automatically behave as true or false.

## Falsy Values

```javascript
false
0
-0
""
null
undefined
NaN
```

Everything else is considered **truthy**.

Example:

```javascript
let username = "";

if (username) {
    console.log("Welcome");
} else {
    console.log("Username Required");
}
```

Output

```
Username Required
```

---

# Ternary Operator

The ternary operator is a short form of `if...else`.

## Syntax

```javascript
condition ? valueIfTrue : valueIfFalse;
```

---

## Example

```javascript
let age = 20;

let result = age >= 18 ? "Adult" : "Minor";

console.log(result);
```

Output

```
Adult
```

---

# When to Use Which Statement

### Use `if`

When checking a single condition.

```javascript
if (age >= 18) {

}
```

---

### Use `if...else`

When there are exactly two outcomes.

```javascript
if (isLoggedIn) {

} else {

}
```

---

### Use `if...else if`

When checking multiple ranges or possibilities.

```javascript
if (...)
else if (...)
else
```

---

### Use Nested `if`

When a second condition depends on the first.

Example:

```
Adult?

    Yes

        Citizen?

            Yes
```

---

### Use Ternary

Only for short conditions.

```javascript
let result = marks >= 35 ? "Pass" : "Fail";
```

---

# Common Beginner Mistakes

## 1. Using `=` Instead of `===`

Wrong

```javascript
if (age = 18) {

}
```

Correct

```javascript
if (age === 18) {

}
```

---

## 2. Forgetting Curly Braces

Wrong

```javascript
if (age >= 18)
console.log("Adult");
console.log("Welcome");
```

Only the first statement belongs to the `if`.

Correct

```javascript
if (age >= 18) {
    console.log("Adult");
    console.log("Welcome");
}
```

---

## 3. Incorrect Condition Order

Wrong

```javascript
let marks = 95;

if (marks >= 35)
    console.log("Pass");
else if (marks >= 90)
    console.log("A+");
```

Output

```
Pass
```

Correct

```javascript
if (marks >= 90)
    console.log("A+");
else if (marks >= 35)
    console.log("Pass");
```

Always place the **most specific** conditions first.

---

# Real-World Uses

Conditional statements are used in almost every application.

Examples:

* Login systems
* Signup validation
* ATM software
* Banking applications
* Shopping carts
* Online exams
* Role-based authentication
* Admin dashboards
* API response handling
* Payment gateways

---

# Practice Questions

1. What is a conditional statement?
2. What is the difference between `if` and `if...else`?
3. Why should we use `===` instead of `==`?
4. When should you use `else if`?
5. What are truthy and falsy values?
6. What does the ternary operator do?
7. What is a nested `if` statement?

---

# Coding Exercises

### Exercise 1

Take a number and check whether it is positive or negative.

---

### Exercise 2

Check if a student has passed.

Passing marks: **35**

---

### Exercise 3

Take an age and display:

* Child
* Teenager
* Adult
* Senior Citizen

---

### Exercise 4

Check whether a year is a leap year.

---

### Exercise 5

Create a login system.

Conditions:

* Username: `"admin"`
* Password: `"12345"`

If both are correct:

```
Login Successful
```

Otherwise:

```
Invalid Credentials
```

---

# Mini Challenge

Write a program that takes three numbers and prints the **largest number** using only `if...else if...else`.

Try solving it without searching online. It is an excellent exercise for improving logical thinking.
