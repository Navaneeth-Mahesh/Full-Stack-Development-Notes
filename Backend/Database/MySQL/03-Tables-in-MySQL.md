# Lesson 3 — Tables in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What a table is
- Rows and columns
- Data types
- Creating tables
- Viewing table structure
- Renaming tables
- Altering tables
- Deleting tables
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# What is a Table?

A **table** is where data is actually stored inside a database.

Think of a database as a **folder**, and tables as **files** inside that folder.

Example:

```
college_db
│
├── students
├── teachers
├── courses
└── attendance
```

Each table stores a specific type of information.

---

# Real-World Example

Imagine you're building a college management system.

Instead of storing everything in one place, you organize data into separate tables:

```
students
teachers
courses
departments
fees
attendance
```

This keeps data organized and easier to manage.

---

# Table Structure

Every table consists of:

- Columns (Attributes)
- Rows (Records)

Example:

Students Table

| StudentID | Name | Age | Branch |
|-----------|------|-----|--------|
| 1 | Navaneeth | 20 | CSE |
| 2 | Rahul | 21 | ECE |
| 3 | Sneha | 19 | IT |

Here:

Columns:

- StudentID
- Name
- Age
- Branch

Rows:

Each student's complete information.

---

# Understanding Rows and Columns

Columns describe **what information** is stored.

Rows store **actual data**.

Example:

```
Name
Age
City
```

These are columns.

```
Rahul | 21 | Hyderabad
```

This entire line is one row.

---

# What is a Schema?

A schema defines the structure of a table.

It includes:

- Column names
- Data types
- Constraints

Example:

```
students

StudentID INT
Name VARCHAR(100)
Age INT
```

This is called the table schema.

---

# Data Types

Every column must have a data type.

Common MySQL Data Types:

| Data Type | Description |
|------------|-------------|
| INT | Whole numbers |
| FLOAT | Decimal numbers |
| DOUBLE | Large decimal values |
| CHAR(n) | Fixed-length text |
| VARCHAR(n) | Variable-length text |
| TEXT | Long text |
| DATE | YYYY-MM-DD |
| TIME | HH:MM:SS |
| DATETIME | Date and time |
| BOOLEAN | TRUE/FALSE |
| DECIMAL(p,s) | Exact decimal values |

---

# Choosing the Right Data Type

Example:

```
StudentID → INT

Name → VARCHAR(100)

Age → INT

Salary → DECIMAL(10,2)

DOB → DATE
```

Choosing appropriate data types improves performance and saves storage.

---

# Creating a Table

Syntax:

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

Example:

```sql
CREATE TABLE students (
    StudentID INT,
    Name VARCHAR(100),
    Age INT,
    Branch VARCHAR(50)
);
```

Output:

```
Query OK
```

---

# Viewing All Tables

To see all tables in the selected database:

```sql
SHOW TABLES;
```

Example Output:

```
students
teachers
courses
```

---

# Viewing Table Structure

Use:

```sql
DESCRIBE students;
```

or

```sql
DESC students;
```

Output:

| Field | Type | Null | Key | Default | Extra |
|-------|------|------|-----|---------|------|
| StudentID | int | YES | | NULL | |
| Name | varchar(100) | YES | | NULL | |
| Age | int | YES | | NULL | |
| Branch | varchar(50) | YES | | NULL | |

---

# Understanding DESCRIBE Output

Field

→ Column name

Type

→ Data type

Null

→ Can it contain NULL?

Key

→ Primary or Foreign Key

Default

→ Default value

Extra

→ AUTO_INCREMENT etc.

---

# Renaming a Table

Syntax:

```sql
RENAME TABLE old_name TO new_name;
```

Example:

```sql
RENAME TABLE students TO student_details;
```

Output:

```
Query OK
```

---

# Altering a Table

The `ALTER TABLE` command modifies an existing table.

You can:

- Add columns
- Remove columns
- Rename columns
- Change data types

---

# Add a Column

Syntax:

```sql
ALTER TABLE students
ADD Email VARCHAR(100);
```

New structure:

```
StudentID
Name
Age
Branch
Email
```

---

# Add Multiple Columns

```sql
ALTER TABLE students
ADD Phone VARCHAR(15),
ADD Address VARCHAR(255);
```

---

# Drop (Remove) a Column

```sql
ALTER TABLE students
DROP COLUMN Address;
```

The Address column is permanently deleted.

---

# Rename a Column

MySQL 8.0+:

```sql
ALTER TABLE students
RENAME COLUMN Branch TO Department;
```

---

# Modify a Column Data Type

Example:

```sql
ALTER TABLE students
MODIFY Age SMALLINT;
```

Age is now stored as SMALLINT instead of INT.

