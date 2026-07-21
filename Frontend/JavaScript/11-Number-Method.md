# JavaScript Number Methods

## Introduction

JavaScript provides many **built-in methods** for working with numbers.

These methods help us:

* Convert numbers into strings
* Format decimal values
* Display numbers in different styles
* Format numbers based on a country's locale
* Control precision
* Work with exponential notation

Instead of writing complex logic ourselves, JavaScript already provides these methods.

---

# What is a Number Method?

A **method** is a function that belongs to an object.

Example:

```javascript
let price = 199.99;

console.log(price.toFixed(2));
```

Here,

* `price` is a Number.
* `toFixed()` is a method.
* The method performs an operation and returns a new value.

---

# Number Methods Overview

| Method             | Purpose                             |
| ------------------ | ----------------------------------- |
| `toString()`       | Converts a number to a string       |
| `toFixed()`        | Formats decimal places              |
| `toPrecision()`    | Formats total significant digits    |
| `toExponential()`  | Converts to exponential notation    |
| `valueOf()`        | Returns the primitive value         |
| `toLocaleString()` | Formats numbers according to locale |

---

# 1. toString()

## What is it?

`toString()` converts a **Number** into a **String**.

---

## Syntax

```javascript
number.toString();
```

---

## Example

```javascript
let age = 20;

let result = age.toString();

console.log(result);
console.log(typeof result);
```

Output

```text
20
string
```

---

## Why Use It?

Suppose you're displaying a number with text.

```javascript
let price = 499;

let message = "Price: " + price.toString();

console.log(message);
```

Output

```text
Price: 499
```

---

## Without toString()

JavaScript often converts automatically, but explicit conversion makes your code clearer.

---

# 2. toFixed()

## What is it?

`toFixed()` formats a number to a specified number of decimal places.

---

## Syntax

```javascript
number.toFixed(decimalPlaces);
```

---

## Example 1

```javascript
let price = 199.4567;

console.log(price.toFixed(2));
```

Output

```text
199.46
```

JavaScript rounds the value automatically.

---

## Example 2

```javascript
let num = 12;

console.log(num.toFixed(3));
```

Output

```text
12.000
```

---

## Example 3

```javascript
let pi = 3.141592653;

console.log(pi.toFixed(4));
```

Output

```text
3.1416
```

---

## Real-World Uses

* Currency
* Prices
* Banking applications
* Shopping carts
* Reports

Example

```javascript
let amount = 1250.56789;

console.log(`₹${amount.toFixed(2)}`);
```

Output

```text
₹1250.57
```

---

# Important Note

`toFixed()` returns a **string**, not a number.

```javascript
let price = 25.678;

let result = price.toFixed(2);

console.log(typeof result);
```

Output

```text
string
```

---

# 3. toPrecision()

## What is it?

`toPrecision()` formats a number to a specified number of **significant digits**.

Unlike `toFixed()`, it considers the **entire number**, not just decimal places.

---

## Syntax

```javascript
number.toPrecision(totalDigits);
```

---

## Example

```javascript
let num = 123.456;

console.log(num.toPrecision(4));
```

Output

```text
123.5
```

---

Another Example

```javascript
let num = 123.456;

console.log(num.toPrecision(2));
```

Output

```text
1.2e+2
```

---

## Difference Between toFixed() and toPrecision()

```javascript
let num = 123.456;
```

Using `toFixed()`

```javascript
console.log(num.toFixed(2));
```

Output

```text
123.46
```

Using `toPrecision()`

```javascript
console.log(num.toPrecision(4));
```

Output

```text
123.5
```

---

# Real-World Uses

Useful when:

* Scientific calculations
* Engineering software
* Physics simulations
* Financial calculations

---

# 4. toExponential()

## What is it?

Converts a number into **scientific notation**.

---

## Syntax

```javascript
number.toExponential(decimalPlaces);
```

---

## Example

```javascript
let num = 125000;

console.log(num.toExponential());
```

Output

```text
1.25e+5
```

Meaning

```text
1.25 × 10⁵
```

---

Another Example

```javascript
let num = 1234.5678;

console.log(num.toExponential(2));
```

Output

```text
1.23e+3
```

---

# Real-World Uses

Scientific notation is used in:

* Physics
* Astronomy
* Chemistry
* Data science

---

# 5. valueOf()

## What is it?

Returns the primitive numeric value.

Normally, JavaScript does this automatically.

---

## Example

```javascript
let num = 100;

console.log(num.valueOf());
```

Output

```text
100
```

---

Example with Number Object

```javascript
let num = new Number(50);

console.log(num.valueOf());
```

Output

```text
50
```

---

## Why It Exists

