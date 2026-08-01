# Lesson 5 — INSERT ROWS in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What is an INSERT statement?
- How to insert one row
- How to insert multiple rows
- How to insert specific columns
- What happens if values are missing
- NULL values
- Common errors
- Best practices
- Interview questions
- Practice exercises

---

# What is INSERT?

The `INSERT` statement is used to add new records (rows) into a table.

Think of a table as an Excel sheet.

Every new student, product, or customer is added using `INSERT`.

Example:

Students Table

| student_id | name | age | branch |
|------------|------|-----|--------|
|1|Navaneeth|20|CSE|

Adding Rahul creates another row.

| student_id | name | age | branch |
|------------|------|-----|--------|
|1|Navaneeth|20|CSE|
|2|Rahul|21|ECE|

---

# Syntax

```sql
INSERT INTO table_name
VALUES(value1, value2, value3, ...);
```

Example:

```sql
INSERT INTO students
VALUES(1, 'Navaneeth', 20, 'CSE');
```

---

# Creating a Sample Table

```sql
CREATE TABLE students(
    student_id INT,
    name VARCHAR(50),
    age INT,
    branch VARCHAR(30)
);
```

---

# Insert One Row

```sql
INSERT INTO students
VALUES(1, 'Navaneeth', 20, 'CSE');
```

View the data:

```sql
SELECT * FROM students;
```

Output:

| student_id | name | age | branch |
|------------|------|-----|--------|
|1|Navaneeth|20|CSE|

---

# Insert Another Row

```sql
INSERT INTO students
VALUES(2, 'Rahul', 21, 'ECE');
```

Now:

```sql
SELECT * FROM students;
```

Output:

| student_id | name | age | branch |
|------------|------|-----|--------|
|1|Navaneeth|20|CSE|
|2|Rahul|21|ECE|

---

# Insert Multiple Rows

Instead of writing many INSERT statements:

```sql
INSERT INTO students
VALUES
(3, 'Sneha', 19, 'IT'),
(4, 'Aman', 22, 'EEE'),
(5, 'Priya', 20, 'CSE');
```

Output:

| student_id | name | age | branch |
|------------|------|-----|--------|
|1|Navaneeth|20|CSE|
|2|Rahul|21|ECE|
|3|Sneha|19|IT|
|4|Aman|22|EEE|
|5|Priya|20|CSE|

---

# Insert into Specific Columns

Sometimes you don't want to insert every column.

Syntax:

```sql
INSERT INTO table_name(column1, column2)
VALUES(value1, value2);
```

Example:

```sql
INSERT INTO students(name, age)
VALUES('Kiran', 18);
```

Only the specified columns receive values.

Other columns become `NULL` (unless restricted).

Result:

| student_id | name | age | branch |
|------------|------|-----|--------|
|NULL|Kiran|18|NULL|

---

# Changing Column Order

The order of values must match the listed columns.

Correct:

```sql
INSERT INTO students(age, name)
VALUES(20, 'Arjun');
```

MySQL maps:

```
age → 20

name → Arjun
```

---

# Incorrect Order

Wrong:

```sql
INSERT INTO students
VALUES('Navaneeth', 20, 'CSE', 1);
```

Expected order:

```
student_id

name

age

branch
```

Given order:

```
name

age

branch

student_id
```

This causes incorrect data or an error.

---

# String Values

Text values must be inside quotes.

Correct:

```sql
INSERT INTO students
VALUES(6, 'Ravi', 22, 'Mechanical');
```

Wrong:

```sql
INSERT INTO students
VALUES(6, Ravi, 22, Mechanical);
```

MySQL thinks Ravi is a column name.

---

# Numbers

Numbers should not be inside quotes.

Good:

```sql
20
```

Although this works:

```sql
'20'
```

it is better to use the correct data type.

---

# NULL Values

You can explicitly insert NULL.

Example:

```sql
INSERT INTO students
VALUES(7, 'John', NULL, 'CSE');
```

Result:

| student_id | name | age | branch |
|------------|------|-----|--------|
|7|John|NULL|CSE|

NULL means **unknown or no value**.

It is **not** the same as:

- 0
- Empty string ""
- False

---

# Inserting Today's Date

Suppose the table has:

