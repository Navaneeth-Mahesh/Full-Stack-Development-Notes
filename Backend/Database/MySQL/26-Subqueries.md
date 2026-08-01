# Lesson 26 — Subqueries

## Learning Objectives

By the end of this lesson, you will understand:

- What a Subquery is
- Why Subqueries are useful
- Single-row Subqueries
- Multi-row Subqueries
- Correlated Subqueries
- Subqueries with SELECT
- Subqueries with WHERE
- Subqueries with FROM
- EXISTS and NOT EXISTS
- Real-world examples
- Performance considerations
- Best practices
- Interview questions
- Practice exercises

---

# What is a Subquery?

A **Subquery** (also called an **Inner Query** or **Nested Query**) is a query written **inside another SQL query**.

The inner query executes first, and its result is used by the outer query.

Think of it as:

```
Outer Query
    │
    └── Subquery
```

Example:

```sql
SELECT name
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);
```

Execution order:

1. Find the average salary.
2. Return employees whose salary is greater than that average.

---

# Why Use Subqueries?

Subqueries help when:

- Comparing values
- Filtering data
- Finding maximum or minimum values
- Creating temporary datasets
- Avoiding multiple separate queries
- Simplifying complex logic

---

# Sample Tables

## employees

| emp_id | name | department | salary |
|--------|------|------------|-------:|
|1|Alice|HR|40000|
|2|Bob|IT|70000|
|3|Charlie|IT|80000|
|4|David|Sales|45000|
|5|Eva|HR|60000|

---

## departments

| dept_id | department |
|---------|------------|
|1|HR|
|2|IT|
|3|Sales|

---

# Basic Subquery

Find employees earning more than the average salary.

```sql
SELECT *
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);
```

Inner query:

```sql
SELECT AVG(salary)
FROM employees;
```

Suppose it returns:

```
59000
```

Outer query becomes:

```sql
SELECT *
FROM employees
WHERE salary > 59000;
```

Result:

| name | salary |
|------|-------:|
|Bob|70000|
|Charlie|80000|
|Eva|60000|

---

# Types of Subqueries

Main categories:

- Single-row
- Multi-row
- Correlated
- Scalar
- Table Subqueries

---

# Single-row Subqueries

Returns exactly one value.

Example:

```sql
SELECT *
FROM employees
WHERE salary =
(
    SELECT MAX(salary)
    FROM employees
);
```

Inner query:

```sql
SELECT MAX(salary)
FROM employees;
```

Returns:

```
80000
```

Outer query:

```sql
SELECT *
FROM employees
WHERE salary = 80000;
```

Result:

| name |
|------|
|Charlie|

---

# Single-row Operators

Used with:

```sql
=
<
>
<=
>=
<>
```

Example:

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

# Multi-row Subqueries

Returns multiple rows.

Example:

```sql
SELECT department
FROM departments;
```

Result:

```
HR
IT
Sales
```

Cannot use:

```sql
=
```

Instead use:

```sql
IN
ANY
ALL
```

---

# IN Operator

Find employees in HR or IT.

```sql
SELECT *
FROM employees
WHERE department IN
(
    SELECT department
    FROM departments
    WHERE department <> 'Sales'
);
```

Subquery returns:

```
HR
IT
```

Result:

```
Alice
Bob
Charlie
Eva
```

---

# ANY Operator

Returns rows satisfying **at least one** value.

Example:

```sql
SELECT *
FROM employees
WHERE salary >
ANY
(
    SELECT salary
    FROM employees
    WHERE department='HR'
);
```

HR salaries:

```
40000
60000
```

Condition:

```
salary > ANY (40000,60000)
```

Equivalent to:

```
salary > 40000
```

Result:

```
Bob
Charlie
David
Eva
```

---

# ALL Operator

Must satisfy **every** value.

```sql
SELECT *
FROM employees
WHERE salary >
ALL
(
    SELECT salary
    FROM employees
    WHERE department='HR'
);
```

HR salaries:

```
40000
60000
```

Condition:

```
salary > 60000
```

Result:

```
Bob
Charlie
```

---

# Subqueries with WHERE

Most common usage.

Example:

```sql
SELECT *
FROM employees
WHERE department =
(
    SELECT department
    FROM employees
    WHERE name='Alice'
);
```

Alice belongs to:

```
HR
```

Final query:

```sql
SELECT *
FROM employees
WHERE department='HR';
```

Result:

```
Alice
Eva
```

---

# Subqueries with SELECT

Subqueries can appear in the SELECT list.

Example:

```sql
SELECT
name,
salary,
(
    SELECT AVG(salary)
    FROM employees
) AS average_salary
FROM employees;
```

Result:

| name | salary | average_salary |
|------|-------:|---------------:|
|Alice|40000|59000|
|Bob|70000|59000|
|Charlie|80000|59000|

---

# Subqueries with FROM

Treat a subquery as a temporary table.

Example:

```sql
SELECT *
FROM
(
    SELECT name, salary
    FROM employees
) AS emp;
```

The alias (`emp`) is mandatory.

---

# Why Alias is Required

Wrong:

```sql
SELECT *
FROM
(
    SELECT *
    FROM employees
);
```

Correct:

```sql
SELECT *
FROM
(
    SELECT *
    FROM employees
) AS emp;
```

---

# Correlated Subqueries

A correlated subquery depends on the outer query.

