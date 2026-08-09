# 03 — JavaScript Arithmetic Operators

> Arithmetic operators are used to perform mathematical calculations in JavaScript.

They are used everywhere in programming:

* Calculating prices
* Calculating marks
* Counting items
* Calculating percentages
* Converting units
* Calculating distances
* Working with time
* Building games
* Processing data

---

# 1. What Are Arithmetic Operators?

Arithmetic operators perform mathematical operations on values.

Example:

```js
const a = 10;
const b = 5;

console.log(a + b);
```

Output:

```text
15
```

Here:

```text
a → 10
b → 5
+ → arithmetic operator
```

---

# 2. JavaScript Arithmetic Operators

The main arithmetic operators are:

| Operator | Name                | Example  |  Result |
| -------- | ------------------- | -------- | ------: |
| `+`      | Addition            | `10 + 5` |    `15` |
| `-`      | Subtraction         | `10 - 5` |     `5` |
| `*`      | Multiplication      | `10 * 5` |    `50` |
| `/`      | Division            | `10 / 5` |     `2` |
| `%`      | Remainder / Modulus | `10 % 3` |     `1` |
| `**`     | Exponentiation      | `2 ** 3` |     `8` |
| `++`     | Increment           | `x++`    | `x + 1` |
| `--`     | Decrement           | `x--`    | `x - 1` |

---

# 3. Addition `+`

The `+` operator adds numbers.

```js
const a = 10;
const b = 20;

const result = a + b;

console.log(result);
```

Output:

```text
30
```

---

# 4. Addition with Decimal Numbers

```js
const price1 = 99.50;
const price2 = 50.25;

console.log(price1 + price2);
```

Output:

```text
149.75
```

---

# 5. Adding More Than Two Numbers

```js
const total = 10 + 20 + 30 + 40;

console.log(total);
```

Output:

```text
100
```

JavaScript evaluates the expression from left to right when operators have the same precedence.

---

# 6. Addition with Variables

```js
const price = 500;
const deliveryFee = 50;

const total = price + deliveryFee;

console.log(total);
```

Output:

```text
550
```

---

# 7. Subtraction `-`

The `-` operator subtracts one number from another.

```js
const a = 20;
const b = 5;

console.log(a - b);
```

Output:

```text
15
```

---

# 8. Subtraction Can Produce Negative Numbers

```js
const balance = 100;

const expense = 150;

console.log(balance - expense);
```

Output:

```text
-50
```

Negative numbers are completely valid in JavaScript.

---

# 9. Multiplication `*`

The `*` operator multiplies values.

```js
const price = 500;
const quantity = 3;

const total = price * quantity;

console.log(total);
```

Output:

```text
1500
```

---

# 10. Multiplication Example

```js
const length = 10;
const width = 5;

const area = length * width;

console.log(area);
```

Output:

```text
50
```

---

# 11. Division `/`

The `/` operator divides one number by another.

```js
const total = 100;
const people = 4;

const share = total / people;

console.log(share);
```

Output:

```text
25
```

---

# 12. JavaScript Division Produces Decimals

Unlike some languages, JavaScript's regular `/` operator produces a number that may contain a fractional part.

```js
console.log(5 / 2);
```

Output:

```text
2.5
```

Another example:

```js
console.log(10 / 3);
```

Output:

```text
3.3333333333333335
```

---

# 13. Division by Zero

JavaScript does not throw a normal arithmetic exception for numeric division by zero.

```js
console.log(10 / 0);
```

Output:

```text
Infinity
```

And:

```js
console.log(-10 / 0);
```

Output:

```text
-Infinity
```

But:

```js
console.log(0 / 0);
```

Output:

```text
NaN
```

`NaN` means:

> Not a Number

---

# 14. Remainder / Modulus `%`

The `%` operator returns the remainder after division.

Example:

```js
console.log(10 % 3);
```

Output:

```text
1
```

Because:

```text
10 ÷ 3 = 3 remainder 1
```

---

# 15. More Modulus Examples

```js
console.log(10 % 2);
console.log(10 % 3);
console.log(20 % 6);
console.log(15 % 4);
```

Output:

```text
0
1
2
3
```

---

# 16. Why Is `%` Useful?

The modulus operator is extremely useful for checking whether numbers are even or odd.

