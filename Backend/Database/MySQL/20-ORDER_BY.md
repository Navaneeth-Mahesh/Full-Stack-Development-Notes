# Lesson 20 — ORDER BY

## Learning Objectives

By the end of this lesson, you will understand:

- What `ORDER BY` is
- Why sorting data is important
- Sorting in Ascending (`ASC`) order
- Sorting in Descending (`DESC`) order
- Sorting using multiple columns
- Sorting NULL values
- Combining `ORDER BY` with `LIMIT`
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# What is ORDER BY?

The `ORDER BY` clause is used to **sort the result of a query**.

Without `ORDER BY`, MySQL returns rows in an undefined order (often the insertion order, but this is **not guaranteed**).

---

# Syntax

```sql
SELECT column1, column2
FROM table_name
ORDER BY column_name;
```

Example:

```sql
SELECT *
FROM students
ORDER BY name;
```

---

# Sample Table

## students

| id | name      | age | marks |
|----|-----------|-----|-------|
| 1  | Rahul     | 20  | 85    |
| 2  | Navaneeth | 19  | 95    |
| 3  | Anjali    | 21  | 78    |
| 4  | Priya     | 20  | 90    |

---

# ASC (Ascending Order)

Ascending means:

- A → Z
- 0 → 9
- Lowest → Highest
- Oldest date → Newest date

`ASC` is the **default** sorting order.

Syntax:

```sql
SELECT *
FROM students
ORDER BY marks ASC;
```

Result:

| name | marks |
|------|------|
| Anjali | 78 |
| Rahul | 85 |
| Priya | 90 |
| Navaneeth | 95 |

Since `ASC` is the default, this is equivalent:

```sql
SELECT *
FROM students
ORDER BY marks;
```

---

# DESC (Descending Order)

Descending means:

- Z → A
- 9 → 0
- Highest → Lowest
- Newest → Oldest

Syntax:

```sql
SELECT *
FROM students
ORDER BY marks DESC;
```

Result:

| name | marks |
|------|------|
| Navaneeth | 95 |
| Priya | 90 |
| Rahul | 85 |
| Anjali | 78 |

---

# Sorting Text Columns

```sql
SELECT *
FROM students
ORDER BY name;
```

Result:

```
Anjali
Navaneeth
Priya
Rahul
```

Descending:

```sql
SELECT *
FROM students
ORDER BY name DESC;
```

Result:

```
Rahul
Priya
Navaneeth
Anjali
```

---

# Sorting Numbers

Ascending:

```sql
SELECT *
FROM students
ORDER BY age;
```

Result:

```
19
20
20
21
```

Descending:

```sql
SELECT *
FROM students
ORDER BY age DESC;
```

Result:

```
21
20
20
19
```

---

# Sorting Dates

Suppose:

| order_id | order_date |
|----------|------------|
|101|2026-01-10|
|102|2026-05-15|
|103|2026-03-08|

Newest first:

```sql
SELECT *
FROM orders
ORDER BY order_date DESC;
```

Oldest first:

```sql
SELECT *
FROM orders
ORDER BY order_date ASC;
```

---

# Sorting by Multiple Columns

Sometimes one column has duplicate values.

Example:

| name | age |
|------|-----|
| Rahul |20|
| Priya |20|
| Navaneeth|19|
| Anjali|21|

Sort by age first, then by name:

```sql
SELECT *
FROM students
ORDER BY age ASC, name ASC;
```

Result:

| name | age |
|------|-----|
| Navaneeth |19|
| Priya |20|
| Rahul |20|
| Anjali |21|

Explanation:

- Age is sorted first.
- If two rows have the same age, MySQL sorts them by name.

---

# Different Sorting Directions

You can mix `ASC` and `DESC`.

```sql
SELECT *
FROM students
ORDER BY age ASC, marks DESC;
```

This means:

1. Sort by age (smallest first)
2. Within the same age, show highest marks first

---

# ORDER BY Column Position

Instead of column names:

```sql
SELECT name, age, marks
FROM students
ORDER BY 3 DESC;
```

Here:

- 1 = name
- 2 = age
- 3 = marks

Although valid, using column names is recommended because it makes queries easier to read and maintain.

---

# ORDER BY Expressions

You can sort using calculations.

Example:

```sql
SELECT name,
       salary,
       salary * 12 AS annual_salary
FROM employees
ORDER BY annual_salary DESC;
```

---

# ORDER BY Alias

```sql
SELECT name,
       marks * 2 AS total
FROM students
ORDER BY total DESC;
```

Aliases can be used directly in `ORDER BY`.

---

# NULL Values

Suppose:

| name | marks |
|------|------|
| Rahul |85|
| Priya |NULL|
| Anjali |90|

Ascending:

```sql
SELECT *
FROM students
ORDER BY marks ASC;
```

Typically, `NULL` values appear **first**.

Descending:

```sql
SELECT *
FROM students
ORDER BY marks DESC;
```

