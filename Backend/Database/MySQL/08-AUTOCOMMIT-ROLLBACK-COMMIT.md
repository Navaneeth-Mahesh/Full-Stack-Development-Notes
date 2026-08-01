# Lesson 7 — AUTOCOMMIT, COMMIT & ROLLBACK

## Learning Objectives

By the end of this lesson, you will understand:

- What is a transaction?
- What is AUTOCOMMIT?
- What is COMMIT?
- What is ROLLBACK?
- How transactions work
- ACID properties
- Transaction examples
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# What is a Transaction?

A **transaction** is a group of one or more SQL statements that are treated as a single unit of work.

A transaction ensures that either:

- **All operations succeed**, or
- **None of them are applied**

This prevents your database from ending up in an inconsistent state.

Example:

Transferring ₹500 from Account A to Account B.

Step 1:

```text
A = 5000
B = 3000
```

Transaction:

```text
Subtract ₹500 from A

Add ₹500 to B
```

After completion:

```text
A = 4500

B = 3500
```

If the second step fails, the first step must also be undone.

That's exactly why transactions exist.

---

# Real-Life Analogy

Imagine withdrawing money from an ATM.

The ATM should:

1. Deduct money from your account.
2. Dispense cash.

If cash isn't dispensed, your balance should **not** be deducted.

This is achieved using a transaction.

---

# What is AUTOCOMMIT?

By default, MySQL runs in **AUTOCOMMIT mode**.

This means:

Every SQL statement is automatically saved as soon as it executes.

Example:

```sql
UPDATE students
SET marks = 95
WHERE id = 1;
```

Immediately after execution:

- Changes are permanently saved.
- You cannot undo them using `ROLLBACK`.

---

# Check AUTOCOMMIT Status

```sql
SELECT @@autocommit;
```

Output:

```text
+--------------+
| @@autocommit |
+--------------+
| 1            |
+--------------+
```

`1` means AUTOCOMMIT is enabled.

`0` means AUTOCOMMIT is disabled.

---

# Disable AUTOCOMMIT

```sql
SET autocommit = 0;
```

Now MySQL will not automatically save changes.

You control when changes are saved.

Verify:

```sql
SELECT @@autocommit;
```

Output:

```text
0
```

---

# Example Table

```sql
CREATE TABLE accounts (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10,2)
);
```

Insert data:

```sql
INSERT INTO accounts VALUES
(1,'Navaneeth',5000),
(2,'Rahul',3000);
```

Current table:

| id | name | balance |
|----|------|---------|
|1|Navaneeth|5000|
|2|Rahul|3000|

---

# COMMIT

`COMMIT` permanently saves all changes made during the current transaction.

Example:

```sql
SET autocommit = 0;

UPDATE accounts
SET balance = 4500
WHERE id = 1;

COMMIT;
```

Now the balance is permanently stored.

Even if MySQL restarts, the data remains.

---

# ROLLBACK

`ROLLBACK` cancels all uncommitted changes.

Example:

```sql
SET autocommit = 0;

UPDATE accounts
SET balance = 2000
WHERE id = 1;

ROLLBACK;
```

The balance returns to its previous value.

Nothing is saved.

---

# COMMIT vs ROLLBACK

Example:

```sql
SET autocommit = 0;

UPDATE accounts
SET balance = balance - 500
WHERE id = 1;

UPDATE accounts
SET balance = balance + 500
WHERE id = 2;
```

If everything is successful:

```sql
COMMIT;
```

Result:

| id | balance |
|----|----------|
|1|4500|
|2|3500|

---

If something goes wrong:

```sql
ROLLBACK;
```

Result:

| id | balance |
|----|----------|
|1|5000|
|2|3000|

Everything returns to its original state.

---

# Manual Transactions

Instead of disabling AUTOCOMMIT globally, you can use:

```sql
START TRANSACTION;
```

Example:

```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 1000
WHERE id = 1;

UPDATE accounts
SET balance = balance + 1000
WHERE id = 2;

COMMIT;
```

If an error occurs:

```sql
ROLLBACK;
```

This method is preferred in real applications.

---

# Another Example

Original table:

| Product | Stock |
|----------|-------|
|Laptop|10|

Customer buys one laptop.

```sql
START TRANSACTION;

UPDATE products
SET stock = stock - 1
WHERE product='Laptop';

COMMIT;
```

