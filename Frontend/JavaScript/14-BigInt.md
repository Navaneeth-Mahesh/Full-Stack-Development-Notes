# JavaScript BigInt

## Introduction

JavaScript's `Number` type can safely represent integers only up to a certain limit.

This limit is:

```javascript
Number.MAX_SAFE_INTEGER
```

Output

```text
9007199254740991
```

Any integer larger than this may lose precision.

To solve this problem, JavaScript introduced **BigInt**.

A **BigInt** allows you to work with integers of **arbitrary size**.

---

# Why BigInt Exists

Example

```javascript
let num = 9007199254740991;

console.log(num + 1);
console.log(num + 2);
```

Output

```text
9007199254740992
9007199254740992
```

The second result is incorrect because JavaScript cannot safely represent integers larger than `MAX_SAFE_INTEGER`.

BigInt solves this limitation.

---

# Creating a BigInt

## Method 1 — Using `n`

```javascript
let big = 123456789012345678901234567890n;

console.log(big);
```

---

## Method 2 — Using `BigInt()`

```javascript
let big = BigInt("123456789012345678901234567890");

console.log(big);
```

---

# Checking the Type

```javascript
let big = 100n;

console.log(typeof big);
```

Output

```text
bigint
```

---

# Arithmetic Operations

Addition

```javascript
let a = 100n;
let b = 20n;

console.log(a + b);
```

Output

```text
120n
```

---

Subtraction

```javascript
console.log(a - b);
```

Output

```text
80n
```

---

Multiplication

```javascript
console.log(a * b);
```

Output

```text
2000n
```

---

Division

```javascript
console.log(a / b);
```

Output

```text
5n
```

BigInt division **does not keep decimal values**.

Example

```javascript
console.log(5n / 2n);
```

Output

```text
2n
```

---

# Comparison

```javascript
console.log(10n > 5n);
```

Output

```text
true
```

---

# Equality

```javascript
console.log(10n == 10);
```

Output

```text
true
```

But

```javascript
console.log(10n === 10);
```

Output

```text
false
```

Reason:

```text
bigint ≠ number
```

---

# Mixing Number and BigInt

Wrong

```javascript
let a = 10n;
let b = 5;

console.log(a + b);
```

Output

```text
TypeError
```

Convert one type first.

```javascript
console.log(a + BigInt(b));
```

or

```javascript
console.log(Number(a) + b);
```

---

# Safe Integer Check

```javascript
console.log(Number.isSafeInteger(100));
```

Output

```text
true
```

Example

```javascript
console.log(Number.isSafeInteger(9007199254740995));
```

Output

```text
false
```

---

# Limitations of BigInt

BigInt **cannot** represent decimal values.

Wrong

```javascript
123.45n
```

This causes a syntax error.

BigInt stores **only integers**.

---

# When Should You Use BigInt?

Use BigInt when working with:

* Banking systems
* Cryptography
* Blockchain
* Scientific calculations
* Large IDs
* Large counters
* Financial software

For normal web applications, the `Number` type is usually sufficient.

---

# Number vs BigInt

| Feature             | Number   | BigInt    |
| ------------------- | -------- | --------- |
| Decimal values      | Yes      | No        |
| Very large integers | No       | Yes       |
| Safe integer limit  | Yes      | Unlimited |
| Type                | `number` | `bigint`  |

---

# Common Beginner Mistakes

### Forgetting the `n`

Wrong

```javascript
let big = 999999999999999999999999;
```

Correct

```javascript
let big = 999999999999999999999999n;
```

---

### Mixing Types

Wrong

```javascript
10n + 5
```

Correct

```javascript
10n + BigInt(5)
```

---

# Practice Questions

1. Why was BigInt introduced?
2. What is `Number.MAX_SAFE_INTEGER`?
3. How do you create a BigInt?
4. Why can't BigInt store decimal values?
5. Why does `10n === 10` return `false`?

---

# Coding Exercises

### Exercise 1

Create a BigInt containing a 30-digit number.

---

### Exercise 2

Add two BigInt values.

---

### Exercise 3

Multiply two BigInt values.

---

### Exercise 4

Compare two BigInt numbers.

---

### Exercise 5

Check whether the following number is safe:

```javascript
9007199254740995
```

using

```javascript
Number.isSafeInteger()
```

---

