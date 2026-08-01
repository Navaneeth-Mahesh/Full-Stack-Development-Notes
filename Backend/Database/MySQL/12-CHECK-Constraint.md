# Lesson 12 — CHECK Constraint

## Learning Objectives

By the end of this lesson, you will understand:

- What a CHECK constraint is
- Why CHECK constraints are important
- How to create CHECK constraints
- Validating numeric ranges
- Restricting allowed values
- CHECK with UPDATE statements
- CHECK with multiple conditions
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# What is a CHECK Constraint?

A **CHECK constraint** is used to ensure that the values entered into a column satisfy a specific condition.

If the condition is **true**, the data is inserted or updated.

If the condition is **false**, MySQL rejects the operation.

Think of it as a security guard that checks whether the data follows your business rules before allowing it into the database.

---

# Why Use CHECK Constraints?

Without validation:

```
Age = -5
Salary = -10000
Marks = 150
Gender = ABC
```

All of these are invalid values.

With CHECK constraints:

```
Age = 20 ✔

Marks = 95 ✔

Salary = 50000 ✔

Gender = Male ✔
```

Invalid data is rejected automatically.

---

# Syntax

```sql
CREATE TABLE table_name (
    column_name datatype CHECK (condition)
);
```

Example:

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT CHECK(age >= 18)
);
```

---

# Example 1 — Minimum Age

Create the table:

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT CHECK(age >= 18)
);
```

Insert valid data:

```sql
INSERT INTO students
VALUES
(1,'Navaneeth',20);
```

Output:

```
Query OK
```

Insert invalid data:

```sql
INSERT INTO students
VALUES
(2,'Rahul',15);
```

Output:

```
ERROR:
Check constraint violated.
```

The row is not inserted.

---

# Example 2 — Marks Between 0 and 100

```sql
CREATE TABLE exams(
    student_id INT,
    marks INT CHECK(marks BETWEEN 0 AND 100)
);
```

Valid:

```sql
INSERT INTO exams
VALUES (1,95);
```

Valid:

```sql
INSERT INTO exams
VALUES (2,0);
```

Valid:

```sql
INSERT INTO exams
VALUES (3,100);
```

Invalid:

```sql
INSERT INTO exams
VALUES (4,120);
```

Rejected.

---

# Example 3 — Positive Salary

```sql
CREATE TABLE employees(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2)
    CHECK(salary > 0)
);
```

Allowed:

```
45000

25000

80000
```

Rejected:

```
0

-500

-10000
```

---

# Restricting Allowed Values

CHECK is useful for limiting values.

Example:

```sql
CREATE TABLE employees(
    id INT,
    gender VARCHAR(10)
    CHECK(gender IN ('Male','Female'))
);
```

Allowed:

```
Male

Female
```

Rejected:

```
Unknown

ABC

Boy

Girl
```

---

# Example 4 — Product Quantity

```sql
CREATE TABLE products(
    id INT,
    quantity INT CHECK(quantity >= 0)
);
```

Allowed:

```
0

5

10

200
```

Rejected:

```
-1

-25
```

---

# Example 5 — Product Price

```sql
CREATE TABLE products(
    product_id INT,
    price DECIMAL(10,2)
    CHECK(price > 0)
);
```

Valid:

```
199

2500

799.99
```

Rejected:

```
0

-300
```

---

# Using Multiple Conditions

You can combine conditions.

Example:

```sql
CREATE TABLE students(
    id INT,
    age INT,
    marks INT,
    CHECK(age >=18 AND marks BETWEEN 0 AND 100)
);
```

Valid:

```
Age = 20

Marks = 95
```

Rejected:

```
Age = 17

Marks = 110
```

Both conditions must be true.

---

# CHECK with OR

Example:

```sql
CREATE TABLE employees(
    id INT,
    department VARCHAR(20),
    CHECK(
        department='HR'
        OR
        department='IT'
    )
);
```

Allowed:

```
HR

IT
```

Rejected:

```
Sales

Marketing
```

---

# CHECK with UPDATE

CHECK constraints also apply to UPDATE statements.

Table:

```sql
CREATE TABLE students(
    id INT,
    age INT CHECK(age>=18)
);
```

Insert:

```sql
INSERT INTO students
VALUES(1,20);
```

Now update:

```sql
UPDATE students
SET age=15
WHERE id=1;
```

