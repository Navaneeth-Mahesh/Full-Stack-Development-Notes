# Lesson 28 — ROLLUP

## Learning Objectives

By the end of this lesson, you will understand:

- What `WITH ROLLUP` is
- Why rollups are useful
- How to generate subtotals
- How to generate grand totals
- Hierarchical grouping
- Multi-column rollups
- Using `GROUP BY` with `ROLLUP`
- Real-world reporting examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Introduction

When using `GROUP BY`, MySQL groups rows and returns one result for each group.

Sometimes we also need:

- Total sales of each category
- Total sales of each department
- Overall company sales

Instead of writing multiple queries, MySQL provides:

```sql
WITH ROLLUP
```

It automatically generates **subtotals** and a **grand total**.

---

# What is WITH ROLLUP?

`WITH ROLLUP` is an extension of the `GROUP BY` clause.

It adds extra rows that contain:

- Subtotals
- Grand total

Think of it like Excel's "Subtotal" feature.

---

# Basic Syntax

```sql
SELECT column_name,
       aggregate_function(column_name)
FROM table_name
GROUP BY column_name WITH ROLLUP;
```

Example:

```sql
SELECT department,
       SUM(salary)
FROM employees
GROUP BY department WITH ROLLUP;
```

---

# Sample Table

## employees

| id | name | department | salary |
|----|------|------------|--------|
|1|Alice|HR|30000|
|2|Bob|HR|35000|
|3|Charlie|IT|50000|
|4|David|IT|45000|
|5|Eva|Sales|40000|

---

# Without ROLLUP

```sql
SELECT department,
       SUM(salary)
FROM employees
GROUP BY department;
```

Result:

| department | SUM(salary) |
|------------|------------:|
|HR|65000|
|IT|95000|
|Sales|40000|

---

# With ROLLUP

```sql
SELECT department,
       SUM(salary)
FROM employees
GROUP BY department WITH ROLLUP;
```

Result:

| department | SUM(salary) |
|------------|------------:|
|HR|65000|
|IT|95000|
|Sales|40000|
|NULL|200000|

The last row is the **grand total**.

---

# Why is NULL Displayed?

During rollup, MySQL uses `NULL` to represent:

> "This row is the total of all groups."

It does **not** mean the department is unknown.

---

# Replacing NULL with a Label

Use `IFNULL()` or `COALESCE()`.

```sql
SELECT
    IFNULL(department,'Grand Total') AS Department,
    SUM(salary) AS TotalSalary
FROM employees
GROUP BY department WITH ROLLUP;
```

Result:

| Department | TotalSalary |
|------------|------------:|
|HR|65000|
|IT|95000|
|Sales|40000|
|Grand Total|200000|

This makes reports easier to read.

---

# Multi-Level ROLLUP

ROLLUP becomes more powerful when grouping by multiple columns.

Suppose we have:

## sales

| region | city | amount |
|---------|------|-------:|
|North|Delhi|1000|
|North|Delhi|2000|
|North|Jaipur|1500|
|South|Chennai|3000|
|South|Bangalore|2500|

Query:

```sql
SELECT region,
       city,
       SUM(amount)
FROM sales
GROUP BY region, city WITH ROLLUP;
```

---

# Result

| region | city | SUM(amount) |
|--------|------|------------:|
|North|Delhi|3000|
|North|Jaipur|1500|
|North|NULL|4500|
|South|Bangalore|2500|
|South|Chennai|3000|
|South|NULL|5500|
|NULL|NULL|10000|

Notice:

- `North NULL` → subtotal for North
- `South NULL` → subtotal for South
- `NULL NULL` → grand total

---

# Understanding Hierarchical Grouping

ROLLUP follows the order of the columns in `GROUP BY`.

```sql
GROUP BY region, city WITH ROLLUP
```

Hierarchy:

```
Region
   ├── City
   ├── City
   └── Region Total

Grand Total
```

If you reverse the order:

```sql
GROUP BY city, region WITH ROLLUP;
```

The subtotals will be calculated by city first.

The order of columns matters.

---

# Practical Example 1 – Online Store

Orders table:

| category | product | amount |
|----------|---------|-------:|
|Electronics|Laptop|50000|
|Electronics|Phone|30000|
|Furniture|Chair|7000|
|Furniture|Table|15000|

Query:

```sql
SELECT category,
       product,
       SUM(amount)
FROM orders
GROUP BY category, product WITH ROLLUP;
```

Result:

| Category | Product | Total |
|-----------|---------|------:|
|Electronics|Laptop|50000|
|Electronics|Phone|30000|
|Electronics|NULL|80000|
|Furniture|Chair|7000|
|Furniture|Table|15000|
|Furniture|NULL|22000|
|NULL|NULL|102000|

---

# Practical Example 2 – College

Marks table:

| department | semester | marks |
|------------|----------|------:|
|CSE|1|400|
|CSE|2|450|
|ECE|1|420|
|ECE|2|430|

