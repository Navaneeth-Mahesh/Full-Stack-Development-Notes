# 09 — JavaScript Random Number Generator

> JavaScript provides the `Math.random()` method for generating pseudo-random numbers.

Random numbers are useful for:

* Games
* Dice rollers
* Random passwords
* OTP-style demos
* Random colors
* Random questions
* Simulations
* Choosing random items
* Number guessing games
* Shuffling data

---

# 1. What is `Math.random()`?

`Math.random()` returns a pseudo-random decimal number between:

```text
0 inclusive
1 exclusive
```

In mathematical notation:

```text
0 <= Math.random() < 1
```

Example:

```js
console.log(Math.random());
```

Possible output:

```text
0.3748291827
```

Another execution:

```text
0.9182736451
```

Another:

```text
0.0529182736
```

The exact value changes each time.

---

# 2. Important Rule

`Math.random()` never returns exactly `1`.

Possible values:

```text
0
0.1
0.25
0.5
0.999999...
```

But not:

```text
1
```

So remember:

```text
Math.random() >= 0
Math.random() < 1
```

---

# 3. Basic Syntax

```js
Math.random();
```

No arguments are required.

Example:

```js
const randomNumber = Math.random();

console.log(randomNumber);
```

---

# 4. Random Decimal Between 0 and 1

```js
const random = Math.random();

console.log(random);
```

Possible output:

```text
0.7281938472
```

This is a decimal number.

Check its type:

```js
console.log(typeof random);
```

Output:

```text
number
```

---

# 5. Random Integer Between 0 and 9

`Math.random()` gives a decimal.

To convert it into an integer, use:

```js
Math.floor()
```

Example:

```js
const randomNumber = Math.floor(Math.random() * 10);

console.log(randomNumber);
```

Possible outputs:

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

# 6. Why Multiply by 10?

Start with:

```js
Math.random();
```

Range:

```text
0 <= value < 1
```

Multiply by `10`:

```js
Math.random() * 10;
```

Range:

```text
0 <= value < 10
```

Possible values:

```text
0.12
1.93
4.56
7.21
9.98
```

Then:

```js
Math.floor()
```

removes the decimal part:

```text
0
1
4
7
9
```

Therefore:

```js
Math.floor(Math.random() * 10);
```

generates integers from:

```text
0 to 9
```

---

# 7. Random Integer Between 1 and 10

Use:

```js
const randomNumber = Math.floor(Math.random() * 10) + 1;

console.log(randomNumber);
```

Possible results:

```text
1
2
3
4
5
6
7
8
9
10
```

---

# 8. Why Add 1?

Consider:

```js
Math.floor(Math.random() * 10);
```

Range:

```text
0 → 9
```

Adding `1`:

```js
Math.floor(Math.random() * 10) + 1;
```

changes it to:

```text
1 → 10
```

So:

```text
0 + 1 = 1
1 + 1 = 2
...
9 + 1 = 10
```

---

# 9. Random Integer Between 1 and 6

This is useful for a dice.

```js
const dice = Math.floor(Math.random() * 6) + 1;

console.log(dice);
```

Possible output:

```text
1
```

or:

```text
2
```

or:

```text
3
```

or:

```text
4
```

or:

```text
5
```

or:

```text
6
```

---

# 10. Random Integer Between 1 and 100

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
98
99
100
```

---

# 11. General Formula

The most important formula is:

```js
Math.floor(Math.random() * (max - min + 1)) + min
```

This generates a random integer between:

```text
min and max
```

with both endpoints included.

Example:

```js
const randomNumber = Math.floor(Math.random() * (20 - 10 + 1)) + 10;

console.log(randomNumber);
```

Possible results:

```text
10
11
12
13
14
15
16
17
18
19
20
```

---

# 12. Understand the Formula

Suppose:

```text
min = 10
max = 20
```

Formula:

```js
Math.floor(Math.random() * (max - min + 1)) + min
```

Substitute:

```js
Math.floor(Math.random() * (20 - 10 + 1)) + 10
```

Simplify:

```js
Math.floor(Math.random() * 11) + 10
```

`Math.random() * 11` gives:

```text
0 <= value < 11
```

`Math.floor()` gives:

```text
0 → 10
```

Add `10`:

```text
10 → 20
```

---

# 13. Random Number Between 5 and 15

```js
const min = 5;
const max = 15;

