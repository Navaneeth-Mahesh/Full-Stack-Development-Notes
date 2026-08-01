# Lesson 9 — CURRENT_DATE() & CURRENT_TIME()

## Learning Objectives

By the end of this lesson, you will understand:

- What Date and Time functions are
- Difference between CURRENT_DATE(), CURRENT_TIME(), NOW()
- CURDATE() and CURTIME()
- How MySQL stores date and time
- Formatting dates
- Practical examples
- Real-world applications
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Introduction

Almost every real-world application works with **dates and time**.

Examples:

- Instagram → Post creation time
- Amazon → Order date
- WhatsApp → Message timestamp
- Banking → Transaction time
- Attendance System → Login time
- Hospital → Appointment date

Instead of entering these values manually, MySQL provides built-in functions that automatically return the current date and time.

---

# Date and Time Data Types

Before learning the functions, let's understand how MySQL stores date and time.

| Data Type | Stores | Example |
|-----------|---------|----------|
| DATE | Date only | 2026-08-01 |
| TIME | Time only | 15:45:30 |
| DATETIME | Date + Time | 2026-08-01 15:45:30 |
| TIMESTAMP | Date + Time (auto update supported) | 2026-08-01 15:45:30 |

---

# CURRENT_DATE()

Returns today's date.

## Syntax

```sql
SELECT CURRENT_DATE();
```

Output

```
2026-08-01
```

Format

```
YYYY-MM-DD
```

---

## Example

```sql
SELECT CURRENT_DATE();
```

Result

```
+----------------+
| CURRENT_DATE() |
+----------------+
| 2026-08-01     |
+----------------+
```

---

# CURRENT_TIME()

Returns the current system time.

## Syntax

```sql
SELECT CURRENT_TIME();
```

Example Output

```
15:40:21
```

Format

```
HH:MM:SS
```

---

# NOW()

Returns both date and time.

## Syntax

```sql
SELECT NOW();
```

Example Output

```
2026-08-01 15:40:21
```

This is one of the most commonly used date functions.

---

# CURDATE()

CURDATE() is another function that returns today's date.

```sql
SELECT CURDATE();
```

Output

```
2026-08-01
```

---

# CURTIME()

Returns the current time.

```sql
SELECT CURTIME();
```

Output

```
15:40:21
```

---

# Difference Between Functions

| Function | Returns |
|----------|----------|
| CURRENT_DATE() | Current Date |
| CURRENT_TIME() | Current Time |
| NOW() | Current Date + Time |
| CURDATE() | Current Date |
| CURTIME() | Current Time |

---

# CURRENT_DATE() vs CURDATE()

Both produce the same result.

```sql
SELECT CURRENT_DATE();

SELECT CURDATE();
```

Output

```
2026-08-01
```

Difference:

None.

They are aliases of each other.

---

# CURRENT_TIME() vs CURTIME()

Both return the same time.

```sql
SELECT CURRENT_TIME();

SELECT CURTIME();
```

Output

```
15:40:21
```

Again, no practical difference.

---

# NOW() vs CURRENT_DATE()

```sql
SELECT NOW();
```

Output

```
2026-08-01 15:40:21
```

Whereas

```sql
SELECT CURRENT_DATE();
```

Output

```
2026-08-01
```

NOW() includes both date and time.

---

# Creating a Table

```sql
CREATE TABLE employees (

id INT PRIMARY KEY,

name VARCHAR(50),

joining_date DATE

);
```

Insert today's date automatically

```sql
INSERT INTO employees
VALUES

(1,'Navaneeth',CURRENT_DATE());
```

Output

| id | name | joining_date |
|----|------|--------------|
|1|Navaneeth|2026-08-01|

---

# Using NOW()

Create another table.

```sql
CREATE TABLE login_history (

id INT,

login_time DATETIME

);
```

Insert

```sql
INSERT INTO login_history

VALUES

(1,NOW());
```

Table

| id | login_time |
|----|----------------------|
|1|2026-08-01 15:40:21|

---

# Attendance Example

```sql
CREATE TABLE attendance (

student_id INT,

attendance_date DATE

);
```

Insert today's attendance.

```sql
INSERT INTO attendance

VALUES

(101,CURRENT_DATE());
```

---

# Banking Example

```sql
CREATE TABLE transactions (

id INT,

amount DECIMAL(10,2),

transaction_time DATETIME

);
```

Insert

```sql
INSERT INTO transactions

VALUES

(1,2500,NOW());
```

Output

```
2026-08-01 15:40:21
```

---

# Formatting Dates

Suppose NOW() returns

```
2026-08-01 18:35:10
```

We can format it using DATE_FORMAT().

Syntax

