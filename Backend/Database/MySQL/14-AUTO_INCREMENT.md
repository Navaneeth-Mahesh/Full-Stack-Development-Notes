# Lesson 14 — AUTO_INCREMENT

## Learning Objectives

By the end of this lesson, you will understand:

- What `AUTO_INCREMENT` is
- Why it is used
- How `AUTO_INCREMENT` works
- Using it with `PRIMARY KEY`
- Setting custom starting values
- Resetting the AUTO_INCREMENT counter
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# What is AUTO_INCREMENT?

`AUTO_INCREMENT` is a MySQL attribute that automatically generates the next numeric value whenever a new row is inserted.

Instead of manually assigning IDs, MySQL generates them for you.

Example:

| StudentID | Name |
|-----------|------|
| 1 | Navaneeth |
| 2 | Rahul |
| 3 | Priya |
| 4 | Sneha |

Notice that the IDs increase automatically.

---

# Why Do We Need AUTO_INCREMENT?

Imagine inserting thousands of users.

Without AUTO_INCREMENT:

```sql
INSERT INTO students
VALUES (1, 'Navaneeth');

INSERT INTO students
VALUES (2, 'Rahul');

INSERT INTO students
VALUES (3, 'Priya');
```

You must remember every ID.

Problems:

- Duplicate IDs
- Missing IDs
- Human mistakes
- More coding effort

With AUTO_INCREMENT:

```sql
INSERT INTO students(name)
VALUES ('Navaneeth');

INSERT INTO students(name)
VALUES ('Rahul');

INSERT INTO students(name)
VALUES ('Priya');
```

MySQL assigns IDs automatically.

---

# How AUTO_INCREMENT Works

Every time a new row is inserted,

MySQL:

1. Reads the current highest value.
2. Adds 1.
3. Stores the new value.

Example:

Current table:

| ID | Name |
|----|------|
|1|Navaneeth|
|2|Rahul|
|3|Priya|

Insert:

```sql
INSERT INTO students(name)
VALUES ('Sneha');
```

Result:

| ID | Name |
|----|------|
|1|Navaneeth|
|2|Rahul|
|3|Priya|
|4|Sneha|

---

# Syntax

```sql
column_name INT AUTO_INCREMENT
```

Usually combined with:

```sql
PRIMARY KEY
```

---

# Creating a Table with AUTO_INCREMENT

```sql
CREATE TABLE students (

    student_id INT AUTO_INCREMENT PRIMARY KEY,

    first_name VARCHAR(50),

    age INT

);
```

Explanation:

- `student_id` → Integer
- `AUTO_INCREMENT` → Automatically increases
- `PRIMARY KEY` → Unique identifier

---

# Inserting Data

Since MySQL generates IDs automatically:

```sql
INSERT INTO students(first_name, age)

VALUES
('Navaneeth',20),
('Rahul',21),
('Sneha',19);
```

View data:

```sql
SELECT * FROM students;
```

Output:

| student_id | first_name | age |
|------------|------------|----|
|1|Navaneeth|20|
|2|Rahul|21|
|3|Sneha|19|

---

# What Happens if You Insert Another Row?

```sql
INSERT INTO students(first_name, age)

VALUES ('Priya',22);
```

Output:

| student_id | first_name |
|------------|------------|
|1|Navaneeth|
|2|Rahul|
|3|Sneha|
|4|Priya|

The next number is generated automatically.

---

# Using AUTO_INCREMENT with PRIMARY KEY

This is the most common pattern.

```sql
CREATE TABLE products(

    product_id INT AUTO_INCREMENT PRIMARY KEY,

    product_name VARCHAR(100),

    price DECIMAL(10,2)

);
```

Every product receives a unique ID automatically.

---

# Real-World Example

Amazon Products

| ProductID | Product |
|------------|---------|
|1|Laptop|
|2|Mouse|
|3|Keyboard|
|4|Monitor|

Even if millions of products exist,

developers never manually assign IDs.

---

# Another Example

Users Table

```sql
CREATE TABLE users(

    user_id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50),

    email VARCHAR(100)

);
```

Insert:

```sql
INSERT INTO users(username,email)

VALUES

('navaneeth','nav@gmail.com'),

('rahul','rahul@gmail.com'),

('sneha','sneha@gmail.com');
```

Result:

| user_id | username |
|---------|----------|
|1|navaneeth|
|2|rahul|
|3|sneha|

---

# Can We Insert IDs Manually?

Yes.

```sql
INSERT INTO students

VALUES

(100,'Kiran',22);
```

Output:

| ID | Name |
|----|------|
|100|Kiran|

Now the next automatic ID becomes:

```
101
```

because MySQL continues after the highest existing value.

---

# Starting AUTO_INCREMENT from Another Number

Suppose you want IDs to start from 1000.

Create the table:

```sql
CREATE TABLE employees(

    employee_id INT AUTO_INCREMENT PRIMARY KEY,

    employee_name VARCHAR(100)

);
```

Set starting value:

```sql
ALTER TABLE employees

AUTO_INCREMENT = 1000;
```

Insert:

```sql
INSERT INTO employees(employee_name)

VALUES

('Navaneeth');
```

Output:

| employee_id | employee_name |
|------------|---------------|
|1000|Navaneeth|

Next insert:

```
1001
```

---

# Viewing the Next AUTO_INCREMENT Value

Run:

```sql
SHOW TABLE STATUS LIKE 'students';
```

Example (simplified):

| Name | Auto_increment |
|------|----------------|
|students|5|