const randomNumber =
  Math.floor(Math.random() * (max - min + 1)) + min;

console.log(randomNumber);
```

Possible output:

```text
5
8
11
15
```

---

# 14. Random Number Between 50 and 100

```js
const min = 50;
const max = 100;

const randomNumber =
  Math.floor(Math.random() * (max - min + 1)) + min;

console.log(randomNumber);
```

Possible output:

```text
73
98
51
100
```

---

# 15. Create a Reusable Random Function

Instead of repeatedly writing the formula, create a function:

```js
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
```

Use it:

```js
console.log(getRandomNumber(1, 10));
```

Another:

```js
console.log(getRandomNumber(50, 100));
```

Another:

```js
console.log(getRandomNumber(1000, 9999));
```

---

# 16. Reusable Function Explained

```js
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
```

### Step 1

```js
Math.random()
```

Generates:

```text
0 <= value < 1
```

### Step 2

```js
Math.random() * (max - min + 1)
```

Creates the required range size.

### Step 3

```js
Math.floor()
```

Converts the decimal into an integer.

### Step 4

```js
+ min
```

Moves the range to start at `min`.

---

# 17. Random Decimal Between 0 and 10

If you want a decimal instead of an integer:

```js
const randomNumber = Math.random() * 10;

console.log(randomNumber);
```

Possible:

```text
2.3847
7.9128
0.1283
9.9921
```

---

# 18. Random Decimal Between 10 and 20

Use:

```js
const min = 10;
const max = 20;

const randomNumber = Math.random() * (max - min) + min;

console.log(randomNumber);
```

Possible output:

```text
12.348
18.927
10.482
19.991
```

Notice that `20` is not included.

The range is:

```text
10 <= value < 20
```

---

# 19. Random Decimal Formula

For a decimal in the range:

```text
min <= value < max
```

use:

```js
Math.random() * (max - min) + min
```

Example:

```js
function getRandomDecimal(min, max) {
  return Math.random() * (max - min) + min;
}

console.log(getRandomDecimal(10, 20));
```

---

# 20. Random Decimal with 2 Decimal Places

Use:

```js
const randomNumber =
  Math.random() * (20 - 10) + 10;

console.log(randomNumber.toFixed(2));
```

Possible output:

```text
14.27
```

Important:

`toFixed()` returns a **string**.

Example:

```js
const value = (Math.random() * 10).toFixed(2);

console.log(typeof value);
```

Output:

```text
string
```

If you need a number:

```js
const value = Number((Math.random() * 10).toFixed(2));

console.log(typeof value);
```

Output:

```text
number
```

---

# 21. `Math.floor()`

`Math.floor()` rounds a number down.

Examples:

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

```js
console.log(Math.floor(4));
```

Output:

```text
4
```

This is why it is commonly used with `Math.random()`.

---

# 22. Why Not Just Use `Math.random() * 10`?

Because:

```js
Math.random() * 10
```

returns decimals.

Example:

```text
7.291837
```

If you need an integer:

```js
Math.floor(Math.random() * 10)
```

gives:

```text
7
```

---

# 23. `Math.round()` vs `Math.floor()`

You may be tempted to use:

```js
Math.round(Math.random() * 10)
```

But this does **not** produce an evenly distributed integer from 0 to 10.

For ordinary inclusive integer ranges, use:

```js
Math.floor(Math.random() * (max - min + 1)) + min
```

---

# 24. `Math.ceil()`

`Math.ceil()` rounds upward.

Example:

```js
console.log(Math.ceil(4.1));
```

Output:

```text
5
```

You can use it with random numbers, but `Math.floor()` is the standard approach for generating an inclusive integer range.

---

# 25. Random Even Number

Generate a random even number between 2 and 20:

```js
const randomEven =
  Math.floor(Math.random() * 10) * 2 + 2;

