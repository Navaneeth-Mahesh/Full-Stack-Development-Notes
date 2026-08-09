# 04 — Accept User Input in JavaScript

> User input allows a JavaScript program to receive information from the person using the application.

Examples:

```text
What is your name?
What is your age?
What is your email?
What number do you want to calculate?
```

User input is essential for building interactive programs.

---

# 1. What Is User Input?

**User input** is information provided by a user to a program.

For example:

```text
Program: What is your name?

User: Navaneeth
```

The program receives:

```text
"Navaneeth"
```

and can store it inside a variable.

```js
const name = "Navaneeth";
```

---

# 2. Why Do We Need User Input?

Without user input, programs can only work with predefined values.

Example:

```js
const name = "Navaneeth";

console.log(`Hello ${name}`);
```

The program always uses:

```text
Navaneeth
```

With user input:

```text
Enter your name:
> Navaneeth
```

Another user could enter:

```text
> Rahul
```

or:

```text
> Ananya
```

Now the same program can work with different users.

---

# 3. Two Common Ways to Accept Input

The method depends on where JavaScript is running.

## Browser

You can use:

```js
prompt()
```

Example:

```js
const name = prompt("Enter your name:");

console.log(name);
```

---

## Node.js

For terminal applications, you can use:

```js
readline
```

Example:

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const name = await rl.question("Enter your name: ");

console.log(`Hello ${name}`);

rl.close();
```

---

# 4. Browser `prompt()`

The simplest way to accept user input in a browser is:

```js
prompt()
```

Example:

```js
const name = prompt("What is your name?");

console.log(name);
```

When the browser executes this, a dialog box appears.

```text
┌──────────────────────────────┐
│ What is your name?            │
│                              │
│ [ Navaneeth              ]   │
│                              │
│       Cancel    OK           │
└──────────────────────────────┘
```

If the user enters:

```text
Navaneeth
```

then:

```js
name
```

contains:

```text
"Navaneeth"
```

---

# 5. Basic `prompt()` Syntax

```js
const variable = prompt("Question");
```

Example:

```js
const name = prompt("Enter your name:");

console.log(name);
```

---

# 6. Example — Ask for Name

```js
const name = prompt("Enter your name:");

console.log(`Hello, ${name}!`);
```

If the user enters:

```text
Navaneeth
```

Output:

```text
Hello, Navaneeth!
```

---

# 7. Example — Ask for Age

```js
const age = prompt("Enter your age:");

console.log(`You are ${age} years old.`);
```

If the user enters:

```text
20
```

the value is initially:

```text
"20"
```

not:

```text
20
```

This is extremely important.

---

# 8. `prompt()` Returns a String

Even if the user enters a number:

```js
const age = prompt("Enter your age:");
```

and enters:

```text
20
```

JavaScript receives:

```js
"20"
```

The value is a **string**.

You can verify this:

```js
const age = prompt("Enter your age:");

console.log(typeof age);
```

Output:

```text
string
```

---

# 9. Why Does This Matter?

Consider:

```js
const age = prompt("Enter your age:");

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

Why?

Because:

```js
"20" + 1
```

becomes:

```text
"201"
```

JavaScript performs string concatenation.

---

# 10. Converting Input to a Number

Use:

```js
Number()
```

Example:

```js
const age = Number(prompt("Enter your age:"));

console.log(age);
```

Now the input:

```text
20
```

becomes:

```js
20
```

which is a number.

---

# 11. Checking the Type

```js
const age = Number(prompt("Enter your age:"));

console.log(typeof age);
```

Output:

```text
number
```

---

# 12. Example — Add Two Numbers

Without conversion:

```js
const num1 = prompt("Enter first number:");
const num2 = prompt("Enter second number:");

console.log(num1 + num2);
```

Input:

```text
10
20
```

Output:

```text
1020
```

Because:

```js
"10" + "20"
```

becomes:

```text
"1020"
```

---

# 13. Correct Version

Convert the input:

```js
const num1 = Number(prompt("Enter first number:"));
const num2 = Number(prompt("Enter second number:"));

const sum = num1 + num2;

console.log(`Sum: ${sum}`);
```

