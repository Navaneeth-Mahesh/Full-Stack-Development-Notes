# Introduction to JavaScript

JavaScript is one of the most popular and important programming languages in the world. It is used to create interactive websites, web applications, mobile apps, desktop software, games, servers, and even AI-powered applications.

If HTML creates the structure of a webpage and CSS designs its appearance, JavaScript makes the webpage **interactive and dynamic**.

---

# What is JavaScript?

JavaScript (JS) is a **high-level, interpreted, lightweight, dynamically typed programming language** used to create interactive and dynamic applications.

Originally, JavaScript was created only for web browsers, but today it is used almost everywhere.

JavaScript can:

* Change webpage content
* Handle button clicks
* Validate forms
* Create animations
* Fetch data from servers
* Build full-stack applications
* Create mobile apps
* Build desktop software
* Develop games
* Create APIs
* Power AI applications

---

## Example

```html
<button onclick="sayHello()">Click Me</button>

<script>
function sayHello() {
    alert("Hello World!");
}
</script>
```

When the user clicks the button, JavaScript runs the function and displays a message.

Without JavaScript, the webpage would simply display a button that does nothing.

---

# Why JavaScript?

JavaScript is everywhere.

It is one of the few programming languages that can be used for:

* Frontend Development
* Backend Development
* Mobile App Development
* Desktop Applications
* Game Development
* Browser Extensions
* AI Integrations
* IoT Applications

Because of its versatility, JavaScript is considered one of the best languages to learn.

---

# History of JavaScript

Understanding JavaScript's history helps explain why it has become so popular.

## 1995 – Creation

JavaScript was created in **1995** by **Brendan Eich** while working at **Netscape Communications**.

Surprisingly, he created the first version of JavaScript in just **10 days**.

Originally, the language was designed to make websites interactive.

---

## Original Name

JavaScript was first called:

```
Mocha
```

Later renamed to:

```
LiveScript
```

Finally renamed:

```
JavaScript
```

The name "JavaScript" was chosen mainly for marketing because Java was very popular at that time.

**Important:**

JavaScript and Java are completely different programming languages.

---

## Browser Wars

During the late 1990s:

* Netscape used JavaScript.
* Microsoft created its own version called JScript.

Because every browser behaved differently, developers faced many compatibility problems.

---

## Standardization

To solve these issues, JavaScript was standardized by **ECMA International**.

The official standardized version became known as:

```
ECMAScript
```

Today, all modern browsers follow the ECMAScript standard.

---

# ECMAScript (ES Versions)

ECMAScript is the official specification that defines how JavaScript should work.

Think of it like this:

```
ECMAScript
        ↓
Rules and Standards
        ↓
JavaScript follows those rules
```

Every few years, new versions introduce new features.

---

## Major ECMAScript Versions

| Version      | Year      | Features                                                                                   |
| ------------ | --------- | ------------------------------------------------------------------------------------------ |
| ES1          | 1997      | First standard                                                                             |
| ES2          | 1998      | Minor improvements                                                                         |
| ES3          | 1999      | Regular expressions, try/catch, better strings                                             |
| ES4          | Cancelled | Never released                                                                             |
| ES5          | 2009      | Strict Mode, JSON support, Array methods                                                   |
| ES6 (ES2015) | 2015      | Biggest update: let, const, classes, arrow functions, template literals, promises, modules |
| ES2016       | 2016      | `includes()`, exponent operator (`**`)                                                     |
| ES2017       | 2017      | Async/Await                                                                                |
| ES2018       | 2018      | Object spread, Rest improvements                                                           |
| ES2019       | 2019      | `flat()`, `flatMap()`                                                                      |
| ES2020       | 2020      | Optional chaining, Nullish coalescing, BigInt                                              |
| ES2021       | 2021      | `replaceAll()`, logical assignment operators                                               |
| ES2022       | 2022      | Top-level `await`, class fields                                                            |
| ES2023       | 2023      | New array methods like `findLast()`                                                        |
| ES2024+      | Ongoing   | Regular improvements and new features                                                      |

---

## Most Important Version

ES6 (ECMAScript 2015) completely changed JavaScript development.

It introduced:

* `let`
* `const`
* Arrow Functions
* Classes
* Modules
* Template Literals
* Promises
* Destructuring
* Spread Operator
* Default Parameters

Most modern JavaScript is based on ES6 and newer versions.

---

# JavaScript Engine

A JavaScript engine is a program that reads, understands, and executes JavaScript code.

Without a JavaScript engine, browsers cannot run JavaScript.

---

## Popular JavaScript Engines

| Browser | Engine         |
| ------- | -------------- |
| Chrome  | V8             |
| Edge    | V8             |
| Firefox | SpiderMonkey   |
| Safari  | JavaScriptCore |
| Opera   | V8             |

---

## What Does a JavaScript Engine Do?

When you write:

```javascript
let x = 5 + 10;
console.log(x);
```

The engine performs the following steps:

1. Reads the code.
2. Parses the code.
3. Converts it into machine-understandable instructions.
4. Optimizes the code for better performance.
5. Executes the code.
6. Produces the output.

---

## Simple Flow

```
JavaScript Code
       ↓
JavaScript Engine
       ↓
Parse
       ↓
Compile / Optimize
       ↓
Execute
       ↓
Output
```

---

# How JavaScript Works

When JavaScript code runs, several components work together.

```
Your JavaScript Code
        ↓
JavaScript Engine
        ↓
Memory Allocation
        ↓
Call Stack
        ↓
Execution
        ↓
Output
```

---

## Memory

Variables are stored in memory.

Example:

```javascript
let name = "Navaneeth";
let age = 19;
```

Memory stores:

```
name → "Navaneeth"

age → 19
```

---

## Call Stack

The Call Stack keeps track of function execution.

Example:

```javascript
function first() {
    second();
}

function second() {
    console.log("Hello");
}

first();
```

Execution:

```
Stack

first()
↓

second()
↓

console.log()

↓

Finished
```

The stack follows **LIFO (Last In, First Out)**.

---

## Single Threaded

JavaScript executes one task at a time.

```
Task 1
↓

Task 2
↓

Task 3
```

Only one task runs at a given moment.

---

## Asynchronous Operations

Some tasks take time:

* API requests
* Timers
* File reading
* Database queries

Instead of blocking the program, JavaScript delegates these tasks to the runtime environment and continues executing other code. When the task is complete, the callback or promise is queued and executed when the call stack is free.

Example:

```javascript
console.log("Start");

setTimeout(() => {
    console.log("Inside Timer");
}, 2000);

console.log("End");
```

Output:

```
Start
End
Inside Timer
```

---

# Client-side vs Server-side JavaScript

JavaScript can run in two different environments.

---

## Client-side JavaScript

Client-side JavaScript runs inside the user's web browser.

Examples:

* Button clicks
* Form validation
* Image sliders
* Animations
* Dynamic UI updates
* DOM manipulation

### Flow

```
User

↓

Browser

↓

JavaScript

↓

Update Webpage
```

Example:

```javascript
document.body.style.backgroundColor = "blue";
```

The browser immediately changes the page's background color.

---

## Server-side JavaScript

Server-side JavaScript runs on a server, most commonly using Node.js.

It is used for:

* Authentication
* Database operations
* REST APIs
* File handling
* Sending emails
* Business logic
* Payment processing

### Flow

```
Browser

↓

Request

↓

Server (Node.js)

↓

Database

↓

Response

↓

Browser
```

Example:

```javascript
app.get("/", (req, res) => {
    res.send("Hello from Server");
});
```

---

## Comparison

| Client-side            | Server-side                 |
| ---------------------- | --------------------------- |
| Runs in Browser        | Runs on Server              |
| Accesses DOM           | Cannot access DOM           |
| Handles UI             | Handles business logic      |
| Faster UI interactions | Processes requests and data |
| Uses Browser APIs      | Uses Node.js APIs           |

---

# JavaScript Runtime

A JavaScript engine alone cannot perform tasks such as reading files, making network requests, or setting timers. Those capabilities are provided by the **runtime environment**.

A JavaScript runtime combines the JavaScript engine with additional APIs and features.

Different runtimes provide different APIs.

### Browser Runtime

The browser runtime includes:

* JavaScript Engine
* DOM API
* BOM API
* Web APIs
* Event Loop
* Callback Queue

```
Browser

↓

JavaScript Engine

↓

Web APIs

↓

Event Loop

↓

Callback Queue
```

### Browser APIs

Examples include:

* `document`
* `window`
* `fetch()`
* `setTimeout()`
* `setInterval()`
* `localStorage`

---

### Node.js Runtime

Node.js provides APIs that are useful on servers.

Examples include:

* File System (`fs`)
* HTTP Server
* Path utilities
* Operating System information
* Streams
* Buffers

```
Node.js

↓

V8 Engine

↓

Node APIs

↓

File System

↓

Network

↓

Database
```

---

# JavaScript Use Cases

JavaScript is used across many areas of software development.

---

## 1. Interactive Websites

Examples:

* Navigation menus
* Sliders
* Forms
* Popups
* Animations

---

## 2. Frontend Development

Popular libraries and frameworks:

* React
* Vue
* Angular
* Svelte

These are used to build modern web applications.

---

## 3. Backend Development

Using Node.js, JavaScript can build:

* REST APIs
* Authentication systems
* Real-time applications
* Microservices
* Server-side rendering

Popular backend frameworks:

* Express.js
* Fastify
* NestJS
* Hono

---

## 4. Full-Stack Development

JavaScript can be used for both the frontend and backend, allowing developers to use a single language throughout an application.

Common stack:

```
Frontend
React

↓

Backend
Node.js + Express

↓

Database
MongoDB / PostgreSQL / MySQL
```

---

## 5. Mobile App Development

JavaScript can build cross-platform mobile apps using:

* React Native
* Expo
* Ionic

---

## 6. Desktop Applications

JavaScript can also create desktop software using:

* Electron
* Tauri

Examples of applications built with these technologies include code editors, chat applications, and productivity tools.

---

## 7. Game Development

JavaScript is used to build:

* 2D Games
* Browser Games
* Multiplayer Games

Popular libraries:

* Phaser
* PixiJS
* Three.js (for 3D graphics)

---

## 8. Browser Extensions

JavaScript powers browser extensions that can:

* Block ads
* Manage passwords
* Take notes
* Improve productivity

---

## 9. Real-Time Applications

Examples include:

* Chat applications
* Video conferencing
* Live notifications
* Collaborative editors

Technologies often used:

* WebSockets
* Socket.IO

---

## 10. AI and Machine Learning

JavaScript is increasingly used with AI services by:

* Calling AI APIs
* Building AI-powered web applications
* Running machine learning models in the browser with libraries such as TensorFlow.js

---

# Summary

JavaScript has evolved from a simple browser scripting language into one of the most versatile programming languages in the software industry.

By learning JavaScript, you can build:

* Interactive websites
* Modern frontend applications
* Backend servers and APIs
* Full-stack applications
* Mobile apps
* Desktop software
* Games
* Browser extensions
* Real-time applications
* AI-powered applications

JavaScript remains one of the most in-demand programming languages, making it an essential skill for aspiring web and full-stack developers.