console.log(randomEven);
```

Possible results:

```text
2
4
6
8
10
12
14
16
18
20
```

A simpler approach is to generate an integer and transform it:

```js
const randomEven =
  (Math.floor(Math.random() * 10) + 1) * 2;

console.log(randomEven);
```

---

# 26. Random Odd Number

Generate a random odd number between 1 and 19:

```js
const randomOdd =
  Math.floor(Math.random() * 10) * 2 + 1;

console.log(randomOdd);
```

Possible results:

```text
1
3
5
7
9
11
13
15
17
19
```

---

# 27. Random Boolean

A simple way to randomly choose `true` or `false`:

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

The comparison produces a boolean.

---

# 28. Random Yes/No

```js
const answer = Math.random() < 0.5 ? "Yes" : "No";

console.log(answer);
```

Possible:

```text
Yes
```

or:

```text
No
```

This combines:

```text
Math.random()
Ternary operator
```

---

# 29. Random Coin Toss

```js
const coin = Math.random() < 0.5 ? "Heads" : "Tails";

console.log(coin);
```

Possible output:

```text
Heads
```

or:

```text
Tails
```

---

# 30. Coin Toss Function

```js
function flipCoin() {
  return Math.random() < 0.5 ? "Heads" : "Tails";
}

console.log(flipCoin());
```

Call it multiple times:

```js
console.log(flipCoin());
console.log(flipCoin());
console.log(flipCoin());
```

---

# 31. Random Dice Roll

```js
function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

console.log(rollDice());
```

Possible:

```text
1
2
3
4
5
6
```

---

# 32. Roll Two Dice

```js
const dice1 = Math.floor(Math.random() * 6) + 1;
const dice2 = Math.floor(Math.random() * 6) + 1;

const total = dice1 + dice2;

console.log(`Dice 1: ${dice1}`);
console.log(`Dice 2: ${dice2}`);
console.log(`Total: ${total}`);
```

Possible output:

```text
Dice 1: 4
Dice 2: 6
Total: 10
```

---

# 33. Random Array Index

Suppose:

```js
const fruits = [
  "Apple",
  "Banana",
  "Mango",
  "Orange"
];
```

Array indexes are:

```text
Apple  → 0
Banana → 1
Mango  → 2
Orange → 3
```

Generate a random index:

```js
const index = Math.floor(Math.random() * fruits.length);

console.log(index);
```

Then:

```js
console.log(fruits[index]);
```

---

# 34. Random Array Element

A very useful pattern:

```js
const fruits = [
  "Apple",
  "Banana",
  "Mango",
  "Orange"
];

const randomFruit =
  fruits[Math.floor(Math.random() * fruits.length)];

console.log(randomFruit);
```

Possible:

```text
Apple
```

or:

```text
Mango
```

or:

```text
Orange
```

---

# 35. Reusable Random Array Function

```js
function getRandomItem(array) {
  const index = Math.floor(Math.random() * array.length);

  return array[index];
}
```

Use:

```js
const colors = [
  "Red",
  "Blue",
  "Green",
  "Yellow"
];

console.log(getRandomItem(colors));
```

---

# 36. Random Name Generator

```js
const names = [
  "Alex",
  "John",
  "Sarah",
  "Emma",
  "David"
];

const randomName =
  names[Math.floor(Math.random() * names.length)];

console.log(`Selected name: ${randomName}`);
```

---

# 37. Random Question

```js
const questions = [
  "What is JavaScript?",
  "What is a variable?",
  "What is an array?",
  "What is a function?",
  "What is an object?"
];

const question =
  questions[Math.floor(Math.random() * questions.length)];

console.log(question);
```

This idea can be used to build a quiz application.

---

# 38. Random Color

```js
const colors = [
  "red",
  "blue",
  "green",
  "yellow",
  "purple"
];

const randomColor =
  colors[Math.floor(Math.random() * colors.length)];

console.log(randomColor);
```

---

# 39. Random RGB Color

RGB values range from:

```text
0 → 255
```

Generate one:

```js
const r = Math.floor(Math.random() * 256);
const g = Math.floor(Math.random() * 256);
const b = Math.floor(Math.random() * 256);

