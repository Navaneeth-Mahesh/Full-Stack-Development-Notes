# Lesson 23 — SELF JOIN

## Learning Objectives

By the end of this lesson, you will understand:

- What a Self Join is
- Why Self Join is needed
- How aliases work
- Manager–Employee relationships
- Hierarchical data
- Different types of Self Joins
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# What is a Self Join?

A **Self Join** is a join where a table is joined **with itself**.

Instead of joining two different tables, we treat the same table as two separate copies.

Example:

```
Employees
        JOIN
Employees
```

Since both are the same table, we use **aliases** to distinguish them.

---

# Why Do We Need a Self Join?

Some tables store relationships within themselves.

Examples:

- Employee → Manager
- Student → Mentor
- Category → Parent Category
- Comment → Parent Comment
- Folder → Parent Folder

Instead of creating another table, we simply reference another row in the same table.

---

# Real-World Example

Imagine a company.

```
CEO

├── HR Manager
│      ├── Recruiter
│      └── Trainer
│
└── Tech Manager
       ├── Backend Developer
       └── Frontend Developer
```

Everyone is an employee.

Managers are also employees.

This is where Self Join becomes useful.

---

# Creating the Employees Table

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    manager_id INT
);
```

Notice:

```
manager_id
```

stores another employee's ID.

---

# Sample Data

```sql
INSERT INTO employees VALUES
(1,'Alice',NULL),
(2,'Bob',1),
(3,'Charlie',1),
(4,'David',2),
(5,'Emma',2),
(6,'Frank',3);
```

Table:

| employee_id | employee_name | manager_id |
|-------------|---------------|------------|
|1|Alice|NULL|
|2|Bob|1|
|3|Charlie|1|
|4|David|2|
|5|Emma|2|
|6|Frank|3|

Hierarchy:

```
Alice

├── Bob
│      ├── David
│      └── Emma
│
└── Charlie
       └── Frank
```

---

# Why Aliases Are Needed

If we write:

```sql
SELECT *
FROM employees
JOIN employees;
```

MySQL doesn't know which table each column belongs to.

It throws an error.

We must give different names.

Example:

```sql
employees e
employees m
```

Here:

```
e = employee

m = manager
```

---

# Basic Self Join

```sql
SELECT
e.employee_name,
m.employee_name
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id;
```

Output:

| Employee | Manager |
|-----------|----------|
|Bob|Alice|
|Charlie|Alice|
|David|Bob|
|Emma|Bob|
|Frank|Charlie|

Explanation:

```
Employee Table
        ↓
manager_id

matches

Manager Table
employee_id
```

---

# Understanding the Join

For Bob:

```
employee_id = 2

manager_id = 1
```

Find:

```
employee_id = 1
```

Result:

```
Manager = Alice
```

---

# Renaming Columns

```sql
SELECT
e.employee_name AS Employee,
m.employee_name AS Manager
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id;
```

Output:

| Employee | Manager |
|-----------|----------|
|Bob|Alice|
|Charlie|Alice|
|David|Bob|

Much easier to read.

---

# LEFT SELF JOIN

What about employees without managers?

Alice has:

```
manager_id = NULL
```

A normal JOIN hides Alice.

To include everyone:

```sql
SELECT
e.employee_name,
m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id;
```

Output:

| Employee | Manager |
|-----------|----------|
|Alice|NULL|
|Bob|Alice|
|Charlie|Alice|
|David|Bob|
|Emma|Bob|
|Frank|Charlie|

LEFT JOIN keeps every employee.

---

# Finding Only Top-Level Managers

```sql
SELECT *
FROM employees
WHERE manager_id IS NULL;
```

Output:

| employee_name |
|---------------|
|Alice|

Alice is the CEO.

---

# Finding Everyone Under Bob

First find Bob's ID.

```
Bob = 2
```

Then:

```sql
SELECT *
FROM employees
WHERE manager_id = 2;
```

Output:

| employee_name |
|---------------|
|David|
|Emma|

---

# Employee Count Per Manager

```sql
SELECT
m.employee_name AS Manager,
COUNT(*) AS Team_Size
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id
GROUP BY m.employee_name;
```

Output:

| Manager | Team_Size |
|----------|-----------|
|Alice|2|
|Bob|2|
|Charlie|1|

---

# Example: Categories

Imagine an e-commerce website.

```
Electronics

