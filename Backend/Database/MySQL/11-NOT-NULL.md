# Lesson 11 — NOT NULL Constraint

## Learning Objectives

By the end of this lesson, you will understand:

- What the NOT NULL constraint is
- Why NOT NULL is important
- How to create NOT NULL columns
- How NOT NULL behaves with INSERT and UPDATE
- Difference between NULL and NOT NULL
- Using NOT NULL with other constraints
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# What is a Constraint?

A **constraint** is a rule that controls what data can be stored in a table.

Constraints help maintain **data accuracy**, **consistency**, and **integrity**.

Some common constraints are:

- NOT NULL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY
- CHECK
- DEFAULT

---

# What is NOT NULL?

The **NOT NULL** constraint ensures that a column **must always contain a value**.

It prevents users from inserting or updating a row with an empty (`NULL`) value in that column.

Think of it as saying:

> "This field is mandatory."

---

# Why is NOT NULL Important?

Imagine a student database.

Every student should have:

- Student ID
- Name

But a phone number may be optional.

Bad data:

| Student_ID | Name | Email |
|------------|------|-------|
| 101 | NULL | nav@example.com |

Who is this student?

The record becomes meaningless.

Using `NOT NULL` prevents this problem.

---

# NULL vs NOT NULL

Suppose we have this table:

| ID | Name | Phone |
|----|------|--------|
|1|Navaneeth|9876543210|
|2|Rahul|NULL|

Here:

- Rahul has no phone number.
- `NULL` means the value is **unknown** or **not provided**.

Now imagine:

| ID | Name |
|----|------|
|3|NULL|

Who is the student?

This is why `Name` should be `NOT NULL`.

---

# Creating a NOT NULL Column

Syntax:

```sql
column_name datatype NOT NULL
```

Example:

```sql
CREATE TABLE students (
    student_id INT,
    name VARCHAR(100) NOT NULL,
    age INT
);
```

Here:

- `student_id` → NULL allowed
- `name` → NULL NOT allowed
- `age` → NULL allowed

---

# Example Table

```sql
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    salary DECIMAL(10,2)
);
```

Only first and last names are mandatory.

---

# Viewing Table Structure

```sql
DESCRIBE employees;
```

Output:

| Field | Type | Null |
|-------|------|------|
|employee_id|int|YES|
|first_name|varchar(50)|NO|
|last_name|varchar(50)|NO|
|email|varchar(100)|YES|

`NO` means NOT NULL.

---

# Inserting Valid Data

```sql
INSERT INTO employees
(employee_id, first_name, last_name)
VALUES
(1,'Navaneeth','Mahesh');
```

Result:

```
Query OK
```

---

# Trying to Insert NULL

```sql
INSERT INTO employees
(employee_id, first_name, last_name)
VALUES
(2,NULL,'Kumar');
```

Output:

```
ERROR:
Column 'first_name' cannot be null
```

The row is not inserted.

---

# Omitting a NOT NULL Column

```sql
INSERT INTO employees
(employee_id,last_name)
VALUES
(3,'Sharma');
```

Output:

```
ERROR:
Field 'first_name' doesn't have a default value
```

Because MySQL tries to insert `NULL` for the missing column.

---

# NOT NULL with UPDATE

Suppose:

```sql
SELECT * FROM employees;
```

| employee_id | first_name | last_name |
|-------------|------------|-----------|
|1|Navaneeth|Mahesh|

Now:

```sql
UPDATE employees
SET first_name = NULL
WHERE employee_id = 1;
```

Output:

```
ERROR:
Column 'first_name' cannot be null
```

The update fails.

---

# NULL Allowed Example

```sql
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100) NOT NULL,
    description TEXT
);
```

Description is optional.

This is valid:

```sql
INSERT INTO products
VALUES
(1,'Laptop',NULL);
```

---

# NOT NULL with PRIMARY KEY

Example:

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);
```

A PRIMARY KEY is automatically:

- NOT NULL
- UNIQUE

So writing:

```sql
PRIMARY KEY NOT NULL
```

is unnecessary.

---

# NOT NULL with UNIQUE

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

Meaning:

- Every customer must provide an email.
- Every email must be different.

Examples:

Allowed:

```
alice@gmail.com

bob@gmail.com
```

Not allowed:

```
NULL

