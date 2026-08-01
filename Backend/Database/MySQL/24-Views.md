# Lesson 24 — Views in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What a View is
- Why Views are used
- Creating Views
- Querying Views
- Updating data through Views
- Replacing and Dropping Views
- Advantages and Limitations
- Security benefits
- Real-world use cases
- Interview questions
- Practice exercises

---

# What is a View?

A **View** is a **virtual table** created from the result of one or more SQL queries.

Unlike a normal table, a View **does not store data itself** (except in some database systems with materialized views—MySQL Views are virtual).

Instead, whenever you query a View, MySQL executes the underlying SQL query and returns the latest data.

Think of a View as a **saved SQL query**.

---

# Why Use Views?

Suppose you frequently run this query:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Engineering';
```

Instead of writing it every time, create a View:

```sql
CREATE VIEW engineering_employees AS
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Engineering';
```

Now simply use:

```sql
SELECT * FROM engineering_employees;
```

This makes your SQL cleaner, reusable, and easier to maintain.

---

# Real-World Example

Imagine an e-commerce database.

Tables:

```
users
products
orders
payments
```

The manager only needs:

- Customer Name
- Product Name
- Order Date

Instead of writing a long JOIN every time, create a View.

```
order_summary
```

Now everyone can query:

```sql
SELECT * FROM order_summary;
```

---

# How Views Work

```
Users
      │
      ▼
+-------------------------+
|        VIEW             |
+-------------------------+
      │
      ▼
SELECT Query
      │
      ▼
Actual Tables
```

The View stores only the SQL query, not the data.

---

# Basic Syntax

```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name;
```

Example:

```sql
CREATE VIEW student_names AS
SELECT id, name
FROM students;
```

---

# Viewing Data

Query the View just like a table.

```sql
SELECT * FROM student_names;
```

Output

```
+----+----------+
| id | name     |
+----+----------+
| 1  | Navaneeth|
| 2  | Rahul    |
+----+----------+
```

---

# Example Database

Students

| id | name | age | branch |
|----|------|-----|---------|
|1|Navaneeth|20|CSE|
|2|Rahul|21|ECE|
|3|Sneha|19|IT|

Create a View:

```sql
CREATE VIEW basic_students AS
SELECT id, name
FROM students;
```

Query:

```sql
SELECT * FROM basic_students;
```

Output

| id | name |
|----|------|
|1|Navaneeth|
|2|Rahul|
|3|Sneha|

---

# Views with WHERE

```sql
CREATE VIEW cse_students AS
SELECT *
FROM students
WHERE branch='CSE';
```

Query:

```sql
SELECT * FROM cse_students;
```

Only CSE students are displayed.

---

# Views with Calculated Columns

Suppose employees table:

| id | salary |
|----|---------|
|1|50000|
|2|70000|

Create:

```sql
CREATE VIEW employee_bonus AS
SELECT
name,
salary,
salary * 0.10 AS bonus
FROM employees;
```

Query:

```sql
SELECT * FROM employee_bonus;
```

Output

| Name | Salary | Bonus |
|------|---------|--------|
|John|50000|5000|
|Alice|70000|7000|

---

# Views with JOIN

Tables:

Customers

| id | name |
|----|------|
|1|Navaneeth|

Orders

| id | customer_id | amount |
|----|-------------|--------|
|1|1|1200|

Create:

```sql
CREATE VIEW customer_orders AS
SELECT
customers.name,
orders.amount
FROM customers
JOIN orders
ON customers.id = orders.customer_id;
```

Query:

```sql
SELECT * FROM customer_orders;
```

Output

| Name | Amount |
|------|---------|
|Navaneeth|1200|

---

# Updating a View

Many Views are **updatable**.

Example:

```sql
CREATE VIEW student_view AS
SELECT id, name
FROM students;
```

Update:

```sql
UPDATE student_view
SET name='Arjun'
WHERE id=1;
```

This updates the original table.

Students table:

Before

|1|Navaneeth|

After

|1|Arjun|

---

# When Views Cannot Be Updated

A View is generally **not updatable** if it contains:

- GROUP BY
- DISTINCT
- Aggregate functions (SUM, COUNT, AVG, etc.)
- UNION
- Subqueries in the SELECT list
- Multiple tables in certain joins

Example:

```sql
CREATE VIEW total_sales AS
SELECT
customer_id,
SUM(amount)
FROM orders
GROUP BY customer_id;
```

Trying to update:

```sql
UPDATE total_sales
SET customer_id = 10;
```

Error.

---

# Inserting Through a View

If the View is simple:

```sql
INSERT INTO student_view(name)
VALUES ('Rahul');
```

This inserts into the original table.

---

# Replacing a View

Instead of dropping and creating again:

```sql
CREATE OR REPLACE VIEW student_view AS
SELECT
id,
name,
branch
FROM students;
```

The old View is replaced.

---

# Viewing Existing Views

```sql
SHOW FULL TABLES
WHERE TABLE_TYPE='VIEW';
```

Example Output

```
student_view

