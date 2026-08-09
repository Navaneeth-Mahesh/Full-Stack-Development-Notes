# 08 — JavaScript Math Object

> The JavaScript `Math` object is a built-in object that provides properties and methods for performing mathematical calculations.

You do **not** need to create a `Math` object.

You can directly use:

```js
Math.method()
```

Example:

```js
console.log(Math.round(4.6));
```

Output:

```text
5
```

---

# 1. What is the Math Object?

JavaScript provides a built-in object called:

```js
Math
```

It contains useful mathematical methods and constants.

Examples:

```js
Math.PI
Math.E

Math.round()
Math.floor()
Math.ceil()
Math.trunc()

Math.abs()
Math.pow()
Math.sqrt()

Math.min()
Math.max()

Math.random()
```

---

# 2. Math Object Syntax

The general syntax is:

```js
Math.method(value);
```

Example:

```js
const number = 4.7;

console.log(Math.round(number));
```

Output:

```text
5
```

---

# 3. Math Constants

The `Math` object contains several mathematical constants.

Important ones include:

```js
Math.PI
Math.E
Math.SQRT2
Math.SQRT1_2
Math.LN2
Math.LN10
Math.LOG2E
Math.LOG10E
```

---

# 4. Math.PI

`Math.PI` represents the mathematical constant π.

Approximately:

```text
3.141592653589793
```

Example:

```js
console.log(Math.PI);
```

Output:

```text
3.141592653589793
```

---

# 5. Circle Area Using Math.PI

Formula:

```text
Area = π × r²
```

JavaScript:

```js
const radius = 5;

const area = Math.PI * radius ** 2;

console.log(area);
```

Output:

```text
78.53981633974483
```

---

# 6. Circle Circumference

Formula:

```text
Circumference = 2 × π × r
```

Example:

```js
const radius = 5;

const circumference = 2 * Math.PI * radius;

console.log(circumference);
```

Output:

```text
31.41592653589793
```

---

# 7. Math.E

`Math.E` represents Euler's number.

Approximately:

```text
2.718281828459045
```

Example:

```js
console.log(Math.E);
```

---

# 8. Math.round()

`Math.round()` rounds a number to the nearest integer.

Example:

```js
console.log(Math.round(4.4));
```

Output:

```text
4
```

```js
console.log(Math.round(4.5));
```

Output:

```text
5
```

```js
console.log(Math.round(4.8));
```

Output:

```text
5
```

---

# 9. Math.round() Rules

Think:

```text
Decimal < .5 → round down
Decimal >= .5 → round up
```

Examples:

```js
Math.round(10.1); // 10
Math.round(10.4); // 10
Math.round(10.5); // 11
Math.round(10.9); // 11
```

---

# 10. Negative Numbers with Math.round()

Be careful with negative values.

```js
console.log(Math.round(-4.4));
```

Output:

```text
-4
```

```js
console.log(Math.round(-4.5));
```

Output:

```text
-4
```

```js
console.log(Math.round(-4.6));
```

Output:

```text
-5
```

---

# 11. Math.floor()

`Math.floor()` always rounds **down toward negative infinity**.

Example:

```js
console.log(Math.floor(4.9));
```

Output:

```text
4
```

```js
console.log(Math.floor(4.1));
```

Output:

```text
4
```

---

# 12. Math.floor() with Negative Numbers

This is important.

```js
console.log(Math.floor(-4.1));
```

Output:

```text
-5
```

Why?

Because `-5` is lower than `-4.1`.

Think:

```text
-5 < -4.1 < -4
```

So:

```js
Math.floor(-4.1);
```

returns:

```text
-5
```

---

# 13. Math.ceil()

`Math.ceil()` always rounds **up toward positive infinity**.

Example:

```js
console.log(Math.ceil(4.1));
```

Output:

```text
5
```

```js
console.log(Math.ceil(4.9));
```

Output:

```text
5
```

---

# 14. Math.ceil() with Negative Numbers

