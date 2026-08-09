# 07 — Counter Program

> A **Counter Program** is a simple JavaScript project where a number can be increased, decreased, or reset.

This project is important because it combines several JavaScript fundamentals into one small application.

---

# 1. What We Are Building

Our counter will have three buttons:

```text
        COUNTER

           0

    [ Decrease ]

    [  Reset   ]

    [ Increase ]
```

The user can:

* Increase the number
* Decrease the number
* Reset the number to `0`

---

# 2. Concepts Used

This project uses:

* Variables
* `let`
* `const`
* Numbers
* Arithmetic operators
* Functions
* DOM
* `getElementById()`
* `textContent`
* Event listeners
* `click` events
* `if` statements
* Increment operator
* Decrement operator

Later, you will build much more advanced versions using arrays, objects, modules, and local storage.

---

# 3. Basic Counter Logic

Before creating a webpage, understand the core logic.

```js
let count = 0;

count++;
console.log(count);

count++;
console.log(count);

count--;
console.log(count);
```

Output:

```text
1
2
1
```

The variable stores the current counter value.

---

# 4. The `++` Operator

The increment operator:

```js
++
```

increases a number by `1`.

Example:

```js
let count = 0;

count++;

console.log(count);
```

Output:

```text
1
```

This:

```js
count++;
```

is equivalent to:

```js
count = count + 1;
```

---

# 5. The `--` Operator

The decrement operator:

```js
--
```

decreases a number by `1`.

Example:

```js
let count = 5;

count--;

console.log(count);
```

Output:

```text
4
```

This:

```js
count--;
```

is equivalent to:

```js
count = count - 1;
```

---

# 6. Counter with Functions

We can create functions for each operation.

```js
let count = 0;

function increase() {
    count++;
}

function decrease() {
    count--;
}

function reset() {
    count = 0;
}
```

Now:

```js
increase();

console.log(count);
```

Output:

```text
1
```

---

# 7. Why Use Functions?

Instead of repeating:

```js
count++;
count++;
count++;
```

we can create:

```js
function increase() {
    count++;
}
```

Then call:

```js
increase();
```

Functions allow us to organize reusable logic.

---

# 8. Creating the HTML

Create a file:

```text
index.html
```

Basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Counter</title>
</head>

<body>

    <h1 id="countLabel">0</h1>

    <button id="decreaseBtn">Decrease</button>
    <button id="resetBtn">Reset</button>
    <button id="increaseBtn">Increase</button>

    <script src="index.js"></script>

</body>
</html>
```

---

# 9. Creating JavaScript

Create:

```text
index.js
```

Start with:

```js
let count = 0;
```

---

# 10. Selecting the HTML Elements

Use:

```js
document.getElementById()
```

Example:

```js
const countLabel = document.getElementById("countLabel");

const decreaseBtn = document.getElementById("decreaseBtn");

const resetBtn = document.getElementById("resetBtn");

const increaseBtn = document.getElementById("increaseBtn");
```

Now JavaScript can interact with those HTML elements.

---

# 11. Changing HTML Text

We can change the text using:

```js
textContent
```

Example:

```js
countLabel.textContent = 10;
```

The HTML:

```html
<h1 id="countLabel">0</h1>
```

will become:

```html
<h1 id="countLabel">10</h1>
```

---

# 12. Connecting the Increase Button

Use:

```js
increaseBtn.onclick = function() {
    count++;
    countLabel.textContent = count;
};
```

Now clicking the button increases the counter.

---

# 13. Connecting the Decrease Button

```js
decreaseBtn.onclick = function() {
    count--;
    countLabel.textContent = count;
};
```

---

# 14. Connecting the Reset Button

```js
resetBtn.onclick = function() {
    count = 0;
    countLabel.textContent = count;
};
```

---

# 15. Complete Basic Counter

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Counter</title>
</head>

<body>

    <h1 id="countLabel">0</h1>

    <button id="decreaseBtn">Decrease</button>
    <button id="resetBtn">Reset</button>
    <button id="increaseBtn">Increase</button>

    <script src="index.js"></script>

</body>
</html>
```

### `index.js`

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

