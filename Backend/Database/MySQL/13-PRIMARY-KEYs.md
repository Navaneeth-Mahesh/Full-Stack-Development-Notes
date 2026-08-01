# Lesson 13 — PRIMARY KEY

## Learning Objectives

By the end of this lesson, you will understand:

- What a Primary Key is
- Why Primary Keys are important
- Characteristics of a Primary Key
- Single vs Composite Primary Keys
- How to create Primary Keys
- Composite Primary Keys
- PRIMARY KEY with AUTO_INCREMENT
- Real-world examples
- Best practices
- Interview questions
- Practice exercises

---

# What is a Primary Key?

A **Primary Key** is a column (or combination of columns) that **uniquely identifies every row in a table**.

Think of it as an **Aadhaar Number**, **Passport Number**, or **Student Roll Number**.

No two people can have the same Aadhaar number.

Similarly, no two rows can have the same Primary Key.

---

# Why Do We Need a Primary Key?

Imagine a Students table:

| Name | Branch |
|------|--------|
| Navaneeth | CSE |
| Rahul | ECE |
| Navaneeth | IT |

Which Navaneeth are we referring to?

We don't know.

Now add a Student ID.

| StudentID | Name | Branch |
|-----------|------|--------|
|101|Navaneeth|CSE|
|102|Rahul|ECE|
|103|Navaneeth|IT|

Now every student can be identified uniquely.

---

# Characteristics of a Primary Key

A Primary Key must satisfy these rules:

## 1. Unique

No duplicate values are allowed.

Correct

| ID |
|----|
|1|
|2|
|3|

Wrong

| ID |
|----|
|1|
|1|
|3|

---

## 2. NOT NULL

A Primary Key can never contain NULL.

Correct

| ID |
|----|
|1|
|2|
|3|

Wrong

| ID |
|----|
|1|
|NULL|
|3|

---

## 3. Only One Primary Key per Table

A table can have only **one Primary Key constraint**.

However, that one Primary Key may contain multiple columns (Composite Primary Key).

---

## 4. Permanent

A Primary Key should rarely change.

Changing a Primary Key can break relationships with other tables.

Example:

Student ID

```
101
```

should remain the same throughout the student's academic life.

---

# Visual Representation

```
Students
---------------------------------------
StudentID   Name        Branch
---------------------------------------
101         Navaneeth   CSE
102         Rahul       ECE
103         Sneha       IT
---------------------------------------
```

StudentID is the Primary Key.

---

# Creating a Primary Key

Syntax

```sql
CREATE TABLE table_name (
    column_name datatype PRIMARY KEY
);
```

Example

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```

---

# Insert Data

```sql
INSERT INTO students
VALUES
(1,'Navaneeth',20),
(2,'Rahul',21),
(3,'Sneha',19);
```

View

```sql
SELECT * FROM students;
```

Output

| student_id | name | age |
|------------|------|-----|
|1|Navaneeth|20|
|2|Rahul|21|
|3|Sneha|19|

---

# Duplicate Primary Key

Example

```sql
INSERT INTO students
VALUES
(1,'Kiran',22);
```

Output

```
ERROR 1062

Duplicate entry '1'
for key 'PRIMARY'
```

Reason

Primary Keys must be unique.

---

# NULL Primary Key

Example

```sql
INSERT INTO students
VALUES
(NULL,'Kiran',22);
```

Output

```
ERROR

Primary key cannot be NULL
```

---

# Adding Primary Key Later

Suppose the table already exists.

```sql
CREATE TABLE students (
    student_id INT,
    name VARCHAR(100)
);
```

Later

```sql
ALTER TABLE students
ADD PRIMARY KEY(student_id);
```

---

# Removing a Primary Key

```sql
ALTER TABLE students
DROP PRIMARY KEY;
```

Use carefully.

---

# Single Primary Key

Most tables use a single column.

Example

```
StudentID

EmployeeID

ProductID

OrderID

CustomerID
```

Each uniquely identifies one record.

---

# Composite Primary Key

Sometimes one column alone cannot uniquely identify a record.

Use multiple columns together.

Example

Student Enrollments

| StudentID | CourseID |
|-----------|----------|
|1|101|
|1|102|
|2|101|

StudentID alone is not unique.

CourseID alone is not unique.

Together they are unique.

---

# Creating a Composite Primary Key

```sql
CREATE TABLE enrollments (

    student_id INT,

    course_id INT,

    enrollment_date DATE,

    PRIMARY KEY(student_id, course_id)

);
```

Now:

```
(1,101)

(1,102)

(2,101)
```

are valid.

But

```
(1,101)
```

cannot appear twice.

---

# Composite Key Example

Valid

| StudentID | CourseID |
|-----------|----------|
|1|101|
|1|102|
|2|101|

Invalid

| StudentID | CourseID |
|-----------|----------|
|1|101|
|1|101|

Duplicate combination.

---

# PRIMARY KEY with AUTO_INCREMENT

Most real-world projects use this.

Example

```sql
CREATE TABLE students (

    student_id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100),

    age INT

);
```

Insert

```sql
INSERT INTO students(name,age)
VALUES

