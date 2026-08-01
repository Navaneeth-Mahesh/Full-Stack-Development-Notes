# Lesson 22 — UNION in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What `UNION` is
- Why `UNION` is used
- Difference between `UNION` and `UNION ALL`
- Rules for using `UNION`
- Combining results from multiple tables
- Using `ORDER BY` with `UNION`
- Real-world examples
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# What is UNION?

`UNION` is used to combine the results of **two or more SELECT queries** into a single result set.

Think of it as merging multiple lists into one.

Example:

Table 1

| Name |
|------|
| Navaneeth |
| Rahul |

Table 2

| Name |
|------|
| Sneha |
| Priya |

Using UNION:

```sql
SELECT Name FROM students
UNION
SELECT Name FROM teachers;
```

Result:

| Name |
|------|
| Navaneeth |
| Rahul |
| Sneha |
| Priya |

---

# Why Use UNION?

Suppose you have two separate tables:

```
customers
employees
```

Both contain names.

Instead of querying them separately, you can combine them into one list.

Without UNION:

```
Run Query 1

Run Query 2

Combine manually
```

With UNION:

```
One Query

↓

One Result
```

---

# Syntax

```sql
SELECT column1
FROM table1

UNION

SELECT column1
FROM table2;
```

You can also combine more than two queries.

Example:

```sql
SELECT name FROM students

UNION

SELECT name FROM teachers

UNION

SELECT name FROM staff;
```

---

# Example Database

Students

| StudentID | Name |
|-----------|------|
|1|Navaneeth|
|2|Rahul|
|3|Sneha|

Teachers

| TeacherID | Name |
|-----------|------|
|101|Arun|
|102|Sneha|
|103|Kiran|

---

# Basic UNION Example

```sql
SELECT Name
FROM students

UNION

SELECT Name
FROM teachers;
```

Result:

| Name |
|------|
|Navaneeth|
|Rahul|
|Sneha|
|Arun|
|Kiran|

Notice that **Sneha appears only once**.

---

# UNION Removes Duplicates

Original Data

Students

```
Navaneeth
Rahul
Sneha
```

Teachers

```
Sneha
Arun
Kiran
```

Using:

```sql
UNION
```

Result

```
Navaneeth
Rahul
Sneha
Arun
Kiran
```

Duplicate values are removed automatically.

---

# UNION ALL

`UNION ALL` combines results **without removing duplicates**.

Syntax:

```sql
SELECT Name
FROM students

UNION ALL

SELECT Name
FROM teachers;
```

Result:

```
Navaneeth

Rahul

Sneha

Sneha

Arun

Kiran
```

Now both occurrences of "Sneha" are shown.

---

# UNION vs UNION ALL

| Feature | UNION | UNION ALL |
|----------|--------|-----------|
|Combines Results|Yes|Yes|
|Removes Duplicates|Yes|No|
|Keeps Duplicates|No|Yes|
|Performance|Slightly Slower|Faster|

---

# When to Use UNION

Use UNION when:

- Duplicate values should not appear
- Creating unique reports
- Combining similar datasets

Example:

```
Registered Users

+

Premium Users

↓

Unique User List
```

---

# When to Use UNION ALL

Use UNION ALL when:

- Every row is important
- Duplicate records matter
- Better performance is needed

Example:

```
Sales of January

+

Sales of February

↓

Complete Sales History
```

Even if the same product appears many times, keep every record.

---

# Rules for UNION

## Rule 1

Each SELECT must have the **same number of columns**.

Correct:

```sql
SELECT Name
FROM students

UNION

SELECT Name
FROM teachers;
```

Wrong:

```sql
SELECT Name, Age
FROM students

UNION

SELECT Name
FROM teachers;
```

Error:

```
The used SELECT statements have a different number of columns
```

---

## Rule 2

The columns must have **compatible data types**.

Correct:

```sql
VARCHAR

UNION

VARCHAR
```

Correct:

```sql
INT

UNION

INT
```

Avoid mixing unrelated types:

```sql
Age

UNION

Salary
```

---

## Rule 3

Column names in the final result come from the **first SELECT statement**.

Example:

```sql
SELECT Name
FROM students

UNION

SELECT TeacherName
FROM teachers;
```

Output column:

```
Name
```

Not:

```
TeacherName
```

---

# Combining Multiple Columns

Students

| Name | City |
|------|------|
|Navaneeth|Hyderabad|
|Rahul|Delhi|

Teachers

| Name | City |
|------|------|
|Arun|Mumbai|
|Sneha|Delhi|

Query:

```sql
SELECT Name, City
FROM students

UNION

SELECT Name, City
FROM teachers;
```

Result:

| Name | City |
|------|------|
|Navaneeth|Hyderabad|
|Rahul|Delhi|
|Arun|Mumbai|
|Sneha|Delhi|