const decreaseBtn = document.getElementById("decreaseBtn");

const resetBtn = document.getElementById("resetBtn");

const increaseBtn = document.getElementById("increaseBtn");

increaseBtn.onclick = function() {
    count++;
    countLabel.textContent = count;
};

decreaseBtn.onclick = function() {
    count--;
    countLabel.textContent = count;
};

resetBtn.onclick = function() {
    count = 0;
    countLabel.textContent = count;
};
```

---

# 16. How the Program Works

Initially:

```js
let count = 0;
```

The value is:

```text
0
```

When the user clicks Increase:

```js
count++;
```

The value becomes:

```text
1
```

Then:

```js
countLabel.textContent = count;
```

updates the webpage.

---

# 17. Program Flow

```text
User clicks Increase
        ↓
click event occurs
        ↓
count++
        ↓
count becomes larger
        ↓
textContent is updated
        ↓
new number appears
```

For decrease:

```text
User clicks Decrease
        ↓
click event occurs
        ↓
count--
        ↓
count becomes smaller
        ↓
textContent is updated
        ↓
new number appears
```

For reset:

```text
User clicks Reset
        ↓
count = 0
        ↓
textContent = 0
        ↓
counter resets
```

---

# 18. Using `addEventListener()`

A more modern and flexible approach is:

```js
increaseBtn.addEventListener("click", function() {
    count++;
    countLabel.textContent = count;
});
```

Instead of:

```js
increaseBtn.onclick = function() {
    count++;
};
```

---

# 19. Complete Version Using Event Listeners

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

const decreaseBtn = document.getElementById("decreaseBtn");

const resetBtn = document.getElementById("resetBtn");

const increaseBtn = document.getElementById("increaseBtn");

increaseBtn.addEventListener("click", function() {
    count++;
    countLabel.textContent = count;
});

decreaseBtn.addEventListener("click", function() {
    count--;
    countLabel.textContent = count;
});

resetBtn.addEventListener("click", function() {
    count = 0;
    countLabel.textContent = count;
});
```

---

# 20. Why `addEventListener()`?

`addEventListener()` allows you to attach event handlers without replacing an existing handler assigned through a property.

Example:

```js
button.addEventListener("click", function() {
    console.log("Button clicked");
});
```

You can also attach another listener:

```js
button.addEventListener("click", function() {
    console.log("Another action");
});
```

Both listeners can respond to the event.

---

# 21. Creating Separate Functions

We can make the program cleaner.

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

function updateDisplay() {
    countLabel.textContent = count;
}

function increase() {
    count++;
    updateDisplay();
}

function decrease() {
    count--;
    updateDisplay();
}

function reset() {
    count = 0;
    updateDisplay();
}
```

Then:

```js
increaseBtn.addEventListener("click", increase);

decreaseBtn.addEventListener("click", decrease);

resetBtn.addEventListener("click", reset);
```

---

# 22. Why Create `updateDisplay()`?

Without it:

```js
countLabel.textContent = count;
```

would be repeated.

With a function:

```js
function updateDisplay() {
    countLabel.textContent = count;
}
```

we can simply call:

```js
updateDisplay();
```

This reduces repetition.

---

# 23. Better Complete Version

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

const decreaseBtn = document.getElementById("decreaseBtn");

const resetBtn = document.getElementById("resetBtn");

const increaseBtn = document.getElementById("increaseBtn");

function updateDisplay() {
    countLabel.textContent = count;
}

function increase() {
    count++;
    updateDisplay();
}

function decrease() {
    count--;
    updateDisplay();
}

function reset() {
    count = 0;
    updateDisplay();
}

increaseBtn.addEventListener("click", increase);

decreaseBtn.addEventListener("click", decrease);

resetBtn.addEventListener("click", reset);
```

---

# 24. Adding a Minimum Value

Suppose we don't want the counter to go below `0`.

We can use an `if` statement.

```js
function decrease() {

    if (count > 0) {
        count--;
    }

    updateDisplay();
}
```

Now:

```text
0 → 0
```

instead of:

```text
0 → -1
```

---

# 25. Adding a Maximum Value

Suppose the maximum is:

```text
10
```

Use:

```js
function increase() {

    if (count < 10) {
        count++;
    }

    updateDisplay();
}
```

Now:

```text
10 → 10
```

instead of:

```text
10 → 11
```

---

# 26. Counter Between 0 and 10

Complete JavaScript:

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

const decreaseBtn = document.getElementById("decreaseBtn");

const resetBtn = document.getElementById("resetBtn");

const increaseBtn = document.getElementById("increaseBtn");

function updateDisplay() {
    countLabel.textContent = count;
}

function increase() {

    if (count < 10) {
        count++;
    }

    updateDisplay();
}

function decrease() {

    if (count > 0) {
        count--;
    }

    updateDisplay();
}

function reset() {
    count = 0;
    updateDisplay();
}

increaseBtn.addEventListener("click", increase);

decreaseBtn.addEventListener("click", decrease);

resetBtn.addEventListener("click", reset);
```

---

# 27. Adding a Step Value

Instead of increasing by `1`, we can increase by a custom amount.

```js
const step = 5;

function increase() {
    count += step;
    updateDisplay();
}
```

Now:

```text
0
5
10
15
20
```

---

# 28. Using `+=`

This:

```js
count += 5;
```

means:

```js
count = count + 5;
```

Similarly:

```js
count -= 5;
```

means:

```js
count = count - 5;
```

---

# 29. Counter with Step

```js
let count = 0;

const step = 5;

function increase() {
    count += step;
}

function decrease() {
    count -= step;
}
```

---

# 30. Counter with User-Selected Step

HTML:

```html
<input
    type="number"
    id="stepInput"
    value="1"
    min="1"
>

<button id="increaseBtn">Increase</button>
<button id="decreaseBtn">Decrease</button>
```

JavaScript:

```js
const stepInput = document.getElementById("stepInput");

function increase() {

    const step = Number(stepInput.value);

    count += step;

    updateDisplay();
}
```

Now the user controls how much the counter changes.

---

# 31. Why `Number()` Is Important Here

The value from:

```js
stepInput.value
```

is a string.

For example:

```text
"5"
```

Without conversion:

```js
count += stepInput.value;
```

could cause string concatenation.

With:

```js
const step = Number(stepInput.value);
```

we get:

```text
5
```

as a number.

---

# 32. Counter with Step Input

Complete JavaScript:

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

const stepInput = document.getElementById("stepInput");

const decreaseBtn = document.getElementById("decreaseBtn");

const resetBtn = document.getElementById("resetBtn");

const increaseBtn = document.getElementById("increaseBtn");

function updateDisplay() {
    countLabel.textContent = count;
}

function getStep() {
    const step = Number(stepInput.value);

    if (Number.isNaN(step)) {
        return 1;
    }

    return step;
}

function increase() {
    count += getStep();
    updateDisplay();
}

function decrease() {
    count -= getStep();
    updateDisplay();
}

function reset() {
    count = 0;
    updateDisplay();
}

increaseBtn.addEventListener("click", increase);

decreaseBtn.addEventListener("click", decrease);

resetBtn.addEventListener("click", reset);
```

---

# 33. Adding Keyboard Support

We can allow:

```text
ArrowUp    → Increase
ArrowDown  → Decrease
R          → Reset
```

Use:

```js
document.addEventListener("keydown", function(event) {

    if (event.key === "ArrowUp") {
        increase();
    }

    if (event.key === "ArrowDown") {
        decrease();
    }

    if (event.key.toLowerCase() === "r") {
        reset();
    }

});
```

---

# 34. Counter with Keyboard Controls

```js
document.addEventListener("keydown", function(event) {

    switch (event.key) {

        case "ArrowUp":
            increase();
            break;

        case "ArrowDown":
            decrease();
            break;

        case "r":
        case "R":
            reset();
            break;
    }

});
```

---

# 35. Adding Color Changes

We can change the number's appearance based on its value.

```js
function updateDisplay() {

    countLabel.textContent = count;

    if (count > 0) {
        countLabel.style.color = "green";
    }
    else if (count < 0) {
        countLabel.style.color = "red";
    }
    else {
        countLabel.style.color = "black";
    }
}
```