customer_orders

employee_bonus
```

---

# Showing View Definition

```sql
SHOW CREATE VIEW student_view;
```

Output:

```sql
CREATE VIEW student_view AS
SELECT ...
```

Useful for reviewing or debugging the View definition.

---

# Dropping a View

Syntax:

```sql
DROP VIEW view_name;
```

Example:

```sql
DROP VIEW student_view;
```

The View is deleted, but the original table remains unchanged.

---

# Difference Between Table and View

| Feature | Table | View |
|----------|-------|------|
|Stores Data|Yes|No (virtual)|
|Can Insert Data|Yes|Sometimes|
|Can Update Data|Yes|Sometimes|
|Consumes Storage|Yes|Very little (definition only)|
|Built from Query|No|Yes|
|Depends on Table|No|Yes|

---

# Advantages of Views

- Simplifies complex queries
- Reusable SQL logic
- Improves readability
- Hides unnecessary columns
- Restricts data access
- Provides abstraction
- Always shows the latest data
- Easier reporting

---

# Limitations of Views

- Some Views are not updatable
- Slight overhead for complex queries
- Depends on underlying tables
- Dropping a base table breaks the View
- Not a replacement for proper indexing

---

# Security Benefit

Suppose the employees table contains:

| Name | Salary | Password |
|------|---------|----------|

HR should not see passwords.

Create a View:

```sql
CREATE VIEW employee_public AS
SELECT
name,
salary
FROM employees;
```

Now HR accesses only the View:

```sql
SELECT * FROM employee_public;
```

Sensitive columns remain hidden.

---

# Real-World Use Cases

## Banking

Create a View showing only customer balances.

---

## E-commerce

Order summary for managers.

---

## Hospital

Doctor schedule without exposing patient records.

---

## School

Student results for teachers.

---

## Dashboard

Business intelligence dashboards often read from Views instead of raw tables.

---

# Best Practices

- Give Views meaningful names
- Keep Views simple
- Avoid nesting too many Views
- Use Views to improve security
- Don't assume every View is updatable
- Use `CREATE OR REPLACE VIEW` when modifying
- Document complex Views

---

# Common Mistakes

### Forgetting `AS`

Wrong

```sql
CREATE VIEW students
SELECT * FROM students;
```

Correct

```sql
CREATE VIEW students_view AS
SELECT * FROM students;
```

---

### Thinking a View Stores Data

A View stores only the query definition.

---

### Updating Non-Updatable Views

Views using `GROUP BY`, `DISTINCT`, or aggregate functions usually cannot be updated.

---

### Dropping the Base Table

If the original table is dropped:

```sql
DROP TABLE students;
```

The View becomes invalid.

---

# Interview Questions

### 1. What is a View?

A View is a virtual table created from a SQL query.

---

### 2. Does a View store data?

No. It stores only the query definition.

---

### 3. Can a View be updated?

Some simple Views can. Complex Views often cannot.

---

### 4. Which command creates a View?

```sql
CREATE VIEW view_name AS
SELECT ...
```

---

### 5. How do you remove a View?

```sql
DROP VIEW view_name;
```

---

### 6. Why are Views useful?

They simplify queries, improve security, and promote code reuse.

---

### 7. What is `CREATE OR REPLACE VIEW`?

It replaces an existing View with a new definition without dropping it manually.

---

# Practice Exercises

## Exercise 1

Create a database:

```sql
college_db
```

---

## Exercise 2

Create a table:

```sql
students
```

with:

- id
- name
- age
- branch

Insert at least five records.

---

## Exercise 3

Create a View showing only:

- id
- name

---

## Exercise 4

Create a View showing only CSE students.

---

## Exercise 5

Create a View with a calculated column:

```
salary + 5000 AS revised_salary
```

(using an employees table).

---

## Exercise 6

Create two related tables:

- customers
- orders

Create a JOIN View displaying:

- Customer Name
- Order Amount

---

## Exercise 7

Display all Views in the current database.

---

## Exercise 8

Show the SQL definition of one View.

---

## Exercise 9

Replace a View using:

```sql
CREATE OR REPLACE VIEW
```

---

## Exercise 10

Drop a View.

---

# Mini Project

Create an **Online Store Dashboard**.

Tables:

```
customers
products
orders
payments
```

Create these Views:

1. `customer_orders`
2. `high_value_orders`
3. `product_prices`
4. `recent_orders`
5. `payment_summary`

Query each View to verify the results.

---

# Summary

In this lesson, you learned:

- What a View is
- Why Views are useful
- Creating Views
- Querying Views
- Updating Views
- Replacing Views
- Dropping Views
- Updatable vs Non-Updatable Views
- Security benefits
- Real-world use cases
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 25 — Indexes**

Topics covered:

- What is an Index?
- Why Indexes improve performance
- Creating Indexes
- Unique Indexes
- Composite Indexes
- Dropping Indexes
- Advantages and disadvantages
- Query optimization
- Real-world examples