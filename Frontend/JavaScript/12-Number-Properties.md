# JavaScript Number Properties

## Introduction

JavaScript provides several built-in **Number Properties** that give us useful information about numbers.

Unlike number methods (such as `toFixed()` or `toString()`), **Number properties do not belong to individual numbers**.

Instead, they belong to the global **`Number` object**.

For example:

```javascript
console.log(Number.MAX_VALUE);
```

Notice that we use:

```javascript
Number
```

and **not**

```javascript
let num = 100;

num.MAX_VALUE ❌
```

This is because `MAX_VALUE` is a property of the **Number object**, not of individual numbers.

---

# Why Number Properties Exist

Imagine you're building:

* Banking software
* Scientific calculator
* Financial application
* Space simulation
* AI application

Sometimes you need to know:

* What's the largest number JavaScript can store?
* What's the smallest number?
* What's the largest safe integer?
* What represents Infinity?
* How does JavaScript handle impossible calculations?

These questions are answered using **Number Properties**.

---

# JavaScript Number Properties

| Property                   | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| `Number.MAX_VALUE`         | Largest possible number                               |
| `Number.MIN_VALUE`         | Smallest positive number                              |
| `Number.MAX_SAFE_INTEGER`  | Largest safe integer                                  |
| `Number.MIN_SAFE_INTEGER`  | Smallest safe integer                                 |
| `Number.POSITIVE_INFINITY` | Positive Infinity                                     |
| `Number.NEGATIVE_INFINITY` | Negative Infinity                                     |
| `Number.EPSILON`           | Smallest difference between two representable numbers |
| `Number.NaN`               | Represents "Not a Number"                             |

---

# Number.MAX_VALUE

## What is it?

`Number.MAX_VALUE` returns the **largest positive number** JavaScript can represent.

Example

```javascript
console.log(Number.MAX_VALUE);
```

Output

```text
1.7976931348623157e+308
```

The output is written in **scientific notation** because the number is extremely large.

---

## Why is it useful?

Suppose you're writing software that performs very large calculations.

If a calculation exceeds this value, JavaScript returns:

```text
Infinity
```

Example

```javascript
console.log(Number.MAX_VALUE * 2);
```

Output

```text
Infinity
```

---

# Number.MIN_VALUE

## What is it?

Returns the **smallest positive number** greater than zero.

Example

```javascript
console.log(Number.MIN_VALUE);
```

Output

```text
5e-324
```

Important:

This is **NOT** the most negative number.

It is the **smallest positive decimal number** JavaScript can store.

---

# Number.MAX_SAFE_INTEGER

## What is a Safe Integer?

JavaScript stores numbers using the **IEEE 754 double-precision floating-point format**.

Because of this, JavaScript can accurately represent integers only up to:

```text
9007199254740991
```

Example

```javascript
console.log(Number.MAX_SAFE_INTEGER);
```

Output

```text
9007199254740991
```

---

## Why is it called "Safe"?

Numbers larger than this may lose precision.

Example

```javascript
console.log(Number.MAX_SAFE_INTEGER + 1);
console.log(Number.MAX_SAFE_INTEGER + 2);
```

Output

```text
9007199254740992
9007199254740992
```

Notice something strange?

Adding **1** and **2** gives the same result.

This happens because JavaScript can no longer represent those integers exactly.

---

# Number.MIN_SAFE_INTEGER

Returns the smallest safe integer.

Example

```javascript
console.log(Number.MIN_SAFE_INTEGER);
```

Output

```text
-9007199254740991
```

---

# Number.POSITIVE_INFINITY

Represents positive infinity.

Example

```javascript
console.log(Number.POSITIVE_INFINITY);
```

Output

```text
Infinity
```

Another example

```javascript
console.log(10 / 0);
```

Output

```text
Infinity
```

---

# Number.NEGATIVE_INFINITY

Represents negative infinity.

Example

```javascript
console.log(Number.NEGATIVE_INFINITY);
```

Output

```text
-Infinity
```

Another example

```javascript
console.log(-10 / 0);
```

Output

```text
-Infinity
```

---

# Number.EPSILON

## What is EPSILON?

`Number.EPSILON` is the **smallest difference between 1 and the next representable number greater than 1**.

Example

```javascript
console.log(Number.EPSILON);
```

Output

```text
2.220446049250313e-16
```

---

## Why is it useful?

Because decimal calculations are sometimes inaccurate.

Example

```javascript
console.log(0.1 + 0.2);
```

Output

```text
0.30000000000000004
```

Instead of comparing decimal numbers directly,

```javascript
let result = 0.1 + 0.2;

console.log(result === 0.3);
```

Output

```text
false
```

Use `Number.EPSILON`.

```javascript
let result = 0.1 + 0.2;

console.log(Math.abs(result - 0.3) < Number.EPSILON);
```

Output

```text
true
```

Professional developers often use this technique when comparing decimal values.

---

# Number.NaN

NaN means:

```text
Not a Number
```

It represents an invalid numeric result.

Example

```javascript
console.log(Number.NaN);
```