('Navaneeth',20),

('Rahul',21),

('Sneha',19);
```

Output

| student_id | name | age |
|------------|------|-----|
|1|Navaneeth|20|
|2|Rahul|21|
|3|Sneha|19|

IDs are generated automatically.

---

# Real-World Examples

## College

Students

| StudentID | Name |
|-----------|------|
|1001|Navaneeth|
|1002|Rahul|

StudentID is Primary Key.

---

## E-Commerce

Products

| ProductID | Product |
|-----------|----------|
|501|Laptop|
|502|Phone|

ProductID is Primary Key.

---

## Banking

Accounts

| AccountNumber | Holder |
|---------------|--------|
|987654321|Navaneeth|

AccountNumber is Primary Key.

---

## Hospital

Patients

| PatientID | Name |
|-----------|------|
|201|Asha|
|202|Rahul|

PatientID uniquely identifies every patient.

---

# Common Mistakes

## Duplicate IDs

Wrong

```sql
INSERT INTO students
VALUES

(1,'Nav'),

(1,'Rahul');
```

Error

Duplicate Primary Key.

---

## NULL Values

Wrong

```sql
INSERT INTO students
VALUES

(NULL,'Nav');
```

Error

Primary Key cannot be NULL.

---

## Using Name as Primary Key

Wrong

```sql
name VARCHAR(50) PRIMARY KEY
```

Many people may share the same name.

Use an ID instead.

---

# Best Practices

- Prefer integer IDs.
- Use `AUTO_INCREMENT` whenever possible.
- Never use names or emails as Primary Keys.
- Keep Primary Keys stable.
- Every table should ideally have a Primary Key.
- Use Composite Keys only when necessary.

---

# Interview Questions

## 1. What is a Primary Key?

A column (or combination of columns) that uniquely identifies each row in a table.

---

## 2. Can a Primary Key contain NULL?

No.

---

## 3. Can a table have multiple Primary Keys?

No.

A table can have only one Primary Key constraint.

---

## 4. Can a Primary Key have duplicate values?

No.

---

## 5. What is a Composite Primary Key?

A Primary Key made up of two or more columns.

---

## 6. Why is AUTO_INCREMENT commonly used with Primary Keys?

It automatically generates unique IDs for new rows, preventing duplicate key errors and reducing manual effort.

---

## 7. What is the difference between PRIMARY KEY and UNIQUE?

| PRIMARY KEY | UNIQUE |
|--------------|---------|
|Only one per table|Multiple UNIQUE constraints allowed|
|Cannot be NULL|Can contain NULL (MySQL allows one NULL per UNIQUE column)|
|Uniquely identifies each row|Ensures uniqueness but is not the main identifier|

---

# Practice Exercises

## Exercise 1

Create a table:

```sql
CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    name VARCHAR(100),

    department VARCHAR(50)

);
```

---

## Exercise 2

Insert three employee records.

---

## Exercise 3

Try inserting another employee with the same employee_id.

Observe the error.

---

## Exercise 4

Try inserting NULL into employee_id.

Observe the error.

---

## Exercise 5

Create a table using AUTO_INCREMENT.

```sql
CREATE TABLE books (

    book_id INT AUTO_INCREMENT PRIMARY KEY,

    title VARCHAR(100),

    author VARCHAR(100)

);
```

Insert records without specifying `book_id`.

---

## Exercise 6

Create a Composite Primary Key.

```sql
CREATE TABLE attendance (

    student_id INT,

    subject_id INT,

    attendance_date DATE,

    PRIMARY KEY(student_id, subject_id)

);
```

Insert multiple valid records, then try inserting a duplicate combination.

---

# Mini Project

Create a database named:

```text
college_db
```

Inside it create:

### students

```text
student_id
name
branch
```

### courses

```text
course_id
course_name
```

### enrollments

```text
student_id
course_id
semester
```

Requirements:

- `student_id` → Primary Key in `students`
- `course_id` → Primary Key in `courses`
- (`student_id`, `course_id`) → Composite Primary Key in `enrollments`

Insert sample data and verify that duplicate primary key values are rejected.

---

# Summary

In this lesson, you learned:

- What a Primary Key is
- Why Primary Keys are important
- Characteristics of Primary Keys
- Creating Primary Keys
- Adding and removing Primary Keys
- Single vs Composite Primary Keys
- PRIMARY KEY with AUTO_INCREMENT
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 14 — AUTO_INCREMENT**

Topics covered:

- What is AUTO_INCREMENT?
- How AUTO_INCREMENT works
- Starting values
- Resetting AUTO_INCREMENT
- AUTO_INCREMENT with PRIMARY KEY
- Real-world examples
- Best practices
- Practice exercises