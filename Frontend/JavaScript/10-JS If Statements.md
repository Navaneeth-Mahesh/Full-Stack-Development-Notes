# 10 — JavaScript If Statements

> **If statements** allow JavaScript to make decisions.

They let your program execute different code depending on whether a condition is `true` or `false`.

For example:

```js
const age = 18;

if (age >= 18) {
  console.log("You are an adult.");
}
```

Output:

```text
You are an adult.
```

The condition:

```js
age >= 18
```

is `true`, so JavaScript executes the code inside the `if` block.

---

# 1. What is an If Statement?

An `if` statement is a decision-making statement.

It basically says:

> "If this condition is true, execute this code."

Syntax:

```js
if (condition) {
  // code to execute
}
```

Example:

```js
const temperature = 30;

if (temperature > 25) {
  console.log("It's hot outside.");
}
```

Output:

```text
It's hot outside.
```

---

# 2. How If Statements Work

Consider:

```js
const age = 20;

if (age >= 18) {
  console.log("Adult");
}
```

JavaScript evaluates:

```js
age >= 18
```

which becomes:

```js
20 >= 18
```

which is:

```js
true
```

Therefore:

```js
console.log("Adult");
```

runs.

---

# 3. Basic Structure

```text
if
 │
 ├── condition
 │
 └── true?
       │
       ├── YES → execute block
       │
       └── NO  → skip block
```

Example:

```js
const age = 15;

if (age >= 18) {
  console.log("You can vote.");
}
```

Since:

```text
15 >= 18
```

is `false`, nothing is printed.

---

# 4. Condition Must Produce a Boolean

An `if` statement evaluates a value as either:

```text
true
```

or:

```text
false
```

Example:

```js
const isLoggedIn = true;

if (isLoggedIn) {
  console.log("Welcome!");
}
```

Output:

```text
Welcome!
```

---

# 5. Using Comparison Operators

You will frequently use comparison operators inside `if`.

```text
>     Greater than
<     Less than
>=    Greater than or equal
<=    Less than or equal
==    Loose equality
===   Strict equality
!=    Loose inequality
!==   Strict inequality
```

Example:

```js
const age = 20;

if (age >= 18) {
  console.log("Adult");
}
```

---

# 6. Greater Than

```js
const score = 80;

if (score > 50) {
  console.log("Score is greater than 50.");
}
```

Output:

```text
Score is greater than 50.
```

---

# 7. Less Than

```js
const age = 15;

if (age < 18) {
  console.log("You are under 18.");
}
```

Output:

```text
You are under 18.
```

---

# 8. Greater Than or Equal

```js
const age = 18;

if (age >= 18) {
  console.log("You are an adult.");
}
```

Output:

```text
You are an adult.
```

Notice:

```text
18 >= 18
```

is `true`.

---

# 9. Less Than or Equal

```js
const marks = 40;

if (marks <= 40) {
  console.log("Marks are 40 or below.");
}
```

Output:

```text
Marks are 40 or below.
```

---

# 10. Strict Equality

Use:

```js
===
```

to check whether both value and type are equal.

Example:

```js
const age = 18;

if (age === 18) {
  console.log("Age is exactly 18.");
}
```

Output:

```text
Age is exactly 18.
```

---

# 11. Why Strict Equality Is Better

Consider:

```js
const age = "18";

if (age == 18) {
  console.log("Match");
}
```

This is `true` because `==` performs type coercion.

But:

```js
if (age === 18) {
  console.log("Match");
}
```

is `false`.

Because:

```text
"18" → string
18   → number
```

Best practice:

> Prefer `===` and `!==` in modern JavaScript unless you intentionally need loose equality.

---

# 12. Not Equal

Use:

```js
!==
```

Example:

```js
const age = 20;

if (age !== 18) {
  console.log("Age is not 18.");
}
```

Output:

```text
Age is not 18.
```

---

# 13. Boolean Conditions

You can directly use a boolean.

```js
const isStudent = true;

if (isStudent) {
  console.log("You are a student.");
}
```

Output:

```text
You are a student.
```

---

# 14. False Boolean

```js
const isStudent = false;

if (isStudent) {
  console.log("You are a student.");
}
```

Nothing is printed.

Because:

```text
false
```

does not satisfy the `if` condition.

---

# 15. Using `!`

The `!` operator means:

> NOT

Example:

```js
const isLoggedIn = false;

if (!isLoggedIn) {
  console.log("Please log in.");
}
```

Output:

```text
Please log in.
```

Because:

```text
!false → true
```

---

# 16. If + User Input

You can combine `if` statements with user input.