This means the next inserted row will receive ID 5.

---

# Resetting AUTO_INCREMENT

Suppose IDs are:

|ID|
|--|
|1|
|2|
|3|
|4|

Delete all rows:

```sql
DELETE FROM students;
```

Now insert again:

```sql
INSERT INTO students(first_name)

VALUES ('Navaneeth');
```

The ID will still continue from the previous value.

Example:

```
5
```

because `DELETE` removes rows but does not reset the counter.

---

# Resetting After Deleting Data

If the table is empty:

```sql
ALTER TABLE students

AUTO_INCREMENT = 1;
```

Next inserted row:

```
1
```

---

# TRUNCATE vs DELETE

### DELETE

```sql
DELETE FROM students;
```

- Removes rows
- Keeps table
- AUTO_INCREMENT continues

Example:

```
Last ID = 50

Next ID = 51
```

---

### TRUNCATE

```sql
TRUNCATE TABLE students;
```

- Deletes all rows
- Resets AUTO_INCREMENT
- Faster than DELETE

Example:

```
Next ID = 1
```

---

# What Happens When Rows Are Deleted?

Current table:

|ID|
|--|
|1|
|2|
|3|
|4|

Delete:

```sql
DELETE FROM students

WHERE student_id = 2;
```

Table becomes:

|ID|
|--|
|1|
|3|
|4|

Insert another student:

Result:

|ID|
|--|
|1|
|3|
|4|
|5|

Notice:

MySQL **does not reuse deleted IDs** automatically.

This helps maintain stable references from other tables.

---

# Why Doesn't MySQL Reuse Deleted IDs?

Suppose an `orders` table stores:

| OrderID | CustomerID |
|---------|------------|
|101|2|

If ID 2 were reused for a different customer, old orders would point to the wrong person.

Leaving gaps keeps relationships safe.

---

# Common Mistakes

## Mistake 1

Providing IDs manually every time.

Bad:

```sql
INSERT INTO students

VALUES

(1,'Navaneeth');
```

Better:

```sql
INSERT INTO students(first_name)

VALUES

('Navaneeth');
```

---

## Mistake 2

Using AUTO_INCREMENT without PRIMARY KEY.

Possible:

```sql
id INT AUTO_INCREMENT
```

Recommended:

```sql
id INT AUTO_INCREMENT PRIMARY KEY
```

---

## Mistake 3

Trying to reset AUTO_INCREMENT when the table still contains higher IDs.

Example:

```sql
ALTER TABLE students

AUTO_INCREMENT = 1;
```

If ID 20 already exists,

the next ID will still be greater than 20.

---

# Best Practices

- Use AUTO_INCREMENT only for numeric IDs.
- Combine it with `PRIMARY KEY`.
- Never edit generated IDs unless necessary.
- Don't depend on IDs being consecutive.
- Use `TRUNCATE` only when you intentionally want to remove all data and reset numbering.

---

# Interview Questions

## 1. What is AUTO_INCREMENT?

It automatically generates sequential numeric values for a column whenever a new row is inserted.

---

## 2. Which data type is commonly used?

```
INT
```

---

## 3. Can AUTO_INCREMENT work without PRIMARY KEY?

Yes, but it is almost always used with a `PRIMARY KEY` or another indexed column.

---

## 4. Does DELETE reset AUTO_INCREMENT?

No.

---

## 5. Which command resets AUTO_INCREMENT by removing all rows?

```sql
TRUNCATE TABLE table_name;
```

---

## 6. How do you set the starting value to 1000?

```sql
ALTER TABLE table_name

AUTO_INCREMENT = 1000;
```

---

## 7. Does MySQL reuse deleted IDs automatically?

No.

---

# Practice Exercises

## Exercise 1

Create a table:

```sql
students
```

with:

- student_id
- name
- age

Use:

- `AUTO_INCREMENT`
- `PRIMARY KEY`

---

## Exercise 2

Insert five students without specifying IDs.

Display the table.

---

## Exercise 3

Delete one student.

Insert another student.

Observe the new ID.

---

## Exercise 4

Create an `employees` table.

Set AUTO_INCREMENT to start at:

```
1000
```

Insert three employees.

---

## Exercise 5

Create a `products` table.

Insert ten products.

Display all records.

---

## Mini Project

Create a simple Library Management database.

### Table: books

```sql
book_id INT AUTO_INCREMENT PRIMARY KEY

title VARCHAR(100)

author VARCHAR(100)

price DECIMAL(8,2)
```

Insert:

- 5 books

Delete one book.

Insert another book.

Observe how `AUTO_INCREMENT` behaves.

Finally:

```sql
SHOW TABLE STATUS LIKE 'books';
```

Find the next AUTO_INCREMENT value.

---

# Summary

In this lesson, you learned:

- What `AUTO_INCREMENT` is
- Why it is useful
- How it works
- Using it with `PRIMARY KEY`
- Inserting rows without IDs
- Manually inserting IDs
- Setting custom starting values
- Viewing the next AUTO_INCREMENT value
- Resetting AUTO_INCREMENT
- Difference between `DELETE` and `TRUNCATE`
- Why deleted IDs are not reused
- Best practices
- Practice exercises

---

# Next Lesson

**Lesson 15 — FOREIGN KEYS**

Topics covered:

- What are Foreign Keys?
- Parent and Child tables
- Creating Foreign Keys
- Referential Integrity
- ON DELETE
- ON UPDATE
- Cascade operations
- Real-world examples