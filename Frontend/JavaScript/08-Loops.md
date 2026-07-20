# JavaScript Loops

## Introduction

Imagine you need to print:

```text
Hello
Hello
Hello
Hello
Hello
```

One way is:

```javascript
console.log("Hello");
console.log("Hello");
console.log("Hello");
console.log("Hello");
console.log("Hello");
```

This works, but what if you need to print it **100** or **10,000** times?

Writing the same code repeatedly is inefficient.

This is where **loops** become useful.

A **loop** allows JavaScript to execute the same block of code multiple times until a condition becomes false.

---

# Why Do We Need Loops?

Loops help us:

* Repeat tasks automatically
* Reduce duplicate code
* Process large amounts of data
* Iterate through arrays and objects
* Build efficient programs

Without loops, programming would involve writing the same code over and over.

---

# Real-World Examples

Loops are used everywhere.

Examples:

* Displaying all products on an e-commerce website
* Showing all comments on a post
* Displaying chat messages
* Printing student marks
* Processing bank transactions
* Creating game animations
* Reading API data

Whenever something repeats, a loop is usually involved.

---

# Types of Loops in JavaScript

JavaScript provides several types of loops.

| Loop         | Used When                       |
| ------------ | ------------------------------- |
| `for`        | Number of iterations is known   |
| `while`      | Number of iterations is unknown |
| `do...while` | Code must run at least once     |
| `for...of`   | Iterate over arrays and strings |
| `for...in`   | Iterate over object properties  |

---

# The `for` Loop

The `for` loop is the most commonly used loop.

## Syntax

```javascript
for (initialization; condition; update) {

    // code

}
```

---

# Understanding the Three Parts

## 1. Initialization

Runs only once.

Example:

```javascript
let i = 1;
```

Creates a counter.

---

## 2. Condition

JavaScript checks the condition before every iteration.

If the condition is true, the loop continues.

If false, the loop stops.

---

## 3. Update

Runs after every iteration.

Usually increases or decreases the counter.

Example:

```javascript
i++;
```

---

# Flow of a `for` Loop

```text
Initialization
      ↓
Check Condition
      ↓
 True?
      ↓
 Execute Code
      ↓
Update Variable
      ↓
Back to Condition
      ↓
False?
      ↓
Stop
```

---

# Example 1

Print numbers from 1 to 5.

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

Output

```text
1
2
3
4
5
```

---

# Line-by-Line Explanation

```javascript
for (let i = 1; i <= 5; i++)
```

### Initialization

```javascript
let i = 1;
```

Counter starts from 1.

---

### Condition

```javascript
i <= 5
```

Checks if the counter is less than or equal to 5.

---

### Update

```javascript
i++
```

Increases `i` by one after each iteration.

---

# Internal Execution

### First Iteration

```text
i = 1

1 <= 5 → true

Print 1

i becomes 2
```

---

### Second Iteration

```text
2 <= 5 → true

Print 2

i becomes 3
```

---

### Third

```text
3 <= 5
```

---

### Fourth

```text
4 <= 5
```

---

### Fifth

```text
5 <= 5
```

---

### Sixth

```text
6 <= 5

false

Loop stops
```

---

# Example 2

Print even numbers.

```javascript
for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}
```

Output

```text
2
4
6
8
10
12
14
16
18
20
```

---

# Example 3

Print numbers in reverse order.

```javascript
for (let i = 10; i >= 1; i--) {
    console.log(i);
}
```

Output

```text
10
9
8
7
6
5
4
3
2
1
```

---

# Infinite Loop

An infinite loop never ends.

Example

```javascript
for (;;) {
    console.log("Hello");
}
```

or

```javascript
while (true) {
    console.log("Running");
}
```

Avoid infinite loops unless intentionally required.

---

# The `while` Loop

The `while` loop executes as long as the condition is true.

## Syntax

```javascript
while (condition) {

    // code

}
```

---

# Example

```javascript
let i = 1;

while (i <= 5) {

    console.log(i);

    i++;

}
```

Output

```text
1
2
3
4
5
```

---

# How It Works

1. Check condition.
2. If true, execute code.
3. Update variable.
4. Repeat.

---

# `for` vs `while`

Both produce the same result.

### Using `for`

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

### Using `while`

```javascript
let i = 1;

while (i <= 5) {
    console.log(i);
    i++;
}
```

---

# When to Use `while`

Use `while` when you don't know how many times the loop should run.

Example:

Reading user input until it becomes valid.

---

# The `do...while` Loop

The `do...while` loop executes the code **at least once**, even if the condition is false.

## Syntax

```javascript
do {

    // code

} while (condition);
```

---

# Example

```javascript
let i = 1;

do {

    console.log(i);

    i++;

} while (i <= 5);
```

Output

```text
1
2
3
4
5
```

---

# Difference Between `while` and `do...while`

### `while`

Condition is checked first.

```javascript
let i = 10;

while (i <= 5) {
    console.log(i);
}
```

Output

```text
Nothing
```

---

### `do...while`