```js
const age = Number(prompt("Enter your age:"));

if (age >= 18) {
  console.log("You are an adult.");
}
```

Remember:

```js
prompt()
```

returns a string, so we convert it using:

```js
Number()
```

---

# 17. Example — Voting Eligibility

```js
const age = Number(prompt("Enter your age:"));

if (age >= 18) {
  console.log("You are eligible to vote.");
}
```

If the user enters:

```text
20
```

Output:

```text
You are eligible to vote.
```

---

# 18. Example — Temperature

```js
const temperature = Number(prompt("Enter temperature:"));

if (temperature > 30) {
  console.log("It's hot.");
}
```

---

# 19. Example — Password

```js
const password = prompt("Enter password:");

if (password === "12345") {
  console.log("Access granted.");
}
```

Important:

> This is only a learning example. Real authentication should never store or compare passwords like this.

---

# 20. Example — Even Number

Use the remainder operator:

```js
%
```

Example:

```js
const number = 10;

if (number % 2 === 0) {
  console.log("Even number.");
}
```

Output:

```text
Even number.
```

Why?

```text
10 % 2 = 0
```

---

# 21. Example — Odd Number

```js
const number = 7;

if (number % 2 !== 0) {
  console.log("Odd number.");
}
```

Output:

```text
Odd number.
```

---

# 22. The `else` Statement

Sometimes you want code to execute when the condition is false.

Use:

```js
else
```

Syntax:

```js
if (condition) {
  // if true
} else {
  // if false
}
```

Example:

```js
const age = 15;

if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

Output:

```text
Minor
```

---

# 23. How `if...else` Works

```text
             Condition
                 │
          ┌──────┴──────┐
          │             │
        true          false
          │             │
          ▼             ▼
       IF block      ELSE block
```

Only one block executes.

---

# 24. Example — Pass or Fail

```js
const marks = 45;

if (marks >= 40) {
  console.log("Pass");
} else {
  console.log("Fail");
}
```

Output:

```text
Pass
```

---

# 25. Example — Positive or Negative

```js
const number = -10;

if (number >= 0) {
  console.log("Positive");
} else {
  console.log("Negative");
}
```

Output:

```text
Negative
```

Technically, `0` is neither positive nor negative, so a more accurate version is shown later.

---

# 26. Example — Adult or Minor

```js
const age = 16;

if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

---

# 27. Multiple Conditions with `else if`

Sometimes there are more than two possibilities.

Use:

```js
else if
```

Example:

```js
const marks = 75;

if (marks >= 90) {
  console.log("A+");
} else if (marks >= 80) {
  console.log("A");
} else if (marks >= 70) {
  console.log("B");
} else if (marks >= 60) {
  console.log("C");
} else {
  console.log("Fail");
}
```

Output:

```text
B
```

---

# 28. How `else if` Works

JavaScript checks conditions from top to bottom.

```text
if
 │
 ├── true → execute and stop
 │
 └── false
       │
       ▼
    else if
       │
       ├── true → execute and stop
       │
       └── false
             │
             ▼
          else
```

---

# 29. Important Rule: First Matching Condition Wins

Example:

```js
const age = 20;

if (age >= 18) {
  console.log("Adult");
} else if (age >= 21) {
  console.log("21+");
}
```

Output:

```text
Adult
```

Why?

Because:

```text
20 >= 18
```

is already true.

JavaScript doesn't continue checking later `else if` branches.

Therefore, order matters.

---

# 30. Correct Ordering

For ranges, put the most restrictive/highest threshold first when appropriate.

```js
const marks = 95;

if (marks >= 90) {
  console.log("A+");
} else if (marks >= 80) {
  console.log("A");
} else if (marks >= 70) {
  console.log("B");
} else {
  console.log("Fail");
}
```

Correct.

---

# 31. Incorrect Ordering

This is problematic:

```js
const marks = 95;

if (marks >= 50) {
  console.log("Pass");
} else if (marks >= 90) {
  console.log("A+");
}
```

Output:

```text
Pass
```

The `90+` condition never gets a chance.

---

# 32. Multiple Conditions with `&&`

Use:

```js
&&
```

when **all conditions must be true**.

Example:

```js
const age = 25;

if (age >= 18 && age <= 60) {
  console.log("Working-age range.");
}
```

Both conditions must be true.

---

# 33. Multiple Conditions with `||`

Use:

```js
||
```

when **at least one condition must be true**.

Example:

```js
const day = "Saturday";

if (day === "Saturday" || day === "Sunday") {
  console.log("Weekend");
}
```

Output:

```text
Weekend
```

---

# 34. Combining `&&` and `||`

Example:

```js
const age = 25;
const hasTicket = true;

if (age >= 18 && hasTicket) {
  console.log("Entry allowed.");
}
```