alice@gmail.com
```

---

# NOT NULL with DEFAULT

```sql
CREATE TABLE employees (
    employee_id INT,
    department VARCHAR(50) NOT NULL DEFAULT 'General'
);
```

Insert:

```sql
INSERT INTO employees(employee_id)
VALUES (1);
```

Result:

| employee_id | department |
|--------------|-----------|
|1|General|

Since a default value exists, MySQL uses it instead of NULL.

---

# NOT NULL with CHECK

```sql
CREATE TABLE accounts (
    account_id INT,
    balance DECIMAL(10,2) NOT NULL CHECK(balance >= 0)
);
```

Rules:

- Balance cannot be NULL.
- Balance cannot be negative.

---

# Adding NOT NULL Later

Existing table:

```sql
CREATE TABLE students (
    student_id INT,
    name VARCHAR(100)
);
```

Modify:

```sql
ALTER TABLE students
MODIFY name VARCHAR(100) NOT NULL;
```

Now `name` becomes mandatory.

---

# Removing NOT NULL

```sql
ALTER TABLE students
MODIFY name VARCHAR(100);
```

Now NULL values are allowed.

---

# Common Mistakes

## Mistake 1

Trying to insert NULL.

```sql
INSERT INTO students
VALUES(1,NULL);
```

Result:

```
Error
```

---

## Mistake 2

Forgetting required columns.

```sql
INSERT INTO employees(id)
VALUES(1);
```

If other NOT NULL columns have no default value, the insert fails.

---

## Mistake 3

Updating mandatory fields to NULL.

```sql
UPDATE employees
SET first_name=NULL;
```

Error.

---

# Real-World Example

## Banking System

```
Account Number
Customer Name
Balance
```

Should these be NULL?

No.

```sql
account_number INT NOT NULL

customer_name VARCHAR(100) NOT NULL

balance DECIMAL(12,2) NOT NULL
```

---

## Hospital

Patient must have:

- Patient ID
- Name
- Gender

Phone number can be optional.

---

## E-Commerce

Products must have:

- Product ID
- Product Name
- Price

Description can be optional.

---

# Best Practices

- Use `NOT NULL` for required information.
- Don't make every column `NOT NULL`.
- Allow NULL only for genuinely optional data.
- Combine `NOT NULL` with `DEFAULT` when appropriate.
- Combine `NOT NULL` with `UNIQUE` for login credentials.
- Use meaningful default values where possible.

---

# Common Interview Questions

## 1. What is NOT NULL?

A constraint that prevents NULL values from being stored in a column.

---

## 2. What is NULL?

A special marker indicating that a value is missing, unknown, or not provided.

---

## 3. Can a PRIMARY KEY contain NULL?

No.

A PRIMARY KEY is automatically `NOT NULL`.

---

## 4. Can a UNIQUE column contain NULL?

Yes.

By default, MySQL allows NULL values in a UNIQUE column unless it is also declared `NOT NULL`.

---

## 5. Can NOT NULL be removed later?

Yes.

Using:

```sql
ALTER TABLE table_name
MODIFY column_name datatype;
```

---

# Practice Exercises

## Exercise 1

Create a table:

```sql
employees
```

Requirements:

- id
- first_name NOT NULL
- last_name NOT NULL
- salary

---

## Exercise 2

Insert three valid employees.

---

## Exercise 3

Try inserting:

```sql
NULL
```

for `first_name`.

Observe the error.

---

## Exercise 4

Update an employee's name to NULL.

Observe the error.

---

## Exercise 5

Create a table:

```sql
products
```

Fields:

- product_id
- product_name NOT NULL
- description
- price NOT NULL

Insert five products.

---

## Exercise 6

Create a table where:

- email is UNIQUE and NOT NULL
- country has a DEFAULT value of 'India'

Insert sample records and observe how DEFAULT works.

---

# Mini Project

Create a simple **College Database**.

Database:

```sql
college_db
```

Table:

```sql
students
```

Columns:

- student_id PRIMARY KEY
- first_name NOT NULL
- last_name NOT NULL
- email UNIQUE NOT NULL
- department NOT NULL DEFAULT 'CSE'
- age CHECK(age >= 17)

Tasks:

1. Insert five students.
2. Try inserting a NULL name.
3. Try inserting a duplicate email.
4. Omit the department and verify the DEFAULT value.
5. Display all records.

---

# Summary

In this lesson, you learned:

- What `NOT NULL` is
- Why mandatory fields are important
- Creating `NOT NULL` columns
- Using `NOT NULL` with `INSERT` and `UPDATE`
- Difference between `NULL` and `NOT NULL`
- Combining `NOT NULL` with `PRIMARY KEY`, `UNIQUE`, `CHECK`, and `DEFAULT`
- Real-world applications
- Best practices
- Common mistakes
- Practice exercises

---

# Next Lesson

**Lesson 12 — CHECK Constraint**

Topics covered:

- What is CHECK?
- Creating CHECK constraints
- Validating numeric ranges
- Restricting allowed values
- CHECK with UPDATE
- CHECK with multiple conditions
- Real-world examples
- Best practices
- Practice exercises