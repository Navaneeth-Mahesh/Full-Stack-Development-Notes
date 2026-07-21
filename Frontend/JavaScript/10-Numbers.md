# JavaScript Numbers

## Introduction

Numbers are one of the **primitive data types** in JavaScript.

A **Number** represents numeric values that can be used for calculations, comparisons, measurements, counting, and mathematical operations.

Examples:

```javascript
10
25
100
3.14
-50
0
```

In JavaScript, **integers** and **decimal numbers** are both represented using the same data type:

```javascript
Number
```

Unlike some programming languages (such as Java or C++), JavaScript does **not** have separate data types like:

* int
* float
* double

Everything is simply a **Number**.

---

# Why Do We Need Numbers?

Numbers are used everywhere in programming.

Examples:

* User age
* Product price
* Student marks
* Bank balance
* Shopping cart total
* Game score
* Distance
* Temperature
* Ratings
* Calculations

Without numbers, computers cannot perform calculations.

---

# Creating Numbers

Numbers can be stored directly inside variables.

```javascript
let age = 19;
let marks = 92;
let price = 499.99;
let temperature = -5;
```

---

# Types of Numbers

Although JavaScript has only one Number type, numbers can appear in different forms.

---

## Integer

Whole numbers without decimal points.

```javascript
let students = 45;
let score = 100;
```

---

## Decimal (Floating Point)

Numbers with decimal values.

```javascript
let pi = 3.14159;
let salary = 25345.75;
```

---

## Negative Numbers

```javascript
let temperature = -12;
```

---

## Zero

```javascript
let balance = 0;
```

---

# Checking Number Type

Use the `typeof` operator.

```javascript
let age = 19;

console.log(typeof age);
```

Output

```text
number
```

Another example

```javascript
console.log(typeof 3.14);
```

Output

```text
number
```

Even decimal numbers return:

```text
number
```

---

# Number Operations

JavaScript supports basic arithmetic.

---

## Addition

```javascript
let a = 10;
let b = 5;

console.log(a + b);
```

Output

```text
15
```

---

## Subtraction

```javascript
console.log(a - b);
```

Output

```text
5
```

---

## Multiplication

```javascript
console.log(a * b);
```

Output

```text
50
```

---

## Division

```javascript
console.log(a / b);
```

Output

```text
2
```

---

## Modulus (%)

Returns the remainder.

```javascript
console.log(10 % 3);
```

Output

```text
1
```

Useful for:

* Even/Odd checking
* Cyclic operations

---

## Exponent (**)

Raises a number to a power.

```javascript
console.log(2 ** 3);
```

Output

```text
8
```

Meaning:

```text
2 × 2 × 2
```

---

# Increment Operator

Increases a value by 1.

```javascript
let count = 5;

count++;

console.log(count);
```

Output

```text
6
```

Equivalent to:

```javascript
count = count + 1;
```

---

# Decrement Operator

Decreases a value by 1.

```javascript
let count = 5;

count--;

console.log(count);
```

Output

```text
4
```

---

# Compound Assignment Operators

Instead of writing:

```javascript
let marks = 50;

marks = marks + 10;
```

Use:

```javascript
marks += 10;
```

Other operators

```javascript
marks -= 5;
marks *= 2;
marks /= 4;
marks %= 3;
```

---

# Floating Point Precision

Computers store decimal numbers in binary.

Because of this, some calculations are not perfectly accurate.

Example

```javascript
console.log(0.1 + 0.2);
```

Output

```text
0.30000000000000004
```

This is **not a JavaScript bug**.

It happens because computers cannot represent some decimal values exactly in binary.

---

# Converting Strings to Numbers

Suppose the user enters:

```text
25
```

User input is always stored as a string.

```javascript
let age = "25";
```

To convert it into a number:

---

## Number()

```javascript
let age = "25";

console.log(Number(age));
```

Output

```text
25
```

---

## parseInt()

Converts only the integer part.

```javascript
console.log(parseInt("45.89"));
```

Output

```text
45
```

---

## parseFloat()

Converts decimal numbers.

```javascript
console.log(parseFloat("45.89"));
```

Output

```text
45.89
```

---

# Checking for NaN

NaN means:

```text
Not a Number
```

Example

```javascript
let value = Number("Hello");

console.log(value);
```

Output

```text
NaN
```

To check it:

```javascript
console.log(Number.isNaN(value));
```

Output

```text
true
```

---

# Infinity

JavaScript supports infinity.

Example

```javascript
console.log(5 / 0);
```

Output

```text
Infinity
```

Negative infinity

```javascript
console.log(-5 / 0);
```

Output

```text
-Infinity
```

---

# Number Properties

---

## Number.MAX_VALUE

Largest possible number.

```javascript
console.log(Number.MAX_VALUE);
```

---

## Number.MIN_VALUE

Smallest positive number.

```javascript
console.log(Number.MIN_VALUE);
```

---

## Number.MAX_SAFE_INTEGER

Largest safe integer.

```javascript
console.log(Number.MAX_SAFE_INTEGER);
```

Output

```text
9007199254740991
```

---

## Number.MIN_SAFE_INTEGER

```javascript
console.log(Number.MIN_SAFE_INTEGER);
```

---

# Useful Number Methods

---

# toFixed()

Rounds to a fixed number of decimal places.

```javascript
let price = 199.4567;

console.log(price.toFixed(2));
```

Output

```text
199.46
```

---

# toString()

Converts a number into a string.

