# Lesson 21 — LIMIT

## Learning Objectives

By the end of this lesson, you will understand:

- What `LIMIT` is
- Why `LIMIT` is useful
- How to limit the number of rows returned
- Using `OFFSET`
- Pagination with `LIMIT`
- Using `LIMIT` with `ORDER BY`
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# What is LIMIT?

`LIMIT` is used to **restrict the number of rows returned** by a query.

Instead of returning every record, MySQL returns only the number of rows you specify.

---

## Syntax

```sql
SELECT column_name
FROM table_name
LIMIT number;
```

Example:

```sql
SELECT *
FROM employees
LIMIT 5;
```

Output:

```
+----+----------+--------+
| id | name     | salary |
+----+----------+--------+
| 1  | John     | 50000  |
| 2  | Alice    | 55000  |
| 3  | Bob      | 47000  |
| 4  | David    | 60000  |
| 5  | Emma     | 65000  |
+----+----------+--------+
```

Only the first **5 rows** are returned.

---

# Why Use LIMIT?

Without `LIMIT`, MySQL returns **all matching rows**.

For large tables containing millions of records, this can:

- Slow down queries
- Consume more memory
- Transfer unnecessary data

Using `LIMIT` improves performance when only a few records are needed.

---

# Example Table

## employees

| id | name | department | salary |
|----|------|------------|--------|
|1|John|HR|45000|
|2|Alice|IT|70000|
|3|David|Sales|52000|
|4|Emma|IT|85000|
|5|Chris|Finance|61000|
|6|Sophia|HR|47000|
|7|Ryan|IT|93000|
|8|Olivia|Sales|58000|

---

# Returning the First 3 Rows

```sql
SELECT *
FROM employees
LIMIT 3;
```

Output:

```
John
Alice
David
```

---

# Returning Only One Row

```sql
SELECT *
FROM employees
LIMIT 1;
```

Output:

```
John
```

Useful when checking whether a table contains data.

---

# LIMIT with WHERE

```sql
SELECT *
FROM employees
WHERE department = 'IT'
LIMIT 2;
```

Output:

```
Alice
Emma
```

Only two IT employees are returned.

---

# LIMIT with ORDER BY

`LIMIT` becomes much more useful when combined with `ORDER BY`.

Example:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

Output:

```
Ryan
Emma
Alice
```

These are the **top 3 highest-paid employees**.

---

Another example:

```sql
SELECT *
FROM employees
ORDER BY salary ASC
LIMIT 2;
```

Output:

```
John
Sophia
```

These are the **lowest-paid employees**.

---

# What is OFFSET?

`OFFSET` tells MySQL **how many rows to skip** before returning results.

---

## Syntax

```sql
SELECT *
FROM table_name
LIMIT number OFFSET skip;
```

Example:

```sql
SELECT *
FROM employees
LIMIT 3 OFFSET 2;
```

Explanation:

Skip:

```
John
Alice
```

Return:

```
David
Emma
Chris
```

---

# Alternative OFFSET Syntax

MySQL also supports:

```sql
LIMIT offset, row_count
```

Example:

```sql
SELECT *
FROM employees
LIMIT 2,3;
```

Meaning:

Skip 2 rows

Return next 3 rows

Equivalent to:

```sql
LIMIT 3 OFFSET 2;
```

---

# Pagination

Pagination means splitting large datasets into pages.

Example:

Suppose each page shows **10 employees**.

---

## Page 1

```sql
SELECT *
FROM employees
LIMIT 10 OFFSET 0;
```

Rows:

```
1–10
```

---

## Page 2

```sql
SELECT *
FROM employees
LIMIT 10 OFFSET 10;
```

Rows:

```
11–20
```

---

## Page 3

```sql
SELECT *
FROM employees
LIMIT 10 OFFSET 20;
```

Rows:

```
21–30
```

---

## Formula

```
OFFSET = (PageNumber - 1) × RecordsPerPage
```

Example:

Page = 5

Records per page = 20

```
OFFSET = (5 - 1) × 20
OFFSET = 80
```

Query:

```sql
SELECT *
FROM employees
LIMIT 20 OFFSET 80;
```