Both must be true.

---

# 35. Example — Discount Eligibility

```js
const age = 65;
const isMember = true;

if (age >= 60 || isMember) {
  console.log("Discount available.");
}
```

Either condition being true is enough.

---

# 36. Parentheses Matter

Consider:

```js
const age = 20;
const hasID = true;
const isMember = false;

if ((age >= 18 && hasID) || isMember) {
  console.log("Allowed");
}
```

Parentheses make the intended logic clear.

Best practice:

> Use parentheses when combining `&&` and `||` if it improves readability.

---

# 37. Nested If Statements

An `if` statement can contain another `if`.

Example:

```js
const age = 20;
const hasID = true;

if (age >= 18) {
  if (hasID) {
    console.log("Entry allowed.");
  }
}
```

Output:

```text
Entry allowed.
```

---

# 38. Nested If with Else

```js
const age = 20;
const hasID = false;

if (age >= 18) {
  if (hasID) {
    console.log("Entry allowed.");
  } else {
    console.log("ID required.");
  }
} else {
  console.log("You must be 18 or older.");
}
```

---

# 39. Nested If vs Logical Operators

Nested version:

```js
if (age >= 18) {
  if (hasID) {
    console.log("Allowed");
  }
}
```

Can often be simplified to:

```js
if (age >= 18 && hasID) {
  console.log("Allowed");
}
```

The second version is often easier to read.

---

# 40. If with Strings

```js
const username = "admin";

if (username === "admin") {
  console.log("Welcome, admin.");
}
```

---

# 41. Case Sensitivity

JavaScript strings are case-sensitive.

```js
const role = "Admin";

if (role === "admin") {
  console.log("Administrator");
}
```

Nothing happens.

Because:

```text
"Admin" !== "admin"
```

---

# 42. Converting Strings Before Comparison

You can normalize input:

```js
const role = prompt("Enter role:").toLowerCase();

if (role === "admin") {
  console.log("Administrator");
}
```

Now:

```text
ADMIN
Admin
AdMiN
```

all become:

```text
admin
```

---

# 43. If with Empty Strings

```js
const username = "";

if (username) {
  console.log("Username provided.");
}
```

Nothing is printed.

Why?

Because:

```text
"" → false
```

This uses JavaScript's truthy/falsy behavior.

---

# 44. Truthy Values

Examples:

```js
if ("hello") {
  console.log("Runs");
}

if (123) {
  console.log("Runs");
}

if ([]) {
  console.log("Runs");
}

if ({}) {
  console.log("Runs");
}
```

All execute because these values are truthy.

---

# 45. Falsy Values

These values are falsy:

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

Example:

```js
if (0) {
  console.log("This will not run.");
}
```

---

# 46. Important: Empty Arrays Are Truthy

This surprises beginners:

```js
if ([]) {
  console.log("This runs.");
}
```

Output:

```text
This runs.
```

Same with:

```js
if ({}) {
  console.log("This runs.");
}
```

Objects are truthy, even when empty.

---

# 47. Checking an Array Correctly

Don't do:

```js
if (items) {
  console.log("Items exist.");
}
```

because:

```js
const items = [];
```

is still truthy.

Instead:

```js
if (items.length > 0) {
  console.log("Items exist.");
}
```

---

# 48. Checking for Null

```js
const user = null;

if (user === null) {
  console.log("No user found.");
}
```

Output:

```text
No user found.
```

---

# 49. Checking for Undefined

```js
let username;

if (username === undefined) {
  console.log("Username is undefined.");
}
```

Output:

```text
Username is undefined.
```

You can also use:

```js
if (typeof username === "undefined") {
  console.log("Undefined");
}
```

The `typeof` pattern is particularly useful when the identifier itself may not have been declared.

---

# 50. Multiple `else if` Conditions

Example:

```js
const temperature = 25;

if (temperature >= 35) {
  console.log("Very hot");
} else if (temperature >= 30) {
  console.log("Hot");
} else if (temperature >= 20) {
  console.log("Comfortable");
} else if (temperature >= 10) {
  console.log("Cool");
} else {
  console.log("Cold");
}
```

Output:

```text
Comfortable
```

---

# 51. Range Checking

Suppose:

```js
const age = 25;
```

You can check a range:

```js
if (age >= 18 && age <= 60) {
  console.log("Age is between 18 and 60.");
}
```

JavaScript does **not** support mathematical chained comparisons like:

```js
18 <= age <= 60
```

Do not write that.

Use:

```js
age >= 18 && age <= 60
```

---

# 52. Grade Calculator

