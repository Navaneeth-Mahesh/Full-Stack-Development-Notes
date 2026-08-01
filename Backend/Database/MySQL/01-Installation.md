# MySQL Introduction

## What is MySQL?

MySQL is an **open-source Relational Database Management System (RDBMS)** used to store, organize, retrieve, and manage data efficiently.

Instead of storing information in Excel sheets or text files, applications use databases like MySQL to manage data.

Examples:

- Instagram stores users
- Amazon stores products
- Netflix stores movies
- Banks store customer accounts

Most modern applications use a database.

---

# What is a Database?

A database is an organized collection of data.

Example:

Students

| ID | Name | Branch |
|----|------|---------|
|1|Navaneeth|CSE|
|2|Rahul|ECE|
|3|Sneha|IT|

Instead of saving this inside files, we save it inside MySQL.

---

# Why MySQL?

Advantages:

- Free and Open Source
- Fast
- Reliable
- Secure
- Supports millions of records
- Easy to learn
- Used by many companies

Examples:

- Facebook (initially)
- YouTube
- Twitter
- GitHub
- Shopify

---

# What is RDBMS?

RDBMS means

Relational Database Management System

It stores data in the form of **tables**.

Example

Students Table

| StudentID | Name | Age |
|-----------|------|-----|
|1|Navaneeth|20|
|2|Rahul|21|

Courses Table

| CourseID | Course |
|----------|---------|
|101|Java|
|102|Python|

These tables can be connected using relationships.

---

# SQL vs MySQL

Many beginners confuse these.

SQL

- Language
- Used to communicate with databases
- Standard language

Example

```sql
SELECT * FROM students;
```

MySQL

- Database software
- Understands SQL
- Stores the data

Think of it like:

English → Language

Google Chrome → Browser

Similarly,

SQL → Language

MySQL → Database Software

---

# How MySQL Works

Application

↓

SQL Query

↓

MySQL Server

↓

Database

↓

Result

Example

```sql
SELECT * FROM students;
```

MySQL searches the database and returns the matching records.

---

# Client and Server

MySQL has two parts.

## Server

Stores all data.

Handles requests.

Processes queries.

## Client

Where users type SQL queries.

Examples

- MySQL Workbench
- VS Code Extension
- Terminal
- Command Prompt

---

# Installing MySQL (Windows)

Step 1

Download

https://dev.mysql.com/downloads/

Choose

MySQL Installer

Community Edition

---

Step 2

Run Installer

Choose

Developer Default

This installs

- MySQL Server
- Workbench
- Shell
- Connectors

---

Step 3

Set Root Password

Example

```
root123
```

Remember this password.

---

Step 4

Finish installation.

---

# Installing MySQL (macOS)

Download

DMG Installer

Install normally.

Or use Homebrew

```bash
brew install mysql
```

Start MySQL

```bash
brew services start mysql
```

---

# Open MySQL Workbench

Connect using

Hostname

```
localhost
```

Port

```
3306
```

Username

```
root
```

Password

Your password

---

# First SQL Query

```sql
SELECT VERSION();
```

Output

```
8.4.x
```

---

# Common SQL Commands

Show databases

```sql
SHOW DATABASES;
```

Show current database

```sql
SELECT DATABASE();
```

Show tables

```sql
SHOW TABLES;
```

Exit MySQL

```sql
EXIT;
```

---

# SQL Statement Rules

Every statement ends with

```sql
;
```

Example

Correct

```sql
SELECT * FROM students;
```

Wrong

```sql
SELECT * FROM students
```

---

# Comments

Single line

```sql
-- This is a comment
```

Multi line

```sql
/*
This
is
a
comment
*/
```

---

# Case Sensitivity

These are the same

```sql
select * from students;
```

```sql
SELECT * FROM students;
```

Convention:

SQL keywords in uppercase

Table names in lowercase

---

# Real-World Example

Imagine Instagram.

Users Table

| ID | Username |
|----|----------|
|1|navaneeth|
|2|john|

Posts Table

| PostID | UserID | Caption |
|---------|--------|---------|
|1|1|Hello World|
|2|2|Vacation|

Everything is stored in MySQL.

---

# Best Practices

✔ Use meaningful table names

✔ Keep SQL keywords uppercase

✔ End every statement with ;

✔ Never share your root password

✔ Backup databases regularly

---

# Interview Questions

## 1. What is MySQL?

An open-source relational database management system.

---

## 2. Difference between SQL and MySQL?

SQL is the language.

MySQL is the database software.

---

## 3. What is RDBMS?

A database system that stores data in related tables.

---

## 4. Default MySQL Port?

3306

---

## 5. What is MySQL Workbench?

A graphical client used to interact with MySQL.

---

# Practice

1. Install MySQL.

2. Open Workbench.

3. Connect to localhost.

4. Run

```sql
SELECT VERSION();
```

5. Run

```sql
SHOW DATABASES;
```

6. Exit MySQL.

---

# Summary

In this lesson you learned:

- What MySQL is
- What a database is
- Difference between SQL and MySQL
- RDBMS
- MySQL architecture
- Installation
- MySQL Workbench
- Basic commands
- SQL syntax
- Comments
- Best practices

Next Lesson:

**02_Databases.md**

We'll learn:

- CREATE DATABASE
- DROP DATABASE
- USE DATABASE
- SHOW DATABASES
- Naming conventions
- Real examples