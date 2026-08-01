# Lesson 7 — UPDATE & DELETE

## Learning Objectives

By the end of this lesson, you will understand:

- What `UPDATE` does
- What `DELETE` does
- Using `WHERE` with `UPDATE`
- Using `WHERE` with `DELETE`
- Updating multiple columns
- Deleting specific rows
- Safe update mode
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Introduction

So far you've learned how to:

- Create databases
- Create tables
- Insert records
- Retrieve records using `SELECT`

But what if:

- A student's phone number changes?
- A product price increases?
- An employee leaves the company?

Instead of creating a new row, we **modify** or **remove** existing rows.

That's where `UPDATE` and `DELETE` come in.

---

# UPDATE Statement

The `UPDATE` statement modifies existing data in a table.

Syntax:

```sql
UPDATE table_name
SET column_name = value
WHERE condition;
```

---

Example Table:

```
students
```

| student_id | name | age | city |
|------------|------|-----|------|
|1|Navaneeth|20|Hyderabad|
|2|Rahul|21|Chennai|
|3|Sneha|19|Bangalore|

---

# Update One Column

Suppose Navaneeth moves to Vizag.

```sql
UPDATE students
SET city = 'Vizag'
WHERE student_id = 1;
```

Result:

| student_id | name | age | city |
|------------|------|-----|------|
|1|Navaneeth|20|Vizag|
|2|Rahul|21|Chennai|
|3|Sneha|19|Bangalore|

Only one row changes.

---

# Why WHERE is Important

Without `WHERE`, every row gets updated.

Example:

```sql
UPDATE students
SET city = 'Delhi';
```

Result:

| student_id | city |
|------------|------|
|1|Delhi|
|2|Delhi|
|3|Delhi|

Every student's city becomes Delhi.

This is one of the most common SQL mistakes.

---

# Update Using Another Column

Instead of using ID:

```sql
UPDATE students
SET age = 22
WHERE name = 'Rahul';
```

Result:

Rahul's age becomes 22.

---

# Update Multiple Columns

You can update more than one column at once.

Example:

```sql
UPDATE students
SET
    age = 21,
    city = 'Mumbai'
WHERE student_id = 1;
```

Result:

| student_id | name | age | city |
|------------|------|-----|------|
|1|Navaneeth|21|Mumbai|

---

# Update Numeric Values

Example:

```
products
```

| id | product | price |
|----|----------|-------|
|1|Laptop|60000|
|2|Mouse|700|

Increase laptop price.

```sql
UPDATE products
SET price = 65000
WHERE id = 1;
```

---

# Update Using Expressions

Suppose every employee receives a ₹5000 salary hike.

```
employees
```

| id | salary |
|----|--------|
|1|30000|
|2|45000|
|3|55000|

Query:

```sql
UPDATE employees
SET salary = salary + 5000;
```

Result:

| id | salary |
|----|--------|
|1|35000|
|2|50000|
|3|60000|

Notice that the old value is used in the calculation.

---

# Update Percentage

Increase all prices by 10%.

```sql
UPDATE products
SET price = price * 1.10;
```

---

# Update with Multiple Conditions

Example:

```sql
UPDATE students
SET city = 'Hyderabad'
WHERE age > 20;
```

All students older than 20 will be updated.

---

# DELETE Statement

`DELETE` removes rows from a table.

Syntax:

```sql
DELETE FROM table_name
WHERE condition;
```

---

Example Table

| id | name |
|----|------|
|1|Navaneeth|
|2|Rahul|
|3|Sneha|

Delete Rahul.

```sql
DELETE FROM students
WHERE student_id = 2;
```

Result:

| id | name |
|----|------|
|1|Navaneeth|
|3|Sneha|

Rahul's row is removed.

---

# Delete Using Another Column

```sql
DELETE FROM students
WHERE name = 'Sneha';
```

---

# Delete Multiple Rows

Delete everyone older than 20.

```sql
DELETE FROM students
WHERE age > 20;
```

---

# DELETE Without WHERE

```sql
DELETE FROM students;
```

Result:

All rows are deleted.

The table still exists.

```
students
```

becomes

| student_id | name | age |
|------------|------|-----|
| *(empty)* | | |

---

# DELETE vs DROP

Many beginners confuse these.

### DELETE

Deletes data only.

Table remains.

```sql
DELETE FROM students;
```

---

### DROP

Deletes the entire table.

```sql
DROP TABLE students;
```

Everything is removed:

- Table
- Data
- Structure

---

# DELETE vs TRUNCATE

### DELETE

- Can use WHERE
- Deletes selected rows
- Can be rolled back (depending on transaction settings)

```sql
DELETE FROM students
WHERE student_id = 1;
```

---

