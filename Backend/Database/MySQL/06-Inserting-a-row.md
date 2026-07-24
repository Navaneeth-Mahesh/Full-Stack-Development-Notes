# Inserting Data into a Table in MySQL

## Introduction

After creating a table, the next step is to insert data into it. In MySQL, new records are added using the **`INSERT INTO`** statement.

Each row inserted into a table represents a single record.

For example, an `employee` table stores one employee per row, including details such as employee ID, name, email, salary, and hire date.

> **Note:** Before inserting data, ensure that:
>
> * The database is selected using the `USE` statement.
> * The table already exists.

---

# INSERT INTO Syntax

The basic syntax for inserting a single row is:

```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

### Syntax Breakdown

| Keyword       | Description                                      |
| ------------- | ------------------------------------------------ |
| `INSERT INTO` | Specifies the table where data will be inserted. |
| `table_name`  | Name of the table.                               |
| `VALUES`      | Contains the values for the new row.             |

> **Important:** The values must be provided in the **same order** as the columns were defined when the table was created.

---

# Inserting a Single Row

### Syntax

```sql
INSERT INTO table_name
VALUES (...);
```

### Example

Suppose the `employee` table has the following columns:

```text
email_id
emp_id
name
designation
salary
hire_date
```

Insert one employee record:

```sql
INSERT INTO employee
VALUES (
    'user@gmail.com',
    1,
    'User',
    'Testing',
    2500.12,
    '2026-07-24'
);
```

View the inserted record:

```sql
SELECT * FROM employee;
```

### Example Output

```text
+------------------+--------+------+-------------+---------+------------+
| email_id         | emp_id | name | designation | salary  | hire_date  |
+------------------+--------+------+-------------+---------+------------+
| user@gmail.com   |      1 | User | Testing     | 2500.12 | 2026-07-24 |
+------------------+--------+------+-------------+---------+------------+
```

---

# Inserting Multiple Rows

Instead of executing multiple `INSERT` statements, you can insert several records in a single query.

### Syntax

```sql
INSERT INTO table_name
VALUES
(value1, value2, ...),
(value1, value2, ...),
(value1, value2, ...);
```

### Example

```sql
INSERT INTO employee
VALUES
('john@gmail.com', 2, 'John', 'Developer', 4500.00, '2026-01-15'),
('alice@gmail.com', 3, 'Alice', 'Designer', 4200.50, '2026-03-10'),
('bob@gmail.com', 4, 'Bob', 'Manager', 6500.00, '2025-12-01');
```

Retrieve all records:

```sql
SELECT * FROM employee;
```

This inserts **three new rows** in a single SQL statement.

---

# Inserting Data into Specific Columns

Sometimes you don't want to insert values into every column. In that case, specify only the columns you want to populate.

### Syntax

```sql
INSERT INTO table_name
(column1, column2, column3, ...)
VALUES
(value1, value2, value3, ...);
```

### Example

```sql
INSERT INTO employee
(emp_id, name, salary)
VALUES
(5, 'David', 5000.00);
```

Retrieve the data:

```sql
SELECT * FROM employee;
```

The remaining columns will contain their **default values** or **NULL** (if allowed).

---

# Inserting Multiple Rows into Specific Columns

You can also insert multiple records while specifying only selected columns.

### Example

```sql
INSERT INTO employee
(emp_id, name, salary)
VALUES
(6, 'Emma', 4200.00),
(7, 'Chris', 3900.50),
(8, 'Sophia', 6100.00);
```

---

# Important Rules

* The number of values must match the number of specified columns.
* Values should be provided in the same order as the listed columns.
* Strings and dates must be enclosed in single quotes (`' '`).
* Numeric values do not require quotes.
* If a column has a default value, you may omit it when specifying columns.
* Columns defined as `NOT NULL` must receive a value unless a default is defined.

---

# Verify Inserted Data

Display all records:

```sql
SELECT * FROM employee;
```

Display specific columns:

```sql
SELECT emp_id, name, salary
FROM employee;
```

---

# Common Errors

## Column Count Doesn't Match

**Error**

```text
ERROR 1136 (21S01): Column count doesn't match value count at row 1
```

**Cause**

The number of values does not match the number of columns.

**Solution**

Ensure every specified column has exactly one corresponding value.

---

## Unknown Column

**Error**

```text
ERROR 1054 (42S22): Unknown column
```

**Cause**

A column name is incorrect or does not exist.

**Solution**

Verify the table structure:

```sql
DESCRIBE employee;
```

---

## Duplicate Entry

**Error**

```text
ERROR 1062 (23000): Duplicate entry
```

**Cause**

A duplicate value is being inserted into a column with a `PRIMARY KEY` or `UNIQUE` constraint.

**Solution**

Insert a unique value or update the existing record instead.

---

## Cannot Be NULL

**Error**

```text
ERROR 1048 (23000): Column cannot be null
```

**Cause**

A required (`NOT NULL`) column was not given a value.

**Solution**

Provide a valid value for the column.

---

# Best Practices

* Specify column names whenever possible.
* Insert multiple rows in a single statement for better performance.
* Use meaningful and valid data.
* Verify inserted data using `SELECT`.
* Ensure data types match the column definitions.

---

# Command Summary

| Command                                                          | Description                                  |
| ---------------------------------------------------------------- | -------------------------------------------- |
| `INSERT INTO table_name VALUES (...);`                           | Inserts a single row into a table.           |
| `INSERT INTO table_name VALUES (...), (...);`                    | Inserts multiple rows in one statement.      |
| `INSERT INTO table_name (column1, column2) VALUES (...);`        | Inserts data into specific columns.          |
| `INSERT INTO table_name (column1, column2) VALUES (...), (...);` | Inserts multiple rows into selected columns. |
| `SELECT * FROM table_name;`                                      | Displays all records in the table.           |
| `SELECT column1, column2 FROM table_name;`                       | Displays selected columns from the table.    |