Input:

```text
10
20
```

Output:

```text
Sum: 30
```

---

# 14. `Number()`

`Number()` converts a value into a number when possible.

Examples:

```js
console.log(Number("10"));
```

Output:

```text
10
```

```js
console.log(Number("10.5"));
```

Output:

```text
10.5
```

```js
console.log(Number("100"));
```

Output:

```text
100
```

---

# 15. Invalid Number Conversion

If conversion isn't possible:

```js
console.log(Number("hello"));
```

Output:

```text
NaN
```

`NaN` means:

```text
Not-a-Number
```

More precisely, it is a special numeric value representing an invalid numeric result.

---

# 16. Checking for `NaN`

Use:

```js
Number.isNaN()
```

Example:

```js
const age = Number(prompt("Enter your age:"));

if (Number.isNaN(age)) {
  console.log("Please enter a valid number.");
}
```

---

# 17. `prompt()` Can Return `null`

If the user presses **Cancel**:

```js
const name = prompt("Enter your name:");

console.log(name);
```

The result can be:

```js
null
```

Therefore, user input should not always be assumed to exist.

---

# 18. Checking for Cancel

```js
const name = prompt("Enter your name:");

if (name === null) {
  console.log("User cancelled the input.");
} else {
  console.log(`Hello ${name}`);
}
```

---

# 19. Checking Empty Input

The user may press OK without entering anything.

Example:

```js
const name = prompt("Enter your name:");

if (name === "") {
  console.log("You didn't enter a name.");
}
```

A better check:

```js
if (name === null || name.trim() === "") {
  console.log("Please enter your name.");
}
```

---

# 20. `trim()`

`trim()` removes whitespace from the beginning and end of a string.

Example:

```js
const name = "   Navaneeth   ";

console.log(name.trim());
```

Output:

```text
Navaneeth
```

This is useful for validating user input.

---

# 21. Complete Name Input Example

```js
const name = prompt("Enter your name:");

if (name === null) {
  console.log("Input cancelled.");
} else if (name.trim() === "") {
  console.log("Name cannot be empty.");
} else {
  console.log(`Hello, ${name.trim()}!`);
}
```

---

# 22. Multiple Inputs

You can ask multiple questions.

```js
const firstName = prompt("Enter your first name:");
const lastName = prompt("Enter your last name:");

console.log(`Full name: ${firstName} ${lastName}`);
```

---

# 23. Example — Student Details

```js
const name = prompt("Enter your name:");
const age = Number(prompt("Enter your age:"));
const branch = prompt("Enter your branch:");

console.log("===== Student Details =====");
console.log(`Name: ${name}`);
console.log(`Age: ${age}`);
console.log(`Branch: ${branch}`);
```

---

# 24. Example — Simple Calculator

```js
const num1 = Number(prompt("Enter first number:"));
const num2 = Number(prompt("Enter second number:"));

console.log(`Addition: ${num1 + num2}`);
console.log(`Subtraction: ${num1 - num2}`);
console.log(`Multiplication: ${num1 * num2}`);
console.log(`Division: ${num1 / num2}`);
```

---

# 25. Example — Rectangle Area

Formula:

```text
Area = length × width
```

JavaScript:

```js
const length = Number(prompt("Enter length:"));
const width = Number(prompt("Enter width:"));

const area = length * width;

console.log(`Area: ${area}`);
```

---

# 26. Example — Circle Area

Formula:

```text
Area = π × r²
```

JavaScript:

```js
const radius = Number(prompt("Enter radius:"));

const area = Math.PI * radius ** 2;

console.log(`Area: ${area}`);
```

---

# 27. Example — Celsius to Fahrenheit

Formula:

```text
F = (C × 9 / 5) + 32
```

Code:

```js
const celsius = Number(prompt("Enter temperature in Celsius:"));

const fahrenheit = (celsius * 9) / 5 + 32;

console.log(`${celsius}°C = ${fahrenheit}°F`);
```

---

# 28. Example — Age Calculation

