# 05 — JavaScript Type Conversion

> Type conversion is the process of changing a value from one data type into another.

For example:

```js
const age = "20";
```

Here `age` is a **string**.

We can convert it into a number:

```js
const age = Number("20");
```

Now `age` is a **number**.

---

# 1. What is Type Conversion?

JavaScript works with different data types:

```text
String
Number
Boolean
BigInt
Symbol
Object
Undefined
Null
```

Sometimes we need to convert one type into another.

Example:

```js
const value = "100";

const number = Number(value);

console.log(number);
```

Output:

```text
100
```

Before conversion:

```text
"100" → String
```

After conversion:

```text
100 → Number
```

---

# 2. Why Do We Need Type Conversion?

Consider user input:

```js
const age = prompt("Enter your age:");

console.log(age);
```

If the user enters:

```text
20
```

It may look like a number, but `prompt()` returns a **string**.

So:

```js
typeof age
```

returns:

```text
string
```

To perform numerical calculations:

```js
const age = Number(prompt("Enter your age:"));

console.log(age + 1);
```

If the user enters `20`:

```text
21
```

Without conversion:

```js
const age = prompt("Enter your age:");

console.log(age + 1);
```

Output:

```text
201
```

Why?

Because:

```text
"20" + 1
```

becomes:

```text
"201"
```

---

# 3. Two Types of Conversion

JavaScript supports:

```text
Explicit Type Conversion
Implicit Type Conversion
```

---

# 4. Explicit Type Conversion

Explicit conversion happens when **you intentionally convert** a value.

Example:

```js
const value = "100";

const number = Number(value);
```

You explicitly told JavaScript:

> Convert this string into a number.

Common conversion functions:

```js
Number()
String()
Boolean()
BigInt()
```

There are also parsing functions:

```js
parseInt()
parseFloat()
```

---

# 5. Implicit Type Conversion

Implicit conversion happens when **JavaScript automatically converts a value** during an operation.

Example:

```js
const result = "10" + 5;

console.log(result);
```

Output:

```text
105
```

JavaScript converted:

```text
5 → "5"
```

Then:

```text
"10" + "5"
```

became:

```text
"105"
```

This automatic behavior is called **type coercion**.

---

# 6. Explicit vs Implicit

Explicit:

```js
const result = Number("10") + 5;
```

Result:

```text
15
```

Implicit:

```js
const result = "10" + 5;
```

Result:

```text
"105"
```

Best practice:

> Use explicit conversion when you want your code to clearly communicate the intended type.

---

# 7. `typeof`

Before learning conversion, you should understand `typeof`.

`typeof` tells you the type of a value.

Example:

```js
const name = "Alex";
const age = 20;
const isStudent = true;

console.log(typeof name);
console.log(typeof age);
console.log(typeof isStudent);
```

Output:

```text
string
number
boolean
```

---

# 8. String to Number

The most common conversion is:

```js
Number()
```

Example:

```js
const value = "100";

const result = Number(value);

console.log(result);
console.log(typeof result);
```

Output:

```text
100
number
```

---

# 9. Number to String

Use:

```js
String()
```

Example:

```js
const age = 20;

const result = String(age);

console.log(result);
console.log(typeof result);
```

Output:

```text
20
string
```

You can also use:

```js
age.toString();
```

Example:

```js
const age = 20;

const result = age.toString();

console.log(result);
```

---

# 10. Boolean Conversion

Use:

```js
Boolean()
```

Example:

```js
const value = 1;

console.log(Boolean(value));
```

Output:

```text
true
```

Another example:

```js
console.log(Boolean(0));
```

Output:

```text
false
```

---

# 11. Number Conversion

```js
Number("10");
```

Result:

```text
10
```

```js
Number("10.5");
```

Result:

```text
10.5
```

```js
Number("-25");
```

Result:

```text
-25
```

---

# 12. Empty String to Number

An empty string:

```js
Number("");
```

produces:

```text
0
```

Example:

```js
console.log(Number(""));
```

Output:

```text
0
```

This can sometimes be surprising.

---

# 13. Whitespace String to Number

Whitespace is ignored around numeric text.

```js
console.log(Number("   100   "));
```

Output:

