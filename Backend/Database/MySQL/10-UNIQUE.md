# Lesson 10 — UNIQUE Constraint

## Learning Objectives

By the end of this lesson, you will understand:

- What a UNIQUE constraint is
- Why UNIQUE is important
- How to create UNIQUE columns
- How to add UNIQUE to existing tables
- Multiple UNIQUE constraints
- Composite UNIQUE constraints
- UNIQUE vs PRIMARY KEY
- Real-world examples
- Best practices
- Interview questions
- Practice exercises

---

# What is a UNIQUE Constraint?

A **UNIQUE** constraint ensures that all values in a column (or a combination of columns) are **different**.

It prevents duplicate values from being inserted into a table.

Think of it as a rule that says:

> "No two rows can have the same value in this column."

---

# Why Do We Need UNIQUE?

Imagine a users table:

| ID | Username |
|----|----------|
|1|navaneeth|
|2|rahul|
|3|navaneeth|

Here, two users have the same username.

This creates confusion because usernames should identify users uniquely.

Using UNIQUE prevents this.

---

# Real-World Examples

Columns that are usually UNIQUE:

- Email address
- Username
- Aadhaar Number
- Passport Number
- Employee ID
- Roll Number
- Vehicle Registration Number
- PAN Number

Example:

```
✓ navaneeth@gmail.com
✓ rahul@gmail.com
✗ navaneeth@gmail.com   (Duplicate)
```

---

# Syntax

```sql
column_name datatype UNIQUE
```

Example:

```sql
email VARCHAR(100) UNIQUE
```

---

# Creating a Table with UNIQUE

```sql
CREATE TABLE users (
    user_id INT,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE
);
```

Both `username` and `email` cannot contain duplicate values.

---

# Example Table

```
users
```

| user_id | username | email |
|---------|----------|------------------------|
|1|navaneeth|nav@gmail.com|
|2|rahul|rahul@gmail.com|

Valid data.

---

Attempt to insert:

```sql
INSERT INTO users
VALUES
(3,'navaneeth','new@gmail.com');
```

Output:

```
ERROR

Duplicate entry
```

Reason:

```
username already exists
```

---

Another Example

```sql
INSERT INTO users
VALUES
(3,'sneha','rahul@gmail.com');
```

Output:

```
ERROR

Duplicate entry
```

Reason:

```
Email already exists.
```

---

# Creating UNIQUE During Table Creation

Example:

```sql
CREATE TABLE students(
    roll_no INT UNIQUE,
    name VARCHAR(50)
);
```

Now every roll number must be different.

---

# Adding UNIQUE to an Existing Table

Suppose:

```sql
CREATE TABLE employees(
    id INT,
    email VARCHAR(100)
);
```

Later you decide email should be unique.

Use:

```sql
ALTER TABLE employees
ADD CONSTRAINT unique_email
UNIQUE(email);
```

Now duplicate emails are not allowed.

---

# Removing a UNIQUE Constraint

To remove a UNIQUE constraint, you generally drop the associated index.

Example (MySQL):

```sql
ALTER TABLE employees
DROP INDEX unique_email;
```

> The index name must match the name used when creating the constraint.

---

# Multiple UNIQUE Constraints

A table can have many UNIQUE columns.

Example:

```sql
CREATE TABLE employees(
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) UNIQUE,
    employee_code VARCHAR(20) UNIQUE
);
```

Rules:

- Email must be unique.
- Phone must be unique.
- Employee code must be unique.

---

# Composite UNIQUE Constraint

Sometimes a single column may have duplicates, but a combination of columns must be unique.

Example:

```sql
CREATE TABLE enrollments(
    student_id INT,
    course_id INT,
    UNIQUE(student_id, course_id)
);
```

This means:

```
Student 1 can enroll in Course 101 once.

Student 1 cannot enroll in Course 101 again.
```

But:

```
Student 1 → Course 102 ✔

Student 2 → Course 101 ✔
```

Both are valid.

---

Example Data

| student_id | course_id |
|------------|-----------|
|1|101|
|1|102|
|2|101|

Allowed.

---

Attempt:

| student_id | course_id |
|------------|-----------|
|1|101|

Again.

Result:

```
ERROR

Duplicate entry
```

---

# UNIQUE with NULL Values

MySQL allows multiple NULL values in a UNIQUE column.

Example:

```sql
CREATE TABLE users(
    id INT,
    email VARCHAR(100) UNIQUE
);
```

Insert:

```sql
INSERT INTO users
VALUES
(1,NULL),
(2,NULL),
(3,NULL);
```