```js
const birthYear = Number(prompt("Enter your birth year:"));

const currentYear = new Date().getFullYear();

const age = currentYear - birthYear;

console.log(`You are approximately ${age} years old.`);
```

---

# 29. Browser Input vs Node.js Input

JavaScript can run in different environments.

## Browser

Common beginner method:

```js
const name = prompt("Enter your name:");
```

## Node.js

Terminal input:

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const name = await rl.question("Enter your name: ");

console.log(`Hello ${name}`);

rl.close();
```

---

# 30. Node.js `readline`

Node.js does not normally provide browser-style `prompt()`.

For terminal applications, one common approach is:

```js
import readline from "readline/promises";
```

Then create an interface:

```js
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
```

---

# 31. Understanding `process.stdin`

```js
process.stdin
```

represents standard input.

Usually:

```text
Keyboard
   ↓
process.stdin
   ↓
Node.js program
```

When the user types into the terminal, Node.js receives that input through standard input.

---

# 32. Understanding `process.stdout`

```js
process.stdout
```

represents standard output.

Usually:

```text
Node.js program
   ↓
process.stdout
   ↓
Terminal
```

This is why we provide:

```js
output: process.stdout
```

to `readline`.

---

# 33. Basic Node.js Input

Create a file:

```text
input.js
```

Code:

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const name = await rl.question("Enter your name: ");

console.log(`Hello, ${name}!`);

rl.close();
```

Run:

```bash
node input.js
```

Example:

```text
Enter your name: Navaneeth
Hello, Navaneeth!
```

---

# 34. Why `await`?

The user doesn't answer immediately.

The program must wait.

```js
const name = await rl.question("Enter your name: ");
```

Conceptually:

```text
Ask question
      ↓
Wait for user
      ↓
User types answer
      ↓
Continue program
```

This introduces the concept of **asynchronous JavaScript**, which you will study later.

---

# 35. Multiple Node.js Inputs

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const name = await rl.question("Enter your name: ");
const age = await rl.question("Enter your age: ");
const city = await rl.question("Enter your city: ");

console.log("\n===== PROFILE =====");
console.log(`Name: ${name}`);
console.log(`Age: ${age}`);
console.log(`City: ${city}`);

rl.close();
```

---

# 36. Converting Node.js Input

Remember:

```js
rl.question()
```

returns a string.

Example:

```js
const age = await rl.question("Enter your age: ");

console.log(typeof age);
```

Output:

```text
string
```

Convert it:

```js
const age = Number(
  await rl.question("Enter your age: ")
);
```

Now:

```js
console.log(typeof age);
```

Output:

```text
number
```

---

# 37. Node.js Calculator

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const num1 = Number(
  await rl.question("Enter first number: ")
);

const num2 = Number(
  await rl.question("Enter second number: ")
);

console.log(`Sum: ${num1 + num2}`);

rl.close();
```

Example:

```text
Enter first number: 20
Enter second number: 30
Sum: 50
```

---

# 38. Node.js Profile Program

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const name = await rl.question("Enter your name: ");
const age = Number(
  await rl.question("Enter your age: ")
);
const city = await rl.question("Enter your city: ");
const profession = await rl.question(
  "Enter your profession: "
);

console.log("\n==============================");
console.log("          PROFILE");
console.log("==============================");

console.log(`Name       : ${name}`);
console.log(`Age        : ${age}`);
console.log(`City       : ${city}`);
console.log(`Profession : ${profession}`);

rl.close();
```

---

# 39. Input Validation

**Input validation** means checking whether the user's input is acceptable.

For example:

```text
Age should be a number.
Age should be positive.
Name should not be empty.
Email should have a valid format.
```

Never blindly trust user input.

---

# 40. Validate a Number

```js
const age = Number(prompt("Enter your age:"));

if (Number.isNaN(age)) {
  console.log("Invalid age.");
} else {
  console.log(`Your age is ${age}`);
}
```

---

# 41. Validate Positive Number

```js
const age = Number(prompt("Enter your age:"));