```text
100
```

Also:

```js
console.log(Number("\n100\t"));
```

Output:

```text
100
```

---

# 14. Invalid String to Number

Consider:

```js
const result = Number("Hello");

console.log(result);
```

Output:

```text
NaN
```

`NaN` means:

> Not a Number

More accurately, `NaN` is a special numeric value representing an invalid numerical result.

---

# 15. `NaN`

Example:

```js
const result = Number("Apple");

console.log(result);
```

Output:

```text
NaN
```

Check it:

```js
console.log(Number.isNaN(result));
```

Output:

```text
true
```

---

# 16. `NaN` is Still a Number Type

This can be confusing:

```js
const value = Number("Hello");

console.log(typeof value);
```

Output:

```text
number
```

So:

```text
NaN
```

has:

```text
typeof NaN → "number"
```

---

# 17. How to Safely Check for `NaN`

Prefer:

```js
Number.isNaN(value)
```

Example:

```js
const value = Number("Hello");

if (Number.isNaN(value)) {
  console.log("Invalid number");
}
```

Output:

```text
Invalid number
```

---

# 18. `parseInt()`

`parseInt()` converts a string into an integer.

Example:

```js
const value = parseInt("100");

console.log(value);
```

Output:

```text
100
```

Decimal portion is removed:

```js
console.log(parseInt("10.99"));
```

Output:

```text
10
```

---

# 19. `parseFloat()`

`parseFloat()` is used when you want a decimal number.

```js
const value = parseFloat("10.99");

console.log(value);
```

Output:

```text
10.99
```

Compare:

```js
console.log(parseInt("10.99"));
console.log(parseFloat("10.99"));
```

Output:

```text
10
10.99
```

---

# 20. `Number()` vs `parseInt()`

This is important.

```js
Number("123abc");
```

Result:

```text
NaN
```

But:

```js
parseInt("123abc");
```

Result:

```text
123
```

Why?

`Number()` expects the entire string to represent a valid number.

`parseInt()` reads an integer from the beginning and stops when it encounters a character that doesn't fit.

---

# 21. `Number()` vs `parseFloat()`

```js
Number("10.50");
```

Result:

```text
10.5
```

```js
parseFloat("10.50");
```

Result:

```text
10.5
```

But:

```js
Number("10.50px");
```

Result:

```text
NaN
```

while:

```js
parseFloat("10.50px");
```

Result:

```text
10.5
```

---

# 22. Parsing with Units

Suppose:

```js
const width = "250px";
```

This is not a pure number.

```js
Number(width);
```

Result:

```text
NaN
```

But:

```js
parseInt(width);
```

Result:

```text
250
```

Similarly:

```js
parseFloat("12.5rem");
```

returns:

```text
12.5
```

This is useful when processing some CSS-like values.

---

# 23. Radix with `parseInt()`

`parseInt()` can accept a second argument called the **radix**.

Example:

```js
const value = parseInt("1010", 2);

console.log(value);
```

Output:

```text
10
```

Because:

```text
1010₂ = 10₁₀
```

Common radices:

```text
2  → Binary
8  → Octal
10 → Decimal
16 → Hexadecimal
```

Best practice:

```js
parseInt("100", 10);
```

when you intend decimal parsing.

---

# 24. String Conversion

Use:

```js
String()
```

Example:

```js
const number = 100;

const text = String(number);

console.log(text);
console.log(typeof text);
```

Output:

```text
100
string
```

---

# 25. `.toString()`

Numbers can also be converted using:

```js
.toString()
```

Example:

```js
const number = 100;

const text = number.toString();

console.log(text);
```

Output:

```text
100
```

Check:

```js
console.log(typeof text);
```

Output:

```text
string
```

---

# 26. Boolean Conversion

Use:

```js
Boolean(value)
```

Example:

```js
console.log(Boolean(1));
```

Output:

```text
true
```

```js
console.log(Boolean(0));
```

Output:

```text
false
```

---

# 27. Truthy and Falsy Values

JavaScript values can behave as either:

```text
Truthy
Falsy
```

when converted to a boolean.

The main falsy values are:

```text
false
0
-0
0n
""
null
undefined
NaN
```

Almost everything else is truthy.