Even:

```js
const number = 10;

console.log(number % 2);
```

Output:

```text
0
```

Odd:

```js
const number = 7;

console.log(number % 2);
```

Output:

```text
1
```

Therefore:

```js
if (number % 2 === 0) {
    console.log("Even");
} else {
    console.log("Odd");
}
```

---

# 17. Exponentiation `**`

The `**` operator raises a number to a power.

```js
console.log(2 ** 3);
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

---

# 18. More Exponentiation Examples

```js
console.log(5 ** 2);
console.log(10 ** 2);
console.log(2 ** 10);
```

Output:

```text
25
100
1024
```

---

# 19. Square of a Number

```js
const number = 8;

const square = number ** 2;

console.log(square);
```

Output:

```text
64
```

---

# 20. Cube of a Number

```js
const number = 4;

const cube = number ** 3;

console.log(cube);
```

Output:

```text
64
```

---

# 21. Square Root

You can use the `Math.sqrt()` method.

```js
const number = 25;

const result = Math.sqrt(number);

console.log(result);
```

Output:

```text
5
```

This is technically part of the `Math` object rather than an arithmetic operator, but it is closely related to mathematical calculations.

---

# 22. Increment Operator `++`

The increment operator increases a value by `1`.

```js
let count = 0;

count++;

console.log(count);
```

Output:

```text
1
```

Equivalent to:

```js
count = count + 1;
```

---

# 23. Multiple Increments

```js
let count = 0;

count++;
count++;
count++;

console.log(count);
```

Output:

```text
3
```

---

# 24. Decrement Operator `--`

The decrement operator decreases a value by `1`.

```js
let count = 5;

count--;

console.log(count);
```

Output:

```text
4
```

Equivalent to:

```js
count = count - 1;
```

---

# 25. Multiple Decrements

```js
let count = 5;

count--;
count--;
count--;

console.log(count);
```

Output:

```text
2
```

---

# 26. Pre-Increment

Pre-increment means:

```js
++x
```

The variable is incremented first, and then the resulting value is used.

Example:

```js
let x = 5;

const result = ++x;

console.log(x);
console.log(result);
```

Output:

```text
6
6
```

Execution:

```text
x = 5
↓
++x
↓
x becomes 6
↓
result receives 6
```

---

# 27. Post-Increment

Post-increment means:

```js
x++
```

The current value is used first, then the variable is incremented.

Example:

```js
let x = 5;

const result = x++;

console.log(x);
console.log(result);
```

Output:

```text
6
5
```

Execution:

```text
x = 5
↓
result receives 5
↓
x becomes 6
```

---

# 28. Pre vs Post Increment

```js
let x = 5;

console.log(++x);
```

Output:

```text
6
```

Because the increment happens first.

---

```js
let y = 5;

console.log(y++);
```

Output:

```text
5
```

Then:

```js
console.log(y);
```

Output:

```text
6
```

---

# 29. Pre-Decrement

```js
let x = 5;

const result = --x;

console.log(x);
console.log(result);
```

Output:

```text
4
4
```

The decrement happens before the value is used.

---

# 30. Post-Decrement

```js
let x = 5;

const result = x--;

console.log(x);
console.log(result);
```

Output:

```text
4
5
```

The current value is used first.

---

# 31. Increment/Decrement Mental Model

```text
++x
│
├── Increase x
└── Use new value


x++
│
├── Use current value
└── Increase x
```

Similarly:

```text
--x
│
├── Decrease x
└── Use new value


x--
│
├── Use current value
└── Decrease x
```

---

# 32. Assignment Operators

Arithmetic operations are often combined with assignment.

Instead of:

```js
let score = 10;

score = score + 5;
```

You can write:

```js
let score = 10;

score += 5;
```

Both result in:

```text
15
```

---

# 33. Addition Assignment `+=`

```js
let number = 10;

number += 5;

console.log(number);
```

Output:

```text
15
```

Equivalent:

```js
number = number + 5;
```

---

# 34. Subtraction Assignment `-=`

```js
let number = 20;

number -= 5;

console.log(number);
```

Output:

```text
15
```

Equivalent:

```js
number = number - 5;
```

---

# 35. Multiplication Assignment `*=`

```js
let number = 10;

number *= 3;