```js
console.log(Math.ceil(-4.9));
```

Output:

```text
-4
```

Because `-4` is greater than `-4.9`.

---

# 15. Math.trunc()

`Math.trunc()` removes the decimal portion.

Example:

```js
console.log(Math.trunc(4.9));
```

Output:

```text
4
```

```js
console.log(Math.trunc(4.1));
```

Output:

```text
4
```

---

# 16. Math.trunc() with Negative Numbers

```js
console.log(Math.trunc(-4.9));
```

Output:

```text
-4
```

Unlike `Math.floor()`:

```js
Math.floor(-4.9); // -5
```

`Math.trunc()` simply removes the decimal:

```js
Math.trunc(-4.9); // -4
```

---

# 17. round vs floor vs ceil vs trunc

This is extremely important.

```js
const number = 4.7;

console.log(Math.round(number));
console.log(Math.floor(number));
console.log(Math.ceil(number));
console.log(Math.trunc(number));
```

Output:

```text
5
4
5
4
```

For positive numbers, `floor()` and `trunc()` often produce the same result.

But for negative numbers:

```js
const number = -4.7;

console.log(Math.round(number));
console.log(Math.floor(number));
console.log(Math.ceil(number));
console.log(Math.trunc(number));
```

Output:

```text
-5
-5
-4
-4
```

---

# 18. Quick Comparison

| Method         | Purpose         | Example | Result |
| -------------- | --------------- | ------: | -----: |
| `Math.round()` | Nearest integer |   `4.7` |    `5` |
| `Math.floor()` | Down            |   `4.7` |    `4` |
| `Math.ceil()`  | Up              |   `4.1` |    `5` |
| `Math.trunc()` | Remove decimal  |   `4.7` |    `4` |

---

# 19. Math.abs()

`Math.abs()` returns the absolute value.

Example:

```js
console.log(Math.abs(-10));
```

Output:

```text
10
```

```js
console.log(Math.abs(10));
```

Output:

```text
10
```

---

# 20. What is Absolute Value?

Absolute value means:

> Distance from zero.

Examples:

```text
|-10| = 10
|-5|  = 5
|5|   = 5
|10|  = 10
```

JavaScript:

```js
Math.abs(-10); // 10
Math.abs(10);  // 10
Math.abs(-5);  // 5
```

---

# 21. Practical Example — Distance

Suppose:

```js
const positionA = 10;
const positionB = 25;

const distance = Math.abs(positionA - positionB);

console.log(distance);
```

Output:

```text
15
```

---

# 22. Math.pow()

`Math.pow()` calculates powers.

Syntax:

```js
Math.pow(base, exponent)
```

Example:

```js
console.log(Math.pow(2, 3));
```

Output:

```text
8
```

Because:

```text
2³ = 8
```

---

# 23. Math.pow() Examples

```js
Math.pow(5, 2); // 25
Math.pow(2, 4); // 16
Math.pow(10, 3); // 1000
```

---

# 24. Exponentiation Operator

Modern JavaScript provides:

```js
**
```

So instead of:

```js
Math.pow(2, 3);
```

you can write:

```js
2 ** 3;
```

Both produce:

```text
8
```

Example:

```js
const result = 5 ** 2;

console.log(result);
```

Output:

```text
25
```

---

# 25. Math.sqrt()

`Math.sqrt()` calculates the square root.

Example:

```js
console.log(Math.sqrt(25));
```

Output:

```text
5
```

Other examples:

```js
Math.sqrt(9);  // 3
Math.sqrt(16); // 4
Math.sqrt(81); // 9
```

---

# 26. Square Root of Non-Perfect Number

```js
console.log(Math.sqrt(2));
```

Output:

```text
1.4142135623730951
```

You can round it:

```js
console.log(Math.round(Math.sqrt(2)));
```

Output:

```text
1
```

Or limit decimal places:

```js
console.log(Math.sqrt(2).toFixed(2));
```

Output:

```text
1.41
```