```sql
SELECT DATE_FORMAT(NOW(),'%d-%m-%Y');
```

Output

```
01-08-2026
```

---

# Common Format Specifiers

| Specifier | Meaning |
|-----------|----------|
| %d | Day |
| %m | Month |
| %Y | Four-digit Year |
| %y | Two-digit Year |
| %H | Hour (24-hour) |
| %h | Hour (12-hour) |
| %i | Minutes |
| %s | Seconds |
| %M | Month Name |
| %W | Weekday Name |

---

# Examples

Date

```sql
SELECT DATE_FORMAT(NOW(),'%d/%m/%Y');
```

Output

```
01/08/2026
```

---

Month Name

```sql
SELECT DATE_FORMAT(NOW(),'%M');
```

Output

```
August
```

---

Day Name

```sql
SELECT DATE_FORMAT(NOW(),'%W');
```

Output

```
Saturday
```

---

Time

```sql
SELECT DATE_FORMAT(NOW(),'%H:%i:%s');
```

Output

```
18:35:10
```

---

# Multiple Functions Together

```sql
SELECT

CURRENT_DATE(),

CURRENT_TIME(),

NOW();
```

Output

```
2026-08-01

18:35:10

2026-08-01 18:35:10
```

---

# Real-World Use Cases

## E-Commerce

Store order date.

```sql
INSERT INTO orders

VALUES

(1,CURRENT_DATE());
```

---

## Social Media

Store post time.

```sql
INSERT INTO posts

VALUES

(1,NOW());
```

---

## Banking

Save transaction timestamp.

```sql
INSERT INTO transactions

VALUES

(10,NOW());
```

---

## Attendance

Automatically save today's attendance.

```sql
CURRENT_DATE()
```

---

## Login History

Store login timestamp.

```sql
NOW()
```

---

# Common Mistakes

## Mistake 1

Using quotes.

Wrong

```sql
SELECT "CURRENT_DATE()";
```

Output

```
CURRENT_DATE()
```

Correct

```sql
SELECT CURRENT_DATE();
```

---

## Mistake 2

Saving NOW() inside DATE column.

DATE column stores only the date.

Time is ignored.

---

## Mistake 3

Saving CURRENT_DATE() inside TIME column.

Result

```
Incorrect value
```

Use CURRENT_TIME() instead.

---

# Best Practices

- Use CURRENT_DATE() for dates only.
- Use CURRENT_TIME() for time only.
- Use NOW() when both are needed.
- Use DATE_FORMAT() to display dates in a user-friendly format.
- Store timestamps automatically instead of entering them manually.

---

# Interview Questions

## 1. Difference between NOW() and CURRENT_DATE()?

NOW() returns both date and time.

CURRENT_DATE() returns only the date.

---

## 2. Difference between CURRENT_TIME() and CURTIME()?

No difference.

Both return the current time.

---

## 3. Which function returns current date and time?

```sql
NOW();
```

---

## 4. Which function returns only today's date?

```sql
CURRENT_DATE();
```

or

```sql
CURDATE();
```

---

## 5. Which function formats dates?

```sql
DATE_FORMAT()
```

---

# Practice Exercises

## Exercise 1

Display today's date.

```sql
SELECT CURRENT_DATE();
```

---

## Exercise 2

Display current time.

```sql
SELECT CURRENT_TIME();
```

---

## Exercise 3

Display current date and time.

```sql
SELECT NOW();
```

---

## Exercise 4

Format today's date as

```
01/08/2026
```

Hint

```sql
DATE_FORMAT()
```

---

## Exercise 5

Create an employee table.

Insert today's joining date using CURRENT_DATE().

---

## Exercise 6

Create a login table.

Store the login timestamp using NOW().

---

# Mini Project

Create an **online shopping database**.

Create two tables.

### orders

| Column | Type |
|---------|------|
| order_id | INT |
| order_date | DATE |

Insert records using CURRENT_DATE().

---

### login_history

| Column | Type |
|---------|------|
| user_id | INT |
| login_time | DATETIME |

Insert records using NOW().

Display all records.

---

# Summary

In this lesson, you learned:

- DATE, TIME, DATETIME and TIMESTAMP data types
- CURRENT_DATE()
- CURRENT_TIME()
- CURDATE()
- CURTIME()
- NOW()
- DATE_FORMAT()
- Common format specifiers
- Practical examples
- Real-world use cases
- Best practices
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 10 — UNIQUE Constraint**

Topics covered:

- What is UNIQUE?
- Why UNIQUE is important
- Creating UNIQUE columns
- Multiple UNIQUE constraints
- UNIQUE vs PRIMARY KEY
- Real-world examples
- Best practices
- Practice exercises
```