```js
const marks = Number(prompt("Enter marks:"));

if (marks >= 90) {
  console.log("Grade: A+");
} else if (marks >= 80) {
  console.log("Grade: A");
} else if (marks >= 70) {
  console.log("Grade: B");
} else if (marks >= 60) {
  console.log("Grade: C");
} else if (marks >= 40) {
  console.log("Grade: D");
} else {
  console.log("Grade: F");
}
```

---

# 53. Age Category Program

```js
const age = Number(prompt("Enter your age:"));

if (age < 0) {
  console.log("Invalid age.");
} else if (age < 13) {
  console.log("Child");
} else if (age < 18) {
  console.log("Teenager");
} else if (age < 60) {
  console.log("Adult");
} else {
  console.log("Senior");
}
```

Notice the order.

---

# 54. Positive, Negative, or Zero

A better version than a simple positive/negative check:

```js
const number = Number(prompt("Enter a number:"));

if (number > 0) {
  console.log("Positive");
} else if (number < 0) {
  console.log("Negative");
} else {
  console.log("Zero");
}
```

---

# 55. Even or Odd

```js
const number = Number(prompt("Enter a number:"));

if (number % 2 === 0) {
  console.log("Even");
} else {
  console.log("Odd");
}
```

---

# 56. Divisibility Check

Check whether a number is divisible by 5:

```js
const number = Number(prompt("Enter a number:"));

if (number % 5 === 0) {
  console.log("Divisible by 5.");
} else {
  console.log("Not divisible by 5.");
}
```

---

# 57. Login Example

```js
const username = prompt("Username:");
const password = prompt("Password:");

if (username === "admin" && password === "1234") {
  console.log("Login successful.");
} else {
  console.log("Invalid credentials.");
}
```

Again, this is only a learning example.

---

# 58. Driving Eligibility

```js
const age = Number(prompt("Enter your age:"));
const hasLicense = prompt("Do you have a license?");

if (age >= 18 && hasLicense === "yes") {
  console.log("You can drive.");
} else {
  console.log("You cannot drive.");
}
```

---

# 59. Discount Program

```js
const amount = Number(prompt("Enter purchase amount:"));

if (amount >= 5000) {
  console.log("20% discount");
} else if (amount >= 2000) {
  console.log("10% discount");
} else if (amount >= 1000) {
  console.log("5% discount");
} else {
  console.log("No discount");
}
```

---

# 60. Simple ATM Check

```js
const balance = 5000;
const withdrawal = Number(prompt("Enter withdrawal amount:"));

if (withdrawal <= 0) {
  console.log("Invalid amount.");
} else if (withdrawal > balance) {
  console.log("Insufficient balance.");
} else {
  console.log("Withdrawal successful.");
}
```

---

# 61. Weather Recommendation

```js
const temperature = Number(prompt("Enter temperature:"));

if (temperature >= 35) {
  console.log("Stay hydrated.");
} else if (temperature >= 25) {
  console.log("Weather is warm.");
} else if (temperature >= 15) {
  console.log("Weather is comfortable.");
} else {
  console.log("Wear warm clothes.");
}
```

---

# 62. Exam Eligibility

```js
const attendance = Number(prompt("Enter attendance percentage:"));
const hasMedicalReason = prompt("Medical reason?");

if (attendance >= 75 || hasMedicalReason === "yes") {
  console.log("Eligible for exam.");
} else {
  console.log("Not eligible for exam.");
}
```

---

# 63. Nested Login Example

```js
const username = prompt("Username:");
const password = prompt("Password:");

if (username === "admin") {
  if (password === "1234") {
    console.log("Login successful.");
  } else {
    console.log("Wrong password.");
  }
} else {
  console.log("Unknown username.");
}
```

---

# 64. Combining Conditions

```js
const age = 25;
const isStudent = true;
const hasID = true;

if (age >= 18 && hasID && isStudent) {
  console.log("Student entry allowed.");
}
```

All three conditions must be true.

---

# 65. OR Conditions

```js
const day = "Sunday";

if (day === "Saturday" || day === "Sunday") {
  console.log("It's the weekend.");
}
```

---

# 66. NOT Conditions

```js
const isLoggedIn = false;

if (!isLoggedIn) {
  console.log("Please log in.");
}
```

---

# 67. Combining NOT and AND

```js
const isLoggedIn = true;
const isBanned = false;

if (isLoggedIn && !isBanned) {
  console.log("Access granted.");
}
```

---

# 68. If Statement with Functions

```js
function checkAge(age) {
  if (age >= 18) {
    console.log("Adult");
  } else {
    console.log("Minor");
  }
}

checkAge(20);
```

Output:

```text
Adult
```

