# JavaScript Bitwise Operators

## Introduction

Most JavaScript developers rarely use **Bitwise Operators** in everyday web development.

However, they are important to understand because they are used in:

* Game development
* Graphics programming
* Image processing
* Cryptography
* Compression algorithms
* Low-level system programming
* Performance optimization

Before learning bitwise operators, you must understand **binary numbers**.

---

# What is Binary?

Humans use the **Decimal Number System (Base 10)**.

Example

```text
25
156
999
```

Computers understand only **Binary (Base 2)**.

Binary contains only two digits.

```text
0
1
```

Example

| Decimal | Binary |
| ------: | :----- |
|       0 | 0000   |
|       1 | 0001   |
|       2 | 0010   |
|       3 | 0011   |
|       4 | 0100   |
|       5 | 0101   |
|       6 | 0110   |
|       7 | 0111   |
|       8 | 1000   |

---

# Why Bitwise Operators?

Bitwise operators work on the **binary representation** of numbers.

Example

```javascript
let a = 5;
let b = 3;
```

Binary

```text
5 = 0101
3 = 0011
```

Bitwise operators compare **each bit**.

---

# Bitwise AND (&)

Returns **1 only if both bits are 1**.

Truth Table

| A | B | A & B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 0     |
| 1 | 0 | 0     |
| 1 | 1 | 1     |

Example

```javascript
let a = 5;
let b = 3;

console.log(a & b);
```

Binary

```text
0101
0011
----
0001
```

Output

```text
1
```

---

# Bitwise OR (|)

Returns **1 if at least one bit is 1**.

Truth Table

| A | B | A | B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 1     |

Example

```javascript
console.log(5 | 3);
```

Binary

```text
0101
0011
----
0111
```

Output

```text
7
```

---

# Bitwise XOR (^)

Returns **1 only when bits are different**.

Truth Table

| A | B | A ^ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

Example

```javascript
console.log(5 ^ 3);
```

Binary

```text
0101
0011
----
0110
```

Output

```text
6
```

---

# Bitwise NOT (~)

Flips every bit.

Example

```javascript
console.log(~5);
```

Output

```text
-6
```

Why?

Internally JavaScript stores integers using **32-bit two's complement**, so the result is not simply the opposite number.

A useful identity:

```text
~x = -(x + 1)
```

Example

```text
~5 = -(5 + 1)
   = -6
```

---

# Left Shift (<<)

Moves bits to the left.

Each left shift approximately multiplies the number by **2**.

Example

```javascript
console.log(5 << 1);
```

Binary

```text
0101

↓

1010
```

Output

```text
10
```

Another example

```javascript
console.log(5 << 2);
```

Output

```text
20
```

---

# Right Shift (>>)

Moves bits to the right.

Each shift approximately divides the number by **2**.

Example

```javascript
console.log(20 >> 1);
```

Binary

```text
10100

↓

01010
```

Output

```text
10
```

---

# Unsigned Right Shift (>>>)

Works like `>>` but always fills the leftmost bits with **0**.

Example

```javascript
console.log(-5 >>> 1);
```

Produces a large positive integer because the sign bit is treated as an ordinary bit.

---

# Summary Table

| Operator | Description          |    |
| -------- | -------------------- | -- |
| `&`      | AND                  |    |
| `        | `                    | OR |
| `^`      | XOR                  |    |
| `~`      | NOT                  |    |
| `<<`     | Left Shift           |    |
| `>>`     | Right Shift          |    |
| `>>>`    | Unsigned Right Shift |    |

---

# Real-World Uses

Although uncommon in standard web apps, bitwise operators are used for:

* Graphics rendering
* Image filters
* RGB color manipulation
* Permission flags
* Compression algorithms
* Encryption
* Network protocols

---

# Common Beginner Mistakes

### Assuming Bitwise and Logical Operators Are the Same

Wrong

```javascript
5 & 3
```

This is **bitwise AND**.

Logical AND is:

```javascript
5 && 3
```

These operators have completely different purposes.

---

# Practice Questions

1. What is binary?
2. Why do computers use binary?
3. What is the difference between `&&` and `&`?
4. What does XOR do?
5. What is the difference between `>>` and `>>>`?
6. Why does `~5` return `-6`?

---

# Coding Exercises

### Exercise 1

Find the result of:

```javascript
12 & 5
```

---

### Exercise 2

Find:

```javascript
12 | 5
```

---

### Exercise 3

Find:

```javascript
12 ^ 5
```

---

### Exercise 4

Multiply a number by 2 using only the left shift operator.

---

### Exercise 5

Divide a number by 2 using only the right shift operator.