if (Number.isNaN(age)) {
  console.log("Please enter a number.");
} else if (age < 0) {
  console.log("Age cannot be negative.");
} else {
  console.log(`Age: ${age}`);
}
```

---

# 42. Validate Age Range

```js
const age = Number(prompt("Enter your age:"));

if (Number.isNaN(age)) {
  console.log("Enter a valid number.");
} else if (age < 0 || age > 120) {
  console.log("Enter a realistic age.");
} else {
  console.log(`Valid age: ${age}`);
}
```

---

# 43. Validate Required Name

```js
const name = prompt("Enter your name:");

if (name === null || name.trim() === "") {
  console.log("Name is required.");
} else {
  console.log(`Welcome, ${name.trim()}!`);
}
```

---

# 44. Validate Multiple Conditions

```js
const age = Number(prompt("Enter your age:"));

if (
  Number.isNaN(age) ||
  age < 0 ||
  age > 120
) {
  console.log("Invalid age.");
} else {
  console.log("Valid age.");
}
```

---

# 45. `parseInt()`

Another way to convert strings to integers is:

```js
parseInt()
```

Example:

```js
const age = parseInt("20", 10);

console.log(age);
```

Output:

```text
20
```

The second argument specifies the radix:

```js
parseInt("20", 10);
```

For decimal integers, using radix `10` is a good habit.

---

# 46. `parseFloat()`

Use:

```js
parseFloat()
```

when you want to parse a decimal number.

Example:

```js
const price = parseFloat("99.99");

console.log(price);
```

Output:

```text
99.99
```

---

# 47. `Number()` vs `parseInt()` vs `parseFloat()`

Consider:

```js
Number("10.5");
```

Result:

```text
10.5
```

```js
parseFloat("10.5");
```

Result:

```text
10.5
```

```js
parseInt("10.5", 10);
```

Result:

```text
10
```

So:

```text
Number()    → converts the entire value when valid
parseInt()  → parses an integer
parseFloat()→ parses a floating-point number
```

---

# 48. Important Difference

Consider:

```js
Number("123abc");
```

Result:

```text
NaN
```

But:

```js
parseInt("123abc", 10);
```

may return:

```text
123
```

And:

```js
parseFloat("123.45abc");
```

may return:

```text
123.45
```

Therefore, for form-like numeric input where the entire string should be a valid number, `Number()` is often easier to reason about.

---

# 49. Boolean Input

User input normally arrives as text.

Suppose the user enters:

```text
true
```

This is:

```js
"true"
```

not:

```js
true
```

This does NOT convert it to a boolean:

```js
Boolean("false");
```

It returns:

```text
true
```

because any non-empty string is truthy.

---

# 50. Converting `"true"` and `"false"` Properly

If you specifically expect those exact strings:

```js
const input = prompt("Enter true or false:");

const value = input === "true";

console.log(value);
```

Input:

```text
true
```

Output:

```text
true
```

Input:

```text
false
```

Output:

```text
false
```

A production application should usually validate unexpected values as well.

---

# 51. Truthy and Falsy Input

JavaScript has truthy and falsy values.

Examples of commonly falsy values:

```js
false
0
-0
0n
""
null
undefined
NaN
```

Example:

```js
const name = "";

if (name) {
  console.log("Name exists");
} else {
  console.log("Name is empty");
}
```

Output:

```text
Name is empty
```

---

# 52. Input and Template Literals

Template literals make output easier.

```js
const name = prompt("Enter your name:");
const age = Number(prompt("Enter your age:"));

console.log(
  `Hello ${name}, you are ${age} years old.`
);
```

---

# 53. Input and Arithmetic

```js
const price = Number(prompt("Enter product price:"));
const quantity = Number(prompt("Enter quantity:"));

const total = price * quantity;

console.log(`Total: ₹${total}`);
```

---

# 54. Input and Conditions

```js
const age = Number(prompt("Enter your age:"));

if (age >= 18) {
  console.log("You are an adult.");
} else {
  console.log("You are a minor.");
}
```

---

# 55. Input and Loops

User input can also control loops.

Example:

```js
const number = Number(prompt("Enter a number:"));