Logic:

```text
Positive → green
Negative → red
Zero     → black
```

---

# 36. Better Styling with `classList`

Instead of directly changing styles:

```js
countLabel.style.color = "red";
```

we can use CSS classes.

CSS:

```css
.positive {
    color: green;
}

.negative {
    color: red;
}

.zero {
    color: black;
}
```

JavaScript:

```js
function updateDisplay() {

    countLabel.textContent = count;

    countLabel.classList.remove(
        "positive",
        "negative",
        "zero"
    );

    if (count > 0) {
        countLabel.classList.add("positive");
    }
    else if (count < 0) {
        countLabel.classList.add("negative");
    }
    else {
        countLabel.classList.add("zero");
    }
}
```

This is a better approach when styling becomes more complex.

---

# 37. Full Counter Project

## HTML

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Counter Program</title>

    <link rel="stylesheet" href="style.css">

</head>

<body>

    <main class="counter">

        <h1>Counter</h1>

        <div id="countLabel">0</div>

        <div class="controls">

            <button id="decreaseBtn">
                −
            </button>

            <button id="resetBtn">
                Reset
            </button>

            <button id="increaseBtn">
                +
            </button>

        </div>

    </main>

    <script src="index.js"></script>

</body>

</html>
```

---

# 38. CSS

Create:

```text
style.css
```

```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 100px;
}

.counter {
    width: 400px;
    margin: auto;
}

#countLabel {
    font-size: 80px;
    margin: 30px;
}

button {
    padding: 10px 20px;
    margin: 5px;
    cursor: pointer;
}

.positive {
    color: green;
}

.negative {
    color: red;
}

.zero {
    color: black;
}
```

---

# 39. JavaScript

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

const decreaseBtn = document.getElementById("decreaseBtn");

const resetBtn = document.getElementById("resetBtn");

const increaseBtn = document.getElementById("increaseBtn");

function updateDisplay() {

    countLabel.textContent = count;

    countLabel.classList.remove(
        "positive",
        "negative",
        "zero"
    );

    if (count > 0) {
        countLabel.classList.add("positive");
    }
    else if (count < 0) {
        countLabel.classList.add("negative");
    }
    else {
        countLabel.classList.add("zero");
    }
}

function increase() {
    count++;
    updateDisplay();
}

function decrease() {
    count--;
    updateDisplay();
}

function reset() {
    count = 0;
    updateDisplay();
}

increaseBtn.addEventListener("click", increase);

decreaseBtn.addEventListener("click", decrease);

resetBtn.addEventListener("click", reset);

updateDisplay();
```

---

# 40. Folder Structure

Your project should look like:

```text
counter-project/
│
├── index.html
├── style.css
└── index.js
```

---

# 41. Execution Flow

When the page loads:

```text
index.html
     ↓
index.js loads
     ↓
count = 0
     ↓
HTML elements selected
     ↓
event listeners registered
     ↓
updateDisplay()
     ↓
counter displays 0
```

When Increase is clicked:

```text
Click
 ↓
increase()
 ↓
count++
 ↓
updateDisplay()
 ↓
DOM changes
```

When Decrease is clicked:

```text
Click
 ↓
decrease()
 ↓
count--
 ↓
updateDisplay()
 ↓
DOM changes
```

When Reset is clicked:

```text
Click
 ↓
reset()
 ↓
count = 0
 ↓
updateDisplay()
 ↓
DOM changes
```

---

# 42. Important Difference: Variable vs Display

There are two different things:

```text
JavaScript state
       ↓
    count = 5

HTML display
       ↓
    <h1>5</h1>
```

The variable:

```js
count
```

stores the actual value.

The DOM:

```js
countLabel.textContent
```

displays the value.

This distinction becomes extremely important when you later learn React.

---

# 43. State

The current value of the counter is called its **state**.

Example:

```js
let count = 5;
```

Current state:

```text
5
```

After:

```js
count++;
```

new state:

```text
6
```

Then we update the UI.

```text
State
 ↓
Update
 ↓
UI
```

This basic pattern appears throughout frontend development.

---

# 44. Counter Using a Single Function

You can also write:

```js
function changeCounter(amount) {

    count += amount;

    updateDisplay();
}
```

Then:

```js
increaseBtn.addEventListener("click", () => {
    changeCounter(1);
});

decreaseBtn.addEventListener("click", () => {
    changeCounter(-1);
});

resetBtn.addEventListener("click", () => {
    count = 0;
    updateDisplay();
});
```

This avoids having separate increase/decrease logic.

---

# 45. Cleaner Version

```js
let count = 0;

const countLabel = document.getElementById("countLabel");

function updateDisplay() {
    countLabel.textContent = count;
}

function changeCounter(amount) {
    count += amount;
    updateDisplay();
}

document
    .getElementById("increaseBtn")
    .addEventListener("click", () => {
        changeCounter(1);
    });

document
    .getElementById("decreaseBtn")
    .addEventListener("click", () => {
        changeCounter(-1);
    });

document
    .getElementById("resetBtn")
    .addEventListener("click", () => {
        count = 0;
        updateDisplay();
    });

updateDisplay();
```

---

# 46. Counter with Maximum and Minimum

```js
let count = 0;

const MIN = 0;
const MAX = 10;

function changeCounter(amount) {

    const newCount = count + amount;

    if (newCount >= MIN && newCount <= MAX) {
        count = newCount;
    }

    updateDisplay();
}
```

Notice:

```js
const MIN = 0;
const MAX = 10;
```

These values don't change, so `const` is appropriate.

---

# 47. Why `const` for DOM Elements?

We usually write:

```js
const countLabel = document.getElementById("countLabel");
```

because the variable itself doesn't need to point to another element.

We can still modify the element:

```js
countLabel.textContent = count;
```

This does **not** violate `const`.

`const` prevents reassignment of the variable:

```js
countLabel = anotherElement;
```

That would cause an error.

But changing properties of the referenced object is allowed.

---

# 48. Common Mistake

Incorrect:

```js
const count = 0;

count++;
```

This causes an error because `count` needs to change.

Correct:

```js
let count = 0;

count++;
```

Use:

```text
let → value changes
const → variable is not reassigned
```

---

# 49. Common Mistake — Forgetting to Update UI

You might write:

```js
function increase() {
    count++;
}
```

The JavaScript variable changes.

But the webpage doesn't automatically know about the change.

You need:

```js
countLabel.textContent = count;
```

or:

```js
updateDisplay();
```

---

# 50. Common Mistake — Wrong ID

HTML:

```html
<h1 id="countLabel">0</h1>
```

JavaScript:

```js
document.getElementById("counterLabel");
```

This returns:

```text
null
```

because the IDs don't match.

Correct:

```js
document.getElementById("countLabel");
```

---

# 51. Common Mistake — Script Loading Too Early

If JavaScript runs before the HTML elements exist, this can cause problems.

One solution is placing:

```html
<script src="index.js"></script>
```

at the end of the body:

```html
<body>

    <!-- HTML -->

    <script src="index.js"></script>

</body>
```

Another modern approach is:

```html
<script src="index.js" defer></script>
```

in the `<head>`.

---

# 52. Counter Using `defer`

```html
<head>

    <script
        src="index.js"
        defer
    ></script>

</head>
```

`defer` tells the browser to download the script while parsing HTML and execute it after the document has been parsed.

---

# 53. `onclick` vs `addEventListener`

### `onclick`

```js
button.onclick = function() {
    console.log("Clicked");
};
```

Simple and useful for beginners.

### `addEventListener`

```js
button.addEventListener("click", function() {
    console.log("Clicked");
});
```

More flexible and commonly used in larger applications.

For your JavaScript learning journey, become comfortable with `addEventListener()`.

---

# 54. Final Recommended Version

