# Lesson 15 — Foreign Keys

## Learning Objectives

By the end of this lesson, you will understand:

- What a Foreign Key is
- Why Foreign Keys are important
- Parent and Child tables
- Referential Integrity
- Creating Foreign Keys
- ON DELETE actions
- ON UPDATE actions
- Cascade operations
- Real-world examples
- Best practices
- Interview questions
- Practice exercises

---

# What is a Foreign Key?

A **Foreign Key (FK)** is a column (or set of columns) in one table that refers to the **Primary Key (PK)** of another table.

It creates a relationship between two tables.

Think of it as a **bridge** that connects related data.

Example:

```
Students
+-----------+----------+
| student_id| name     |
+-----------+----------+
| 1         | Navaneeth|
| 2         | Rahul    |
+-----------+----------+

Orders
+----------+-----------+
| order_id | student_id|
+----------+-----------+
| 101      | 1         |
| 102      | 2         |
+----------+-----------+
```

Here,

```
Orders.student_id
```

is a Foreign Key that references

```
Students.student_id
```

---

# Why Do We Need Foreign Keys?

Without Foreign Keys:

```
Orders

order_id | student_id
---------|------------
101      | 99
```

Student 99 doesn't exist.

The database now contains invalid data.

Foreign Keys prevent this.

Benefits:

- Maintains data integrity
- Prevents invalid references
- Connects related tables
- Makes JOIN operations possible
- Reduces duplicate data

---

# Parent and Child Tables

The table containing the Primary Key is called the **Parent Table**.

The table containing the Foreign Key is called the **Child Table**.

Example:

```
Students
(student_id PK)
```

↓

```
Orders
(student_id FK)
```

Students → Parent

Orders → Child

---

# Visual Representation

```
Students
--------------------
student_id (PK)
name

        ▲
        │
        │
Orders
--------------------
order_id (PK)
student_id (FK)
amount
```

The child points to the parent.

---

# Real-World Example

Imagine Amazon.

```
Customers

customer_id
name
email
```

```
Orders

order_id
customer_id
total
```

One customer can place many orders.

```
Customers
      │
      │
      ▼
Orders
```

---

# Creating Parent Table

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

---

# Creating Child Table

```sql
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course VARCHAR(100),

    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
);
```

Relationship created successfully.

---

# Inserting Parent Data

```sql
INSERT INTO students
VALUES
(1,'Navaneeth'),
(2,'Rahul');
```

---

# Valid Insert

```sql
INSERT INTO enrollments
VALUES
(101,1,'Java');
```

Success.

Student 1 exists.

---

# Invalid Insert

```sql
INSERT INTO enrollments
VALUES
(102,10,'Python');
```

Output:

```
Cannot add or update a child row

Foreign key constraint fails
```

Student 10 doesn't exist.

---

# Referential Integrity

Referential Integrity means:

Every Foreign Key value must exist in the Parent table.

Example:

Students

```
1
2
3
```

Orders

```
1
2
3
```

Valid.

But

Orders

```
1
2
10
```

Invalid.

Student 10 doesn't exist.

---

# One-to-Many Relationship

One Student

↓

Many Enrollments

```
Student

1

↓

Enrollment

101

102

103

104
```

One parent

Many children

This is the most common relationship.

---

# Many-to-One

Many orders can belong to one customer.

```
Customer

1

↓

Orders

101

102

103
```

Same concept.

---

# ON DELETE

When a parent row is deleted,

what should happen to child rows?

MySQL provides several options.

---

# 1. RESTRICT (Default)

Parent cannot be deleted.

Example:

```
Student 1

↓

Enrollment 101
```

Delete student:

```sql
DELETE FROM students
WHERE student_id=1;
```

Error.

Because enrollments still exist.

---

# 2. CASCADE

Delete parent

↓

Delete all child rows automatically.

Example:

```sql
FOREIGN KEY(student_id)
REFERENCES students(student_id)
ON DELETE CASCADE;
```

Students

```
1
```

Enrollments

```
101

102
```

Delete student.

Result:

```
Student removed

Enrollment 101 removed

Enrollment 102 removed
```

Everything linked is deleted.

---

# 3. SET NULL

When parent is deleted

Child Foreign Key becomes NULL.

```sql
FOREIGN KEY(student_id)
REFERENCES students(student_id)
ON DELETE SET NULL;
```

Before

```
Enrollment

student_id=1
```

After deleting student

```
Enrollment

student_id=NULL
```

The enrollment remains.

---

# 4. NO ACTION

Behaves similar to RESTRICT in MySQL.

Parent deletion is blocked if child rows exist.

---

# ON UPDATE

What if the Primary Key changes?

Example:

Student ID

```
1
```

↓

Change to

```
10
```

Child table must decide what to do.

---

# ON UPDATE CASCADE

```sql
FOREIGN KEY(student_id)
REFERENCES students(student_id)
ON UPDATE CASCADE;
```

Before

Students

```
1
```

Enrollments

```
1
```

Update

```sql
UPDATE students
SET student_id=10
WHERE student_id=1;
```

After

Students

```
10
```

Enrollments

```
10
```

Automatically updated.

---

# ON UPDATE SET NULL

If parent key changes,

Child Foreign Key becomes NULL.

Less common than CASCADE.

---

# Complete Example