---

# 28. Falsy Values

### `false`

```js
Boolean(false);
```

Result:

```text
false
```

### `0`

```js
Boolean(0);
```

Result:

```text
false
```

### Empty string

```js
Boolean("");
```

Result:

```text
false
```

### `null`

```js
Boolean(null);
```

Result:

```text
false
```

### `undefined`

```js
Boolean(undefined);
```

Result:

```text
false
```

### `NaN`

```js
Boolean(NaN);
```

Result:

```text
false
```

---

# 29. Truthy Values

Examples:

```js
Boolean("Hello");
```

```text
true
```

```js
Boolean("0");
```

```text
true
```

```js
Boolean([]);
```

```text
true
```

```js
Boolean({});
```

```text
true
```

```js
Boolean(-1);
```

```text
true
```

---

# 30. Empty String vs `"0"`

This is a common interview question.

```js
Boolean("");
```

Result:

```text
false
```

But:

```js
Boolean("0");
```

Result:

```text
true
```

Why?

Because `"0"` is a **non-empty string**.

---

# 31. Empty Array is Truthy

This surprises many beginners:

```js
console.log(Boolean([]));
```

Output:

```text
true
```

Even though the array contains no elements.

Similarly:

```js
console.log(Boolean({}));
```

Output:

```text
true
```

Objects and arrays are truthy.

---

# 32. Implicit Conversion with `+`

The `+` operator is special because it can perform either:

```text
Addition
```

or:

```text
String concatenation
```

Example:

```js
console.log(10 + 20);
```

Output:

```text
30
```

But:

```js
console.log("10" + 20);
```

Output:

```text
1020
```

---

# 33. String Wins with `+`

Example:

```js
console.log("5" + 5);
```

Output:

```text
55
```

Another:

```js
console.log(5 + "5");
```

Output:

```text
55
```

JavaScript converts the number to a string.

---

# 34. Other Arithmetic Operators

Operators such as:

```text
-
*
/
%
**
```

usually convert numeric strings to numbers when appropriate.

Example:

```js
console.log("10" - 5);
```

Output:

```text
5
```

```js
console.log("10" * 2);
```

Output:

```text
20
```

```js
console.log("20" / 4);
```

Output:

```text
5
```

---

# 35. `+` vs `-`

Compare:

```js
console.log("10" + 5);
```

Output:

```text
105
```

But:

```js
console.log("10" - 5);
```

Output:

```text
5
```

Remember:

```text
+ → can concatenate strings
- → numeric operation
```

---

# 36. Boolean to Number

JavaScript converts booleans numerically like this:

```text
true  → 1
false → 0
```

Example:

```js
console.log(Number(true));
```

Output:

```text
1
```

```js
console.log(Number(false));
```

Output:

```text
0
```

---

# 37. Number to Boolean

```js
Boolean(1);
```

Result:

```text
true
```

```js
Boolean(0);
```

Result:

```text
false
```

---

# 38. String to Boolean

```js
Boolean("true");
```

Result:

```text
true
```

But:

```js
Boolean("false");
```

also returns:

```text
true
```

Why?

Because `"false"` is still a non-empty string.

This is a very common beginner mistake.

---

# 39. Empty String to Boolean

```js
Boolean("");
```

Result:

```text
false
```

But:

```js
Boolean(" ");
```

Result:

```text
true
```

A space is still a character, so the string is not empty.

---

# 40. `null` Conversion

To number:

```js
console.log(Number(null));
```

Output:

```text
0
```

To string:

```js
console.log(String(null));
```

Output:

```text
"null"
```

To boolean:

```js
console.log(Boolean(null));
```

Output:

```text
false
```

---

# 41. `undefined` Conversion

To number:

```js
console.log(Number(undefined));
```

Output:

```text
NaN
```

To string:

```js
console.log(String(undefined));
```

Output:

```text
"undefined"
```

To boolean:

```js
console.log(Boolean(undefined));
```

Output:

```text
false
```

---

# 42. Conversion Table