Output:

```
ERROR

Check constraint violated.
```

The value is not updated.

---

# Real-World Example — Banking

```sql
balance >= 0
```

Customers cannot have a negative account balance if the rule requires non-negative values.

---

# Real-World Example — Online Shopping

```sql
quantity >=0
```

Inventory can never be negative.

---

# Real-World Example — School

```
marks BETWEEN 0 AND 100
```

Marks cannot exceed the maximum allowed value.

---

# Real-World Example — Employee Portal

```
salary > 0
```

Negative salaries are not allowed.

---

# Named CHECK Constraints

You can give a CHECK constraint a name.

```sql
CREATE TABLE employees(
    id INT,
    salary DECIMAL(10,2),
    CONSTRAINT chk_salary
    CHECK(salary>0)
);
```

This makes it easier to identify the constraint if an error occurs.

---

# Common Mistakes

## Mistake 1

```sql
CHECK(age > 18)
```

This excludes 18.

If the rule is "18 or older", use:

```sql
CHECK(age >=18)
```

---

## Mistake 2

Forgetting the range.

Wrong:

```sql
CHECK(marks >0)
```

Allows:

```
101

500

1000
```

Better:

```sql
CHECK(marks BETWEEN 0 AND 100)
```

---

## Mistake 3

Using incorrect values.

Wrong:

```sql
CHECK(status='YES')
```

If multiple values are allowed:

```sql
CHECK(status IN ('YES','NO'))
```

---

# Advantages

- Improves data quality
- Prevents invalid values
- Reduces application-side validation
- Enforces business rules
- Keeps data consistent

---

# Limitations

- Cannot validate data from another table
- Cannot replace FOREIGN KEY constraints
- Complex business logic should still be handled in the application when necessary

---

# Best Practices

- Use CHECK whenever there are business rules.
- Keep conditions simple and readable.
- Use BETWEEN for numeric ranges.
- Use IN for predefined values.
- Give important constraints meaningful names.
- Combine CHECK with NOT NULL and PRIMARY KEY for stronger validation.

---

# Interview Questions

### 1. What is a CHECK constraint?

A CHECK constraint restricts the values that can be stored in a column by enforcing a condition.

---

### 2. Does CHECK work during UPDATE?

Yes. CHECK constraints are validated during both INSERT and UPDATE operations.

---

### 3. Can CHECK contain multiple conditions?

Yes.

Example:

```sql
CHECK(age>=18 AND salary>0)
```

---

### 4. Which operator is commonly used to restrict specific values?

```sql
IN
```

Example:

```sql
CHECK(status IN ('Active','Inactive'))
```

---

### 5. What happens if a CHECK condition fails?

The INSERT or UPDATE operation is rejected, and the data is not stored.

---

# Practice Exercises

## Exercise 1

Create a table where age must be at least 18.

---

## Exercise 2

Create a table where salary must be greater than 0.

---

## Exercise 3

Create a table where marks must be between 0 and 100.

---

## Exercise 4

Create a table where quantity cannot be negative.

---

## Exercise 5

Create a table where gender can only be:

```
Male

Female
```

using the `IN` operator.

---

## Exercise 6

Create a table with:

- Age must be at least 18
- Salary must be greater than 10000

using multiple CHECK conditions.

---

# Mini Project

Create a **College Admission** table.

Requirements:

- Student ID → Primary Key
- Name → Cannot be NULL
- Age → Must be at least 18
- Percentage → Between 0 and 100
- Gender → Only 'Male', 'Female', or 'Other'

Insert:

- 3 valid records
- 3 invalid records

Observe which inserts succeed and which are rejected.

---

# Summary

In this lesson, you learned:

- What a CHECK constraint is
- Why CHECK constraints are useful
- Creating CHECK constraints
- Validating numeric ranges
- Restricting allowed values using `IN`
- Using CHECK with `UPDATE`
- Combining multiple conditions with `AND` and `OR`
- Named CHECK constraints
- Common mistakes
- Best practices
- Practice exercises

---

# Next Lesson

**Lesson 13 — PRIMARY KEY**

Topics covered:

- What is a Primary Key?
- Characteristics of a Primary Key
- Single vs Composite Primary Keys
- Creating Primary Keys
- Composite Keys
- PRIMARY KEY with AUTO_INCREMENT
- Real-world examples
- Best practices
- Practice exercises