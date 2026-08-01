# Lesson 6 — SELECT Statement in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What the `SELECT` statement is
- How to retrieve data from a table
- Selecting all columns
- Selecting specific columns
- Using aliases (`AS`)
- Removing duplicate values with `DISTINCT`
- Filtering data using `WHERE`
- Using comparison operators
- Using arithmetic expressions
- SQL execution order
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# What is SELECT?

The `SELECT` statement is used to retrieve data from one or more tables.

Think of it as asking MySQL a question.

Example:

```
Show me all students.
```

SQL:

```sql
SELECT * FROM students;
```

---

# Sample Table

We'll use this table throughout the lesson.

## students

| student_id | first_name | last_name | age | branch | cgpa |
|------------|------------|-----------|-----|--------|------|
|1|Navaneeth|Mahesh|20|CSE|8.9|
|2|Rahul|Kumar|21|ECE|7.5|
|3|Sneha|Reddy|20|IT|9.3|
|4|Ajay|Sharma|22|CSE|8.1|

---

# Basic Syntax

```sql
SELECT column_name
FROM table_name;
```

Example:

```sql
SELECT first_name
FROM students;
```

Output:

| first_name |
|------------|
|Navaneeth|
|Rahul|
|Sneha|
|Ajay|

---

# Selecting All Columns

Use `*` to retrieve every column.

```sql
SELECT *
FROM students;
```

Output:

| student_id | first_name | last_name | age | branch | cgpa |
|------------|------------|-----------|-----|--------|------|
|1|Navaneeth|Mahesh|20|CSE|8.9|
|2|Rahul|Kumar|21|ECE|7.5|
|3|Sneha|Reddy|20|IT|9.3|
|4|Ajay|Sharma|22|CSE|8.1|

---

# Selecting Multiple Columns

```sql
SELECT first_name, branch
FROM students;
```

Output:

| first_name | branch |
|------------|--------|
|Navaneeth|CSE|
|Rahul|ECE|
|Sneha|IT|
|Ajay|CSE|

---

# Selecting a Single Column

```sql
SELECT cgpa
FROM students;
```

Output:

| cgpa |
|------|
|8.9|
|7.5|
|9.3|
|8.1|

---

# Column Order

The output follows the order you specify.

```sql
SELECT branch, first_name
FROM students;
```

Output:

| branch | first_name |
|--------|------------|
|CSE|Navaneeth|
|ECE|Rahul|
|IT|Sneha|
|CSE|Ajay|

---

# Using Aliases (AS)

Aliases rename columns temporarily.

Syntax:

```sql
SELECT column_name AS alias_name
FROM table;
```

Example:

```sql
SELECT first_name AS Name
FROM students;
```

Output:

| Name |
|------|
|Navaneeth|
|Rahul|
|Sneha|
|Ajay|

---

# Multiple Aliases

```sql
SELECT
first_name AS FirstName,
last_name AS LastName,
cgpa AS GPA
FROM students;
```

Output:

| FirstName | LastName | GPA |
|------------|----------|-----|
|Navaneeth|Mahesh|8.9|
|Rahul|Kumar|7.5|
|Sneha|Reddy|9.3|
|Ajay|Sharma|8.1|

---

# DISTINCT

Suppose many students belong to the same branch.

Without DISTINCT:

```sql
SELECT branch
FROM students;
```

Output:

```
CSE
ECE
IT
CSE
```

Duplicates appear.

Using DISTINCT:

```sql
SELECT DISTINCT branch
FROM students;
```

Output:

```
CSE
ECE
IT
```

Duplicates are removed.

---

# WHERE Clause

Used to filter rows.

Syntax:

```sql
SELECT *
FROM table
WHERE condition;
```

Example:

```sql
SELECT *
FROM students
WHERE branch = 'CSE';
```

Output:

| student_id | first_name | branch |
|------------|------------|--------|
|1|Navaneeth|CSE|
|4|Ajay|CSE|

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| = | Equal |
| != | Not Equal |
| <> | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

# Equal To

```sql
SELECT *
FROM students
WHERE age = 20;
```

---

# Greater Than

```sql
SELECT *
FROM students
WHERE cgpa > 8;
```

---

# Less Than

```sql
SELECT *
FROM students
WHERE age < 21;
```

---

# Not Equal

```sql
SELECT *
FROM students
WHERE branch != 'ECE';
```

---

# Numeric Filtering