for (let i = 1; i <= number; i++) {
  console.log(i);
}
```

Input:

```text
5
```

Output:

```text
1
2
3
4
5
```

---

# 56. Input and Functions

You can pass user input into functions.

```js
function greet(name) {
  console.log(`Hello, ${name}!`);
}

const name = prompt("Enter your name:");

greet(name);
```

---

# 57. Input and Arrays

You can collect multiple values.

```js
const name1 = prompt("Enter first name:");
const name2 = prompt("Enter second name:");
const name3 = prompt("Enter third name:");

const names = [name1, name2, name3];

console.log(names);
```

---

# 58. Better Approach — Reusable Input Function

In Node.js, you can create helper functions.

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function ask(question) {
  return await rl.question(question);
}

const name = await ask("Enter your name: ");
const city = await ask("Enter your city: ");

console.log(`Hello ${name} from ${city}`);

rl.close();
```

This makes repeated input cleaner.

---

# 59. Number Input Helper

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function askNumber(question) {
  return Number(await rl.question(question));
}

const age = await askNumber("Enter your age: ");
const score = await askNumber("Enter your score: ");

console.log(`Age: ${age}`);
console.log(`Score: ${score}`);

rl.close();
```

---

# 60. Validated Number Input

A more useful helper:

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function askNumber(question) {
  while (true) {
    const input = await rl.question(question);
    const value = Number(input);

    if (!Number.isNaN(value)) {
      return value;
    }

    console.log("Please enter a valid number.");
  }
}

const age = await askNumber("Enter your age: ");

console.log(`Your age is ${age}`);

rl.close();
```

This combines:

* User input
* Conversion
* Validation
* Loops
* Functions

---

# 61. Mini Project — Student Grade Input

```js
const name = prompt("Enter your name:");

const marks = Number(
  prompt("Enter your marks:")
);

if (name === null || name.trim() === "") {
  console.log("Name is required.");
} else if (Number.isNaN(marks)) {
  console.log("Marks must be a number.");
} else if (marks < 0 || marks > 100) {
  console.log("Marks must be between 0 and 100.");
} else {
  console.log("======================");
  console.log(`Student: ${name.trim()}`);
  console.log(`Marks: ${marks}`);
  console.log("======================");
}
```

---

# 62. Mini Project — BMI Calculator

Formula:

```text
BMI = weight / height²
```

Assume:

```text
weight → kilograms
height → meters
```

Code:

```js
const weight = Number(
  prompt("Enter weight in kg:")
);

const height = Number(
  prompt("Enter height in meters:")
);

const bmi = weight / height ** 2;

console.log(`Your BMI is ${bmi.toFixed(2)}`);
```

---

# 63. Mini Project — Bill Calculator

```js
const price = Number(
  prompt("Enter product price:")
);

const quantity = Number(
  prompt("Enter quantity:")
);

const taxRate = 0.18;

const subtotal = price * quantity;
const tax = subtotal * taxRate;
const total = subtotal + tax;

console.log("========== BILL ==========");
console.log(`Subtotal : ₹${subtotal}`);
console.log(`Tax      : ₹${tax}`);
console.log(`Total    : ₹${total}`);
console.log("==========================");
```

---

# 64. Mini Project — Login Simulation

```js
const username = prompt("Enter username:");
const password = prompt("Enter password:");

const correctUsername = "admin";
const correctPassword = "1234";

if (
  username === correctUsername &&
  password === correctPassword
) {
  console.log("Login successful.");
} else {
  console.log("Invalid username or password.");
}
```

> This is only a learning example. Real applications should never store or compare passwords like this on the client side.

---

# 65. Mini Project — Simple Calculator

```js
const num1 = Number(prompt("Enter first number:"));
const operator = prompt("Enter operator (+, -, *, /):");
const num2 = Number(prompt("Enter second number:"));

if (Number.isNaN(num1) || Number.isNaN(num2)) {
  console.log("Please enter valid numbers.");
} else if (operator === "+") {
  console.log(`Result: ${num1 + num2}`);
} else if (operator === "-") {
  console.log(`Result: ${num1 - num2}`);
} else if (operator === "*") {
  console.log(`Result: ${num1 * num2}`);
} else if (operator === "/") {
  if (num2 === 0) {
    console.log("Cannot divide by zero.");
  } else {
    console.log(`Result: ${num1 / num2}`);
  }
} else {
  console.log("Invalid operator.");
}
```