Query:

```sql
SELECT department,
       semester,
       SUM(marks)
FROM marks
GROUP BY department, semester WITH ROLLUP;
```

Result:

- Semester totals
- Department totals
- College total

---

# Aggregate Functions with ROLLUP

ROLLUP works with any aggregate function.

## SUM()

```sql
SELECT department,
       SUM(salary)
FROM employees
GROUP BY department WITH ROLLUP;
```

---

## COUNT()

```sql
SELECT department,
       COUNT(*)
FROM employees
GROUP BY department WITH ROLLUP;
```

---

## AVG()

```sql
SELECT department,
       AVG(salary)
FROM employees
GROUP BY department WITH ROLLUP;
```

---

## MAX()

```sql
SELECT department,
       MAX(salary)
FROM employees
GROUP BY department WITH ROLLUP;
```

---

## MIN()

```sql
SELECT department,
       MIN(salary)
FROM employees
GROUP BY department WITH ROLLUP;
```

---

# Real-World Uses

## Sales Reports

- Sales per category
- Category subtotal
- Company total

---

## Finance

- Expenses per department
- Department totals
- Annual total

---

## Schools

- Marks per class
- Class total
- School total

---

## Hospitals

- Patients per ward
- Ward total
- Hospital total

---

## Inventory

- Products by category
- Category totals
- Overall stock

---

# Combining WHERE with ROLLUP

```sql
SELECT department,
       SUM(salary)
FROM employees
WHERE salary > 30000
GROUP BY department WITH ROLLUP;
```

Filtering happens **before** grouping.

---

# Combining HAVING with ROLLUP

```sql
SELECT department,
       SUM(salary)
FROM employees
GROUP BY department WITH ROLLUP
HAVING SUM(salary) > 50000;
```

`HAVING` filters grouped results.

Be aware that it can also remove subtotal or grand total rows if they don't meet the condition.

---

# Common Mistakes

## Mistake 1

Forgetting `GROUP BY`.

Wrong:

```sql
SELECT SUM(salary)
WITH ROLLUP;
```

Correct:

```sql
SELECT department,
       SUM(salary)
FROM employees
GROUP BY department WITH ROLLUP;
```

---

## Mistake 2

Thinking `NULL` means missing data.

In rollup output, `NULL` usually indicates a subtotal or grand total row.

---

## Mistake 3

Ignoring column order.

```sql
GROUP BY city, region
```

produces different subtotals than

```sql
GROUP BY region, city
```

---

# Best Practices

- Use `WITH ROLLUP` for reports.
- Replace `NULL` with descriptive labels.
- Use meaningful column order.
- Combine with aggregate functions.
- Test reports with sample data before using them in production.

---

# Interview Questions

## 1. What is `WITH ROLLUP`?

It extends `GROUP BY` to generate subtotals and a grand total automatically.

---

## 2. Which clause is used with `ROLLUP`?

`GROUP BY`

---

## 3. Why does `ROLLUP` return `NULL`?

`NULL` represents subtotal or grand total rows.

---

## 4. Can `ROLLUP` work with multiple columns?

Yes. It creates hierarchical subtotals based on the order of grouped columns.

---

## 5. Does column order matter in `ROLLUP`?

Yes. The order determines how subtotals are calculated.

---

# Practice Exercises

## Exercise 1

Find the total salary for each department along with the grand total.

---

## Exercise 2

Display the number of employees in each department and the overall employee count.

---

## Exercise 3

Calculate average salary by department with a grand average row.

---

## Exercise 4

Create a `sales` table with:

- region
- city
- amount

Use `ROLLUP` to generate:

- City totals
- Region totals
- Grand total

---

## Exercise 5

Replace `NULL` values in the rollup output with:

```
Grand Total
```

using `IFNULL()` or `COALESCE()`.

---

# Mini Project

Create an `orders` table:

| category | product | amount |
|----------|---------|-------:|
|Electronics|Laptop|50000|
|Electronics|Phone|30000|
|Furniture|Chair|7000|
|Furniture|Table|15000|
|Books|SQL Guide|1200|

Tasks:

1. Show total sales for each product.
2. Show subtotal for each category.
3. Show the grand total.
4. Replace `NULL` with readable labels.
5. Try changing the order of columns in `GROUP BY` and observe how the output changes.

---

# Summary

In this lesson, you learned:

- What `WITH ROLLUP` is
- How it extends `GROUP BY`
- How to generate subtotals
- How to generate grand totals
- Why `NULL` appears in rollup rows
- How to replace `NULL` with labels
- Hierarchical grouping with multiple columns
- Practical reporting examples
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 29 — ON DELETE**

Topics covered:

- Foreign key actions
- `ON DELETE CASCADE`
- `ON DELETE SET NULL`
- `ON DELETE RESTRICT`
- `ON DELETE NO ACTION`
- Practical parent-child relationship examples