---

# 27. Math.cbrt()

`Math.cbrt()` calculates the cube root.

Example:

```js
console.log(Math.cbrt(27));
```

Output:

```text
3
```

Because:

```text
3 × 3 × 3 = 27
```

Examples:

```js
Math.cbrt(8);   // 2
Math.cbrt(64);  // 4
Math.cbrt(125); // 5
```

---

# 28. Math.max()

`Math.max()` returns the largest value.

Example:

```js
console.log(Math.max(10, 20, 5, 30));
```

Output:

```text
30
```

---

# 29. Math.min()

`Math.min()` returns the smallest value.

Example:

```js
console.log(Math.min(10, 20, 5, 30));
```

Output:

```text
5
```

---

# 30. Math.max() with Variables

```js
const a = 10;
const b = 25;
const c = 15;

const largest = Math.max(a, b, c);

console.log(largest);
```

Output:

```text
25
```

---

# 31. Math.min() with Variables

```js
const a = 10;
const b = 25;
const c = 15;

const smallest = Math.min(a, b, c);

console.log(smallest);
```

Output:

```text
10
```

---

# 32. Math.max() with an Array

This does **not** work as expected:

```js
const numbers = [10, 20, 30, 40];

console.log(Math.max(numbers));
```

Result:

```text
NaN
```

Why?

`Math.max()` expects individual arguments.

Use the spread operator:

```js
const numbers = [10, 20, 30, 40];

console.log(Math.max(...numbers));
```

Output:

```text
40
```

---

# 33. Math.min() with an Array

```js
const numbers = [10, 20, 30, 40];

console.log(Math.min(...numbers));
```

Output:

```text
10
```

---

# 34. Math.random()

`Math.random()` generates a pseudo-random number between:

```text
0 inclusive
```

and:

```text
1 exclusive
```

Example:

```js
console.log(Math.random());
```

Possible output:

```text
0.583920173
```

Another run might produce:

```text
0.124837291
```

---

# 35. Math.random() Range

The important rule:

```text
0 <= Math.random() < 1
```

It can return:

```text
0
```

but will never return:

```text
1
```

---

# 36. Random Number from 0 to 9

Use:

```js
const randomNumber = Math.floor(Math.random() * 10);

console.log(randomNumber);
```

Possible results:

```text
0
1
2
3
4
5
6
7
8
9
```

---

# 37. Why `Math.floor()`?

Suppose:

```js
Math.random()
```

returns:

```text
0.73
```

Multiply by 10:

```text
7.3
```

Then:

```js
Math.floor(7.3)
```

gives:

```text
7
```

So:

```js
Math.floor(Math.random() * 10)
```

produces an integer from:

```text
0 → 9
```

---

# 38. Random Number from 1 to 10

To generate:

```text
1 → 10
```

use:

```js
const randomNumber = Math.floor(Math.random() * 10) + 1;

console.log(randomNumber);
```

---

# 39. Random Number from 1 to 100

```js
const randomNumber = Math.floor(Math.random() * 100) + 1;

console.log(randomNumber);
```

Possible values:

```text
1
2
3
...
99
100
```

---

# 40. Random Number from 0 to 100

```js
const randomNumber = Math.floor(Math.random() * 101);

console.log(randomNumber);
```

Possible values:

```text
0 → 100
```

---

# 41. Random Number Between Two Values

A general formula for an integer between `min` and `max`, inclusive:

```js
Math.floor(Math.random() * (max - min + 1)) + min
```

Example:

```js
const min = 10;
const max = 20;

const randomNumber =
  Math.floor(Math.random() * (max - min + 1)) + min;

console.log(randomNumber);
```

Possible values:

```text
10 → 20
```

---

# 42. Create a Reusable Random Function

```js
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(getRandomNumber(1, 10));
console.log(getRandomNumber(50, 100));
```

This is much more reusable.

---

# 43. Random Boolean

You can generate a random boolean:

