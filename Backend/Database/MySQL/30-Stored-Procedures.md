# Lesson 30 — Stored Procedures

## Learning Objectives

By the end of this lesson, you will understand:

- What Stored Procedures are
- Why they are used
- Advantages and disadvantages
- How to create Stored Procedures
- How to execute Stored Procedures
- Parameters (`IN`, `OUT`, `INOUT`)
- Local variables
- Control flow (`IF`, `CASE`, `LOOP`, `WHILE`)
- Real-world examples
- Best practices
- Interview questions
- Practice exercises

---

# What is a Stored Procedure?

A **Stored Procedure** is a collection of one or more SQL statements that are **saved inside the MySQL database** and can be executed whenever needed.

Instead of writing the same SQL queries repeatedly, you write them once, store them in the database, and call them whenever required.

Think of it like a function in programming languages.

Example:

Instead of writing:

```sql
SELECT * FROM employees WHERE salary > 50000;
```

every day,

you create:

```sql
CALL GetHighSalaryEmployees();
```

The database executes the saved SQL automatically.

---

# Why Use Stored Procedures?

Imagine an e-commerce website.

Every time a customer places an order, the system needs to:

- Insert the order
- Update product stock
- Calculate total amount
- Generate invoice
- Save payment details
- Log the activity

Without Stored Procedures:

The application sends multiple SQL queries.

With Stored Procedures:

The application sends only:

```sql
CALL PlaceOrder(...);
```

The procedure handles everything.

---

# Benefits

- Reusable code
- Faster execution
- Better security
- Less network traffic
- Easier maintenance
- Centralized business logic

---

# How Stored Procedures Work

```
Application

        ↓

CALL Procedure()

        ↓

Stored Procedure

        ↓

SQL Statements

        ↓

Database
```

---

# Basic Syntax

```sql
DELIMITER //

CREATE PROCEDURE procedure_name()
BEGIN

    SQL Statements;

END //

DELIMITER ;
```

---

# Why DELIMITER?

Normally MySQL ends a statement at:

```sql
;
```

But procedures contain many semicolons.

Example:

```sql
BEGIN

SELECT * FROM employees;

SELECT COUNT(*) FROM employees;

END
```

MySQL would stop after the first semicolon.

So we temporarily change the delimiter.

Example:

```sql
DELIMITER //

...

END //

DELIMITER ;
```

---

# Creating Your First Procedure

Example:

```sql
DELIMITER //

CREATE PROCEDURE ShowEmployees()

BEGIN

SELECT * FROM employees;

END //

DELIMITER ;
```

Procedure created successfully.

---

# Calling a Procedure

Syntax

```sql
CALL procedure_name();
```

Example

```sql
CALL ShowEmployees();
```

Output

```
All employee records
```

---

# Example Database

Employees

| ID | Name | Salary |
|----|------|---------|
|1|Alice|45000|
|2|Bob|60000|
|3|John|75000|

Procedure

```sql
CALL ShowEmployees();
```

Returns every employee.

---

# Procedure with IN Parameter

An **IN parameter** receives a value from the caller.

Example

```sql
DELIMITER //

CREATE PROCEDURE EmployeeById(

IN empId INT

)

BEGIN

SELECT *

FROM employees

WHERE id = empId;

END //

DELIMITER ;
```

Execute

```sql
CALL EmployeeById(2);
```

Output

```
Bob
```

---

# Multiple IN Parameters

```sql
DELIMITER //

CREATE PROCEDURE EmployeesAboveSalary(

IN amount DECIMAL(10,2)

)

BEGIN

SELECT *

FROM employees

WHERE salary > amount;

END //

DELIMITER ;
```

Call

```sql
CALL EmployeesAboveSalary(50000);
```

Output

```
Bob

John
```

---

# OUT Parameter

OUT parameters return values.

Example

```sql
DELIMITER //

CREATE PROCEDURE EmployeeCount(

OUT total INT

)

BEGIN

SELECT COUNT(*)

INTO total

FROM employees;

END //

DELIMITER ;
```

Execute

```sql
CALL EmployeeCount(@count);

SELECT @count;
```

Output

```
3
```

---

# INOUT Parameter

INOUT works as both input and output.

Example

```sql
DELIMITER //

CREATE PROCEDURE DoubleValue(

INOUT number INT

)

BEGIN

SET number = number * 2;

END //

DELIMITER ;
```

Execute

```sql
SET @num = 10;

CALL DoubleValue(@num);

SELECT @num;
```

Output

```
20
```

---

# Parameter Types Summary

| Type | Purpose |
|-------|----------|
| IN | Input only |
| OUT | Output only |
| INOUT | Input + Output |

---

# Local Variables

Variables exist only inside the procedure.

Example

```sql
DECLARE total INT;
```

Complete Example

```sql
DELIMITER //

CREATE PROCEDURE Example()

BEGIN

DECLARE total INT;

SET total = 50;

SELECT total;

END //

DELIMITER ;
```

Output

```
50
```

---

# Using SELECT INTO

Example

```sql
DECLARE employeeSalary DECIMAL(10,2);

SELECT salary

INTO employeeSalary

FROM employees

WHERE id = 1;
```

The variable now stores the salary.

---

# IF Statement

Example

```sql
IF salary > 50000 THEN

SELECT 'High Salary';

ELSE

SELECT 'Average Salary';

END IF;
```

---

# CASE Statement

```sql
CASE

WHEN salary > 70000

THEN

SELECT 'Excellent';

WHEN salary > 50000

THEN

SELECT 'Good';

ELSE

SELECT 'Average';

END CASE;
```

