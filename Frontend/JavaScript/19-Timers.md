# JavaScript Timers

## Introduction

JavaScript timers allow you to **schedule code to execute later**, either:

- **Once after a specified delay**
- **Repeatedly at fixed intervals**

Timers are extremely useful for creating interactive and dynamic web applications.

### Common Uses

- Countdown timers
- Digital clocks
- Slideshows
- Loading animations
- Auto-save functionality
- Notifications
- Polling APIs
- Games

---

# Timer Functions

JavaScript provides four built-in timer functions.

| Function | Description |
|----------|-------------|
| `setTimeout()` | Executes a function once after a specified delay. |
| `setInterval()` | Executes a function repeatedly after every specified interval. |
| `clearTimeout()` | Cancels a timeout created by `setTimeout()`. |
| `clearInterval()` | Stops an interval created by `setInterval()`. |

---

# The `setTimeout()` Function

## What is `setTimeout()`?

`setTimeout()` schedules a function to execute **once** after a specified amount of time.

### Syntax

```javascript
setTimeout(callbackFunction, delay);