---

# Using ORDER BY with UNION

You can sort the final combined result.

```sql
SELECT Name
FROM students

UNION

SELECT Name
FROM teachers

ORDER BY Name;
```

Result:

```
Arun

Kiran

Navaneeth

Rahul

Sneha
```

Notice that `ORDER BY` is written **only once**, after the final `SELECT`.

---

# UNION with WHERE

```sql
SELECT Name
FROM students
WHERE City='Hyderabad'

UNION

SELECT Name
FROM teachers
WHERE City='Hyderabad';
```

Only Hyderabad people are returned.

---

# Using Aliases

```sql
SELECT Name AS Person
FROM students

UNION

SELECT Name
FROM teachers;
```

Output:

```
Person
```

---

# Real-World Example 1

## Online Store

Tables

```
customers

employees
```

Need:

```
All People
```

Query:

```sql
SELECT Name
FROM customers

UNION

SELECT Name
FROM employees;
```

---

# Real-World Example 2

University Portal

Tables

```
students

faculty

staff
```

Query:

```sql
SELECT Name FROM students

UNION

SELECT Name FROM faculty

UNION

SELECT Name FROM staff;
```

Creates a complete people directory.

---

# Real-World Example 3

Bank

```
Current Accounts

Savings Accounts
```

Need:

```
All Account Holders
```

```sql
SELECT CustomerName
FROM current_accounts

UNION

SELECT CustomerName
FROM savings_accounts;
```

---

# Common Errors

## Different Number of Columns

Wrong:

```sql
SELECT Name, Age
FROM students

UNION

SELECT Name
FROM teachers;
```

Error:

```
Different number of columns
```

---

## Wrong Data Types

```sql
SELECT Name
FROM students

UNION

SELECT Salary
FROM employees;
```

This may produce unexpected results or type conversions.

---

## ORDER BY in the Wrong Place

Wrong:

```sql
SELECT Name
FROM students
ORDER BY Name

UNION

SELECT Name
FROM teachers;
```

Correct:

```sql
SELECT Name
FROM students

UNION

SELECT Name
FROM teachers

ORDER BY Name;
```

---

# Performance Notes

`UNION`

- Removes duplicates
- Requires extra work to compare rows
- Slightly slower

`UNION ALL`

- Simply appends results
- No duplicate checking
- Faster

Use `UNION ALL` if duplicate removal is unnecessary.

---

# Best Practices

- Use `UNION` for unique results.
- Use `UNION ALL` when duplicates should remain.
- Ensure all SELECT statements have the same number of columns.
- Keep data types compatible.
- Place `ORDER BY` only at the end.
- Use meaningful column aliases.

---

# Interview Questions

## 1. What is UNION?

`UNION` combines the results of two or more SELECT queries into a single result while removing duplicates.

---

## 2. What is UNION ALL?

`UNION ALL` combines results without removing duplicates.

---

## 3. Which is faster?

`UNION ALL`, because it doesn't perform duplicate elimination.

---

## 4. Can UNION combine different tables?

Yes, as long as the selected columns follow the UNION rules.

---

## 5. What are the rules for UNION?

- Same number of columns
- Compatible data types
- Similar column order
- `ORDER BY` only at the end

---

## 6. Does UNION remove duplicates?

Yes.

---

## 7. Does UNION ALL remove duplicates?

No.

---

# Practice Exercises

## Exercise 1

Create two tables.

Students

| Name |
|------|
|Navaneeth|
|Rahul|

Teachers

| Name |
|------|
|Sneha|
|Rahul|

Display all unique names using `UNION`.

---

## Exercise 2

Display all names, including duplicates, using `UNION ALL`.

---

## Exercise 3

Create two tables containing:

```
ProductName

Price
```

Combine them using `UNION`.

---

## Exercise 4

Sort the combined result alphabetically.

---

## Exercise 5

Combine data from three tables:

- students
- teachers
- staff

into one result.

---

# Mini Project

Suppose you have three tables:

```
customers

employees

vendors
```

Each table contains:

```
Name
City
```

Tasks:

1. Display every unique person.
2. Display every record, including duplicates.
3. Sort results by city.
4. Filter only people from Hyderabad before combining.
5. Compare the output of `UNION` and `UNION ALL`.

---

# Summary

In this lesson, you learned:

- What `UNION` is
- Why it is used
- Difference between `UNION` and `UNION ALL`
- Rules for `UNION`
- Combining multiple tables
- Using `ORDER BY` and `WHERE` with `UNION`
- Real-world applications
- Performance differences
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 23 — SELF JOIN**

Topics covered:

- What is a Self Join?
- Why Self Join is needed
- Manager–Employee relationships
- Hierarchical data
- Self Join with aliases
- Real-world examples
- Practice exercises