├── Phones
├── Laptops
└── Watches
```

Table:

| id | category | parent_id |
|----|----------|-----------|
|1|Electronics|NULL|
|2|Phones|1|
|3|Laptops|1|
|4|Watches|1|

Self Join:

```sql
SELECT
c.category,
p.category AS Parent
FROM categories c
LEFT JOIN categories p
ON c.parent_id = p.id;
```

Output:

| Category | Parent |
|-----------|----------|
|Electronics|NULL|
|Phones|Electronics|
|Laptops|Electronics|
|Watches|Electronics|

---

# Example: Comments

Social media comments.

```
Nice Post

├── Thanks
│
└── Great
```

Table:

| id | comment | parent_id |
|----|----------|-----------|
|1|Nice Post|NULL|
|2|Thanks|1|
|3|Great|1|

Self Join shows replies.

---

# Example: File System

```
Documents

├── Resume.pdf
├── Notes.txt
└── Projects
```

Each folder references another folder.

Perfect use case for Self Join.

---

# INNER vs LEFT Self Join

### INNER JOIN

Returns only rows with matching managers.

```
Alice disappears
```

---

### LEFT JOIN

Returns all employees.

```
Alice appears
Manager = NULL
```

---

# Common Mistakes

## Forgetting Aliases

Wrong:

```sql
SELECT *
FROM employees
JOIN employees;
```

Error:

```
Not unique table/alias
```

Correct:

```sql
employees e
employees m
```

---

## Wrong Join Condition

Wrong:

```sql
ON e.employee_id = m.employee_id
```

This matches the same row.

Correct:

```sql
ON e.manager_id = m.employee_id
```

---

## Confusing Employee and Manager

Remember:

```
Employee.manager_id

matches

Manager.employee_id
```

---

# Best Practices

- Always use aliases (`e`, `m`) for readability.
- Use meaningful alias names when queries get larger.
- Prefer `LEFT JOIN` if you want to include top-level records.
- Ensure self-referencing columns are indexed for better performance.
- Avoid ambiguous column names by prefixing them with aliases.

---

# Interview Questions

### 1. What is a Self Join?

A Self Join joins a table with itself to compare related rows.

---

### 2. Why do we use aliases?

To treat the same table as two separate logical tables.

---

### 3. Give a real-world use case.

Employee–Manager hierarchy.

---

### 4. Can a Self Join use LEFT JOIN?

Yes.

It includes rows without matching parent records.

---

### 5. Does a Self Join require two tables?

No.

It uses the same table twice.

---

# Practice Exercises

## Exercise 1

Create:

```sql
employees
```

table.

---

## Exercise 2

Insert at least six employees.

---

## Exercise 3

Display:

```
Employee
Manager
```

using a Self Join.

---

## Exercise 4

Show every employee including the CEO.

---

## Exercise 5

Count how many employees work under each manager.

---

## Exercise 6

Create a `categories` table with:

```
id
category
parent_id
```

Display each category with its parent.

---

## Exercise 7

Create a `folders` table representing a file system and use a Self Join to show each folder with its parent folder.

---

# Mini Project

Design a simple company hierarchy.

Tables:

```
employees
```

Requirements:

- CEO has no manager.
- Managers report to the CEO.
- Developers report to managers.
- Display every employee with their manager.
- Show team size for each manager.

---

# Summary

In this lesson, you learned:

- What a Self Join is
- Why it is needed
- Self Join syntax
- Table aliases
- Employee–Manager relationships
- Hierarchical data
- INNER vs LEFT Self Join
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 24 — Views**

Topics covered:

- What is a View?
- Creating Views
- Updating Views
- Dropping Views
- Advantages and limitations
- Real-world use cases
- Practice exercises