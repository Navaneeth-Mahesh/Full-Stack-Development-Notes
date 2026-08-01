# Lesson 4 — INSERT ROWS in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What inserting data means
- How to use the `INSERT INTO` statement
- Insert single and multiple rows
- Insert values into specific columns
- Use `NULL` values
- Insert dates and timestamps
- Common errors and how to fix them
- Best practices
- Interview questions
- Practice exercises

---

# What is INSERT?

Creating a table only defines its structure. To store actual information, you use the `INSERT` statement.

Think of a table as an empty notebook. `INSERT` writes information into that notebook.

Example:

Students Table

| StudentID | Name | Age |
|------------|------|-----|
| (empty) | | |

After inserting:

| StudentID | Name | Age |
|------------|------|-----|
| 1 | Navaneeth | 20 |

---

# Syntax

```sql
INSERT INTO table_name
VALUES(value1, value2, value3);
```

Example:

```sql
INSERT INTO students
VALUES(1, 'Navaneeth', 20);
```

---

# Creating a Sample Table

```sql
CREATE TABLE students(
    student_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT
);
```

---

# Insert One Row

```sql
INSERT INTO students
VALUES
(1,'Navaneeth','Mahesh',20);
```

Result:

| student_id | first_name | last_name | age |
|------------|------------|-----------|-----|
|1|Navaneeth|Mahesh|20|

---

# View Data

```sql
SELECT * FROM students;
```

Output:

| student_id | first_name | last_name | age |
|------------|------------|-----------|-----|
|1|Navaneeth|Mahesh|20|

---

# Insert Multiple Rows

Instead of inserting one row at a time:

```sql
INSERT INTO students
VALUES
(2,'Rahul','Kumar',21),
(3,'Anjali','Reddy',19),
(4,'Sneha','Patel',20);
```

Output:

| student_id | first_name | last_name | age |
|------------|------------|-----------|-----|
|1|Navaneeth|Mahesh|20|
|2|Rahul|Kumar|21|
|3|Anjali|Reddy|19|
|4|Sneha|Patel|20|

This is faster than writing multiple INSERT statements.

---

# Insert into Specific Columns

You don't always have to insert values into every column.

Syntax:

```sql
INSERT INTO table_name(column1,column2)
VALUES(value1,value2);
```

Example:

```sql
INSERT INTO students(student_id, first_name)
VALUES(5,'Arjun');
```

Output:

| student_id | first_name | last_name | age |
|------------|------------|-----------|-----|
|5|Arjun|NULL|NULL|

Unspecified columns receive NULL (unless a default value is defined).

---

# Column Order Matters

Correct:

```sql
INSERT INTO students
(student_id, first_name, age)

VALUES
(6,'Meena',22);
```

Wrong:

```sql
INSERT INTO students
(student_id, first_name, age)

VALUES
('Meena',6,22);
```

Always match values to the listed columns.

---

# Using NULL

NULL means **no value** or **unknown value**.

Example:

```sql
INSERT INTO students
VALUES
(7,'Kiran',NULL,NULL);
```

Output:

| student_id | first_name | last_name | age |
|------------|------------|-----------|-----|
|7|Kiran|NULL|NULL|

NULL is different from:

```
0
''
False
```

It represents missing information.

---

# Inserting Dates

Create a table:

```sql
CREATE TABLE employees(

employee_id INT,

employee_name VARCHAR(50),

joining_date DATE

);
```

Insert:

```sql
INSERT INTO employees
VALUES
(1,'Navaneeth','2026-08-01');
```

Date format:

```
YYYY-MM-DD
```

---

# DATETIME Example

```sql
CREATE TABLE orders(

order_id INT,

ordered_at DATETIME

);
```

Insert:

```sql
INSERT INTO orders
VALUES
(1,'2026-08-01 10:45:30');
```

Format:

```
YYYY-MM-DD HH:MM:SS
```

---

# Using CURRENT_DATE()

```sql
INSERT INTO employees
VALUES
(2,'Rahul',CURRENT_DATE());
```

Automatically inserts today's date.

---

# Using CURRENT_TIMESTAMP()

```sql
CREATE TABLE login_history(

id INT,

login_time TIMESTAMP

);
```

```sql
INSERT INTO login_history
VALUES
(1,CURRENT_TIMESTAMP());
```

