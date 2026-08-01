# Lesson 29 — ON DELETE

## Learning Objectives

By the end of this lesson, you will understand:

- What `ON DELETE` is
- Why it is used with foreign keys
- Parent-child relationships
- `ON DELETE CASCADE`
- `ON DELETE SET NULL`
- `ON DELETE RESTRICT`
- `ON DELETE NO ACTION`
- When to use each option
- Real-world examples
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Introduction

In the previous lesson, you learned about **Foreign Keys**, which create relationships between tables.

But an important question remains:

> **What should happen to child records when a parent record is deleted?**

This is where **ON DELETE** comes into play.

`ON DELETE` tells MySQL **how to handle child rows when the referenced parent row is deleted**.

---

# Parent-Child Relationship

Imagine two tables:

## Departments (Parent)

| department_id | department_name |
|--------------:|-----------------|
| 1 | Computer Science |
| 2 | Electronics |

---

## Students (Child)

| student_id | name | department_id |
|-----------:|------|--------------:|
|101|Navaneeth|1|
|102|Rahul|1|
|103|Anjali|2|

Relationship:

```
Departments
     │
     │
     ▼
Students
```

`department_id` in **Students** references **Departments**.

Now imagine deleting:

```
Computer Science
```

What happens to Navaneeth and Rahul?

Different `ON DELETE` rules give different answers.

---

# Foreign Key Syntax

```sql
FOREIGN KEY (department_id)
REFERENCES departments(department_id)
ON DELETE action;
```

Where `action` can be:

- CASCADE
- SET NULL
- RESTRICT
- NO ACTION

---

# Sample Database

## Parent Table

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);
```

---

## Child Table

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
    ON DELETE CASCADE
);
```

We'll change only the last line in different examples.

---

# 1. ON DELETE CASCADE

## Meaning

When a parent row is deleted,

➡ Delete all matching child rows automatically.

---

Example

Departments

| ID | Name |
|---:|------|
|1|CSE|
|2|ECE|

Students

|ID|Student|Dept|
|--:|-------|---:|
|1|Navaneeth|1|
|2|Rahul|1|
|3|Anjali|2|

Delete:

```sql
DELETE FROM departments
WHERE department_id = 1;
```

Result:

Departments

|ID|Name|
|--:|----|
|2|ECE|

Students

|ID|Student|Dept|
|--:|-------|---:|
|3|Anjali|2|

Navaneeth and Rahul are automatically deleted.

---

## Visualization

Before

```
Department 1
   │
   ├── Navaneeth
   └── Rahul
```

Delete Department 1

↓

After

```
Department removed

Navaneeth removed

Rahul removed
```

Everything connected disappears.

---

## When to Use CASCADE

Good for:

- Order → Order Items
- Blog → Comments
- Playlist → Songs
- Invoice → Invoice Details

Deleting the parent should also delete related data.

---

# 2. ON DELETE SET NULL

## Meaning

When the parent row is deleted,

The child row remains,

but the foreign key becomes `NULL`.

---

Example

Students

|Student|Department|
|--------|---------:|
|Navaneeth|1|
|Rahul|1|

Delete Department 1

Result

|Student|Department|
|--------|----------|
|Navaneeth|NULL|
|Rahul|NULL|

Students remain.

Only their department reference disappears.

---

## Important

The foreign key column **must allow NULL values**.

Correct:

```sql
department_id INT NULL
```

Wrong:

```sql
department_id INT NOT NULL
```

Otherwise MySQL cannot set it to `NULL`.

---

Example

```sql
FOREIGN KEY (department_id)
REFERENCES departments(department_id)
ON DELETE SET NULL;
```

---

## When to Use

Useful for:

- Employees leaving departments
- Books whose authors are deleted
- Customers whose sales representative leaves

Keep the record,

remove only the relationship.

---

# 3. ON DELETE RESTRICT

## Meaning

Do **not allow** deletion of the parent if child records exist.

---

Example

Departments

|ID|
|--:|
|1|

Students

|Student|Dept|
|--------|---:|
|Navaneeth|1|

Try:

```sql
DELETE FROM departments
WHERE department_id = 1;
```

MySQL says:

```
Cannot delete

Child records exist.
```

Deletion fails.

---

Visualization

```
Department
     │
     ▼
Students

Delete?

❌ Not Allowed
```

---

## When to Use

Best for:

- Banks
- Hospitals
- Government records
- Financial transactions

Where deleting parent data could corrupt historical records.

---

# 4. ON DELETE NO ACTION

## Meaning

In MySQL, `NO ACTION` behaves the same as `RESTRICT`.

It prevents deleting the parent row while child rows reference it.

Example:

```sql
FOREIGN KEY (department_id)
REFERENCES departments(department_id)
ON DELETE NO ACTION;
```

