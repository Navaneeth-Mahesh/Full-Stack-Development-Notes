# Lesson 17 — SQL Functions

## Learning Objectives

By the end of this lesson, you will understand:

- What SQL Functions are
- Aggregate Functions
- String Functions
- Numeric Functions
- Date & Time Functions
- NULL Functions
- Nested Functions
- Real-world examples
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Exercises

---

# What are SQL Functions?

SQL Functions are **built-in methods** provided by MySQL that perform calculations or manipulate data.

Instead of manually calculating values, you can let MySQL do the work.

Example:

Instead of counting students manually,

```sql
SELECT COUNT(*) FROM students;
```

MySQL returns the total number of students.

---

# Types of SQL Functions

SQL functions are mainly divided into:

```
SQL Functions
│
├── Aggregate Functions
├── String Functions
├── Numeric Functions
├── Date Functions
└── NULL Functions
```

---

# Sample Table

We'll use this table throughout the lesson.

```text
employees
```

| emp_id | name    | department | salary | age | joining_date |
|--------|----------|------------|--------|-----|--------------|
|1|Navaneeth|IT|60000|21|2024-01-10|
|2|Rahul|HR|45000|25|2023-08-20|
|3|Sneha|IT|70000|24|2022-12-15|
|4|John|Sales|50000|28|2023-05-01|
|5|Priya|IT|65000|23|2024-03-12|

---

# Aggregate Functions

Aggregate functions work on **multiple rows** and return **one result**.

---

## COUNT()

Counts rows.

### Syntax

```sql
SELECT COUNT(column_name)
FROM table_name;
```

Example

```sql
SELECT COUNT(*) FROM employees;
```

Output

```
5
```

Count employees in IT department.

```sql
SELECT COUNT(*)
FROM employees
WHERE department='IT';
```

Output

```
3
```

---

## SUM()

Returns the total.

```sql
SELECT SUM(salary)
FROM employees;
```

Output

```
290000
```

---

## AVG()

Returns the average value.

```sql
SELECT AVG(salary)
FROM employees;
```

Output

```
58000
```

---

## MIN()

Returns the smallest value.

```sql
SELECT MIN(salary)
FROM employees;
```

Output

```
45000
```

---

## MAX()

Returns the largest value.

```sql
SELECT MAX(salary)
FROM employees;
```

Output

```
70000
```

---

## Aggregate Example

Find the highest salary in IT.

```sql
SELECT MAX(salary)
FROM employees
WHERE department='IT';
```

Output

```
70000
```

---

# String Functions

Used for manipulating text.

---

## UPPER()

Converts text to uppercase.

```sql
SELECT UPPER(name)
FROM employees;
```

Output

```
NAVANEETH
RAHUL
SNEHA
```

---

## LOWER()

Converts text to lowercase.

```sql
SELECT LOWER(name)
FROM employees;
```

Output

```
navaneeth
rahul
sneha
```

---

## LENGTH()

Returns number of characters.

```sql
SELECT LENGTH(name)
FROM employees;
```

Output

```
9
5
5
4
5
```

---

## CONCAT()

Joins strings together.

```sql
SELECT CONCAT(name,' works in ',department)
FROM employees;
```

Output

```
Navaneeth works in IT
Rahul works in HR
```

---

## TRIM()

Removes spaces.

```sql
SELECT TRIM('    Hello SQL    ');
```

Output

```
Hello SQL
```

---

## LEFT()

Returns left characters.

```sql
SELECT LEFT(name,3)
FROM employees;
```

Output

```
Nav
Rah
Sne
```

---

## RIGHT()

Returns right characters.

```sql
SELECT RIGHT(name,2)
FROM employees;
```

Output

```
th
ul
ha
```

---

## SUBSTRING()

Extracts part of a string.

```sql
SELECT SUBSTRING(name,2,4)
FROM employees;
```

Output

```
avan
ahul
neha
```

---

## REPLACE()

Replaces text.

```sql
SELECT REPLACE(name,'a','@')
FROM employees;
```

Output

```
N@v@neeth
R@hul
```

---

# Numeric Functions

Used for calculations.

---

## ROUND()

Rounds a decimal.

```sql
SELECT ROUND(23.678,2);
```

Output

```
23.68
```

---

## CEIL()

Rounds up.

```sql
SELECT CEIL(18.2);
```

Output

```
19
```

---

## FLOOR()

Rounds down.

```sql
SELECT FLOOR(18.9);
```

Output

```
18
```

---

## ABS()

Returns absolute value.

```sql
SELECT ABS(-200);
```

Output

```
200
```

---

## MOD()

Returns remainder.

```sql
SELECT MOD(20,3);
```

Output

```
2
```

---

## POWER()

Raises to a power.

```sql
SELECT POWER(3,4);
```

Output

```
81
```

---

## SQRT()

Returns square root.

```sql
SELECT SQRT(64);
```

Output

```
8
```

---

# Date Functions

Useful for working with dates.

---

## CURRENT_DATE()

Returns today's date.

```sql
SELECT CURRENT_DATE();
```

Example

```
2026-08-01
```

---

## CURRENT_TIME()

Returns current time.

```sql
SELECT CURRENT_TIME();
```

---

## NOW()

Returns current date and time.

```sql
SELECT NOW();
```

Example

```
2026-08-01 20:45:18
```

---

## YEAR()

Extracts year.