Automatically stores the current date and time.

---

# String Values

Text values must be inside single quotes.

Correct:

```sql
INSERT INTO students
VALUES
(8,'Ajay','Rao',22);
```

Wrong:

```sql
INSERT INTO students
VALUES
(8,Ajay,Rao,22);
```

---

# Numeric Values

Numbers should not be enclosed in quotes.

Correct:

```sql
20
```

Not recommended:

```sql
'20'
```

MySQL may convert it automatically, but using the correct data type is better.

---

# Common Errors

## Error 1

Wrong number of values

```sql
INSERT INTO students
VALUES
(1,'Navaneeth');
```

Output:

```
Column count doesn't match value count
```

Fix:

Provide a value for every column or specify the column names.

---

## Error 2

Wrong data type

```sql
INSERT INTO students
VALUES
('abc','Navaneeth','Mahesh',20);
```

If `student_id` is INT, MySQL may produce an error depending on SQL mode.

---

## Error 3

Misspelled table name

```sql
INSERT INTO student
VALUES(...);
```

Output:

```
Table doesn't exist
```

---

## Error 4

Forgetting quotes

Wrong:

```sql
INSERT INTO students
VALUES
(1,Navaneeth,Mahesh,20);
```

Correct:

```sql
INSERT INTO students
VALUES
(1,'Navaneeth','Mahesh',20);
```

---

# Real-World Example

Users Table

```sql
CREATE TABLE users(

user_id INT,

username VARCHAR(50),

email VARCHAR(100)

);
```

Insert:

```sql
INSERT INTO users
VALUES

(1,'navaneeth','nav@gmail.com'),

(2,'rahul','rahul@gmail.com'),

(3,'sneha','sneha@gmail.com');
```

---

# Best Practices

- Always specify column names.
- Insert multiple rows in one statement when possible.
- Use meaningful values.
- Match data types correctly.
- Use single quotes for strings.
- Store dates in `YYYY-MM-DD` format.
- Validate data before inserting.

---

# Interview Questions

## 1. Which command inserts data into a table?

```sql
INSERT INTO
```

---

## 2. Can multiple rows be inserted at once?

Yes.

Example:

```sql
INSERT INTO students
VALUES
(...),
(...),
(...);
```

---

## 3. Why specify column names?

It improves readability and prevents errors if the table structure changes.

---

## 4. What is NULL?

A missing or unknown value.

---

## 5. What is the difference between NULL and 0?

- NULL = no value / unknown
- 0 = actual numeric value

---

## 6. Which function inserts today's date?

```sql
CURRENT_DATE()
```

---

## 7. Which function inserts the current date and time?

```sql
CURRENT_TIMESTAMP()
```

---

# Practice Exercises

## Exercise 1

Create this table:

```sql
CREATE TABLE products(

product_id INT,

product_name VARCHAR(50),

price DECIMAL(8,2)

);
```

---

## Exercise 2

Insert one product.

---

## Exercise 3

Insert five products in a single query.

---

## Exercise 4

Insert only:

- product_id
- product_name

Leave price empty.

---

## Exercise 5

Create an employee table with a joining date and insert today's date using `CURRENT_DATE()`.

---

# Mini Project

Create a `books` table:

```sql
CREATE TABLE books(

book_id INT,

title VARCHAR(100),

author VARCHAR(100),

price DECIMAL(8,2)

);
```

Insert these records:

| book_id | title | author | price |
|----------|----------------------|--------------|-------|
|1|Atomic Habits|James Clear|499.00|
|2|Deep Work|Cal Newport|599.00|
|3|Clean Code|Robert Martin|799.00|
|4|The Pragmatic Programmer|Andrew Hunt|899.00|
|5|Think Like a Monk|Jay Shetty|450.00|

Display the table:

```sql
SELECT * FROM books;
```

---

# Summary

In this lesson, you learned:

- What `INSERT INTO` does
- Insert a single row
- Insert multiple rows
- Insert into selected columns
- Use `NULL`
- Insert dates and timestamps
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 5 — SELECT Statement**

Topics covered:

- Retrieving data
- Selecting specific columns
- `SELECT *`
- `DISTINCT`
- `WHERE`
- Aliases (`AS`)
- Filtering records
- Practical examples