This is valid in MySQL because `NULL` means "unknown," and unknown values are not considered equal.

---

# UNIQUE vs PRIMARY KEY

| Feature | UNIQUE | PRIMARY KEY |
|---------|---------|-------------|
|Duplicate values|Not allowed|Not allowed|
|NULL values|Allowed (multiple in MySQL)|Not allowed|
|Only one per table|No|Yes|
|Multiple constraints allowed|Yes|No|
|Identifies each row|Not necessarily|Yes|

---

Example

```sql
CREATE TABLE employees(
    employee_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

Here:

- `employee_id` uniquely identifies each row.
- `email` must also be unique.

---

# Real-World Example

```
Users Table

ID
Username
Email
Phone
```

Rules:

```
ID

PRIMARY KEY
```

```
Username

UNIQUE
```

```
Email

UNIQUE
```

```
Phone

UNIQUE
```

This prevents duplicate accounts.

---

# Common Errors

## Error 1

Duplicate username.

```sql
INSERT INTO users
VALUES
(5,'rahul','new@gmail.com');
```

Output:

```
Duplicate entry
```

---

## Error 2

Duplicate email.

```sql
INSERT INTO users
VALUES
(6,'sneha','rahul@gmail.com');
```

Output:

```
Duplicate entry
```

---

## Error 3

Trying to insert duplicate employee code.

```
ERROR

Duplicate entry
```

---

# Best Practices

- Use UNIQUE for email addresses.
- Use UNIQUE for usernames.
- Use UNIQUE for government IDs.
- Use UNIQUE for employee codes.
- Give constraints meaningful names.
- Combine UNIQUE with NOT NULL when appropriate.
- Use composite UNIQUE when uniqueness depends on multiple columns.

---

# Interview Questions

## 1. What is a UNIQUE constraint?

It ensures that all values in a column (or combination of columns) are unique.

---

## 2. Can a table have multiple UNIQUE constraints?

Yes.

---

## 3. Can UNIQUE contain NULL values?

Yes. In MySQL, multiple NULL values are allowed.

---

## 4. Difference between UNIQUE and PRIMARY KEY?

- PRIMARY KEY uniquely identifies rows and cannot contain NULL values.
- UNIQUE prevents duplicates but allows NULL values (in MySQL).

---

## 5. Can multiple columns be part of one UNIQUE constraint?

Yes.

Example:

```sql
UNIQUE(student_id, course_id)
```

---

# Practice Exercises

## Exercise 1

Create a table:

```sql
CREATE TABLE users(
    id INT,
    username VARCHAR(50) UNIQUE
);
```

Insert unique usernames.

Try inserting a duplicate username.

Observe the error.

---

## Exercise 2

Create a table:

```sql
CREATE TABLE employees(
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) UNIQUE
);
```

Insert valid records.

Then try inserting:

- Duplicate email
- Duplicate phone

Observe the errors.

---

## Exercise 3

Create a table:

```sql
CREATE TABLE enrollments(
    student_id INT,
    course_id INT,
    UNIQUE(student_id, course_id)
);
```

Insert:

```text
(1,101)

(1,102)

(2,101)
```

Then try inserting:

```text
(1,101)
```

Observe the error.

---

# Mini Project

Create a `college_db` database (if it doesn't already exist) and use it.

Create a `students` table with the following rules:

- `student_id` → PRIMARY KEY
- `roll_no` → UNIQUE
- `email` → UNIQUE
- `phone` → UNIQUE
- `name` → NOT NULL

```sql
CREATE DATABASE IF NOT EXISTS college_db;
USE college_db;

CREATE TABLE students(
    student_id INT PRIMARY KEY,
    roll_no INT UNIQUE,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) UNIQUE
);
```

Insert three valid student records.

Then try to:

- Insert a duplicate roll number
- Insert a duplicate email
- Insert a duplicate phone number

Observe the errors generated by MySQL.

---

# Summary

In this lesson, you learned:

- What a UNIQUE constraint is
- Why UNIQUE is important
- How to create UNIQUE columns
- Adding UNIQUE to existing tables
- Removing UNIQUE constraints
- Multiple UNIQUE constraints
- Composite UNIQUE constraints
- UNIQUE with NULL values
- UNIQUE vs PRIMARY KEY
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 11 — NOT NULL Constraint**

Topics covered:

- What is NOT NULL?
- Why NOT NULL is important
- Creating NOT NULL columns
- NOT NULL with INSERT and UPDATE
- NOT NULL vs NULL
- Combining NOT NULL with other constraints
- Real-world examples
- Best practices
- Practice exercises