Unlike normal subqueries, it executes once **for every row** of the outer query.

Example:

```sql
SELECT e1.name,
       e1.salary
FROM employees e1
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees e2
    WHERE e1.department = e2.department
);
```

Explanation:

For every employee:

1. Find the average salary in that employee's department.
2. Compare the employee's salary to that average.

This cannot be executed independently because the inner query uses `e1.department`.

---

# EXISTS

Checks whether a subquery returns **at least one row**.

Example:

```sql
SELECT *
FROM departments d
WHERE EXISTS
(
    SELECT *
    FROM employees e
    WHERE e.department=d.department
);
```

Meaning:

Return only departments that have employees.

---

# NOT EXISTS

Returns rows where the subquery returns **no rows**.

Example:

```sql
SELECT *
FROM departments d
WHERE NOT EXISTS
(
    SELECT *
    FROM employees e
    WHERE e.department=d.department
);
```

Useful for finding:

- Empty departments
- Customers without orders
- Products never sold

---

# Nested Subqueries

Subqueries can contain another subquery.

Example:

```sql
SELECT *
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM
    (
        SELECT salary
        FROM employees
    ) AS temp
);
```

Although possible, avoid unnecessary nesting.

---

# Real-World Example 1

Find customers who placed orders.

```sql
SELECT *
FROM customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM orders
);
```

---

# Real-World Example 2

Products never ordered.

```sql
SELECT *
FROM products
WHERE product_id NOT IN
(
    SELECT product_id
    FROM order_items
);
```

---

# Real-World Example 3

Employees earning the highest salary.

```sql
SELECT *
FROM employees
WHERE salary=
(
    SELECT MAX(salary)
    FROM employees
);
```

---

# Real-World Example 4

Students scoring above average.

```sql
SELECT *
FROM students
WHERE marks >
(
    SELECT AVG(marks)
    FROM students
);
```

---

# Performance Considerations

Subqueries are powerful, but not always the fastest solution.

Example:

```sql
SELECT *
FROM employees
WHERE department IN
(
    SELECT department
    FROM departments
);
```

For large datasets, a JOIN may perform better.

Compare:

Subquery:

```sql
SELECT *
FROM employees
WHERE department IN
(
    SELECT department
    FROM departments
);
```

JOIN:

```sql
SELECT e.*
FROM employees e
JOIN departments d
ON e.department=d.department;
```

The optimizer often rewrites queries internally, but understanding both approaches helps you choose the best one.

---

# Common Mistakes

## Using = with Multiple Rows

Wrong:

```sql
SELECT *
FROM employees
WHERE department =
(
    SELECT department
    FROM departments
);
```

Error:

```
Subquery returns more than one row
```

Correct:

```sql
WHERE department IN (...)
```

---

## Missing Alias in FROM

Wrong:

```sql
FROM
(
    SELECT *
    FROM employees
);
```

Correct:

```sql
FROM
(
    SELECT *
    FROM employees
) AS emp;
```

---

## Unnecessary Correlated Subqueries

Avoid:

```sql
SELECT *
FROM employees e
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
    WHERE department=e.department
);
```

when a window function or JOIN can solve the problem more efficiently in some databases.

---

# Best Practices

- Keep subqueries readable.
- Use aliases for clarity.
- Prefer JOINs for large datasets when appropriate.
- Use EXISTS instead of IN for existence checks on large tables.
- Avoid deeply nested subqueries.
- Always test performance on production-sized data.

---

# Interview Questions

## 1. What is a subquery?

A query written inside another SQL query.

---

## 2. What is a correlated subquery?

A subquery that references columns from the outer query and runs once for each outer row.

---

## 3. Difference between IN and EXISTS?

- `IN` compares values against a returned list.
- `EXISTS` only checks whether at least one matching row exists.

---

## 4. Where can subqueries be used?

- SELECT
- FROM
- WHERE
- HAVING

---

## 5. Can a subquery return multiple rows?

Yes. In that case, use operators like `IN`, `ANY`, or `ALL` instead of `=`.

---

# Practice Exercises

## Exercise 1

Find employees earning more than the average salary.

---

## Exercise 2

Find the employee with the maximum salary.

---

## Exercise 3

Find employees working in departments returned by another query.

---

## Exercise 4

Display each employee with the company's average salary.

---

## Exercise 5

Find departments that currently have employees using `EXISTS`.

---

## Exercise 6

Find departments that have no employees using `NOT EXISTS`.

---

## Exercise 7

Write a correlated subquery to find employees earning above the average salary of their own department.

---

# Mini Project

Using an e-commerce database:

- Find customers who placed at least one order.
- Find products that have never been ordered.
- Find products priced above the average price.
- Find orders whose total exceeds the average order value.
- Display each product with the average product price.

---

# Summary

In this lesson, you learned:

- What a Subquery is
- Why Subqueries are useful
- Single-row Subqueries
- Multi-row Subqueries
- Scalar Subqueries
- Correlated Subqueries
- Subqueries in `SELECT`
- Subqueries in `WHERE`
- Subqueries in `FROM`
- `EXISTS`
- `NOT EXISTS`
- Real-world examples
- Performance considerations
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 27 — GROUP BY**

Topics covered:

- What is GROUP BY?
- Aggregate Functions
- HAVING
- GROUP BY Multiple Columns
- GROUP BY with ORDER BY
- Real-world examples