---

# LIMIT with ORDER BY Example

Highest-paid employee:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;
```

---

Second highest-paid employee:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

---

Third highest-paid employee:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
```

---

# LIMIT with Multiple Conditions

```sql
SELECT *
FROM employees
WHERE department='IT'
ORDER BY salary DESC
LIMIT 2;
```

Returns:

Top two highest-paid IT employees.

---

# LIMIT with LIKE

```sql
SELECT *
FROM employees
WHERE name LIKE 'A%'
LIMIT 5;
```

Returns up to five employees whose names start with **A**.

---

# Real-World Examples

## Instagram Feed

Instead of loading every post:

```sql
SELECT *
FROM posts
ORDER BY created_at DESC
LIMIT 20;
```

Only the latest 20 posts are shown.

---

## Amazon Products

```sql
SELECT *
FROM products
LIMIT 30;
```

Displays the first 30 products on a page.

---

## YouTube

```sql
SELECT *
FROM videos
ORDER BY views DESC
LIMIT 10;
```

Shows the top 10 trending videos.

---

## Banking

```sql
SELECT *
FROM transactions
ORDER BY transaction_date DESC
LIMIT 5;
```

Displays the latest five transactions.

---

# Common Mistakes

## Forgetting ORDER BY

```sql
SELECT *
FROM employees
LIMIT 5;
```

The "first" five rows are not guaranteed to be in any meaningful order.

Always use:

```sql
SELECT *
FROM employees
ORDER BY id
LIMIT 5;
```

or another relevant column.

---

## Negative LIMIT

Incorrect:

```sql
LIMIT -5;
```

This is invalid.

---

## Large OFFSET Values

```sql
LIMIT 20 OFFSET 100000;
```

Very large offsets can be slow because MySQL must skip many rows first.

For very large datasets, advanced pagination techniques (like keyset pagination) are often preferred.

---

# Best Practices

- Use `LIMIT` when displaying data in applications.
- Combine `LIMIT` with `ORDER BY`.
- Use pagination for large datasets.
- Keep page sizes reasonable (10–50 rows).
- Avoid huge offsets whenever possible.

---

# Interview Questions

## 1. What is LIMIT?

It restricts the number of rows returned by a query.

---

## 2. What does OFFSET do?

It skips a specified number of rows before returning results.

---

## 3. How do you get the first 5 rows?

```sql
SELECT *
FROM table_name
LIMIT 5;
```

---

## 4. How do you get rows 11–20?

```sql
SELECT *
FROM table_name
LIMIT 10 OFFSET 10;
```

---

## 5. Why should LIMIT be used with ORDER BY?

To ensure the returned rows are in a predictable and meaningful order.

---

## 6. How do you get the highest-paid employee?

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;
```

---

# Practice Exercises

## Exercise 1

Return the first five employees.

---

## Exercise 2

Return the first three IT employees.

---

## Exercise 3

Display the top five highest salaries.

---

## Exercise 4

Display the three lowest salaries.

---

## Exercise 5

Skip the first five employees and return the next five.

---

## Exercise 6

Find the second highest-paid employee.

---

## Exercise 7

Display page 4 if each page contains 15 employees.

(Hint: Calculate the correct `OFFSET`.)

---

# Mini Project

Assume you have an **ecommerce** database with a `products` table.

Write queries to:

1. Display the latest 10 products.
2. Display the top 5 most expensive products.
3. Display page 3 with 20 products per page.
4. Display the second most expensive product.
5. Display the first 8 products in the "Electronics" category.

---

# Summary

In this lesson, you learned:

- What `LIMIT` is
- Why it improves query performance
- How to limit returned rows
- Using `OFFSET`
- Alternative `LIMIT offset, row_count` syntax
- Pagination
- `LIMIT` with `ORDER BY`
- `LIMIT` with `WHERE`
- Real-world applications
- Common mistakes
- Best practices
- Practice exercises

---

# Next Lesson

**Lesson 22 — UNION**

Topics covered:

- What is `UNION`?
- `UNION` vs `UNION ALL`
- Rules for UNION
- Combining Multiple Tables
- Real-world Examples
- Practice Exercises
```