---

# 66. Browser vs Node.js — Quick Comparison

| Feature                 | Browser         | Node.js             |
| ----------------------- | --------------- | ------------------- |
| Basic input             | `prompt()`      | `readline`          |
| Input source            | Dialog          | Terminal            |
| Output                  | `console.log()` | `console.log()`     |
| Common use              | Web apps        | CLI/server programs |
| Input usually starts as | String          | String              |

---

# 67. Common Mistakes

## Mistake 1 — Forgetting conversion

```js
const age = prompt("Enter age:");

console.log(age + 1);
```

Input:

```text
20
```

Output:

```text
201
```

Correct:

```js
const age = Number(prompt("Enter age:"));

console.log(age + 1);
```

Output:

```text
21
```

---

# 68. Mistake 2 — Assuming Input Is Always Valid

Bad:

```js
const age = Number(prompt("Enter age:"));

console.log(age + 10);
```

The user could enter:

```text
hello
```

Then:

```text
age = NaN
```

Better:

```js
const age = Number(prompt("Enter age:"));

if (Number.isNaN(age)) {
  console.log("Invalid number.");
} else {
  console.log(age + 10);
}
```

---

# 69. Mistake 3 — Ignoring Cancel

Bad:

```js
const name = prompt("Enter name:");

console.log(name.toUpperCase());
```

If the user clicks Cancel:

```text
name = null
```

Calling:

```js
null.toUpperCase()
```

causes an error.

Better:

```js
const name = prompt("Enter name:");

if (name === null) {
  console.log("Input cancelled.");
} else {
  console.log(name.toUpperCase());
}
```

---

# 70. Mistake 4 — Assuming `"false"` Is False

This:

```js
Boolean("false")
```

returns:

```text
true
```

because `"false"` is a non-empty string.

Never assume string input automatically becomes the intended boolean.

---

# 71. Mistake 5 — Not Trimming Text

Input:

```text
"   Navaneeth   "
```

contains unnecessary spaces.

Use:

```js
name.trim()
```

to normalize it for many simple text-input cases.

---

# 72. Best Practices

## 1. Validate input

Never blindly trust user input.

---

## 2. Convert numeric input

Use:

```js
Number()
```

when you expect a number.

---

## 3. Check `NaN`

Use:

```js
Number.isNaN()
```

---

## 4. Handle cancellation

Browser `prompt()` can return:

```js
null
```

---

## 5. Trim text

Use:

```js
.trim()
```

when leading/trailing whitespace should not matter.

---

## 6. Give useful prompts

Bad:

```js
prompt("Input:");
```

Better:

```js
prompt("Enter your age:");
```

Best:

```js
prompt("Enter your age in years:");
```

The user should know exactly what is expected.

---

# 73. Important Concepts to Remember

```text
User Input
    ↓
Usually arrives as text
    ↓
Validate it
    ↓
Convert it if necessary
    ↓
Use it in your program
```

For numbers:

```text
"25"
 ↓
Number()
 ↓
25
```

For text:

```text
"Navaneeth"
 ↓
trim()
 ↓
"Navaneeth"
```

For browser cancellation:

```text
Cancel
 ↓
null
```

---

# 74. Complete Mental Model

```text
                  USER
                    │
                    ▼
             Enters information
                    │
                    ▼
              JavaScript
                    │
          ┌─────────┴─────────┐
          │                   │
       Browser             Node.js
          │                   │
      prompt()             readline
          │                   │
          └─────────┬─────────┘
                    ▼
                String
                    │
                    ▼
               Validation
                    │
                    ▼
              Type Conversion
                    │
          ┌─────────┼─────────┐
          │         │         │
        String    Number    Boolean
          │         │         │
          ▼         ▼         ▼
       Program   Program   Program
```

---

# 75. Quick Reference

### Browser

```js
const name = prompt("Enter your name:");
```