console.log(`rgb(${r}, ${g}, ${b})`);
```

Possible output:

```text
rgb(72, 193, 41)
```

---

# 40. Why 256?

RGB values include:

```text
0
1
2
...
254
255
```

That's:

```text
256 possible values
```

Therefore:

```js
Math.floor(Math.random() * 256)
```

produces:

```text
0 → 255
```

---

# 41. Random Hex Color

A hexadecimal color uses:

```text
0 1 2 3 4 5 6 7 8 9
A B C D E F
```

Example:

```text
#FF5733
```

Generate one:

```js
function getRandomHexColor() {
  const value = Math.floor(Math.random() * 0x1000000);

  return `#${value.toString(16).padStart(6, "0")}`;
}

console.log(getRandomHexColor());
```

Possible:

```text
#3fa8c1
```

---

# 42. Random Password Character

```js
const characters =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

const index =
  Math.floor(Math.random() * characters.length);

const character = characters[index];

console.log(character);
```

This selects one random character.

Important:

> `Math.random()` is not suitable for generating security-sensitive passwords, authentication tokens, reset tokens, or cryptographic secrets.

For security-sensitive randomness, use the Web Crypto API such as `crypto.getRandomValues()`.

---

# 43. Random Password Generator

For a simple learning/demo project:

```js
const characters =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

let password = "";

for (let i = 0; i < 8; i++) {
  const index =
    Math.floor(Math.random() * characters.length);

  password += characters[index];
}

console.log(password);
```

Example:

```text
a8Kx92Lm
```

Again, don't use this approach for real security credentials.

---

# 44. Random Letter

```js
const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const index =
  Math.floor(Math.random() * letters.length);

console.log(letters[index]);
```

---

# 45. Random Number Guessing

Generate a secret number:

```js
const secret =
  Math.floor(Math.random() * 100) + 1;

console.log(secret);
```

This produces:

```text
1 → 100
```

You can then compare a user's guess against it.

This is the foundation of a **Number Guessing Game**.

---

# 46. Random Number Generator Program

```js
const min = Number(prompt("Enter minimum:"));
const max = Number(prompt("Enter maximum:"));

const randomNumber =
  Math.floor(Math.random() * (max - min + 1)) + min;

console.log(`Random number: ${randomNumber}`);
```

Example:

```text
Minimum: 10
Maximum: 50

Random number: 37
```

---

# 47. Validate the Range

A better version:

```js
const min = Number(prompt("Enter minimum:"));
const max = Number(prompt("Enter maximum:"));

if (Number.isNaN(min) || Number.isNaN(max)) {
  console.log("Please enter valid numbers.");
} else if (min > max) {
  console.log("Minimum cannot be greater than maximum.");
} else {
  const randomNumber =
    Math.floor(Math.random() * (max - min + 1)) + min;

  console.log(`Random number: ${randomNumber}`);
}
```

---

# 48. Random Number Generator Function

```js
function getRandomNumber(min, max) {
  if (min > max) {
    throw new Error("min must be less than or equal to max");
  }

  return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(getRandomNumber(1, 10));
```

---

# 49. Negative Ranges

The formula also works with negative numbers.

Example:

```js
console.log(getRandomNumber(-10, -1));
```

Possible:

```text
-10
-7
-3
-1
```

Mixed range:

```js
console.log(getRandomNumber(-5, 5));
```

Possible:

```text
-5
-2
0
3
5
```

---

# 50. Random Number Between -1 and 1

```js
const random =
  Math.random() * 2 - 1;

console.log(random);
```

Range:

```text
-1 <= value < 1
```

---

# 51. Random Integer Between -10 and 10

```js
const random =
  Math.floor(Math.random() * 21) - 10;

console.log(random);
```

Possible:

```text
-10
-9
...
0
...
9
10
```

---

# 52. Random Percentage

Generate a random decimal percentage:

```js
const percentage = Math.random() * 100;

console.log(percentage);
```

Possible:

```text
47.28391
```

Generate an integer percentage:

```js
const percentage =
  Math.floor(Math.random() * 101);

console.log(percentage);
```

Possible:

```text
0 → 100
```

---

# 53. Random Date

You can generate a random timestamp between two dates.

```js
const start = new Date("2025-01-01").getTime();
const end = new Date("2025-12-31").getTime();

const randomTime =
  Math.random() * (end - start) + start;

const randomDate = new Date(randomTime);

console.log(randomDate);
```

This is useful for:

* Testing
* Demo data
* Simulations
* Mock data generation

---

# 54. Random Array Shuffle

A simple shuffle approach is:

```js
const numbers = [1, 2, 3, 4, 5];

numbers.sort(() => Math.random() - 0.5);

console.log(numbers);
```

However, this is **not a reliably uniform shuffle**.

For a proper unbiased shuffle, use the **Fisher-Yates algorithm**.

---

# 55. Fisher-Yates Shuffle

```js
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));

    [array[i], array[j]] = [array[j], array[i]];
  }

  return array;
}
```

Use:

```js
const numbers = [1, 2, 3, 4, 5];