### TRUNCATE

Deletes all rows instantly.

```sql
TRUNCATE TABLE students;
```

Cannot delete selected rows.

Much faster than DELETE.

---

# Safe Update Mode

MySQL Workbench often enables **Safe Update Mode**.

If you run:

```sql
UPDATE students
SET city = 'Vizag';
```

You may see:

```
Error Code: 1175
You are using safe update mode...
```

This prevents accidental updates or deletes without a key column in the `WHERE` clause.

Solution:

Use a key column like:

```sql
UPDATE students
SET city = 'Vizag'
WHERE student_id = 1;
```

Or disable Safe Update Mode (not recommended for beginners).

---

# Best Practices

Always preview rows before updating or deleting.

Example:

```sql
SELECT *
FROM students
WHERE student_id = 1;
```

If the correct row appears, then run:

```sql
UPDATE students
SET city = 'Vizag'
WHERE student_id = 1;
```

This avoids accidental changes.

---

# Common Mistakes

## Mistake 1

```sql
UPDATE students
SET city = 'Delhi';
```

Updates every row.

---

## Mistake 2

```sql
DELETE FROM students;
```

Deletes every row.

---

## Mistake 3

Updating the wrong row because of an incorrect condition.

Example:

```sql
UPDATE students
SET age = 25
WHERE age = 20;
```

Every student aged 20 is updated.

---

## Mistake 4

Forgetting to verify data before deleting.

Always run:

```sql
SELECT *
FROM students
WHERE student_id = 5;
```

first.

---

# Real-World Example

### E-commerce

Product price increases.

```sql
UPDATE products
SET price = 999
WHERE product_id = 10;
```

---

### College

Student changes phone number.

```sql
UPDATE students
SET phone = '9876543210'
WHERE student_id = 5;
```

---

### Banking

Customer closes account.

```sql
DELETE FROM accounts
WHERE account_number = 10025;
```

---

### Hospital

Patient record corrected.

```sql
UPDATE patients
SET blood_group = 'O+'
WHERE patient_id = 12;
```

---

# Interview Questions

### 1. Difference between UPDATE and DELETE?

UPDATE modifies existing rows.

DELETE removes rows.

---

### 2. Why should WHERE be used?

To avoid changing or deleting every row in the table.

---

### 3. Can UPDATE modify multiple columns?

Yes.

Example:

```sql
UPDATE students
SET
    age = 21,
    city = 'Mumbai'
WHERE student_id = 1;
```

---

### 4. Does DELETE remove the table?

No.

It removes only the rows.

---

### 5. Difference between DELETE and DROP?

DELETE removes data.

DROP removes the entire table.

---

### 6. Difference between DELETE and TRUNCATE?

DELETE removes selected or all rows and supports `WHERE`.

TRUNCATE removes all rows quickly but does not support `WHERE`.

---

# Practice Exercises

## Exercise 1

Change Rahul's city to Delhi.

---

## Exercise 2

Increase every employee's salary by ₹2,000.

---

## Exercise 3

Update two columns for one student.

---

## Exercise 4

Delete one product using its ID.

---

## Exercise 5

Delete all students older than 22.

---

## Exercise 6

Remove every record from a table using DELETE.

---

## Exercise 7

Create a products table:

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);
```

Insert:

```sql
INSERT INTO products VALUES
(1,'Laptop',65000,10),
(2,'Keyboard',1500,30),
(3,'Mouse',700,50),
(4,'Monitor',12000,8);
```

Perform these operations:

- Increase Laptop price to 70000
- Increase all prices by 5%
- Reduce Monitor stock to 5
- Delete Mouse
- Display the final table

---

# Mini Project

Create an `employees` table with:

- Employee ID
- Name
- Department
- Salary
- City

Insert at least 5 records.

Perform the following:

1. Update one employee's city.
2. Increase all salaries by ₹5,000.
3. Change one employee's department.
4. Delete one employee.
5. Delete all employees with salary below ₹30,000.
6. Display the final table using:

```sql
SELECT * FROM employees;
```

---

# Summary

In this lesson, you learned:

- `UPDATE`
- `DELETE`
- `WHERE` with UPDATE
- `WHERE` with DELETE
- Updating multiple columns
- Updating using expressions
- Deleting selected rows
- `DELETE` vs `DROP`
- `DELETE` vs `TRUNCATE`
- Safe Update Mode
- Common mistakes
- Best practices
- Real-world examples
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 8 — AUTOCOMMIT, COMMIT & ROLLBACK**

Topics covered:

- Transactions
- ACID properties
- AUTOCOMMIT
- COMMIT
- ROLLBACK
- SAVEPOINT
- Transaction control
- Real-world banking examples
- Practice exercises