console.log(number);
```

Output:

```text
30
```

Equivalent:

```js
number = number * 3;
```

---

# 36. Division Assignment `/=`

```js
let number = 100;

number /= 4;

console.log(number);
```

Output:

```text
25
```

Equivalent:

```js
number = number / 4;
```

---

# 37. Remainder Assignment `%=`

```js
let number = 10;

number %= 3;

console.log(number);
```

Output:

```text
1
```

Equivalent:

```js
number = number % 3;
```

---

# 38. Exponentiation Assignment `**=`

```js
let number = 2;

number **= 3;

console.log(number);
```

Output:

```text
8
```

Equivalent:

```js
number = number ** 3;
```

---

# 39. Complete Assignment Operator Table

| Operator | Meaning              | Example   |  Result |
| -------- | -------------------- | --------- | ------: |
| `=`      | Assign               | `x = 10`  |    `10` |
| `+=`     | Add and assign       | `x += 5`  | `x + 5` |
| `-=`     | Subtract and assign  | `x -= 5`  | `x - 5` |
| `*=`     | Multiply and assign  | `x *= 5`  | `x * 5` |
| `/=`     | Divide and assign    | `x /= 5`  | `x / 5` |
| `%=`     | Remainder and assign | `x %= 5`  | `x % 5` |
| `**=`    | Power and assign     | `x **= 2` |    `x²` |

---

# 40. Operator Precedence

When an expression contains multiple operators, JavaScript follows operator precedence rules.

Example:

```js
const result = 10 + 5 * 2;

console.log(result);
```

You might expect:

```text
30
```

But the result is:

```text
20
```

Why?

Multiplication happens before addition:

```text
10 + (5 * 2)
10 + 10
20
```

---

# 41. Basic Arithmetic Precedence

A simplified order is:

```text
1. Parentheses ()
2. Exponentiation **
3. Multiplication *
4. Division /
5. Remainder %
6. Addition +
7. Subtraction -
```

For many everyday expressions, remember:

```text
()
**
* / %
+ -
```

---

# 42. Parentheses Override Precedence

Example:

```js
const result = (10 + 5) * 2;

console.log(result);
```

Output:

```text
30
```

Without parentheses:

```js
const result = 10 + 5 * 2;
```

Output:

```text
20
```

---

# 43. Use Parentheses for Clarity

Even when you know precedence, parentheses can make your intention obvious.

Instead of:

```js
const total = price + tax * quantity;
```

If the intended logic is to calculate price plus tax for each item:

```js
const total = (price + tax) * quantity;
```

Good parentheses improve readability and prevent logic mistakes.

---

# 44. Left-to-Right Evaluation

Operators at the same precedence level are generally evaluated according to their associativity.

For example:

```js
const result = 20 / 5 * 2;
```

Division and multiplication have the same precedence.

So:

```text
20 / 5 * 2
↓
4 * 2
↓
8
```

Result:

```text
8
```

It is not:

```text
20 / (5 * 2)
```

which would be `2`.

---

# 45. Exponentiation Associativity

Exponentiation behaves differently.

```js
const result = 2 ** 3 ** 2;

console.log(result);
```

Exponentiation is right-associative, so it behaves like:

```js
2 ** (3 ** 2)
```

Then:

```text
3 ** 2 = 9
2 ** 9 = 512
```

Result:

```text
512
```

When in doubt, use parentheses.

---

# 46. Negative Numbers

JavaScript supports negative numbers.

```js
const temperature = -10;

console.log(temperature);
```

Arithmetic works normally:

```js
console.log(-10 + 5);
```

Output:

```text
-5
```

---

# 47. Decimal Numbers

JavaScript uses the `Number` type for ordinary numeric values.

```js
const price = 99.99;

console.log(price);
```

You can perform arithmetic:

```js
console.log(99.99 + 10.50);
```

However, floating-point precision has important edge cases.

---

# 48. Floating-Point Precision

Consider:

```js
console.log(0.1 + 0.2);
```

You might expect:

```text
0.3
```

But JavaScript gives:

```text
0.30000000000000004
```

Why?

JavaScript numbers are generally represented using IEEE 754 double-precision floating-point representation, and some decimal fractions cannot be represented exactly in binary.

---

# 49. Handling Decimal Results

For display purposes, you can use:

```js
const result = 0.1 + 0.2;