| Value       | Number | String              | Boolean |
| ----------- | -----: | ------------------- | ------- |
| `"10"`      |   `10` | `"10"`              | `true`  |
| `""`        |    `0` | `""`                | `false` |
| `"hello"`   |  `NaN` | `"hello"`           | `true`  |
| `true`      |    `1` | `"true"`            | `true`  |
| `false`     |    `0` | `"false"`           | `false` |
| `null`      |    `0` | `"null"`            | `false` |
| `undefined` |  `NaN` | `"undefined"`       | `false` |
| `0`         |    `0` | `"0"`               | `false` |
| `1`         |    `1` | `"1"`               | `true`  |
| `[]`        |    `0` | `""`                | `true`  |
| `[10]`      |   `10` | `"10"`              | `true`  |
| `{}`        |  `NaN` | `"[object Object]"` | `true`  |

---

# 43. Object to String

Example:

```js
const user = {
  name: "Alex"
};

console.log(String(user));
```

Typical output:

```text
[object Object]
```

Objects can define custom conversion behavior using mechanisms such as `toString()` and `Symbol.toPrimitive`, but the default object-to-string conversion often produces this result.

---

# 44. Array to String

```js
const fruits = ["Apple", "Banana", "Mango"];

console.log(String(fruits));
```

Output:

```text
Apple,Banana,Mango
```

This happens because arrays have a string conversion behavior based on their elements.

---

# 45. `Number([])`

This is a strange-looking example:

```js
console.log(Number([]));
```

Output:

```text
0
```

An empty array converts to an empty string first in this conversion path, and:

```text
Number("")
```

is:

```text
0
```

---

# 46. `Number([10])`

```js
console.log(Number([10]));
```

Output:

```text
10
```

But:

```js
console.log(Number([10, 20]));
```

Output:

```text
NaN
```

because the array's string representation is:

```text
"10,20"
```

which is not a valid numeric string.

---

# 47. Unary Plus Operator

A quick way to convert a value to a number is:

```js
+
```

Example:

```js
const value = "100";

const number = +value;

console.log(number);
```

Output:

```text
100
```

This:

```js
+"100"
```

is roughly equivalent to:

```js
Number("100")
```

---

# 48. Unary Plus with User Input

```js
const age = +prompt("Enter your age:");

console.log(age);
```

This works, but beginners may find:

```js
Number(prompt("Enter your age:"))
```

clearer.

For readable production code, explicit conversion is often preferable.

---

# 49. Unary Minus

Unary minus converts a value to a number and negates it.

```js
console.log(-"10");
```

Output:

```text
-10
```

Example:

```js
const value = "50";

console.log(-value);
```

Output:

```text
-50
```

---

# 50. Double NOT `!!`

You may see:

```js
!!value
```

used to convert a value to boolean.

Example:

```js
const value = "Hello";

console.log(!!value);
```

Output:

```text
true
```

Conceptually:

```text
!value
```

converts to boolean and negates it.

Then:

```text
!!value
```

negates again.

So:

```js
!!"Hello"
```

becomes:

```text
true
```

However:

```js
Boolean("Hello")
```

is usually clearer for beginners.

---

# 51. `String()` vs `.toString()`

Consider:

```js
const value = null;
```

This works:

```js
String(value);
```

Result:

```text
"null"
```

But:

```js
value.toString();
```

throws an error because `null` has no method to call.

Similarly:

```js
String(undefined);
```

works.

Therefore:

```js
String(value)
```

is often safer when the value may be `null` or `undefined`.

---

# 52. `parseInt()` and Invalid Input

```js
console.log(parseInt("hello"));
```

Output:

```text
NaN
```

But:

```js
console.log(parseInt("100hello"));
```

Output:

```text
100
```

And:

```js
console.log(parseInt("hello100"));
```

Output:

```text
NaN
```

Parsing begins from the start of the string.

---

# 53. `parseFloat()` and Invalid Input

```js
console.log(parseFloat("12.5px"));
```

Output:

```text
12.5
```

But:

```js
console.log(parseFloat("px12.5"));
```

Output:

```text
NaN
```

---

# 54. `Number.isInteger()`

After conversion, you can check whether a number is an integer.

```js
const value = Number("100");

console.log(Number.isInteger(value));
```

Output:

```text
true
```

Example:

```js
console.log(Number.isInteger(10.5));
```

Output:

