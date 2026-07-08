# DATATYPES

# Primitive Data Types

JavaScript provides several built-in data types to represent different kinds of values. These data types are broadly divided into two categories:

* **Primitive Data Types**
* **Non-Primitive (Reference) Data Types**

In this chapter, we'll first learn about **Primitive Data Types**.

---

# What are Primitive Data Types?

**Primitive data types** are the most basic types of data in JavaScript. A primitive value is a **single, immutable value**, meaning the value itself cannot be changed after it is created.

When you assign a primitive value to another variable, JavaScript creates a **copy** of that value instead of sharing the same memory location.

JavaScript has **7 primitive data types**:

* Number
* String
* Boolean
* Undefined
* Null
* BigInt
* Symbol

---

## Primitive vs Non-Primitive

| Primitive                | Non-Primitive                 |
| ------------------------ | ----------------------------- |
| Stores a single value    | Stores a collection of values |
| Immutable                | Mutable                       |
| Compared by value        | Compared by reference         |
| Stored directly          | Stored by reference           |
| Examples: Number, String | Examples: Object, Array       |

---

# 1. Number

The **Number** data type represents both **integer** and **floating-point (decimal)** numbers.

Unlike many programming languages, JavaScript has only **one number type** for all numeric values.

---

## Integer Numbers

```javascript
let age = 19;
let score = 100;
let temperature = -5;

console.log(age);
console.log(score);
console.log(temperature);
```

Output

```text
19
100
-5
```

---

## Decimal Numbers

```javascript
let price = 199.99;
let pi = 3.14159;

console.log(price);
console.log(pi);
```

Output

```text
199.99
3.14159
```

---

## Scientific Notation

Large or very small numbers can be written using exponential notation.

```javascript
let largeNumber = 5e6;
let smallNumber = 5e-6;

console.log(largeNumber);
console.log(smallNumber);
```

Output

```text
5000000
0.000005
```

---

## Special Number Values

### Infinity

```javascript
console.log(10 / 0);
```

Output

```text
Infinity
```

---

### -Infinity

```javascript
console.log(-10 / 0);
```

Output

```text
-Infinity
```

---

### NaN (Not a Number)

`NaN` represents an invalid mathematical operation.

```javascript
console.log("Hello" / 5);
```

Output

```text
NaN
```

Another example:

```javascript
console.log(Math.sqrt(-1));
```

Output

```text
NaN
```

---

## Checking Number Type

```javascript
let marks = 95;

console.log(typeof marks);
```

Output

```text
number
```

---

## Common Number Methods

```javascript
let price = 199.5678;

console.log(price.toFixed(2));
console.log(price.toPrecision(4));
console.log(Number.isInteger(price));
```

Output

```text
199.57
199.6
false
```

---

# 2. String

A **String** is a sequence of characters used to represent text.

Strings can contain:

* Letters
* Numbers
* Symbols
* Spaces
* Emojis
* Unicode characters

---

## Creating Strings

Strings can be created using:

### Single Quotes

```javascript
let name = 'Navaneeth';
```

---

### Double Quotes

```javascript
let city = "Hyderabad";
```

---

### Template Literals (Backticks)

```javascript
let language = `JavaScript`;
```

---

## String Example

```javascript
let firstName = "Navaneeth";
let lastName = "Kumar";

console.log(firstName);
console.log(lastName);
```

Output

```text
Navaneeth
Kumar
```

---

## String Concatenation

```javascript
let first = "Hello";
let second = "World";

console.log(first + " " + second);
```

Output

```text
Hello World
```

---

## Template Literals

Template literals allow you to embed variables directly inside strings.

```javascript
let name = "Navaneeth";
let age = 19;

console.log(`My name is ${name} and I am ${age} years old.`);
```

Output

```text
My name is Navaneeth and I am 19 years old.
```

---

## Escape Characters

```javascript
console.log("He said \"Hello\"");
console.log('It\'s JavaScript');
console.log("Line1\nLine2");
console.log("Column1\tColumn2");
```

Output

```text
He said "Hello"
It's JavaScript
Line1
Line2
Column1    Column2
```

---

## Checking String Type

```javascript
let course = "JavaScript";

console.log(typeof course);
```

Output

```text
string
```

---

## Common String Methods

```javascript
let text = "JavaScript";

console.log(text.length);
console.log(text.toUpperCase());
console.log(text.toLowerCase());
console.log(text.includes("Script"));
console.log(text.slice(0, 4));
```

Output

```text
10
JAVASCRIPT
javascript
true
Java
```

---

# 3. Boolean

A **Boolean** represents one of two values:

* `true`
* `false`

Booleans are commonly used in:

* Conditions
* Loops
* Comparisons
* Decision making

---

## Example

```javascript
let isLoggedIn = true;
let isAdmin = false;

console.log(isLoggedIn);
console.log(isAdmin);
```