console.log(result.toFixed(2));
```

Output:

```text
0.30
```

Important:

`toFixed()` returns a **string**.

```js
const result = (0.1 + 0.2).toFixed(2);

console.log(typeof result);
```

Output:

```text
string
```

---

# 50. Money Calculations

Do not blindly rely on floating-point arithmetic for financial systems.

For simple learning examples:

```js
const price = 19.99;
const quantity = 3;

const total = price * quantity;

console.log(total);
```

For production financial applications, consider representing monetary values in the smallest unit, such as paise/cents:

```js
const priceInPaise = 1999;
const quantity = 3;

const totalInPaise = priceInPaise * quantity;

console.log(totalInPaise);
```

Then format the amount appropriately.

For more complex financial systems, use a suitable decimal/money library and server-side validation.

---

# 51. `NaN`

`NaN` means:

```text
Not-a-Number
```

Example:

```js
const result = "hello" * 5;

console.log(result);
```

Output:

```text
NaN
```

You can check it with:

```js
console.log(Number.isNaN(result));
```

Output:

```text
true
```

---

# 52. `Infinity`

Example:

```js
const result = 10 / 0;

console.log(result);
```

Output:

```text
Infinity
```

You can check:

```js
console.log(Number.isFinite(result));
```

Output:

```text
false
```

---

# 53. Negative Infinity

```js
console.log(-10 / 0);
```

Output:

```text
-Infinity
```

---

# 54. Arithmetic with `null`

JavaScript performs type conversion in some arithmetic expressions.

Example:

```js
console.log(10 + null);
```

Output:

```text
10
```

Because `null` is converted to `0` in numeric addition.

But:

```js
console.log("10" + null);
```

produces:

```text
10null
```

because `+` also performs string concatenation when a string is involved.

This is an important distinction.

---

# 55. Arithmetic with Booleans

In numeric arithmetic:

```js
true
```

can be converted to:

```text
1
```

and:

```js
false
```

to:

```text
0
```

Example:

```js
console.log(10 + true);
```

Output:

```text
11
```

And:

```js
console.log(10 + false);
```

Output:

```text
10
```

However, relying heavily on implicit coercion can make code harder to understand. Explicit conversion is often clearer.

---

# 56. Arithmetic with Strings

This is very important.

```js
console.log("10" + 5);
```

Output:

```text
105
```

Why?

Because `+` can perform string concatenation.

But:

```js
console.log("10" - 5);
```

Output:

```text
5
```

JavaScript converts `"10"` into a number for `-`.

Similarly:

```js
console.log("10" * 2);
```

Output:

```text
20
```

And:

```js
console.log("10" / 2);
```

Output:

```text
5
```

---

# 57. The Special Behavior of `+`

The `+` operator has two major jobs:

### Numeric addition

```js
10 + 5
```

Result:

```text
15
```

### String concatenation

```js
"Hello " + "World"
```

Result:

```text
Hello World
```

This is why type conversion matters.

---

# 58. Explicit Number Conversion

Instead of relying on implicit conversion:

```js
const input = "10";

const number = Number(input);

console.log(number + 5);
```

Output:

```text
15
```

This is much clearer.

---

# 59. Arithmetic with User Input

Suppose:

```js
const age = prompt("Enter your age:");
```

`prompt()` returns a string.

So:

```js
console.log(age + 1);
```

If the user enters:

```text
20
```

the result may be:

```text
201
```

because `"20" + 1` performs string concatenation.

Correct:

```js
const age = Number(prompt("Enter your age:"));

console.log(age + 1);
```

Output:

```text
21
```

---

# 60. Example — Simple Calculator

```js
const a = 20;
const b = 5;

console.log("Addition:", a + b);
console.log("Subtraction:", a - b);
console.log("Multiplication:", a * b);
console.log("Division:", a / b);
console.log("Remainder:", a % b);
console.log("Power:", a ** b);
```

Output:

```text
Addition: 25
Subtraction: 15
Multiplication: 100
Division: 4
Remainder: 0
Power: 3200000
```

---

# 61. Example — Student Marks

```js
const math = 85;
const science = 90;
const english = 80;

const total = math + science + english;

const average = total / 3;