```javascript
let age = 20;

console.log(age.toString());
```

Output

```text
"20"
```

---

# valueOf()

Returns the primitive value.

```javascript
let num = 100;

console.log(num.valueOf());
```

Output

```text
100
```

---

# The Math Object

JavaScript provides a built-in object called `Math`.

It contains useful mathematical functions.

---

# Math.round()

Rounds to the nearest integer.

```javascript
console.log(Math.round(4.6));
```

Output

```text
5
```

---

# Math.floor()

Rounds down.

```javascript
console.log(Math.floor(4.9));
```

Output

```text
4
```

---

# Math.ceil()

Rounds up.

```javascript
console.log(Math.ceil(4.1));
```

Output

```text
5
```

---

# Math.trunc()

Removes the decimal part.

```javascript
console.log(Math.trunc(4.99));
```

Output

```text
4
```

---

# Math.abs()

Returns absolute value.

```javascript
console.log(Math.abs(-25));
```

Output

```text
25
```

---

# Math.sqrt()

Square root.

```javascript
console.log(Math.sqrt(64));
```

Output

```text
8
```

---

# Math.pow()

Power calculation.

```javascript
console.log(Math.pow(2, 5));
```

Output

```text
32
```

Modern JavaScript also supports:

```javascript
console.log(2 ** 5);
```

---

# Math.min()

```javascript
console.log(Math.min(5, 2, 9, 1));
```

Output

```text
1
```

---

# Math.max()

```javascript
console.log(Math.max(5, 2, 9, 1));
```

Output

```text
9
```

---

# Math.random()

Returns a random number between:

```text
0 and 1
```

```javascript
console.log(Math.random());
```

Example Output

```text
0.723456781
```

---

# Random Number Between 1 and 10

```javascript
let random = Math.floor(Math.random() * 10) + 1;

console.log(random);
```

Possible Output

```text
7
```

Every run produces a different value.

---

# Comparing Numbers

```javascript
let a = 25;
let b = 30;

console.log(a > b);
console.log(a < b);
console.log(a === b);
console.log(a !== b);
```

Output

```text
false
true
false
true
```

---

# Common Beginner Mistakes

## Adding Strings Instead of Numbers

Wrong

```javascript
let a = "10";
let b = "20";

console.log(a + b);
```

Output

```text
1020
```

Correct

```javascript
let a = Number("10");
let b = Number("20");

console.log(a + b);
```

Output

```text
30
```

---

## Forgetting Number Conversion

Wrong

```javascript
let age = prompt("Enter Age");

console.log(age + 5);
```

Input

```text
20
```

Output

```text
205
```

Correct

```javascript
let age = Number(prompt("Enter Age"));

console.log(age + 5);
```

Output

```text
25
```

---

## Comparing Strings Instead of Numbers

Wrong

```javascript
console.log("100" > "20");
```

String comparison compares characters, not numeric values.

Always convert to numbers when performing calculations or numeric comparisons.

---

# Real-World Uses

Numbers are used in almost every application.

Examples

* Online banking
* Shopping websites
* Game scores
* Student marks
* Attendance systems
* Weather applications
* Financial dashboards
* GPS distance calculations
* Payment gateways
* Analytics reports

---

# Practice Questions

1. What is the Number data type?
2. Does JavaScript have separate `int` and `float` types?
3. What is the difference between `Number()` and `parseInt()`?
4. What does `NaN` mean?
5. Why does `0.1 + 0.2` produce an unexpected result?
6. What is the purpose of the `Math` object?
7. What is the difference between `Math.floor()` and `Math.ceil()`?
8. What does `toFixed()` do?
9. How do you generate a random number between 1 and 100?
10. What is `Number.isNaN()` used for?

---

# Coding Exercises

## Exercise 1

Take two numbers and display:

* Addition
* Subtraction
* Multiplication
* Division
* Modulus
* Exponent

---

## Exercise 2

Ask the user to enter their age.

Convert the input to a number and print:

```text
You are 20 years old.
```

---

## Exercise 3

Calculate the area of a rectangle.

Formula:

```text
Area = Length × Width
```

---

## Exercise 4

Generate a random number between **1 and 50**.

---

## Exercise 5

Round the following number using:

* `Math.round()`
* `Math.floor()`
* `Math.ceil()`
* `Math.trunc()`

```text
25.87
```

---

## Exercise 6

Check whether the user's input is a valid number.

If valid:

```text
Valid Number
```

Otherwise:

```text
Invalid Number
```

---

## Exercise 7

Convert:

```text
"125.75"
```

Using:

* `Number()`
* `parseInt()`
* `parseFloat()`

Print the result of each conversion.

---

## Exercise 8

Build a simple calculator.

Ask the user for:

* First number
* Second number

Display:

* Addition
* Subtraction
* Multiplication
* Division
* Modulus

---

# Mini Project — Student Percentage Calculator

Create a program that:

1. Accepts marks for **5 subjects**.
2. Calculates:

   * Total marks
   * Average marks
   * Percentage
3. Displays:

   * Total
   * Average
   * Percentage
4. Determines the result:

   * Percentage ≥ 90 → Grade A+
   * Percentage ≥ 75 → Grade A
   * Percentage ≥ 60 → Grade B
   * Percentage ≥ 35 → Grade C
   * Otherwise → Fail

This mini project combines **numbers, arithmetic operators, user input, conditional statements, and basic calculations**, making it excellent practice for mastering JavaScript Numbers.
