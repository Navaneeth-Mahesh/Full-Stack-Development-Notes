# JavaScript Strings

## Introduction

A **string** is one of the most commonly used data types in JavaScript.

A string is simply **a sequence of characters** enclosed within quotes.

A string can contain:

* Letters
* Numbers
* Symbols
* Spaces
* Emojis
* Special characters

Examples:

```javascript
"Hello"
"JavaScript"
"12345"
"Welcome to India"
"😊"
```

Whenever you work with text in JavaScript, you are working with **strings**.

---

# Why Do We Need Strings?

Imagine building a website without strings.

How would you display:

* User names
* Email addresses
* Passwords
* Product names
* Messages
* Error notifications
* Comments
* Chat messages

Almost every website uses strings everywhere.

Examples:

Instagram

```text
Navaneeth
```

Amazon

```text
Apple iPhone 16
```

YouTube

```text
Subscribe
```

Netflix

```text
Continue Watching
```

Everything above is a string.

---

# Creating Strings

JavaScript provides three ways to create strings.

---

## 1. Double Quotes

```javascript
let name = "Navaneeth";
```

---

## 2. Single Quotes

```javascript
let city = 'Hyderabad';
```

---

## 3. Template Literals (Backticks)

Uses the **backtick (`)** character.

```javascript
let language = `JavaScript`;
```

Template literals are the modern and recommended way because they support:

* Variable interpolation
* Multi-line strings

We will learn them later in this chapter.

---

# String Examples

```javascript
let firstName = "Navaneeth";
let lastName = "Mahesh";
let course = "Computer Science";
```

---

# String Length

Every string has a built-in property called `length`.

It tells us how many characters are present in the string.

Example

```javascript
let language = "JavaScript";

console.log(language.length);
```

Output

```text
10
```

Explanation

```
J a v a S c r i p t
1 2 3 4 5 6 7 8 9 10
```

Spaces are also counted.

Example

```javascript
let message = "Hello World";

console.log(message.length);
```

Output

```text
11
```

The space between "Hello" and "World" counts as one character.

---

# Accessing Individual Characters

Each character has an **index**.

Indexes start from **0**.

Example

```text
JavaScript

J  a  v  a  S  c  r  i  p  t
0  1  2  3  4  5  6  7  8  9
```

---

## Using Square Brackets

```javascript
let language = "JavaScript";

console.log(language[0]);
```

Output

```text
J
```

---

Another example

```javascript
console.log(language[4]);
```

Output

```text
S
```

---

# Accessing the Last Character

```javascript
let language = "JavaScript";

console.log(language[language.length - 1]);
```

Output

```text
t
```

Explanation

```javascript
language.length
```

returns

```text
10
```

Since indexing starts from zero,

Last index =

```text
10 - 1 = 9
```

Character at index 9 is

```text
t
```

---

# Strings are Immutable

One important concept.

Strings **cannot be modified directly**.

Example

```javascript
let name = "Navaneeth";

name[0] = "R";

console.log(name);
```

Output

```text
Navaneeth
```

Nothing changes.

Strings are immutable.

If you want to change a string, create a new one.

```javascript
let name = "Navaneeth";

name = "Rahul";

console.log(name);
```

Output

```text
Rahul
```

---

# String Concatenation

Concatenation means joining strings together.

Using `+`

```javascript
let firstName = "Navaneeth";
let lastName = "Mahesh";

let fullName = firstName + " " + lastName;

console.log(fullName);
```

Output

```text
Navaneeth Mahesh
```

---

# Using Template Literals

Instead of

```javascript
let message = "Hello " + firstName;
```

Use

```javascript
let message = `Hello ${firstName}`;

console.log(message);
```

Output

```text
Hello Navaneeth
```

---

# Multiple Variables

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

# Multi-line Strings

Without template literals

```javascript
let message = "Hello
World";
```

This causes an error.

Using backticks

```javascript
let message = `Hello
World`;

console.log(message);
```

Output

```text
Hello
World
```

---

# Escape Characters

Sometimes we need special characters inside strings.

---

## Double Quotes

```javascript
let message = "He said \"Hello\"";

console.log(message);
```

Output

```text
He said "Hello"
```

---

## Single Quote

```javascript
let message = 'It\'s JavaScript';

console.log(message);
```

Output

```text
It's JavaScript
```

---

## New Line

```javascript
console.log("Hello\nWorld");
```

Output

```text
Hello
World
```

---

## Tab Space

```javascript
console.log("Name\tAge");
```

Output

```text
Name    Age
```

---

## Backslash

```javascript
console.log("C:\\Users\\Navaneeth");
```

Output

```text
C:\Users\Navaneeth
```

---

# Common String Methods

JavaScript provides many built-in methods.

---

# `toUpperCase()`

Converts all letters to uppercase.

```javascript
let name = "navaneeth";

console.log(name.toUpperCase());
```

Output

```text
NAVANEETH
```

---

# `toLowerCase()`

```javascript
let name = "NAVANEETH";

console.log(name.toLowerCase());
```

Output

```text
navaneeth
```

---

# `trim()`

Removes spaces from the beginning and end.

```javascript
let name = "   JavaScript   ";

console.log(name.trim());
```

Output

```text
JavaScript
```

---

# `includes()`

Checks whether a string contains another string.

```javascript
let language = "JavaScript";

console.log(language.includes("Script"));
```

Output

```text
true
```

---

# `startsWith()`

```javascript
let language = "JavaScript";

console.log(language.startsWith("Java"));
```

Output

```text
true
```

---

# `endsWith()`

```javascript
let language = "JavaScript";

console.log(language.endsWith("Script"));
```

Output

```text
true
```

---

# `indexOf()`

Returns the index of the first occurrence.

```javascript
let language = "JavaScript";

console.log(language.indexOf("S"));
```

Output

```text
4
```

If not found

```javascript
console.log(language.indexOf("Python"));
```

Output

```text
-1
```

---

# `slice()`

Extracts part of a string.

```javascript
let language = "JavaScript";

console.log(language.slice(0, 4));
```

Output

```text
Java
```

Another example

```javascript
console.log(language.slice(4));
```

Output

```text
Script
```

---

# `replace()`

Replaces the first occurrence.

```javascript
let text = "Hello World";

console.log(text.replace("World", "JavaScript"));
```

Output

```text
Hello JavaScript
```

---

# `replaceAll()`

Replaces all occurrences.

```javascript
let text = "cat cat cat";

console.log(text.replaceAll("cat", "dog"));
```

Output

```text
dog dog dog
```

---

# `split()`

Converts a string into an array.

```javascript
let text = "Apple,Banana,Mango";

console.log(text.split(","));
```

Output

```text
["Apple", "Banana", "Mango"]
```

---

# Method Chaining

Methods can be combined.

```javascript
let name = "   javascript   ";

console.log(name.trim().toUpperCase());
```

Output

```text
JAVASCRIPT
```

---

# Comparing Strings

```javascript
let a = "Apple";
let b = "Apple";

console.log(a === b);
```

Output

```text
true
```

Another example

```javascript
console.log("Apple" === "apple");
```

Output

```text
false
```

JavaScript comparisons are **case-sensitive**.

---

# Looping Through Strings

```javascript
let language = "JavaScript";

for (let letter of language) {

    console.log(letter);

}
```

Output

```text
J
a
v
a
S
c
r
i
p
t
```

---

# String vs Number

```javascript
let a = "10";
let b = 10;

console.log(a === b);
```

Output

```text
false
```

Because one is a string and the other is a number.

---

# Converting to String

```javascript
let number = 100;

let text = String(number);

console.log(text);
```

Output

```text
100
```

---

# Common Beginner Mistakes

## Forgetting Quotes

Wrong

```javascript
let name = Navaneeth;
```

Correct

```javascript
let name = "Navaneeth";
```

---

## Using `+` Instead of Template Literals

Less readable

```javascript
let name = "Navaneeth";

console.log("Hello " + name);
```

Better

```javascript
console.log(`Hello ${name}`);
```

---

## Trying to Modify a Character

Wrong

```javascript
let text = "Java";

text[0] = "P";
```

Strings are immutable.

---

# Real-World Uses

Strings are used everywhere.

Examples

* User names
* Passwords
* Email addresses
* Product names
* Search bars
* URLs
* API responses
* Chat messages
* File names
* Error messages

Almost every web application processes strings continuously.

---

# Practice Questions

1. What is a string?
2. Name the three ways to create strings in JavaScript.
3. What does the `length` property do?
4. Why are strings called immutable?
5. What is string concatenation?
6. What are template literals?
7. What is the difference between `replace()` and `replaceAll()`?
8. What does `split()` return?
9. Why is `===` preferred when comparing strings?
10. Explain method chaining with an example.

---

# Coding Exercises

## Exercise 1

Print your full name using template literals.

---

## Exercise 2

Print the first and last character of your name.

---

## Exercise 3

Convert a sentence to uppercase.

---

## Exercise 4

Remove extra spaces from:

```text
"   JavaScript is Awesome   "
```

---

## Exercise 5

Check whether the word **"Developer"** contains `"Dev"`.

---

## Exercise 6

Replace `"Python"` with `"JavaScript"` in a sentence.

---

## Exercise 7

Split this string into an array.

```text
HTML,CSS,JavaScript,React
```

---

## Exercise 8

Reverse a string using a loop.

Example

```text
JavaScript
```

Expected Output

```text
tpircSavaJ
```

---

## Exercise 9

Count how many vowels are present in a string.

Example

```text
Programming
```

Expected Output

```text
3
```

---

## Exercise 10 (Mini Challenge)

Ask the user to enter their full name.

Then display:

* Original name
* Name in uppercase
* Name in lowercase
* Total number of characters
* First character
* Last character
* Whether the name starts with `"N"`
* Whether the name ends with `"h"`

This exercise combines string methods, indexing, properties, user input, and conditional statements, making it excellent practice for mastering JavaScript strings.