```sql
SELECT first_name, cgpa
FROM students
WHERE cgpa >= 8.5;
```

---

# String Filtering

```sql
SELECT *
FROM students
WHERE first_name = 'Rahul';
```

Remember:

Strings must be inside quotes.

Correct:

```sql
'Rahul'
```

Wrong:

```sql
Rahul
```

---

# Arithmetic Expressions

SQL can perform calculations.

Example:

```sql
SELECT
first_name,
cgpa + 1 AS UpdatedCGPA
FROM students;
```

Output:

| first_name | UpdatedCGPA |
|------------|-------------|
|Navaneeth|9.9|
|Rahul|8.5|
|Sneha|10.3|
|Ajay|9.1|

This does **not** update the table.
It only changes the displayed result.

---

# Concatenating Columns

```sql
SELECT
CONCAT(first_name,' ',last_name) AS FullName
FROM students;
```

Output:

| FullName |
|-----------|
|Navaneeth Mahesh|
|Rahul Kumar|
|Sneha Reddy|
|Ajay Sharma|

---

# SQL Execution Order

Although we write:

```sql
SELECT first_name
FROM students
WHERE age = 20;
```

MySQL internally executes:

```
FROM

↓

WHERE

↓

SELECT
```

Understanding this helps with complex queries.

---

# Real-World Example

Imagine an e-commerce database.

Products:

| id | product | price | stock |
|----|----------|-------|------|
|1|Laptop|65000|15|
|2|Mouse|500|100|
|3|Keyboard|1200|40|

Retrieve expensive products:

```sql
SELECT product, price
FROM products
WHERE price > 1000;
```

---

# Common Mistakes

## Missing Quotes

Wrong:

```sql
SELECT *
FROM students
WHERE first_name = Rahul;
```

Correct:

```sql
WHERE first_name = 'Rahul';
```

---

## Wrong Column Name

Wrong:

```sql
SELECT firstname
FROM students;
```

Correct:

```sql
SELECT first_name
FROM students;
```

---

## Forgetting Semicolon

Wrong:

```sql
SELECT *
FROM students
```

Correct:

```sql
SELECT *
FROM students;
```

---

# Best Practices

- Avoid `SELECT *` in production; fetch only required columns.
- Use meaningful aliases.
- Filter unnecessary data with `WHERE`.
- Keep SQL keywords uppercase for readability.
- Use `DISTINCT` only when needed.

---

# Interview Questions

## 1. What does `SELECT` do?

Retrieves data from one or more tables.

---

## 2. Difference between `SELECT *` and selecting specific columns?

`SELECT *` retrieves all columns, while selecting specific columns returns only the required data.

---

## 3. What is `DISTINCT`?

It removes duplicate values from the result set.

---

## 4. What is an alias?

A temporary name for a column or table using `AS`.

---

## 5. Does `SELECT` change the data?

No. It only reads data.

---

## 6. Why use `WHERE`?

To filter rows based on conditions.

---

# Practice Exercises

## Exercise 1

Display all students.

```sql
SELECT *
FROM students;
```

---

## Exercise 2

Display only first names.

---

## Exercise 3

Display first name and CGPA.

---

## Exercise 4

Display only unique branches.

---

## Exercise 5

Display students with CGPA greater than 8.

---

## Exercise 6

Display students whose branch is CSE.

---

## Exercise 7

Display age and rename it as StudentAge.

---

## Exercise 8

Display full names using `CONCAT()`.

---

# Mini Project

Create an `employees` table with columns:

- emp_id
- emp_name
- department
- salary

Insert at least five records.

Then write queries to:

1. Show all employees.
2. Show only employee names.
3. Show unique departments.
4. Show employees with salary greater than 50000.
5. Rename salary as MonthlySalary.
6. Display employee full names (if you split names into first and last).

---

# Summary

In this lesson, you learned:

- `SELECT`
- `SELECT *`
- Selecting specific columns
- Aliases (`AS`)
- `DISTINCT`
- `WHERE`
- Comparison operators
- Arithmetic expressions
- `CONCAT()`
- SQL execution order
- Best practices
- Common mistakes
- Practice exercises

---

# Next Lesson

**Lesson 7 — UPDATE & DELETE**

Topics covered:

- `UPDATE`
- `DELETE`
- `WHERE` with UPDATE
- `WHERE` with DELETE
- Updating multiple columns
- Safe updates
- Common mistakes
- Real-world examples
- Practice exercises