### Number input

```js
const age = Number(prompt("Enter your age:"));
```

### Check number

```js
if (Number.isNaN(age)) {
  console.log("Invalid number");
}
```

### Trim input

```js
const name = prompt("Enter your name:");

if (name !== null) {
  console.log(name.trim());
}
```

### Node.js

```js
import readline from "readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const name = await rl.question("Enter your name: ");

console.log(name);

rl.close();
```

### Node.js number

```js
const age = Number(
  await rl.question("Enter your age: ")
);
```

---

# 76. Practice Questions

## Beginner

### 1. Name Program

Ask the user for their name and print:

```text
Hello, Navaneeth!
```

---

### 2. Age Program

Ask for age and print:

```text
You are 20 years old.
```

---

### 3. Addition

Ask for two numbers and print their sum.

---

### 4. Rectangle

Ask for length and width and calculate area.

---

### 5. Circle

Ask for radius and calculate area.

---

# 77. Intermediate Practice

### 6. Average Marks

Ask for:

```text
Math
Physics
Chemistry
```

Calculate the average.

Formula:

```text
average = (math + physics + chemistry) / 3
```

---

### 7. Shopping Bill

Ask for:

```text
Product price
Quantity
```

Calculate the total.

---

### 8. Age Validator

Ask for age.

Accept only:

```text
0–120
```

---

### 9. Temperature Converter

Ask for Celsius and convert to Fahrenheit.

---

### 10. BMI Calculator

Ask for:

```text
Weight
Height
```

Calculate BMI.

---

# 78. Advanced Practice

### 11. Calculator

Ask for:

```text
Number 1
Operator
Number 2
```

Support:

```text
+
-
*
/
```

---

### 12. Student Profile

Ask for:

```text
Name
Age
College
Branch
Year
CGPA
```

Validate the numeric values and print a formatted profile.

---

### 13. Expense Calculator

Ask for:

```text
Food expense
Travel expense
Shopping expense
Other expense
```

Calculate:

```text
Total expense
```

---

### 14. Salary Calculator

Ask for:

```text
Basic salary
Bonus
Tax
```

Calculate:

```text
Final salary
```

---

# 79. Key Takeaways

Remember these five rules:

```text
1. User input usually starts as a string.

2. Use Number() when you need a number.

3. Validate user input before using it.

4. Browser prompt() can return null when cancelled.

5. Node.js commonly uses readline for terminal input.
```

The most important pattern is:

```js
const input = prompt("Enter something:");

if (input === null || input.trim() === "") {
  console.log("Invalid input.");
} else {
  console.log(input.trim());
}
```

For numbers:

```js
const input = prompt("Enter a number:");
const number = Number(input);

if (Number.isNaN(number)) {
  console.log("Invalid number.");
} else {
  console.log(`You entered: ${number}`);
}
```

---

# 80. What You Should Know Before Moving On

You should now be comfortable with:

* [ ] What user input means
* [ ] `prompt()`
* [ ] Browser input
* [ ] Node.js input
* [ ] `readline`
* [ ] `process.stdin`
* [ ] `process.stdout`
* [ ] `rl.question()`
* [ ] `await`
* [ ] String input
* [ ] `Number()`
* [ ] `parseInt()`
* [ ] `parseFloat()`
* [ ] `NaN`
* [ ] `Number.isNaN()`
* [ ] `null`
* [ ] Empty strings
* [ ] `trim()`
* [ ] Input validation
* [ ] Numeric validation
* [ ] Boolean input
* [ ] Template literals with input
* [ ] Input with conditions
* [ ] Input with loops
* [ ] Input with functions
* [ ] Building small interactive programs
* [ ] Browser vs Node.js input

---

# Next Topic

## 05 — Type Conversion

Next, you'll go deeper into converting values between:

```text
String
Number
Boolean
```

You'll learn:

```js
String()
Number()
Boolean()

parseInt()
parseFloat()

.toString()

Implicit conversion
Explicit conversion
Type coercion
Truthy and falsy values
NaN
null
undefined
```

These concepts are extremely important because JavaScript automatically converts values in many situations.