---

# 69. Returning from an If

Functions can use `return` inside conditions.

```js
function checkAge(age) {
  if (age >= 18) {
    return "Adult";
  }

  return "Minor";
}

console.log(checkAge(20));
```

Output:

```text
Adult
```

---

# 70. If with Arrays

```js
const fruits = ["Apple", "Banana", "Mango"];

if (fruits.length > 0) {
  console.log("The array has fruits.");
}
```

Output:

```text
The array has fruits.
```

---

# 71. If with Objects

```js
const user = {
  name: "Alex",
  age: 20
};

if (user.age >= 18) {
  console.log("User is an adult.");
}
```

---

# 72. Checking Object Properties

```js
const user = {
  name: "Alex"
};

if (user.name) {
  console.log("Name exists.");
}
```

For more precise checks, you can use:

```js
if ("name" in user) {
  console.log("Property exists.");
}
```

---

# 73. If with `NaN`

Remember:

```js
NaN
```

is falsy.

Example:

```js
const value = NaN;

if (value) {
  console.log("This won't run.");
}
```

For validation, use:

```js
if (Number.isNaN(value)) {
  console.log("Invalid number.");
}
```

---

# 74. If with `Infinity`

```js
const value = Infinity;

if (value) {
  console.log("Infinity is truthy.");
}
```

Output:

```text
Infinity is truthy.
```

But:

```js
Number.isFinite(value)
```

returns:

```text
false
```

---

# 75. Block Scope

Variables declared with `let` and `const` inside an `if` block are only available inside that block.

```js
if (true) {
  const message = "Hello";

  console.log(message);
}
```

This works.

But:

```js
if (true) {
  const message = "Hello";
}

console.log(message);
```

causes a `ReferenceError`.

---

# 76. `var` and If Blocks

`var` does not have block scope.

```js
if (true) {
  var message = "Hello";
}

console.log(message);
```

This can work because `var` is function-scoped rather than block-scoped.

Modern JavaScript generally prefers:

```js
let
const
```

over `var`.

---

# 77. Dangling Else

Consider:

```js
if (age >= 18)
  if (hasID)
    console.log("Allowed");
  else
    console.log("ID required");
```

The `else` belongs to the nearest unmatched `if`.

This can be confusing.

Best practice:

> Always use braces `{}`.

Write:

```js
if (age >= 18) {
  if (hasID) {
    console.log("Allowed");
  } else {
    console.log("ID required");
  }
}
```

---

# 78. Always Prefer Braces

Avoid:

```js
if (age >= 18)
  console.log("Adult");
```

Prefer:

```js
if (age >= 18) {
  console.log("Adult");
}
```

Why?

Because braces:

* Improve readability
* Reduce mistakes
* Make future changes safer
* Clearly show which statements belong to the condition

---

# 79. Common Mistake — Assignment Instead of Comparison

Wrong:

```js
if (age = 18) {
  console.log("Age is 18");
}
```

This assigns `18` to `age`.

Correct:

```js
if (age === 18) {
  console.log("Age is 18");
}
```

---

# 80. Common Mistake — Using `=` Instead of `===`

Remember:

```text
=    Assignment
==   Loose equality
===  Strict equality
```

Example:

```js
let age = 20;

age = 18;
```

means:

> Assign 18.

But:

```js
age === 18
```

means:

> Is age exactly 18?

---

# 81. Common Mistake — Incorrect Range

Wrong:

```js
if (18 <= age <= 60) {
  console.log("Valid age");
}
```

JavaScript does not interpret this like mathematical notation.

Correct:

```js
if (age >= 18 && age <= 60) {
  console.log("Valid age");
}
```

---

# 82. Common Mistake — Forgetting `===`

Avoid:

```js
if (age == 18) {
  console.log("18");
}
```

Prefer:

```js
if (age === 18) {
  console.log("18");
}
```

---

# 83. Common Mistake — Comparing Different Types

```js
const age = prompt("Enter age:");

if (age === 18) {
  console.log("Adult");
}
```

This won't work if the user enters `18`.

Why?

```text
prompt() → "18"
```

but:

```text
18 → number
```

Correct:

```js
const age = Number(prompt("Enter age:"));

if (age === 18) {
  console.log("Adult");
}
```

---

# 84. Common Mistake — Empty Array

Wrong assumption:

```js
const items = [];

if (items) {
  console.log("Items exist.");
}
```

This runs because an empty array is truthy.

Correct:

```js
if (items.length > 0) {
  console.log("Items exist.");
}
```

---

# 85. Common Mistake — `"false"`

This:

```js
if ("false") {
  console.log("Runs");
}
```

runs.

Because:

```text
"false"
```

is a non-empty string.

---

# 86. Practical Project — Number Checker

```js
const number = Number(prompt("Enter a number:"));

if (Number.isNaN(number)) {
  console.log("Invalid number.");
} else if (number > 0) {
  console.log("Positive number.");
} else if (number < 0) {
  console.log("Negative number.");
} else {
  console.log("Zero.");
}
```

---

# 87. Practical Project — Student Result

```js
const marks = Number(prompt("Enter your marks:"));

if (Number.isNaN(marks) || marks < 0 || marks > 100) {
  console.log("Invalid marks.");
} else if (marks >= 90) {
  console.log("Grade A+");
} else if (marks >= 80) {
  console.log("Grade A");
} else if (marks >= 70) {
  console.log("Grade B");
} else if (marks >= 60) {
  console.log("Grade C");
} else if (marks >= 40) {
  console.log("Grade D");
} else {
  console.log("Fail");
}
```

---

# 88. Practical Project — Electricity Bill Category

```js
const units = Number(prompt("Enter electricity units:"));

if (Number.isNaN(units) || units < 0) {
  console.log("Invalid units.");
} else if (units <= 100) {
  console.log("Low usage.");
} else if (units <= 300) {
  console.log("Medium usage.");
} else if (units <= 500) {
  console.log("High usage.");
} else {
  console.log("Very high usage.");
}
```

---

# 89. Practical Project — Login System

```js
const username = prompt("Enter username:");
const password = prompt("Enter password:");

if (username === "admin" && password === "1234") {
  console.log("Welcome!");
} else if (username !== "admin") {
  console.log("Username not found.");
} else {
  console.log("Incorrect password.");
}
```

---

# 90. Practical Project — Movie Ticket

```js
const age = Number(prompt("Enter your age:"));
const isWeekend = prompt("Is it weekend?").toLowerCase();

let price;

if (age < 5) {
  price = 0;
} else if (age < 18) {
  price = isWeekend === "yes" ? 150 : 120;
} else {
  price = isWeekend === "yes" ? 250 : 200;
}

console.log(`Ticket price: ₹${price}`);
```

This example also previews the **ternary operator**, which is covered later.

---

# 91. Practical Project — ATM

```js
let balance = 10000;

const amount = Number(prompt("Enter withdrawal amount:"));

if (Number.isNaN(amount)) {
  console.log("Enter a valid number.");
} else if (amount <= 0) {
  console.log("Amount must be greater than zero.");
} else if (amount > balance) {
  console.log("Insufficient balance.");
} else {
  balance -= amount;

  console.log("Withdrawal successful.");
  console.log(`Remaining balance: ₹${balance}`);
}
```

---

# 92. Practical Project — Leap Year

A year is a leap year when:

* It is divisible by 4
* Except years divisible by 100 are not leap years
* Unless they are also divisible by 400

Code:

```js
const year = Number(prompt("Enter year:"));

if (Number.isNaN(year)) {
  console.log("Invalid year.");
} else if (year % 400 === 0) {
  console.log("Leap year.");
} else if (year % 100 === 0) {
  console.log("Not a leap year.");
} else if (year % 4 === 0) {
  console.log("Leap year.");
} else {
  console.log("Not a leap year.");
}
```

---

# 93. Practical Project — Largest of Two Numbers

```js
const a = Number(prompt("Enter first number:"));
const b = Number(prompt("Enter second number:"));

if (a > b) {
  console.log(`${a} is larger.`);
} else if (b > a) {
  console.log(`${b} is larger.`);
} else {
  console.log("Both numbers are equal.");
}
```

---

# 94. Practical Project — Largest of Three Numbers

```js
const a = Number(prompt("Enter first number:"));
const b = Number(prompt("Enter second number:"));
const c = Number(prompt("Enter third number:"));

if (a >= b && a >= c) {
  console.log(`${a} is the largest.`);
} else if (b >= a && b >= c) {
  console.log(`${b} is the largest.`);
} else {
  console.log(`${c} is the largest.`);
}
```

---

# 95. If Statement Execution Flow

Example:

```js
const score = 75;

if (score >= 90) {
  console.log("A+");
} else if (score >= 80) {
  console.log("A");
} else if (score >= 70) {
  console.log("B");
} else {
  console.log("Fail");
}
```

Execution:

```text
score = 75

75 >= 90 → false
       ↓
75 >= 80 → false
       ↓
75 >= 70 → true
       ↓
Print "B"
       ↓
Stop checking this chain
```

---

# 96. If vs Else If vs Else

## `if`

Used when you want something to happen only when a condition is true.

```js
if (condition) {
  // code
}
```

## `else if`