console.log(`Total: ${total}`);
console.log(`Average: ${average}`);
```

Output:

```text
Total: 255
Average: 85
```

---

# 62. Example — Percentage

```js
const obtainedMarks = 450;
const totalMarks = 500;

const percentage = (obtainedMarks / totalMarks) * 100;

console.log(`Percentage: ${percentage}%`);
```

Output:

```text
Percentage: 90%
```

---

# 63. Example — Shopping Cart

```js
const laptopPrice = 70000;
const mousePrice = 1500;
const keyboardPrice = 2500;

const total =
  laptopPrice +
  mousePrice +
  keyboardPrice;

console.log(`Total: ₹${total}`);
```

Output:

```text
Total: ₹74000
```

---

# 64. Example — Quantity Calculation

```js
const productPrice = 500;
const quantity = 4;

const total = productPrice * quantity;

console.log(`Total: ₹${total}`);
```

Output:

```text
Total: ₹2000
```

---

# 65. Example — Discount

Suppose a product costs ₹1000 and has a 20% discount.

```js
const price = 1000;
const discountPercent = 20;

const discountAmount =
  price * (discountPercent / 100);

const finalPrice =
  price - discountAmount;

console.log(`Discount: ₹${discountAmount}`);
console.log(`Final Price: ₹${finalPrice}`);
```

Output:

```text
Discount: ₹200
Final Price: ₹800
```

---

# 66. Example — Tax Calculation

```js
const price = 1000;
const taxRate = 0.18;

const tax = price * taxRate;

const finalPrice = price + tax;

console.log(`Tax: ₹${tax}`);
console.log(`Final Price: ₹${finalPrice}`);
```

Output:

```text
Tax: ₹180
Final Price: ₹1180
```

---

# 67. Example — Rectangle Area

Formula:

```text
Area = length × width
```

JavaScript:

```js
const length = 20;
const width = 10;

const area = length * width;

console.log(`Area: ${area}`);
```

Output:

```text
Area: 200
```

---

# 68. Example — Rectangle Perimeter

Formula:

```text
Perimeter = 2 × (length + width)
```

JavaScript:

```js
const length = 20;
const width = 10;

const perimeter = 2 * (length + width);

console.log(`Perimeter: ${perimeter}`);
```

Output:

```text
Perimeter: 60
```

---

# 69. Example — Circle Area

Formula:

```text
Area = π × r²
```

JavaScript:

```js
const radius = 5;

const area = Math.PI * radius ** 2;

console.log(`Area: ${area}`);
```

---

# 70. Example — Average

```js
const a = 80;
const b = 90;
const c = 70;

const average = (a + b + c) / 3;

console.log(`Average: ${average}`);
```

Output:

```text
Average: 80
```

---

# 71. Example — Time Conversion

Convert minutes into hours and remaining minutes.

```js
const totalMinutes = 135;

const hours = Math.floor(totalMinutes / 60);

const minutes = totalMinutes % 60;

console.log(`${hours} hours ${minutes} minutes`);
```

Output:

```text
2 hours 15 minutes
```

Notice the use of `%`:

```js
totalMinutes % 60
```

It gives the remaining minutes.

---

# 72. Example — Even or Odd

```js
const number = 42;

if (number % 2 === 0) {
  console.log("Even");
} else {
  console.log("Odd");
}
```

Output:

```text
Even
```

---

# 73. Example — Last Digit

You can use `% 10` to get the last digit of a positive integer.

```js
const number = 12345;

const lastDigit = number % 10;

console.log(lastDigit);
```

Output:

```text
5
```

---

# 74. Example — Remove Last Digit

For a positive integer:

```js
const number = 12345;

const result = Math.floor(number / 10);

console.log(result);
```

Output:

```text
1234
```

---

# 75. Example — Convert Seconds

Convert:

```text
3675 seconds
```

into:

```text
1 hour 1 minute 15 seconds
```

Code:

```js
const totalSeconds = 3675;

const hours = Math.floor(totalSeconds / 3600);

const remainingSeconds = totalSeconds % 3600;

const minutes = Math.floor(remainingSeconds / 60);

const seconds = remainingSeconds % 60;

console.log(`${hours}h ${minutes}m ${seconds}s`);
```

Output:

```text
1h 1m 15s
```

This type of arithmetic is commonly used in timers and media applications.

---

# 76. Example — Distance Calculation

```js
const speed = 60;
const time = 2;