```js
let count = 0;

const countLabel = document.getElementById("countLabel");
const decreaseBtn = document.getElementById("decreaseBtn");
const resetBtn = document.getElementById("resetBtn");
const increaseBtn = document.getElementById("increaseBtn");

const MIN = 0;
const MAX = 10;

function updateDisplay() {

    countLabel.textContent = count;

    countLabel.classList.remove(
        "positive",
        "negative",
        "zero"
    );

    if (count > 0) {
        countLabel.classList.add("positive");
    }
    else if (count < 0) {
        countLabel.classList.add("negative");
    }
    else {
        countLabel.classList.add("zero");
    }
}

function changeCounter(amount) {

    const newCount = count + amount;

    if (newCount >= MIN && newCount <= MAX) {
        count = newCount;
    }

    updateDisplay();
}

increaseBtn.addEventListener("click", () => {
    changeCounter(1);
});

decreaseBtn.addEventListener("click", () => {
    changeCounter(-1);
});

resetBtn.addEventListener("click", () => {
    count = 0;
    updateDisplay();
});

updateDisplay();
```

---

# 55. What You Learned

This small project introduced an important frontend programming pattern:

```text
USER ACTION
    ↓
EVENT
    ↓
FUNCTION
    ↓
STATE CHANGE
    ↓
UI UPDATE
```

For example:

```text
Click Increase
      ↓
"click" event
      ↓
changeCounter(1)
      ↓
count changes
      ↓
updateDisplay()
      ↓
HTML changes
```

This pattern is fundamental to browser JavaScript and will become even more important when you learn React.

---

# 56. Practice Tasks

Build these versions yourself without copying the solution.

## Level 1 — Basic

Create:

```text
+
-
Reset
```

Counter should start at:

```text
0
```

---

## Level 2 — Minimum

Prevent the counter from going below:

```text
0
```

---

## Level 3 — Maximum

Prevent the counter from going above:

```text
100
```

---

## Level 4 — Step Counter

Add:

```html
<input type="number">
```

Allow the user to choose:

```text
1
5
10
50
```

as the increment/decrement amount.

---

## Level 5 — Keyboard

Implement:

```text
↑ → Increase
↓ → Decrease
R → Reset
```

---

## Level 6 — Color

Implement:

```text
Positive → Green
Negative → Red
Zero → Black
```

---

## Level 7 — Advanced Counter

Build a counter with:

```text
Current Value
Minimum Value
Maximum Value
Step Value

Increase
Decrease
Reset

Keyboard Controls
```

---

# 57. Interview Questions

### Q1. What is `++`?

The increment operator increases a numeric value by `1`.

```js
count++;
```

---

### Q2. What is `--`?

The decrement operator decreases a numeric value by `1`.

```js
count--;
```

---

### Q3. Why use `let` for the counter?

Because the counter value changes.

```js
let count = 0;
```

---

### Q4. Why use `const` for DOM references?

Because we don't normally reassign the variable to another element.

```js
const countLabel = document.getElementById("countLabel");
```

---

### Q5. What does `textContent` do?

It gets or sets the text content of an element.

```js
countLabel.textContent = count;
```

---

### Q6. What does `addEventListener()` do?

It registers a function to run when a particular event occurs.

```js
button.addEventListener("click", function() {
    console.log("Clicked");
});
```

---

### Q7. What is the DOM?

The **Document Object Model** is the browser's object representation of the HTML document.

JavaScript can use the DOM to:

* Find elements
* Change text
* Change styles
* Add/remove elements
* Respond to events

You will study the DOM in much greater detail later.

---

# 58. Key Takeaways

Remember these:

```text
let count = 0;
```

Stores the current counter state.

```js
count++;
```

Increases by `1`.

```js
count--;
```

Decreases by `1`.

```js
count += 5;
```

Increases by `5`.

```js
count -= 5;
```

Decreases by `5`.

```js
count = 0;
```

Resets the counter.

```js
element.textContent = count;
```

Updates the webpage.

```js
element.addEventListener("click", function() {});
```

Responds to button clicks.

---

# 59. Final Concept

The Counter Program looks simple, but it teaches an extremely important idea:

> **JavaScript stores state, responds to user events, changes that state, and updates the UI.**

The fundamental pattern is:

```text
        USER
         │
         ▼
      ACTION
         │
         ▼
       EVENT
         │
         ▼
     JAVASCRIPT
         │
         ▼
   STATE CHANGES
         │
         ▼
      DOM UPDATE
         │
         ▼
        UI
```

Once you understand this pattern, you're ready to build much larger interactive applications.
