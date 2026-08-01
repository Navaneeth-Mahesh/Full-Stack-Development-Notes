# Lesson 25 — Indexes in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What an Index is
- Why Indexes improve query performance
- How MySQL searches data with and without indexes
- Creating Indexes
- Unique Indexes
- Composite (Multi-column) Indexes
- Viewing existing Indexes
- Dropping Indexes
- Query Optimization using EXPLAIN
- Advantages and disadvantages
- Best practices
- Interview questions
- Practice exercises

---

# What is an Index?

An **Index** is a special data structure that helps MySQL locate rows much faster without scanning the entire table.

Think of an index in a database like the index at the back of a textbook.

Instead of reading every page to find "Normalization", you check the index, which tells you the exact page number.

Similarly, MySQL uses indexes to quickly locate matching rows.

---

# Why Do We Need Indexes?

Imagine a table with:

```
Customers
```

containing

```
10 rows
```

Searching is very fast.

Now imagine:

```
50 Million rows
```

Searching every row becomes extremely slow.

Indexes solve this problem.

---

# Without an Index

Suppose we execute:

```sql
SELECT * FROM customers
WHERE email = 'john@gmail.com';
```

If `email` is not indexed:

```
Customer Table

↓

Row 1 ❌

↓

Row 2 ❌

↓

Row 3 ❌

↓

...

↓

Row 50,000,000 ✅
```

MySQL checks every row.

This is called a **Full Table Scan**.

Time Complexity (simplified):

```
O(n)
```

---

# With an Index

If `email` has an index:

```
Customer Table

↓

Email Index

↓

john@gmail.com

↓

Directly locate matching row
```

MySQL jumps directly to the required data.

Time Complexity (simplified):

```
O(log n)
```

Much faster.

---

# Real-Life Analogy

Imagine a dictionary.

Without an index:

You start at page 1 and read every page.

With an index:

You immediately open the correct page.

That's exactly how database indexes work.

---

# Where are Indexes Used?

Indexes are commonly created on:

- Primary Keys
- Foreign Keys
- Email
- Username
- Phone Number
- Product Code
- Order Number

Basically, columns frequently used in:

- WHERE
- JOIN
- ORDER BY
- GROUP BY

---

# Sample Table

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    email VARCHAR(100)
);
```

---

# Searching Without an Index

```sql
SELECT *
FROM employees
WHERE email = 'alice@gmail.com';
```

MySQL checks every row.

Slow for millions of records.

---

# Creating an Index

Syntax

```sql
CREATE INDEX index_name
ON table_name(column_name);
```

Example

```sql
CREATE INDEX idx_email
ON employees(email);
```

Now searching by email becomes much faster.

---

# Another Example

```sql
CREATE INDEX idx_department
ON employees(department);
```

Useful when department is frequently searched.

Example:

```sql
SELECT *
FROM employees
WHERE department = 'HR';
```

---

# Viewing Existing Indexes

Syntax

```sql
SHOW INDEXES
FROM employees;
```

Output

```
PRIMARY

idx_email

idx_department
```

Shows:

- Index name
- Column
- Type
- Cardinality
- Unique or Not

---

# Unique Index

A **Unique Index** ensures duplicate values cannot exist.

Example

```sql
CREATE UNIQUE INDEX idx_unique_email
ON employees(email);
```

Now:

```
alice@gmail.com
```

cannot appear twice.

Trying:

```sql
INSERT INTO employees(first_name,email)
VALUES('Bob','alice@gmail.com');
```

Produces:

```
Duplicate entry
```

---

# Difference Between UNIQUE and UNIQUE INDEX

Both prevent duplicates.

Example:

```sql
email VARCHAR(100) UNIQUE
```

creates a unique index automatically.

Or manually:

```sql
CREATE UNIQUE INDEX idx_email
ON employees(email);
```

Both achieve the same goal.

---

# Composite Index

A composite index contains multiple columns.

Syntax

```sql
CREATE INDEX index_name
ON table(col1, col2);
```

Example

```sql
CREATE INDEX idx_name
ON employees(last_name, first_name);
```

Now queries like:

```sql
SELECT *
FROM employees
WHERE last_name='Smith'
AND first_name='John';
```

become faster.

---

# Order Matters

Suppose:

```sql
CREATE INDEX idx_name
ON employees(last_name, first_name);
```

Efficient:

```sql
WHERE last_name='Smith'
```

Efficient:

```sql
WHERE last_name='Smith'
AND first_name='John'
```

Less efficient:

```sql
WHERE first_name='John'
```

Because indexes are used from left to right.

---

# Multiple Indexes

You can create several indexes.

```sql
CREATE INDEX idx_salary
ON employees(salary);

CREATE INDEX idx_department
ON employees(department);

CREATE INDEX idx_lastname
ON employees(last_name);
```

Each helps different queries.

---

# Dropping an Index

Syntax

```sql
DROP INDEX index_name
ON table_name;
```

Example

```sql
DROP INDEX idx_department
ON employees;
```

The table remains.

Only the index is removed.

---

# Primary Key Index

Every Primary Key automatically has an index.

Example

```sql
emp_id INT PRIMARY KEY
```

MySQL creates an index automatically.

No need to create another.

---

# Foreign Key Index

Many storage engines automatically create indexes for foreign keys because joins depend on them.

---

# Query Optimization

Suppose:

```sql
SELECT *
FROM employees
WHERE email='alice@gmail.com';
```

How do we know if MySQL is using an index?

Use:

```sql
EXPLAIN
SELECT *
FROM employees
WHERE email='alice@gmail.com';
```

Output may show:

```
type = ref

