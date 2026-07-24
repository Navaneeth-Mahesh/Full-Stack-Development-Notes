# Modifying Table Columns in MySQL

After creating a table, you may need to make changes to its structure. MySQL provides several `ALTER TABLE` commands that allow you to:

* Add new columns
* Rename existing columns
* Modify a column's data type or size
* Change the position of a column
* Delete unwanted columns

All of these operations are performed using the **`ALTER TABLE`** statement.

---

# ALTER TABLE Syntax

```sql
ALTER TABLE table_name
operation;
```

Replace `table_name` with the name of the table you want to modify.

---

# Adding a New Column

Use the `ADD COLUMN` clause to add a new column to an existing table.

## Syntax

```sql
ALTER TABLE table_name
ADD COLUMN column_name DATA_TYPE;
```

### Example

```sql
ALTER TABLE employee
ADD COLUMN email VARCHAR(100);
```

This adds a new column named `email` that can store up to 100 characters.

---

## Verify the Changes

```sql
DESCRIBE employee;
```

Output:

```text
+-------------+--------------+
| Field       | Type         |
+-------------+--------------+
| emp_id      | int          |
| first_name  | varchar(50)  |
| last_name   | varchar(50)  |
| hourly_pay  | decimal(5,2) |
| hire_date   | date         |
| email       | varchar(100) |
+-------------+--------------+
```

---

# Add Multiple Columns

You can add more than one column in a single statement.

```sql
ALTER TABLE employee
ADD COLUMN phone VARCHAR(15),
ADD COLUMN department VARCHAR(50);
```

---

# Renaming a Column

If you want to change the name of a column without changing its purpose, use the `RENAME COLUMN` statement.

## Syntax (MySQL 8.0+)

```sql
ALTER TABLE table_name
RENAME COLUMN old_column_name TO new_column_name;
```

### Example

```sql
ALTER TABLE employee
RENAME COLUMN hourly_pay TO salary_per_hour;
```

Now the column name becomes:

```text
salary_per_hour
```

---

# Modifying a Column

Use the `MODIFY COLUMN` clause when you want to change:

* Data type
* Column size
* Precision
* Nullability

**The column name remains the same.**

## Syntax

```sql
ALTER TABLE table_name
MODIFY COLUMN column_name NEW_DATA_TYPE;
```

### Example 1: Increase the Length

```sql
ALTER TABLE employee
MODIFY COLUMN first_name VARCHAR(100);
```

The maximum length of `first_name` is now 100 characters instead of 50.

---

### Example 2: Change Data Type

```sql
ALTER TABLE employee
MODIFY COLUMN salary_per_hour DECIMAL(8,2);
```

The column can now store larger salary values.

---

# Changing the Position of a Column

By default, MySQL adds new columns at the end of the table.

You can change the position of a column using `FIRST` or `AFTER`.

---

## Place a Column at the Beginning

### Syntax

```sql
ALTER TABLE table_name
MODIFY COLUMN column_name DATA_TYPE FIRST;
```

### Example

```sql
ALTER TABLE employee
MODIFY COLUMN email VARCHAR(100) FIRST;
```

The `email` column now becomes the first column in the table.

---

## Place a Column After Another Column

### Syntax

```sql
ALTER TABLE table_name
MODIFY COLUMN column_name DATA_TYPE
AFTER existing_column;
```

### Example

```sql
ALTER TABLE employee
MODIFY COLUMN email VARCHAR(100)
AFTER last_name;
```

New order:

```text
emp_id
first_name
last_name
email
salary_per_hour
hire_date
```

---

# Dropping (Deleting) a Column

If a column is no longer needed, it can be permanently removed.

## Syntax

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

### Example

```sql
ALTER TABLE employee
DROP COLUMN email;
```

The `email` column is permanently deleted.

---

## Verify

```sql
DESCRIBE employee;
```

The `email` column will no longer appear.

---

# Complete Example

Suppose the table initially looks like this:

```text
employee
-----------------------------
emp_id
first_name
last_name
hourly_pay
hire_date
```

### Step 1: Add Email

```sql
ALTER TABLE employee
ADD COLUMN email VARCHAR(100);
```

Result:

```text
emp_id
first_name
last_name
hourly_pay
hire_date
email
```

---

### Step 2: Rename Salary Column

```sql
ALTER TABLE employee
RENAME COLUMN hourly_pay TO salary_per_hour;
```

Result:

```text
emp_id
first_name
last_name
salary_per_hour
hire_date
email
```

---

### Step 3: Increase Name Length

```sql
ALTER TABLE employee
MODIFY COLUMN first_name VARCHAR(100);
```

---

### Step 4: Move Email After Last Name

```sql
ALTER TABLE employee
MODIFY COLUMN email VARCHAR(100)
AFTER last_name;
```

Result:

```text
emp_id
first_name
last_name
email
salary_per_hour
hire_date
```

---

### Step 5: Remove Email

```sql
ALTER TABLE employee
DROP COLUMN email;
```

Final table:

```text
emp_id
first_name
last_name
salary_per_hour
hire_date
```

---

# Common Errors

## Unknown Column

```text
ERROR 1054 (42S22): Unknown column
```

**Cause:** The specified column does not exist.

**Solution:** Check the column names using:

```sql
DESCRIBE table_name;
```

---

## Duplicate Column Name

```text
ERROR 1060 (42S21): Duplicate column name
```

**Cause:** A column with the same name already exists.

**Solution:** Choose a different name or remove the existing column.

---

## Data Too Long

```text
ERROR 1406 (22001): Data too long for column
```

**Cause:** Existing data exceeds the new column size.

**Solution:** Increase the column size or clean the data before modifying the column.

---

# Summary

| Command                                                                             | Purpose                                       |
| ----------------------------------------------------------------------------------- | --------------------------------------------- |
| `ALTER TABLE table_name ADD COLUMN column_name DATA_TYPE;`                          | Adds a new column.                            |
| `ALTER TABLE table_name RENAME COLUMN old_name TO new_name;`                        | Renames a column.                             |
| `ALTER TABLE table_name MODIFY COLUMN column_name DATA_TYPE;`                       | Changes the data type or size of a column.    |
| `ALTER TABLE table_name MODIFY COLUMN column_name DATA_TYPE FIRST;`                 | Moves a column to the beginning of the table. |
| `ALTER TABLE table_name MODIFY COLUMN column_name DATA_TYPE AFTER existing_column;` | Moves a column after another column.          |
| `ALTER TABLE table_name DROP COLUMN column_name;`                                   | Permanently deletes a column.                 |

---