```js
const result = Math.random() < 0.5;

console.log(result);
```

Possible output:

```text
true
```

or:

```text
false
```

---

# 44. Random Array Element

Suppose:

```js
const fruits = [
  "Apple",
  "Banana",
  "Mango",
  "Orange"
];
```

Select a random fruit:

```js
const randomIndex = Math.floor(Math.random() * fruits.length);

const fruit = fruits[randomIndex];

console.log(fruit);
```

---

# 45. Better Random Array Function

```js
function getRandomElement(array) {
  const index = Math.floor(Math.random() * array.length);

  return array[index];
}

const fruits = [
  "Apple",
  "Banana",
  "Mango",
  "Orange"
];

console.log(getRandomElement(fruits));
```

---

# 46. Math.sign()

`Math.sign()` tells you whether a number is:

```text
negative
positive
zero
```

Example:

```js
console.log(Math.sign(10));
```

Output:

```text
1
```

```js
console.log(Math.sign(-10));
```

Output:

```text
-1
```

```js
console.log(Math.sign(0));
```

Output:

```text
0
```

---

# 47. Math.sign() Examples

```js
Math.sign(100);  // 1
Math.sign(-100); // -1
Math.sign(0);    // 0
Math.sign(-0);   // -0
Math.sign(NaN);  // NaN
```

---

# 48. Math.hypot()

`Math.hypot()` calculates the square root of the sum of squares.

It is useful for calculating distances.

Example:

```js
console.log(Math.hypot(3, 4));
```

Output:

```text
5
```

Because:

```text
√(3² + 4²)
= √(9 + 16)
= √25
= 5
```

---

# 49. Distance Between Two Points

For two-dimensional coordinates:

```text
(x1, y1)
(x2, y2)
```

Distance:

```text
√((x2-x1)² + (y2-y1)²)
```

JavaScript:

```js
const x1 = 2;
const y1 = 3;

const x2 = 8;
const y2 = 11;

const distance = Math.hypot(
  x2 - x1,
  y2 - y1
);

console.log(distance);
```

---

# 50. Math.log()

`Math.log()` calculates the natural logarithm.

Example:

```js
console.log(Math.log(Math.E));
```

Output:

```text
1
```

Because:

```text
ln(e) = 1
```

---

# 51. Math.log10()

Calculates the base-10 logarithm.

```js
console.log(Math.log10(100));
```

Output:

```text
2
```

Because:

```text
10² = 100
```

---

# 52. Math.log2()

Calculates the base-2 logarithm.

```js
console.log(Math.log2(8));
```

Output:

```text
3
```

Because:

```text
2³ = 8
```

---

# 53. Math.exp()

`Math.exp(x)` calculates:

```text
eˣ
```

Example:

```js
console.log(Math.exp(1));
```

Output:

```text
2.718281828459045
```

Because:

```text
e¹ = e
```

---

# 54. Trigonometric Functions

JavaScript's `Math` object provides:

```js
Math.sin()
Math.cos()
Math.tan()

Math.asin()
Math.acos()
Math.atan()
Math.atan2()
```

Important:

> JavaScript trigonometric functions use radians, not degrees.

---

# 55. Math.sin()

```js
console.log(Math.sin(0));
```

Output:

```text
0
```

For 90°:

```js
const radians = Math.PI / 2;

console.log(Math.sin(radians));
```

Output is approximately:

```text
1
```

---

# 56. Math.cos()

For 0 radians:

```js
console.log(Math.cos(0));
```

Output:

```text
1
```

For 90°:

```js
const radians = Math.PI / 2;

console.log(Math.cos(radians));
```

Output is approximately:

```text
0
```

---

# 57. Math.tan()

```js
console.log(Math.tan(0));
```

Output:

```text
0
```

Example:

```js
const radians = Math.PI / 4;

console.log(Math.tan(radians));
```

Output is approximately:

```text
1
```

---

# 58. Degrees to Radians

Formula:

```text
radians = degrees × π / 180
```

