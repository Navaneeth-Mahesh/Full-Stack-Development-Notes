# Lesson 31 — Triggers in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What triggers are
- Why triggers are used
- BEFORE vs AFTER triggers
- INSERT, UPDATE, DELETE triggers
- OLD and NEW keywords
- Audit logging
- Enforcing business rules
- Real-world examples
- Best practices
- Interview questions
- Practice exercises

---

# What is a Trigger?

A **Trigger** is a special SQL object that automatically executes when a specific event occurs on a table.

You don't call a trigger manually.

It runs automatically whenever an event happens.

Think of it like a motion sensor.

```
Someone enters room
        ↓
Sensor detects movement
        ↓
Lights turn ON automatically
```

Similarly,

```
INSERT happens
        ↓
Trigger executes automatically
```

---

# Why Use Triggers?

Triggers help automate tasks.

Examples:

- Save audit logs
- Prevent invalid data
- Automatically update another table
- Maintain history
- Track salary changes
- Update stock after an order
- Record deleted records

Without triggers:

```
Application
      ↓
Insert data
      ↓
Insert audit log
```

With triggers:

```
Application
      ↓
Insert data
      ↓
Trigger automatically inserts audit log
```

---

# Trigger Events

A trigger executes on three database events:

| Event | Description |
|--------|-------------|
| INSERT | New row added |
| UPDATE | Existing row modified |
| DELETE | Row removed |

---

# Trigger Timing

A trigger can run:

| Timing | Runs |
|----------|--------------------|
| BEFORE | Before the operation |
| AFTER | After the operation |

Examples:

```
BEFORE INSERT

AFTER INSERT

BEFORE UPDATE

AFTER UPDATE

BEFORE DELETE

AFTER DELETE
```

---

# Trigger Syntax

```sql
CREATE TRIGGER trigger_name
BEFORE INSERT
ON employees
FOR EACH ROW

BEGIN

    -- SQL Statements

END;
```

Explanation:

```
CREATE TRIGGER
```

Creates a new trigger.

```
BEFORE INSERT
```

When to execute.

```
ON employees
```

Which table.

```
FOR EACH ROW
```

Runs once for every affected row.

---

# Sample Table

```sql
CREATE TABLE employees
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(50),

    salary DECIMAL(10,2)
);
```

---

# BEFORE INSERT Trigger

Suppose salary must never be negative.

```
Wrong

Salary = -5000
```

Trigger:

```sql
DELIMITER //

CREATE TRIGGER check_salary

BEFORE INSERT

ON employees

FOR EACH ROW

BEGIN

    IF NEW.salary < 0 THEN
        SET NEW.salary = 0;
    END IF;

END//

DELIMITER ;
```

Insert:

```sql
INSERT INTO employees(name,salary)

VALUES('John',-5000);
```

Stored value:

```
John

0
```

The trigger corrected the value before insertion.

---

# AFTER INSERT Trigger

Suppose every new employee should be recorded in an audit table.

Audit table:

```sql
CREATE TABLE employee_logs
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    employee_name VARCHAR(50),

    action VARCHAR(100)
);
```

Trigger:

```sql
DELIMITER //

CREATE TRIGGER employee_insert_log

AFTER INSERT

ON employees

FOR EACH ROW

BEGIN

INSERT INTO employee_logs(employee_name,action)

VALUES

(NEW.name,'Employee Added');

END//

DELIMITER ;
```

Insert:

```sql
INSERT INTO employees(name,salary)

VALUES('Alice',50000);
```

Automatically:

```
employee_logs

Alice

Employee Added
```

---

# BEFORE UPDATE Trigger

Suppose salary should never become negative.

```sql
DELIMITER //

CREATE TRIGGER validate_update

BEFORE UPDATE

ON employees

FOR EACH ROW

BEGIN

IF NEW.salary < 0 THEN

SET NEW.salary = OLD.salary;

END IF;

END//

DELIMITER ;
```

Update:

```sql
UPDATE employees

SET salary=-100

WHERE id=1;
```

Instead of storing -100,

it keeps the previous salary.

---

# AFTER UPDATE Trigger

Audit every salary change.

Audit table:

```sql
CREATE TABLE salary_history
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    employee_id INT,

    old_salary DECIMAL(10,2),

    new_salary DECIMAL(10,2)
);
```

Trigger:

```sql
DELIMITER //

CREATE TRIGGER salary_audit

AFTER UPDATE

ON employees

FOR EACH ROW

BEGIN

INSERT INTO salary_history

(employee_id,old_salary,new_salary)

VALUES

(OLD.id,OLD.salary,NEW.salary);

END//

DELIMITER ;
```

Whenever salary changes,

history is recorded automatically.

---

# BEFORE DELETE Trigger

Suppose managers cannot be deleted.

Table:

```sql
employees

role
```

Trigger:

```sql
DELIMITER //

CREATE TRIGGER prevent_manager_delete

BEFORE DELETE

ON employees

FOR EACH ROW

BEGIN

IF OLD.role='Manager' THEN

SIGNAL SQLSTATE '45000'

SET MESSAGE_TEXT='Managers cannot be deleted';

END IF;

END//

DELIMITER ;
```

Now deleting a manager raises an error.

---

# AFTER DELETE Trigger

Archive deleted employees.

Archive table:

```sql
deleted_employees
```

Trigger:

```sql
DELIMITER //

CREATE TRIGGER archive_employee

AFTER DELETE

ON employees

FOR EACH ROW

BEGIN

INSERT INTO deleted_employees

(name,salary)

VALUES

(OLD.name,OLD.salary);

END//

DELIMITER ;
```