```text
false
```

---

# 55. `Number.isFinite()`

Check whether a value is a finite number.

```js
console.log(Number.isFinite(100));
```

Output:

```text
true
```

```js
console.log(Number.isFinite(Infinity));
```

Output:

```text
false
```

Important:

```js
Number.isFinite("100")
```

returns:

```text
false
```

because `"100"` is a string.

It does not perform implicit conversion.

---

# 56. `isNaN()` vs `Number.isNaN()`

This is an important difference.

Global:

```js
isNaN("hello");
```

returns:

```text
true
```

Global `isNaN()` performs coercion before testing.

But:

```js
Number.isNaN("hello");
```

returns:

```text
false
```

because `"hello"` itself is not the numeric value `NaN`; it is a string.

Prefer:

```js
Number.isNaN()
```

when you specifically want to test for the actual `NaN` value.

---

# 57. User Input Example

Suppose:

```js
const age = prompt("Enter your age:");
```

The input is a string.

Convert it:

```js
const age = Number(prompt("Enter your age:"));
```

Then:

```js
console.log(typeof age);
```

Output:

```text
number
```

---

# 58. User Input Validation

Don't blindly assume conversion succeeded.

```js
const input = prompt("Enter your age:");
const age = Number(input);

if (Number.isNaN(age)) {
  console.log("Please enter a valid number.");
} else {
  console.log(`Your age is ${age}`);
}
```

---

# 59. Calculator Example

```js
const first = Number(prompt("Enter first number:"));
const second = Number(prompt("Enter second number:"));

const sum = first + second;

console.log(`Sum: ${sum}`);
```

Without conversion:

```js
const first = prompt("Enter first number:");
const second = prompt("Enter second number:");

console.log(first + second);
```

Entering:

```text
10
20
```

would produce:

```text
1020
```

With conversion:

```text
30
```

---

# 60. Temperature Example

```js
const celsius = Number(prompt("Enter temperature in Celsius:"));

const fahrenheit = (celsius * 9) / 5 + 32;

console.log(`${fahrenheit}°F`);
```

---

# 61. Age Example

```js
const birthYear = Number(prompt("Enter your birth year:"));

const currentYear = new Date().getFullYear();

const age = currentYear - birthYear;

console.log(`You are approximately ${age} years old.`);
```

For real applications, age calculations should account for the exact birth date rather than only the year.

---

# 62. Shopping Cart Example

```js
const price = Number(prompt("Enter product price:"));
const quantity = Number(prompt("Enter quantity:"));

const total = price * quantity;

console.log(`Total: ₹${total}`);
```

---

# 63. Percentage Example

```js
const marks = Number(prompt("Enter marks:"));
const totalMarks = Number(prompt("Enter total marks:"));

const percentage = (marks / totalMarks) * 100;

console.log(`Percentage: ${percentage}%`);
```

---

# 64. String Concatenation Problem

Bad:

```js
const age = prompt("Enter age:");

console.log("You are " + age + 1);
```

Input:

```text
20
```

Output:

```text
You are 201
```

Correct:

```js
const age = Number(prompt("Enter age:"));

console.log("You are " + (age + 1));
```

Output:

```text
You are 21
```

---

# 65. Template Literals

Template literals make output easier to read.

```js
const age = Number(prompt("Enter age:"));

console.log(`Next year you will be ${age + 1}`);
```

This is cleaner than:

```js
console.log("Next year you will be " + (age + 1));
```

---

# 66. Important Conversion Rules

Remember:

```text
Number("100") → 100
Number("10.5") → 10.5
Number("") → 0
Number("hello") → NaN

String(100) → "100"
String(true) → "true"
String(null) → "null"

Boolean(1) → true
Boolean(0) → false
Boolean("hello") → true
Boolean("") → false
Boolean([]) → true
Boolean({}) → true
```

---

# 67. Common Beginner Mistakes

## Mistake 1 — Assuming `prompt()` returns a number

```js
const age = prompt("Age:");
```

`age` is a string.

Correct:

```js
const age = Number(prompt("Age:"));
```

---

## Mistake 2 — Thinking `"false"` is false

```js
Boolean("false");
```

Result:

```text
true
```