Attempting to delete a referenced department results in an error.

---

## Difference Between RESTRICT and NO ACTION

### SQL Standard

- **RESTRICT** checks immediately.
- **NO ACTION** may delay the check until the end of the transaction (in databases that support deferred constraints).

### MySQL

MySQL treats both the same.

So in MySQL:

```
RESTRICT == NO ACTION
```

---

# Comparison Table

| Action | Parent Deleted? | Child Rows |
|---------|-----------------|------------|
|CASCADE|Yes|Deleted automatically|
|SET NULL|Yes|Foreign key becomes NULL|
|RESTRICT|No|Deletion blocked|
|NO ACTION|No|Deletion blocked (same as RESTRICT in MySQL)|

---

# Complete Example

Create Parent

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
```

Create Child

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
    ON DELETE CASCADE
);
```

Insert Departments

```sql
INSERT INTO departments VALUES
(1,'CSE'),
(2,'ECE');
```

Insert Students

```sql
INSERT INTO students VALUES
(101,'Navaneeth',1),
(102,'Rahul',1),
(103,'Anjali',2);
```

Delete

```sql
DELETE FROM departments
WHERE department_id=1;
```

Students referencing department 1 disappear automatically.

---

# Real-World Examples

## E-Commerce

```
Orders
      │
      ▼
Order Items
```

Delete Order

↓

Delete all order items.

Use:

```
CASCADE
```

---

## HR System

```
Departments
      │
      ▼
Employees
```

Delete Department

↓

Employees stay,

Department becomes NULL.

Use:

```
SET NULL
```

---

## Banking

```
Customers
      │
      ▼
Transactions
```

Delete Customer?

Never.

Use:

```
RESTRICT
```

---

## University

```
Departments
      │
      ▼
Students
```

Depending on business rules:

- Delete students too → `CASCADE`
- Keep students without a department → `SET NULL`
- Prevent deletion while students exist → `RESTRICT`

---

# Common Mistakes

## Mistake 1

Using `SET NULL`

but column is:

```sql
department_id INT NOT NULL
```

This will fail because `NULL` cannot be stored.

---

## Mistake 2

Using `CASCADE` without understanding its impact.

Deleting one parent row can remove hundreds or thousands of child records.

Always double-check before running `DELETE`.

---

## Mistake 3

Assuming `NO ACTION` is different from `RESTRICT` in MySQL.

In MySQL, they behave the same.

---

# Best Practices

- Use `CASCADE` only when child data has no meaning without the parent.
- Use `SET NULL` when child data should remain.
- Use `RESTRICT` for financial or historical records.
- Review business rules before choosing an action.
- Test foreign key behavior on sample data before production.
- Keep backups before performing large delete operations.

---

# Interview Questions

## 1. What is `ON DELETE`?

It specifies what should happen to child rows when a referenced parent row is deleted.

---

## 2. What does `ON DELETE CASCADE` do?

Deletes all related child rows automatically.

---

## 3. What does `ON DELETE SET NULL` do?

Sets the foreign key column in child rows to `NULL` while keeping the rows.

---

## 4. What does `ON DELETE RESTRICT` do?

Prevents deletion of the parent row if child rows exist.

---

## 5. Is `NO ACTION` different from `RESTRICT` in MySQL?

No. In MySQL they behave the same.

---

## 6. When would you use `CASCADE`?

When child records should not exist without the parent (for example, order items belonging to an order).

---

## 7. Why must a column allow `NULL` for `SET NULL`?

Because MySQL needs to store `NULL` in the foreign key column after deleting the parent.

---

# Practice Exercises

### Exercise 1

Create:

- `departments`
- `students`

Use:

```sql
ON DELETE CASCADE
```

Delete one department and observe the result.

---

### Exercise 2

Recreate the tables using:

```sql
ON DELETE SET NULL
```

Delete a department and check the students table.

---

### Exercise 3

Recreate the tables using:

```sql
ON DELETE RESTRICT
```

Try deleting a department with existing students.

Observe the error.

---

### Exercise 4

Replace `RESTRICT` with:

```sql
ON DELETE NO ACTION
```

Verify that the behavior is identical in MySQL.

---

# Summary

In this lesson, you learned:

- Parent-child relationships
- Why `ON DELETE` is needed
- `ON DELETE CASCADE`
- `ON DELETE SET NULL`
- `ON DELETE RESTRICT`
- `ON DELETE NO ACTION`
- Differences between each action
- Real-world use cases
- Common mistakes
- Best practices
- Interview questions
- Hands-on practice

---

# Next Lesson

**Lesson 30 — Stored Procedures**

Topics covered:

- What are Stored Procedures?
- Why use them?
- Creating procedures
- Calling procedures
- Parameters (`IN`, `OUT`, `INOUT`)
- Variables
- Real-world examples
- Best practices