Useful when working with **Number Objects** instead of primitive numbers.

In everyday programming, you rarely need to call it yourself.

---

# 6. toLocaleString()

## What is it?

Formats numbers according to a country's numbering system.

---

## Example

```javascript
let number = 1234567;

console.log(number.toLocaleString());
```

Possible Output

```text
1,234,567
```

---

## Indian Number Format

```javascript
let amount = 12345678;

console.log(amount.toLocaleString("en-IN"));
```

Output

```text
1,23,45,678
```

---

## US Number Format

```javascript
console.log(amount.toLocaleString("en-US"));
```

Output

```text
12,345,678
```

---

## Currency Formatting

```javascript
let amount = 2500;

console.log(
    amount.toLocaleString("en-IN", {
        style: "currency",
        currency: "INR"
    })
);
```

Output

```text
₹2,500.00
```

---

Another Example

```javascript
console.log(
    amount.toLocaleString("en-US", {
        style: "currency",
        currency: "USD"
    })
);
```

Output

```text
$2,500.00
```

---

# Method Chaining

Methods can be combined.

Example

```javascript
let price = 12345.6789;

console.log(
    Number(price.toFixed(2)).toLocaleString("en-IN")
);
```

Output

```text
12,345.68
```

---

# Comparison of Number Methods

| Method             | Returns | Purpose                  |
| ------------------ | ------- | ------------------------ |
| `toString()`       | String  | Convert number to string |
| `toFixed()`        | String  | Fixed decimal places     |
| `toPrecision()`    | String  | Significant digits       |
| `toExponential()`  | String  | Scientific notation      |
| `valueOf()`        | Number  | Primitive number         |
| `toLocaleString()` | String  | Locale-based formatting  |

---

# Common Beginner Mistakes

## Mistake 1

Thinking `toFixed()` returns a number.

Wrong

```javascript
let result = (12.567).toFixed(2);

console.log(typeof result);
```

Output

```text
string
```

Convert back if needed.

```javascript
let result = Number((12.567).toFixed(2));
```

---

## Mistake 2

Confusing `toFixed()` and `toPrecision()`.

```javascript
let num = 123.456;

console.log(num.toFixed(2));
```

Output

```text
123.46
```

```javascript
console.log(num.toPrecision(2));
```

Output

```text
1.2e+2
```

They serve different purposes.

---

## Mistake 3

Using `toLocaleString()` for calculations.

```javascript
let amount = 1000;

let formatted = amount.toLocaleString();
```

Output

```text
1,000
```

This is **display text**, not a value for mathematical operations.

---

# Real-World Uses

These methods are used in:

* Banking systems
* Shopping websites
* Financial dashboards
* GST invoices
* Currency converters
* Scientific applications
* Data visualization
* Reports
* Accounting software

---

# Practice Questions

1. What is a Number method?
2. What is the difference between `toString()` and `valueOf()`?
3. What does `toFixed()` do?
4. What is the difference between `toFixed()` and `toPrecision()`?
5. Why is `toExponential()` useful?
6. What does `toLocaleString()` do?
7. Which Number methods return a string?
8. Why does `toFixed()` return a string instead of a number?

---

# Coding Exercises

## Exercise 1

Convert the number `500` into a string.

Print its data type.

---

## Exercise 2

Round the following number to:

* 1 decimal place
* 2 decimal places
* 4 decimal places

```text
15.678923
```

---

## Exercise 3

Use `toPrecision()` with:

```text
1234.56789
```

Print the result using:

* 2 digits
* 4 digits
* 6 digits

---

## Exercise 4

Convert the following number into exponential notation.

```text
987654321
```

---

## Exercise 5

Display the number:

```text
123456789
```

In:

* Indian format
* US format

Using `toLocaleString()`.

---

## Exercise 6

Display the amount:

```text
45899.5
```

As:

* Indian Rupees
* US Dollars

Using `toLocaleString()`.

---

## Exercise 7

Take a decimal number from the user.

Display:

* Original value
* `toFixed(2)`
* `toPrecision(4)`
* `toExponential(2)`

---

# Mini Project — Bill Formatter

Create a simple billing program.

```javascript
let product = "Laptop";
let price = 54999.756;
let quantity = 2;
```

Calculate:

* Total Price
* Display total with **2 decimal places**
* Display total in **Indian currency format**
* Display total in **US currency format**

Expected Output

```text
Product : Laptop
Price   : ₹54,999.76
Quantity: 2

Total   : ₹109,999.51

US Total: $109,999.51
```

This mini project combines arithmetic operations, formatting methods, currency formatting, and string interpolation—skills commonly used in real-world e-commerce and billing applications.