Output

```text
true
false
```

---

## Comparison Operators Return Booleans

```javascript
console.log(10 > 5);
console.log(20 < 10);
console.log(5 === 5);
```

Output

```text
true
false
true
```

---

## Boolean in if Statement

```javascript
let isStudent = true;

if (isStudent) {
    console.log("Welcome Student");
}
```

Output

```text
Welcome Student
```

---

## Checking Boolean Type

```javascript
let value = false;

console.log(typeof value);
```

Output

```text
boolean
```

---

# 4. Undefined

`undefined` means a variable has been declared but **has not been assigned a value**.

---

## Example

```javascript
let age;

console.log(age);
```

Output

```text
undefined
```

---

## Function Without Return

```javascript
function greet() {}

console.log(greet());
```

Output

```text
undefined
```

Functions that don't explicitly return a value return `undefined`.

---

## Checking Undefined Type

```javascript
let x;

console.log(typeof x);
```

Output

```text
undefined
```

---

# 5. Null

`null` represents the **intentional absence of a value**.

Unlike `undefined`, which is assigned automatically by JavaScript, `null` is assigned manually by the programmer.

---

## Example

```javascript
let user = null;

console.log(user);
```

Output

```text
null
```

---

## Difference Between null and undefined

| undefined                | null                                         |
| ------------------------ | -------------------------------------------- |
| Automatically assigned   | Assigned by programmer                       |
| Means "not assigned yet" | Means "no value intentionally"               |
| Type is `"undefined"`    | `typeof` returns `"object"` (historical bug) |

---

## Strange Behavior

```javascript
console.log(typeof null);
```

Output

```text
object
```

This is a well-known historical bug in JavaScript that has been kept for backward compatibility.

---

# 6. BigInt

The **BigInt** data type is used to store integers that are **larger than the safe limit** of the Number type.

The maximum safe integer in JavaScript is:

```javascript
Number.MAX_SAFE_INTEGER
```

Output

```text
9007199254740991
```

For numbers larger than this, use `BigInt`.

---

## Creating BigInt

Add `n` to the end of an integer.

```javascript
let big = 123456789012345678901234567890n;

console.log(big);
```

Output

```text
123456789012345678901234567890n
```

---

## BigInt Operations

```javascript
let a = 100n;
let b = 50n;

console.log(a + b);
console.log(a - b);
console.log(a * b);
```

Output

```text
150n
50n
5000n
```

---

## Mixing Number and BigInt

```javascript
let a = 10n;
let b = 5;

console.log(a + b);
```

Output

```text
TypeError
```

You cannot mix `Number` and `BigInt` directly.

---

## Checking BigInt Type

```javascript
let value = 100n;

console.log(typeof value);
```

Output

```text
bigint
```

---

# 7. Symbol

A **Symbol** is a unique and immutable primitive value.

Every Symbol is unique, even if they have the same description.

Symbols are mainly used as unique property keys in objects to avoid naming conflicts.

---

## Creating Symbols

```javascript
let id = Symbol();
let userId = Symbol("userId");
```

---

## Unique Symbols

```javascript
let s1 = Symbol("id");
let s2 = Symbol("id");

console.log(s1 === s2);
```

Output

```text
false
```

Even though both symbols have the same description, they are different values.

---

## Using Symbol as Object Key

```javascript
const id = Symbol("id");

const user = {
    name: "Navaneeth",
    [id]: 101
};

console.log(user[id]);
```

Output

```text
101
```

The symbol property won't conflict with normal string property names.

---

## Checking Symbol Type

```javascript
let sym = Symbol();

console.log(typeof sym);
```

Output

```text
symbol
```

---

# Summary of Primitive Data Types

| Data Type     | Description                         | Example         |
| ------------- | ----------------------------------- | --------------- |
| **Number**    | Stores integers and decimal numbers | `10`, `3.14`    |
| **String**    | Stores text                         | `"Hello"`       |
| **Boolean**   | Stores logical values               | `true`, `false` |
| **Undefined** | Variable declared but not assigned  | `undefined`     |
| **Null**      | Intentional absence of a value      | `null`          |
| **BigInt**    | Stores very large integers          | `123456789n`    |
| **Symbol**    | Stores unique identifiers           | `Symbol("id")`  |

---

# Key Points to Remember

* JavaScript has **7 primitive data types**.
* Primitive values are **immutable**—their values cannot be changed after creation.
* Variables holding primitive values store the actual value, not a reference.
* `Number` handles both integers and floating-point values.
* `String` stores textual data and supports template literals.
* `Boolean` is used for logical operations and conditions.
* `undefined` means a value has not been assigned yet.
* `null` means the absence of a value is intentional.
* `BigInt` is used for integers larger than `Number.MAX_SAFE_INTEGER`.
* `Symbol` creates unique values, commonly used as unique object property keys.