Deleted records are safely stored.

---

# OLD and NEW Keywords

Triggers can access row values.

## NEW

Represents the new row.

Example:

```sql
NEW.salary
```

New salary after update.

---

## OLD

Represents the previous row.

Example:

```sql
OLD.salary
```

Previous salary.

---

Example:

Salary changed

```
Old Salary

50000

↓

New Salary

65000
```

Trigger sees:

```
OLD.salary = 50000

NEW.salary = 65000
```

---

# OLD vs NEW Availability

| Trigger Type | OLD | NEW |
|--------------|-----|-----|
| INSERT | ❌ | ✅ |
| UPDATE | ✅ | ✅ |
| DELETE | ✅ | ❌ |

Reason:

INSERT has no old row.

DELETE has no new row.

UPDATE has both.

---

# Audit Logging Example

Employee changes email.

Without trigger:

No history.

With trigger:

```
Old Email

john@gmail.com

↓

New Email

john@company.com

↓

Audit Table

Old

New

Date

User
```

Every change is permanently stored.

---

# Business Rules

Triggers enforce company policies.

Examples:

```
Salary cannot be negative

Age must be above 18

Stock cannot go below zero

Managers cannot be deleted

Discount cannot exceed 50%
```

---

# Real-World Example

### Banking

```
Money transferred

↓

Trigger

↓

Create transaction history

↓

Update account balance

↓

Record audit log
```

---

### E-commerce

```
Order placed

↓

Trigger

↓

Reduce stock

↓

Create invoice

↓

Update sales report
```

---

### Hospital

```
Patient discharged

↓

Trigger

↓

Generate bill

↓

Archive patient

↓

Update room availability
```

---

# Viewing Triggers

```sql
SHOW TRIGGERS;
```

Output:

```
employee_insert_log

salary_audit

archive_employee
```

---

# Deleting a Trigger

Syntax:

```sql
DROP TRIGGER trigger_name;
```

Example:

```sql
DROP TRIGGER salary_audit;
```

---

# Advantages

- Automatic execution
- Keeps data consistent
- Enforces rules
- Tracks history
- Reduces application code
- Improves data integrity

---

# Disadvantages

- Harder to debug
- Can reduce performance if overused
- Hidden logic may confuse developers
- Complex trigger chains become difficult to maintain

---

# Best Practices

- Keep triggers small and simple.
- Avoid heavy computations inside triggers.
- Use meaningful trigger names.
- Document why each trigger exists.
- Prefer application logic for complex workflows.
- Avoid recursive trigger behavior.
- Test triggers thoroughly before production.

---

# Common Mistakes

### Forgetting `FOR EACH ROW`

```sql
CREATE TRIGGER test
AFTER INSERT
ON employees;
```

Incorrect.

Always include:

```sql
FOR EACH ROW
```

---

### Using `OLD` in INSERT

```sql
OLD.salary
```

Incorrect.

INSERT only has `NEW`.

---

### Using `NEW` in DELETE

```sql
NEW.salary
```

Incorrect.

DELETE only has `OLD`.

---

### Missing DELIMITER

When writing multi-statement triggers, forgetting to change the delimiter causes syntax errors.

Correct:

```sql
DELIMITER //

CREATE TRIGGER ...

BEGIN
    ...
END//

DELIMITER ;
```

---

# Interview Questions

## 1. What is a trigger?

A trigger is a database object that automatically executes when an INSERT, UPDATE, or DELETE event occurs on a table.

---

## 2. Difference between BEFORE and AFTER triggers?

- **BEFORE** triggers run before the data modification.
- **AFTER** triggers run after the modification is completed.

---

## 3. What is `FOR EACH ROW`?

It tells MySQL to execute the trigger once for every affected row.

---

## 4. What are `OLD` and `NEW`?

- `OLD` refers to the existing row values.
- `NEW` refers to the new row values.

---

## 5. Can `OLD` be used in an INSERT trigger?

No. INSERT has no existing row.

---

## 6. Can `NEW` be used in a DELETE trigger?

No. DELETE removes the row, so only `OLD` is available.

---

## 7. How do you view all triggers?

```sql
SHOW TRIGGERS;
```

---

## 8. How do you delete a trigger?

```sql
DROP TRIGGER trigger_name;
```

---

# Practice Exercises

## Exercise 1

Create an `AFTER INSERT` trigger that records every new employee in an audit table.

---

## Exercise 2

Create a `BEFORE INSERT` trigger that changes negative salaries to `0`.

---

## Exercise 3

Create an `AFTER UPDATE` trigger that stores salary changes in a history table.

---

## Exercise 4

Create an `AFTER DELETE` trigger that archives deleted employee records.

---

## Exercise 5

Display all triggers in the current database.

---

## Mini Project

Create an **Employee Management System** with:

### Tables

- employees
- employee_logs
- salary_history
- deleted_employees

### Triggers

- BEFORE INSERT → Prevent negative salaries
- AFTER INSERT → Log employee creation
- AFTER UPDATE → Record salary changes
- AFTER DELETE → Archive deleted employees

Test each trigger by performing INSERT, UPDATE, and DELETE operations.

---

# Summary

In this lesson, you learned:

- What triggers are
- BEFORE and AFTER triggers
- INSERT, UPDATE, and DELETE triggers
- `OLD` and `NEW` keywords
- Audit logging
- Business rule enforcement
- Real-world use cases
- Viewing and deleting triggers
- Advantages and disadvantages
- Best practices
- Common mistakes
- Practice exercises