Used to check another condition if the previous condition was false.

```js
if (condition1) {
  // code
} else if (condition2) {
  // code
}
```

## `else`

Used when none of the previous conditions are true.

```js
if (condition) {
  // code
} else {
  // code
}
```

---

# 97. Decision-Making Pattern

Most beginner programs follow this pattern:

```js
const value = /* input */;

if (condition1) {
  // case 1
} else if (condition2) {
  // case 2
} else if (condition3) {
  // case 3
} else {
  // default case
}
```

Learn this pattern well.

You will use it constantly.

---

# 98. Real-World Example

Imagine an e-commerce website.

```js
const cartTotal = 4500;

if (cartTotal >= 5000) {
  console.log("Free shipping + 20% discount");
} else if (cartTotal >= 3000) {
  console.log("Free shipping + 10% discount");
} else if (cartTotal >= 1000) {
  console.log("Free shipping");
} else {
  console.log("Shipping charges apply");
}
```

This is the same concept used in real applications.

---

# 99. Interview Questions

## Q1. What is an `if` statement?

An `if` statement executes code when a specified condition evaluates to `true`.

---

## Q2. What is the difference between `if` and `else`?

`if` executes when its condition is true.

`else` executes when the preceding `if` condition is false.

---

## Q3. What is `else if`?

`else if` allows you to test additional conditions when previous conditions were false.

---

## Q4. Can an `if` statement exist without `else`?

Yes.

```js
if (age >= 18) {
  console.log("Adult");
}
```

---

## Q5. Can you have multiple `else if` statements?

Yes.

```js
if (score >= 90) {
  // A+
} else if (score >= 80) {
  // A
} else if (score >= 70) {
  // B
}
```

---

## Q6. Can you have multiple `else` blocks?

No.

An `if...else if...else` chain can have only one final `else`.

---

## Q7. Can you nest if statements?

Yes.

```js
if (condition1) {
  if (condition2) {
    // code
  }
}
```

---

## Q8. What happens if no condition is true?

If there is an `else`, it executes.

If there isn't an `else`, JavaScript simply skips the entire chain.

---

# 100. Practice Questions

### Question 1

What is the output?

```js
const age = 20;

if (age >= 18) {
  console.log("Adult");
}
```

Answer:

```text
Adult
```

---

### Question 2

What is the output?

```js
const age = 15;

if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

Answer:

```text
Minor
```

---

### Question 3

What is the output?

```js
const score = 85;

if (score >= 90) {
  console.log("A+");
} else if (score >= 80) {
  console.log("A");
} else {
  console.log("B");
}
```

Answer:

```text
A
```

---

### Question 4

What is the output?

```js
const number = 10;

if (number % 2 === 0) {
  console.log("Even");
} else {
  console.log("Odd");
}
```

Answer:

```text
Even
```

---

### Question 5

What is the output?

```js
if ("hello") {
  console.log("Yes");
}
```

Answer:

```text
Yes
```

---

### Question 6

What is the output?

```js
if ("") {
  console.log("Yes");
} else {
  console.log("No");
}
```

Answer:

```text
No
```

---

### Question 7

What is the output?

```js
if ([]) {
  console.log("Yes");
}
```

Answer:

```text
Yes
```

---

### Question 8

What is the output?

```js
const age = "18";

if (age === 18) {
  console.log("Adult");
} else {
  console.log("Not matched");
}
```

Answer:

```text
Not matched
```

---

# 101. Coding Challenges

## Challenge 1 — Even/Odd

Ask the user for a number and print:

```text
Even
```

or:

```text
Odd
```

---

## Challenge 2 — Age Category

Ask for age and print:

```text
Child
Teenager
Adult
Senior
```

---

## Challenge 3 — Grade Calculator

Input marks and print:

```text
A+
A
B
C
D
F
```

---

## Challenge 4 — Login

Ask for:

```text
username
password
```

Check whether both are correct.

---

## Challenge 5 — Number Comparison

Ask for two numbers and print:

```text
First is larger
Second is larger
Both are equal
```

---

## Challenge 6 — Discount

Ask for purchase amount.

Apply:

```text
5000+ → 20%
3000+ → 10%
1000+ → 5%
Below 1000 → No discount
```

---

## Challenge 7 — Leap Year

Ask for a year and determine whether it is a leap year.

---

# 102. Mini Project — Number Guessing Logic

This previews the number guessing game you will build later.

```js
const secretNumber = 7;
const guess = Number(prompt("Guess the number:"));

if (guess === secretNumber) {
  console.log("Correct!");
} else if (guess > secretNumber) {
  console.log("Too high!");
} else {
  console.log("Too low!");
}
```

---

# 103. Mini Project — Temperature Advisor

```js
const temperature = Number(prompt("Enter temperature:"));