```javascript
let i = 10;

do {

    console.log(i);

} while (i <= 5);
```

Output

```text
10
```

The loop executes once before checking the condition.

---

# The `break` Statement

`break` immediately exits the loop.

Example

```javascript
for (let i = 1; i <= 10; i++) {

    if (i === 6) {
        break;
    }

    console.log(i);

}
```

Output

```text
1
2
3
4
5
```

The loop stops when `i` becomes `6`.

---

# The `continue` Statement

`continue` skips the current iteration.

Example

```javascript
for (let i = 1; i <= 5; i++) {

    if (i === 3) {
        continue;
    }

    console.log(i);

}
```

Output

```text
1
2
4
5
```

---

# Nested Loops

A loop inside another loop is called a nested loop.

Example

```javascript
for (let row = 1; row <= 3; row++) {

    for (let col = 1; col <= 3; col++) {

        console.log(row, col);

    }

}
```

Output

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

Nested loops are useful for:

* Tables
* Matrices
* Chess boards
* Pattern printing

---

# The `for...of` Loop

Used for iterable objects like arrays and strings.

Example with an array

```javascript
let fruits = ["Apple", "Banana", "Orange"];

for (let fruit of fruits) {

    console.log(fruit);

}
```

Output

```text
Apple
Banana
Orange
```

---

# `for...of` with Strings

```javascript
let name = "JavaScript";

for (let letter of name) {

    console.log(letter);

}
```

Output

```text
J
a
v
a
S
c
r
i
p
t
```

---

# The `for...in` Loop

Used for object properties.

Example

```javascript
let student = {

    name: "Navaneeth",
    age: 19,
    course: "CSE"

};

for (let key in student) {

    console.log(key, ":", student[key]);

}
```

Output

```text
name : Navaneeth
age : 19
course : CSE
```

---

# Which Loop Should You Use?

| Situation                    | Best Loop    |
| ---------------------------- | ------------ |
| Known number of iterations   | `for`        |
| Unknown number of iterations | `while`      |
| Run at least once            | `do...while` |
| Arrays and strings           | `for...of`   |
| Object properties            | `for...in`   |

---

# Common Beginner Mistakes

## Forgetting the Update

Wrong

```javascript
let i = 1;

while (i <= 5) {

    console.log(i);

}
```

This creates an infinite loop because `i` never changes.

Correct

```javascript
let i = 1;

while (i <= 5) {

    console.log(i);

    i++;

}
```

---

## Wrong Condition

Wrong

```javascript
for (let i = 1; i >= 5; i++) {
    console.log(i);
}
```

The condition is false from the beginning.

Correct

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

---

## Using `for...in` with Arrays

Avoid

```javascript
let numbers = [10, 20, 30];

for (let index in numbers) {
    console.log(index);
}
```

This prints indexes:

```text
0
1
2
```

Preferred

```javascript
for (let number of numbers) {
    console.log(number);
}
```

Output

```text
10
20
30
```

---

# Real-World Uses

Loops are used in almost every JavaScript application.

Examples:

* Displaying products on Amazon
* Showing Instagram posts
* Reading API responses
* Creating HTML tables
* Validating multiple form fields
* Processing shopping cart items
* Rendering dashboard data
* Animations and game loops

---

# Practice Questions

1. What is a loop?
2. Why do we use loops?
3. Explain the three parts of a `for` loop.
4. What is the difference between `for` and `while`?
5. What is the difference between `while` and `do...while`?
6. What does `break` do?
7. What does `continue` do?
8. What is a nested loop?
9. When should you use `for...of`?
10. When should you use `for...in`?

---

# Coding Exercises

## Exercise 1

Print numbers from **1 to 100**.

---

## Exercise 2

Print numbers from **100 to 1**.

---

## Exercise 3

Print all even numbers between **1 and 50**.

---

## Exercise 4

Print all odd numbers between **1 and 50**.

---

## Exercise 5

Calculate the sum of numbers from **1 to 100**.

Expected Output

```text
5050
```

---

## Exercise 6

Print the multiplication table of **7**.

Expected Output

```text
7 × 1 = 7
7 × 2 = 14
...
7 × 10 = 70
```

---

## Exercise 7

Reverse a string using a loop.

Example

```text
JavaScript
```

Output

```text
tpircSavaJ
```

---

## Exercise 8

Count how many vowels are present in a string.

Example

```text
Programming
```

Output

```text
3
```

---

## Exercise 9

Print this pattern using nested loops.

```text
*
**
***
****
*****
```

---

## Exercise 10

Print this pattern.

```text
1
12
123
1234
12345
```

---

# Mini Project

## Student Marks Analyzer

Create an array of student marks.

Example

```javascript
let marks = [82, 91, 67, 45, 98, 74, 59];
```

Using loops:

* Print all marks.
* Calculate the total marks.
* Calculate the average.
* Find the highest mark.
* Find the lowest mark.
* Count how many students passed (marks ≥ 35).
* Count how many students scored above 90.

This mini project combines loops, conditions, arrays, variables, and logical thinking—the exact skills you'll use in real JavaScript applications.