JavaScript:

```js
function degreesToRadians(degrees) {
  return degrees * Math.PI / 180;
}

console.log(degreesToRadians(90));
```

Output:

```text
1.5707963267948966
```

---

# 59. Radians to Degrees

Formula:

```text
degrees = radians × 180 / π
```

JavaScript:

```js
function radiansToDegrees(radians) {
  return radians * 180 / Math.PI;
}

console.log(radiansToDegrees(Math.PI));
```

Output:

```text
180
```

---

# 60. Math.atan2()

`Math.atan2(y, x)` calculates the angle from the positive x-axis to a point.

Example:

```js
const x = 1;
const y = 1;

const angle = Math.atan2(y, x);

console.log(angle);
```

The result is approximately:

```text
0.7853981633974483
```

which is:

```text
45°
```

---

# 61. Convert atan2 Result to Degrees

```js
const x = 1;
const y = 1;

const radians = Math.atan2(y, x);

const degrees = radians * 180 / Math.PI;

console.log(degrees);
```

Output:

```text
45
```

---

# 62. Math.clz32()

`Math.clz32()` counts the number of leading zero bits in the 32-bit binary representation of a number.

Example:

```js
console.log(Math.clz32(1));
```

Output:

```text
31
```

This is more advanced and is mainly useful when working with low-level bitwise operations.

---

# 63. Math.imul()

`Math.imul()` performs 32-bit integer multiplication.

Example:

```js
console.log(Math.imul(2, 4));
```

Output:

```text
8
```

This is an advanced method and is mainly useful for low-level numeric operations.

---

# 64. Math.fround()

`Math.fround()` converts a number to the nearest 32-bit single-precision floating-point representation.

Example:

```js
console.log(Math.fround(1.337));
```

The result may look slightly different because 32-bit floating-point numbers cannot represent every decimal exactly.

This is mostly useful for specialized numeric and performance-related work.

---

# 65. Floating-Point Precision

JavaScript uses IEEE 754 double-precision floating-point numbers for ordinary `Number` values.

Therefore:

```js
console.log(0.1 + 0.2);
```

may produce:

```text
0.30000000000000004
```

instead of exactly:

```text
0.3
```

This is a floating-point representation issue, not a `Math` bug.

---

# 66. Handling Decimal Display

If you only want to display a certain number of decimal places:

```js
const result = 0.1 + 0.2;

console.log(result.toFixed(2));
```

Output:

```text
0.30
```

Remember:

> `toFixed()` returns a string.

Example:

```js
const result = (0.1 + 0.2).toFixed(2);

console.log(typeof result);
```

Output:

```text
string
```

---

# 67. Rounding to 2 Decimal Places

A common technique:

```js
const number = 12.34567;

const rounded = Math.round(number * 100) / 100;

console.log(rounded);
```

Output:

```text
12.35
```

However, for financial applications, don't assume ordinary floating-point arithmetic is sufficient for every requirement. Use an appropriate decimal/integer-based strategy when exact monetary calculations matter.

---

# 68. Math Functions Don't Modify the Original Value

Example:

```js
const number = 4.7;

Math.floor(number);

console.log(number);
```

Output:

```text
4.7
```

`Math.floor()` returns a new numeric result.

Correct:

```js
const number = 4.7;

const result = Math.floor(number);

console.log(result);
```

Output:

```text
4
```

---

# 69. Combining Math Methods

You can combine multiple methods.

Example:

```js
const number = -4.7;

const result = Math.abs(Math.floor(number));

console.log(result);
```

Step-by-step:

```text
-4.7
↓
Math.floor()
↓
-5
↓
Math.abs()
↓
5
```

Result:

```text
5
```

---

# 70. Math.max() and Math.min() Together

```js
const numbers = [10, 20, 5, 50, 30];

const largest = Math.max(...numbers);
const smallest = Math.min(...numbers);

console.log(`Largest: ${largest}`);
console.log(`Smallest: ${smallest}`);
```

