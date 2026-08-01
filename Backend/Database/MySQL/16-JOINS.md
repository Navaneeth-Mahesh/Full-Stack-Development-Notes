# Lesson 16 — JOINS in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What a JOIN is
- Why JOINs are important
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- CROSS JOIN
- Joining multiple tables
- Table Aliases
- Real-world examples
- Performance tips
- Common mistakes
- Interview questions
- Practice exercises

---

# What is a JOIN?

A **JOIN** combines rows from **two or more tables** based on a related column.

Imagine you're building an e-commerce application.

Instead of storing everything in one huge table, databases separate data into related tables.

Example:

Users Table

| user_id | name |
|---------|------|
|1|Navaneeth|
|2|Rahul|
|3|Anjali|

Orders Table

| order_id | user_id | product |
|----------|---------|---------|
|101|1|Laptop|
|102|1|Mouse|
|103|2|Keyboard|

Notice:

The `user_id` exists in both tables.

This allows MySQL to connect them.

---

# Why Do We Need JOINs?

Without JOINs, we'd have duplicate information.

Bad Design

|Order ID|Customer Name|Product|
|---------|-------------|-------|
|101|Navaneeth|Laptop|
|102|Navaneeth|Mouse|

Customer name is repeated.

Better Design

Users

|ID|Name|
|--|----|
|1|Navaneeth|

Orders

|Order|UserID|Product|
|-----|------|-------|
|101|1|Laptop|

JOIN combines them whenever needed.

---

# Types of JOINs

MySQL supports:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- CROSS JOIN

Visual representation:

```
INNER JOIN
Only Matching Records

LEFT JOIN
All Left + Matching Right

RIGHT JOIN
All Right + Matching Left

CROSS JOIN
Every Possible Combination
```

---

# Sample Database

## Customers

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

Insert Data

```sql
INSERT INTO customers VALUES
(1,'Navaneeth'),
(2,'Rahul'),
(3,'Anjali'),
(4,'John');
```

---

## Orders

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50)
);
```

Insert Data

```sql
INSERT INTO orders VALUES
(101,1,'Laptop'),
(102,1,'Mouse'),
(103,2,'Keyboard'),
(104,5,'Phone');
```

Notice:

Customer 5 doesn't exist.

Customer 3 and 4 have no orders.

---

# INNER JOIN

Returns only matching records.

Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

Example

```sql
SELECT *
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

Output

|Customer|Order|Product|
|---------|------|-------|
|Navaneeth|101|Laptop|
|Navaneeth|102|Mouse|
|Rahul|103|Keyboard|

Customer 3 → Not shown

Customer 4 → Not shown

Order 104 → Not shown

Because they don't match.

---

# INNER JOIN with Selected Columns

Instead of:

```sql
SELECT *
```

Use:

```sql
SELECT
customers.name,
orders.product
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

Output

|Name|Product|
|----|--------|
|Navaneeth|Laptop|
|Navaneeth|Mouse|
|Rahul|Keyboard|

---

# LEFT JOIN

Returns:

- Every row from LEFT table
- Matching rows from RIGHT table

If no match:

NULL is returned.

Syntax

```sql
SELECT *
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
```

Output

|Customer|Product|
|---------|-------|
|Navaneeth|Laptop|
|Navaneeth|Mouse|
|Rahul|Keyboard|
|Anjali|NULL|
|John|NULL|

Customers with no orders are still shown.

---

# RIGHT JOIN

Returns:

- Every row from RIGHT table
- Matching rows from LEFT table

```sql
SELECT *
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;
```

Output

|Customer|Product|
|---------|-------|
|Navaneeth|Laptop|
|Navaneeth|Mouse|
|Rahul|Keyboard|
|NULL|Phone|

Customer doesn't exist.

So NULL appears.

---

# CROSS JOIN

Returns every possible combination.

Formula

```
Rows in A × Rows in B
```

Example

4 Customers

×

4 Orders

=

16 Rows

Query

```sql
SELECT *
FROM customers
CROSS JOIN orders;
```

Useful for:

- Product variations
- Calendar generation
- Seating arrangements
- Testing

---

# JOIN Comparison

Suppose

Customers

```
1
2
3
```

Orders

```
1
2
4
```

INNER JOIN

```
1
2
```

LEFT JOIN

```
1
2
3
```

RIGHT JOIN

```
1
2
4
```

CROSS JOIN

```
1×1
1×2
1×4
2×1
...
```

Every combination.

---

# Joining Multiple Tables

Example

Customers

↓

Orders

↓

Payments

Payments Table

```sql
CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10,2)
);
```

Query

```sql
SELECT
customers.name,
orders.product,
payments.amount
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id
JOIN payments
ON orders.order_id = payments.order_id;
```

You can join as many tables as needed.

---

# Table Aliases

Aliases make queries shorter.

Instead of

```sql
SELECT customers.name
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