const distance = speed * time;

console.log(`Distance: ${distance} km`);
```

Formula:

```text
Distance = Speed × Time
```

---

# 77. Example — Simple Interest

Formula:

```text
SI = (P × R × T) / 100
```

JavaScript:

```js
const principal = 10000;
const rate = 5;
const time = 2;

const simpleInterest =
  (principal * rate * time) / 100;

console.log(`Simple Interest: ₹${simpleInterest}`);
```

Output:

```text
Simple Interest: ₹1000
```

---

# 78. Example — BMI

Formula:

```text
BMI = weight / height²
```

JavaScript:

```js
const weight = 70;
const height = 1.75;

const bmi = weight / height ** 2;

console.log(`BMI: ${bmi}`);
```

For display:

```js
console.log(`BMI: ${bmi.toFixed(2)}`);
```

---

# 79. Common Mistake — Forgetting Parentheses

Incorrect:

```js
const percentage = obtained / total * 100;
```

This can actually be mathematically equivalent because multiplication and division have the same precedence and evaluate left-to-right.

But when the formula becomes more complex, parentheses make the intended grouping much clearer.

Prefer:

```js
const percentage = (obtained / total) * 100;
```

---

# 80. Common Mistake — Using `^` for Power

A common beginner mistake is:

```js
const result = 2 ^ 3;
```

This is **not exponentiation** in JavaScript.

`^` is the bitwise XOR operator.

Use:

```js
const result = 2 ** 3;
```

Output:

```text
8
```

---

# 81. Common Mistake — Using `/` for Remainder

Incorrect:

```js
10 / 3
```

This gives:

```text
3.3333333333333335
```

If you want the remainder:

```js
10 % 3
```

Result:

```text
1
```

---

# 82. Common Mistake — Incrementing `const`

This is invalid:

```js
const count = 0;

count++;
```

Because `++` reassigns the variable.

Use:

```js
let count = 0;

count++;
```

---

# 83. Common Mistake — String + Number

```js
const age = "20";

console.log(age + 1);
```

Result:

```text
201
```

Because the string causes concatenation.

Correct:

```js
const age = Number("20");

console.log(age + 1);
```

Result:

```text
21
```

---

# 84. Common Mistake — Floating-Point Equality

Avoid assuming:

```js
0.1 + 0.2 === 0.3
```

will be true.

```js
console.log(0.1 + 0.2 === 0.3);
```

Output:

```text
false
```

For many numeric comparisons, use an appropriate tolerance or representation depending on the application.

Example:

```js
const result = 0.1 + 0.2;

const isClose =
  Math.abs(result - 0.3) < Number.EPSILON;

console.log(isClose);
```

---

# 85. Arithmetic Operator Cheat Sheet

```text
+     Addition
-     Subtraction
*     Multiplication
/     Division
%     Remainder
**    Exponentiation
++    Increment
--    Decrement

+=    Add and assign
-=    Subtract and assign
*=    Multiply and assign
/=    Divide and assign
%=    Remainder and assign
**=   Power and assign
```

---

# 86. Quick Examples

```js
10 + 5
// 15

10 - 5
// 5

10 * 5
// 50

10 / 5
// 2

10 % 3
// 1

2 ** 3
// 8
```

---

# 87. Operator Precedence Cheat Sheet

Remember:

```text
()
↓
**
↓
* / %
↓
+ -
```

Example:

```js
const result = 10 + 2 * 3;
```

First:

```text
2 * 3 = 6
```

Then:

```text
10 + 6 = 16
```

Result:

```text
16
```

With parentheses:

```js
const result = (10 + 2) * 3;
```

Result:

```text
36
```

---

# 88. Mini Project — Bill Calculator

```js
const product1 = 500;
const product2 = 1000;
const product3 = 250;

const subtotal =
  product1 +
  product2 +
  product3;

const taxRate = 0.18;

const tax = subtotal * taxRate;

const total = subtotal + tax;

console.log(`Subtotal: ₹${subtotal}`);
console.log(`Tax: ₹${tax}`);
console.log(`Total: ₹${total}`);
```

---

# 89. Mini Project — Student Result Calculator

```js
const math = 85;
const physics = 90;
const chemistry = 80;
const english = 88;
const computer = 95;