Typically, `NULL` values appear **last**.

---

# ORDER BY with LIMIT

Find the highest-scoring student:

```sql
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 1;
```

Result:

| name | marks |
|------|------|
| Navaneeth |95|

---

Top 3 students:

```sql
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 3;
```

---

Lowest 5 salaries:

```sql
SELECT *
FROM employees
ORDER BY salary ASC
LIMIT 5;
```

---

# ORDER BY with WHERE

Example:

```sql
SELECT *
FROM students
WHERE age >= 20
ORDER BY marks DESC;
```

Execution order:

1. Filter rows using `WHERE`
2. Sort the filtered rows using `ORDER BY`

---

# ORDER BY with GROUP BY

```sql
SELECT department,
       AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

Departments are sorted by their average salary.

---

# ORDER BY with JOIN

```sql
SELECT c.name,
       o.total
FROM customers c
JOIN orders o
ON c.id = o.customer_id
ORDER BY o.total DESC;
```

Customers are listed by their order amount.

---

# Real-World Examples

## Example 1: Latest Orders

```sql
SELECT *
FROM orders
ORDER BY order_date DESC;
```

---

## Example 2: Cheapest Products

```sql
SELECT *
FROM products
ORDER BY price ASC;
```

---

## Example 3: Highest Paid Employees

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

---

## Example 4: Alphabetical Customer List

```sql
SELECT *
FROM customers
ORDER BY customer_name;
```

---

## Example 5: Top 10 Expensive Products

```sql
SELECT *
FROM products
ORDER BY price DESC
LIMIT 10;
```

---

# Common Mistakes

### Forgetting DESC

Wrong:

```sql
SELECT *
FROM students
ORDER BY marks;
```

If you wanted the highest marks first, this returns the lowest marks first because `ASC` is the default.

Correct:

```sql
SELECT *
FROM students
ORDER BY marks DESC;
```

---

### Ordering by a Non-Existent Column

Wrong:

```sql
SELECT *
FROM students
ORDER BY score;
```

If `score` doesn't exist, MySQL returns an error.

---

### Assuming Row Order Without ORDER BY

Never assume rows are returned in insertion order.

Always use:

```sql
ORDER BY
```

when the order matters.

---

# Best Practices

- Always use `ORDER BY` when result order is important.
- Prefer column names over column positions.
- Combine `ORDER BY` with `LIMIT` for top/bottom records.
- Use meaningful aliases when sorting calculated values.
- Keep sorting columns indexed for better performance on large tables.

---

# Interview Questions

## 1. What is `ORDER BY`?

It sorts query results in ascending or descending order.

---

## 2. What is the default sorting order?

`ASC` (Ascending)

---

## 3. Which keyword sorts highest to lowest?

```sql
DESC
```

---

## 4. Can we sort by multiple columns?

Yes.

Example:

```sql
ORDER BY age ASC, marks DESC;
```

---

## 5. Can we sort using aliases?

Yes.

---

## 6. Can `ORDER BY` be used with `LIMIT`?

Yes.

Example:

```sql
SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;
```

---

## 7. Why shouldn't we rely on insertion order?

Because SQL does not guarantee the order of rows unless `ORDER BY` is specified.

---

# Practice Exercises

### Exercise 1

Display all students alphabetically by name.

---

### Exercise 2

Show employees ordered by highest salary.

---

### Exercise 3

Display products from cheapest to most expensive.

---

### Exercise 4

Find the latest five orders.

---

### Exercise 5

Sort students by age, then by marks (highest first within the same age).

---

### Exercise 6

Display the top three highest-paid employees.

---

### Exercise 7

Sort customers alphabetically in reverse order.

---

### Exercise 8

Sort products by category, then by price (lowest first).

---

# Mini Project

Assume the following table:

## products

| product_id | name | category | price |
|------------|------|----------|------|
|101|Laptop|Electronics|65000|
|102|Mouse|Electronics|800|
|103|Shoes|Fashion|2500|
|104|Keyboard|Electronics|1500|
|105|Watch|Fashion|5000|

Write queries to:

1. Sort by price (lowest first).
2. Sort by price (highest first).
3. Sort alphabetically by product name.
4. Sort by category, then by price.
5. Display the three most expensive products.
6. Display the two cheapest products.

---

# Summary

In this lesson, you learned:

- What `ORDER BY` does
- Sorting with `ASC`
- Sorting with `DESC`
- Sorting numbers, text, and dates
- Sorting using multiple columns
- Mixing `ASC` and `DESC`
- Sorting with aliases and expressions
- Handling `NULL` values
- Using `ORDER BY` with `LIMIT`
- Using `ORDER BY` with `WHERE`, `GROUP BY`, and `JOIN`
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 21 — LIMIT**

Topics covered:

- What is `LIMIT`?
- Limiting Rows
- OFFSET
- Pagination
- LIMIT with ORDER BY
- Real-world Examples
- Practice Exercises