Because it is a non-empty string.

---

## Mistake 3 — Using `parseInt()` for validation

```js
parseInt("100abc");
```

returns:

```text
100
```

If the entire input must be a valid number, `Number()` plus validation is often more appropriate.

---

## Mistake 4 — Ignoring `NaN`

```js
const value = Number("hello");

console.log(value + 10);
```

Result:

```text
NaN
```

Validate input when necessary.

---

# 68. Best Practices

### 1. Prefer explicit conversion

Instead of relying on:

```js
"10" - 5
```

prefer:

```js
Number("10") - 5
```

This communicates your intention.

---

### 2. Validate external input

Data from:

* Users
* APIs
* Forms
* URLs
* Local storage
* Files

may not have the type you expect.

Convert and validate it.

---

### 3. Use `Number()` when the entire value should be numeric

Example:

```js
const price = Number(input);
```

---

### 4. Use `parseInt()` when parsing an integer prefix

Example:

```js
const pixels = parseInt("250px", 10);
```

---

### 5. Use `parseFloat()` when parsing a decimal prefix

Example:

```js
const width = parseFloat("12.5rem");
```

---

### 6. Prefer `Number.isNaN()`

Use:

```js
Number.isNaN(value)
```

for a precise `NaN` check.

---

### 7. Prefer `Boolean()` when teaching or communicating intent

Instead of:

```js
!!value
```

you can write:

```js
Boolean(value)
```

when readability matters.

---

# 69. Type Coercion Examples

Study these carefully.

```js
console.log("5" + 2);
```

Output:

```text
52
```

---

```js
console.log("5" - 2);
```

Output:

```text
3
```

---

```js
console.log("5" * 2);
```

Output:

```text
10
```

---

```js
console.log("5" / 2);
```

Output:

```text
2.5
```

---

```js
console.log("5" == 5);
```

Output:

```text
true
```

Loose equality performs coercion.

---

```js
console.log("5" === 5);
```

Output:

```text
false
```

Strict equality does not perform that type coercion.

---

# 70. Why `===` Is Usually Preferred

Loose equality:

```js
"10" == 10
```

returns:

```text
true
```

Strict equality:

```js
"10" === 10
```

returns:

```text
false
```

Because:

```text
"10" → String
10   → Number
```

They are different types.

In modern JavaScript, prefer:

```js
===
```

and:

```js
!==
```

unless you intentionally need loose equality behavior.

---

# 71. Conversion with `null`

Study these:

```js
console.log(null + 1);
```

Output:

```text
1
```

Because `null` becomes `0` in numeric conversion.

But:

```js
console.log(null + "1");
```

Output:

```text
null1
```

because string concatenation occurs.

These coercion rules are one reason explicit conversion is often easier to reason about.

---

# 72. Conversion with `undefined`

```js
console.log(undefined + 1);
```

Output:

```text
NaN
```

Because:

```text
Number(undefined) → NaN
```

---

# 73. `null` vs `undefined`

For number conversion:

```text
null      → 0
undefined → NaN
```

For boolean conversion:

```text
null      → false
undefined → false
```

For string conversion:

```text
null      → "null"
undefined → "undefined"
```

---

# 74. Conversion with Arrays

```js
console.log(String([]));
```

Output:

```text
""
```

```js
console.log(String([1, 2, 3]));
```

Output:

```text
"1,2,3"
```

And:

```js
console.log(Number([]));
```

Output:

```text
0
```

These are valid JavaScript behaviors but are generally not something you should rely on for application logic unless you understand the conversion intentionally.

---

# 75. Conversion with Objects

```js
const user = {};

console.log(Boolean(user));
```

Output:

```text
true
```

Even an empty object is truthy.

```js
console.log(String(user));
```

Typical output:

```text
[object Object]
```

But:

```js
console.log(Number(user));
```

usually produces:

```text
NaN
```

---

# 76. Practical Example — Login Form

```js
const username = prompt("Enter username:");
const password = prompt("Enter password:");

const hasUsername = Boolean(username);
const hasPassword = Boolean(password);

if (hasUsername && hasPassword) {
  console.log("Login information provided.");
} else {
  console.log("Please fill in all fields.");
}
```

