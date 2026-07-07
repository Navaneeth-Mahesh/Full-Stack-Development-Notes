# JavaScript Data Types

## What are Data Types?

A **data type** tells JavaScript what kind of value a variable stores.

Think of it like this:

- `"Navaneeth"` → Text
- `19` → Number
- `true` → Yes/No value

Different types of data are stored differently and have different operations.

---

# JavaScript has 8 Data Types

| Data Type | Example |
|-----------|---------|
| String | `"Hello"` |
| Number | `100` |
| BigInt | `12345678901234567890n` |
| Boolean | `true` |
| Undefined | `undefined` |
| Null | `null` |
| Symbol | `Symbol("id")` |
| Object | `{ name: "John" }` |

These are divided into **Primitive** and **Non-Primitive** data types.

---

# 1. Primitive Data Types

Primitive values store a **single value**.

There are **7 primitive data types**.

## String

Stores text.

```javascript
let name = "Navaneeth";

console.log(name);
```

Output

```
Navaneeth
```

Strings can use:

```javascript
"Double Quotes"
'Single Quotes'
`Backticks`
```

Example

```javascript
let city = "Hyderabad";
let country = 'India';
let message = `Welcome`;

console.log(city);
console.log(country);
console.log(message);
```

---

## Number

Stores integers and decimal numbers.

```javascript
let age = 18;
let price = 99.99;

console.log(age);
console.log(price);
```

Output

```
18
99.99
```

JavaScript has only one Number type.

Both are Numbers:

```javascript
10
10.5
```

---

## BigInt

Used for very large integers.

Example

```javascript
let bigNumber = 123456789012345678901234567890n;

console.log(bigNumber);
```

Notice the **`n`** at the end.

Without `n`, JavaScript may lose precision for extremely large integers.

---

## Boolean

Stores only two values.

- `true`
- `false`

Example

```javascript
let isStudent = true;
let isLoggedIn = false;

console.log(isStudent);
console.log(isLoggedIn);
```

Booleans are commonly used in conditions.

```javascript
let age = 18;

console.log(age >= 18);
```

Output

```
true
```

---

## Undefined

A variable that has been declared but **not assigned a value**.

```javascript
let username;

console.log(username);
```

Output

```
undefined
```

---

## Null

Represents an **intentional empty value**.

```javascript
let user = null;

console.log(user);
```

Output

```
null
```

Difference:

```javascript
let a;
let b = null;

console.log(a); // undefined
console.log(b); // null
```

- `undefined` → No value assigned yet.
- `null` → Value intentionally set to empty.

---

## Symbol

Creates a unique value.

```javascript
let id1 = Symbol("id");
let id2 = Symbol("id");

console.log(id1 === id2);
```

Output

```
false
```

Even though both have the same description, every Symbol is unique.

Symbols are mostly used for creating unique object property keys.

---

# 2. Non-Primitive Data Type

JavaScript has one main non-primitive type:

## Object

Objects store multiple values using **key-value pairs**.

```javascript
let student = {
    name: "Navaneeth",
    age: 18,
    course: "B.Tech"
};

console.log(student);
```

Output

```
{
  name: 'Navaneeth',
  age: 18,
  course: 'B.Tech'
}
```

Access properties

```javascript
console.log(student.name);
console.log(student.age);
```

Output

```
Navaneeth
18
```

---

# Arrays

Arrays are a special kind of Object.

```javascript
let fruits = ["Apple", "Banana", "Mango"];

console.log(fruits);
```

Output

```
[ 'Apple', 'Banana', 'Mango' ]
```

Access an element

```javascript
console.log(fruits[0]);
```

Output

```
Apple
```

---

# Functions

Functions are also Objects in JavaScript.

```javascript
function greet() {
    console.log("Hello");
}

greet();
```

Output

```
Hello
```

---

# Checking Data Types

Use the `typeof` operator.

Syntax

```javascript
typeof value
```

Examples

```javascript
console.log(typeof "Hello");
console.log(typeof 100);
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof {});
console.log(typeof []);
console.log(typeof function () {});
```

Output

```
string
number
boolean
undefined
object
object
object
function
```

### Important Note

```javascript
typeof null
```

returns

```
object
```

This is a well-known historical bug in JavaScript that has been kept for backward compatibility.

---

# Primitive vs Non-Primitive

| Primitive | Non-Primitive |
|------------|---------------|
| Stores a single value | Stores collections of values |
| Immutable | Mutable |
| Compared by value | Compared by reference |
| Stored directly | Stored by reference |

Example

```javascript
let x = 10;
let y = x;

y = 20;

console.log(x);
console.log(y);
```

Output

```
10
20
```

Objects behave differently.

```javascript
let person1 = {
    name: "John"
};

let person2 = person1;

person2.name = "Mike";

console.log(person1.name);
```

Output

```
Mike
```

Both variables refer to the same object.

---

# Summary

| Data Type | Primitive? | Example |
|-----------|------------|---------|
| String | Yes | `"Hello"` |
| Number | Yes | `100` |
| BigInt | Yes | `100n` |
| Boolean | Yes | `true` |
| Undefined | Yes | `undefined` |
| Null | Yes | `null` |
| Symbol | Yes | `Symbol()` |
| Object | No | `{}` |
| Array | No (Object) | `[]` |
| Function | No (Object) | `function(){}` |

---

# Key Points

- JavaScript has **8 data types**.
- **7 are primitive** and **1 is non-primitive (Object)**.
- Arrays and Functions are special kinds of Objects.
- Use `typeof` to check the type of a value.
- `null` is intentionally empty, while `undefined` means no value has been assigned.
- Objects are stored by reference, while primitive values are stored directly.