---

# WHILE Loop

Example

```sql
DECLARE i INT DEFAULT 1;

WHILE i <= 5 DO

SELECT i;

SET i = i + 1;

END WHILE;
```

---

# REPEAT Loop

```sql
REPEAT

SET i = i + 1;

UNTIL i = 10

END REPEAT;
```

---

# LOOP Statement

```sql
myLoop:

LOOP

SET i = i + 1;

IF i = 10 THEN

LEAVE myLoop;

END IF;

END LOOP;
```

---

# Procedure to Insert Employee

```sql
DELIMITER //

CREATE PROCEDURE AddEmployee(

IN empName VARCHAR(50),

IN empSalary DECIMAL(10,2)

)

BEGIN

INSERT INTO employees(

name,

salary

)

VALUES(

empName,

empSalary

);

END //

DELIMITER ;
```

Execute

```sql
CALL AddEmployee(

'David',

70000

);
```

Employee inserted.

---

# Procedure to Increase Salary

```sql
DELIMITER //

CREATE PROCEDURE IncreaseSalary(

IN percent DECIMAL(5,2)

)

BEGIN

UPDATE employees

SET salary = salary + (salary * percent / 100);

END //

DELIMITER ;
```

Call

```sql
CALL IncreaseSalary(10);
```

Everyone receives a 10% raise.

---

# Procedure to Delete Employee

```sql
DELIMITER //

CREATE PROCEDURE DeleteEmployee(

IN empId INT

)

BEGIN

DELETE

FROM employees

WHERE id = empId;

END //

DELIMITER ;
```

Execute

```sql
CALL DeleteEmployee(3);
```

---

# Viewing Procedures

```sql
SHOW PROCEDURE STATUS;
```

---

# Show Procedure Definition

```sql
SHOW CREATE PROCEDURE ShowEmployees;
```

---

# Deleting a Procedure

```sql
DROP PROCEDURE ShowEmployees;
```

Safe version

```sql
DROP PROCEDURE IF EXISTS ShowEmployees;
```

---

# Real-World Example

Bank Application

Procedure:

```text
TransferMoney()

```

Tasks:

- Check sender balance
- Deduct amount
- Add amount to receiver
- Save transaction
- Write logs
- Commit transaction

Application simply executes:

```sql
CALL TransferMoney(...);
```

---

# Another Example

Online Shopping

Procedure:

```
PlaceOrder()
```

Steps:

- Insert order
- Reduce inventory
- Save payment
- Generate invoice
- Send notification

All inside one procedure.

---

# Advantages

- Reusable
- Fast execution
- Reduced network traffic
- Better security
- Easier maintenance
- Centralized business rules

---

# Disadvantages

- Harder to debug
- Database-specific syntax
- Can become difficult to maintain if too large
- Version control is harder than application code

---

# Best Practices

- Use meaningful names
- Keep procedures focused on one task
- Use parameters instead of hardcoded values
- Handle errors where appropriate
- Avoid unnecessary complexity
- Document business logic
- Use transactions for critical operations

---

# Common Mistakes

❌ Forgetting `DELIMITER`

❌ Forgetting `CALL`

❌ Using wrong parameter type

❌ Not resetting delimiter

❌ Creating one huge procedure for everything

---

# Interview Questions

## 1. What is a Stored Procedure?

A stored collection of SQL statements saved in the database that can be executed repeatedly.

---

## 2. Why are Stored Procedures faster?

They are precompiled/optimized by the database and reduce repeated parsing and network traffic.

---

## 3. Difference between Procedure and Function?

| Procedure | Function |
|------------|----------|
| Called using `CALL` | Called inside SQL expressions |
| May return multiple values using `OUT` parameters | Must return a single value |
| Can modify database data | Often used to compute and return a value (subject to MySQL rules) |

---

## 4. What are `IN`, `OUT`, and `INOUT` parameters?

- **IN** → Receives input
- **OUT** → Returns output
- **INOUT** → Receives input and returns a modified value

---

## 5. Why do we use `DELIMITER`?

To temporarily change the statement terminator so MySQL can correctly parse the entire procedure definition.

---

# Practice Exercises

### Exercise 1

Create a procedure that displays all products.

---

### Exercise 2

Create a procedure that accepts a department ID and displays employees in that department.

---

### Exercise 3

Create a procedure that returns the total number of employees using an `OUT` parameter.

---

### Exercise 4

Create a procedure that increases all employee salaries by a given percentage.

---

### Exercise 5

Create a procedure that inserts a new student into a `students` table.

---

# Mini Project

Create a **Library Management System** with these procedures:

- `AddBook()`
- `BorrowBook()`
- `ReturnBook()`
- `DeleteBook()`
- `AvailableBooks()`
- `BookCount()`

Use `IN`, `OUT`, and `INOUT` parameters where appropriate.

---

# Summary

In this lesson, you learned:

- What Stored Procedures are
- Why they are useful
- Creating and calling procedures
- Using `IN`, `OUT`, and `INOUT` parameters
- Declaring local variables
- Control flow with `IF`, `CASE`, `WHILE`, `REPEAT`, and `LOOP`
- Viewing and dropping procedures
- Real-world applications
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 31 — Triggers**

Topics covered:

- What are Triggers?
- BEFORE and AFTER triggers
- INSERT, UPDATE, DELETE triggers
- OLD and NEW keywords
- Audit logging
- Business rules
- Real-world examples
- Best practices