Use

```sql
SELECT c.name,
o.product
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

Much cleaner.

---

# Aliases with AS

```sql
SELECT
c.name AS Customer,
o.product AS Product
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

Output

|Customer|Product|
|---------|-------|
|Navaneeth|Laptop|

---

# Real-World Example

Food Delivery App

Tables

```
Users

Restaurants

Orders

Payments

Drivers
```

Query

```sql
SELECT
u.name,
r.restaurant_name,
o.total_amount,
p.payment_method,
d.driver_name
FROM users u
JOIN orders o
ON u.user_id=o.user_id
JOIN restaurants r
ON o.restaurant_id=r.restaurant_id
JOIN payments p
ON o.order_id=p.order_id
JOIN drivers d
ON o.driver_id=d.driver_id;
```

One query retrieves data from five tables.

---

# Filtering JOIN Results

```sql
SELECT
c.name,
o.product
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
WHERE o.product='Laptop';
```

---

# Ordering Results

```sql
SELECT
c.name,
o.product
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
ORDER BY c.name;
```

---

# Counting Orders

```sql
SELECT
customers.name,
COUNT(orders.order_id) AS total_orders
FROM customers
LEFT JOIN orders
ON customers.customer_id=orders.customer_id
GROUP BY customers.name;
```

Output

|Name|Orders|
|----|------|
|Navaneeth|2|
|Rahul|1|
|Anjali|0|
|John|0|

---

# Performance Tips

## 1. Join Using Indexed Columns

Good

```sql
customer_id
```

Bad

```sql
name
```

Indexes make joins much faster.

---

## 2. Avoid SELECT *

Instead of

```sql
SELECT *
```

Use

```sql
SELECT name, product
```

Only fetch the columns you need.

---

## 3. Filter Early

```sql
WHERE status='Completed'
```

before processing unnecessary rows.

---

## 4. Use Primary Keys and Foreign Keys

Primary Keys uniquely identify rows.

Foreign Keys create relationships.

JOINs work best with these.

---

# Common Mistakes

### Forgetting ON

Wrong

```sql
SELECT *
FROM customers
JOIN orders;
```

Always specify:

```sql
ON customers.customer_id = orders.customer_id
```

---

### Joining Wrong Columns

Wrong

```sql
customers.name = orders.product
```

Correct

```sql
customer_id = customer_id
```

---

### Using CROSS JOIN Accidentally

Missing `ON` in some joins can produce a huge number of rows.

Always verify your JOIN conditions.

---

# Best Practices

- Use meaningful aliases (`c`, `o`, `p`).
- Prefer `INNER JOIN` when only matching data is required.
- Use `LEFT JOIN` to include records with no matches.
- Join on indexed columns whenever possible.
- Avoid `SELECT *` in production.
- Keep JOIN conditions simple and clear.

---

# Interview Questions

### 1. What is a JOIN?

A JOIN combines data from multiple tables based on a related column.

---

### 2. Difference between INNER JOIN and LEFT JOIN?

INNER JOIN returns only matching rows.

LEFT JOIN returns all rows from the left table and matching rows from the right table.

---

### 3. What happens if no match exists in a LEFT JOIN?

The columns from the right table contain `NULL`.

---

### 4. What does CROSS JOIN do?

Returns every possible combination of rows from both tables.

---

### 5. Why are aliases used?

To make queries shorter, cleaner, and easier to read.

---

# Practice Exercises

### Exercise 1

Create `students` and `courses` tables.

Join them using `student_id`.

---

### Exercise 2

Display all customers with their orders.

---

### Exercise 3

Display customers who have not placed any orders.

(Hint: Use `LEFT JOIN` and check for `NULL`.)

---

### Exercise 4

Display all orders even if the customer doesn't exist.

(Hint: Use `RIGHT JOIN`.)

---

### Exercise 5

Create `payments` table and join:

- Customers
- Orders
- Payments

Display:

- Customer Name
- Product
- Payment Amount

---

# Mini Project

Create an Online Shopping Database with:

Tables:

- customers
- products
- orders
- order_items
- payments

Write queries to:

1. Show customer names with products purchased.
2. Show customers who haven't placed any orders.
3. Show all payments with customer names.
4. Count total orders per customer.
5. Display the highest payment made by each customer.

---

# Summary

In this lesson, you learned:

- What JOINs are
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- CROSS JOIN
- Joining multiple tables
- Table aliases
- Filtering joined data
- Ordering joined results
- Counting with JOINs
- Performance tips
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 17 — SQL Functions**

Topics covered:

- Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)
- String Functions
- Numeric Functions
- Date Functions
- NULL Functions
- Real-world examples
```