Remember that this only checks whether input was provided; it is not actual authentication.

---

# 77. Practical Example — Product Price

```js
const input = prompt("Enter product price:");

const price = Number(input);

if (Number.isNaN(price)) {
  console.log("Invalid price.");
} else {
  console.log(`Product price: ₹${price}`);
}
```

---

# 78. Practical Example — Age Validation

```js
const input = prompt("Enter your age:");

const age = Number(input);

if (Number.isNaN(age)) {
  console.log("Please enter a valid number.");
} else if (age < 0) {
  console.log("Age cannot be negative.");
} else {
  console.log(`Your age is ${age}.`);
}
```

---

# 79. Practical Example — Marks Calculator

```js
const math = Number(prompt("Math marks:"));
const science = Number(prompt("Science marks:"));
const english = Number(prompt("English marks:"));

const total = math + science + english;
const percentage = total / 3;

console.log(`Total: ${total}`);
console.log(`Average: ${percentage}`);
```

---

# 80. Mini Project — Simple Calculator

```js
const first = Number(prompt("Enter first number:"));
const operator = prompt("Enter operator (+, -, *, /):");
const second = Number(prompt("Enter second number:"));

let result;

if (operator === "+") {
  result = first + second;
} else if (operator === "-") {
  result = first - second;
} else if (operator === "*") {
  result = first * second;
} else if (operator === "/") {
  result = first / second;
} else {
  console.log("Invalid operator.");
}

if (result !== undefined) {
  console.log(`Result: ${result}`);
}
```

This combines:

```text
Variables
Type conversion
Strings
Numbers
Operators
Conditions
Strict equality
```

---

# 81. Mini Project — Bill Calculator

```js
const price = Number(prompt("Enter item price:"));
const quantity = Number(prompt("Enter quantity:"));
const taxRate = Number(prompt("Enter tax percentage:"));

const subtotal = price * quantity;
const tax = subtotal * (taxRate / 100);
const total = subtotal + tax;

console.log(`Subtotal: ₹${subtotal}`);
console.log(`Tax: ₹${tax}`);
console.log(`Total: ₹${total}`);
```

---

# 82. Mini Project — BMI Calculator

```js
const weight = Number(prompt("Enter weight in kg:"));
const height = Number(prompt("Enter height in meters:"));

const bmi = weight / (height * height);

console.log(`BMI: ${bmi.toFixed(2)}`);
```

Here:

```js
Number()
```

converts the user input.

---

# 83. Practice Questions

## Question 1

What is the output?

```js
console.log(Number("50"));
```

Answer:

```text
50
```

---

## Question 2

What is the output?

```js
console.log(Number("hello"));
```

Answer:

```text
NaN
```

---

## Question 3

What is the output?

```js
console.log(Boolean(0));
```

Answer:

```text
false
```

---

## Question 4

What is the output?

```js
console.log(Boolean("0"));
```

Answer:

```text
true
```

---

## Question 5

What is the output?

```js
console.log("10" + 5);
```

Answer:

```text
105
```

---

## Question 6

What is the output?

```js
console.log("10" - 5);
```

Answer:

```text
5
```

---

## Question 7

What is the output?

```js
console.log(Number(""));
```

Answer:

```text
0
```

---

## Question 8

What is the output?

```js
console.log(Number(null));
```

Answer:

```text
0
```

---

## Question 9

What is the output?

```js
console.log(Number(undefined));
```

Answer:

```text
NaN
```

---

## Question 10

What is the output?

```js
console.log(typeof NaN);
```

Answer:

```text
number
```

---

# 84. Practice Challenge

Create a program that asks the user for:

```text
Name
Age
Height
Weight
```

Convert the numerical values properly.

Then display:

```text
Name: ...
Age: ...
Height: ...
Weight: ...
```

---

# 85. Practice Challenge — Shopping

Ask the user for:

```text
Product price
Quantity
Discount percentage
```

Convert all numerical inputs.

Calculate:

```text
Subtotal
Discount
Final price
```

---

# 86. Practice Challenge — Student Marks

Ask for:

```text
Math
Physics
Chemistry
English
Computer Science
```

Convert all values to numbers.

Calculate:

```text
Total
Average
Percentage
```

