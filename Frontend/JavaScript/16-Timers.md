# Timers-Introduction.md

This file should cover the fundamentals.

## Topics

### 1. Introduction to Timers

* What are timers?
* Why do we need timers?
* Real-world examples
* How JavaScript executes timers

---

### 2. Synchronous vs Asynchronous

```js
console.log("Start");

setTimeout(() => {
    console.log("Middle");
}, 1000);

console.log("End");
```

Explain why output is

```
Start
End
Middle
```

---

### 3. JavaScript Runtime

Explain

* Call Stack
* Web APIs
* Callback Queue
* Event Loop

(simple beginner-friendly explanation)

---

### 4. setTimeout()

Cover everything

* Syntax
* Parameters
* Delay
* Anonymous functions
* Named functions
* Passing arguments
* Zero delay
* Multiple timeouts

Examples

```js
setTimeout(function () {
    console.log("Hello");
}, 2000);
```

Arrow function

```js
setTimeout(() => {
    console.log("Hello");
}, 2000);
```

Named function

```js
function greet() {
    console.log("Welcome");
}

setTimeout(greet, 3000);
```

Passing arguments

```js
function greet(name) {
    console.log(name);
}

setTimeout(greet, 2000, "Navaneeth");
```

---

### 5. clearTimeout()

Explain

* Why it exists
* How it works
* Real-world example

```js
const timer = setTimeout(() => {
    console.log("Executed");
}, 5000);

clearTimeout(timer);
```

---

### 6. Timer IDs

Explain

```js
const id = setTimeout(...);
```

What actually gets stored?

---

### 7. Nested setTimeout()

---

### 8. Common Beginner Mistakes

* Forgetting delay
* Calling function immediately

Wrong

```js
setTimeout(greet(),2000)
```

Correct

```js
setTimeout(greet,2000)
```

---

### 9. Practice Questions

---

### 10. Coding Exercises

* Greeting after 5 seconds
* Countdown using setTimeout
* Delayed calculator

---

### 11. Mini Project

**Countdown Timer**

---

# Advanced-Timers.md

This file covers everything advanced.

## Topics

### 1. setInterval()

Complete explanation

Syntax

```js
setInterval(callback, delay)
```

---

### 2. How setInterval Works

Execution flow

```
Start

↓

Wait

↓

Execute

↓

Wait

↓

Execute

↓

Repeat
```

---

### 3. clearInterval()

```js
const timer = setInterval(() => {
    console.log("Running");
},1000);

clearInterval(timer);
```

---

### 4. Digital Clock

```js
setInterval(()=>{
    console.log(new Date());
},1000);
```

---

### 5. Stopwatch

Explain

* seconds
* minutes
* start
* stop
* reset

---

### 6. Countdown Timer

Build complete countdown

```
10
9
8
7
...
0
```

---

### 7. Recursive setTimeout()

Explain why many developers prefer

```js
function repeat(){

    console.log("Running");

    setTimeout(repeat,1000);

}

repeat();
```

instead of

```js
setInterval()
```

---

### 8. setTimeout vs setInterval

Comparison table

| setTimeout        | setInterval     |
| ----------------- | --------------- |
| Runs once         | Runs repeatedly |
| One-time task     | Repeating task  |
| Easier to control | Can overlap     |

---

### 9. Timer Drift

Explain why

```
1000 ms

↓

Actually

1003 ms

1007 ms

998 ms
```

Timers are **not perfectly accurate**.

---

### 10. Event Loop with Timers

Explain

```
Call Stack

↓

Web APIs

↓

Callback Queue

↓

Event Loop

↓

Call Stack
```

This is the most important concept.

---

### 11. Real-world Uses

* OTP countdown
* Loading animation
* Auto logout
* Notifications
* Carousel
* Slideshow
* Live clocks
* Stopwatch
* Quiz timer
* Pomodoro timer
* Auto save
* Debounce/Throttle (mention only; cover later)

---

### 12. Common Mistakes

Infinite interval

```js
setInterval(()=>{
    console.log("Hello");
},1000);
```

Never stopping

---

Creating multiple intervals

```js
setInterval(...)
setInterval(...)
setInterval(...)
```

---

Not clearing timers

---

### 13. Best Practices

* Always clear intervals
* Store timer IDs
* Prefer recursive `setTimeout` for variable delays
* Avoid unnecessary timers
* Use `requestAnimationFrame` for animations (brief introduction)

---

### 14. Interview Questions

Examples:

* Difference between `setTimeout()` and `setInterval()`
* Why does `setTimeout(..., 0)` not execute immediately?
* Explain the Event Loop.
* Why are timers asynchronous?
* Why can timers be delayed?

---

### 15. Coding Exercises

* Build a stopwatch
* Build a digital clock
* OTP countdown
* Traffic signal simulator
* Pomodoro timer
* Quiz timer
* Auto slideshow

---

### 16. Mini Project

**Digital Productivity Timer**

Features:

* Start
* Pause
* Resume
* Reset
* Countdown
* Alarm when finished
* Progress display

---