console.log(shuffle(numbers));
```

Possible:

```text
[3, 1, 5, 2, 4]
```

---

# 56. Important: `Math.random()` Is Pseudo-Random

`Math.random()` does not provide true physical randomness.

It generates **pseudo-random** values using an algorithm.

For normal applications:

```js
Math.random()
```

is usually perfectly fine for things like:

* Games
* Random UI choices
* Simulations
* Practice projects
* Randomized animations

But it should not be used for security-sensitive randomness.

---

# 57. `Math.random()` and Security

Do NOT use:

```js
Math.random()
```

for:

* Password generation
* Authentication tokens
* Password reset tokens
* API secrets
* Session identifiers
* Cryptographic keys
* Security-sensitive OTP generation

For browser-based secure randomness, use:

```js
crypto.getRandomValues()
```

Example:

```js
const array = new Uint32Array(1);

crypto.getRandomValues(array);

console.log(array[0]);
```

The Web Crypto API is designed for security-sensitive random values.

---

# 58. `Math.random()` Distribution

A common misconception is:

> Every possible decimal number is equally likely.

That's not quite how to think about it because there are infinitely many possible real numbers between 0 and 1, while JavaScript actually produces values from a finite implementation-defined set.

The practical model is:

```text
Math.random()
```

produces pseudo-random values distributed approximately uniformly over its supported range.

For ordinary programming tasks, think:

```text
0 <= Math.random() < 1
```

---

# 59. Random Integer Formula Cheat Sheet

## 0 to 9

```js
Math.floor(Math.random() * 10);
```

## 1 to 10

```js
Math.floor(Math.random() * 10) + 1;
```

## 1 to 6

```js
Math.floor(Math.random() * 6) + 1;
```

## 1 to 100

```js
Math.floor(Math.random() * 100) + 1;
```

## min to max

```js
Math.floor(Math.random() * (max - min + 1)) + min;
```

---

# 60. Random Decimal Formula Cheat Sheet

## 0 to less than 1

```js
Math.random();
```

## 0 to less than 10

```js
Math.random() * 10;
```

## 10 to less than 20

```js
Math.random() * (20 - 10) + 10;
```

## min to less than max

```js
Math.random() * (max - min) + min;
```

---

# 61. Random Array Item Cheat Sheet

```js
array[Math.floor(Math.random() * array.length)]
```

Example:

```js
const colors = ["red", "blue", "green"];

const randomColor =
  colors[Math.floor(Math.random() * colors.length)];