---

# Delete a Table

Syntax:

```sql
DROP TABLE table_name;
```

Example:

```sql
DROP TABLE students;
```

This permanently deletes:

- Table
- Data
- Structure

Be careful—this cannot be undone.

---

# Prevent Errors

Instead of:

```sql
DROP TABLE students;
```

Use:

```sql
DROP TABLE IF EXISTS students;
```

If the table doesn't exist, MySQL won't throw an error.

---

# Temporary vs Permanent Changes

Commands like:

```sql
ALTER TABLE
```

and

```sql
DROP TABLE
```

change the database permanently.

Always verify before executing.

---

# Real-World Example

An e-commerce application might have:

Products Table

| ProductID | Name | Price | Stock |
|-----------|------|-------|------|

Users Table

| UserID | Name | Email |

Orders Table

| OrderID | UserID | Total |

Each table stores different types of data but belongs to the same database.

---

# Common Mistakes

## 1. Creating a table without selecting a database

```sql
CREATE TABLE students (...);
```

Error:

```
No database selected
```

Solution:

```sql
USE college_db;
```

---

## 2. Using duplicate table names

```sql
CREATE TABLE students (...);
```

when the table already exists.

Solution:

```sql
CREATE TABLE IF NOT EXISTS students (...);
```

---

## 3. Forgetting commas

Incorrect:

```sql
CREATE TABLE students(
StudentID INT
Name VARCHAR(100)
);
```

Correct:

```sql
CREATE TABLE students(
StudentID INT,
Name VARCHAR(100)
);
```

---

## 4. Using wrong data types

Incorrect:

```sql
Age VARCHAR(100)
```

Better:

```sql
Age INT
```

Choose data types based on the data you plan to store.

---

# Best Practices

- Use meaningful table names.
- Use lowercase names.
- Use singular or plural consistently (e.g., `student` or `students`).
- Choose appropriate data types.
- Avoid unnecessary columns.
- Keep related data in separate tables.
- Always review changes before using `ALTER` or `DROP`.

---

# Interview Questions

### 1. What is a table?

A table stores related data in rows and columns.

---

### 2. Difference between a database and a table?

- Database → Collection of tables.
- Table → Collection of related rows and columns.

---

### 3. Which command creates a table?

```sql
CREATE TABLE
```

---

### 4. Which command displays all tables?

```sql
SHOW TABLES;
```

---

### 5. Which command displays a table's structure?

```sql
DESCRIBE table_name;
```

or

```sql
DESC table_name;
```

---

### 6. Which command changes a table's structure?

```sql
ALTER TABLE
```

---

### 7. Which command deletes a table?

```sql
DROP TABLE
```

---

# Practice Exercises

## Exercise 1

Create a database:

```sql
CREATE DATABASE IF NOT EXISTS college_db;
```

Select it:

```sql
USE college_db;
```

---

## Exercise 2

Create a table named `students` with:

- StudentID
- Name
- Age
- Branch

---

## Exercise 3

Display all tables.

---

## Exercise 4

Describe the `students` table.

---

## Exercise 5

Add a column:

```
Email
```

---

## Exercise 6

Add another column:

```
Phone
```

---

## Exercise 7

Rename `Branch` to `Department`.

---

## Exercise 8

Modify the `Phone` column to:

```sql
VARCHAR(20)
```

---

## Exercise 9

Remove the `Phone` column.

---

## Exercise 10

Rename the table:

```
students
```

to

```
student_details
```

---

## Exercise 11

Delete the table using:

```sql
DROP TABLE IF EXISTS student_details;
```

---

# Mini Project

Create a database:

```text
library_db
```

Inside it, create three tables:

### books

- BookID
- Title
- Author
- Price

### members

- MemberID
- Name
- Email

### borrow_records

- BorrowID
- BookID
- MemberID
- BorrowDate

After creating them:

- Display all tables.
- Describe each table.
- Add a `Phone` column to `members`.
- Rename `borrow_records` to `loans`.
- Drop the `Phone` column.
- Verify the updated structure.

---

# Summary

In this lesson, you learned:

- What a table is
- Rows and columns
- Table schema
- MySQL data types
- `CREATE TABLE`
- `SHOW TABLES`
- `DESCRIBE` / `DESC`
- `ALTER TABLE`
- `RENAME TABLE`
- `DROP TABLE`
- Best practices
- Common mistakes
- Practice exercises

---

# Next Lesson

**Lesson 4 — INSERT Rows**

Topics covered:

- `INSERT INTO`
- Inserting single rows
- Inserting multiple rows
- Inserting partial data
- Handling `NULL`
- Common errors
- Real-world examples
- Practice exercises