```sql
CREATE TABLE students (

student_id INT PRIMARY KEY,

name VARCHAR(100)

);

CREATE TABLE enrollments (

enrollment_id INT PRIMARY KEY,

student_id INT,

course VARCHAR(100),

FOREIGN KEY(student_id)

REFERENCES students(student_id)

ON DELETE CASCADE

ON UPDATE CASCADE

);
```

---

# Multiple Foreign Keys

Example:

Orders table

```sql
CREATE TABLE orders(

order_id INT PRIMARY KEY,

customer_id INT,

product_id INT,

FOREIGN KEY(customer_id)
REFERENCES customers(customer_id),

FOREIGN KEY(product_id)
REFERENCES products(product_id)

);
```

One table can have multiple Foreign Keys.

---

# Real-World Example

Hospital

```
Patients

patient_id
name
```

Doctors

```
doctor_id
name
```

Appointments

```
appointment_id

patient_id FK

doctor_id FK
```

Appointments connect both tables.

---

# Foreign Key Rules

The referenced column:

- Must exist
- Should usually be a Primary Key or UNIQUE
- Data types must match
- Storage engines should support Foreign Keys (InnoDB)

---

# Viewing Constraints

```sql
SHOW CREATE TABLE enrollments;
```

Displays:

- Primary Key
- Foreign Key
- Indexes
- Constraints

---

# Dropping a Foreign Key

First find the constraint name.

```sql
SHOW CREATE TABLE enrollments;
```

Then:

```sql
ALTER TABLE enrollments

DROP FOREIGN KEY enrollments_ibfk_1;
```

---

# Common Errors

## Error 1

Parent row doesn't exist.

```sql
INSERT INTO enrollments

VALUES (1,100,'Java');
```

Error:

```
Foreign key constraint fails
```

---

## Error 2

Deleting parent while children exist.

Without CASCADE.

```
Cannot delete parent row
```

---

## Error 3

Different data types.

Wrong:

```
Students

student_id INT
```

```
Orders

student_id VARCHAR(20)
```

Types must match.

---

# Best Practices

- Use Foreign Keys whenever tables are related.
- Prefer InnoDB engine.
- Match data types exactly.
- Name constraints clearly in large projects.
- Use `ON DELETE CASCADE` only when automatic deletion is desired.
- Avoid updating Primary Keys frequently.
- Don't disable Foreign Key checks unless absolutely necessary.

---

# Interview Questions

## 1. What is a Foreign Key?

A Foreign Key is a column that references the Primary Key of another table to create a relationship.

---

## 2. Why are Foreign Keys used?

To maintain referential integrity and prevent invalid data.

---

## 3. What is a Parent Table?

The table containing the referenced Primary Key.

---

## 4. What is a Child Table?

The table containing the Foreign Key.

---

## 5. What is Referential Integrity?

It ensures every Foreign Key value matches an existing Primary Key value in the parent table.

---

## 6. Difference between Primary Key and Foreign Key?

| Primary Key | Foreign Key |
|--------------|-------------|
| Uniquely identifies a row | References a row in another table |
| Must be unique | Can contain duplicate values |
| Cannot be NULL | Can be NULL (unless restricted) |
| One per table (commonly) | Multiple allowed in a table |

---

## 7. What does `ON DELETE CASCADE` do?

When a parent row is deleted, all related child rows are automatically deleted.

---

## 8. What does `ON UPDATE CASCADE` do?

When the parent key changes, the related Foreign Key values are automatically updated.

---

# Practice Exercises

### Exercise 1

Create a `customers` table.

Columns:

- customer_id
- name

Make `customer_id` the Primary Key.

---

### Exercise 2

Create an `orders` table.

Columns:

- order_id
- customer_id
- total

Make `customer_id` a Foreign Key referencing `customers(customer_id)`.

---

### Exercise 3

Insert two customers.

---

### Exercise 4

Insert three valid orders.

---

### Exercise 5

Try inserting an order with a non-existent `customer_id`.

Observe the error.

---

### Exercise 6

Create the relationship using:

```sql
ON DELETE CASCADE
ON UPDATE CASCADE
```

Delete a customer and observe what happens to their orders.

---

# Mini Project

Create a simple **Library Management Database**.

### Books

```
book_id (PK)
title
author
```

### Members

```
member_id (PK)
name
```

### Borrowed_Books

```
borrow_id (PK)
book_id (FK)
member_id (FK)
borrow_date
```

Requirements:

- Create all three tables.
- Add Foreign Keys for `book_id` and `member_id`.
- Use `ON DELETE CASCADE`.
- Insert sample data.
- Perform JOIN queries to display which member borrowed which book.
- Delete a book and observe the cascading effect.

---

# Summary

In this lesson, you learned:

- What Foreign Keys are
- Parent and Child tables
- Referential Integrity
- Creating Foreign Keys
- Valid and invalid inserts
- `ON DELETE` options (`RESTRICT`, `CASCADE`, `SET NULL`, `NO ACTION`)
- `ON UPDATE` options
- Cascade operations
- Multiple Foreign Keys
- Common errors
- Best practices
- Practice exercises
- Real-world relationships

---

# Next Lesson

**Lesson 16 — JOINS**

Topics covered:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- CROSS JOIN
- Joining multiple tables
- Aliases
- Real-world queries
- Performance tips