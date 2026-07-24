Here's a more detailed and well-structured version for your MySQL notes.

# Creating and Managing Tables in MySQL

## Introduction

A **table** is one of the most important objects in a database. It stores data in the form of **rows** and **columns**.

* **Rows** represent individual records.
* **Columns** represent the attributes (fields) of each record.

For example, an `employee` table may contain information such as employee ID, first name, salary, and hire date.

> **Important:** Before creating a table, make sure you have selected a database using the `USE` statement.

```sql
USE database_name;
```

---

# Creating a Table

Use the `CREATE TABLE` statement to create a new table inside the currently selected database.

## Syntax

```sql
CREATE TABLE table_name (
    column_name1 DATA_TYPE,
    column_name2 DATA_TYPE,
    column_name3 DATA_TYPE,
    ...
);
```

### Syntax Breakdown

| Keyword        | Description                                       |
| -------------- | ------------------------------------------------- |
| `CREATE TABLE` | Creates a new table.                              |
| `table_name`   | Name of the table you want to create.             |
| `column_name`  | Name of a column in the table.                    |
| `DATA_TYPE`    | Specifies what type of data the column can store. |

---

# Common MySQL Data Types

| Data Type      | Description                        | Example               |
| -------------- | ---------------------------------- | --------------------- |
| `INT`          | Stores whole numbers               | `101`                 |
| `BIGINT`       | Stores very large integers         | `9999999999`          |
| `VARCHAR(n)`   | Stores variable-length text        | `"John"`              |
| `CHAR(n)`      | Stores fixed-length text           | `"A"`                 |
| `TEXT`         | Stores long text                   | Paragraphs            |
| `DECIMAL(p,s)` | Stores exact decimal numbers       | `2500.75`             |
| `FLOAT`        | Stores approximate decimal numbers | `12.45`               |
| `DOUBLE`       | Stores large decimal values        | `98765.4321`          |
| `DATE`         | Stores a date                      | `2026-07-24`          |
| `TIME`         | Stores time                        | `14:30:00`            |
| `DATETIME`     | Stores date and time               | `2026-07-24 14:30:00` |
| `TIMESTAMP`    | Stores timestamp values            | Current timestamp     |
| `BOOLEAN`      | Stores `TRUE` or `FALSE` values    | `TRUE`                |

---

# Example: Creating an Employee Table

```sql
CREATE TABLE employee (
    emp_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5,2),
    hire_date DATE
);
```

### Explanation

| Column       | Data Type      | Description                                             |
| ------------ | -------------- | ------------------------------------------------------- |
| `emp_id`     | `INT`          | Stores the employee ID.                                 |
| `first_name` | `VARCHAR(50)`  | Stores the employee's first name (up to 50 characters). |
| `last_name`  | `VARCHAR(50)`  | Stores the employee's last name (up to 50 characters).  |
| `hourly_pay` | `DECIMAL(5,2)` | Stores the hourly salary with two decimal places.       |
| `hire_date`  | `DATE`         | Stores the employee's joining date.                     |

---

# Verify That the Table Was Created

To display all tables in the currently selected database:

```sql
SHOW TABLES;
```

Example output:

```text
+----------------+
| Tables_in_hr   |
+----------------+
| employee       |
+----------------+
```

---

# View the Table Structure

To see the columns, data types, and other details of a table:

```sql
DESCRIBE employee;
```

or

```sql
DESC employee;
```

Example output:

```text
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| emp_id      | int          | YES  |     | NULL    |       |
| first_name  | varchar(50)  | YES  |     | NULL    |       |
| last_name   | varchar(50)  | YES  |     | NULL    |       |
| hourly_pay  | decimal(5,2) | YES  |     | NULL    |       |
| hire_date   | date         | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
```

---

# Display All Data in a Table

Use the `SELECT` statement to retrieve records from a table.

## Syntax

```sql
SELECT * FROM table_name;
```

The `*` (asterisk) means **select all columns**.

### Example

```sql
SELECT * FROM employee;
```

If the table is empty, MySQL returns an empty result set.

Example output:

```text
Empty set
```

After inserting data, the output might look like:

```text
+--------+------------+-----------+------------+------------+
| emp_id | first_name | last_name | hourly_pay | hire_date  |
+--------+------------+-----------+------------+------------+
| 101    | John       | Smith     | 18.50      | 2025-05-10 |
| 102    | Alice      | Brown     | 22.75      | 2024-09-18 |
+--------+------------+-----------+------------+------------+
```

---

# Delete (Drop) a Table

If you no longer need a table, you can permanently remove it using the `DROP TABLE` statement.

## Syntax

```sql
DROP TABLE table_name;
```

### Example

```sql
DROP TABLE employee;
```

### What Happens?

* The table is permanently deleted.
* All rows stored in the table are removed.
* The table structure is deleted.
* Indexes, constraints, and other associated objects are also removed.
* This operation **cannot be undone**.

---

# Drop a Table Only If It Exists

To avoid an error when the table does not exist, use:

```sql
DROP TABLE IF EXISTS employee;
```

This command safely removes the table only if it is present.

---

# Difference Between DELETE, TRUNCATE, and DROP

| Command    | Deletes Data | Deletes Table Structure | Can Be Recovered (Transaction Dependent) |
| ---------- | ------------ | ----------------------- | ---------------------------------------- |
| `DELETE`   | Yes          | No                      | Usually Yes                              |
| `TRUNCATE` | Yes          | No                      | No                                       |
| `DROP`     | Yes          | Yes                     | No                                       |

---

# Common Errors

## No Database Selected

Error:

```text
ERROR 1046 (3D000): No database selected
```

Solution:

```sql
USE database_name;
```

---

## Table Already Exists

Error:

```text
ERROR 1050 (42S01): Table 'employee' already exists
```

Solution:

Use a different table name or remove the existing table.

You can also create the table only if it does not already exist:

```sql
CREATE TABLE IF NOT EXISTS employee (
    emp_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5,2),
    hire_date DATE
);
```

---

# Summary

| Command                                        | Description                                       |
| ---------------------------------------------- | ------------------------------------------------- |
| `CREATE TABLE table_name (...);`               | Creates a new table.                              |
| `SHOW TABLES;`                                 | Displays all tables in the current database.      |
| `DESCRIBE table_name;`                         | Displays the table structure.                     |
| `DESC table_name;`                             | Short form of `DESCRIBE`.                         |
| `SELECT * FROM table_name;`                    | Displays all records from a table.                |
| `DROP TABLE table_name;`                       | Permanently deletes a table and all its data.     |
| `DROP TABLE IF EXISTS table_name;`             | Deletes the table only if it exists.              |
| `CREATE TABLE IF NOT EXISTS table_name (...);` | Creates a table only if it doesn't already exist. |