```sql
admission_date DATE
```

You can insert today's date automatically:

```sql
INSERT INTO students
VALUES
(8, 'Sara', 20, 'IT', CURRENT_DATE());
```

---

# Common Errors

## Error 1: Wrong Number of Values

Table:

```sql
student_id

name

age

branch
```

Query:

```sql
INSERT INTO students
VALUES(1, 'Navaneeth');
```

Output:

```
Column count doesn't match value count.
```

---

## Error 2: Missing Quotes

Wrong:

```sql
INSERT INTO students
VALUES(1, Navaneeth, 20, CSE);
```

Correct:

```sql
INSERT INTO students
VALUES(1, 'Navaneeth', 20, 'CSE');
```

---

## Error 3: Wrong Data Type

```sql
INSERT INTO students
VALUES('ABC', 'Navaneeth', 20, 'CSE');
```

If `student_id` is an integer, this may produce an error.

---

## Error 4: Duplicate Primary Key

Suppose:

```sql
student_id = 1
```

already exists.

Trying:

```sql
INSERT INTO students
VALUES(1, 'Rahul', 20, 'ECE');
```

will fail if `student_id` is the Primary Key.

---

# Real-World Example

Products Table

```sql
CREATE TABLE products(
    product_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);
```

Insert data:

```sql
INSERT INTO products
VALUES
(101, 'Laptop', 65000.00, 20),
(102, 'Mouse', 699.00, 120),
(103, 'Keyboard', 1499.00, 50);
```

Check:

```sql
SELECT * FROM products;
```

Output:

| product_id | product_name | price | stock |
|------------|--------------|-------|------:|
|101|Laptop|65000.00|20|
|102|Mouse|699.00|120|
|103|Keyboard|1499.00|50|

---

# Best Practices

- Always specify column names when possible.
- Match the number of columns and values.
- Use single quotes for strings.
- Use the correct data type.
- Insert multiple rows in one query for better performance.
- Verify data using `SELECT` after inserting.
- Use meaningful values.

---

# Interview Questions

### 1. Which SQL statement adds new records?

```sql
INSERT
```

---

### 2. Insert one row.

```sql
INSERT INTO students
VALUES(1, 'Navaneeth', 20, 'CSE');
```

---

### 3. Insert multiple rows.

```sql
INSERT INTO students
VALUES
(2, 'Rahul', 21, 'ECE'),
(3, 'Sneha', 19, 'IT');
```

---

### 4. Why specify column names in INSERT?

It makes the query safer, more readable, and independent of the table's column order.

---

### 5. What is NULL?

A special value representing missing or unknown data.

---

# Practice Exercises

## Exercise 1

Create:

```sql
CREATE TABLE employees(
    emp_id INT,
    emp_name VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(30)
);
```

---

## Exercise 2

Insert one employee.

---

## Exercise 3

Insert five more employees using a single INSERT statement.

---

## Exercise 4

Insert only:

- emp_name
- salary

Leave the remaining columns empty.

---

## Exercise 5

Insert one employee with:

```text
salary = NULL
```

---

## Exercise 6

Display all employees.

```sql
SELECT * FROM employees;
```

---

# Mini Project

Create a `books` table:

```sql
CREATE TABLE books(
    book_id INT,
    title VARCHAR(100),
    author VARCHAR(100),
    price DECIMAL(8,2)
);
```

Insert these records:

| book_id | title | author | price |
|---------:|-------|--------|------:|
|1|Atomic Habits|James Clear|499.00|
|2|Deep Work|Cal Newport|599.00|
|3|Clean Code|Robert C. Martin|799.00|
|4|The Pragmatic Programmer|Andrew Hunt|899.00|

Display the table:

```sql
SELECT * FROM books;
```

---

# Summary

In this lesson, you learned:

- What `INSERT` is
- Insert a single row
- Insert multiple rows
- Insert specific columns
- Column order
- String vs numeric values
- `NULL`
- Common errors
- Best practices
- Practice exercises

---

# Next Lesson

**Lesson 6 — SELECT Statement**

Topics covered:

- `SELECT *`
- Selecting specific columns
- `WHERE`
- Comparison operators
- Aliases (`AS`)
- `DISTINCT`
- Filtering data
- Real-world examples