key = idx_email
```

Meaning:

MySQL is using the email index.

---

# Reading EXPLAIN (Basics)

Example

```
id      1

table   employees

type    ref

key     idx_email

rows    1
```

Important columns:

| Column | Meaning |
|---------|----------|
| type | Search method used |
| key | Index being used |
| rows | Estimated rows scanned |
| Extra | Additional information |

Lower `rows` generally means better performance.

---

# When Should You Create Indexes?

Good candidates:

Frequently searched columns.

```sql
WHERE email
```

Frequently joined columns.

```sql
customer_id
```

Frequently sorted columns.

```sql
ORDER BY salary
```

Frequently grouped columns.

```sql
GROUP BY department
```

---

# When NOT to Create Indexes

Avoid indexing:

- Very small tables
- Columns rarely searched
- Columns with frequent updates
- Columns with very few distinct values

Example:

```
gender

Yes/No

Active/Inactive
```

Usually not useful.

---

# Advantages

- Faster SELECT queries
- Faster searching
- Faster JOIN operations
- Faster ORDER BY
- Faster GROUP BY
- Better scalability

---

# Disadvantages

Indexes also have costs.

- Extra disk space
- Slower INSERT
- Slower UPDATE
- Slower DELETE
- Maintenance overhead

Every time data changes, indexes must also be updated.

---

# Real-World Example

Imagine Amazon.

Products Table

```
5 Crore Products
```

User searches:

```
iPhone 16
```

Without index:

Search every product.

With index:

Jump directly to matching products.

Search completes in milliseconds.

---

# Best Practices

- Index columns used in WHERE
- Index foreign keys
- Avoid unnecessary indexes
- Don't duplicate indexes
- Use composite indexes carefully
- Monitor slow queries
- Use EXPLAIN before optimizing

---

# Common Mistakes

## Creating Too Many Indexes

Bad.

Every INSERT becomes slower.

---

## Indexing Every Column

Not recommended.

Only index columns that improve queries.

---

## Duplicate Indexes

Wrong

```sql
CREATE INDEX idx_email
ON employees(email);

CREATE INDEX another_email
ON employees(email);
```

Waste of space.

---

## Ignoring Composite Order

```sql
(last_name, first_name)
```

is different from

```sql
(first_name, last_name)
```

Choose the order based on your queries.

---

# Interview Questions

## 1. What is an Index?

A data structure that speeds up data retrieval.

---

## 2. Does an Index store data?

No.

It stores references to table rows.

---

## 3. Why are indexes faster?

They avoid scanning every row.

---

## 4. Which commands create an index?

```sql
CREATE INDEX
```

---

## 5. Which command removes an index?

```sql
DROP INDEX
```

---

## 6. What is a Composite Index?

An index created on multiple columns.

---

## 7. What is a Unique Index?

An index that prevents duplicate values.

---

## 8. Which SQL command checks if an index is being used?

```sql
EXPLAIN
```

---

## 9. Can too many indexes hurt performance?

Yes.

They slow down INSERT, UPDATE, and DELETE operations.

---

## 10. Does a Primary Key have an index?

Yes.

Automatically.

---

# Practice Exercises

## Exercise 1

Create a table.

```sql
CREATE TABLE students(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(100),
    branch VARCHAR(50)
);
```

---

## Exercise 2

Create an index on `email`.

---

## Exercise 3

Create an index on `branch`.

---

## Exercise 4

Show all indexes.

---

## Exercise 5

Create a unique index on `email`.

---

## Exercise 6

Create a composite index on:

```
branch

name
```

---

## Exercise 7

Use `EXPLAIN` to check whether MySQL uses the email index.

---

## Exercise 8

Drop the branch index.

---

# Mini Project

Imagine you're designing a **College Management System**.

Create a table:

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    roll_no VARCHAR(20),
    email VARCHAR(100),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    cgpa DECIMAL(3,2)
);
```

Tasks:

1. Create a **Unique Index** on `roll_no`.
2. Create a **Unique Index** on `email`.
3. Create a normal index on `department`.
4. Create a **Composite Index** on `(last_name, first_name)`.
5. Run `SHOW INDEXES FROM students;`.
6. Use `EXPLAIN` on a query that searches by `email`.
7. Drop the department index.

---

# Summary

In this lesson, you learned:

- What an Index is
- How indexes improve search performance
- Full Table Scan vs Indexed Search
- Creating indexes
- Viewing indexes
- Unique indexes
- Composite indexes
- Automatic indexes (Primary & Foreign Keys)
- Query optimization with `EXPLAIN`
- Advantages and disadvantages
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 26 — Subqueries**

Topics covered:

- What is a Subquery?
- Single-row Subqueries
- Multi-row Subqueries
- Correlated Subqueries
- Subqueries with SELECT
- Subqueries with WHERE
- Subqueries with FROM
- EXISTS and NOT EXISTS
- Real-world examples
- Performance considerations