```sql
SELECT YEAR(joining_date)
FROM employees;
```

Output

```
2024
2023
2022
```

---

## MONTH()

Extracts month.

```sql
SELECT MONTH(joining_date)
FROM employees;
```

Output

```
1
8
12
```

---

## DAY()

Returns day of month.

```sql
SELECT DAY(joining_date)
FROM employees;
```

---

## DATEDIFF()

Difference between dates.

```sql
SELECT DATEDIFF(CURRENT_DATE(), joining_date)
FROM employees;
```

Returns the number of days since each employee joined.

---

# NULL Functions

NULL represents **missing or unknown data**.

---

## IFNULL()

Replaces NULL with another value.

Example Table

| name | bonus |
|------|------|
|Navaneeth|1000|
|Rahul|NULL|

Query

```sql
SELECT name,
IFNULL(bonus,0)
FROM employees;
```

Output

```
Navaneeth 1000
Rahul 0
```

---

## COALESCE()

Returns the first non-NULL value.

```sql
SELECT COALESCE(NULL,NULL,500,NULL);
```

Output

```
500
```

---

# Nested Functions

Functions can be combined.

Example

```sql
SELECT UPPER(CONCAT(name,' - ',department))
FROM employees;
```

Output

```
NAVANEETH - IT
RAHUL - HR
```

---

# Using Functions with GROUP BY

```sql
SELECT department,
AVG(salary)
FROM employees
GROUP BY department;
```

Output

| Department | Average Salary |
|------------|---------------|
|HR|45000|
|IT|65000|
|Sales|50000|

---

# Using Functions with WHERE

Employees earning above average salary.

```sql
SELECT *
FROM employees
WHERE salary >
(
SELECT AVG(salary)
FROM employees
);
```

---

# Real-World Example

Suppose you own an e-commerce website.

Products table:

| Product | Price |
|----------|-------|
|Laptop|65000|
|Phone|35000|
|Mouse|800|

Useful queries:

Total revenue

```sql
SELECT SUM(price)
FROM products;
```

Average price

```sql
SELECT AVG(price)
FROM products;
```

Most expensive product

```sql
SELECT MAX(price)
FROM products;
```

Cheapest product

```sql
SELECT MIN(price)
FROM products;
```

Total products

```sql
SELECT COUNT(*)
FROM products;
```

---

# Common Mistakes

### Using Aggregate Functions Without GROUP BY

Wrong

```sql
SELECT department,
AVG(salary)
FROM employees;
```

Correct

```sql
SELECT department,
AVG(salary)
FROM employees
GROUP BY department;
```

---

### Confusing COUNT(*)

```sql
COUNT(*)
```

Counts all rows.

```sql
COUNT(column)
```

Counts only non-NULL values.

---

### Forgetting NULL Handling

Wrong

```sql
salary + bonus
```

If bonus is NULL, the result becomes NULL.

Correct

```sql
salary + IFNULL(bonus,0)
```

---

# Best Practices

- Use aggregate functions for summaries.
- Use aliases for readable output.
- Handle NULL values with `IFNULL()` or `COALESCE()`.
- Combine functions to simplify queries.
- Avoid unnecessary nested functions that reduce readability.

---

# Interview Questions

### 1. What is an Aggregate Function?

A function that performs calculations on multiple rows and returns a single value.

---

### 2. Difference between COUNT(*) and COUNT(column)?

- `COUNT(*)` counts all rows.
- `COUNT(column)` counts only non-NULL values.

---

### 3. Which function returns today's date?

```sql
CURRENT_DATE()
```

---

### 4. Which function returns current date and time?

```sql
NOW()
```

---

### 5. Which function joins strings?

```sql
CONCAT()
```

---

### 6. Which function replaces NULL values?

```sql
IFNULL()
```

or

```sql
COALESCE()
```

---

### 7. Which function converts text to uppercase?

```sql
UPPER()
```

---

### 8. Which function returns the largest value?

```sql
MAX()
```

---

# Practice Exercises

### Exercise 1

Count total employees.

---

### Exercise 2

Find the average salary.

---

### Exercise 3

Find the highest salary.

---

### Exercise 4

Display all employee names in uppercase.

---

### Exercise 5

Display employee names along with their department using `CONCAT()`.

---

### Exercise 6

Find employees who joined in the year 2024.

---

### Exercise 7

Round the value `45.6789` to two decimal places.

---

### Exercise 8

Replace NULL bonuses with 0.

---

### Exercise 9

Find the total salary of employees in the IT department.

---

### Exercise 10

Find the employee count in each department.

---

# Summary

In this lesson, you learned:

- SQL Functions
- Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)
- String Functions (`UPPER`, `LOWER`, `LENGTH`, `CONCAT`, `TRIM`, `LEFT`, `RIGHT`, `SUBSTRING`, `REPLACE`)
- Numeric Functions (`ROUND`, `CEIL`, `FLOOR`, `ABS`, `MOD`, `POWER`, `SQRT`)
- Date Functions (`CURRENT_DATE`, `CURRENT_TIME`, `NOW`, `YEAR`, `MONTH`, `DAY`, `DATEDIFF`)
- NULL Functions (`IFNULL`, `COALESCE`)
- Nested Functions
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 18 — AND, OR, NOT Operators**

Topics covered:

- AND
- OR
- NOT
- Combining Multiple Conditions
- Operator Precedence
- Real-world Examples
- Practice Exercises
- Interview Questions