const total =
  math +
  physics +
  chemistry +
  english +
  computer;

const percentage = (total / 500) * 100;

console.log(`Total Marks: ${total}`);
console.log(`Percentage: ${percentage}%`);
```

Output:

```text
Total Marks: 438
Percentage: 87.6%
```

---

# 90. Mini Project — Counter

```js
let count = 0;

count++;
count++;
count++;
count--;

console.log(`Count: ${count}`);
```

Output:

```text
Count: 2
```

---

# 91. Mini Project — Number Breakdown

```js
const number = 12345;

const lastDigit = number % 10;

const remainingNumber = Math.floor(number / 10);

console.log(`Last digit: ${lastDigit}`);
console.log(`Remaining: ${remainingNumber}`);
```

Output:

```text
Last digit: 5
Remaining: 1234
```

---

# 92. Practice Questions

## Question 1

Calculate:

```text
25 + 15
```

Expected:

```text
40
```

---

## Question 2

Calculate:

```text
100 - 45
```

Expected:

```text
55
```

---

## Question 3

Calculate:

```text
12 × 8
```

Expected:

```text
96
```

---

## Question 4

Calculate:

```text
100 / 4
```

Expected:

```text
25
```

---

## Question 5

Find the remainder:

```text
17 % 5
```

Expected:

```text
2
```

---

## Question 6

Calculate:

```text
3 ** 4
```

Expected:

```text
81
```

---

## Question 7

What is the output?

```js
let x = 10;

x += 5;

console.log(x);
```

---

## Question 8

What is the output?

```js
let x = 10;

console.log(x++);

console.log(x);
```

---

## Question 9

What is the output?

```js
let x = 10;

console.log(++x);
```

---

## Question 10

What is the output?

```js
console.log(10 + 5 * 2);
```

---

# 93. Challenge

Create a program that receives:

```text
Price
Quantity
Discount percentage
Tax percentage
```

and calculates:

```text
Subtotal
Discount amount
Price after discount
Tax amount
Final price
```

Example:

```text
Price: ₹1000
Quantity: 3
Discount: 10%
Tax: 18%
```

Expected logic:

```text
Subtotal
= 1000 × 3
= 3000

Discount
= 3000 × 10%
= 300

After discount
= 3000 - 300
= 2700

Tax
= 2700 × 18%
= 486

Final price
= 2700 + 486
= 3186
```

Try writing the JavaScript yourself before looking for a solution.

---

# 94. What You Should Understand Before Moving On

You should be comfortable with:

* [ ] Addition `+`
* [ ] Subtraction `-`
* [ ] Multiplication `*`
* [ ] Division `/`
* [ ] Remainder `%`
* [ ] Exponentiation `**`
* [ ] Increment `++`
* [ ] Decrement `--`
* [ ] Pre-increment
* [ ] Post-increment
* [ ] Pre-decrement
* [ ] Post-decrement
* [ ] Assignment `=`
* [ ] `+=`
* [ ] `-=`
* [ ] `*=`
* [ ] `/=`
* [ ] `%=`
* [ ] `**=`
* [ ] Operator precedence
* [ ] Parentheses
* [ ] `NaN`
* [ ] `Infinity`
* [ ] Negative numbers
* [ ] Decimal numbers
* [ ] Floating-point precision
* [ ] Arithmetic with strings
* [ ] Explicit number conversion
* [ ] Even/odd checking with `%`
* [ ] Real-world calculations
* [ ] Difference between `x++` and `++x`

---

# 95. Final Mental Model

```text
                 ARITHMETIC OPERATORS
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     BASIC             POWER          UPDATE
        │                │                │
   +  -  *  /  %         **           ++  --
        │
        └──────────────┐
                       │
                ASSIGNMENT
                       │
        ┌──────────────┼──────────────┐
        │              │              │
       +=             -=             *=
        │
        ├──────────────┐
        │              │
       /=             %=
                       │
                      **=
```

The most important rule:

```text
Arithmetic
   ↓
Understand the operator
   ↓
Understand precedence
   ↓
Use parentheses when needed
   ↓
Watch for type conversion
   ↓
Watch for floating-point precision
```

Once these concepts become comfortable, you'll be able to build calculations into almost every JavaScript program.