Output:

```text
Largest: 50
Smallest: 5
```

---

# 71. Practical Project — Circle Calculator

```js
const radius = Number(prompt("Enter radius:"));

const area = Math.PI * radius ** 2;
const circumference = 2 * Math.PI * radius;

console.log(`Area: ${area}`);
console.log(`Circumference: ${circumference}`);
```

---

# 72. Practical Project — Random Dice

A six-sided dice has values:

```text
1 → 6
```

Code:

```js
const dice = Math.floor(Math.random() * 6) + 1;

console.log(`You rolled: ${dice}`);
```

---

# 73. Practical Project — Random Number Generator

```js
const min = Number(prompt("Enter minimum:"));
const max = Number(prompt("Enter maximum:"));

const randomNumber =
  Math.floor(Math.random() * (max - min + 1)) + min;

console.log(`Random number: ${randomNumber}`);
```

---

# 74. Practical Project — Random Password Character

```js
const characters =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

const index = Math.floor(Math.random() * characters.length);

const randomCharacter = characters[index];

console.log(randomCharacter);
```

---

# 75. Practical Project — Generate Random Password

```js
const characters =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";

let password = "";

const length = 12;

for (let i = 0; i < length; i++) {
  const index = Math.floor(Math.random() * characters.length);

  password += characters[index];
}

console.log(password);
```

> For security-sensitive password/token generation, `Math.random()` is not cryptographically secure. Browser applications should use the Web Crypto API instead.

---

# 76. Practical Project — Random Color

```js
const red = Math.floor(Math.random() * 256);
const green = Math.floor(Math.random() * 256);
const blue = Math.floor(Math.random() * 256);

const color = `rgb(${red}, ${green}, ${blue})`;

console.log(color);
```

Possible output:

```text
rgb(125, 42, 220)
```

---

# 77. Practical Project — Temperature Range

```js
const min = -10;
const max = 40;

const temperature =
  Math.floor(Math.random() * (max - min + 1)) + min;

console.log(`Temperature: ${temperature}°C`);
```

---

# 78. Practical Project — Distance Calculator

```js
const x1 = Number(prompt("Enter x1:"));
const y1 = Number(prompt("Enter y1:"));

const x2 = Number(prompt("Enter x2:"));
const y2 = Number(prompt("Enter y2:"));

const distance = Math.hypot(
  x2 - x1,
  y2 - y1
);

console.log(`Distance: ${distance}`);
```

---

# 79. Practical Project — BMI Calculator

```js
const weight = Number(prompt("Enter weight in kg:"));
const height = Number(prompt("Enter height in meters:"));

const bmi = weight / height ** 2;

console.log(`BMI: ${bmi.toFixed(2)}`);
```

---

# 80. Practical Project — Triangle Hypotenuse

Using Pythagoras:

```text
c = √(a² + b²)
```

JavaScript:

```js
const a = Number(prompt("Enter side A:"));
const b = Number(prompt("Enter side B:"));

const c = Math.hypot(a, b);

console.log(`Hypotenuse: ${c}`);
```

---

# 81. Practical Project — Find Largest Number

```js
const a = Number(prompt("Enter number 1:"));
const b = Number(prompt("Enter number 2:"));
const c = Number(prompt("Enter number 3:"));

const largest = Math.max(a, b, c);

console.log(`Largest: ${largest}`);
```

---

# 82. Practical Project — Find Smallest Number

```js
const a = Number(prompt("Enter number 1:"));
const b = Number(prompt("Enter number 2:"));
const c = Number(prompt("Enter number 3:"));

const smallest = Math.min(a, b, c);

console.log(`Smallest: ${smallest}`);
```

---

# 83. Math Object Cheat Sheet

## Rounding

```js
Math.round(4.7);  // 5
Math.floor(4.7);  // 4
Math.ceil(4.1);   // 5
Math.trunc(4.7);  // 4
```

## Absolute Value

```js
Math.abs(-10);    // 10
```