---

# 87. Practice Challenge — Currency

Ask the user:

```text
Amount in INR
Exchange rate
```

Convert both to numbers.

Calculate the converted amount.

Example:

```js
const inr = Number(prompt("Enter INR:"));
const rate = Number(prompt("Enter exchange rate:"));

const converted = inr * rate;

console.log(`Converted amount: ${converted}`);
```

---

# 88. Important Cheat Sheet

## Number

```js
Number("100");       // 100
Number("10.5");      // 10.5
Number("");          // 0
Number("hello");     // NaN
Number(true);        // 1
Number(false);       // 0
Number(null);        // 0
Number(undefined);   // NaN
```

---

## String

```js
String(100);         // "100"
String(true);        // "true"
String(false);       // "false"
String(null);        // "null"
String(undefined);   // "undefined"
```

---

## Boolean

```js
Boolean(1);          // true
Boolean(0);          // false
Boolean("hello");    // true
Boolean("");         // false
Boolean("false");    // true
Boolean(null);       // false
Boolean(undefined);  // false
Boolean([]);         // true
Boolean({});         // true
```

---

## Parsing

```js
parseInt("100", 10);       // 100
parseInt("10.5", 10);      // 10
parseInt("100px", 10);     // 100

parseFloat("10.5");        // 10.5
parseFloat("10.5px");      // 10.5
```

---

# 89. Mental Model

Remember this:

```text
                TYPE CONVERSION
                      │
          ┌───────────┴───────────┐
          │                       │
       Explicit                Implicit
          │                       │
      You convert             JS converts
          │                       │
    Number(value)              "10" - 2
    String(value)              "10" + 2
    Boolean(value)
          │
          ▼
     Check result
          │
     ┌────┼────┐
     │    │    │
 Number String Boolean
```

---

# 90. Most Important Rules

Memorize these:

```text
1. prompt() returns a string.
2. Use Number() when you need a number.
3. Number("hello") → NaN.
4. Number("") → 0.
5. Number(null) → 0.
6. Number(undefined) → NaN.
7. Boolean(0) → false.
8. Boolean("") → false.
9. Boolean("false") → true.
10. Boolean([]) → true.
11. Boolean({}) → true.
12. "10" + 5 → "105".
13. "10" - 5 → 5.
14. parseInt() extracts an integer prefix.
15. parseFloat() extracts a decimal prefix.
16. Number.isNaN() is useful for checking NaN.
17. Number.isInteger() checks for integers.
18. Number.isFinite() checks for finite numbers.
19. Prefer explicit conversion when clarity matters.
20. Use === instead of == in most modern JavaScript code.
```

---

# 91. Final Checklist

Before moving to the next topic, make sure you understand:

* [ ] What type conversion means
* [ ] Explicit conversion
* [ ] Implicit conversion
* [ ] Type coercion
* [ ] `typeof`
* [ ] `Number()`
* [ ] `String()`
* [ ] `Boolean()`
* [ ] `.toString()`
* [ ] `parseInt()`
* [ ] `parseFloat()`
* [ ] Radix
* [ ] `NaN`
* [ ] `Number.isNaN()`
* [ ] `Number.isInteger()`
* [ ] `Number.isFinite()`
* [ ] Truthy values
* [ ] Falsy values
* [ ] `null` conversion
* [ ] `undefined` conversion
* [ ] Array conversion
* [ ] Object conversion
* [ ] Unary `+`
* [ ] Unary `-`
* [ ] `!!`
* [ ] String concatenation
* [ ] Arithmetic coercion
* [ ] `==` vs `===`
* [ ] User input conversion
* [ ] Input validation
* [ ] Practical calculator programs

---

# 92. One-Line Summary

> **Type conversion is changing a value from one JavaScript data type to another, either explicitly by using functions such as `Number()`, `String()`, and `Boolean()`, or implicitly through JavaScript's type coercion rules.**

---

# 93. Next Topic

## 06 — Constants

You will learn:

```text
const
```

in more depth, including:

* Constant values
* Reassignment
* Objects with `const`
* Arrays with `const`
* Mutation vs reassignment
* `const` scope
* Best practices
* Common mistakes
* Real-world examples