console.log(randomColor);
```

---

# 62. Common Mistakes

## Mistake 1 — Forgetting `Math.floor()`

```js
const number = Math.random() * 10;
```

This produces decimals.

If you need an integer:

```js
const number = Math.floor(Math.random() * 10);
```

---

## Mistake 2 — Wrong range

Incorrect:

```js
Math.floor(Math.random() * 10);
```

if you need:

```text
1 → 10
```

This gives:

```text
0 → 9
```

Correct:

```js
Math.floor(Math.random() * 10) + 1;
```

---

## Mistake 3 — Using `Math.round()`

Avoid:

```js
Math.round(Math.random() * 10);
```

for generating a uniformly distributed integer in a range.

Prefer:

```js
Math.floor(Math.random() * 11);
```

for:

```text
0 → 10
```

---

## Mistake 4 — Forgetting `+ min`

Incorrect:

```js
Math.floor(Math.random() * (max - min + 1));
```

This generates:

```text
0 → max-min
```

Correct:

```js
Math.floor(Math.random() * (max - min + 1)) + min;
```

---

# 63. Common Interview Question

### How do you generate a random integer between 1 and 10?

Answer:

```js
Math.floor(Math.random() * 10) + 1;
```

---

# 64. Common Interview Question

### How do you generate a random integer between 1 and 100?

```js
Math.floor(Math.random() * 100) + 1;
```

---

# 65. Common Interview Question

### How do you generate a random integer between `min` and `max`?

```js
Math.floor(Math.random() * (max - min + 1)) + min;
```

---

# 66. Common Interview Question

### Why does `Math.random()` use `< 1`?

Because its standard range is:

```text
0 inclusive
1 exclusive
```

Therefore:

```js
Math.random() * 10
```

produces:

```text
0 <= value < 10
```

After `Math.floor()`:

```text
0 → 9
```

---

# 67. Common Interview Question

### How do you select a random array element?

```js
const randomItem =
  array[Math.floor(Math.random() * array.length)];
```

---

# 68. Mini Project — Dice Roller

```js
function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

const dice = rollDice();

console.log(`You rolled: ${dice}`);
```

---

# 69. Mini Project — Coin Toss

```js
function flipCoin() {
  return Math.random() < 0.5
    ? "Heads"
    : "Tails";
}

console.log(flipCoin());
```

---

# 70. Mini Project — Random Quote

```js
const quotes = [
  "Keep learning.",
  "Keep building.",
  "Practice makes progress.",
  "Never stop improving.",
  "Consistency beats motivation."
];

function getRandomQuote() {
  const index =
    Math.floor(Math.random() * quotes.length);

  return quotes[index];
}

console.log(getRandomQuote());
```

---

# 71. Mini Project — Random Username

```js
const adjectives = [
  "Cool",
  "Smart",
  "Fast",
  "Brave",
  "Silent"
];

const animals = [
  "Tiger",
  "Wolf",
  "Eagle",
  "Lion",
  "Fox"
];

function getRandomItem(array) {
  return array[Math.floor(Math.random() * array.length)];
}

const username =
  getRandomItem(adjectives) +
  getRandomItem(animals) +
  getRandomNumber(100, 999);

console.log(username);

function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
```

Possible output:

```text
SmartWolf427
```

---

# 72. Mini Project — Random Team Picker

```js
const students = [
  "Alex",
  "John",
  "Sarah",
  "Emma",
  "David",
  "Mike"
];

function pickStudent(students) {
  const index =
    Math.floor(Math.random() * students.length);

  return students[index];
}

console.log(`Selected student: ${pickStudent(students)}`);
```

---

# 73. Mini Project — Lucky Number

```js
function generateLuckyNumber() {
  return Math.floor(Math.random() * 100) + 1;
}

const luckyNumber = generateLuckyNumber();

console.log(`Your lucky number is ${luckyNumber}`);
```

---

# 74. Mini Project — Random Password Demo

For learning purposes only:

```js
const characters =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";

function generatePassword(length) {
  let password = "";

  for (let i = 0; i < length; i++) {
    const index =
      Math.floor(Math.random() * characters.length);

    password += characters[index];
  }

  return password;
}

console.log(generatePassword(12));
```

For real security-sensitive passwords, use a cryptographically secure random source instead.

---

# 75. Mini Project — Random Number Game

```js
const secret =
  Math.floor(Math.random() * 10) + 1;

const guess =
  Number(prompt("Guess a number from 1 to 10:"));

