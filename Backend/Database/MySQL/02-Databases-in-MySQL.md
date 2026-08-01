# Lesson 2 — Databases in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What a database is
- Why databases are used
- How to create a database
- How to view databases
- How to select a database
- How to delete a database
- Database naming conventions
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# What is a Database?

A **database** is an organized collection of related data.

Think of it like a digital folder that stores information.

Example:

A college management system may have one database named:

```
college_db
```

Inside this database you can have multiple tables:

```
college_db
│
├── students
├── teachers
├── courses
├── departments
└── attendance
```

A database is simply a container for tables.

---

# Why Do We Need Databases?

Imagine storing student information inside Excel files.

Problems:

- Difficult to search
- Duplicate data
- No security
- Hard to manage
- Multiple users cannot work efficiently

Databases solve these problems.

Advantages:

- Fast searching
- Better organization
- Data security
- Backup support
- Supports millions of records
- Multiple users can access data simultaneously

---

# Database Hierarchy

```
MySQL Server
│
├── Database 1
│      ├── Table
│      ├── Table
│      └── Table
│
├── Database 2
│      ├── Table
│      └── Table
│
└── Database 3
       ├── Table
       └── Table
```

Think of it like:

```
Computer
    ↓
Folder
    ↓
Files
```

Similarly,

```
MySQL Server
      ↓
Database
      ↓
Tables
```

---

# Viewing Existing Databases

SQL Command:

```sql
SHOW DATABASES;
```

Example Output:

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```

These databases are created automatically by MySQL.

---

# Understanding Default Databases

## information_schema

Stores metadata about databases, tables, columns, and indexes.

Think of it as MySQL's dictionary.

---

## mysql

Stores user accounts, passwords, permissions, and server settings.

Important:

Never modify these tables manually unless you know what you're doing.

---

## performance_schema

Stores server performance information.

Used by administrators to monitor MySQL.

---

## sys

Provides easy-to-read reports based on performance_schema.

Useful for optimization and debugging.

---

# Creating a Database

Syntax:

```sql
CREATE DATABASE database_name;
```

Example:

```sql
CREATE DATABASE college_db;
```

Output:

```
Query OK
```

A new database is now created.

---

# Verify the Database

Run:

```sql
SHOW DATABASES;
```

Output:

```
college_db
```

Your database now appears in the list.

---

# Selecting (Using) a Database

Before creating tables, you must choose the database.

Syntax:

```sql
USE database_name;
```

Example:

```sql
USE college_db;
```

Output:

```
Database changed
```

Now all operations will happen inside `college_db`.

---

# Check the Current Database

Command:

```sql
SELECT DATABASE();
```

Example Output:

```
college_db
```

If the output is:

```
NULL
```

No database is currently selected.

---

# Creating Multiple Databases

Example:

```sql
CREATE DATABASE hospital_db;

CREATE DATABASE school_db;

CREATE DATABASE ecommerce_db;
```

Each database is completely separate.

---

# Viewing the Current Database

```sql
SELECT DATABASE();
```

Example Output:

```
ecommerce_db
```

---

# Deleting a Database

Syntax:

```sql
DROP DATABASE database_name;
```

Example:

```sql
DROP DATABASE school_db;
```

Output:

```
Query OK
```

The database and all its tables are permanently deleted.

---

# Warning

This command:

```sql
DROP DATABASE college_db;
```

Deletes:

- Database
- Tables
- Data
- Relationships

Everything is lost.

There is no Undo.

Always be careful before using `DROP`.

---

# Prevent Errors Using IF EXISTS

Instead of:

```sql
DROP DATABASE college_db;
```

Use:

```sql
DROP DATABASE IF EXISTS college_db;
```

If the database doesn't exist, MySQL won't throw an error.

---

# Creating Only If It Doesn't Exist

Instead of:

```sql
CREATE DATABASE college_db;
```

Use:

```sql
CREATE DATABASE IF NOT EXISTS college_db;
```

If it already exists, MySQL simply skips creation.

This is considered good practice.

---

# Complete Example

```sql
CREATE DATABASE IF NOT EXISTS college_db;

SHOW DATABASES;

USE college_db;

SELECT DATABASE();
```

Expected Output:

```
college_db
```

---

# Database Naming Rules

A database name:

- Can contain letters
- Can contain numbers
- Can contain underscores (_)

Example:

```
student_db

college2026

inventory_system
```

Avoid:

```
College Database

my-db

123@db
```

Special characters and spaces should not be used.

---

# Naming Conventions

Good:

```
college_db

employee_db

inventory_db

bank_db
```

Bad:

```
test

abc

newdatabase

database1

mydb12345
```

Use meaningful names.

---

# Real-World Example

Imagine building an e-commerce website.

```
ecommerce_db
│
├── users
├── products
├── orders
├── cart
├── wishlist
└── payments
```

Each table stores related information inside one database.

---

# Common Errors

## Error 1

```sql
USE college_db;
```

Before creating it.

Output:

```
Unknown database
```

Solution:

Create the database first.

---

## Error 2

```sql
CREATE DATABASE college_db;
```

When it already exists.

Output:

```
Can't create database
```

Solution:

```sql
CREATE DATABASE IF NOT EXISTS college_db;
```

---

## Error 3

Trying to create tables without selecting a database.

Example:

```sql
CREATE TABLE students (...);
```

Output:

```
No database selected
```

Solution:

```sql
USE college_db;
```

---

# Best Practices

- Use meaningful database names.
- Use lowercase names.
- Separate projects into different databases.
- Use `IF NOT EXISTS` while creating.
- Use `IF EXISTS` while deleting.
- Never drop production databases accidentally.
- Backup databases regularly.

---

# Interview Questions

## 1. What is a database?

A database is an organized collection of related data.

---

## 2. Which command shows all databases?

```sql
SHOW DATABASES;
```

---

## 3. Which command selects a database?

```sql
USE database_name;
```

---

## 4. Which command creates a database?

```sql
CREATE DATABASE database_name;
```

---

## 5. Which command deletes a database?

```sql
DROP DATABASE database_name;
```

---

## 6. How do you check the current database?

```sql
SELECT DATABASE();
```

---

## 7. What is the purpose of `IF NOT EXISTS`?

It prevents an error if the database already exists.

---

# Practice Exercises

## Exercise 1

Create a database named:

```text
student_db
```

---

## Exercise 2

Create another database:

```text
company_db
```

---

## Exercise 3

Show all databases.

---

## Exercise 4

Select:

```text
student_db
```

---

## Exercise 5

Check the current database.

---

## Exercise 6

Delete:

```text
company_db
```

using:

```sql
DROP DATABASE IF EXISTS company_db;
```

---

# Mini Project

Create these databases:

```text
library_db

hospital_db

bank_db

restaurant_db
```

Use:

```sql
SHOW DATABASES;
```

to verify they were created.

Then:

- Select `library_db`
- Check the current database
- Delete `restaurant_db`

---

# Summary

In this lesson, you learned:

- What a database is
- Why databases are important
- Database hierarchy
- Default MySQL databases
- `SHOW DATABASES`
- `CREATE DATABASE`
- `USE`
- `SELECT DATABASE()`
- `DROP DATABASE`
- `IF EXISTS`
- `IF NOT EXISTS`
- Naming conventions
- Common mistakes
- Best practices
- Practice exercises

---

# Next Lesson

**Lesson 3 — Tables**

Topics covered:

- What is a table?
- Rows and Columns
- Data Types
- `CREATE TABLE`
- `DESCRIBE`
- `ALTER TABLE`
- `DROP TABLE`
- `RENAME TABLE`
- Real-world examples
- Practice exercises