Output

```text
NaN
```

Another example

```javascript
console.log(Number("Hello"));
```

Output

```text
NaN
```

---

## Checking for NaN

Instead of writing

```javascript
value === NaN
```

Use

```javascript
Number.isNaN(value);
```

Example

```javascript
let value = Number("Hello");

console.log(Number.isNaN(value));
```

Output

```text
true
```

---

# Checking Safe Integers

JavaScript provides another useful method.

```javascript
console.log(Number.isSafeInteger(100));
```

Output

```text
true
```

Example

```javascript
console.log(Number.isSafeInteger(Number.MAX_SAFE_INTEGER));
```

Output

```text
true
```

Example

```javascript
console.log(Number.isSafeInteger(Number.MAX_SAFE_INTEGER + 1));
```

Output

```text
false
```

---

# Complete Example

```javascript
console.log("MAX_VALUE:", Number.MAX_VALUE);

console.log("MIN_VALUE:", Number.MIN_VALUE);

console.log("MAX_SAFE_INTEGER:", Number.MAX_SAFE_INTEGER);

console.log("MIN_SAFE_INTEGER:", Number.MIN_SAFE_INTEGER);

console.log("POSITIVE_INFINITY:", Number.POSITIVE_INFINITY);

console.log("NEGATIVE_INFINITY:", Number.NEGATIVE_INFINITY);

console.log("EPSILON:", Number.EPSILON);

console.log("NaN:", Number.NaN);
```

Output

```text
MAX_VALUE: 1.7976931348623157e+308
MIN_VALUE: 5e-324
MAX_SAFE_INTEGER: 9007199254740991
MIN_SAFE_INTEGER: -9007199254740991
POSITIVE_INFINITY: Infinity
NEGATIVE_INFINITY: -Infinity
EPSILON: 2.220446049250313e-16
NaN: NaN
```

---

# Summary Table

| Property                   | Returns                       | Example             |
| -------------------------- | ----------------------------- | ------------------- |
| `Number.MAX_VALUE`         | Largest number                | `1.79e+308`         |
| `Number.MIN_VALUE`         | Smallest positive number      | `5e-324`            |
| `Number.MAX_SAFE_INTEGER`  | Largest safe integer          | `9007199254740991`  |
| `Number.MIN_SAFE_INTEGER`  | Smallest safe integer         | `-9007199254740991` |
| `Number.POSITIVE_INFINITY` | Infinity                      | `Infinity`          |
| `Number.NEGATIVE_INFINITY` | Negative Infinity             | `-Infinity`         |
| `Number.EPSILON`           | Smallest precision difference | `2.22e-16`          |
| `Number.NaN`               | Invalid number                | `NaN`               |

---

# Common Beginner Mistakes

## Mistake 1

Wrong

```javascript
let num = 100;

console.log(num.MAX_VALUE);
```

Output

```text
undefined
```

Correct

```javascript
console.log(Number.MAX_VALUE);
```

---

## Mistake 2

Wrong

```javascript
let value = Number("Hello");

if (value === NaN) {
    console.log("Invalid");
}
```

This never works.

Correct

```javascript
if (Number.isNaN(value)) {
    console.log("Invalid");
}
```

---

## Mistake 3

Assuming `MIN_VALUE` means the most negative number.

Wrong understanding:

```text
MIN_VALUE = Most Negative Number
```

Correct understanding:

```text
MIN_VALUE = Smallest Positive Number
```

---

# Real-World Uses

Number properties are commonly used in:

* Financial software
* Banking systems
* Scientific calculations
* Physics simulations
* Data validation
* Graphics engines
* Machine learning
* AI calculations
* Space research
* Game development

---

# Practice Questions

1. What is `Number.MAX_VALUE`?
2. What is the difference between `MIN_VALUE` and `MIN_SAFE_INTEGER`?
3. Why does JavaScript have `MAX_SAFE_INTEGER`?
4. What does `Number.EPSILON` represent?
5. Why shouldn't you compare decimal numbers using `===`?
6. What does `Number.NaN` represent?
7. How do you check if a value is `NaN`?
8. What happens if a number exceeds `Number.MAX_VALUE`?

---

# Coding Exercises

## Exercise 1

Print all Number properties.

---

## Exercise 2

Multiply `Number.MAX_VALUE` by `10` and observe the output.

---

## Exercise 3

Convert `"Hello"` into a number and check whether it is `NaN`.

---

## Exercise 4

Write a program that checks whether a number entered by the user is a **safe integer** using `Number.isSafeInteger()`.

---

## Exercise 5

Compare:

```javascript
0.1 + 0.2
```

with

```javascript
0.3
```

First using `===`, then using `Number.EPSILON`.

Observe the difference.

---

# Mini Challenge

Create a program that accepts user input and determines whether it is:

* A valid number
* `NaN`
* A safe integer
* Positive Infinity
* Negative Infinity

Display meaningful messages for each case.

This challenge combines **Number properties**, **type checking**, **conditional statements**, and **user input**, helping you understand how JavaScript handles numeric values in real-world applications.