if (guess === secret) {
  console.log("Correct!");
} else {
  console.log(`Wrong! The number was ${secret}.`);
}
```

This combines:

```text
Variables
Math.random()
Math.floor()
Number()
prompt()
if
strict equality
```

---

# 76. Advanced Utility Functions

## Random Integer

```js
function randomInt(min, max) {
  if (!Number.isInteger(min) || !Number.isInteger(max)) {
    throw new TypeError("min and max must be integers");
  }

  if (min > max) {
    throw new RangeError("min must be <= max");
  }

  return Math.floor(Math.random() * (max - min + 1)) + min;
}
```

---

## Random Decimal

```js
function randomFloat(min, max) {
  if (min > max) {
    throw new RangeError("min must be <= max");
  }

  return Math.random() * (max - min) + min;
}
```

---

## Random Array Item

```js
function randomItem(array) {
  if (array.length === 0) {
    return undefined;
  }

  return array[Math.floor(Math.random() * array.length)];
}
```

---

# 77. Real-World Uses

Random number generation appears in many applications.

### Games

```text
Enemy spawn position
Damage values
Loot selection
Dice
Card selection
Critical hits
```

### Web applications

```text
Random testimonials
Random recommendations
Randomized UI
A/B experiments
Demo data
```

### Education

```text
Random quiz questions
Random math problems
Practice exercises
```

### Simulations

```text
Probability experiments
Traffic simulations
Financial models
Scientific experiments
```

---

# 78. Important Distinction

### Random integer

```js
Math.floor(Math.random() * 10);
```

Produces:

```text
0 → 9
```

### Random decimal

```js
Math.random() * 10;
```

Produces:

```text
0 <= value < 10
```

### Random array item

```js
array[Math.floor(Math.random() * array.length)];
```

### Random boolean

```js
Math.random() < 0.5;
```

---

# 79. Final Mental Model

```text
Math.random()
      │
      ▼
0 <= value < 1
      │
      ├── * 10
      │      │
      │      ▼
      │   0 <= value < 10
      │      │
      │      ▼
      │   Math.floor()
      │      │
      │      ▼
      │    0 → 9
      │
      └── * (max - min + 1)
             │
             ▼
        Math.floor()
             │
             ▼
           + min
             │
             ▼
        min → max
```

---

# 80. Final Cheat Sheet

```js
// Random decimal: 0 <= x < 1
Math.random();

// Random integer: 0 → 9
Math.floor(Math.random() * 10);

// Random integer: 1 → 10
Math.floor(Math.random() * 10) + 1;

// Random integer: 1 → 100
Math.floor(Math.random() * 100) + 1;

// Random integer: min → max
Math.floor(Math.random() * (max - min + 1)) + min;

// Random decimal: min <= x < max
Math.random() * (max - min) + min;

// Random boolean
Math.random() < 0.5;

// Random array element
array[Math.floor(Math.random() * array.length)];
```

---

# 81. Final Checklist

Before moving to Topic 10, make sure you understand:

* [ ] What `Math.random()` does
* [ ] `0 <= Math.random() < 1`
* [ ] Why `Math.random()` doesn't include `1`
* [ ] `Math.floor()`
* [ ] Random integer generation
* [ ] Random decimal generation
* [ ] Random integer between `1` and `10`
* [ ] Random integer between `min` and `max`
* [ ] Random negative numbers
* [ ] Random booleans
* [ ] Coin toss
* [ ] Dice roll
* [ ] Random array elements
* [ ] Random colors
* [ ] Random RGB colors
* [ ] Random hex colors
* [ ] Random dates
* [ ] Array shuffling
* [ ] Fisher-Yates shuffle
* [ ] Pseudo-random numbers
* [ ] Why `Math.random()` is not cryptographically secure
* [ ] `crypto.getRandomValues()`
* [ ] Building random-number utilities
* [ ] Building small random-number projects

---

# 82. One-Line Summary

> **`Math.random()` generates a pseudo-random number from 0 (inclusive) up to 1 (exclusive), and by combining it with `Math.floor()`, multiplication, and addition, you can generate random integers and decimals within useful ranges.**