## Powers

```js
Math.pow(2, 3);   // 8
2 ** 3;           // 8
```

## Roots

```js
Math.sqrt(25);    // 5
Math.cbrt(27);    // 3
```

## Minimum / Maximum

```js
Math.min(10, 20, 5); // 5
Math.max(10, 20, 5); // 20
```

## Random

```js
Math.random();
```

## Sign

```js
Math.sign(-10);   // -1
Math.sign(0);     // 0
Math.sign(10);    // 1
```

## Constants

```js
Math.PI
Math.E
Math.SQRT2
Math.SQRT1_2
Math.LN2
Math.LN10
Math.LOG2E
Math.LOG10E
```

## Logarithms

```js
Math.log(x)
Math.log2(x)
Math.log10(x)
```

## Trigonometry

```js
Math.sin(x)
Math.cos(x)
Math.tan(x)

Math.asin(x)
Math.acos(x)
Math.atan(x)
Math.atan2(y, x)
```

## Other Advanced Methods

```js
Math.hypot()
Math.exp()
Math.clz32()
Math.imul()
Math.fround()
```

---

# 84. Most Important Math Methods for Beginners

Focus on these first:

```text
Math.round()
Math.floor()
Math.ceil()
Math.trunc()

Math.abs()

Math.pow()
Math.sqrt()
Math.cbrt()

Math.min()
Math.max()

Math.random()

Math.PI
Math.E
```

These will appear frequently in beginner and intermediate JavaScript projects.

---

# 85. Common Mistakes

## Mistake 1 — Calling Math methods incorrectly

Wrong:

```js
Math.round;
```

This references the function but doesn't call it.

Correct:

```js
Math.round(4.7);
```

---

## Mistake 2 — Forgetting that Math.random() excludes 1

Wrong assumption:

```text
Math.random() → 0 to 1 inclusive
```

Correct:

```text
0 <= Math.random() < 1
```

---

## Mistake 3 — Wrong random range

For `1 → 10`:

```js
Math.floor(Math.random() * 10) + 1;
```

Not:

```js
Math.floor(Math.random() * 10);
```

The second version gives:

```text
0 → 9
```

---

## Mistake 4 — Using Math.max() directly on an array

Wrong:

```js
Math.max([10, 20, 30]);
```

Correct:

```js
Math.max(...[10, 20, 30]);
```

---

## Mistake 5 — Confusing floor and trunc

For:

```js
-4.7
```

```js
Math.floor(-4.7); // -5
Math.trunc(-4.7); // -4
```

Remember:

```text
floor → toward -Infinity
trunc → remove decimal part
```

---

# 86. Interview Questions

### Q1. What is the Math object?

A built-in JavaScript object containing mathematical constants and methods.

---

### Q2. What does `Math.random()` return?

A pseudo-random floating-point number:

```text
0 <= value < 1
```

---

### Q3. How do you generate a random number from 1 to 10?

```js
Math.floor(Math.random() * 10) + 1;
```

---

### Q4. Difference between `Math.floor()` and `Math.ceil()`?

```text
Math.floor() → toward -Infinity
Math.ceil()  → toward +Infinity
```

---

### Q5. Difference between `Math.floor()` and `Math.trunc()`?

For negative decimals:

```js
Math.floor(-4.7); // -5
Math.trunc(-4.7); // -4
```

---

### Q6. How do you find the largest number?

```js
Math.max(10, 20, 30);
```

---

### Q7. How do you find the smallest number?

```js
Math.min(10, 20, 30);
```

---

### Q8. How do you calculate a square root?

```js
Math.sqrt(25);
```

---

### Q9. How do you calculate a power?

```js
Math.pow(2, 3);
```

or:

```js
2 ** 3;
```

---

### Q10. What does `Math.abs()` do?

It returns the absolute value.

```js
Math.abs(-10); // 10
```

---

# 87. Practice Problems

## Beginner

### Problem 1

Round:

```text
4.7
```