if (Number.isNaN(temperature)) {
  console.log("Invalid temperature.");
} else if (temperature >= 35) {
  console.log("Very hot. Stay hydrated.");
} else if (temperature >= 25) {
  console.log("Warm weather.");
} else if (temperature >= 15) {
  console.log("Comfortable weather.");
} else if (temperature >= 5) {
  console.log("Cold weather.");
} else {
  console.log("Very cold.");
}
```

---

# 104. Best Practices

### Use strict equality

Prefer:

```js
if (value === 10) {
}
```

instead of:

```js
if (value == 10) {
}
```

---

### Use braces

Prefer:

```js
if (condition) {
  console.log("Hello");
}
```

---

### Keep conditions readable

Instead of:

```js
if (age >= 18 && age <= 60 && hasID && !isBanned && isVerified) {
}
```

you may use meaningful variables:

```js
const validAge = age >= 18 && age <= 60;
const canEnter = validAge && hasID && !isBanned && isVerified;

if (canEnter) {
  console.log("Access granted.");
}
```

---

### Validate input

Don't assume user input is valid.

```js
const age = Number(prompt("Enter age:"));

if (Number.isNaN(age)) {
  console.log("Invalid input.");
}
```

---

### Order conditions carefully

For ranges:

```js
if (score >= 90) {
} else if (score >= 80) {
} else if (score >= 70) {
}
```

usually makes sense.

---

# 105. Quick Cheat Sheet

```js
// Basic
if (condition) {
}

// If / Else
if (condition) {
} else {
}

// If / Else If / Else
if (condition1) {
} else if (condition2) {
} else {
}

// AND
if (a && b) {
}

// OR
if (a || b) {
}

// NOT
if (!a) {
}

// Equality
if (a === b) {
}

// Inequality
if (a !== b) {
}

// Greater
if (a > b) {
}

// Less
if (a < b) {
}

// Greater or equal
if (a >= b) {
}

// Less or equal
if (a <= b) {
}
```

---

# 106. Mental Model

Think of an `if` statement as a gate:

```text
                CONDITION
                    │
              ┌─────┴─────┐
              │           │
            TRUE        FALSE
              │           │
              ▼           ▼
          IF BLOCK     ELSE BLOCK
              │           │
              └─────┬─────┘
                    ▼
               Continue
```

For an `else if` chain:

```text
Condition 1?
    │
    ├── YES → Run block → DONE
    │
    └── NO
         │
         ▼
    Condition 2?
         │
         ├── YES → Run block → DONE
         │
         └── NO
              │
              ▼
           Condition 3?
              │
              └── ...
                    │
                    ▼
                  ELSE
```

---

# 107. What You Should Be Able to Build Now

After learning `if` statements, you should be able to build:

* Age checker
* Even/odd checker
* Positive/negative checker
* Grade calculator
* Login checker
* Voting eligibility checker
* Discount calculator
* ATM validation
* Number comparison
* Temperature advisor
* Leap-year checker
* Exam eligibility checker
* Basic authentication logic
* Simple game decision logic

---

# 108. Final Checklist

Before moving to Topic 11, make sure you understand:

* [ ] What an `if` statement is
* [ ] Basic `if` syntax
* [ ] Conditions
* [ ] Boolean expressions
* [ ] Comparison operators
* [ ] `===`
* [ ] `!==`
* [ ] `>`
* [ ] `<`
* [ ] `>=`
* [ ] `<=`
* [ ] `else`
* [ ] `else if`
* [ ] Multiple conditions
* [ ] `&&`
* [ ] `||`
* [ ] `!`
* [ ] Nested `if`
* [ ] Truthy values
* [ ] Falsy values
* [ ] String conditions
* [ ] Number conditions
* [ ] User input
* [ ] Input validation
* [ ] Range checking
* [ ] Array conditions
* [ ] Object conditions
* [ ] `null`
* [ ] `undefined`
* [ ] `NaN`
* [ ] Block scope
* [ ] Common `=` vs `===` mistake
* [ ] Common range-checking mistake
* [ ] Writing real-world decision logic

---

# 109. One-Line Summary

> **An `if` statement allows JavaScript to make decisions by executing code only when a specified condition evaluates to true.**

---

# 110. Next Topic

## 11 — Checked Property

You will learn how to work with checkbox/radio-style properties in JavaScript, including:

* `checked`
* Reading checkbox state
* Changing checkbox state
* Checkbox events
* Multiple checkboxes
* Radio buttons
* Form validation
* Practical examples
* Mini projects