Stock becomes:

```text
9
```

If payment fails:

```sql
ROLLBACK;
```

Stock remains:

```text
10
```

---

# ACID Properties

Transactions follow **ACID** principles.

## A — Atomicity

Either all operations happen or none happen.

Example:

Money transfer.

Both debit and credit must succeed.

---

## C — Consistency

Database remains valid before and after the transaction.

Example:

A bank balance should never become inconsistent because of a failed transaction.

---

## I — Isolation

Multiple transactions should not interfere with each other.

Example:

Two customers booking the same movie seat simultaneously.

Isolation prevents conflicts.

---

## D — Durability

Once committed, changes are permanent.

Even after a system crash, committed data is preserved.

---

# Common Workflow

```sql
START TRANSACTION;

UPDATE ...

INSERT ...

DELETE ...

COMMIT;
```

Or if something fails:

```sql
START TRANSACTION;

UPDATE ...

DELETE ...

ROLLBACK;
```

---

# Common Mistakes

## Mistake 1

Forgetting `COMMIT`.

```sql
UPDATE students
SET marks = 90;
```

Then closing the connection.

Result:

Changes are lost if they were never committed.

---

## Mistake 2

Using `ROLLBACK` after `COMMIT`.

Example:

```sql
COMMIT;

ROLLBACK;
```

Nothing happens because the changes are already permanent.

---

## Mistake 3

Expecting `ROLLBACK` to undo changes while AUTOCOMMIT is enabled.

Example:

```sql
UPDATE students
SET marks = 80;

ROLLBACK;
```

Nothing changes because the update was already committed automatically.

---

# Best Practices

- Use transactions for operations involving multiple SQL statements.
- Prefer `START TRANSACTION` over disabling AUTOCOMMIT globally.
- Always `COMMIT` after successful operations.
- Always `ROLLBACK` if an error occurs.
- Keep transactions as short as possible to avoid locking resources.

---

# Interview Questions

## 1. What is a transaction?

A transaction is a group of SQL statements executed as a single unit of work.

---

## 2. What is AUTOCOMMIT?

A mode where every SQL statement is automatically committed.

---

## 3. What does COMMIT do?

It permanently saves all changes made in the current transaction.

---

## 4. What does ROLLBACK do?

It undoes all uncommitted changes in the current transaction.

---

## 5. Can ROLLBACK undo committed changes?

No.

Once `COMMIT` is executed, the changes are permanent.

---

## 6. What are ACID properties?

- Atomicity
- Consistency
- Isolation
- Durability

---

## 7. Which is preferred in real projects?

Using:

```sql
START TRANSACTION;
```

instead of disabling AUTOCOMMIT globally.

---

# Practice Exercises

## Exercise 1

Create an `accounts` table.

---

## Exercise 2

Insert two users with different balances.

---

## Exercise 3

Start a transaction.

Subtract ₹1000 from Account 1.

Add ₹1000 to Account 2.

Commit the transaction.

---

## Exercise 4

Repeat the transaction, but use `ROLLBACK` instead of `COMMIT`.

Observe that the balances remain unchanged.

---

## Exercise 5

Check the AUTOCOMMIT status.

```sql
SELECT @@autocommit;
```

---

## Exercise 6

Disable AUTOCOMMIT.

```sql
SET autocommit = 0;
```

Update a row, then use `ROLLBACK`.

Verify that the original data is restored.

---

# Mini Project

Create a simple banking system:

```text
accounts
```

Columns:

- id
- customer_name
- balance

Tasks:

1. Insert three customers.
2. Transfer ₹500 from one customer to another using a transaction.
3. Commit the transaction.
4. Try another transfer and use `ROLLBACK`.
5. Compare the results after `COMMIT` and `ROLLBACK`.

---

# Summary

In this lesson, you learned:

- What a transaction is
- AUTOCOMMIT
- COMMIT
- ROLLBACK
- START TRANSACTION
- ACID properties
- Transaction workflows
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 9 — CURRENT_DATE() & CURRENT_TIME()**

Topics covered:

- Date and Time functions
- NOW()
- CURRENT_DATE()
- CURRENT_TIME()
- CURDATE()
- CURTIME()
- Practical examples
- Formatting dates
- Real-world use cases