using `Math.round()`.

---

### Problem 2

Find the floor of:

```text
9.99
```

---

### Problem 3

Find the ceiling of:

```text
5.01
```

---

### Problem 4

Find the absolute value of:

```text
-500
```

---

### Problem 5

Find the square root of:

```text
144
```

---

## Intermediate

### Problem 6

Generate a random number from:

```text
1 → 50
```

---

### Problem 7

Find the largest number:

```text
25, 67, 12, 89, 34
```

---

### Problem 8

Find the smallest number:

```text
25, 67, 12, 89, 34
```

---

### Problem 9

Calculate the area of a circle with radius `10`.

---

### Problem 10

Calculate the distance between:

```text
(2, 3)
(8, 11)
```

---

# 88. Mini Challenge

Create a program that generates **10 random numbers between 1 and 100**.

Expected structure:

```js
for (let i = 1; i <= 10; i++) {
  const number = Math.floor(Math.random() * 100) + 1;

  console.log(number);
}
```

---

# 89. Mini Challenge — Random Dice Game

Generate two dice rolls:

```js
const dice1 = Math.floor(Math.random() * 6) + 1;
const dice2 = Math.floor(Math.random() * 6) + 1;

const total = dice1 + dice2;

console.log(`Dice 1: ${dice1}`);
console.log(`Dice 2: ${dice2}`);
console.log(`Total: ${total}`);
```

---

# 90. Mini Challenge — Random Team Picker

```js
const players = [
  "Alex",
  "John",
  "Sam",
  "David",
  "Mike"
];

const index = Math.floor(Math.random() * players.length);

console.log(`Selected player: ${players[index]}`);
```

---

# 91. Mini Challenge — Random Choice

```js
const choices = [
  "Rock",
  "Paper",
  "Scissors"
];

const index = Math.floor(Math.random() * choices.length);

console.log(`Computer chose: ${choices[index]}`);
```

This concept will be useful later when building:

```text
Rock Paper Scissors
Dice Roller
Number Guessing Game
Random Password Generator
Games
Randomized UI
Array Shuffling
```

---

# 92. Final Mental Model

Think of the `Math` object as your JavaScript mathematical toolbox:

```text
                    Math
                      │
       ┌──────────────┼──────────────┐
       │              │              │
    Rounding        Numbers       Random
       │              │              │
   round()          abs()         random()
   floor()          min()
   ceil()           max()
   trunc()          pow()
                    sqrt()
                    cbrt()
       │              │              │
       └──────────────┼──────────────┘
                      │
                  Advanced
                      │
             sin / cos / tan
             log / log2 / log10
             hypot / exp
```

---

# 93. Final Checklist

Before moving to Topic 09, make sure you can explain and use:

* [ ] `Math`
* [ ] `Math.PI`
* [ ] `Math.E`
* [ ] `Math.round()`
* [ ] `Math.floor()`
* [ ] `Math.ceil()`
* [ ] `Math.trunc()`
* [ ] `Math.abs()`
* [ ] `Math.pow()`
* [ ] `**`
* [ ] `Math.sqrt()`
* [ ] `Math.cbrt()`
* [ ] `Math.min()`
* [ ] `Math.max()`
* [ ] `Math.random()`
* [ ] Random integer ranges
* [ ] Random array elements
* [ ] `Math.sign()`
* [ ] `Math.hypot()`
* [ ] `Math.log()`
* [ ] `Math.log2()`
* [ ] `Math.log10()`
* [ ] `Math.exp()`
* [ ] `Math.sin()`
* [ ] `Math.cos()`
* [ ] `Math.tan()`
* [ ] Degrees ↔ radians
* [ ] Floating-point precision
* [ ] Combining Math methods
* [ ] Real-world Math programs

---

# 94. One-Line Summary

> **The JavaScript `Math` object provides built-in constants and methods for rounding, random numbers, powers, roots, comparisons, trigonometry, logarithms, and many other mathematical operations.**
